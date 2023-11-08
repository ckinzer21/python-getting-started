contacts = {
    'number' : 4,
    'students':
    [
        {'name':'Chris', 'email':'a@b.com'},
        {'name':'John', 'email':'b@b.com'},
        {'name':'Joe', 'email':'c@b.com'},
        {'name':'Doe', 'email':'d@b.com'},
    ]
}

print('Student emails: ')
for student in contacts['students']:
    print(student['email'])