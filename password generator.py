import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=['!','@','#','$','&','*','(',')','_']
password_list=[]
print("Welcome to password Generator\n")
n_letters=int(input("Enter how many letters do you want in your password:\n"))
n_numbers=int(input("Enter how many numbers do you want in your password:\n"))
n_symbols=int(input("Enter how many symbols do you want in your password:\n"))
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list.append(char)
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list.append(char)
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list.append(char)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=str(char)
print(password)

