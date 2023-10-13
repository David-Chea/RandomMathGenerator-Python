import random
from time import time
from colorama import Fore

import sys, subprocess

import os
os.system("cls||clear")

def clear_prompt():
    operating_system = sys.platform
    
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
        
    if operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear, shell=True')

score = 1
ques_correct = 1
ques_incorrect = 1
total_right_answer_seconds = 0.00
question = 1

while True:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    
    
    
    start_time = time()
    ans = x * y
    response = int(input(f"{Fore.LIGHTBLUE_EX}What is " + str(x) + " x " + str(y) + f" ?\n  {Fore.LIGHTMAGENTA_EX}Answer: {Fore.LIGHTWHITE_EX}"))
    elapsed_time = time() - start_time
    average_time = (total_right_answer_seconds/ques_correct)
    
    stats = (f"{Fore.LIGHTCYAN_EX}Score - ({score}), Current Question - ({question}), Correct/Inccorect - ({Fore.LIGHTGREEN_EX}{ques_correct}{Fore.LIGHTWHITE_EX}/{Fore.RED}{ques_incorrect}{Fore.LIGHTWHITE_EX}), Correct Average time - ({average_time:.2f})")
    
    clear_prompt()
    
    if response == ans:
        score += 1
        ques_correct +=1
        question += 1
        total_right_answer_seconds += elapsed_time
        print(f"{Fore.LIGHTGREEN_EX}Correct! You took {elapsed_time:.2f} seconds, {stats}")
    else:
        score -= 1
        ques_incorrect +=1
        question += 1
        print(f"{Fore.RED}Incorrect, You took {elapsed_time:.2f} seconds, {stats}")