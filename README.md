# Consumer Complaints

## Table of Contents
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Expected output](README.md#expected-output)
1. [Testing the code](README.md#testing-your-code)

## Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This project builds the tool to identify the number of complaints filed and how they're spread across different companies. 

**In particular, this project will analyze the input complaint.csv file and extracts the following information: for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company. 

## The Approach
1. The source code included in this project is written in the langauge of Python 2. 
2. The source code uses only the built-in data structure modules that are in the standard Python 2 library, including csv and os. 
3. The source code consists of functional modules that are separated by comments explaining their respective purposes.
4. In terms of the data strutures used, the source code use a composite dictionary to store the relevant information, where each key is a unique combination of product and year and each value is list of three elements: [the # of complaints that the product and year receives, the # of distinct companies that the product and year receives, an inner dictionary where the keys are the names of all companies receives complaints for the product and year and the values are the corresponding # of complaints each of them receives].
 
  ** The point of using a dictionary for this program is mainly based on its time effciciency (average O(1)) for searching keys, and adding new entries, and its space effciency in   not having a fixed size. 


## Input dataset
To run this program, move an input file, `complaints.csv`, to the top-most `input` directory of the repository. The format of the input file can be found in the testing input files inlcuded in the top-most `insight_testsuite` directory. The code will process it and write the results to an output file, `report.csv` that will be placed in the top-most `output` directory of the repository.

## Expected output
After reading and processing the input file, the code will create an output file, `report.csv`, with as many lines as unique pairs of product and year (of `Date received`) in the input file. 

Each line in the output file lists the following fields in the following order:
* product (name should be written in all lowercase)
* year
* total number of complaints received for that product and year
* total number of companies receiving at least one complaint for that product and year
* highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Use standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, should round to 1% and anything less than 0.5% should round to 0%)

The lines in the output file are sorted by product (alphabetically) and year (ascending).

## Testing the code
Under the top-most `insight_testsuite` directory, there are multiple tests for the code, a separate folder for each test. Each test folder has a separate `input` subdirectory containing the `complaint.csv` input file, and an `output` subdirectory containing the expected `report.csv` output for that test.

The test (`test_1`) is given by the original code challenge.
