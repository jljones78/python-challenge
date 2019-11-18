import csv

# filepath = os.path.join('~','Users','JLJones','Desktop','bootcamp','UT-MCB-DATA-PT-11-2019-U-C','Homework','02-Python','Instructions','pybank','resources','budgetdata.csv')



# with open('budget_data.csv','r') as budget_data:
#     budget_csv = csv.reader(budget_data)
#     header = next(budget_data)
#     for row in budget_csv:
#         income_row = row[1]
#         print(sum(map(int, income_row)))
    
# with open('budget_data.csv','r') as budget_data:
#     budget_csv = csv.reader(budget_data)
#     header = next(budget_data)
#     for row in budget_csv:
#         income_row = row[1]
#         if income_row[:1] == '-':
#             neg_income = income_row.replace('-','')
#             print(sum(map(int, neg_income)))

with open('budget_data.csv','r') as budget_data:
    budget_csv = csv.reader(budget_data)
    header = next(budget_data)
    for row in budget_csv:
        income_row = row[1]
        if income_row[:1] == '-':
            neg_income = income_row.replace('-','')

