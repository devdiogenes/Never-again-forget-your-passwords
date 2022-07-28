import pyperclip
import cryptocode
import getpass

input("Copie a senha a ser descriptografada, e em seguida, aperte Enter")
crypto_pw = pyperclip.paste()
print(">" + crypto_pw)
master_pw = getpass.getpass("\nDigite a chave para descriptografar \n")

try: 
    pw = cryptocode.decrypt(crypto_pw, master_pw)
    input("\nSenha descriptografada: \n" + pw + " \n \nPressione Enter para copiar. \n")

    pyperclip.copy(pw)
except: 
    input("Chave incorreta!")