class Entry:
    """
    Crossword clue entry
    """

    def __init__(self, clue: str, answer: str, number: int, is_across: bool) -> None:
        self.clue = clue
        self.answer = "_{}_".format(answer)
        self.number = number
        self.is_across = is_across

    def length(self):
        """
        Returns the length of the entry
        """
        return len(self.answer)
    
    def __str__(self) -> str:
        return self.answer

    def __repr__(self) -> str:
        return self.answer
