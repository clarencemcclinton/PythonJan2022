favorite_color = input('What is your favorite color? ') 
print(f'Your favorite color is: {favorite_color}')

guess = input("Pick a number between 1 & 10: ")
comp_num = 6

new_num = int(guess) * 1000
print(f"Here's your guess times 1000: {new_num}")

if guess == "6":
    print("You got it!")
else: 
    print("Sorry! Wrong number try again!")