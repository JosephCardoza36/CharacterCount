characters = input("Enter a sentence of 20 or more characters: ")

while len(characters) < 20:
    characters = input("I'm sorry but please enter a string of 20 or more characters: ")


#function to return dict format
def add_to_dict(dict, list):
    for letter in list:
        if letter in dict:   #if letter already in dict, then update the number value by 1.
            dict[letter] += 1
        else:
            dict[letter] = 1   
    return dict

#--------------------------------------------------------------- Analysis 1 - to show characters in lowercase + count--------------------------------------------------------- #

print("\n\nThe original string is: " + characters)
print("The string being analyzed is: " + characters.lower())
characters_strip = characters.replace(" ", "")      #remove all white space, so that we don't count spaces as characters
print(f"The total number of characters is: {len(characters_strip)}")

characters_to_analyze = [letter.lower() for letter in characters_strip]  #list comprehension to create an isolated list of every letter and turning that specific letter to lower case.

d = {} 
characters_to_analyze.sort()  #sort in alpha order
d = add_to_dict(d, characters_to_analyze)

print("\nAnalysis 1 Character Count, Lower.")
print("------------------------------------")
for key, value in d.items():
    print(f"Frequency => {key}: {value} || ASCII value: {ord(key)}")

#--------------------------------------------------------------- Analysis 2 - to show characters in uppercase + count--------------------------------------------------------- #

characters_to_analyze = [letter for letter in characters_strip]
print("\n\nThe original string is: " + characters)
characters = characters.replace(" ", "")   
print(f"The total number of characters is: {len(characters)}")


d = {}   #reset dict to empty
d = add_to_dict(d, sorted(characters_to_analyze, key=lambda letter: (letter.upper(), letter[0].islower())))  


print("\nAnalysis 2 Character Count, Upper.")
print("------------------------------------")

for key, value in d.items():
    print(f"Frequency => {key}: {value} || ASCII value: {ord(key)}")

