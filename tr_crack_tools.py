import random
import string
import pyfiglet
import time,os
import requests
from colorama import Fore
import zipfile
import itertools
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import pyzipper
import pikepdf
import rarfile
import py7zr
import patoolib
from lzma import LZMAError

def home_menu():
    print(Fore.CYAN+f"\n[1] Bruteforce Password Generator\n")
    print(Fore.LIGHTBLUE_EX+"[2] Mobile Number Passlist Generator\n")
    print(Fore.GREEN+"[3] Pin Code Generator\n")
    print(Fore.YELLOW+"[4] Zip File Cracker\n")
    print(Fore.BLUE+"[5] Short Url\n")
    print(Fore.RED+"[0] Exit")

def back_home():
    back_home = input(f"\n{Fore.GREEN}[B] {Fore.WHITE}Back Home {Fore.RED}[E] {Fore.WHITE}Exit {Fore.LIGHTBLUE_EX}>>> {Fore.WHITE}").lower()
    if back_home == "b":
        main()
    elif back_home == "e":
        os._exit(0)

def banner():
    print(Fore.LIGHTMAGENTA_EX+"*"*75)
    text = pyfiglet.figlet_format("TR CRCAK TOOLS")
    print(Fore.YELLOW+text)
    print(Fore.LIGHTMAGENTA_EX+"*"*75)
    time.sleep(2)
def banner_2():
    text = pyfiglet.figlet_format("PASSWORD GENERATOR")
    print(Fore.BLUE+text)
def banner_3():
    text = pyfiglet.figlet_format("PHONE NUMBER GENERATOR")
    print(Fore.BLUE+text)
def banner_4():
    text = pyfiglet.figlet_format("PIN GENERATOR")
    print(Fore.BLUE+text)  
def banner_5():
    text = pyfiglet.figlet_format("SHORT URL") 
    print(Fore.BLUE+text) 
