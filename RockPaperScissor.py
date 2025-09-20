import random
# we can also  use random.randint(0,2) which generate random no. between 0-2 
def define(n):
    if(n == 1):
        return "Rock"
    elif(n == 2):
        return "Paper"
    elif(n == 3):
        return "Scissor"

print("WELCOME!, LETS PLAY RACK PAPER SCISSOR")
option = [1,2,3]

while True:
    n = int(input(f"\nChoose\n 1 for ROCK\n 2 for PAPER\n 3 for SCISSOR\n 4 for QUIT : "))
    computer = random.choice(option)
    if(n == 4):
        break
    elif(n < 1 or n > 3):
        print("Invalid option")
    elif(n == computer):
        print("Draw")
    elif((n == 1 and computer == 3) or (n == 2 and computer == 1) or (n == 3 and computer == 2)):
        print("You win")
        print(f"You choose {define(n)}")
        print(f"Computer choose {define(computer)}")
    else:
        print("You lose")
        print(f"You choose {define(n)}")
        print(f"Computer choose {define(computer)}")


    

