''' 
QN1
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
'''
numbers = []
for number in range(2000 , 3200):
    if (number%7 == 0) and (number%5 != 0):
        numbers.append(number)
        # print(number, sep=',')
print(numbers)
print(100*"+")

'''
QN2
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
'''
my_sequence_letters = input("\nEnter any sentence to be capitalized please! \n :> ")
print("Your sentence is {}\n".format(my_sequence_letters.upper()))
print(100*"+")


'''
QN3
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''
bin=input("\n Enter a binary values\n :> ")
for i in range(0,len(bin),5):
    if int(bin[i:i+4],2)%5==0:
        print(bin[i:i+4],end=',')