def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def bruteforce_password(first_name, middle_name, last_name,
                                           first_name_ca, 
                                           first_name_lo,
                                           first_name_ti,
                                           middle_name_ca,
                                           middle_name_lo,
                                           middle_name_ti,
                                           last_name_ca,
                                           last_name_lo,
                                           last_name_ti,
                                           phone_num,
                                           birth_day,
                                           birth_month,
                                           birth_year):
    passwords = []
    symbol_at = ("@")
    symbol_hash = ("#")
    symbol_and = ("&")
    
    passwords.append(f"{first_name}")
    passwords.append(f"{first_name_ca}")
    passwords.append(f"{first_name_lo}")
    passwords.append(f"{first_name_ti}")
    passwords.append(f"{first_name}{symbol_at}")
    passwords.append(f"{first_name_ca}{symbol_at}")
    passwords.append(f"{first_name_lo}{symbol_at}")
    passwords.append(f"{first_name_ti}{symbol_at}")
    passwords.append(f"{first_name}{symbol_hash}")
    passwords.append(f"{first_name_ca}{symbol_hash}")
    passwords.append(f"{first_name_lo}{symbol_hash}")
    passwords.append(f"{first_name_ti}{symbol_hash}")
    passwords.append(f"{first_name}{symbol_and}")
    passwords.append(f"{first_name_ca}{symbol_and}")
    passwords.append(f"{first_name_lo}{symbol_and}")
    passwords.append(f"{first_name_ti}{symbol_and}")
    if middle_name:
        passwords.append(f"{middle_name}")
        passwords.append(f"{middle_name_ca}")
        passwords.append(f"{middle_name_lo}")
        passwords.append(f"{middle_name_ti}")
        
    for zero in range (21):
        passwords.append("0"*zero)
        
    passwords.append(f"{last_name}")
    passwords.append(f"{last_name_ca}")
    passwords.append(f"{last_name_lo}")
    passwords.append(f"{last_name_ti}")
    passwords.append(f"{last_name}{symbol_at}")
    passwords.append(f"{last_name_ca}{symbol_at}")
    passwords.append(f"{last_name_lo}{symbol_at}")
    passwords.append(f"{last_name_ti}{symbol_at}")
    passwords.append(f"{last_name}{symbol_hash}")
    passwords.append(f"{last_name_ca}{symbol_hash}")
    passwords.append(f"{last_name_lo}{symbol_hash}")
    passwords.append(f"{last_name_ti}{symbol_hash}")
    passwords.append(f"{last_name}{symbol_and}")
    passwords.append(f"{last_name_ca}{symbol_and}")
    passwords.append(f"{last_name_lo}{symbol_and}")
    passwords.append(f"{last_name_ti}{symbol_and}")
    
    full_name_1 = f"{first_name}{middle_name}{last_name}" if middle_name else f"{first_name}{last_name}"
    passwords.append(f"{full_name_1}")
    passwords.append(f"{full_name_1.upper()}")
    passwords.append(f"{full_name_1.lower()}")
    passwords.append(f"{full_name_1.title()}")
    
    full_name_2 = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
    passwords.append(f"{full_name_2.upper()}")
    passwords.append(f"{full_name_2.lower()}")
    passwords.append(f"{full_name_2.title()}")
    
    ## NEW UPDATE 2.0
    if phone_num:
        passwords.append(f"{phone_num}")
        passwords.append(f"{first_name}{symbol_at}{phone_num}")
        passwords.append(f"{first_name}{symbol_hash}{phone_num}")
        passwords.append(f"{first_name}{symbol_and}{phone_num}")
        passwords.append(f"{last_name}{symbol_at}{phone_num}")
        passwords.append(f"{last_name}{symbol_hash}{phone_num}")
        passwords.append(f"{last_name}{symbol_and}{phone_num}")
        
    if birth_day:
        all_birth = (birth_day+birth_month+birth_year)
        passwords.append(f"{birth_day}")
        passwords.append(f"{birth_month}")
        passwords.append(f"{birth_year}")
        passwords.append(f"{all_birth}")  
        passwords.append(f"{birth_day}{birth_month}")
        passwords.append(f"{birth_month}{birth_year}")
        passwords.append(f"{birth_day}{birth_year}")
        passwords.append(f"{first_name}{phone_num}")
        passwords.append(f"{last_name}{phone_num}")
        passwords.append(f"{first_name}{birth_day}")
        passwords.append(f"{first_name}{birth_month}")
        passwords.append(f"{first_name}{birth_year}")
        passwords.append(f"{last_name}{birth_day}")
        passwords.append(f"{last_name}{birth_month}")
        passwords.append(f"{last_name}{birth_year}")
        
        passwords.append(f"{first_name}{symbol_at}{birth_day}")
        passwords.append(f"{first_name}{symbol_at}{birth_month}")
        passwords.append(f"{first_name}{symbol_at}{birth_year}")
        passwords.append(f"{first_name}{symbol_hash}{birth_day}")
        passwords.append(f"{first_name}{symbol_hash}{birth_month}")
        passwords.append(f"{first_name}{symbol_hash}{birth_year}")
        passwords.append(f"{first_name}{symbol_and}{birth_day}")
        passwords.append(f"{first_name}{symbol_and}{birth_month}")
        passwords.append(f"{first_name}{symbol_and}{birth_year}")
        passwords.append(f"{last_name}{symbol_at}{birth_day}")
        passwords.append(f"{last_name}{symbol_at}{birth_month}")
        passwords.append(f"{last_name}{symbol_at}{birth_year}")
        passwords.append(f"{last_name}{symbol_hash}{birth_day}")
        passwords.append(f"{last_name}{symbol_hash}{birth_month}")
        passwords.append(f"{last_name}{symbol_hash}{birth_year}")
        passwords.append(f"{last_name}{symbol_and}{birth_day}")
        passwords.append(f"{last_name}{symbol_and}{birth_month}")
        passwords.append(f"{last_name}{symbol_and}{birth_year}")

        passwords.append(f"{first_name}{all_birth}")
        passwords.append(f"{first_name}{symbol_at}{all_birth}")
        passwords.append(f"{first_name}{symbol_hash}{all_birth}")
        passwords.append(f"{first_name}{symbol_and}{all_birth}")
        passwords.append(f"{last_name}{all_birth}")
        passwords.append(f"{last_name}{symbol_at}{all_birth}")
        passwords.append(f"{last_name}{symbol_hash}{all_birth}")
        passwords.append(f"{last_name}{symbol_and}{all_birth}")
    
    if middle_name and birth_day:
        passwords.append(f"{middle_name}{phone_num}")
        passwords.append(f"{middle_name}{birth_day}")
        passwords.append(f"{middle_name}{birth_month}")
        passwords.append(f"{middle_name}{birth_year}")
        passwords.append(f"{middle_name}{symbol_at}{phone_num}")
        passwords.append(f"{middle_name}{symbol_hash}{phone_num}")
        passwords.append(f"{middle_name}{symbol_and}{phone_num}")
        passwords.append(f"{middle_name}{symbol_at}{birth_day}")
        passwords.append(f"{middle_name}{symbol_at}{birth_month}")
        passwords.append(f"{middle_name}{symbol_at}{birth_year}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_day}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_month}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_year}")
        passwords.append(f"{middle_name}{symbol_and}{birth_day}")
        passwords.append(f"{middle_name}{symbol_and}{birth_month}")
        passwords.append(f"{middle_name}{symbol_and}{birth_year}")
        passwords.append(f"{middle_name}{all_birth}")
        passwords.append(f"{middle_name}{symbol_at}{all_birth}")
        passwords.append(f"{middle_name}{symbol_hash}{all_birth}")
        passwords.append(f"{middle_name}{symbol_and}{all_birth}")

    for num in range(100001): 
        digit = str(num)  
        
        passwords.append(f"{first_name}{digit}")
        passwords.append(f"{first_name_ca}{digit}")
        passwords.append(f"{first_name_lo}{digit}")
        passwords.append(f"{first_name_ti}{digit}")
        
        #Symbol_firstname
        #symbol_hash = ("@") FIRSTNAME 
        passwords.append(f"{first_name}{symbol_at}{digit}")
        passwords.append(f"{first_name_ca}{symbol_at}{digit}")
        passwords.append(f"{first_name_lo}{symbol_at}{digit}")
        passwords.append(f"{first_name_ti}{symbol_at}{digit}")
        
        #symbol_hash = ("#") FIRSTNAME
        passwords.append(f"{first_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{first_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{first_name}{symbol_hash}{digit}")
        
        #symbol_and = ("&") FIRSTNAME
        passwords.append(f"{first_name_ca}{symbol_and}{digit}")
        passwords.append(f"{first_name}{symbol_and}{digit}")
        passwords.append(f"{first_name_lo}{symbol_and}{digit}")
        passwords.append(f"{first_name_ti}{symbol_and}{digit}")
        
        if middle_name: 
            passwords.append(f"{middle_name}{digit}")
            passwords.append(f"{middle_name_ca}{digit}")
            passwords.append(f"{middle_name_lo}{digit}")
            passwords.append(f"{middle_name_ti}{digit}")
            
            #Symbol_middlename
            # symbol_at = ("@") Middle Name
            passwords.append(f"{middle_name_ca}{symbol_at}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_at}{digit}")
            passwords.append(f"{middle_name}{symbol_at}{digit}")
            
            # symbol_hash = ("#")
            passwords.append(f"{middle_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{middle_name}{symbol_hash}{digit}")
            
            # symbol_and = ("&")
            passwords.append(f"{middle_name_ca}{symbol_and}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_and}{digit}")
            passwords.append(f"{middle_name}{symbol_and}{digit}")
            
            # Symbol FirstName+MiddleName
            passwords.append(f"{first_name}{middle_name}{symbol_at}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_at}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_at}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_at}{digit}")
            passwords.append(f"{first_name}{middle_name}{symbol_hash}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{first_name}{middle_name}{symbol_and}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_and}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_and}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_and}{digit}")
            
            #Special Symbol MiddleName+LastName
            passwords.append(f"{middle_name}{last_name}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_at}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_at}{digit}")
            passwords.append(f"{middle_name}{last_name}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{middle_name}{last_name}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_and}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_and}{digit}")
        
        #Symbol_lastname
        # symbol_at = ("@")
        passwords.append(f"{last_name_ca}{symbol_at}{digit}")
        passwords.append(f"{last_name_lo}{symbol_at}{digit}")
        passwords.append(f"{last_name_ti}{symbol_at}{digit}")
        passwords.append(f"{last_name}{symbol_at}{digit}")
        
        # symbol_hash = ("#")
        passwords.append(f"{last_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{last_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{last_name}{symbol_hash}{digit}")
        
        # symbol_and = ("&")
        passwords.append(f"{last_name_ca}{symbol_and}{digit}")
        passwords.append(f"{last_name_lo}{symbol_and}{digit}")
        passwords.append(f"{last_name_ti}{symbol_and}{digit}")
        passwords.append(f"{last_name}{symbol_and}{digit}")
        
        passwords.append(f"{last_name}{digit}")
        passwords.append(f"{last_name_ca}{digit}")
        passwords.append(f"{last_name_lo}{digit}")
        passwords.append(f"{last_name_ti}{digit}")
        
        full_name = f"{first_name}{middle_name}{last_name}" if middle_name else f"{first_name}{last_name}"
        passwords.append(f"{full_name}{digit}")
        passwords.append(f"{full_name.upper()}{digit}")
        passwords.append(f"{full_name.lower()}{digit}")
        passwords.append(f"{full_name.title()}{digit}")
        
        full_name_space = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
        passwords.append(f"{full_name_space}{digit}")
        passwords.append(f"{full_name_space.upper()}{digit}")
        passwords.append(f"{full_name_space.lower()}{digit}")
        passwords.append(f"{full_name_space.title()}{digit}")
        
        full_name_cap = f"{first_name.capitalize()}{middle_name.capitalize()}{last_name.capitalize()}" if middle_name else f"{first_name.capitalize()}{last_name.capitalize()}"
        passwords.append(f"{full_name_cap}{digit}")
        
        # Special Symbol FastName+LastName
        passwords.append(f"{first_name}{last_name}{symbol_at}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_at}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_at}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_at}{digit}")
        passwords.append(f"{first_name}{last_name}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{first_name}{last_name}{symbol_and}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_and}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_and}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_and}{digit}")
        
        # Special Symbol LastName+FirstName
        passwords.append(f"{last_name}{first_name}{symbol_at}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_at}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_at}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_at}{digit}")
        passwords.append(f"{last_name}{first_name}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{last_name}{first_name}{symbol_and}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_and}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_and}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_and}{digit}")
        passwords.append(f"{digit}") 
        passwords.append(f"{digit}{digit}")    
                         
    return passwords

