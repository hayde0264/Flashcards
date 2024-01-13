import json 
import os
from colorama import Fore, Style


with open("1.json", "r") as in_file: 
    data = json.load(in_file)



if __name__ == "__main__": 
    if (os.path.exists("./missed.txt")): 
        open("./missed.txt", "w").close()

    remaining = len(data)
    ptr = 0
    outdata = {}
    correct = 0 
    missed = 0 
    total = len(data)
    
    while (remaining!=0):
        question = data[ptr]["question"]
        answer = data[ptr]["answer"]
        # opening line (Question)
        print( int(len(question) + 9) * '-')
        # second line (Question) 
        print( "|" +  
            (" " * 4) + Fore.RED + 
            data[ptr]["question"] + Style.RESET_ALL + 
            (" " * 3) + 
            '|') 
        # closing line (Question)
        print((len(data[ptr]["question"]) + 9) *'-')
        view_answer = input()
        print(Fore.MAGENTA + (data[ptr]["answer"]))
        print(Style.RESET_ALL)
        print("-"*28) 
        print("|" + (" " * 4) + Fore.CYAN + "Did you know this?" + (" " * 4) + Style.RESET_ALL + "|")
        print('|' + (" " * 6) + Fore.GREEN + "If so, enter" + Style.RESET_ALL + (" " * 8) + "|")
        print(Style.RESET_ALL + "|" + (" " * 11) +Fore.YELLOW + "y/n" + Style.RESET_ALL + (" " * 12) + "|") 
        print(Style.RESET_ALL + ("-"*28))

        knows = input()
        while (True): 
            if (knows=='y' or knows=='n'): 
                break
            else:
                print( Fore.RED + "please enter y or n" + Style.RESET_ALL)
                knows = input()

        if (knows == 'n'): 
            missed+=1 
            if (os.path.exists("./missed.txt")): 
                with open("./missed.txt", "a") as out_file: 
                    out_file.write(f"{question}\n{answer}\n\n")
            else: 
               with open("./missed.txt", "w")  as out_file: 
                   out_file.write(f"{question}\n{answer}\n\n")

            
            

        print('\n')
        ptr+=1
        remaining-=1
        os.system('cls' if os.name == 'nt' else 'clear')
