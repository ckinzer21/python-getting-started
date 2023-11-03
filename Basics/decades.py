age = int(input("How old are you?\n"))
decades = age//10 # / will give decimal // will give whole numbers
years = age % 10


print("You are " + str(decades) + " decade(s) and "+str(years)+" years old.")