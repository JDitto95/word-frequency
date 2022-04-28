import random
def play_game():
    with open("words.txt") as test_word:
        words = test_word.read()
        test_word = list(map(str, words.split()))
        random_word = random.choice(test_word)
        # Add user input
        # what line of code would help me tell the user how many turns they have to guess the word?
        intro = input("would you like to play a game? y/n ").lower()
        if intro == "y":
            intro2 = input("which level would you like to play? 1,2,3 ")
            print("\nYour word is", len(random_word),"letters")
        if intro == "n":
            print("Thank you, come again!")
            exit()
        count = 8
        print(random_word)
        #letter_placement = len(random_word) * "_"
        guesses = []
        while count > 0:
            answer = input("\nplease  input one letter per spot ").casefold()
            w = 0
            guesses += answer    
            for letter in random_word:   # loop for keeping track of guesses
                if letter in guesses:
                    print(letter, end='')
                else :
                    print('_', end='')
                    w+=1
            
            if w == 0:
                print("\nCONGRATULATIONS!! YOU WIN!!\nThe Mystery Word was " + random_word + "and was solved in " + str(count ))
                exit()
            # if len(answer) > 1:  
            #     print("You can't do that!!")
            if answer in random_word:
                print("\nYour guess is correct!!", count ,'wrong guesses left')
            if answer not in random_word:
                count = count-1
                print("\nincorrect", count, 'wrong guesses left')
        if count == 0:
            print('GAME OVER, AMIGO')
        # while count == 0:     
        #exit()
        
        
'''if guesses are in the word then keep track of guesses''' # I dont know what I am trying to do.
#for letter in range(8):
    
        

if __name__ == "__main__":
    play_game()
