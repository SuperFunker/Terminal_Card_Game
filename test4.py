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
card4 = Card(4, "Battle Axe (10 Damage)",10)

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
def Credits():
    _ = system('clear')
    print("\n\n\t\tMade by John")
    sleep(4)
    Menu_Choice()
def Menu_Choice():
    _ = system('clear')
    choice = input("\n Welcome {}, Please type the letter of your choice and press enter > ".format(name))
    if choice.lower() == 'a':
        Game(False)
    elif choice.lower() == 'b':
        Credits()
    elif choice.lower() == 'c':
        exit()
    else:
        print("\n This is not a valid choice")
        Menu_Choice()
def Game(turn):
    _ = system('clear')
    print("\nEnemy Health: {}".format(enemy.total_health))
    print("\n\n\n\n {} Health: {}\n".format(name,main_p.total_health))
    i = 0
    for card in main_p.deck:
        i += 1
        print("\t\n {}) {}".format(i,card))
    if turn is False:
        card_ind = int(input("\n\n Choose a number > "))
        if card_ind <= 7 and card_ind > 0:
            chosen_card = main_p.deck[(card_ind - 1)]
            main_p.play_card(card_ind,chosen_card)    
        else:
            print("\n Not an Availiable Option !")         
            sleep(2)
            Game(False)
    else:
        card_ind2 = random.randint(1,7)
        chosen_card2 = enemy.deck[card_ind2]
        enemy.play_card(card_ind2,chosen_card2)

#region MECHANICS
def random_card():    
    r = random.randint(1,4)
    if r == 1:
        return card1
    elif r == 2:
        return card2
    elif r == 3:
        return card3
    else:
        return card4
def create_random_deck():
    deck = []    
    for x in range(0,7):
        card_choice = random.randint(1,4)
        if card_choice == 1:
            deck.append(card1)
        elif card_choice == 2:
            deck.append(card2)
        elif card_choice == 3:
            deck.append(card3)
        else:
            deck.append(card4)
    return deck
def card_played(card_id,player_id):
    if card_id == 1:
        if player_id == 1:
            enemy.take_damage(10)
            print("\nYou played Fireball !")
            sleep(2)
            Game(True)
        else:
            main_p.take_damage(10)
            print("\nEnemy Played Fireball !")
            sleep(2)
            Game(False)
    elif card_id == 2:
        if player_id == 1:
            enemy.take_damage(5)
            main_p.healed(5)
            print("\nYou played Bite !")
            sleep(2)
            Game(True)
        else:
            enemy.healed(5)
            main_p.take_damage(5)
            print("\nEnemy Played Bite !")
            sleep(2)
            Game(False)
    elif card_id == 3:
        if player_id == 1:
            main_p.healed(15)
            print("\nYou played Health Potion !")
            sleep(2)
            Game(True)
        else:
            enemy.healed(15)
            print("\nEnemy Played Health Potion !")
            sleep(2)
            Game(False)
    else:
        if player_id == 1:
            enemy.take_damage(10)
            print("\nYou played Battle Axe !")
            sleep(2)
            Game(True)
        else:
            main_p.take_damage(10)
            print("\nEnemy Played Battle Axe !")
            sleep(2)
            Game(False)

        
class Player():
    def __init__(self,total_health,player_id):
        self.total_health = total_health
        self.player_id = player_id
        self.deck = create_random_deck()
    def draw_card(self):
        self.deck.append(random_card())
    def play_card(self,card_index,card):
        self.deck.pop(card_index - 1)        
        self.draw_card()        
        card_played(card.id,self.player_id)
    def take_damage(self,amnt):
        self.total_health -= amnt
    def healed(self,amnt):
        self.total_health += amnt
#endregion

main_p = Player(100,1)
enemy = Player(80,2)


name = Open_Screen()
Menu_Choice()




