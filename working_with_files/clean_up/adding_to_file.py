

print("adding to file input.txt\n")
add_to_file = input("What to add to the file:\n")

#r for readonly, w for writing only (will erase old), a for appending (adding) at the end,  r+ reading and writing, mode is optional, r will be assumed
with open('input.txt', 'a') as file:
    file.write(add_to_file + "\n")