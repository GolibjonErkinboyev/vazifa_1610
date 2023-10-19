class Card:
    def __init__(self, id, kredit) -> None:
        self._id = id
        self._kredit = kredit

    def add_summa(self, value):
        self._kredit += value

    @property
    def kretid(self):
        return self._kredit

    