# GNTY Budget Calculating
The python script takes in an exported CSV file from gnty.com online banking. The script then calculates all unique
transaction descriptions and sum them up. This is accomplished by leveraging the pandas groupby function. The script
then saves to a new CSV file.

## How to run
```
python budget.py -i <input_filename> -o <output_filename>
```

## Help Menu
```
puython budget.py --help
```
```
budget.py [-h] -i filename -o filename

Total up unique category types on all transactions from GNTY.com

optional arguments:
  -h, --help            show this help message and exit
  -i filename, --input filename
                        Opens and reads the specified CSV file.
  -o filename, --output filename
                        Saves the specified CSV file.
```
