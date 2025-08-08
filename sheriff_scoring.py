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
            num_players=input('How many players are in the game (Between 3 and 6 players)')
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
            print(self.players)
            counter_players+=1
    

    def scoreplayers(self):
        """
        Score all players in player list
        """
        for i,player in enumerate(self.players):
            player.scoring()
        self.appleking()
        self.cheeseking()
        self.breadking()
        self.chickenking()
        self.rankings()



   
    def appleking():
        """
        Score winner of apple king and queen
        Apple king gets 20
        Apple queen gets 10
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king

        """

    def cheeseking():
        """
        Score winner of  cheese king and queen
        cheese king gets 15 
        cheese queen gets 10
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king

        """
    def breadking():
        """
        Score winner of  king and queen
        bread king gets 15 
        bread queen gets 10
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king
        """
    def chickenking():
        """
        Score winner of  king and queen
        chicken king gets 10
        chicken queen gets 5 
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king

        """
    
    def rankings(self):
        """
        Rank all players in game
        """
        for player in self.players:
            print(player)

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
        print(test_game.players)
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
test_game.addplayers()
test_game.scoreplayers()
for counter,player in enumerate(test_game.players):
    print(test_game.players[counter].score)


