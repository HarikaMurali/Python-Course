'''def validateAge(Age):
    if(Age<18):
        raise Exception("Invalid Age, less than 18")
    else:
        print("Valid Age")

validateAge(18)'''

def validateAge(Age):
    if(Age<18):
        raise LessAgeException("Invalid Age, less than 18")
    elif(Age>60):
        raise MoreAgeException("Invalid Age, greater than 60")
    print(f"You are Eligible {Age} ")

class LessAgeException(Exception):
    pass
class MoreAgeException(Exception):
    pass
try:
    validateAge(61)
except LessAgeException as e:
    print(e)
except MoreAgeException as e:
    print(e)    
