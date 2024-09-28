import random as r
import math as m
import sys
import time as t
import os
gold=0
hp=40
maxhp=40
def death():
    if hp<=0:
        print(""" ____  ____   ___   _____  _____   ______   _____  ________  ______    
|_  _||_  _|.'   `.|_   _||_   _| |_   _ `.|_   _||_   __  ||_   _ `.  
  \ \  / / /  .-.  \ | |    | |     | | `. \ | |    | |_ \_|  | | `. \ 
   \ \/ /  | |   | | | '    ' |     | |  | | | |    |  _| _   | |  | | 
   _|  |_  \  `-'  /  \ \__/ /     _| |_.' /_| |_  _| |__/ | _| |_.' / 
  |______|  `.___.'    `.__.'     |______.'|_____||________||______.'  
                                                                       """)
        sys.exit()
print("welcome to Curse of Strad")
print("transcribed to python by Alex")
print("Choose a class 1. Barbarian 2. Bard 3. Fighter 4. Ranger")
playerclass=input("Select 1,2,3,4 ")
def playerclassselect():
    if playerclass=="1":
        print("Barbarian selected")
        meeleattackdmg=r.randint(2,16)+7
        magicattackdmg=r.randint(2,5)
        swordattackdmg=meeleattackdmg+10-r.randint(5,10)
    elif playerclass=="2":
        print("Bard selected")
        meeleattackdmg=r.randint(1,8)-1
        magicattackdmg=r.randint(12,20)
        swordattackdmg=meeleattackdmg+5
    elif playerclass=="3":
        meeleattackdmg=r.randint(2,16)+2
        magicattackdmg=r.randint(2,5)
        swordattackdmg=meeleattackdmg+10
        print("Fighter selected")
    elif playerclass=="4":
        print("Ranger selected")
        meeleattackdmg=r.randint(2,10)
        magicattackdmg=r.randint(2,12)
        swordattackdmg=meeleattackdmg+5
    else:
        playerclassselectbackup()
def playerclassselectbackup():
    playerclass=input("Select 1,2,3,4 ")
    if playerclass=="1":
        print("Barbarian selected")
        meeleattackdmg=r.randint(2,16)+7
        magicattackdmg=r.randint(2,5)
        swordattackdmg=meeleattackdmg+10-r.randint(5,10)
    elif playerclass=="2":
        print("Bard selected")
        meeleattackdmg=r.randint(1,8)-1
        magicattackdmg=r.randint(12,20)
        swordattackdmg=meeleattackdmg+5
    elif playerclass=="3":
        meeleattackdmg=r.randint(2,16)+2
        magicattackdmg=r.randint(2,5)
        swordattackdmg=meeleattackdmg+10
        print("Fighter selected")
    elif playerclass=="4":
        print("Ranger selected")
        meeleattackdmg=r.randint(2,10)
        magicattackdmg=r.randint(2,12)
        swordattackdmg=meeleattackdmg+5
    else:
        playerclassselect()
def playerclassselectnewint():
    if playerclass=="1":
        meeleattackdmg=r.randint(2,16)+7
        magicattackdmg=r.randint(2,5)
        swordattackdmg=meeleattackdmg+10-r.randint(5,10)
        return meeleattackdmg,magicattackdmg,swordattackdmg
    elif playerclass=="2":
        meeleattackdmg=r.randint(1,8)-1
        magicattackdmg=r.randint(12,20)
        swordattackdmg=meeleattackdmg+5
        return meeleattackdmg,magicattackdmg,swordattackdmg
    elif playerclass=="3":
        meeleattackdmg=r.randint(2,16)+2
        magicattackdmg=r.randint(2,5)
        swordattackdmg=meeleattackdmg+10
        return meeleattackdmg,magicattackdmg,swordattackdmg
    elif playerclass=="4":
        meeleattackdmg=r.randint(2,10)
        magicattackdmg=r.randint(2,12)
        swordattackdmg=meeleattackdmg+5
        return meeleattackdmg,magicattackdmg,swordattackdmg
    else:
        playerclassselect()