def mobile_num_passlist(input_num):
    print(Fore.LIGHTGREEN_EX+"\nIt tooks take times depends on your device capability.")
    print(Fore.BLUE+"Wait Sometimes Generate 90M password.....................\n")
    file_name = (f"{input_num}_Passlist.txt")
    
    with open(file_name, "w") as passlist:
            for num in range(9999999, 99999999): ## 9999999, 99999999
                number_list = (f"{input_num}{num}")
                passlist.write(number_list + "\n")
                
    print(Fore.WHITE+"-"*50)
    print(Fore.MAGENTA+f"Password List Save to {Fore.YELLOW}'{file_name}'")
    print(Fore.WHITE+"-"*50)

def pin_generate_3digit(pin_digit):
    print(Fore.LIGHTGREEN_EX+"\nIt tooks take times depends on your device capability")
    print(Fore.BLUE+"Wait Sometimes..............\n")
    file_name = (f"{pin_digit}_Digit_Password_List.txt")
    with open(file_name, "w") as pin_list:
        for pass_list in range(1000):
            pin_list.write(f"{pass_list:03d}\n")
            
    print(Fore.WHITE+"-"*50)
    print(Fore.MAGENTA+f"Password List Save to {Fore.YELLOW}'{file_name}'")
    print(Fore.WHITE+"-"*50)


