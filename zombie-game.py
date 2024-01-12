print('''
             ,
          _,-""-._
        ,"        ".
       /    ,-,  ,"\
      "    /   \ | o|
      \    `-o-"  `-',
       `,   _.--'`'--`
         `--`---'                    |   _)
           ,' '      _  /  _ \  ` \   _ \ |  -_)
         ./ ,  `,    ___|\___/_|_|_|_.__/_|\___|
         / /     \
        (_)))_ _,"
           _))))_,
  --------(_,-._)))-------------------------------


  n4bis
''')
print("Welcome to Zombie Appocalypse.")
print("Your mission is to escape the city.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input("You are in the city, where do you want to go? Type 'left' or 'right'\n)." ).lower()

if choice1 == "left":
  #Continue in the game.
  choice2 = input("You arrived at a river. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
  if choice2 == "wait":
    #Continue in the game.
    choice3 = input("You arrived at the small island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
    if choice3 == "red":
        print("It's a room full of zombie dogs. You are dead.")
    elif choice3 == "yellow":
        print("You found the airplane! You win!")
    elif choice3 == "blue":
        print("You enter a room of zombie cats. You are dead.")
    else:
        print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You got attacked by an angry zombie. Game over.")
else:
  print("You came to the hospital, but there is a zombie ambush inside. Game over.")
  