playerclassselect()
print("you wake up in a strange forest")
input("Choose a direction North,West,South,East ")
print("you come across a road")
print("you head down the road")
print("you encounter 2 barbarians ")
hostile="The barbarians"
hostilehp=30
dmg1=15
dmg2=20
hostiledamage=r.randint(dmg1,dmg2) 
def liveattack():
    hostiledamage=r.randint(dmg1,dmg2)   
    hp,hostilehp=liveattack()
    playerclassselectnewint()
    meeleattackdmg,magicattackdmg,swordattackdmg=playerclassselectnewint()
    print("1. Melee 2. Magic 3. Sword")
    liveattackselect=input("Select 1,2,3 ")
    if liveattackselect=="1":
        print(hostile+" attacks you and deals "+ str(hostiledamage)+ " damage. You are at "+ str(hp-hostiledamage))
        hp=hp-hostiledamage
        hostiledamage=r.randint(dmg1,dmg2)   
        print("You hit back and deal" +str(meeleattackdmg)+" damage" )
        hostilehp=hostilehp-hostiledamage
        death()
        if hostilehp>0:
            return hp,hostilehp
            liveattack()
        else:
            print("you kill  "+ hostile)
    elif liveattackselect=="2":
        print("The "+hostile+" attacks you and deals "+ str(hostiledamage)+ " damage. You are at "+ str(hp-hostiledamage))
        hp=hp-hostiledamage
        hostiledamage=r.randint(dmg1,dmg2)   
        print("You hit back and deal" +str(meeleattackdmg)+" damage" )
        hostilehp=hostilehp-hostiledamage
        death()
        return hp,hostilehp
        if hostilehp>0:
            print("again")
            liveattack()
        else:
            print("you kill  "+ hostile)
    elif liveattackselect=="3":
        print("The "+hostile+" attacks you and deals "+ str(hostiledamage)+ " damage. You are at "+ str(hp-hostiledamage))
        hostiledamage=r.randint(dmg1,dmg2)   
        print("You hit back and deal" +str(swordattackdmg)+" damage" )
        death()
        if hostilehp>0:
            liveattack()
        else:
            print("you kill  "+ hostile)
    else:
        liveattack()
liveattack()
print(" You see the doors of a town\n The town of Barovia")
print("you walk inside and see 1. a tavern 2. a house 3. a manor \nand 4. a church")
def Baroviaselect():
    blv=input("Select 1,2,3,4 ")
    if blv=="1":
        ismarkquest=True
        print("""You enter the tavern a man walks up to you and 
        offers to pay for your drinks. He tells you his name is 
        Ismark and he says\"Please help me I need you to escort my sister to
        Valaki. You can find her in the Church\"""")
        yn=input("do you want to break it down y/n")
        if yn == "yes" or "Yes" or "y" or "Y":
            print("You are now healed "+str(hp*0+maxhp))
        Baroviaselect()
    elif blv=="2":
        print("The door is locked")
        yn=input("do you want to break it down y/n")
        if yn == "yes" or "Yes" or "y" or "Y":
            print("you found 15 gold you now have " +str(gold+15)+" gold")
            Baroviaselect()
        else:
            Baroviaselect()
    elif blv=="3":
        if ismarkquest==True:
            print("You walk up to the manor you see a garden that was once pretty\n now reduced to dead flowers as you walk closer you claw marks on the boarded up windows.\n once you get to the door you knock and someone who must be Ismarks sister ")
            print("She introduces herself as Ireena. She invites you in and \ntells you that she will go with you if you carry her dead father to the Church.\n stuned you agree")
            deadfather=True
            Baroviaselect()
        else:
            print("you see someone on the other side of the door but they do not let you in.")
            Baroviaselect()
    elif blv=="4":
        if deadfather==True:
            print("As you walk up holding the coffin Irrena unlocks the door to the church.\nYou hear someone screaming downstairs and run down there you see a zombie and he trys to attack you")
            hostile="The Deranged zombie"
            hostilehp=5
            def currentdmg():
                damage=r.randint(1,10)
            liveattack()
            print("after killing the zombie you find a sword in the zombies cold hands.\nYou take it\n After that you burry the father and leave for Valaki")
            
    else: 
        print("The doors are covered in chains and you cannot enter")
        Baroviaselect()
Baroviaselect()
print("you walk to Valaki but run into a fortune teller on the way")
print("she offers you food and a fortune")
print("\n\n\n")
t.sleep(3)
print("\"The land of Barovia has been troubled by evil you have the weapon needed to beat Strad\n now you must find your ally in the mountains and then find Strad\"")
print("you leave and are ambushed")
hostile="zombies"
hostilehp=40
def currentdmg():
    damage=r.randint(5,15)
liveattack()
print("you safely make it to Valaki")
print("you hear shouting in the square.")
print("you see what looks to be a protest")
yn=input("do you want to go to the inn y/n")
if yn == "yes" or "Yes" or "y" or "Y":
    print("you arrive at the inn safely and go to sleep")
else:
    print("the protest turns violent the croud riots many are killed in the stampede")
    hp=0
    death()

    



