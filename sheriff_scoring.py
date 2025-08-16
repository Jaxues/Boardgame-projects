class Game():
    def __init__(self):
        """
        Intialize setup of game
        """
        self.num_players=0
        self.apple_king_and_queen=[]
        self.cheese_king_and_queen=[]
        self.bread_king_and_queen=[]
        self.chicken_king_and_queen=[]
        self.players=[]


    def addplayers(self):
        """
        add method for adding players
        """
        counter_players=0
        num_players_valid=False
        while num_players_valid is False:
            num_players=input('How many players are in the game (Between 3 and 6 players)' )
            if num_players.isdigit():
                if int(num_players)>=3 and int(num_players)<=6:
                    print(f'Setting up a {num_players} game')
                    self.num_players=int(num_players)
                    num_players_valid=True
                else:
                    print('Invalid number of players. Please enter number between 3 and 6')
            else:
                print('Invalid input. Must be integer between 3 and 6 players inclusive')

        while counter_players<self.num_players:
            player_name=input(f"Enter name of Player {counter_players+1}: ")
            self.players.append(Player(player_name))
            counter_players+=1
    

    def scoreplayers(self):
        """
        Score all players in player list
        """
        for player in self.players:
            player.scoring()
        self.appleking()
        self.cheeseking()
        self.breadking()
        self.chickenking()
        self.rankings()


    def appleking(self):
        """
        Score winner of apple king and queen
        Apple king gets 20
        Apple queen gets 10
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king

        Rankings is a list which has tuple for data.
        Tuple stores player object, name, and number of apples
         
        """
        apple_rankings=[]

        for player in self.players:
            if len(apple_rankings)==0:
                apple_rankings.append((player,player.name,player.num_apples))
            elif player.num_apples>=apple_rankings[0][-1]:
                apple_rankings.insert(0,(player,player.name,player.num_apples))
            elif len(apple_rankings)==1:
                apple_rankings.append((player,player.name,player.num_apples))
        print(apple_rankings)
        if apple_rankings[0][-1]==0:
           self.apple_king_and_queen.append('No apple king or queen')
        elif apple_rankings[0][-1]==apple_rankings[1][-1]:
            """
            If both players tied for apple king
            """
            apple_rankings[0][0].score+=15
            apple_rankings[1][0].score+=15
            self.apple_king_and_queen.append(f'{apple_rankings[0][1]} & {apple_rankings[0][1]}')

        elif len(apple_rankings)==3:
            """
            Can only be 3 players if two tied for queen 
            """
            apple_rankings[0][0].score+=20
            apple_rankings[1][0].score+=5
            apple_rankings[2][0].score+=5
            self.apple_king_and_queen.append(f'{apple_rankings[0][1]}')
            self.apple_king_and_queen.append(f'{apple_rankings[1][1]} & {apple_rankings[2][1]}')
        else:
            apple_rankings[0][0].score+=20
            apple_rankings[1][0].score+=15

    def cheeseking(self):
        """
        Score winner of  cheese king and queen
        cheese king gets 15 
        cheese queen gets 10
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king

        Rankings is a list which has tuple for data.
        Tuple stores player object, name, and amount of cheese
        """
        cheese_rankings=[]
        for player in self.players:
            if len(cheese_rankings)==0:
                cheese_rankings.append((player,player.name,player.num_cheese))
            elif player.num_cheese>=cheese_rankings[0][-1]:
                cheese_rankings.insert(0,(player,player.name,player.num_cheese))
            elif len(cheese_rankings)==1:
                cheese_rankings.append((player,player.name,player.num_cheese))
        if cheese_rankings[0][-1]==0:
            self.cheese_king_and_queen.append('No cheese king or queen')

        elif cheese_rankings[0][-1]==cheese_rankings[1][-1]:
            """
            If both players tied for cheese king
            """
            cheese_rankings[0][0].score+=12
            cheese_rankings[1][0].score+=12
            self.cheese_king_and_queen.append(f'{cheese_rankings[0][1]} & {cheese_rankings[0][1]} are tied for cheese king')

        elif len(cheese_rankings)==3:
            """
            Can only be 3 players if two tied for cheese queen 
            """
            cheese_rankings[0][0].score+=15
            cheese_rankings[1][0].score+=5
            cheese_rankings[2][0].score+=5
            self.cheese_king_and_queen.append(f'{cheese_rankings[0][1]} is cheese king')
            self.cheese_king_and_queen.append(f'{cheese_rankings[1][1]} & {cheese_rankings[2][1]} are tied for cheese queen')
        else:
            cheese_rankings[0][0].score+=15
            cheese_rankings[1][0].score+=10
    def breadking(self):
        """
        Score winner of  king and queen
        bread king gets 15 
        bread queen gets 10
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king
        
        Rankings is a list which has tuple for data.
        Tuple stores player object, name, and amount of bread
        
        self.bread_king_and_queen is list of King and Queen for game
        Player who has most or second most bread

        If tied will share 
        """
        bread_rankings=[]
        for player in self.players:
            if len(bread_rankings)==0:
                bread_rankings.append((player,player.name,player.num_bread))
            elif player.num_bread>=bread_rankings[0][-1]:
                bread_rankings.insert(0,(player,player.name,player.num_bread))
            elif len(bread_rankings)==1:
                bread_rankings.append((player,player.name,player.num_bread))

        if bread_rankings[0][-1]==0:
            self.bread_king_and_queen.append('No bread king')

        if bread_rankings[0][-1]==bread_rankings[1][-1]:
            """
            If both players tied for bread king
            """
            bread_rankings[0][0].score+=12
            bread_rankings[1][0].score+=12
            self.bread_king_and_queen.append(f'{bread_rankings[0][1]} & {bread_rankings[0][1]}')

        elif len(bread_rankings)==3:
            """
            Can only be 3 players if two tied for queen 
            """
            bread_rankings[0][0].score+=15
            bread_rankings[1][0].score+=5
            bread_rankings[2][0].score+=5
            self.bread_king_and_queen.append(f'{bread_rankings[0][1]}')
            self.bread_king_and_queen.append(f'{bread_rankings[1][1]} & {bread_rankings[2][1]}')
        else:
            bread_rankings[0][0].score+=15
            bread_rankings[1][0].score+=10


    def chickenking(self):
        """
        Score winner of  king and queen
        chicken king gets 10
        chicken queen gets 5 
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king

        Rankings is a list which has tuple for data.
        Tuple stores player object, name, and number of chickens
        """
        chicken_rankings=[]
        for player in self.players:
            if len(chicken_rankings)==0:
                bread_rankings.append((player,player.name,player.num_chickens))
            elif player.num_chickens>=chicken_rankings[0][-1]:
                chicken_rankings.insert(0,(player,player.name,player.num_chickens))
            elif len(chicken_rankings)==1:
                chicken_rankings.append((player,player.name,player.num_chicken))
        if chicken_rankings[0][-1]==0:
            self.chicken_king_and_queen.append('No Chicken king or queen')
        if chicken_rankings[0][-1]==chicken_rankings[1][-1]:
            """
            If both players tied for chicken king
            """
            chicken_rankings[0][0].score+=7
            chicken_rankings[1][0].score+=7
            self.chicken_king_and_queen.append(f'{chicken_rankings[0][1]} & {chicken_rankings[0][1]}')

        elif len(chicken_rankings)==3:
            """
            Can only be 3 players if two tied for chicken queen 
            """
            chicken_rankings[0][0].score+=10
            chicken_rankings[1][0].score+=2
            chicken_rankings[2][0].score+=2
            self.chicken_king_and_queen.append(f'{chicken_rankings[0][1]}')
            self.chicken_king_and_queen.append(f'{chicken_rankings[1][1]} & {chicken_rankings[2][1]}')
        else:
            chicken_rankings[0][0].score+=10
            chicken_rankings[1][0].score+=5
   
    def rankings(self):
        """
        Rank all players in game
        """
        for player in self.players:
            print(player.name,player.score)

    def tie_breaking(self):
        """
        compares different measures in order to break ties
        """ 


