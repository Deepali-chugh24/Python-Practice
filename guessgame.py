# from curses import KEY_ENTER
import random
# from pynput import keyboard
# keyboard.press_and_release(hotkey: _ParseableHotkey, do_press: bool = True, do_release: bool = True)
# combination=[{keyboard.Key.enter}]
# current=set()
# def execute():
#    print("Enter to start ")
# def on_presskey():
#       if ([KEY_ENTER in combination]):
#             execute()
a=int(input("First number "))
b=int(input("Second number "))
i=random.randint(a,b)
print(i)
print("You will only get 8 chances ")
for d in range(8):
       c=int(input("Guess the number:- "))
       if c==i:
            print("You Guessed right number  ") 
            print(f"You did it in {d} try") 
            break
       if c>i:
             print("You Guessed too High")
       if c<i:
             print("You Guessed too Low")      
       else:
             print("Try Again")
             if d==7:
                   print("You only have single chance left")
else:
      print("Better luck next time")      
            