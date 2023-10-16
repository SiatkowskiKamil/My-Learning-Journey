from menu import Menu
from game import Game

menu = Menu()
game = Game(menu.human_player, menu.computer_player)
menu.introduce()

while menu.game_counter > 0:
    game.rock_paper_sissors_game()
    menu.game_counter -= 1

game.who_wins()
