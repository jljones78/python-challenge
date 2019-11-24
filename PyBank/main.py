import csv


# filepath = "https://github.com/the-Coding-Boot-Camp-at-UT/UT-MCB-DATA-PT-11-2019-U-C/tree/master/Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv"
income_dict = {}
with open("budget_data.csv", "r") as budget_data:
    budget_csv = csv.reader(budget_data)
    csv_header = next(budget_csv)
    for row in budget_csv:
        income_dict[int(row[1])] = row[0]

    # establish variables for solution
    max_income = max(income_dict)
    min_income = min(income_dict)
    total_income = sum(income_dict)
    avg_chg_round = round(total_income / len(income_dict), 2)

# print results
print("\nFinancial Analysis\n----------------------------")
print("Total Months: " + str(len(income_dict)))
print("Total: $" + str(sum(income_dict)))
print("Average Change: $" + str(avg_chg_round))
print(
    "Greatest Increase in Profits: "
    + income_dict[max_income]
    + " $("
    + str(max_income)
    + ")"
)
print(
    "Greatest Decrease in Profits: "
    + income_dict[min_income]
    + " $("
    + str(min_income)
    + ")"
)

