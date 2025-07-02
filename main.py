#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# invited_names = []
PLACEHOLDER = "[name]"

with open(file = "./Input/Names/invited_names.txt") as names_file:
    invited_names = names_file.readlines()
    
# print(invited_names)

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    
    for name in invited_names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        
        with open(file = f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode = "w") as new_file:
            new_file.write(new_letter)

