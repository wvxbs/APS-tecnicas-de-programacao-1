import re

ex = ("^(?=.*[a-z]) (?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")


def RegexSearch(Password, Regex):
        Search = re.compile(Regex)

        if(re.search(Search, Password)):
            return True
        else:
            return False

def LenghtPolicy(Password):
    if( 8 >= len(Password)):
        return True
    else:
        return False


def VerifyPolicies(Password):
    ProblemCounter = 0

    if(RegexSearch(Password, "^(?=.*[a-z])") == False):
        ProblemCounter = 1 + ProblemCounter

    if(RegexSearch(Password, "^(?=.*[A-Z])") == False):
        ProblemCounter = 1 + ProblemCounter

    if(RegexSearch(Password, "^(?=.*\\d)") == False):
        ProblemCounter = 1 + ProblemCounter

    if(RegexSearch(Password, "^(?=.*[-+_!@#$%^&*., ?]).+$") == False):
        ProblemCounter = 1 + ProblemCounter

    if(LenghtPolicy(Password) == False):
        ProblemCounter = 1 + ProblemCounter
        
    return ProblemCounter

def ValidatePassword(Password):
    if(VerifyPolicies(Password) > 0):
        return False
    else:
        return True
