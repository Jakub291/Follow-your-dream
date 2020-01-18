import random

zbior = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 12 # password length
p =  "".join(random.sample(zbior,passlen ))
print (p)