def pin_generate_4digit(pin_digit):
    print(Fore.LIGHTGREEN_EX+"\nIt tooks take times depends on your device capability")
    print(Fore.BLUE+"Wait Sometimes..............\n")
    file_name = (f"{pin_digit}_Digit_Password_List.txt")
    with open(file_name, "w") as pin_list:
        for pass_list in range(10000):
            pin_list.write(f"{pass_list:04d}\n")
            
    print(Fore.WHITE+"-"*50)
    print(Fore.MAGENTA+f"Password List Save to {Fore.YELLOW}'{file_name}'")
    print(Fore.WHITE+"-"*50)

def pin_generate_5digit(pin_digit):
    print(Fore.LIGHTGREEN_EX+"\nIt tooks take times depends on your device capability")
    print(Fore.BLUE+"Wait Sometimes..............\n")
    file_name = (f"{pin_digit}_Digit_Password_List.txt")
    with open(file_name, "w") as pin_list:
        for pass_list in range(100000):
            pin_list.write(f"{pass_list:05d}\n")
            
    print(Fore.WHITE+"-"*50)
    print(Fore.MAGENTA+f"Password List Save to {Fore.YELLOW}'{file_name}'")
    print(Fore.WHITE+"-"*50)

def pin_generate_6digit(pin_digit):
    print(Fore.LIGHTGREEN_EX+"\nIt tooks take times depends on your device capability")
    print(Fore.BLUE+"Wait Sometimes..............\n")
    file_name = (f"{pin_digit}_Digit_Password_List.txt")
    with open(file_name, "w") as pin_list:
        for pass_list in range(1000000):
            pin_list.write(f"{pass_list:06d}\n")
            
    print(Fore.WHITE+"-"*50)
    print(Fore.MAGENTA+f"Password List Save to {Fore.YELLOW}'{file_name}'")
    print(Fore.WHITE+"-"*50)

