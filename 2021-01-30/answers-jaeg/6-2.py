import string
def is_valid(password):
    check_lower = False
    check_upper = False
    check_digit = False

    #length check
    if len(password) < 8:
        return False
    
    #check if contains lowercase
    for letter in password:
        if letter in string.ascii_lowercase:
            check_lower = True

    #check if contains uppercase
    for letter in password:
        if letter in string.ascii_uppercase:
            check_upper = True

    #check if contains digit
    for letter in password:
        if letter in string.digits:
            check_digit = True


    #returns true if all checks are true
    if check_upper==True and check_lower==True and check_digit == True:
        return True
    else:
        return False

assert(is_valid('t00Shrt') == False)
assert(is_valid('thispasswordisverylongbutdoesntconta1nuppercaseletters') == False)
assert(is_valid('Th1s1isAvalidPasSSword') == True)
