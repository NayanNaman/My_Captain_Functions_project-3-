i=input("Please enter a string: ")
table={} 
for letter in i:
    if letter in table:
        table[letter] +=1
    else:
        table[letter] = 1
      

print(sorted(table.items(), key=lambda x : x[1], reverse=True ))
