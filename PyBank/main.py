import os
import csv
import pandas as pd
import numpy as np

fileloc = '/Users/laurahawkins/Desktop/vanderbilt homework files/Homework/3 - Python Homework'
budget_df = pd.read_csv(fileloc, encoding="UTF-8")

months = budget_df.shape[0]

pl_total = budget_df["Profit/Losses"].sum()

budget_df["pl_difference"] = budget_df["Profit/Losses"] - budget_df["Profit/Losses"].shift(1)

avg_change = budget_df["pl_difference"].mean()

max_change = budget_df["pl_difference"].max()

min_change = budget_df["pl_difference"].min()

max_change_output = budget_df[budget_df["pl_difference"] == max_change]

pl_date_max = max_change_output.iloc[0]["Date"]
pl_difference_max = max_change_output.iloc[0]["pl_difference"]

min_change_output = budget_df[budget_df["pl_difference"] == min_change]

pl_date_min = min_change_output.iloc[0]["Date"]
pl_difference_min = min_change_output.iloc[0]["pl_difference"]

pl_max = (str(pl_date_max) + " $" + str(round(pl_difference_max)))
pl_min = (str(pl_date_min) + " $" + str(round(pl_difference_min)))

print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: " + "$" + str(pl_total))
print("Average Change: " + "$" + str(round(avg_change, 2)))
print("Greatest Increase in Profits: " + str(pl_max))
print("Greatest Decrease in Profits: " + str(pl_min))

f= open("PyBank Results", 'w+')

line1 = "Financial Analysis" + "\n"
line2 = "----------------------------" + "\n"
line3 = "Total Months: " + str(months) + "\n"
line4 = "Total: " + "$" + str(pl_total)
line5 = "Average Change: " + "$" + str(round(avg_change, 2)) + "\n"
line6 = "Greatest Increase in Profits: " + str(pl_max) + "\n"
line7 = "Greatest Decrease in Profits: " + str(pl_min) + "\n"

f.writelines([line1, line2, line3, line4, line5, line6, line7])

f.close()