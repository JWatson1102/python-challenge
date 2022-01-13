import os
import csv
import pathlib

budget_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources','budget_data.csv' )

#print(budget_csv_path)


#reads through the csv file and creates a list of the values in the Profits/Losses column
with open(budget_path) as interactor:
    reader = csv.reader(interactor, delimiter = ",")
    header = next(interactor)

    months = 0
    total_profit = 0

    profit_list = []
    month_list = []

    for row in reader:
        months += 1
        total_profit += int(row[1])

        profit_list.append(int(row[1]))
        month_list.append(str(row[0]))


#uses a while loop to create a list of the profit changes
#also saves the highest and lowest change in profits between months
#and will record the date in which the highest/lowest change occured

profit_changes = []
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


        


print(f"Over a period of {months} months")
print(f"we made ${total_profit} in net profit!")

print(f"The average change in our profits across months was {average_change}.")
print(f"The largest increase in profits was {largest_increase} in {largest_increase_month} and the largest decrease was {largest_decrease} in {largest_decrease_month}.")


