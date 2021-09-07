def ParseDataToWriteToFIle(User, Password):
    ParsedData = f"user: {User} \nPassword: {Password}"

    return ParsedData

def WriteLoginToTextFile(User, Password):
    with open('login.txt', 'w') as f:
        f.write(ParseDataToWriteToFIle(User, Password))

    return True