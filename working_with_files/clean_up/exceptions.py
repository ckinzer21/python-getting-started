dictionary = {'key1': 'value1',
              'key2': 'value2'}

try:
    definition = dictionary['key3']
except:
    print('The key does not exist')
finally:
    print('Ending program')