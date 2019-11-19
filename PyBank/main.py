import os
import csv

# filepath = os.path.join('~','Users','JLJones','Desktop','bootcamp','UT-MCB-DATA-PT-11-2019-U-C','Homework','02-Python','Instructions','pybank','resources','budgetdata.csv')

#         print(sum(map(int, income_row)))
    

# with open('budget_data.csv','r') as budget_data:
#     budget_csv = csv.reader(budget_data)
#     header = next(budget_data)
#     for line in budget_data:
#         row = line.strip().split(",")
#         date_row = row[0]
#         income_row = row[1]


all_income = []
with open('budget_data.csv','r') as budget_data:
    budget_csv = csv.reader(budget_data, delimiter=',')
    csv_header = next(budget_csv)
    for row in budget_csv:
        all_income.append(int(row[1]))
    print(sum(all_income))





        # if income_row[:1] == '-':
        #     neg_income = income_row.replace('-','')


