
import csv
import os

#folder path
filepath = os.path.join("Resources", "Unit 3 - Python_Homework_Instructions_PyBank_Resources_budget_data.csv")

#read csv file in folder
with open(filepath, 'r') as input_file:
    csvreader = csv.reader(input_file,delimiter=",")
# create variables - skip header
    header = next(csvreader)
    date = []
    Budget = []
    Change_dif = []
    greatest_inc= 0
    greatest_dec= 0
    
    first_row = next(csvreader)
    Previous_num = int(first_row[1])
    Total_Tot = 0
    Total_Tot = Total_Tot + int(first_row[1])
    
    # loop through to find out and output data results
    for row in csvreader:
        date.append(row[0])
        Budget.append(int(row[1]))
        Total_Tot = Total_Tot + int(row[1])
        Change = int(row[1]) - Previous_num
        Previous_num = int(row[1])
        Change_dif = Change_dif + [Change]
        Num_Months = len(date)+1
        if Change > greatest_inc:
            greatest_inc = Change
            greatest_inc_mon = row[0]
        
        if Change < greatest_dec:
            greatest_dec = Change
            greatest_dec_mon = row[0]

#get rounded average
Average = round(sum(Change_dif) / len(Change_dif),2)

#print results and output txt 
Header_out = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
)

print(Header_out)
print(f"Total Months: {(Num_Months)}\n")
print(f"Total: ${Total_Tot}\n")
print(f"Average Change: ${Average}\n")
print(f"Greatest Increase in Profits: {greatest_inc_mon} (${greatest_inc})\n")
print(f"Greatest Decrease in Profits: {greatest_dec_mon} (${greatest_dec})\n")

with open("pb_output.txt", 'w') as txt_output:
    txt_output.write(Header_out)
    txt_output.write(f"Total Months: {(Num_Months)}\n")
    txt_output.write(f"Total: ${Total_Tot}\n")
    txt_output.write(f"Average Change: ${Average}\n")
    txt_output.write(f"Greatest Increase in Profits: {greatest_inc_mon} (${greatest_inc})\n")
    txt_output.write(f"Greatest Decrease in Profits: {greatest_dec_mon} (${greatest_dec})\n")
