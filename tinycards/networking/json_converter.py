"""Several helper functions to convert between data objects and JSON."""
from tinycards.model import Card, Concept, Deck, Fact, Side, User


# --- User conversion

def json_to_user(json_data):
    """Convert a JSON dict into a User object."""
    user_obj = User(
        creation_date=json_data['creationDate'],
        email=json_data['email'],
        fullname=json_data['fullname'],
        user_id=json_data['id'],
        learning_language=json_data['learningLanguage'],
        picture_url=json_data['pictureUrl'],
        subscribed=json_data['subscribed'],
        subscriber_count=json_data['subscriberCount'],
        subscription_count=json_data['subscriptionCount'],
        ui_language=json_data['uiLanguage'],
        username=json_data['username']
    )

    return user_obj


# --- Fact conversion

def json_to_fact(json_data):
    """Convert a JSON dict into a Fact object."""
    fact_obj = Fact(
        text=json_data['text'],
        fact_id=json_data['id'],
        fact_type=json_data['type']
    )

    return fact_obj


def fact_to_json(fact_obj):
    """Convert a Fact object into a JSON dict."""
    json_data = {
        'id': fact_obj.id,
        'text': fact_obj.text,
        'type': fact_obj.type
    }

    return json_data


# --- Concept conversion

def json_to_concept(json_data):
    """Convert a JSON dict into a Concept object."""
    concept_obj = Concept(
        fact=json_to_fact(json_data['fact']),
        user_id=json_data['userId'],
        concept_id=json_data['id'],
        creation_timestamp=json_data['createdAt'],
        update_timestamp=json_data['updatedAt']
    )

    return concept_obj


def concept_to_json(concept_obj):
    """Convert a Concept object into a JSON dict."""
    json_data = {
        'createdAt': concept_obj.creation_timestamp,
        'fact': fact_to_json(concept_obj.fact),
        'id': concept_obj.id,
        'noteFacts': [],
        'updatedAt': concept_obj.update_timestamp,
        'userId': concept_obj.user_id
    }

    return json_data


# --- Side conversion

def json_to_side(json_data):
    """Convert a JSON dict into a Side object."""
    side_obj = Side(
        side_id=json_data['id'],
        user_id=json_data['userId'],
        concepts=[json_to_concept(c) for c in json_data['concepts']]
    )

    return side_obj


def side_to_json(side_obj):
    """Convert a Side object into a JSON dict."""
    json_data = {
        'concepts': [concept_to_json(c) for c in side_obj.concepts],
        'id': side_obj.side_id,
        'userId': side_obj.user_id
    }

    return json_data


# --- Card conversion

def json_to_card(json_data):
    """Convert a JSON dict into a Card object."""
    card_obj = Card(
        front=json_to_side(json_data['sides'][0]),
        back=json_to_side(json_data['sides'][1]),
        user_id=json_data['userId'],
        card_id=json_data['id']
    )

    return card_obj


def card_to_json(card_obj):
    """Convert a Card object into a JSON dict."""
    json_data = {
        'id': card_obj.id,
        'sides': [
            side_to_json(card_obj.front),
            side_to_json(card_obj.back)
        ],
        'userId': card_obj.user_id
    }

    return json_data


# --- Deck conversion

def json_to_deck(json_data):
    """Convert a JSON dict into a Deck object."""
    deck_obj = Deck(
        title=json_data['name'],
        description=json_data['description'],
        deck_id=json_data['id'],
        cover=json_data['imageUrl'],
        cards=([json_to_card(c) for c in json_data['cards']]
               if 'cards' in json_data else [])
    )

    return deck_obj


def deck_to_json(deck_obj):
    """Convert a Deck object into a JSON dict.

    Contains a lot of placeholder values at the moment.
    """
    json_data = {
        'name': deck_obj.title,
        'description': deck_obj.description,
        'private': False,
        'shareable': False,
        'cards': [card_to_json(c) for c in deck_obj.cards],
        'ttsLanguages': [],
        'blacklistedSideIndices': [],
        'blacklistedQuestionTypes': [],
        'gradingModes': [],
        'fromLanguage': 'en',
        'imageFile': None
    }

    return json_data
