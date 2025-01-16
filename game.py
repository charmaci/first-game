import random
import numpy as np
running = True
player_turn = True
# this part of the code is where the message you get when choosing your name is determined
def greeting(PlayerName):
 match PlayerName.lower(): 
    case "aigis":
       print("Are you a fellow ROBOTFUCKER as well?")
    
    case "avery":
       print("OMG hi how are you mrs. beauty")
    
    case "spamton":
       print("Holy [Hyperlink Blocked], are you the [BIG SHOT] himself???")
    
    case "maki" | "maci":
       print("Go pretend to be someone else.")
       return False
    case "bibi" | "crumbs":
       print("I didn't make anything special for irrelevants, sorry.")
    case _:
       print("Never heard of that name before, but welcome!")
 return True
player_name = input("Hi! What is your name? ")
while not greeting(player_name):
    player_name = input("> ")

def damage_calculator(PlayerName): #exists to give more damage if you are spamton
    if PlayerName.lower() == "spamton":
        return 60
    if PlayerName.lower() == "crumbs":
        return 1
    else:
        return 40
def hp_calculator(PlayerName): #exists to give the player hp, more hp if the player is aigis
    if PlayerName.lower() == "aigis":
        return 600
    if PlayerName.lower() == "crumbs":
        return 300
    else:
        return 450
