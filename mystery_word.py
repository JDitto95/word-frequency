import random
def play_game():
    with open("test-word.txt") as test_word:
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
        #letter_placement = len(random_word) * "_"
        guesses = ' '
        while count > 0:
            answer = input("\nplease only input one letter per spot ").casefold()
            guesses += answer    
            for letter in random_word:   # loop for keeping track of guesses
                if letter in guesses:
                    print(letter, end='')
                elif letter not in guesses:
                    print('_', end='')
                    
            
            
            # if len(answer) > 1:  
            #     print("You can't do that!!")
            if answer in random_word:
                count = count-1
                print("\nYour guess is correct!!")
            if answer not in random_word:
                count = count-1
                print("\nincorrect")
        
        while count == 0:
            exit()
        
        
'''if guesses are in the word then keep track of guesses''' # I dont know what I am trying to do.
#for letter in range(8):
    
        

if __name__ == "__main__":
    play_game()
