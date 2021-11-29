def read_file(filename):
    """reads file as filename and returns a list"""
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines

def had_contact(name, filename):
    #create a list containing all the people in the file provided
    contact_information = read_file(filename)
    print(contact_information)
    #if the name provided is present in the provided file, the function returns true
    for person in contact_information:
        if f"{name}.+" in contact_information:
            return True
    return False

print(had_contact('Cortez', '8/1.txt'))