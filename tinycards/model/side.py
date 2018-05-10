from uuid import uuid4

from .concept import Concept


class Side(object):
    """"Data class for an Tinycards side entity."""

    def __init__(self,
                 user_id,
                 side_id=None,
                 concepts=None):
        """Initialize a new instance of the Side class."""
        self.side_id = side_id if side_id else str(uuid4())
        self.user_id = user_id
        if isinstance(concepts, Concept):
            self.concepts = [concepts]
        elif isinstance(concepts, list):
            self.concepts = concepts
        else:
            raise ValueError("Concepts property can only be a Concept \
                             or list of Concepts")

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
