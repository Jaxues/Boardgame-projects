class Game():
    def __init__():
        num_players=0



class Player()
    __init__(self):
        name=''
        num_apples=0
        num_bread=0
        num_cheese=0
        num_chicken=0
        contraband=False
        coins=0
        num_contraband=0
    def __coins__(self):
        denom=[1,5,20,50]
        counter_coins=0
        while counter_coins<4:
            num_coins=input(f'How many {denom[counter_coins]} coins does player have? '))
            if num_coins.isdigit():
                coins+=denom[counter_coins]*num_coins
                counter_coins+=1
            else:
                print("Please enter a valid number of coins for {self.player}")
    
    def __scoring__(self):
        legal_goods=(('apples',2),('cheese',3),('chickens',4),('bread',3))
        counter_legal=0
        amount_good=[]
        while counter_legal < 4:
            if counter_legal%2==0:
                num_legal=input(f'How many {legal_goods[counter_legal][0]} does player have? ')
            elif counter_legal%2==1:
                num_legal=input(f'How much {legal_goods[counter_legal][0]} does player have? ')
            if num_legal.isdigit():
                score+=legal_goods[counter_legal][1]*int(num_legal)
                amount_goods.append(int(num_legal))
        num_apples,num_cheese,num_chickens,num_bread=amount_goods 

        if self.contrabandscoring==True:
            self.contrabandscoring()
        


    def __contrabandscoring__(self):
        illegal_goods=(('Pepper',6),('Silks',8),('Mead',7),('Crossbows',8))
        royal_goods=(('Green Apples',4,2),('Gouda Cheese',6,2)('Rye Bread',6,2)('Golden Apples',6,3)('Blue Cheese',9,3)('Pumpernickel',9,3)('Royal Rooster',8,2))
        counter_illegal=0
        counter_royal=0
        type_royal=''
        while counter_legal<4:
            if counter_illegal%2==0:
                num_illegal=input(f'How many {illegal_goods[counter_illegal][0]} does player have? ')
            elif counter_legal%2==1:
                num_illegal=input(f'How much {illegal_goods[counter_illegal][0]} does player have? ')
            if num_illegal.isdigit()
               self.score+=illegal_goods[counter_illegal][1]*num_illegal 
               self.num_contraband+=num_illegal
        while counter_royal<7:
            if counter_royal%7==0 or counter_royal%7==3:
                num_royal=input(f'How many {royal_goods[counter_illegal][0]} does {self.name} have? ')
                type_royal='apples'
            elif counter_royal%7==1 or counter_royal%7==4:
                num_royal=input(f'How much {royal_goods[counter_illegal][0]} does {self.name} have? ')
                type_royal='cheese'

            elif counter_royal%7==2 or counter_royal%7==5:
                num_royal=input(f'How much {royal_goods[counter_illegal][0]} does {self.name} have? ')
                type_royal='bread'

            elif counter_royal%7==6:
                num_royal=input(f'How many {royal_goods[counter_illegal][0]} does player have? ')
                type_royal='chickens'
            if num_royal.isdigit():
                score+=royal_goods[counter_royal][1]*num_royal 
                if type_royal='apples':
                    self.num_apples+=royal_goods[counter_royal][2]
                elif type_royal='cheese':
                   self.num_cheese+=royal_goods[counter_royal][2]
                elif type_royal='bread':
                   self.num_bread+=royal_goods[counter_royal][2]
                elif type_royal='chickens':
                   self.num_chickens+=royal_goods[counter_royal][2]
