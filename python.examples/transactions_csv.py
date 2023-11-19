# importing csv module
import csv

filename = "transactions.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')  

    fields = csvreader.fieldnames

    for row in csvreader:
        rows.append(row)

    print("Total no. of rows: %d" % csvreader.line_num)

print('Field names are:' + ', '.join(field for field in fields))

def analyze_first_digits(data):
    digit_counts = {str(i): 0 for i in range(1, 10)}

    for row in data:
        value = row["value"] 
        first_digit = str(value)[0]

        if first_digit in digit_counts:
            digit_counts[first_digit] += 1

    print("Statistics of first digits:")
    for digit, count in digit_counts.items():
        print(f"Digit {digit}: {count} occurrences")

analyze_first_digits(rows)
