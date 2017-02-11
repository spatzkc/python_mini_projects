
def capitalize_first_letter(word):
    #capitalizes the first letter of a string
    output = ""
    for i in range(len(word)):
        if i == 0:
            output = word[i].upper()
        else:
            output += word[i]
    return output


def main():
    print "Welcome to Mad Libs!"
    name_person = raw_input("Enter the name of a person: ")
    gender = raw_input("Enter the gender pronoun for this person (he/she/they): ")
    adjective = raw_input("Enter an adjective: ")
    noun = raw_input("Enter a noun: ")
    print "Here's your Mad Libs story!"
    print ""
    print "One day, " + name_person + " was walking to school when " + gender + \
    " saw a " + adjective + " " + noun + "." + "\n" \
    + capitalize_first_letter(gender) + " tripped over the " + noun + " and fell into a puddle." + "\n" \
    + "\'Oh no!\' " + name_person + " said. \'I guess I'll have to go home and change.\'" 
    
main()