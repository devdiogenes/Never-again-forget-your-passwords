import cryptocode
import getpass
import json

class ModelNeverAgainForgetYourPasswords:
    def __init__(self):
        self.__data = self.__open_data()
        self.__testing_pw = "devdiogenes.com"

    def __open_data(self): #Open a data file if it exist, create if don't
        try: 
            json_file = open("Passwords.json", "r")
            json_data = json.loads(json_file.read())
            json_file.close()
            return json_data
        except: 
            self.__data = {}
            self.__write_data()
            return {}

    def __write_data(self):
        open("Passwords.json", "w").write(json.dumps(self.__data, indent = 4))
    
    def _check_register(self):
        if "master_pw" in self.__data.keys():
            return True
        else:
            return False
        
    def _register(self, master_pw):
        encrypted_master_pw = cryptocode.encrypt(self.__testing_pw, master_pw)
        self.__data["master_pw"] = encrypted_master_pw
        self.__write_data()

    def _try_login(self, master_pw):
        decrypted_master_pw = cryptocode.decrypt(self.__data["master_pw"], master_pw)
        if decrypted_master_pw == self.__testing_pw:
            return master_pw
        else:
            return False
        
    def _add_pass(self, encrypted_pw, description):
        if "passwords" not in self.__data.keys():
            self.__data["passwords"] = {}
        self.__data["passwords"][description] = encrypted_pw
        self.__write_data()

    def _get_passwords(self):
        if "passwords" not in self.__data.keys():
            self.__data["passwords"] = {}
        return self.__data["passwords"]
        
        