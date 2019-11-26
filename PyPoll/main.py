import csv

with open("election_data.csv", "r") as election_data:
    election_csv = csv.reader(election_data)
    csv_header = next(election_csv)
    vote_counts = {}
    for row in election_csv:
        voter_ID = row[0]
        candidate_name = row[2]
        if candidate_name in vote_counts:
            vote_counts[candidate_name] += 1
        else:
            vote_counts[candidate_name] = 1
    print(sum(vote_counts.values()))
    print(vote_counts)
    khan_votes = vote_counts["Khan"]
    correy_votes = vote_counts["Correy"]
    li_votes = vote_counts["Li"]
    otooley_votes = vote_counts["O'Tooley"]


# vote_dict[candidate_name] = voter_ID

# for candidate_name in vote_dict.items():
#     candidate = candidate_name[0]
#     print(candidate)


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

