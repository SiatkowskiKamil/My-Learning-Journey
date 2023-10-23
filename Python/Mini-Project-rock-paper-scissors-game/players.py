class Player:
    """
    Base class for players in the game.
    """

    def __init__(self):
        """
        Initialize a player.
        """
        self.name = 'Gallonimus Annonimus'

    def __str__(self):
        """
        Get a string representation of the player.
        """


class HumanPlayer(Player):
    """
    Class representing a human player.
    """

    def __init__(self):
        """
        Initialize a human player.
        """
        super().__init__()
        self.name = self.whats_your_name()

    def whats_your_name(self):
        """
        Ask the user for their name.
        """
        self.player_name = input('What\'s your name? ')
        return self.player_name


class ComputerPlayer(Player):
    """
    Class representing a computer player.
    """

    def __init__(self):
        """
        Initialize a computer player.
        """
        super().__init__()
        self.name = 'Bob'