mrbeast_stats = {
    "name": "Mr. Beast",
    "health": 1100,
    "damage": 35
}
dog_stats = {
    "name": "The Dog",
    "health": 700,
    "damage": 10

}
class Enemy:
    def __init__(self,stats):
        self.name = stats["name"]
        self.hp = stats["health"]
        self.damage = stats["damage"]
        self.max_hp = stats["health"]
        self.attacks = [self.basic_attack,self.casino,self.holy_trinity]
    def enemy_introduction(self):
        match self.name:
            case "Mr. Beast":
             return "A wild "+ self.name + " appeared! \n health: " + str(self.hp) +" damage: "+ str(self.damage)+"."
            case "The Dog" | "HOMOPHOBIC DOG":
             return "A cute little dog appeared! How can anyone hurt something so adorable? "+str(self.damage)+" damage, "+str(self.hp)+" health. Literally harmless..."
    def hit_enemy(self,damage):
     self.hp -= damage
     match self.name:
         case "Mr. Beast":
             if (self.hp < (self.max_hp*0.25)) and (self.lunchly not in self.attacks):
              print(self.name + " has lost half of their health, so they went to the Mr.Beast shop and bought something...")
              self.attacks.append(self.lunchly)
         case "The Dog" | "HOMOPHOBIC DOG":
           if (self.hp < (self.max_hp*0.35)) and (self.lunchly not in self.attacks) and (self.faggot not in self.attacks):
              print(self.name+" can't take it anymore... you hurt him too much. You monster")
              print(self.name+" starts smelling your insane homosexuality... and he doesn't like it.")
              print(self.name +" has became... HOMOPHOBIC DOG")
              self.name = "HOMOPHOBIC DOG"
              self.hp += 800
              self.damage += 40
              self.attacks.append(self.lunchly)
              self.attacks.append(self.faggot)
    enemy_turn = False

              
           

    def info_enemy(self):
        return self.name + ": " + str(self.damage)+ " damage. "+ str(self.hp)+ " Hitpoints left."
    def basic_attack(self):
         match self.name:
            case "Mr. Beast":
               print("You might be too much of a coward to use your hands to attack, but "+self.name+ " sure isn't!\n"+self.name+" punches you, dealing "+str(round(self.damage))+ " damage")
               print("Realising that you are too much of a coward to attack with your hands reduces your damage by 5")
               player.damage -= 5

               return self.damage
            case "The Dog" | "HOMOPHOBIC DOG":
                print(self.name+" bites you, dealing "+str(round(self.damage))+ " damage! Ow.")
                return self.damage
    def casino(self):
        match self.name:
         case "Mr. Beast":
          print(self.name+" learns about gambling, spending most of their money for a 10% "+  "chance to deal enermous damage!")
          casino_damage = [0,1]
          casino_damage_decider = random.choices(casino_damage, weights=[9,1])
          if casino_damage_decider[0] == casino_damage[1]:
              print("Oops, "+self.name+" got actually lucky this time! Dealing a whopping "+str(round(self.damage*6.5))+" damage.")
              return self.damage*6.5
          else:
            print(self.name+" didn't get anything this time. Don't worry, 99%"+" of gamblers quit before they deal "+str(round(self.damage*6.5))+" damage!")
            return 0
         case "The Dog" | "HOMOPHOBIC DOG":
            print(self.name+" flips a coin...")
            coin_damage = [0,1]
            coin_damage_decider = random.choice(coin_damage)
            if coin_damage_decider == coin_damage[1]:
                print("...It's heads, so "+self.name+ " uses his head to bite you and deal "+str(round(self.damage*1.5))+" damage.")
                return self.damage*1.5
            else:
                print("...It's tails, so "+self.name+ " wiggles his tail, filling everyone with joy! And granting them more damage.")
                player.damage += round(player.damage*0.1)
                self.damage += round(self.damage*0.2)
                return 0 

    def holy_trinity(self):
      match self.name:
        case "Mr. Beast":
         possible_damages = [self.damage*0.15,self.damage*0.25,self.damage*0.3,self.damage*0.4,self.damage*0.5,self.damage*0.6,self.damage*0.8]
         final_damage = random.choices(possible_damages, k=3)
         print(self.name+" throws three random punches in random angles, dealing "+ str(round(final_damage[0]))+" "+ str(round(final_damage[1]))+" " +str(round(final_damage[2])) +" damage each!")
         return sum(final_damage)
        case "The Dog" | "HOMOPHOBIC DOG":
            player_hp_based_damage = np.array([player.hp*0.1,player.hp*0.2,player.hp*0.25,player.hp*0.3,player.hp*0.4])
            player_hp_damage = random.choices(player_hp_based_damage, k=5)
            dog_damages = np.array([self.damage*0.15,self.damage*0.2,self.damage*0.25,self.damage*0.3,self.damage*0.35])
            dog_dmg = random.choices(dog_damages, k=5)
            final_damage_claw = np.add(dog_dmg,player_hp_damage)
            actual_final_damage = (random.choices(final_damage_claw, k=2))
            print(self.name +" uses his two sharp claws to scratch you, dealing "+ str(round(actual_final_damage[0]))+" and "+ str(round(actual_final_damage[1]))+" damage!" )
            return sum(actual_final_damage)

    def lunchly(self):
        match self.name:
            case "Mr. Beast":
             self.hit_enemy(round(-80-(self.hp*0.7)))
             self.damage += 6
             print(self.name + " went ahead and bought a delicious lunchly pack and ate it! healing "+ str(round(80+self.hp*0.7)) +" hitpoints. And gaining 6 damage after \n overcoming the fear of lying about how horrible a product is")
             return 0
            case "The Dog" | "HOMOPHOBIC DOG":
                print(self.name+" barks loudly with excitement, giving himself additional 8 damage")
                self.damage += 8
                return 0
    def faggot(self):
       print(self.name+" yells not very family friendly homophobic slurs at you, ouch!")
       print("It may not hurt you phsyically, but the emotional damage is enough to remove 1/5 of your damage!")
       player.damage -= round(player.damage*0.2)
       return 0

    def enemey_attack_decider(self):
        attack_enemy = random.choice(self.attacks)
        return round(attack_enemy())

