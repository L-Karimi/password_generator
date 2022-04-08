import random
import string
print("Hello,welcome to  password generator")
length = int(input("\n Enter the length of the password: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase

num = string.digits
Symb = string.punctuation
all = lower + upper + num + Symb



all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all,length))
print(password)