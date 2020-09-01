import pyautogui
import time
import winsound
import sys
import keyboard


def key_detection():
    print("Appuyez sur la touche 's' pour demarrer le program, \nAppuyez deux fois sur Ctrl + c pour annuler !")
    while True:
        try: 
            if keyboard.is_pressed("s"):
                print('Lancement au cours .... \b')
                frequency = 5000  
                duration = 500 
                winsound.Beep(frequency, duration)
                break 
            else:
                pass
        except:
            break  


def lauch():
    launching_time = 5
    while launching_time != 1:
        print("launching in " + str(launching_time))
        launching_time -= 1
        time.sleep(1)


def spam():
    f = open("skwal", 'r')
    for word in f:
        print(word)
        pyautogui.typewrite(word)
        pyautogui.press("enter")


def main():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    key_detection()
    lauch()
    spam()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting.... \nBye !")
        sys.exit()
        exit()
