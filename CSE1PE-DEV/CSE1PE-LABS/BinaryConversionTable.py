# Binary Coversion Table 
start = int(input('Start: '))
stop = int(input('Stop: '))

# Create the binary conversion table, saving it to table.txt.
table_file = open('table.txt', 'w') #Open file for writing

for i in range(start, stop):
    binary_representation = f'{i:08b}'
    table_file.write(f'{binary_representation} is {i}\n')

table_file.close() # Closing file after writing

# Read and display the contents of the file.
table_file_readonly = open('table.txt', 'r')
print(table_file_readonly.read(), end='')
table_file_readonly.close()  # Close the file after reading
