from dataclasses import dataclass
from typing import Dict, List


@dataclass
class TrendableData(object):
    """All data fields of the Trendable class.

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
    blacklisted_question_types: List
    blacklisted_side_indices: List
    card_count: int
    compact_id: str
    cover_image_url: str
    created_at: float
    deck_groups: List
    description: str
    enabled: bool
    favorite_count: int
    from_language: str
    fullname: str
    grading_modes: List
    hashes: Dict[str, str]
    id: str
    image_url: str
    name: str
    picture: str
    private: bool
    shareable: bool
    slug: str
    tag_ids: List[str]
    tts_languages: List[str]
    ui_language: str
    updated_at: float
    user_id: int
    username: str

