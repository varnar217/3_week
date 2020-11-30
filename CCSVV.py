import csv

fields =[
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]




with open('export.csv', 'w', encoding='utf-8', newline='') as f:

    writer = csv.DictWriter(f,fieldnames=list(fields[0].keys()),quoting=csv.QUOTE_NONNUMERIC )
    writer.writeheader()
    for d in fields:
        writer.writerow(d)


    #writer.writeheader()
    #for user in user_list:
        #writer.writerow(user)
