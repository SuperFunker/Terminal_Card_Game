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
        card_played(card,self.player_id)
    def take_damage(self,amnt):
        self.total_health -= amnt
        if self.total_health <= 0:
            self.Death(self.player_id)    
    def healed(self,amnt):
        self.total_health += amnt
        if self.total_health > 100:
            self.total_health = 100
    def Death(self,player_id):
        _ = system('clear')
        print("\n\t\t\t GAME    OVER")
        if player_id == main_p.player_id:
            print("\n\n\n\n\tYou have Died")
            sleep(6)
            Open_Screen('has')
        else:
            print("\n\n\n\n\t You Won")
            sleep(6)
            Open_Screen('has')
# CARDS
card1 = Card(1,"Fireball (15 damage)", 15)
card2 = Card(2,"Bite (5 attack / 5 heal)",5,5)
card3 = Card(3,"Health Potion (15 heal)",0,15)
card4 = Card(4, "Battle Axe (20 Damage)",20)
card5 = Card(5, "Sword (13 Damage)", 13)

#region GUI
def Open_Screen(name_is):
    _ = system('clear')
    print("\tWelcome To Deadly Roads")
    print("\n A) Play\n B) Credits\n C) Exit")
    if name_is is None:
        name = input("\n\n Please type your name first. > ")        
        return name       
    else:
        Menu_Choice()
def Credits():
    _ = system('clear')
    print("\n\n\t\tMade by John")
    sleep(4)
    Open_Screen('has')
def Menu_Choice():    
    choice = input("\n Welcome {}, Please type the letter of your choice and press enter > ".format(name))
    if choice.lower() == 'a':
        Game(False)
    elif choice.lower() == 'b':
        Credits()
    elif choice.lower() == 'c':
        exit()
    else:
        print("\n This is not a valid choice")
        sleep(1)
        Open_Screen('has')
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
        card_ind2 = random.randint(1,6)
        chosen_card2 = enemy.deck[card_ind2]
        enemy.play_card(card_ind2,chosen_card2)
#endregion

#region MECHANICS
def random_card():    
    r = random.randint(1,5)
    if r == 1:
        return card1
    elif r == 2:
        return card2
    elif r == 3:
        return card3
    elif r == 4:
        return card4
    else:
        return card5
def create_random_deck():
    deck = []    
    for x in range(0,7):
        card_choice = random.randint(1,5)
        if card_choice == 1:
            deck.append(card1)
        elif card_choice == 2:
            deck.append(card2)
        elif card_choice == 3:
            deck.append(card3)
        elif card_choice == 4:
            deck.append(card4)
        else:
            deck.append(card5)
    return deck
def card_played(card,player_id):
    if card.id == 1:
        if player_id == 1:
            enemy.take_damage(card.damage)
            print("\nYou played Fireball !")
            sleep(2)
            Game(True)
        else:
            main_p.take_damage(card.damage)
            print("\n\n\nEnemy Played Fireball !")
            sleep(2)
            Game(False)
    elif card.id == 2:
        if player_id == 1:
            enemy.take_damage(card.damage)
            main_p.healed(card.heal)
            print("\nYou played Bite !")
            sleep(2)
            Game(True)
        else:
            enemy.healed(card.heal)
            main_p.take_damage(card.damage)
            print("\n\n\nEnemy Played Bite !")
            sleep(2)
            Game(False)
    elif card.id == 3:
        if player_id == 1:
            main_p.healed(card.heal)
            print("\nYou played Health Potion !")
            sleep(2)
            Game(True)
        else:
            enemy.healed(card.heal)
            print("\n\n\nEnemy Played Health Potion !")
            sleep(2)
            Game(False)
    elif card.id == 4:
        if player_id == 1:
            enemy.take_damage(card.damage)
            print("\nYou played Battle Axe !")
            sleep(2)
            Game(True)
        else:
            main_p.take_damage(card.damage)
            print("\n\n\nEnemy Played Battle Axe !")
            sleep(2)
            Game(False)  
    else:
        if player_id == 1:
            enemy.take_damage(card.damage)
            print("\nYou played Sword !")
            sleep(2)
            Game(True)
        else:
            main_p.take_damage(card.damage)
            print("\n\n\nEnemy Played Battle Axe !")
            sleep(2)
            Game(False)
                
#endregion

# PLAYERS
main_p = Player(100,1)
enemy = Player(80,2)

# PROGRAM START
name = Open_Screen(None)
Menu_Choice()






