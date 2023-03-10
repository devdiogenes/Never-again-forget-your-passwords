import pyperclip
import cryptocode
import getpass
import json
from model import ModelNeverAgainForgetYourPasswords

class NeverAgainForgetYourPasswords(ModelNeverAgainForgetYourPasswords):
    def __init__(self): 
        self.__master_pw = False
        self.__pw = ""
        self.__encrypted_pw = ""
        self.__model = ModelNeverAgainForgetYourPasswords()
        self.__model.__init__()

    def __login(self):
        registered = self.__model._check_register()
        while not registered:
            try1 = getpass.getpass("\nCreate a master password. It will be used to decrypt the passwords you will save here...\n")
            try2 = getpass.getpass("Repeat the master password you just created...\n")
            if try1 == try2:
                input("Master password set successfully")
                self.__model._register(try1)
                registered = True
            else:
                print("The passwords are different. Try again...")

        while self.__master_pw == False:
            self.__master_pw = self.__model._try_login(getpass.getpass("\nType the master password... \n>")) #Run ask for master pw while it's wrong

    def __encrypt(self): 
        pw = input("\nType the password you want to save... \n>")
        encrypted_pw = cryptocode.encrypt(pw, self.__master_pw)
        description = input("\nNow type a description for this password\n")
        self.__model._add_pass(encrypted_pw, description)
        print("Password saved successfully")

    def __decrypt(self):
        passwords = self.__model._get_passwords()
        sorted_passwords = sorted(self.__model._get_passwords())
        print("\nChoose a password: ")
        for index, password in enumerate(sorted_passwords):
            print(str(index) + " - " + password)
        choosen_pw_number = input()
        try:
            encrypted_pw = passwords[sorted_passwords[int(choosen_pw_number)]]
            pw = cryptocode.decrypt(encrypted_pw , self.__master_pw)
            input("Uncrypted password: " + pw + " \nPress Enter to copy... \n")
            pyperclip.copy(pw)
        except: 
            print("\nInvalid option! Try again...\n")
            self.__decrypt()

    def __encrypt_or_decrypt(self):
        result = "0"
        while result in ["0", "1", "2", "3"]:
            print("\nChoose an option...")
            print("1 - Save a new password")
            print("2 - Remember a password you have already save")
            print("3 - Exit")
            result = input(">...")
            if result == "1":
                self.__encrypt()
            elif result == "2":
                self.__decrypt()
            elif result == "3":
                quit()
            else: 
                result = "0"

    def run(self):
        self.__login()
        self.__encrypt_or_decrypt()


NeverAgainForgetYourPasswords().run()