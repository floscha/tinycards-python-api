from model.card import Card


class Deck(object):
    """Data class for an Tinycards deck entity."""

    def __init__(self,
                 title,
                 description=None,
                 cover=None,
                 deck_id=None,
                 visibility='everyone',
                 front_language=None,
                 back_language=None,
                 cards=None):
        """Initialize a new instance of the Deck class."""
        self.id = deck_id
        self.user_id = None

        self.creation_timestamp = None

        self.title = title
        self.description = description

        self.cards = cards if cards else []

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def add_card(self, card):
        """Add a new card to the deck."""
        if type(card) is tuple and len(card) == 2:
            new_card = Card(
                front=card[0],
                back=card[1],
                user_id=self.user_id
            )
        self.cards.append(new_card)
