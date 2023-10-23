import random


class Game:
    """
    Class representing the game.
    """

    human_player_score = 0
    computer_player_score = 0

    def __init__(self, human_player, computer_player):
        """
        Initialize the game with human and computer players.
        :param human_player: An instance of the HumanPlayer class.
        :param computer_player: An instance of the ComputerPlayer class.
        """
        self.human_player = human_player
        self.computer_player = computer_player

    def rock_paper_scissors_game(self):
        """
        Play a round of rock-paper-scissors with the user.
        """
        user_choice_comparison = ''
        possibilities = ['paper', 'rock', 'scissors']
        winning_combinations = {
            ("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")}
        losing_combinations = {
            ("rock", "paper"), ("scissors", "rock"), ("paper", "scissors")}

        user_choice = input('Rock, paper or scissors [r/p/s]? ')

        while user_choice not in ['r', 'p', 's']:
            print(
                'Invalid choice. Please enter "r" for rock, "p" for paper, or "s" for scissors.')
            user_choice = input('Rock, paper or scissors [r/p/s]? ')

        if user_choice == 'r':
            user_choice_comparison = 'rock'
        elif user_choice == 'p':
            user_choice_comparison = 'paper'
        elif user_choice == 's':
            user_choice_comparison = 'scissors'
        else:
            print('again...')

        computer_choice = random.choice(possibilities)

        if (user_choice_comparison, computer_choice) in winning_combinations:
            print(
                f"And my choice is {computer_choice}! {user_choice_comparison.capitalize()} beats {computer_choice}. You win!")
            Game.human_player_score += 1
            self.score_info()
            self.who_wins()
        elif (user_choice_comparison, computer_choice) in losing_combinations:
            print(
                f"And my choice is {computer_choice}! {computer_choice.capitalize()} beats {user_choice_comparison}. Computer wins!")
            Game.computer_player_score += 1
            self.score_info()
            self.who_wins()
        else:
            print(f"And my choice is {computer_choice}! It's a tie!")
            self.score_info()
            self.who_wins()

    def score_info(self):
        """
        Display the current score.
        """
        print(
            f'You: {Game.human_player_score} {self.computer_player.name}: {Game.computer_player_score}')

    def who_wins(self):
        """
        Determine and display the winner of the game.
        """
        if Game.human_player_score > Game.computer_player_score:
            print('You win!')
        elif Game.human_player_score < Game.computer_player_score:
            print('Sorry dude! You lose!')
        else:
            print('It\'s a tie, sweetheart!')
