#This program builds a simple guessing game with multiplayer
import sys
import random
class Game:
    #Initializing the attributes
    def __init__(self, single_player, comp_guess):
        

        self.__single_player = single_player
        self.__comp_guess = random.randint(1, 10)


    #Creating our methods for the attributes
    def set_single_player(self, single):
        self.__single_player = single


    def get_single_player(self):
        
        if self.__single_player > comp_guess:
            return "Guess too high"
        elif self.__single_player < comp_guess:
            return "Guess too low"
        else: 
            return "congratulations!!! You got my guess."



#This is the multiplayer class
class multiplayer(Game):
    #Initializing the attributes
    def __init__(self, single_player, player_1, player_2):
        #Copying the parent attribute to the multiplayer class
        Game.__init__(self, single_player, comp_guess)

        self.__player_1 = player_1
        self.__player_2 = player_2



    #Creating the mutator for the special attributes
    def set_player_1(self, guess):
        self.__player_1 = guess

    def set_player_2(self, guess):
        self.__player_2 = guess


    #The accessor
    def get_player_1(self):
        if self.__player_1 > comp_guess:
            print("Guess too high.")
        elif self.__player_1 < comp_guess:
            print("Guess to low.")
        else:
            print("Congratulations!!! you got my guess.")

    def get_player_2(self):
        if self.__player_2 > comp_guess:
            print("Guess too high.")
        elif self.__player_2 < comp_guess:
            print("guess too low.")
        else:
            print("Congratulations!!! You got my guess.")


    
#Creating the instance for the class
print("This is a simple guessing game.")
print("You only have 6 times to play this game\nYour guessing should be in the range of 1 and 10")
print("Select your preferred option from the option below")
print("1. Single game\t\t 2. multiplayer")
print("3. Exit")
choice = int(input("Enter your choice: "))
counts_1 = 0
counts_2 = 0
if choice == 1:
    for count in range(1,7):
        
        comp_guess = random.randint(1, 10)
        single_player = int(input("Enter your guess: "))
        Y = Game(single_player, comp_guess)
        Y.get_single_player()
        if comp_guess == single_player:
            counts_1+=1
    print("You only win the computer ", counts_1, 'times out of 6.')

if choice == 2:
    #This is for player_1
    again = True
    while again:
        for count in range(1,7):
            single_player = 1
            comp_guess = random.randint(1, 10)
            player_1 = int(input("Enter your guess player 1: "))
            A = multiplayer(single_player, player_1, player_2 = 1)
            A.get_player_1()
            if player_1 == comp_guess:
                counts_1+=1
    #This is for player 2
        print()
        print("================================")
        print("PLAYER_2 Turn")
            
        for count in range(1,7):
            player_1 = 1
            single_player = 1
            comp_guess = random.randint(1, 10)
            player_2 = int(input("Enter your guess player 2: "))
            B = multiplayer(single_player, player_1, player_2)
            B.get_player_2()
            if comp_guess == player_2:
                counts_2 +=1

        print()
        print()
        if counts_1>counts_2:
            print("Player_1 won the game.")
        elif counts_2>counts_1:
            print("Player_2 won the game.")
        else:
            print("Its a thigh.")
        print()
        print("Enter yes/no to play again.")
        ans = input(":").lower()
        if ans == 'yes':
            again = True
        else:
            print("Thanks for playing.")
            again = False

if choice==3:
    
    sys.exit()
