#Write a program that asks the user to enter the amount s/he has
#budgeted for a month. A loop should  then prompt the user to enter each
#of the expenses for  the month and keep a running total. When the loop
#finishes, the program should display the amount that the user is over
#or under budget.  
##________________________________________________________________________________
#Hints
#Declare variables to store the budget amount, amount spent,difference,and total

budget = 0.0
difference = 0.0
total = 0.0
spent = 1.0
expense = 0.0
expenseTotal = 0.0
more = 'y'#initialize for while loop
#Get the budgeted amount from the user (has to be a float)
budget = float(input("What is your budget for the month?:"))
print("Please begin entering the amounts of each of your monthly expenses:")
#Get the total amount spent from the user (while statement starts, make sure
#to enter exit criteria)
while more == 'y':
    expense = float(input("Monthly expense amount? $:"))
#Determine whether the user is over or under budget, and display the result
    total = total + expense
    more =  input("Do you have any other expenses?: Type y for yes, any key for no:")
#(use formatting: 2f) print what was the budgeted amount.print what was the
#amount spent
if expense < budget:
    difference = budget - expense
    print("You are under budget by", "$" + format(difference, '.2f'))
elif expense > budget:
    difference = expense - budget
    print("You are over budget by", "$" + format(difference, '.2f'))
    
else:
    print("You were right on budget. Great Job!!!", "$" + format(difference,+\
                                                                 '.2f'))
    input("Press enter to exit.")
