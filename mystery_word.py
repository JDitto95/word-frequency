import random
def play_game():
    with open("test-word.txt") as test_word:
        words = test_word.read()
        test_word = list(map(str, words.split()))
        random_word = random.choice(test_word)
        # Add user input
        # what line of code would help me tell the user how many turns they have to guess the word?
        intro = input("would you like to play a game? y/n").lower()
        if intro == "y":
            intro2 = input("which level would you like to play? 1,2,3")
            print("Your word is", len(random_word),"letters")
        if intro == "n":
            print("Thank you, come again!")
            exit()
        count = 8
        letter_placement = len(random_word) * "_"
        guesses = []
        while count > 0:
            answer = input("please only input one letter per spot ").casefold()
            # if len(answer) > 1:  
            #     print("You can't do that!!")
            if answer in random_word:
                print("Your guess is correct!!")
            if answer not in random_word:
                print("incorrect")
            

        
        

if __name__ == "__main__":
    play_game()
