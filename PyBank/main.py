#importing os so we can navigate in the file system to the folder where the csv is
import os
#importing CSV so we can open the CSV
import csv

#going to the resources folder
os.chdir("Resources")

#setting up two lists, one for the dates and one for the dollar amounts
dates = []
profits = []

#go through the CSV file, adding each line to the two lists
with open("budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #skipping the headers
               line_count = line_count + 1
        else:
            dates.append(row[0])
            profits.append(row[1])
            line_count = line_count + 1

#var for finding out the total net total
total_money = 0

#vars for figuring out the monthly change
current_profit = 0
current_month = None
last_profit = 0
last_month = None

#setting up variables for tracking monthly changes
current_change = 0
greatest_gain = 0
greatest_gain_month = None
greatest_loss = 0
greatest_loss_month = None
average_change_total = 0

#looping through the lists
for x in range(len(profits)):
    #figuring the net total value
    total_money = total_money + int(profits[x])
    #setting the current month for comparing to the last month
    current_month = dates[x]
    current_profit = profits[x]
    #figuring the change
    current_change = int(current_profit) - int(last_profit)
    #adding changes together to figure the average change
    average_change_total =+ (int(current_profit) - int(last_profit))
    
    #if the change is bigger than the greatest gain ever, saving to greatest gain
    if (int(current_change) > int(greatest_gain)):
        greatest_gain = current_change
        greatest_gain_month = current_month
    #if the chane is lesser than the greatest loss ever, saving to the greatest loss
    elif (int(current_change) < int(greatest_loss)):
        greatest_loss = current_change
        greatest_loss_month = current_month

    #setting the current to the last before we move onto the next row
    last_month = current_month
    last_profit = current_profit

#printing results to screen
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(dates)))
print("Total: $" + str(total_money))
print("Average Change: $" + str(round(average_change_total / len(profits), 2)))
print("Greatest Increase in Profits: " + str(greatest_gain_month) + " ($" + str(greatest_gain) + ")")
print("Greatest Decrease in Profits: " + str(greatest_loss_month) + " ($" + str(greatest_loss) + ")")

#navigating to analysis folder
os.chdir("..")
os.chdir("Analysis")

#printing to .txt
file1 = open("output.txt", "w")
file1.write("Financial Analysis")
file1.write("\n")
file1.write("----------------------------")
file1.write("\n")
file1.write("Total Months: " + str(len(dates)))
file1.write("\n")
file1.write("Total: $" + str(total_money))
file1.write("\n")
file1.write("Average Change: $" + str(round(average_change_total / len(profits), 2)))
file1.write("\n")
file1.write("Greatest Increase in Profits: " + str(greatest_gain_month) + " ($" + str(greatest_gain) + ")")
file1.write("\n")
file1.write("Greatest Decrease in Profits: " + str(greatest_loss_month) + " ($" + str(greatest_loss) + ")")
file1.close()
print("Writing to output.txt in the Analysis folder!")