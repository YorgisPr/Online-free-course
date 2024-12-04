import random

number_of_doors = 3

# Display welcome messages
print('Welcome to the Angry Goblin Hunt')
print('An award-winning game full of adventure and excitement (!)')

# Get player name
name = input('What is your name?: ')
print('Hi ' + name + ', do you think you can find the goblin hiding in the kitchen cupboards?')

print('|_|' * number_of_doors)

def printEmptyBox(repeats):
    print('|_|'*repeats)
    
goblin_place = random.randint(1, number_of_doors) # This variable represents the goblin's position set automatically

keep_trying = True

# Main game loop
while keep_trying:
    answer = input('Which cupboard do you think the goblin is in [type in number 1-3]: ')
    answer = int(answer)

    if answer == goblin_place: # If player guesses correctly
        print('Well done!! You have found the goblin. He was so scared he ran away.')
        keep_trying = False
    else: # If player's guess is incorrect
        print('Sorry! The goblin is still lurking somewhere else.')

print("Thank you for playing. Now get back to work!")