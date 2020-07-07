#the secret word game

secret_word = "giraffe"                             # create secret word variable for secret word
guess = ""                                          # create variable for user to enter strings of letters
guess_count = 0                                     # create a variable with how many times they've guessed, starting wih 0
guess_limit = 3                                     # create a variable with the limit of how many guesses they get
out_of_guesses = False                              # create a variable to let the program know if they are out of guesses

while guess != secret_word and not(out_of_guesses): #while they haven't guessed the secret word and they haven't run out of guesses
    if guess_count < guess_limit:                   #this checks the limit on the guesses they've made
       guess = input("Enter guess: ")               #this asks the user for input
       guess_count += 1                             #this keeps track of how many guesses they've made, going up one at a time
    else:                                           #this else runs after the while if loop has been fulfilled
        out_of_guesses = True                       #this is the result of the else, they've run out of guesses

if out_of_guesses:                                  #if they run out of guesses, it will print "Out of guesses, you lose."
    print("Out of guesses, you lose.")              #this is printed as a result of the 'Trueness' of the else statement
else:                                               #this is the result of the if statement
    print("You win!")                               #this is printed as a result ---- 'if statements' are followed by 'else'
