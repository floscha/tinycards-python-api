from uuid import uuid4

from model.concept import Concept
from model.fact import Fact
from model.side import Side


class Card(object):
    """Data class for an Tinycards card entity."""

    def __init__(self,
                 front,
                 back,
                 user_id,
                 card_id=None):
        """Initialize a new instance of the Card class."""
        self.id = card_id if card_id else str(uuid4())
        self.user_id = user_id

        # While Tinycards originally uses a (2 element) tuple to
        # represent both sides, we chose to go with a more
        # semantic naming here.
        if type(front) is Side:
            self.front = front
        elif type(front) is str:
            self.front = Side(concepts=Concept(Fact(front), self.user_id),
                              user_id=self.user_id)
        else:
            raise ValueError("Front property can only be of type Side")
        if type(back) is Side:
            self.back = back
        elif type(back) is str:
            self.back = Side(concepts=Concept(Fact(back), self.user_id),
                             user_id=self.user_id)
        else:
            raise ValueError("Back property can only be of type Side")

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
