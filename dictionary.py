#Dictionary
marks = {'urdu':80,'English':90}
print (marks)

print (type(marks))

#individual subject marks 
print (marks['urdu'])

print (marks.get('maths'))
#Adding items to the dictionary
marks ['maths'] = 100
print (marks)

#delete values
del marks ['urdu']
print (marks)

# find items length value

print (len(marks))