from src.ReceiveUserInput import ReceiveUserInput
from src.ValidatePassword import ValidatePassword
from src.DisplayResults import DisplayResults
from src.WriteLoginToTextFile import WriteLoginToTextFile

def main():

    CadastrationComplete = False

    while CadastrationComplete == False:
        User = ReceiveUserInput("Insira o nome de usuário")
        Password = ReceiveUserInput("Insira a senha")

        if(ValidatePassword(Password) == False):
            DisplayResults("Senha cadastrada com sucesso")
            CadastrationComplete = False

        else:

            if(WriteLoginToTextFile(User, Password)):
                DisplayResults("Senha cadastrada com sucesso")
                CadastrationComplete = True
            else:
                DisplayResults("Erro ao cadastrar senha. Tente novamente mais tarde")
                CadastrationComplete = False
main()