'''
  start in a house
  choose if get food / look for an escape
    if food:
      wander around, find a door
      if open:
        boss
        if attack high:
          win
        else:
          lose
      if look for another:
        find weird door
        if open:
          find person
          if charisma high:
            win
          else:
            lose
        else:
          repeat
    if escape:
      find a person
        if money:
          win
        if no money:
        fight
        if high defense or charisma:
          win
        else:
          lose
'''

import time,os,sys,turtle

screen = turtle.Screen()
screen.bgcolor("black")




def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input() 
  return value  

def clear():
  os.system("clear")

def sceneset(backc,color,size,content):
  screen.clear()
  screen.bgcolor("black")
  turtle.pencolor(color)
  turtle.hideturtle()
  style = ('Courier', int(size))
  turtle.penup()
  turtle.goto(0,-150)
  turtle.pendown()
  turtle.write(content, font=style, align='center')
  turtle.penup()

def nar(text):
  print("================================")
  typingPrint(text)
  print("")
  print("================================")
  print("")
  time.sleep(2)

def dia(text):
  typingPrint(text)
  print("")
  print("")
  time.sleep(2)
  
'''
  Choice Template
  while True:
    choice = input("")
      if choice == "1":
        
        time.sleep(15)
        break
      elif choice == "2":
       
        time.sleep(15)
        break
      else:
        print("Choose 1 or 2")
        sceneset('black','red', 300, '❌')
        screen.bgcolor("black")
    time.sleep(15)
    break
'''

# Uses class to define all characters

class char:
    def __init__(self, name, attack, charisma, defense, money):
        self.name = name
        self.attack = attack
        self.charisma = charisma
        self.defense = defense
        self.money = money
        
    def __str__(self):
      return self.name+' has '+str(self.attack) +' attack, '+str(self.charisma) +' charisma, '+str(self.defense)+' defense, and '+str(self.money)+' money.'

finished = 1
while finished == 1:
  name = input("Enter a name ")
  sp = 10
  while sp > 0:
    sceneset("black",'white', 300, '⚔')
    attack = int(input("Enter attack value (Integer) "))
    sp -= attack
    sceneset("black",'white', 300, '💗')
    print('You have ' + str(sp) + ' Skill Points left.')
    charisma = int(input("Enter charisma value (Integer) "))
    sp -= charisma
    sceneset("black",'white', 300, '🛡')
    print('You have ' + str(sp) + ' Skill Points left.')
    defense = int(input("Enter defense value (Integer) "))
    sp -= defense
    sceneset("black",'white', 300, '💰')
    print('You have ' + str(sp) + ' Skill Points left.')
    money = int(input("Enter your money (Integer) "))
    sp -= money
    print('You have ' + str(sp) + ' Skill Points left.')
  if sp < 0:
    os.system("clear")
    print("Looks like you messed up point allocation... Try again.")
    pass
  else:
    finished = 0
    MC = char(
      name = name,
      attack = attack,
      charisma = charisma,
      defense = defense,
      money = money
      )

print(MC)


Verified = input('Proceed? (Y/N)')
while True:
  turtle.hideturtle()
  if  Verified == 'Y':
    sceneset("black",'white', 300, '🏚')
    screen.bgcolor("black")
    nar("You start in a very spooky house...")
    nar('You have 2 choices, look for food or an escape. (input 1 or 2)')
    while True:
      choice = input("")
      if choice == "1":
        clear()
        dia("I'm really hungry, I wonder if there is food here?...")
        nar("You find a door, do you enter? (input 1 or 2)")
        
        while True:
          choice = input("")
          if choice == "1":
            nar("You enter the door, you find a monster.")
            
            if MC.attack >= 5:
              nar("Congratulations, you win!")
            else:
              nar("You have been slain.")
            time.sleep(15)
            break
          elif choice == "2":
            nar("You find a wacky door, do you enter? (input 1 or 2)")
            
            while True:
              choice = input("")
              if choice == "1":
        
                time.sleep(15)
                break
              elif choice == "2":
                pass
                #go back to other door
              else:
                print("Choose 1 or 2")
                sceneset('black','red', 300, '❌')
                screen.bgcolor("black")
              
            
          else:
            print("Choose 1 or 2")
            sceneset('black','red', 300, '❌')
            screen.bgcolor("black")
        
        time.sleep(15)
        break
      elif choice == "2":
        clear()
        dia("This place is creepy, I'm going to find an exit...")
        sceneset("black",'white', 300, '🙋')
        nar("You find a man, do you talk to him?")
        
        while True:
          choice = input("")
          if choice == "1":
            sceneset("black",'white', 300, '😁')
            time.sleep(2)
            sceneset("black",'white', 300, '💰')
            nar('The man thanks you for acknowledging him and says, "If you have 5 bucks I will let you go."')
            time.sleep(2)
            
            if MC.money >= 5:
              sceneset("black",'white', 300, '🏆')
              nar("Congradulations, you win!")
            else:
              sceneset("black",'white', 300, '🪦')
              nar("You have been slain.")
 
            time.sleep(15)
            break
          elif choice == "2":
            sceneset("black",'white', 300, '😠')
            nar('The man gets angered and says, "You shall die here."')
            
            if MC.defense >= 5:
              sceneset("black",'white', 300, '🏆')
              nar("Congradulations, you win!")
            else:
              sceneset("black",'white', 300, '🪦')
              nar("You have been slain.")
            time.sleep(15)
            break
          else:
            print("Choose 1 or 2")
            sceneset('black','red', 300, '❌')
            screen.bgcolor("black")
      else:
        print("Choose 1 or 2")
        sceneset('black','red', 300, '❌')
        screen.bgcolor("black")
    time.sleep(15)
    break
  elif Verified == 'N':
    clear()
    MC = char(
    input("Enter a name "),
      attack = int(input("Enter attack value (Integer) ")),
      charisma = int(input("Enter charisma value (Integer) ")),
      defense = int(input("Enter defense value (Integer) ")),
      money = int(input("Enter your money (Integer) "))
      )
    
    print(MC)

    Verified = input('Proceed? (Y/N)')
  else:
    clear()
    print("Please type capital 'Y' or 'N'.")
    print(MC)
    Verified = input('Proceed? (Y/N)')
