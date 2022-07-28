import pyperclip
import cryptocode

chave = input("Digite a senha master \n>")

while(1==1):
    senha = input("\nDigite a senha a ser criptografada \n>")

    senha_criptografada = cryptocode.encrypt(senha, chave)

    copiar = print("\nSenha criptografada: \n" + senha_criptografada + " \n \n")

    pyperclip.copy(senha_criptografada)