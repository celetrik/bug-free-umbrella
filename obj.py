my_dict = dict()
print(my_dict)



person ={
    'Name': 'Hillary',
    'age': 24,
    'hobbies': ['writing','reading']
}



print(person['Name'])

person['Food'] = 'Pancakes'

print(person)



users = {
    'Authur': {
        'Name': 'Authur Curry',
        'Age': 29,
        'Occupation': 'Atlantean King',
    },
    'Peter': {
        'Name': 'Peter Parkter',
        'Age': 19,
        'Occupation': 'Photographer'
    },
    'Bruce': {
        'Name': 'Bruce Wayne',
        'Age': 31,
        'Occupation': 'Business Mogul'
    },
    'Diana':{
        'Name': 'Diana Prince',
        'Age': 'Unknown',
        'Occuaption': 'Art Currator'
    }
}




for k, v in sorted(users.items()):
    print(f"{k}'s fullname is {v['Name']}")