import pyperclip
import cryptocode

masterpw = input("Digite a senha master \n>")

pw = input("\nDigite a senha a ser criptografada \n>")

crypto_pw = cryptocode.encrypt(pw, masterpw)

print("\nSenha criptografada: \n" + crypto_pw + " \n \n")

pyperclip.copy(crypto_pw)