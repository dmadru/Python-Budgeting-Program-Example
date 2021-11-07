""" prog4.py   Author: Dylan Madru

This program will allow a user to analyze their ability to balance a budget
for the amount of months that they enter. This program will use functions and
also a for loop. The program begins with asking for how many months that
the user would like to analyze their budget. Then for each month, the user
will input how much they budgeted and how much they spent. The program then
decides wether the user has matched the budget to the amount spent, gone over
the budget, or gone under the budget. The program will then display the
results for each month.
"""

#Define the function describeProgram

def DescribeProgram():
    print(""" This program is to help with budgeting. You will first have
to enter the amount of months that you want to analyze your budget. Then
this program will ask you how much you budgeted and how much you spent
for each month. The program then displays how you did depending on if
you went over, under, or matched your budget.""")

#Get months code goes here
def GetMonths():
    months = int(input("\n\nInput the amount of months you'd like to analyze your budget for:"))
    return months
                   

#Define the function GetMonthBudgetandSpent()
#This function prompts for and reads in from the keyboard
#the amount budgeted and the amount spent for a month and then returns these via the
#function name. 

def GetMonthBudgetandSpent():
    monthBudget = float(input("Enter the amount that you budgeted for this month:"))
    monthSpent = float(input("Enter how much you spent for this month:"))
    return monthBudget,monthSpent 

#Define the function AnalyzeBudget(months)

#This function accepts via an argument, months, that was
#returned from the GetMonths() function and uses months in a for loop that calls the
#GetMonthBudgetandSpent() function within its loop body to get the budget amount and
#amount spent for the month; determines whether the amount spent matches the
#budget amount, the amount spent is over the budget amount, or the amount spent is
#under the budget amount; and then displays the corresponding results. 

def AnalyzeBudget(months):
    for month in range(months):
        print("\nMonth",month + 1,":")
        print("=========")
        monthBudget,monthSpent = GetMonthBudgetandSpent()
        
        print("\nFor month",month + 1,"you budgeted $",format(monthBudget,',.2f'),"and spent $" ,format(monthSpent,',.2f'))
        if monthSpent == monthBudget:
            print("Spending matches budget for month",month + 1,"GOOD PLANNING!")
        elif monthSpent < monthBudget:
            print("For month",month + 1," you were $",format(monthBudget - monthSpent,',.2f')," under budget. WELL DONE!")
        elif monthSpent > monthBudget:
                  print("For month",month + 1," you were $",format(monthSpent - monthBudget,',.2f')," over budget. PLAN BETTER NEXT TIME!")
                  
    
def main():

    DescribeProgram()

    months = GetMonths()

    AnalyzeBudget(months)

    
main()


    
