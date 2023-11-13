#working with input.txt in working_with_files directory

# #with has exception handling built into it
#similar to using statement where it disposes of objects
# with open('input.txt') as file:
#     result = file.read()
#     print(result)

# with open('input.txt') as file:
#     result = file.readlines()
#     for line in result:
#         print(line)


look_up = input("Search for acronym in text tile:\n")

found = False

with open('input.txt') as file:
    for line in file:
        if look_up.lower() in line.lower(): #make it not case sensitive
            print("line exists: " + line)
            found = True
            break

if not found:
    print('Not found')