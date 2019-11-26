import csv


vote_dict = {}
with open("election_data.csv", "r") as election_data:
    election_csv = csv.reader(election_data)
    csv_header = next(election_csv)
    for row in election_csv:
        voter_ID = row[0]
        candidate = row[2]
        vote_dict[candidate] = voter_ID

    for candidate in vote_dict.items():
        print(candidate[0])


#     budget_csv = csv.reader(budget_data)
#     csv_header = next(budget_csv)
#     for row in budget_csv:
#         income_dict[int(row[1])] = row[0]

#     # establish variables for solution
#     max_income = max(income_dict)
#     min_income = min(income_dict)
#     total_income = sum(income_dict)
#     avg_chg_round = round(total_income / len(income_dict), 2)

# # print results
# print("\nFinancial Analysis\n----------------------------")
# print("Total Months: " + str(len(income_dict)))
# print("Total: $" + str(sum(income_dict)))
# print("Average Change: $" + str(avg_chg_round))
# print(
#     "Greatest Increase in Profits: "
#     + income_dict[max_income]
#     + " $("
#     + str(max_income)
#     + ")"
# )
# print(
#     "Greatest Decrease in Profits: "
#     + income_dict[min_income]
#     + " $("
#     + str(min_income)
#     + ")"
# )

