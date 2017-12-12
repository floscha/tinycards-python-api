"""."""
from uuid import uuid4


class Fact(object):
    """Data class for an Tinycards fact entity."""

    def __init__(self, text, fact_id=None, fact_type=None):
        """Initialize a new instance of the Fact class."""
        self.id = fact_id if fact_id else str(uuid4()).replace('-', '')
        self.text = text
        self.type = fact_type if fact_type else 'TEXT'

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
