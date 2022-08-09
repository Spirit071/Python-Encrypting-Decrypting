
import random
import json

# this function is used to generate random numbers for encrypting messages, and then for the decrypt function
def get_random_number():
     return random.randint(1, 1000)

# this function is used to delete earlier json data, and recieving new data
def clearJson():
    with open('randoms.json', 'w') as F:
            json.dump(None, F)

def rndNumListCreator(s):
    rndNumList = []
    for x in range(len(s)):
        rndNumList.append(get_random_number())
# making the list of random numbers in the json file
    with open('randoms.json', 'w') as F:
        json.dump(rndNumList, F)

    with open('randoms.json', 'r') as openfile:
            # read the list of random numbers from the file
        data = json.load(openfile)

    return data

def decrypt(toDecrypt):  # the 'toDecrypt' string is an encrypted message
    # load data from json and prepare it for decryption
   with open('randoms.json', 'r') as openfile:
            # read the list of random numbers from the file
            data = json.load(openfile)
            index = 0
            s = ''
            for char in toDecrypt:
                a = chr(ord(char) - int(data[index]))
                s+=a
                index+=1
            print("The decrypted message is: {0}".format(s))

def encrypt(q):
    s = ''
    with open('randoms.json', 'r') as openfile:
        index = 0  # here, the first value is for the first character
        n = rndNumListCreator(q)
        # for each character in the 'q' string
        for char in q:
            a = chr(ord(char) + int(n[index])) # turn the ASCII into an actual text(char)
            s = s + a
            index = index + 1
        print(f' The encrypted message is: {s}')


def main():
    action = input("Encrypt(e) or decrypt(d)? ").lower()  # get the action
    var = 0
    '''
    encrypting the message
    '''
    if action == 'e':
        string = input("Please enter a message to encrypt: ")      
        rev = ''
        var = 1
        for char in string[::-1]:
            rev = rev + char
# see if we have a palindromic message
        if rev == string:
            print('Error! Palindromic message detected!')
            main()
            # if not then encrypt
        else:
            encrypt(string)
# if we want to decrypt the message then decrypt it
    if action == 'd':
        var = 1
        string = input("Please enter a message to decrypt: ")   
        decrypt(string)
        clearJson()
    # if another action provided and we don't have another function running, rerun the script
    else:
        if var != 1:
            main()

if __name__ == '__main__':
    var = 1
    main()
