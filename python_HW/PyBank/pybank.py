#pybank - python HW
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#* The total number of months included in the dataset
#* The total amount of revenue gained over the entire period
#* The average change in revenue between months over the entire period
#* The greatest increase in revenue (date and amount) over the entire period

#Notes
""" two coulunms same headers use dicts 
- loops need starter numbers
- cast rev as int

"""
# import dependencis
import csv
import os       #(os not needed for this)

# paths for read and write
data_1_path = "raw_data/budget_data_1.csv"
revenue_output_path = "Revenue/budget_analysis_1.txt"

# set counters for calculations
total_months = 0
prev_revenue = 0
total_revenue = 0

#Make lists for output and new data
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the csv and convert it into a list of dictionaries
with open(data_1_path) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        # Track the total months included
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
        total_revenue2 = '{:,}'.format(total_revenue)

        # Track the revenue change from prior month
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change] #Dan
        month_of_change = month_of_change + [row["Date"]]  
       


        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
          
        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change
          
# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
revenue_avg2 = '{:,.0f}'.format(revenue_avg)

# Generate Output Summary
# ** changed the output format for the end user

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months included: {total_months}\n"
    #f"Total Revenue for {total_months} months : ${total_revenue}\n"
    f"Total Revenue for {total_months} Months   : ${total_revenue2}\n"
    #f"Average Monthly Revenue Change: ${float(revenue_avg)}\n"
    f"Average Monthly Revenue Change:     ${revenue_avg2}\n"   
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(revenue_output_path, "w") as txt_file:
    txt_file.write(output)