class Player():
    def __init__(self,name):
        self.name=name
        self.num_apples=0
        self.num_bread=0
        self.num_cheese=0
        self.num_chicken=0
        self.contraband=False
        self.coins=0
        self.num_contraband=0
        self.score=0
    def score_coins(self):
        denom=[1,5,20,50]
        counter_coins=0
        while counter_coins<4:
            num_coins=input(f'How many ${denom[counter_coins]} coins does {self.name} have? ')
            if num_coins.isdigit():
                self.coins+=denom[counter_coins]*int(num_coins)
                counter_coins+=1
            else:
                print(f"Please enter a valid number of coins for {self.name}")
    
    def scoring(self):
        legal_goods=(('apples',2),('cheese',3),('chickens',4),('bread',3))
        counter_legal=0
        amount_goods=[]
        self.score_coins()
        while counter_legal < 4:
            if counter_legal%2==0:
                num_legal=input(f'How much {legal_goods[counter_legal][0]} does {self.name} have? ')
            elif counter_legal%2==1:
                num_legal=input(f'How many {legal_goods[counter_legal][0]} does {self.name} have? ')
            if num_legal.isdigit():
                self.score+=legal_goods[counter_legal][1]*int(num_legal)
                amount_goods.append(int(num_legal))
                counter_legal+=1
            elif not num_legal.isdigit():
                print(f"Enter a valid number for {self.name}")
        self.num_apples,self.num_cheese,self.num_chickens,self.num_bread=amount_goods 
        
        self.has_contraband()

        if self.contraband==True:
            self.contrabandscoring()
        print(self.score)


    def has_contraband(self):
        determine_contraband=False
        while determine_contraband is False:
            has_counter=input(f'Does {self.name} have any contraband. Answer with y or n')
            if has_counter.lower()=='y':
                self.contraband=True
                determine_contraband=True
            elif has_counter.lower()=='n':
                determine_contraband=True
            else:
                print('Please enter valid input')
        

    def contrabandscoring(self):
        illegal_goods=(('Pepper',6),('Silks',8),('Mead',7),('Crossbows',8))
        royal_goods=(('Green Apples',4,2),('Gouda Cheese',6,2),('Rye Bread',6,2),('Golden Apples',6,3),('Blue Cheese',9,3),('Pumpernickel Bread',9,3),('Royal Roosters',8,2))
        counter_illegal=0
        counter_royal=0
        type_royal=''
        while counter_illegal<4:
            if counter_illegal%2==0:
                num_illegal=input(f'How many {illegal_goods[counter_illegal][0]} does {self.name} have? ')
            elif counter_illegal%2==1:
                num_illegal=input(f'How much {illegal_goods[counter_illegal][0]} does {self.name} have? ')
            if num_illegal.isdigit():
                num_illegal=int(num_illegal)
                self.score+=illegal_goods[counter_illegal][1]*num_illegal
                self.num_contraband+=num_illegal
                counter_illegal+=1
            elif not num_illegal.isdigit():
                print("Enter valid number for {self.name}")
        while counter_royal<7:
            if counter_royal%7==0 or counter_royal%7==3:
                num_royal=input(f'How many {royal_goods[counter_royal][0]} does {self.name} have? ')
                type_royal+='apples'
            elif counter_royal%7==1 or counter_royal%7==4:
                num_royal=input(f'How much {royal_goods[counter_royal][0]} does {self.name} have? ')
                type_royal+='cheese'

            elif counter_royal%7==2 or counter_royal%7==5:
                num_royal=input(f'How much {royal_goods[counter_royal][0]} does {self.name} have? ')
                type_royal='bread'

            elif counter_royal%7==6:
                num_royal=input(f'How many {royal_goods[counter_royal][0]} does player have? ')
                type_royal='chickens'
            if num_royal.isdigit():
                num_royal=int(num_royal)
                self.score+=royal_goods[counter_royal][1]*num_royal 
                if type_royal=='apples':
                    self.num_apples+=royal_goods[counter_royal][2]
                elif type_royal=='cheese':
                   self.num_cheese+=royal_goods[counter_royal][2]
                elif type_royal=='bread':
                   self.num_bread+=royal_goods[counter_royal][2]
                elif type_royal=='chickens':
                   self.num_chickens+=royal_goods[counter_royal][2]
                type_royal=''
                counter_royal+=1
            elif not num_royal.isdigit():
                print(f"Enter valid number of royal goods for {self.name}")

test_game=Game()
test_game.players=[Player('a'),Player('b'),Player('c')]
#test_game.players[0].num_cheese=8
test_game.players[0].num_apples= 5
#test_game.players[0].num_bread=7
#test_game.players[0].num_chickens=

#test_game.players[1].num_cheese=8
test_game.players[1].num_apples= 5
#test_game.players[1].num_bread=7
#test_game.players[1].num_chickens=

#test_game.players[2].num_cheese=0
#test_game.players[2].num_bread= 6
test_game.players[2].num_apples=6
#test_game.players[2].num_chickens=



#test_game.addplayers()
#test_game.scoreplayers()
test_game.cheeseking()
#test_game.appleking()
test_game.rankings()
