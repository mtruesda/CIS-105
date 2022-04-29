#creating the file
test_file = open('test.txt', 'w')

#add content
for i in range(4):
    test_file.write('Henlo ' + str(i) + '\n')

#close the file
test_file.close()

#opening in a read format
test_file = open('test.txt', 'r')
test_file.read()

#closing and printing the location in RAM
test_file.close()
print(test_file)

#reopening in read
test_file = open('test.txt', 'r')

#you can insert numbers in paranthesis to limit what gets used.
line1 = test_file.readline()
line2 = test_file.readline()
line3 = test_file.readline()

test_file.close()

#finding out if you can print them after
print('testing')
print(line3)
