from sheriff_scoring import Game
from sheriff_player import Player

test_game=Game()
test_game.addplayers()
print(test_game.num_players,test_game.players)
test_game.scoreplayers()
test_game.rankings()