class Player:
    def __init__(self,player_name):
        self.damage = damage_calculator(player_name)
        self.hp = hp_calculator(player_name)
        self.name = player_name
    def player_introduction(self):
        if self.name.lower() == "spamton":
            return "WELCOME TO THE [Hyperlink Blocked]! SINCE YOU ARE A [BIG SHOT], YOU HAVE MORE DAMAGE!!!  YOUR HP IS " + str(self.hp) +" AND YOUR DAMAGE IS " + str(self.damage)
        if self.name.lower() == "aigis":
            return "You gain additional hp  because your body is fucking metal! making your hp " + str(self.hp) +" and you deal " + str(self.damage) + " damage!"
        if self.name.lower() == "crumbs":
            return "Hahaha, imagine calling me not a gay fag at heart. You have less hp and damage, I wont even say how much, cry about it."
        else:
            return "Your hp is " + str(self.hp) +" and you deal " + str(self.damage) + " damage!"
    def hit_player(self,damage):
     self.hp -= damage
    def kick(self):
        print("To not make your hands hurt, you used your legs to kick the enemy instead, dealing "+str(self.damage)+" damage to them!")
        return self.damage
    def gambling(self):
        gamble_damage = [self.damage*0.25,self.damage*0.5,self.damage*0.75,self.damage*1.75,self.damage*2.25]
        gamble_damage_final = random.choice(gamble_damage)
        print("You threw a dice clinging to the hope of dealing more damage than usual, dealing "+ str(round(gamble_damage_final)) + " damage to the enemy!")
        return round(gamble_damage_final)
    def sac(self):
        if self.hp < 150:
            print("Nuh uh! You don't have enough health to sacrifice.")
            return None
        else:
         self.hit_player(150) 
         print("You stabbed yourself (ow), dealing 150 damage to yourself. But hey! You dealt "+str(self.damage*3)+" damage to the enemy in exchange.")
         return self.damage*3
    def healing(self):
        max_hp = 425 if self.name.lower() == "aigis" else 325
                       
        if self.hp > max_hp:
             print("only Mr. Beast and his team can exceed the hp limit. sorry, they have more money.")
             return 0
        else:
            print("You beg the game dev to give you more hp, and they accept! healing you by 125 hitpoints")
            self.hit_player(-125)
            return True
    def buff(self):
        max_dmg = 35 if self.name.lower() == "crumbs" else 70
        print("You write a complaint to the game devs that you cant increase your damage...")
        if self.hp < 250:
           print("hi, game dev here! go get some fucking health first.")
           return None
        if self.damage >= max_dmg:
           print("pay for the premium subscription so you can gain theoritially infinite damage!")
           print("You hit the damage buff limit")
           return None
        else:
           print("i accept your offering.")
           print("You lose 250 hp, ouch! But the 15 additional damage is probably worth it")
           self.hit_player(250)
           self.damage += 15
           return  True
    def punish(self):
        print("you selfish imbecile, did your mother ever teach you manners?/srs \n  how do you feel about being an asshole, huh, how? just insulting things you don't like \n i think you should look into the mirror and reconsider your life decisions. \n how low do you need to get to insult a game... just... how low... \n oh well, thankfullly, this is MY game. and i WILL punish you. \n die, loser.")
        self.hit_player(99999999999999999)
        self.damage = 0
    def info_player(self):
        return self.name + ": " + str(self.damage)+ " damage. "+ str(self.hp)+ " Hitpoints left."
        

player = Player(player_name)
print(player.player_introduction())
enemy_unpicked = True
while enemy_unpicked:
    print("Pick your enemy")
    print("Mr. Beast, Dog")
    enemy_option = input("> ")
    match enemy_option.lower():
       case  "mr. beast" | "mr beast":
        enemy = Enemy(mrbeast_stats) 
        enemy_unpicked = False
       case "dog" | "the dog":
        enemy = Enemy(dog_stats)
        enemy_unpicked = False

print(enemy.enemy_introduction())




while running:
    while player_turn:
        print("What do you want to do?")
        print("[kick,gamble,sacrifice,heal,buff,info]")
        player_option = input("> ")
        match player_option.lower():
            case "kick":
                 enemy.hit_enemy(player.kick())
                 player_turn = False
            case "gamble":
                 enemy.hit_enemy(player.gambling())
                 player_turn = False
            case "sacrifice":
                 damage_to_be_dealt = player.sac()
                 if damage_to_be_dealt != None:
                    enemy.hit_enemy(damage_to_be_dealt)
                    player_turn = False
            case "heal":
                 if player.healing():
                  player_turn = False
            case "buff":
                if player.buff():
                   player_turn = False
            case "fuck you" | "kys":
                player.punish()
                player_turn = False
            case "info":
                 print(player.info_player())
                 print(enemy.info_enemy())
    enemy_turn = True
    if enemy.hp <= 0:
        print("No way!! You have succesfully killed the enemey!!!!! Good job!!!")
        break
    while enemy_turn:
        print("It's the enemy's turn now!")
        enemy_damage = enemy.enemey_attack_decider() 
        player.hit_player(enemy_damage)
        print(" ")
        enemy_turn = False
        player_turn = True
    if player.hp <= 0:
        print("Jesus Christ, how are you this bad? You loser. Imagine dying lmfaooooooooooo")
        break
print("The game ends here, thanks for trying out my little thing. Hope it was a fun time killer")
p = input("Press ENTER to quit")