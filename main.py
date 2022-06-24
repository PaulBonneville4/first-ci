def count_char(password):
    return len(password)

def check_invalid_special_char(password):
    """
        banned char: '@', '=', '+', ' '
        return True if not invalid char else False
    """
    for c in password:
        if c in ['@', '=', '+', ' ']:
            return False 
    return True

def check_if_maj(password):
    for c in password:
        if c.isupper():
            return True
    return False

def check_if_special_char(password):
    for c in password:
        if c in ["!","#",";"]:
            return True
    return False

def check_if_password_valid(password):
    if count_char(password) <=10:
        return False
    if check_invalid_special_char(password) == False:
        return False
    if check_if_maj(password) == False:
        return False
    if check_if_special_char(password) == False:
        return False
    return True

print(check_if_password_valid("Bonjourrrrrrr!"))