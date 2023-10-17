import random
from players import HumanPlayer, ComputerPlayer


class Menu:

    def __init__(self):
        """
        Initialize the Menu with human and computer players and set the game counter to 0.
        """
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()
        self.game_counter = 0

    def __str__(self):
        pass

    def player_mistake_message(self):
        """
        Display a random player mistake message.
        """
        player_mistake_messages = [
            "\nit appears reading isn't your strong suit, huh?\n",
            "\nreading comprehension issues, perhaps?\n",
            "\nyou might want to work on your reading skills...\n",
            "\nis 'y or n' too complicated to understand?\n",
            "\njust in case you didn't know, 'y' means 'yes'.\n",
            "\nyou really need to work on your input skills...\n",
            "\nmaybe the keyboard layout is confusing?\n",
            "\nhow about trying 'y' for yes?\n",
            "\nunderstanding 'y or n' can be challenging...\n",
            "\nyour keyboard must have a defective 'y' key...\n",
        ]
        print('\n' + self.human_player.name + ',' + ' ' +
              random.choice(player_mistake_messages))

    def introduce(self):
        """
        Introduce the game to the user and collect the game counter input.
        """
        print(
            f'Hi {self.human_player.name} My name is {self.computer_player.name}.')
        while True:
            introduce_question = input(
                'Do you wanna play rock-paper-scissors game? (y/n): ')
            if introduce_question.lower() == 'y':
                game_counter_input = input(
                    'Let\'s play!\n--- Rock-Paper-Scissors Game ---\nHow many rounds would you like to play? ')
                if game_counter_input.isdigit():
                    self.game_counter = int(game_counter_input)
                    break
                else:
                    print('Invalid input. Please enter a number.')
                    continue
            if introduce_question.lower() == 'n':
                are_you_sure = input('Are you sure? ')
                if are_you_sure == 'y':
                    print("\nMaybe next time!\n")
                    return 0
                elif are_you_sure == 'n':
                    continue
                else:
                    print('Sweetie, just enter \'y\' or \'n\'...')
                    continue
            else:
                self.player_mistake_message()
