print("=====Number Guessing Game=====")
secret= 67
lives= 5
print("I have guessed a number, Try to guess it!")
print("You have 5 lives...")
print("Best of luck!")
user_guess= int(input("Enter your first Guess: "))
if user_guess == 40 or 41 or 42 or 43 or 44 or 45:
    print("Cold(You are far from it!)")
    print("Lives remaining: ", lives-1)
    if lives ==0:
        print("Game Over! The Secret Number Was", secret, "!")
elif user_guess == 46 or 47 or 48 or 49 or 50:
    print("Normal(You are close but not quite!)")
    print("Lives remaining: ", lives-1)
    if lives ==0:
        print("Game Over! The Secret Number Was", secret, "!")
elif user_guess == 51 or 52 or 53 or 54 or 55:
    print("Warm(You are getiing closer!:O)")
    print("Lives remaining: ", lives-1)
    if lives ==0:
        print("Game Over! The Secret Number Was", secret, "!")
elif user_guess == 56 or 57 or 58 or 59 or 60 :
    print("Hot(You are very close to it!)")
    print("Lives reamaining: ", lives-1)
    if lives ==0:
        print("Game Over! The Secret Number Was", secret, "!") 
elif user_guess== secret:
    print("You have guessed the correct number!")
    print(" hehe we have scammed you! >:)")
    



   