import pandas as pd
import argparse

# create a parser object
parser = argparse.ArgumentParser(description="Total up unique category types on all transactions from GNTY.com")

parser.add_argument("-i", "--input", type=str, nargs=1,
                    metavar="filename", default=None, required=True,
                    help="Opens and reads the specified CSV file.")

parser.add_argument("-o", "--output", type=str, nargs=1,
                    metavar="filename", default=None, required=True,
                    help="Saves the specified CSV file.")

# parse the arguments from standard input
args = parser.parse_args()

# Assingn arguments passed in
input_file = args.input[0]
output_file = args.output[0]

try:
    df = pd.read_csv(input_file)
except:
    print("Could not open file: %s",input_file)

# Total up all unique categories
df_new = df.groupby(['Category']).sum()

# Convert all Amounts to Positive Numbers
for index, row in df_new.iterrows():
    if row['Amount'] < 0.00:
        row['Amount'] = row['Amount'] * -1.00

df_new = df_new.sort_values(by='Amount',ascending=False)
df_new = df_new.reset_index()

# Create a new dataframe with only Category and Amount for columns
calculated_df = df_new[['Category', 'Amount']]
print(calculated_df)

try:
    # Save to CSV file without the index column
    calculated_df.to_csv(output_file,index=False)
except:
    print("Could not save to file: %s", output_file)