import re

def RegexSearch(Password, Regex):
        Search = re.compile(Regex)

        if re.search(Search, Password):
            return True
        else:
            return False

def LenghtPolicy(Password):
    if len(Password) < 8:
        return False
    else:
        return True


def VerifyPolicies(Password):
    ProblemCounter = 0

    if LenghtPolicy(Password) == False:
        ProblemCounter = 1 + ProblemCounter

    if RegexSearch(Password, ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[-+_!@#$%^&*., ?]).+$")) == False:
        ProblemCounter = 1 + ProblemCounter
    
    print(ProblemCounter)

    return ProblemCounter

def ValidatePassword(Password):
    if(VerifyPolicies(Password) > 0):
        return False
    else:
        return True
