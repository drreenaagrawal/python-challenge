import os, csv

csv_path = os.path.join('..', 'Resources', 'budget_data.csv')

col_profit_loss = [] 
#array to hold the profit/loss column from the csv file
change = [] 
#array to hold the change in profit/loss
column_month = [] 
#array to hold the column of months

f = open("outputbank.txt", "a") 
#open text file outputbank.txt to store output

print("'''text", file = f)
print("Financial Analysis", file = f)
print("Financial Analysis")
print("-"*25, file = f )
print("-"*25)
#print title for the text file

with open(csv_path, newline="", encoding="UTF8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
#open and read csv file
    next(csv_reader)
#moves over the header row
    for row in csv_reader:
        col_profit_loss.append(row[1])
        #appends the second column of the csv file to col_profit_loss
        column_month.append(row[0])
        #appends the first column of the csv file to column_month

    print(f"Total months: {len(col_profit_loss)}", file = f)
    print(f"Total months: {len(col_profit_loss)}")
    #print total number of months
    sum_profit_or_loss = sum(int(i) for i in col_profit_loss)
    print(f"Total: ${sum_profit_or_loss}", file = f)
    print(f"Total: ${sum_profit_or_loss}")
    #print total profit/loss

    for i in range(1,len(col_profit_loss)):
        change.append(int(col_profit_loss[i]) - int(col_profit_loss[i-1]))
    #determine change in profit/loss and append it to column change
    sum_change = sum(i for i in change)

    average_change = round(sum_change / len(change),2)
    print(f"Average Change: ${average_change}", file = f)
    print(f"Average Change: ${average_change}")
    #max(change) gives greatest increase in profits
    #min(change) gives the greatest decrease in profits

    index1 = change.index(max(change)) + 1
    print(f"Greatest Increase in Profits: {column_month[index1]} (${max(change)})", file = f)
    print(f"Greatest Increase in Profits: {column_month[index1]} (${max(change)})")
    index2 = change.index(min(change)) + 1
    print(f"Greatest Decrease in Profits: {column_month[index2]} (${min(change)})", file = f)
    print(f"Greatest Decrease in Profits: {column_month[index2]} (${min(change)})")
    print("'''", file = f)
f.close()
