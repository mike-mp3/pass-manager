import random

print("Working...")


def main():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = (random.randint(8, 12))
    length = (random.randint(8, 12))
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        return password


d = open('data.txt', 'a+')
print("*" * 10 + " <Password manager> " + "*" * 10)
print("Write down how many passwords you need")
c = int(input())
while c != 0:
    d.write(f'{main()}\n')
    c -= 1
print('Done! Saves go to data.txt')
d.close()
