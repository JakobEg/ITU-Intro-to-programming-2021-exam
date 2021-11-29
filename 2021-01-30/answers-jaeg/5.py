# Make a list L of dead author names of length 3 or 4
L = ['Agatha Christie', 'schopenhauer', 'Kierkegaard', 'Jung']
# print the length of L (should be 3 or 4)
print(len(L))
# insert 'Plato' at the end of the list
L.append('Plato') 
# Make another list of length at least 3
Q = ['Goethe', 'Blixen', 'Andersen'] 
# Add all the authors in Q to L
L.append(Q) 
# Remove the 2nd and 3rd authors from the list L using slicing
L.remove()
# Print each author in L on a separate line, without any quotation marks
for i in L:
    print(i)
