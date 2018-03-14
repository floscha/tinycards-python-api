class TrendableData(object):
    """All data fields of the Trendable class."""
    def __init__(self,
                 blacklisted_question_types,
                 blacklisted_side_indices,
                 card_count,
                 compact_id,
                 cover_image_url,
                 created_at,
                 deck_groups,
                 description,
                 enabled,
                 favorite_count,
                 from_language,
                 fullname,
                 grading_modes,
                 hashes,
                 id_,
                 image_url,
                 name,
                 picture,
                 private,
                 shareable,
                 slug,
                 tag_ids,
                 tts_languages,
                 ui_language,
                 updated_at,
                 user_id,
                 username):
        """Initialize a new instance of the TrendableData class.

        Args:
            blacklisted_question_types (list):
            blacklisted_side_indices (list):
            card_count (int): The number of cards in the deck.
            compact_id (str): The compact version of the deck ID.
            cover_image_url: URL for the cover image of the deck.
            created_at (float): Timestamp for when the deck was created.
            deck_groups (list):
            description (str): Textual description of the set.
            enabled (bool): Whether or not the deck is enabled.
            favorite_count: The number of users who favorited this deck.
            from_language (str): The language used for learning.
            fullname (str): Full name of the deck's creator.
            grading_modes (list):
            hashes (dict): The hashes for 'author', 'cardCount', 'deck',
                'deckGroups', and 'favorite'.
            id_ (str): Unique identifier of the deck.
            image_url (str):
            name (str): The name of the deck.
            picture (str): URL to the picture of the trendable.
            private (bool): Whether or not the deck is private.
            shareable (bool): Whether or not the deck can be shared.
            slug (str): A more URL-compatible format of the name.
            tag_ids (list): List of tags used for the deck.
            tts_languages (list): The languages selected for speech generation.
            ui_language (str): Language selected for the user interface.
            updated_at (float): Timestamp for when the deck was last updated.
            user_id (int): User ID of the deck's creator.
            username (str): Duolingo user name of the deck's creator.
        """
        self.blacklisted_question_types = blacklisted_question_types
        self.blacklisted_side_indices = blacklisted_side_indices
        self.card_count = card_count
        self.compact_id = compact_id
        self.cover_image_url = cover_image_url
        self.created_at = created_at
        self.deck_groups = deck_groups
        self.description = description
        self.enabled = enabled
        self.favorite_count = favorite_count
        self.from_language = from_language
        self.fullname = fullname
        self.grading_modes = grading_modes
        self.hashes = hashes
        self.id = id_
        self.image_url = image_url
        self.name = name
        self.picture = picture
        self.private = private
        self.shareable = shareable
        self.slug = slug
        self.tag_ids = tag_ids
        self.tts_languages = tts_languages
        self.ui_language = ui_language
        self.updated_at = updated_at
        self.user_id = user_id
        self.username = username

