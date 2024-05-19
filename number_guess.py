import random
import time
number=random.randint(1, 200)
#safůwodfnikdsa

#asdflwpniekd
def intro():
    print("Jak se jmenuješ?")
    name=input() 
    print(name + ", zahrajeme si hru. Myslím si číslo od 1 do 200.")
    time.sleep(.5)
    print("Tak pojď. Hádej.")
#asdlfwpndidkwl
def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
        enter=input("Hádané číslo: ") 
        try: 
            guess = int(enter)

            if guess<=200 and guess>=1: 
                guessesTaken=guessesTaken+1 
                if guessesTaken<6:
                    if guess<number:
                        print("Číslo, které musíš uhodnout je větší.")
                    if guess>number:
                        print("Číslo, které musíš uhodnout je menší.")
                    if guess != number:
                        #asdflkwdnifniak
                        time.sleep(.5)
                        print("Zkus to znova.")
                if guess==number:
                    break 
            if guess>200 or guess<1:
                print("Říkal jsem od 1 do 200.")
                time.sleep(.25)
                print("Prosím zadej tedy číslo od 1 do 200.")

        except: 
            print("Nemyslím si že, "+enter+" je číslo.")
            
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Dobrá práce, ' + name + '! Uhádl si číslo na ' + guessesTaken + ' pokusů!')

    if guess != number:
        print('Bohužel číslo, které jsi musel/a uhodnout bylo: ' + str(number))
#asldfkjownodf

playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    intro()
    pick()
    print("Chceš si zahrát znova?")
    playagain=input()
