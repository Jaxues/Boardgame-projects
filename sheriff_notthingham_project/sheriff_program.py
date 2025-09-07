from sheriff_scoring import Game
from sheriff_player import Player

test_game=Game()

a=Player('a')
a.score=20
a.coins=6
b=Player('b')
b.score=20
b.coins=4
c=Player('c')
c.score=21
d=Player('d')
d.score=20
d.coins=5
test_game.players=[a,b,c,d]
test_game.num_players=4
test_game.rankings()

