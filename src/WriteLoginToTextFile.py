def ParseDataToWriteToFIle(User, Password):
    ParsedData = f"user: {User} \npassword: {Password}"

    return ParsedData

def WriteLoginToTextFile(User, Password):
    try:
        with open('login.txt', 'w') as f:
            f.write(ParseDataToWriteToFIle(User, Password))
            
        return True
            
    except IOError:
        return False