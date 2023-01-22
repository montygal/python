#This is practice on lists
acronyms = ['LOL', 'IDK', 'SMH']

#We can add more to the list with 'append'
acronyms.append('BFN')
acronyms.append('IMHO')

#Remove an acronym
acronyms.remove('BFN')

#Or we could remove it according to index
del acronyms[0]

#We can check to see if something is in the list
word = 'BFN'
if word in acronyms:
    print(word + ' ' +'is in the list')
else:
    print(word + ' ' +'is NOT in the list')

#To print in seperate lines:
for acronym in acronyms:
    print(acronym)

