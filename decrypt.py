import pyperclip
import cryptocode
import getpass

input("Copie a senha a ser descriptografada, e em seguida, aperte Enter")
senha = pyperclip.paste()
print(">" + senha)
chave = getpass.getpass("\nDigite a chave para descriptografar \n")

try: 
    senha_criptografada = cryptocode.decrypt(senha, chave)
    copiar = input("\nSenha descriptografada: \n" + senha_criptografada + " \n \nPressione Enter para copiar. \n")

    pyperclip.copy(senha_criptografada)
except: 
    input("Chave incorreta!")