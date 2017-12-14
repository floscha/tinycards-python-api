import os
from uuid import uuid4

import requests

from networking import json_converter


API_URL = 'https://tinycards.duolingo.com/api/1/'

DEFAULT_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://tinycards.duolingo.com/',
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4)' +
                   ' AppleWebKit/537.36 (KHTML, like Gecko)' +
                   ' Chrome/58.0.3029.94 Safari/537.36')
}


class RestApi(object):
    """Repository-like fascade for the Tinycards API.

    Abstracts away all queries to the original Tinycards API and handles all
    JSON (un-)marshalling.
    """

    def __init__(self):
        """Initialize a new instance of the RestApi class."""
        self.session = requests.session()

    def login(self,
              identifier=None,
              password=None):
        """Log in an user with its Tinycards or Duolingo credentials.

        Args:
            identifier (str): The Tinycards identifier to use for logging in.
                For example, a user's email address.
                Will be taken from ENV if not specified:
                .. envvar:: TINYCARDS_IDENTIFIER
            password (str): The user's password to login to Tinycards.
                Will be taken from ENV if not specified.
                .. envvar:: TINYCARDS_PASSWORD
        """
        # Take credetioals from ENV if not specified.
        identifier = identifier or os.environ.get('TINYCARDS_IDENTIFIER')
        password = password or os.environ.get('TINYCARDS_PASSWORD')

        request_payload = {
            'identifier': identifier,
            'password': password
        }
        r = self.session.post(url=API_URL + 'login',
                              json=request_payload)
        json_response = r.json()

        user_id = json_response['id']
        print("Logged in as '%s' (%s)"
              % (json_response['fullname'], json_response['email']))

        return user_id

    # --- Read user info.

    def get_user_info(self, user_id):
        """Get info data about the given user."""
        request_url = API_URL + 'users/' + str(user_id)
        r = self.session.get(url=request_url)

        if r.status_code != 200:
            raise ValueError(r.text)

        json_response = r.json()
        user_info = json_converter.json_to_user(json_response)

        return user_info

    # --- Deck CRUD

    def get_decks(self, user_id):
        """Get all Decks for the currently logged in user.

        Returns:
            list: The list of retrieved decks.

        """
        request_url = API_URL + 'decks?userId=' + str(user_id)
        r = self.session.get(url=request_url)

        if r.status_code != 200:
            raise ValueError(r.text)

        json_response = r.json()
        decks = []
        for d in json_response['decks']:
            current_deck = json_converter.json_to_deck(d)
            decks.append(current_deck)

        return decks

    def get_deck(self, deck_id, user_id, include_cards=True):
        """Get the Deck with the given ID.

        Args:
            deck_id (str): The ID of the deck to retrieve.
            include_cards (bool): Only include the cards of the deck when set
                to True (as by default). Otherwise cards will be an empty list.

        Returns:
            Deck: The retrieved deck.

        """
        request_url = API_URL + 'decks/' + deck_id
        if include_cards:
            request_url += '?expand=true'
        r = self.session.get(url=request_url)
        json_response = r.json()

        deck = json_converter.json_to_deck(json_response)
        # Set additional properties.
        deck.id = deck_id
        deck.user_id = user_id

        return deck

    @staticmethod
    def _generate_form_boundary():
        """Generate a 16 digit boundary like the one used by Tinycards."""
        boundary = str(uuid4()).replace('-', '')[:16]
        return boundary

    @staticmethod
    def _to_multipart_form(data, boundary):
        """Create a multipart form like produced by HTML forms from a dict."""
        form_lines = []
        for k, v in data.items():
            form_lines.append('--' + boundary)
            # Handle special case for imageFile.
            if k == 'imageFile':
                form_lines.append('Content-Disposition: form-data; ' +
                                  'name="%s"; filename="cover.jpg"' % k)
                form_lines.append('Content-Type: image/jpeg')
                form_lines.append('')
                form_lines.append('')
            else:
                form_lines.append('Content-Disposition: form-data; name="%s"'
                                  % k)
                form_lines.append('')
                # Lowercase bool values to follow JSON standards.
                form_lines.append(str(v) if type(v) is not bool
                                  else str(v).lower())
        form_lines.append('--' + boundary + '--')

        joined_form = '\n'.join(form_lines)
        return joined_form

    def create_deck(self, deck):
        """Create a new Deck for the currently logged in user.

        Args:
            deck (Deck): The Deck object to create.

        Returns:
            Deck: The created Deck object if creation was successful.

        """
        form_boundary = self._generate_form_boundary()

        # Clone headers to not modify the global variable.
        headers = dict(DEFAULT_HEADERS)
        # Explicitly set Content-Type to multipart/form-data.
        headers['Content-Type'] = ('multipart/form-data; boundary=%s'
                                   % form_boundary)

        request_payload = json_converter.deck_to_json(deck)
        request_payload = self._to_multipart_form(request_payload,
                                                  form_boundary)
        r = self.session.post(url=API_URL + 'decks',
                              headers=headers,
                              data=request_payload)

        json_data = r.json()
        created_deck = json_converter.json_to_deck(json_data)

        return created_deck

    def update_deck(self, deck):
        """Update an existing deck.

        Args:
            deck (Deck): The Deck object to update.

        Returns:
            Deck: The updated Deck object if update was successful.

        """
        headers = DEFAULT_HEADERS
        request_payload = json_converter.deck_to_json(deck)

        r = self.session.patch(url=API_URL + 'decks/' + deck.id,
                               headers=headers,
                               json=request_payload)

        json_data = r.json()
        updated_deck = json_converter.json_to_deck(json_data)

        return updated_deck

    def delete_deck(self, deck_id):
        """Delete an existing deck.

        Args:
            deck_id (str): The ID of the Deck to delete.

        Returns:
            Deck: The deleted Deck object if deletion was successful.

        """
        if type(deck_id) is not str:
            raise ValueError("'deck_id' parameter must be of type str")

        headers = DEFAULT_HEADERS

        r = self.session.delete(url=API_URL + 'decks/' + deck_id,
                                headers=headers)

        json_data = r.json()
        deleted_deck = json_converter.json_to_deck(json_data)

        return deleted_deck