def pin_generate_7digit(pin_digit):
    print(Fore.LIGHTGREEN_EX+"\nIt tooks take times depends on your device capability")
    print(Fore.BLUE+"Wait Sometimes..............\n")
    file_name = (f"{pin_digit}_Digit_Password_List.txt")
    with open(file_name, "w") as pin_list:
        for pass_list in range(10000000):
            pin_list.write(f"{pass_list:07d}\n")
            
    print(Fore.WHITE+"-"*50)
    print(Fore.MAGENTA+f"Password List Save to {Fore.YELLOW}'{file_name}'")
    print(Fore.WHITE+"-"*50)
 
def pin_generate_8digit(pin_digit):
    print(Fore.LIGHTGREEN_EX+"\nIt tooks take times depends on your device capability")
    print(Fore.BLUE+"Wait Sometimes..............\n")
    file_name = (f"{pin_digit}_Digit_Password_List.txt")
    with open(file_name, "w") as pin_list:
        for pass_list in range(100000000):
            pin_list.write(f"{pass_list:08d}\n")
            
    print(Fore.WHITE+"-"*50)
    print(Fore.MAGENTA+f"Password List Save to {Fore.YELLOW}'{file_name}'")
    print(Fore.WHITE+"-"*50)

def save_to_file(passwords, filename="Custom_Passwordlist.txt"):
    with open(filename, "w") as file:
        for password in passwords:
            file.write(password + "\n")
            
    print(Fore.RED+"-"*60)       
    print(Fore.YELLOW+f"\nPassword list saved to {Fore.WHITE}'{filename}'\n")
    print(Fore.RED+"-"*60)

def url_generate(input_url):
    url_api = (f"http://tinyurl.com/api-create.php?url={input_url}")
    response = requests.get(f"{url_api}")
    if response.status_code == 200:
        return response.text
    else:
        print(Fore.RED+"\nURL NOT FOUND !!")
        time.sleep(3)
        main()
        
