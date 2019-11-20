import os
import csv

# filepath = os.path.join('~','Users','JLJones','Desktop','bootcamp','UT-MCB-DATA-PT-11-2019-U-C','Homework','02-Python','Instructions','pybank','resources','budgetdata.csv')


    
income = []
months = []
income_dict = {}
with open('budget_data.csv','r') as budget_data:
    budget_csv = csv.reader(budget_data)
    csv_header = next(budget_csv)
    for row in budget_csv:
        income.append(int(row[1]))
        months.append((row[0]))
        income_dict[int(row[1])] = row[0]
    avg_chg = round(((sum(income)/len(income))),2)
    max_income = max(income_dict)
    min_income = min(income_dict)

# print results
    print('\nFinancial Analysis\n----------------------------')
    print('Total Months: ' + str(len(months)))
    print('Total: $' + str(sum(income)))
    print('Average Change: $' + str(avg_chg))
    print('Greatest Increase in Profits: ' + income_dict[max_income] + ' $' + str(max_income))
    print('Greatest Decrease in Profits: ' + income_dict[min_income] + ' $' + str(min_income))
