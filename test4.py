from os import system
from time import sleep
import random

class Card():
    def __init__(self, id, description, damage=0,heal=0):
        self.id = id
        self.description = description
        self.damage = damage
        self.heal = heal
    def __repr__(self):
        return self.description
    def playing():
        pass

card1 = Card(1,"Fireball (10 damage)", 10)
card2 = Card(2,"Bite (5 attack / 5 heal)",5,5)
card3 = Card(3,"Health Potion (15 heal)",0,15)

#region function ideas
def update_screen():
    pass
#endregion

#region GUI
def Open_Screen():
    _ = system('clear')
    print("\tWelcome To Deadly Roads")
    print("\n A) Play\n B) Credits\n C) Exit")
    name = input("\n\n Please type your name first. > ")
    return name
def Menu_Choice():
    choice = input("\n Welcome {}, Please type the letter of your choice and press enter > ".format(name))
    if choice.lower() == 'a':
        pass
    elif choice.lower() == 'b':
        pass
    elif choice.lower() == 'c':
        exit()
    else:
        print("\n This is not a valid choice")
        Menu_Choice()


#region MECHANICS
def random_card():    
    r = random.randint(1,3)
    if r == 1:
            return card1
    elif r == 2:
        return card2
    else:
        return card3
def create_random_deck():
    deck = []
    card_choice = random.randint(1,3)
    for x in 7:
        if card_choice == 1:
            deck.append(card1)
        elif card_choice == 2:
            deck.append(card2)
        else:
            deck.append(card3)
    return deck


        
class Player():
    def __init__(self,total_health):
        self.total_health = total_health
        self.deck = create_random_deck()
    def draw_card(self):
        self.deck.append(random_card())
    def play_card(self,card_index):
        self.deck.pop(card_index + 1)
    def take_damage(self,amnt):
        self.total_health -= amnt
    def healed(self,amnt):
        self.total_health += amnt
#endregion

main_p = Player(100)


name = Open_Screen()
Menu_Choice()



