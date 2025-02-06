#PLEASE MAKE SURE THE INPUT FILE IS IN THE SAME DIRECTORY AS THE PROGRAM

file_name = None
counter = 0

#ensures file name can be found
while file_name == None:
    try:
        file_name = input("Please enter the name of the input data file: ")
        file = open(file_name.strip(), "r")


    except FileNotFoundError as err:
        print("File not found: ", err)
        file_name = None

#prompting for output file name
user_filename = input("Please enter the name of the output data file: ")
output = open(user_filename, 'w')

#for loop that writes data to the new file for each line of code
for line in file:
    line_stripped = line.strip()
    words = line_stripped.split(" ")
    word_count = len(words)
    words_str = str(words)

    #if statement to check if the line is the students hobby
    if word_count > 1 :

        #code to write to new file
        counter += 1
        output.write("Student_")
        output.write(str(counter))
        output.write("\n")
        output.write(str(word_count))
        output.write("\n")

        #stores the word count as a str into a list to be passed into the below elif statement
        word_count_number_variable = [str(word_count)]

    #elif statement to ensure that the line being checked is not a student number line
    elif (word_count == 1) and words_str.count('t') < 1:

        #if-elif statements for comparing if the pre determined number is correct
        if words == word_count_number_variable:
            output.write("True")
            output.write("\n")
            output.write("\n")
        elif words != word_count_number_variable:
            output.write("False")
            output.write("\n")
            output.write("\n")

#closes files
file.close()
output.close()
print("All data was successfully processed and saved to the requested output file.")
