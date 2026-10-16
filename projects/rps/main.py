import random
# logic
# rock = 1
# paper = 2
# scissor = 3

# Rock And Paper And seicor Game

# Get Choice From User And Bot And Store In Variable.
bot = random.choice(range(1,4))
print("1.Rock\n2.Paper\n3.Seiccor")
you = int(input("Enter Your Choice: "))

#Dicts need In choice in print

dicts={1:"Rock",
       2:"Paper",
       3:"Seiccor"}

choise = f" You Choose {you}:{dicts[you]}\n bot Choose {bot}:{dicts[bot]}"

#main function that decide win and loose and print the result

if bot == you:
    print("This Is A Draw")
    print(choise)
else:
    if bot ==1 and you ==3:
         print("You Loose! ")
         print(choise)
    elif you ==1 and bot==3:
        print("You Win!")
        print(choise)
    elif bot<you:
        print("You Win! ")
        print(choise)
    elif you<bot:
        print("You Loose! ")
        print(choise)
    else:
        print("Something Went Wrong")
        print(choise)