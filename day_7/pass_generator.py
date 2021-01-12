import string, secrets, pyperclip

pass_len = int(input("Password length: "))
upper_letters = int(input("Minimal number of upper case letters : "))
numbers = int(input("Minimal number of digits :"))
special = int(input("Minimal number of special characters :"))

alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(pass_len))

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(pass_len))
    if (any(c.islower() for c in password)
            and sum(c.isupper() for c in password)>=upper_letters
            and sum(c.isdigit() for c in password)>=numbers
            and sum(c in string.punctuation for c in password)>=special):
        break

pyperclip.copy(password)
print(password)
