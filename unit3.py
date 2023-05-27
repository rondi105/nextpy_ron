import string

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character, position):
        self.illegal_character = illegal_character
        self.position = position

    def __str__(self):
        return f"The username contains an illegal character '{self.illegal_character}' at index {self.position}."

class UsernameTooShort(Exception):
    def __str__(self):
        return "The username must be at least 3 characters long."

class UsernameTooLong(Exception):
    def __str__(self):
        return "The username must be at most 16 characters long."
class PasswordTooShort(Exception):
    def __str__(self):
        return "The password must be at least 3 characters long."

class PasswordTooLong(Exception):
    def __str__(self):
        return "The password must be at most 16 characters long."
class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character."

class PasswordMissingCapitalLetter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingSmallLetter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingNumber(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecialCharacter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"

def check_input(username, password):
    legal_characters = string.ascii_letters + string.digits + "_"

    if any(char not in legal_characters for char in username):
        illegal_char = next(char for char in username if char not in legal_characters)
        position = username.index(illegal_char)
        raise UsernameContainsIllegalCharacter(illegal_char, position)

    if len(username) < 3:
        raise UsernameTooShort()

    if len(username) > 16:
        raise UsernameTooLong()

    if len(password) < 8:
        raise PasswordTooShort()

    if len(password) > 40:
        raise PasswordTooLong()

    char_kinds = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation
    ]

    for char_set in char_kinds:
        if not any(char in password for char in char_set):
            if char_set == string.ascii_uppercase:
                raise PasswordMissingCapitalLetter()
            elif char_set == string.ascii_lowercase:
                raise PasswordMissingSmallLetter()
            elif char_set == string.digits:
                raise PasswordMissingNumber()
            elif char_set == string.punctuation:
                raise PasswordMissingSpecialCharacter()

    print("OK")

class  UnderAge(Exception):
    def __init__(self,age):
        self._age=age
    def __str__(self):
        return "your age %s is under 18! and you can be invited in %d years."%(self._age,18-self._age)
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return f"__CONTENT_START__\n{content}__CONTENT_END__"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"

def send_invitation(name, age):
    try:
        if(int(age) < 18):
            raise UnderAge(age)
        else:
              print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)



def main():
    print(read_file("file.txt"))
    print(read_file("notexist.txt"))

    send_invitation("ron",17)
    send_invitation("may",20)

    while True:
        try:
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            check_input(username, password)
            break
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
                PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as e:
            print(e)

if __name__ == '__main__':
    main()

