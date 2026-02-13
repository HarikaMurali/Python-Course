class ValidationError(Exception):
    pass


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def validate(self):
        if len(self.firstname) <= 3:
            raise ValidationError("First name must be more than 3 characters")

        if len(self.lastname) <= 3:
            raise ValidationError("Last name must be more than 3 characters")

        if not self.firstname.isalpha():
            raise ValidationError("First name should contain only characters")

        if not self.lastname.isalpha():
            raise ValidationError("Last name should contain only characters")

        print("Validation successful!")
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)


# Taking user input
try:
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")

    user = User(fname, lname)
    user.validate()

except ValidationError as e:
    print("Validation Error:", e)
