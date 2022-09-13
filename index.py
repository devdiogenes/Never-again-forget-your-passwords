import pyperclip
import cryptocode
import getpass
import json

class DatabaseNeverAgainForgetYourPasswords:
    def __init__(self):
        self.__data = self.__open_data()
        self.__testing_pw = "diogenes-souza-dev"

    def __open_data(self):
        try: 
            json_file = open("Passwords.json", "r")
            json_data = json.loads(json_file.read())
            return json_data
        except: 
            self.__data = {}
            self._write_data()
            self.__open_data()
    
    def _check_master_pw_setted(self):
        try:
            self.__data["encrypted_master_pw"]
        except: 
            self.__set_new_master_pw()

    def _login(self, master_pw):
        decrypted_master_pw = cryptocode.decrypt(self.__data["encrypted_master_pw"], master_pw)
        if decrypted_master_pw == self.__testing_pw:
            return master_pw
        else:
            return False

    def __set_new_master_pw(self):
        master_pw = False
        while master_pw == False: 
            try1 = getpass.getpass("\nCreate a master password. It will be used to decrypt the passwords you will save here...\n")
            try2 = getpass.getpass("Repeat the master password you just created...\n")
            if try1 == try2:
                master_pw = try1
                input("Master password set successfully")
            else:
                input("The passwords are different. Try again...")

        encrypted_master_pw = cryptocode.encrypt(self.__testing_pw, master_pw)
        self.__data["encrypted_master_pw"] = encrypted_master_pw
        self._write_data()
        return self.__data

    def _write_data(self):
        open("Passwords.json", "w").write(json.dumps(self.__data))


class NeverAgainForgetYourPasswords(DatabaseNeverAgainForgetYourPasswords):
    def __init__(self): 
        self.__master_pw = False
        self.__pw = ""
        self.__encrypted_pw = ""
        self.__database = DatabaseNeverAgainForgetYourPasswords()
        self.__database.__init__()

    def __ask_master_pw(self):
        self.__database._check_master_pw_setted()
        while self.__master_pw == False:
            self.__master_pw = self.__database._login(getpass.getpass("\nType the master password... \n>"))

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
        print("3 - Exit")
        result = input(">...")
        if result == "1":
            self.__encrypt()
        elif result == "2":
            self.__decrypt()
        elif result == "3":
            quit()
        else: 
            print("")
            self.__encrypt_or_decrypt()

    def run(self):
        self.__ask_master_pw()
        self.__encrypt_or_decrypt()


NeverAgainForgetYourPasswords().run()