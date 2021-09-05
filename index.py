#from src.DisplayUserInteraction import DisplayUserInteraction
from src.ReceiveUserInput import ReceiveUserInput
#from src.ValidatePassword import ValidatePassword
#from src.WritePasswordToTextFile import WritePasswordToTextFile

def main():
    User = ReceiveUserInput("Insira o nome de usuário")
    Password = ReceiveUserInput("Insira a senha")

    print(User)
    print(Password)

main()
