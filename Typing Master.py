from random import *
from threading import Timer

def welcome():
    print("WELCOME TO TYPING SPEED TEST")
    global Q
    Q = "-----------------------------------"
    print(Q)

def generate_word():
    A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"]
    global w
    w = ""
    y= sample(A,randrange(1,10))


    for i in y:
        w += i
    print(f'Here Is The Word :  {w}')

def game():

    welcome()

    while True:

        play = input("WANNA PLAY( Y OR N ) : ")
        if play.upper() == "Y":
            marks = 0

            while True:
                generate_word()
                time_interval = len(w)
                t = Timer(time_interval,print,["TIMES UPP......."])

                t.start()
                x = str(input("Type The Word    : "))
                t.cancel()

                if x.upper()==w:
                    marks +=10
                    print(Q)
                    print(f'CONGRATS YOU WON | YOUR MARKS : {marks}')
                    print(Q)
                elif x.upper() == "*":
                    break
                else:
                    if marks == 0:
                        print(Q)
                        break
                    else:
                        marks -= 10

                    print(Q)
                    print(f'OOPS ! YOU WRONG | YOUR MARKS : {marks}')
                    print(Q)

            print(f'GAME OVER ! YOUR MARKS : {marks}')
            z = input("THANK YOU ! WANNA PLAY AGAIN ? Y OR N : ")

            if z.upper() == "Y":
                print(Q)
                game()

            else:
                print(Q)
                print("HAVE A NICE DAY HOMIE....!")
                break

            break

        elif play.upper() == "N":
            print(Q)
            print("HAVE A NICE DAY HOMIE....!")
            break

        else:
            continue


game()