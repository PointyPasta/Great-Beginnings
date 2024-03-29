txt1 = "Hello World"
print(txt1)

txt1 = "Goodbye World"
print(txt1, "\n")

myName = "juan hung"
print(myName.title())
print(myName.upper())
print(myName.lower(),"\n")

first_name = "juan"
last_name = "hung"
full_name = f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello {full_name.title()}\n")

f_name = f"Hello {full_name.title()}\n"
print(f_name, "\n")










#MATH SECTION

print(5+3)
print(10-2)
print(4*2)
print(16/2, "\n")

fav_Num = 7
print(fav_Num, "\n")








# WORKING WITH LISTS





books = ['dune', 'a song of ice and fire', 
         'the priory of the orange tree', 'vagabond']
print(books[0])
print(books[0].title())
print(books[-1].title(), "\n")

fav_Book = f"My favorite book is {books[0].title()}\n"
print(fav_Book)

books[0] = 'uzumaki'
print(books, "\n")

books.append('dune')
print(books, '\n')

books.insert(0, 'devilman')
print(books, '\n')

del books[1]
print(books, '\n')

manga = books.pop(0)
print(books, '\n')
print(manga, '\n')

books.remove('vagabond')
print(books, '\n')

books.append('vagabond')
print(books, '\n')

remove = 'vagabond'
books.remove(remove)
print(books, '\n')

print(len(books), '\n')

for book in books:
    print(book.title())

print('\n')

for book in books:
    print(f'{book.title()} is an amazing book and I recommend it')






# Numerical List
    

print('\n')
for value in range(1, 11):
    print(value)
print('\n')

numbers = list(range(1,6))
print(numbers)

odd_numbers = list(range(1,12,2))
print(odd_numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

squares = [num**2 for num in range(1, 7)]
print(squares, '\n')

print(squares[1:5])
print(squares[:5])
print(squares[1:])
print(squares[-3:])

for num in squares[-3:]:
    print(num)

print('\n')
mine_block = ('grass', 'cobble')
print(mine_block[0])
print(mine_block[1], '\n')

for blocks in mine_block:
    print(blocks)
