from cgitb import text
from inspect import ClosureVars
import os
import csv
import pathlib

budget_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources','budget_data.csv' )

#print(budget_csv_path)


#reads through the csv file and creates a list of the values in the Profits/Losses column
with open(budget_path) as interactor:
    reader = csv.reader(interactor, delimiter = ",")
    header = next(interactor)

    #variable for storing the number of months
    months = 0

    #variable for storing the total profits
    total_profit = 0

    #these lists will eventually hold all the values from the csv
    #profits -> profit_list and months -> month_list
    profit_list = []
    month_list = []

    #reads the csv file
    for row in reader:
        
        #counts the number of months
        months += 1

        #sums all of th profits together
        total_profit += int(row[1])

        
        profit_list.append(int(row[1])) #adds profit value to a list
        month_list.append(str(row[0])) #adds the months to a list


#uses a while loop to create a list of the profit changes
#also saves the highest and lowest change in profits between months
#and will record the date in which the highest/lowest change occured

profit_changes = [] #used for storing all of the changes in profits between months
largest_increase = 0
largest_decrease = 0

largest_increase_month = ""
largest_decrease_month = ""

x = 0
while x < months:

    if x > 0:
        change = (profit_list[x] - profit_list[x-1])

        if change > largest_increase:
            largest_increase = change 
            largest_increase_month = month_list[x]           

        if change < largest_decrease:
            largest_decrease = change
            largest_decrease_month = month_list[x]

        profit_changes.append(change)

    x += 1

#calculates the average change across months in our list of changes
#and rounds to 2 decimal places
average_change = round(sum(profit_changes) / len(profit_changes),2)

output_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "analysis", "analysis.txt" )

output_line_1 = "Total Months: " + str(months)
output_line_2 = "Total: $" + str(total_profit)
output_line_3 = "Average Change: " + str(average_change)
output_line_4 = "Greatest Increase in Profits: " + str(largest_increase) + " " + str(largest_increase_month)
output_line_5 = "Greatest Decrease in Profits: " + str(largest_decrease) + " " + str(largest_decrease_month)

full_output = ["Financial Analysis", "", output_line_1, output_line_2, output_line_3, output_line_4, output_line_5]

with open(output_path, 'w') as output_interactor:

    for line in full_output:
        output_interactor.write(line)
        output_interactor.write("\n")
        


for line in full_output:
    print(line)
