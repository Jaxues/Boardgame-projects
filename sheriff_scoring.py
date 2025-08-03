class Game():
    def __init__():
        """
        Intialize setup of game
        """
        num_players=0
        apple_king_and_queen=[]
        cheese_king_and_queen=[]
        bread_king_and_queen=[]
        chicken_king_and_queen=[]
    def tie_breaking():
        """
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king
        """ 

    def appleking():
        """
        Score winner of apple king and queen
        Apple king gets 20
        Apple queen gets 10

        """

    def cheeseking():
        """
        Score winner of  cheese king and queen
        cheese king gets 15 
        cheese queen gets 10

        """
    def breadking():
        """
        Score winner of  king and queen
        bread king gets 15 
        bread queen gets 10

        """
    def chickenking():
        """
        Score winner of  king and queen
        chicken king gets 10
        chicken queen gets 5 
        """
    
    def rankings():
        """
        Rank all players in game
        """


    def tiebreaker():
        """
        Break ties in any rankings.
        First number of coins
        Second number of contraband
        """
        pass


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
    def coins(self):
        denom=[1,5,20,50]
        counter_coins=0
        while counter_coins<4:
            num_coins=input(f'How many {denom[counter_coins]} coins does {self.name} have? ')
            if num_coins.isdigit():
                coins+=denom[counter_coins]*num_coins
                counter_coins+=1
            else:
                print("Please enter a valid number of coins for {self.name}")
    
    def scoring(self):
        legal_goods=(('apples',2),('cheese',3),('chickens',4),('bread',3))
        counter_legal=0
        amount_goods=[]
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
                print("Enter a valid number for {self.name}")
        self.num_apples,self.num_cheese,self.num_chickens,self.num_bread=amount_goods 

        if self.contraband==True:
            self.contrabandscoring()
        

    def contrabandscoring(self):
        illegal_goods=(('Pepper',6),('Silks',8),('Mead',7),('Crossbows',8))
        royal_goods=(('Green Apples',4,2),('Gouda Cheese',6,2),('Rye Bread',6,2),('Golden Apples',6,3),('Blue Cheese',9,3),('Pumpernickel Bread',9,3),('Royal Rooster',8,2))
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
                print("Enter valid number of royal goods for {self.name}")

avery=Player('Avery')
avery.scoring()
print(avery.score)
