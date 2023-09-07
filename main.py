from colorama import Fore, Style
import pickle

try:
    with open("contacts.pkl", "rb") as file:
        contacts = pickle.load(file)
except EOFError:
    contacts = {}
except FileNotFoundError:
    print(Fore.RED + "File 'contacts.pkl' not found. Creating a new contact list." + Style.RESET_ALL)
    contacts = {}

print(Fore.BLUE + """
       _____ ____  _   _ _______       _____ _______ _____ 
      / ____/ __ \| \ | |__   __|/\   / ____|__   __/ ____|
     | |   | |  | |  \| |  | |  /  \ | |       | | | (___  
     | |   | |  | | . ` |  | | / /\ \| |       | |  \___ \ 
     | |___| |__| | |\  |  | |/ ____ \ |____   | |  ____) |
      \_____\____/|_| \_|  |_/_/    \_\_____|  |_| |_____/ 
                                                      
    Please, choose one of the options:

    [0]. Show all contacts
    [1]. Find a number
    [2]. Add a number
    [3]. Delete a number
    [4]. Rename the contact
    [5]. Quit
    """ + Style.RESET_ALL)

try:
    while True:

        option = int(input(Fore.GREEN + "Your option: " + Style.RESET_ALL))

        if option == 0:
            if contacts:
                for key, value in contacts.items():
                    print(f"{key}: {value}")
                continue
            else:
                print(Fore.RED + """
                                There list is empty!
                                Please, add some numbers by clicking [2]...
                                """ + Style.RESET_ALL)
                continue

        if option == 1:
            name = input("Name: ")

            if name in contacts:
                print(f"{name}: {contacts[name]}")
                continue
            else:
                print(Fore.RED + """
                There is no such name in contacts!
                Please, correct your prompt or add a number by clicking [2]...
                """ + Style.RESET_ALL)
                continue

        if option == 2:
            name = input("Name: ")
            number = input("Number: ")
            contacts[name] = number
            print(Fore.MAGENTA + f"Added '{name}' with number '{number}'." + Style.RESET_ALL)
            continue

        if option == 3:
            delete_name = input("Name to delete: ")
            try:
                if delete_name in contacts:
                    num_print = contacts[delete_name]
                    del contacts[delete_name]
                    print(Fore.YELLOW + f"The '{delete_name}' with the '{num_print}' number was successfully deleted!" + Style.RESET_ALL)
                    continue
                else:
                    print(Fore.RED + f"No contact found with the name '{delete_name}'." + Style.RESET_ALL)
                    continue
            except:
                print(Fore.RED + "Something went wrong! Please, try again!" + Style.RESET_ALL)
                continue

        if option == 4:
            try:
                old_name = input("Old name: ")
                if old_name in contacts:
                    number = contacts[old_name]
                    new_name = input("New name: ")

                    del contacts[old_name]
                    contacts[new_name] = number
                    print(Fore.MAGENTA + f"The '{old_name}' name was changed to the '{new_name}'!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"No contact found with the name '{old_name}'." + Style.RESET_ALL)
                    continue
            except:
                print(Fore.RED + "Something went wrong! Please, try again!" + Style.RESET_ALL)
                continue

        if option == 5:
            with open("contacts.pkl", "wb") as file:
                pickle.dump(contacts, file)
            print(Fore.CYAN + "Data saved! Goodbye!" + Style.RESET_ALL)
            break

except KeyboardInterrupt:
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contacts, file)
    print(Fore.RED + " \n\n| Data saved! See you again :) |" + Style.RESET_ALL)