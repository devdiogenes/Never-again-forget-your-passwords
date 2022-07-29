import pyperclip
import cryptocode
import getpass

class NeverAgainForgetYourPasswords:
    def __init__(self): 
        self.__master_pw = self.__ask_master_pw()
        self.__pw = ""
        self.__encrypted_pw = ""

    def __ask_master_pw(self):
        master_pw = False
        while master_pw == False:
            try1 = getpass.getpass("\nType the master password... \n>")
            try2 = getpass.getpass("Type the master password again... \n>")
            if try1 == try2:
                master_pw = try1
            else: 
                master_pw = False
                print("\nTry again... \n")
        return master_pw    

    def __encrypt(self): 
        self.__pw = input("\nType the password you want to encrypt... \n>")
        self.__encrypted_pw = cryptocode.encrypt(self.__pw, self.__master_pw)
        input("\nEncrypted password: " + self.__encrypted_pw + "\nPress Enter to copy...\n")
        pyperclip.copy(self.__encrypted_pw)
        self.__encrypt_or_decrypt()

    def __decrypt(self):
        input("\nCopy the password you want to decrypt, then, press Enter...")
        self.__encrypted_pw = pyperclip.paste()
        print("\nEncrypted password: " + self.__encrypted_pw)
        try: 
            pw = cryptocode.decrypt(self.__encrypted_pw , self.__master_pw)
            input("Uncrypted password: " + pw + " \nPress Enter to copy... \n")
            pyperclip.copy(pw)
            self.__encrypt_or_decrypt()
        except: 
            print("\n\nWrong password! Try again...\n\n")
            self.__decrypt()

    def __encrypt_or_decrypt(self):
        print("\nDo you want...")
        print("1 - Save a new password?...")
        print("2 - Remember a password you have already save?...")
        result = input(">...")
        if result == "1":
            self.__encrypt()
        elif result == "2":
            self.__decrypt()
        else: 
            print("")
            self.__encrypt_or_decrypt()

    def run(self):
        self.__encrypt_or_decrypt()


NeverAgainForgetYourPasswords().run()