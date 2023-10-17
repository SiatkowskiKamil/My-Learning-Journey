def main():
    """
    Main function to play the Rock-Paper-Scissors game.
    """

    from menu import Menu
    from game import Game

    # Initialize the menu and game objects
    menu = Menu()
    game = Game(menu.human_player, menu.computer_player)

    # Start the game by introducing the menu
    menu.introduce()

    exit_the_game = True

    while exit_the_game:
        while menu.game_counter > 0:
            game.rock_paper_scissors_game()
            menu.game_counter -= 1
            if menu.game_counter == 0:
                question = input('Play again? [y/n]: ')
                if question == 'n':
                    exit_the_game = False
                elif question == 'y':
                    how_many_rounds = input('How many rounds? ')

                    if how_many_rounds.isdigit():
                        menu.game_counter = int(how_many_rounds)
                        break
                    else:
                        print('Invalid input. Please enter a number.')
                        continue

                else:
                    print("Seriously, you're not too smart...")


if __name__ == "__main__":
    main()
