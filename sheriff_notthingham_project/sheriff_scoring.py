from sheriff_player import Player
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
                chicken_rankings.append((player,player.name,player.num_chickens))
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
        ordered_players=[]
        counter_index=0
        while counter_index<self.num_players:
            print(self.players[counter_index].name)
            counter_index+=1

    def tie_breaking(self):
        """
        compares different measures in order to break ties
        """ 
