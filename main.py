# pick phone number form text file 

import re

all_contacts = []
lines = []

for i in range(10):
    all_phones = []
    with open(f'{i+1}.txt') as f:
        lines = f.readlines()
        for line in lines:
            phones = re.findall(r"\d\d\d-\d\d\d-\d\d\d\d",line)
            all_phones.extend(phones)

    contacts = {
        'source': f'{i+1}.txt',
        'contact_list' : all_phones
    }

    all_contacts.append(contacts)


for contacts in all_contacts:
    for key,value in contacts.items():
        print(f"{key} : {value}")