def main():
    cl()
    banner()
    home_menu()
    home_select = input(Fore.WHITE+f"\nChoose Option >>>> {Fore.LIGHTCYAN_EX}")
    
    if home_select == "1":
        cl()
        banner_2()
        first_name = input(Fore.CYAN+f"\nEnter Target First Name >>{Fore.GREEN} ").strip()
        middle_name = input(Fore.CYAN+f"Enter Target Middle Name {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ").strip()
        last_name = input(Fore.CYAN+f"Enter Target Last Name >>{Fore.GREEN} ").strip()
        
        first_name_ca = first_name.upper()
        first_name_lo = first_name.lower()
        first_name_ti = first_name.title()
        middle_name_ca = middle_name.upper()
        middle_name_lo = middle_name.lower()
        middle_name_ti = middle_name.title()
        last_name_ca = last_name.upper()
        last_name_lo = last_name.lower()
        last_name_ti = last_name.title()
        
        phone_num = input(Fore.CYAN+f"Target Phone Number {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ").strip()
        
        birth_day = input(Fore.CYAN+f"\nTarget Birth Day {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        birth_month = input(Fore.CYAN+f"Target Birth Month {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        birth_year = input(Fore.CYAN+f"Target Birth Year {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        
        case1 = random.choice(string.ascii_letters)
        case2 = random.choice(string.digits)
        random_case = (f"{first_name.upper()}_{case1}{case2}")
        
        file_name = (f"Passwordlist_{random_case}.txt")
        
        password_list = bruteforce_password(first_name, middle_name, last_name,
                                            first_name_ca, 
                                            first_name_lo,
                                            first_name_ti,
                                            middle_name_ca,
                                            middle_name_lo,
                                            middle_name_ti,
                                            last_name_ca,
                                            last_name_lo,
                                            last_name_ti,
                                            phone_num,
                                            birth_day,
                                            birth_month,
                                            birth_year)
        save_to_file(password_list, file_name)                                   
        back_home()
        
    elif home_select == "2":
        cl()
        banner_3()
        print(Fore.GREEN+"\n[A] Airtel\n[B] Banglalink\n[R] Robi\n[G] Grameenphone\n[H] Home")
        choose_network = input("\n>>> ").lower()
        if choose_network == "a":
            input_num = "016"
        elif choose_network == "b":
            input_num = "019"
        elif choose_network == "r":
            input_num = "018"
        elif choose_network == "g":
            input_num = "017"
        else:
            main()
        
        mobile_num_passlist(input_num)
        back_home()
    
    elif home_select == "3":
        cl()
        banner_4()
        print(Fore.YELLOW+"\n[ Enter value you wnat to generate pin code (ex: 3) get 3 digit pin code ]\n")
        pin_list = input(Fore.LIGHTCYAN_EX+"Enter Generate Pin Digits (3/4/5/6/7/8) >>> ")       
        if pin_list == "3":
            pin_digit = "3"
            pin_generate_3digit(pin_digit)
            back_home()
        elif pin_list == "4":
            pin_digit = "4"
            pin_generate_4digit(pin_digit)
            back_home()
        elif pin_list == "5":
            pin_digit = "5"
            pin_generate_5digit(pin_digit)
            back_home()
        elif pin_list == "6":
            pin_digit = "6"
            pin_generate_6digit(pin_digit)
            back_home()
        elif pin_list == "7":
            pin_digit = "7"
            pin_generate_7digit(pin_digit)
            back_home()
        elif pin_list == "8":
            pin_digit = "8"
            pin_generate_8digit(pin_digit)
            back_home()
        else:
            main()

    elif home_select == "0":
        print("\nEXIT DONE \n")
        os._exit(0) 
    
    elif home_select == "5":
        cl()
        banner_5()
        input_url = input(Fore.MAGENTA+f"\nEnter Long Url >>> {Fore.LIGHTWHITE_EX}")   
        short_url = url_generate(input_url)
        time.sleep(2)
        cl()
        print(Fore.WHITE+"-"*50)
        print(Fore.LIGHTYELLOW_EX+f"Short Url: {Fore.LIGHTCYAN_EX}{short_url}")
        print(Fore.WHITE+"-"*50)
        back_home()
        

    elif home_select == "4":
        cl()
        banner()
        def extract_zip(zip_path, password):
            try:
                with pyzipper.AESZipFile(zip_path) as zip_ref:
                    zip_ref.extractall(pwd=password.encode('utf-8'))
                    return True
            except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
                return False
            except Exception as e:
                return False

        def extract_pdf(pdf_path, password):
            try:
                with pikepdf.open(pdf_path, password=password):
                    return True
            except pikepdf._qpdf.PasswordError:
                return False
            except Exception as e:
                return False

        def extract_rar(rar_path, password):
            try:
                with rarfile.RarFile(rar_path) as rar_ref:
                    rar_ref.extractall(pwd=password)
                    return True
            except rarfile.BadRarFile:
                return False
            except Exception as e:
                return False

        def extract_7z(seven_zip_path, password):
            try:
                with py7zr.SevenZipFile(seven_zip_path, password=password) as seven_zip_ref:
                    seven_zip_ref.extractall()
                    return True
            except (py7zr.exceptions.CrcError, py7zr.exceptions.Bad7zFile, EOFError, LZMAError, RuntimeError):
                return False
            except Exception as e:
                return False

        def extract_with_patool(file_path, password, archive_type):
            try:
                patoolib.extract_archive(file_path, outdir='.', password=password)
                return True
            except Exception as e:
                return False

        def dictionary_attack(file_path, password_list_path, file_type):
            with open(password_list_path, 'r') as password_file:
                for line in password_file:
                    password = line.strip()
                    status_label.config(text=f"Trying password: {password}")
                    root.update()
                    if file_type == 'zip' and extract_zip(file_path, password):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
                    elif file_type == 'pdf' and extract_pdf(file_path, password):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
                    elif file_type == 'rar' and extract_rar(file_path, password):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
                    elif file_type == '7z' and extract_7z(file_path, password):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
                    elif file_type in ['gzip', 'bzip2', 'tar', 'wim', 'xz'] and extract_with_patool(file_path, password, file_type):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
            messagebox.showinfo("Failure", "Password not found in the dictionary.")

        def brute_force_attack(file_path, max_length, file_type):
            characters = string.ascii_letters + string.digits + string.punctuation
            for length in range(1, max_length + 1):
                for password in itertools.product(characters, repeat=length):
                    password = ''.join(password)
                    status_label.config(text=f"Trying password: {password}")
                    root.update()
                    if file_type == 'zip' and extract_zip(file_path, password):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
                    elif file_type == 'pdf' and extract_pdf(file_path, password):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
                    elif file_type == 'rar' and extract_rar(file_path, password):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
                    elif file_type == '7z' and extract_7z(file_path, password):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
                    elif file_type in ['gzip', 'bzip2', 'tar', 'wim', 'xz'] and extract_with_patool(file_path, password, file_type):
                        messagebox.showinfo("Success", f"Password found: {password}")
                        return
            messagebox.showinfo("Failure", "Password not found using brute force.")

        def select_file():
            selected_file = filedialog.askopenfilename(filetypes=[("All supported files", "*.zip *.pdf *.rar *.7z *.gz *.bz2 *.tar *.wim *.xz")])
            if selected_file:
                file_extension = os.path.splitext(selected_file)[1].lower()
                if file_extension in ['.zip', '.pdf', '.rar', '.7z', '.gz', '.bz2', '.tar', '.wim', '.xz']:
                    file_path.set(selected_file)
                    file_label.config(text=f"Selected file: {file_path.get()}")
                    if file_extension == '.zip':
                        file_type.set('zip')
                    elif file_extension == '.pdf':
                        file_type.set('pdf')
                    elif file_extension == '.rar':
                        file_type.set('rar')
                    elif file_extension == '.7z':
                        file_type.set('7z')
                    elif file_extension == '.gz':
                        file_type.set('gzip')
                    elif file_extension == '.bz2':
                        file_type.set('bzip2')
                    elif file_extension == '.tar':
                        file_type.set('tar')
                    elif file_extension == '.wim':
                        file_type.set('wim')
                    elif file_extension == '.xz':
                        file_type.set('xz')
                else:
                    messagebox.showerror("Invalid File", "The selected file is not supported. Please select a supported file.")
            else:
                messagebox.showerror("Invalid File", "No file selected.")

        def select_password_file():
            selected_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if selected_file:
                password_list_path.set(selected_file)
                password_label.config(text=f"Selected Password file: {password_list_path.get()}")

        def start_cracking():
            if file_path.get() and password_list_path.get():
                start_time = time.time()
                threading.Thread(target=dictionary_attack, args=(file_path.get(), password_list_path.get(), file_type.get())).start()
                end_time = time.time()
                status_label.config(text=f"Total time taken: {end_time - start_time:.2f} seconds")
            else:
                messagebox.showwarning("Input Required", "Please select both a file and a password list")

        root = tk.Tk()
        root.title("TR CRACK TOOL (Zip Cracker)")

        file_path = tk.StringVar()
        password_list_path = tk.StringVar()
        file_type = tk.StringVar()

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(padx=10, pady=10)

        file_button = tk.Button(frame, text="Select File", command=select_file)
        file_button.grid(row=0, column=0, padx=5, pady=5)

        file_label = tk.Label(frame, text="No file selected")
        file_label.grid(row=0, column=1, padx=5, pady=5)

        password_button = tk.Button(frame, text="Select Password File", command=select_password_file)
        password_button.grid(row=1, column=0, padx=5, pady=5)

        password_label = tk.Label(frame, text="No password file selected")
        password_label.grid(row=1, column=1, padx=5, pady=5)

        start_button = tk.Button(frame, text="Start Cracking", command=start_cracking)
        start_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        status_label = tk.Label(frame, text="Status: Waiting to start")
        status_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        root.mainloop()
        back_home()    
      

                
if __name__ == "__main__":
    main()
