from src.ReceiveUserInput import ReceiveUserInput
from src.ValidatePassword import ValidatePassword
from src.DisplayResults import DisplayResults
#from src.WritePasswordToTextFile import WritePasswordToTextFile

def main():

    CadastrationComplete = False

    while CadastrationComplete == False:
        User = ReceiveUserInput("Insira o nome de usuário")
        Password = ReceiveUserInput("Insira a senha")

        if(ValidatePassword(Password)):
            DisplayResults("Senha cadastrada com sucesso")
            CadastrationComplete = True
            
        else:
            DisplayResults("Senha inválida")
            CadastrationComplete = False



main()
