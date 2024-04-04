#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'

with open('./Input/names/invited_names.txt') as names_file:
    names = names_file.readlines() #para convertir cada fila en una lista
    # print(names)

with open('./input/letters/starting_letter.txt') as letter_file:
    letter_contetnts = letter_file.read()
    # print(letter_contetnts)
    for name in names:
        stripped_name = name.strip() # para quitar el enter de cada nombre
        new_letter = letter_contetnts.replace(PLACEHOLDER, stripped_name) #reemplazar cada nombre en cada carta
        with open(f'./output/readytosend/letter_for_{stripped_name}.txt', mode='w') as final_leter_file: #crear cada carta para cada nombre
            final_leter_file.write(new_letter)
