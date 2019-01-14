""" 
# write to a file

def main ():
    outfile = open ('test.txt', 'w')
    outfile.write ('Python is fun')
    outfile.close ()

main ()
#----------------------------------------------
# read from a file

def main ():
    infile = open ('test.txt', 'r')
    content = infile.read ()                #calling the read method, what the program finds it will put it in a variable call content
    infile.close ()
    print (content)

main ()

#----------------------------------------------

# append to a file (existing file)

def main ():
    myfile = open ('test.txt', 'a')
    myfile.write('\n\tPython is object oriented')
    myfile.close()

main ()
"""
"""
#-------------------------------------------------

#read one line at a time

def main ():
    txt = open ('test.txt', 'r')
    #read three lines from the file
    ln1 = txt.readline ()
    ln2 = txt.readline ()
    ln3 = txt.readline ()
    txt.close ()
    print (ln1)
    print (ln2)
    print (ln3)

main ()

"""
"""
#-----------------------------------------------

# Get string input from user and write it to a file

def main ():
    c1 = input ('city #1: ')
    c2 = input ('city #2: ')
    c3 = input ('city #3: ')
    # create and open a file to write on
    newfile = open (r'C:\Users\abreu\Desktop\PACE\OBJECT ORIENTED\PHYTON SCRIPTS\test2.txt', 'w')
    newfile.write(c1 + '\n')
    newfile.write(c2 + '\n')
    newfile.write(c3 + '\n')
    newfile.close ()

main ()
"""

#----------------------------------------


# get numeric input from user and write it to a file

def main ():
    out = open (r'C:\Users\abreu\Desktop\PACE\OBJECT ORIENTED\PHYTON SCRIPTS\test3.txt', 'w')
    #get numeric input from user
    n1 = input ('Enter a number: ')
    n2 = input ('Enter a number: ')
    #write numbers to the file
    out.write(str(n1) + '\n')
    out.write(str(n2) + '\n')
    out.close ()

main ()

#---------------------------------------------------------------------------------------------------

#reading string and stripping \n
# open an existing file

def main ():
    infile = open ('test.txt', 'r')
    #read two line from the file
    ln1 = infile.readline ()
    ln2 = infile.readline ()

    #strip \n from strings
    ln1 = ln1.rstrip ('\n')
    ln2 = ln2.rstrip ('\n')
    infile.close
    print (ln1)
    print (ln2)

main ()


#--------------------------------------------------------------------------

# Handling exception: IOError
try:
    fh = open ('megafile.txt', 'w')
    fh.write ('this is a test file for exception handling.')

except IOError:
    print ('Error: can\'t find the file or read data.')
else:
    print ('written content on the file successfully')
    fh.close ()
#--------------------------------------------------------------------------------------

#IOError

try:
    fh = open ('megfile.txt', 'r')
    content = fh.read ()
except IOError:
    print ('can\'t find the file')
else:
    print ('read the content of the file.')

#---------------------------------------------------------------------------------------

#try block and two exception blocks
try:
    num1, num2 = eval(input ("enter two numbers seperated by comma: "))
    result = num1 / num2
    print ("result is: ", result)
except SyntaxError:
    print ('comma is required')
except ZeroDivisionError:
    print ('division by zero is not allowed')
except NameError:
    print ('data type string is not acceptable')
else:
    print ('there is no exception')
finally:
    print ('this message will always print, even if there is an exception')

#-------------------------------------------------------------------------------------
# to raise your exceptions from your own methods
# "raise" is a keyword in python
# how to use it: raise ExceptionClass ("Your argument")

def enterage (age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")
    if age % 2 == 0:
        print ("age is an even number")
    else:
        print ('age is an odd number ')

try:
    num = int (input("enter age: "))
    enterage (num)
except ValueError:
    print ("only positive integers please")
except:
    print ('something went wrong')
    
