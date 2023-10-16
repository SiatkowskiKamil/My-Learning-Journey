class Player:

    def __init__(self):
        self.name = 'Gallonimus Annonimus'


class HumanPlayer(Player):

    def __init__(self):
        self.name = self.whats_your_name()

    def whats_your_name(self):
        """
        Ask the user for their name.
        """
        self.player_name = input('What\'s your name? ')
        return self.player_name


class ComputerPlayer(Player):

    def __init__(self):
        self.name = 'Bob'
