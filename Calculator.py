import time
import os
import pyfiglet
from colorama import Fore, Back, Style
 
def logo():
    logo = pyfiglet.figlet_format('Calculator')
    print(Fore.LIGHTMAGENTA_EX + logo)
    

def add():
    num1 = int(input('Enter number 1 ->> '))
    num2 = int(input('Enter number 2 ->> '))
    print('Your result is ->>', num1+num2)
    time.sleep(2.5)
    
def sub():
    num1 = int(input('Enter number 1 ->> '))
    num2 = int(input('Enter number 2 ->> '))
    print('Your result is ->>', num1-num2)
    time.sleep(2.5)

def mult():
    num1 = int(input('Enter number 1 ->> '))
    num2 = int(input('Enter number 2 ->> '))
    print('Your result is ->>', num1*num2)
    time.sleep(2.5)

def div():
    num1 = int(input('Enter number 1 ->> '))
    num2 = int(input('Enter number 2 ->> '))
    print('Your result is ->>', num1/num2)
    time.sleep(2.5)


def calculate():
    os.system('cls')
    logo()
    action = str(input('''Choose an action: Add(a)
                  Sub(s)
                  Mult(m)
                  Div(d) 
                  -->> '''))
    os.system('cls')
    logo()
    
    if action == 'a':
        add()
    elif action == 's':
        sub() 
    elif action == 'm':
        mult()
    elif action == 'd':
        div()
    os.system('cls')



while True:
    calculate()