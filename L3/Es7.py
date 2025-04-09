# Conta vocali
import re

st = input("Enter a string: ")

l_st = re.sub(r"\W*", " ", st).split()

vocals = ["a", "e", "i", "o", "u"]

count_vocals = {}

for i in vocals:
     if i in l_st:
         k = l_st.count(i)
         count_vocals[i] = k

print(count_vocals)