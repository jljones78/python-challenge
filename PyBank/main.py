import os
import csv

# filepath = os.path.join('~','Users','JLJones','Desktop','bootcamp','UT-MCB-DATA-PT-11-2019-U-C','Homework','02-Python','Instructions','pybank','resources','budgetdata.csv')

#         print(sum(map(int, income_row)))
    
income = []
months = []
with open('budget_data.csv','r') as budget_data:
    budget_csv = csv.reader(budget_data, delimiter=',')
    csv_header = next(budget_csv)
    for row in budget_csv:
        income.append(float(row[1]))
        months.append((row[0]))
    print(sum(income))
    print(len(months))
