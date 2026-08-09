password = input("Enter Your password")
upper = False
lower = False
digit = False
special_char = False

for char in password:
    if char.isupper():
        upper = True
    if char.islower():
        lower = True
    if char.isdigit():
        digit = True
    if not char.isalnum():
        special_char = True
 
score = 0

length =len(password)

if length >=8:
    score = score + 1
if upper:
    score = score + 1
if lower:
    score = score + 1
if digit:
    score = score + 1
if special_char:
    score = score + 1
    
    

if score >=5:
    print("strong password")
elif score == 3 or score == 4:
    print("medium password")
else:
    print("Weak Password")


