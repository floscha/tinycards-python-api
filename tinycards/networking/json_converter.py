"""Several helper functions to convert between data objects and JSON."""
from tinycards.model import Card, Concept, Deck, Fact, Favorite
from tinycards.model import SearchableData, Side, Trendable, TrendableData
from tinycards.model import User


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
        # 'id': fact_obj.id,
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
        # 'createdAt': concept_obj.creation_timestamp,
        'fact': fact_to_json(concept_obj.fact),
        # 'id': concept_obj.id,
        # 'noteFacts': [],
        # 'updatedAt': concept_obj.update_timestamp,
        # 'userId': concept_obj.user_id
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
        # 'id': side_obj.side_id,
        # 'userId': side_obj.user_id
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
        # 'id': card_obj.id,
        'creationTimestamp': card_obj.creation_timestamp,
        'sides': [
            side_to_json(card_obj.front),
            side_to_json(card_obj.back)
        ],
        # 'userId': card_obj.user_id
    }

    # Add additional fields if not None.
    # if card_obj.creation_timestamp:
    #     json_data['creationTimestamp'] = card_obj.creation_timestamp

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


def deck_to_json(deck_obj, cards_as_string=False):
    """Convert a Deck object into a JSON dict.

    Contains a lot of placeholder values at the moment.

    Args:
        cards_as_string (bool): Convert the cards list into a single string.
    """
    cards = [card_to_json(c) for c in deck_obj.cards]

    json_data = {
        'name': deck_obj.title,
        'description': deck_obj.description,
        'private': False,
        'shareable': False,
        'cards': str(cards) if cards_as_string else cards,
        'ttsLanguages': [],
        'blacklistedSideIndices': [],
        'blacklistedQuestionTypes': [],
        'gradingModes': [],
        'fromLanguage': 'en',
        # 'imageFile': None
    }

    return json_data


# --- Trendable conversion

def json_to_trendable(json_data):
    """Convert a JSON dict into a Trendable object."""
    json_trendable_data = json_data.get('data')
    if not json_trendable_data:
        raise ValueError("JSON object contains no 'data' field")

    try:
        trendable_data = TrendableData(
            json_trendable_data['blacklistedQuestionTypes'],
            json_trendable_data['blacklistedSideIndices'],
            json_trendable_data['cardCount'],
            json_trendable_data['compactId'],
            json_trendable_data['coverImageUrl'],
            json_trendable_data['createdAt'],
            json_trendable_data['deckGroups'],
            json_trendable_data['description'],
            json_trendable_data['enabled'],
            json_trendable_data['favoriteCount'],
            json_trendable_data['fromLanguage'],
            json_trendable_data.get('fullname'),
            json_trendable_data['gradingModes'],
            json_trendable_data['hashes'],
            json_trendable_data['id'],
            json_trendable_data['imageUrl'],
            json_trendable_data['name'],
            json_trendable_data['picture'],
            json_trendable_data['private'],
            json_trendable_data['shareable'],
            json_trendable_data['slug'],
            json_trendable_data['tagIds'],
            json_trendable_data['ttsLanguages'],
            json_trendable_data['uiLanguage'],
            json_trendable_data['updatedAt'],
            json_trendable_data['userId'],
            json_trendable_data['username']
        )
    except KeyError as ke:
        raise ke

    trendable_obj = Trendable(id_=json_data['id'],
                              type_=json_data['type'],
                              data=trendable_data)

    return trendable_obj


def trendable_to_json(trendable_obj: Trendable):
    """Convert a Trendable object into a JSON dict."""
    trendable_data = trendable_obj.data
    json_trendable_data = {
        'blacklistedQuestionTypes': trendable_data.blacklisted_question_types,
        'blacklistedSideIndices': trendable_data.blacklisted_side_indices,
        'cardCount': trendable_data.card_count,
        'compactId': trendable_data.compact_id,
        'coverImageUrl': trendable_data.cover_image_url,
        'createdAt': trendable_data.created_at,
        'deckGroups': trendable_data.deck_groups,
        'description': trendable_data.description,
        'enabled': trendable_data.enabled,
        'favoriteCount': trendable_data.favorite_count,
        'fromLanguage': trendable_data.from_language,
        'fullname': trendable_data.fullname,
        'gradingModes': trendable_data.grading_modes,
        'hashes': trendable_data.hashes,
        'id': trendable_data.id,
        'imageUrl': trendable_data.image_url,
        'name': trendable_data.name,
        'picture': trendable_data.picture,
        'private': trendable_data.private,
        'shareable': trendable_data.shareable,
        'slug': trendable_data.slug,
        'tagIds': trendable_data.tagIds,
        'ttsLanguages': trendable_data.tts_languages,
        'uiLanguage': trendable_data.ui_language,
        'updatedAt': trendable_data.updated_at,
        'userId': trendable_data.user_id,
        'username': trendable_data.username
    }

    json_data = {
        'id': trendable_obj.id,
        'type': trendable_obj.type,
        'data': json_trendable_data
    }

    return json_data


# --- Searchable conversion

def json_to_searchable(json_data):
    """Convert a JSON dict into a Searchable object."""
    json_searchable_data = json_data.get('data')
    if not json_searchable_data:
        raise ValueError("JSON object contains no 'data' field")

    try:
        searchable_data = SearchableData(
            json_searchable_data['id'],
            json_searchable_data['name'],
            json_searchable_data['description'],
            json_searchable_data.get('averageFreshness')
        )
    except KeyError as ke:
        raise ke

    searchable_obj = Trendable(id_=json_data['id'],
                               type_=json_data['type'],
                               data=searchable_data)

    return searchable_obj


# --- Favorite conversion

def json_to_favorite(json_data):
    """Convert a JSON dict into a Favorite object."""
    favorite_obj = Favorite(id_=json_data['id'],
                            deck=json_to_deck(json_data['deck']))

    return favorite_obj


def favorite_to_json(favorite_obj: Favorite):
    """Convert a Favorite object into a JSON dict."""
    json_data = {
        'id': favorite_obj.id,
        'deck': deck_to_json(favorite_obj.deck)
    }

    return json_data

