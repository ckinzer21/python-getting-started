dictionary = {"key1": "value 1",
        "key2": "value 2"}

print(dict["key1"])

dict2 = {}
dict2["burger_price"] = float(10.5)
print(dict2["burger_price"])

dict2["burger_price"] = float(15.80)
print(dict2["burger_price"])

del dict2["burger_price"]
print(dict2)

definition = dict2.get('burger_price') #prevents error if it does not exist
if definition:
        print(definition)
else:
        print("key doesn't exist")

for key in dictionary:
        print(key)

key = input("Enter key number:\n")
value = dictionary.get(key)

if value == None:
        print("no key")
else:
        print(key, value)