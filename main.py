# pick phone number form text file 

import re
regex = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
# regex = r"\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}"

all_contacts = []
m =[]

for i in range(3):
    all_phones = []
    with open(f'{i+1}.txt') as f:
        text = f.read()
        phones = re.findall(regex, text)
        
        if phones: 
            for phone in phones:
                if len(phone) >= 10: # ignore number less than 10 digit
                    all_phones.append(phone)
            
    contacts = {
        'source': f'{i+1}.txt',
        'contact_list' : all_phones,

    }

    all_contacts.append(contacts)

for contacts in all_contacts:
    for key,value in contacts.items():
        print(f"{key} : {value}")

