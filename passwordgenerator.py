import random
import string

Letters = string.ascii_letters
Nums = '012345678910'
SPE = '-+*%$&@#_:'
Symbols = Letters + Nums + SPE
len = int(input("Enter Your Password Length: "))
password = random.sample(Symbols,len)

print(password)
