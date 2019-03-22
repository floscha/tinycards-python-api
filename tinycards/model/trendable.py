from dataclasses import dataclass

from tinycards.model import TrendableData


@dataclass
class Trendable(object):
    """Represents a trending object on Tinycards.

    Args:
        id (int): ID of the entity.
        type (str): The entity type (Can be DECK, DECK_GROUP or USER).
        data (TrendableData): All data fields of the Trendable.
    """
    id: int
    type: str
    data: TrendableData
