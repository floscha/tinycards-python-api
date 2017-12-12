from time import time
from uuid import uuid4


class Concept(object):
    """Data class for an Tinycards concept entity."""

    def __init__(self,
                 fact,
                 user_id,
                 concept_id=None,
                 creation_timestamp=None,
                 update_timestamp=None):
        """Initialize a new instance of the Concept class."""
        self.fact = fact
        self.user_id = user_id
        self.id = concept_id if concept_id else str(uuid4())
        self.creation_timestamp = (creation_timestamp if creation_timestamp
                                   else time())
        self.update_timestamp = (update_timestamp if update_timestamp
                                 else self.creation_timestamp)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
