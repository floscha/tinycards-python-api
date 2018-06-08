"""."""
from uuid import uuid4


class Fact(object):
    """Data class for an Tinycards fact entity."""

    def __init__(self, text=None, fact_id=None, fact_type=None, image_url=None, tts_url=None):
        """Initialize a new instance of the Fact class."""
        self.id = fact_id if fact_id else str(uuid4()).replace('-', '')
        self.text = text
        self.type = fact_type if fact_type else 'TEXT'
        self.image_url = image_url
        self.tts_url = tts_url

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
