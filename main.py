# pick phone number form text file 

import re

regex = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
name_regex = r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]+"

all_contacts = []

for i in range(4):
    all_phones = []
    all_names = []

    with open(f'{i+1}.txt') as f:
        text = f.read()
        phones = re.findall(regex, text)
        names = re.findall(name_regex, text)

        if phones: 
            for phone in phones:
                if len(phone) >= 10: # ignore number less than 10 digit
                    all_phones.append(phone)

        if names:
            all_names.extend(names)
            
    contacts = {
        'source': f'{i+1}.txt',
        'contact_list' : all_phones,
        'names' : all_names
    }

    all_contacts.append(contacts)

for contacts in all_contacts:
    for key,value in contacts.items():
        print(f"{key} : {value}")
    print('')

