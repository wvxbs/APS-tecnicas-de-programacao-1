def UpperCasePolicy(Password):
    return False
def LowerCasePolicy(Password):
    return False
def NumberPolicy(Password):
    return False
def SpecialCharacterPolicy(Password):
    return False
def LenghtPolicy(Password):
    return False

def VerifyPolicies(Password):
    ProblemCounter = 0

    if(UpperCasePolicy(Password) == False):
        ProblemCounter = 1 + ProblemCounter

    if(LowerCasePolicy(Password) == False):
        ProblemCounter = 1 + ProblemCounter

    if(NumberPolicy(Password) == False):
        ProblemCounter = 1 + ProblemCounter

    if(SpecialCharacterPolicy(Password) == False):
        ProblemCounter = 1 + ProblemCounter

    if(LenghtPolicy(Password) == False):
        ProblemCounter = 1 + ProblemCounter
    return ProblemCounter

def ValidatePassword(Password):
    if(VerifyPolicies(Password) > 0):
        return False
    else:
        return True
