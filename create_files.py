# create txt file with random text and phone number

import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()

word_list =[]
for word in words[:50]:
    wrd = word.decode()
    word_list.append(wrd)


def gen_phone():
    first = str(random.randint(100,999))
    second = str(random.randint(1,888)).zfill(3)

    last = (str(random.randint(1,9998)).zfill(4))
    while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
        last = (str(random.randint(1,9998)).zfill(4))

    return '{}-{}-{}'.format(first,second, last)


for i in range(10):
    file = open(f"{i+1}.txt", "w")
    j=0
    
    for word in word_list:
        position = random.randint(6,7)
        file.write(word)
        
        file.write(" ")
        if(j % position):
            file.write(f"{gen_phone()} ")
        
        if j%10 == 0:
            file.write("\n")
        
        j+=1
    file.close()

