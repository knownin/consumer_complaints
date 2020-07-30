# Consumer Complaints

To do:
summarize your approach and run instructions (if any) in your README.


## Table of Contents
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Expected output](README.md#expected-output)
1. [Instructions](README.md#instructions)
1. [Testing your code](README.md#testing-your-code)

## Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This project builds the tool to identify the number of complaints filed and how they're spread across different companies. 

**In particular, this project will analyze the input complaint.csv file and extracts the following information: for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company. 

## The Approach
1. The source code included in this project is written in the langauge of Python 2. 
2. The source code uses only the built-in data structure modules that are built into the standard Python 2 library, including csv, sys, fileinput, and os.  
3. The source code consists of functional modules that are separated by comments explaining their respective purposes. 


## Input dataset
To run this program, move an input file, `complaints.csv`, to the top-most `input` directory of the repository. The code will process it and write the results to an output file, `report.csv` that will be placed in the top-most `output` directory of the repository.

Below are the contents of an example `complaints.csv` file: 
```
Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24,Debt collection,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
2019-10-24,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
```
Each line of the input file, except for the first-line header, represents one complaint. Consult the [Consumer Finance Protection Bureau's technical documentation](https://cfpb.github.io/api/ccdb/fields.html) for a description of each field.  

* Notice that complaints were not listed in chronological order
* In 2019, there was a complaint against `TRANSWORLD SYSTEMS INC` for `Debt collection` 
* Also in 2019, `Experian Information Solutions Inc.` received one complaint for `Credit reporting, credit repair services, or other personal consumer reports` while `TRANSUNION INTERMEDIATE HOLDINGS, INC.` received two
* In 2020, `Experian Information Solutions Inc.` received a complaint for `Credit reporting, credit repair services, or other personal consumer reports`

In summary that means 
* In 2019, there was one complaint for `Debt collection`, and 100% of it went to one company 
* Also in 2019, three complaints against two companies were received for `Credit reporting, credit repair services, or other personal consumer reports` and 2/3rd of them (or 67% if we rounded the percentage to the nearest whole number) were against one company (TRANSUNION INTERMEDIATE HOLDINGS, INC.)
* In 2020, only one complaint was received for `Credit reporting, credit repair services, or other personal consumer reports`, and so the highest percentage received by one company would be 100%

For this challenge, we want for each product and year that complaints were received, the total number of complaints, number of companies receiving a complaint and the highest percentage of complaints directed at a single company.

For the purposes of this challenge, all names, including company and product, should be treated as case insensitive. For example, "Acme", "ACME", and "acme" would represent the same company.

## Expected output

After reading and processing the input file, your code should create an output file, `report.csv`, with as many lines as unique pairs of product and year (of `Date received`) in the input file. 

Each line in the output file should list the following fields in the following order:
* product (name should be written in all lowercase)
* year
* total number of complaints received for that product and year
* total number of companies receiving at least one complaint for that product and year
* highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Use standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, should round to 1% and anything less than 0.5% should round to 0%)

The lines in the output file should be sorted by product (alphabetically) and year (ascending)

Given the above `complaints.csv` input file, we'd expect an output file, `report.csv`, in the following format
```
"credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100
```
Notice that because `debt collection` was only listed for 2019 and not 2020, the output file only has a single entry for debt collection. Also, notice that when a product has a comma (`,`) in the name, the name should be enclosed by double quotation marks (`"`). Finally, notice that percentages are listed as numbers and do not have `%` in them.

## Instructions



## Testing your code
As an engineer, you'll want to make sure you are thoroughly testing your code. Use the `insight_testsuite` directory to showcase the tests you conducted on your code. Under that directory, create a separate folder for each test. Each test directory should also have a separate `input` subdirectory containing the `complaint.csv` input file you want to test, and an `output` subdirectory containing the expected `report.csv` output for that test.

We've included one test (`test_1`), which contains the sample input and output files detailed in this Readme. To test your code, you can manually move each input test file into the top-level input directory, then run your program and compare the output with the expected output. Or you can write a script to do this automatically, but note we are not requiring you to write a test script.

We do ask that you test your code using the <a href="https://insight-cc-submission.com/test-my-repo-link">web page</a> mentioned earlier to ensure your code can run in the Linux environment that we will review your code. The test page will check to see if your code passes `test_1`. If there are errors or if the results don't match what is expected, you should debug your code's behavior by yourself. If you receive system errors that you do not believe are due to your code, you can email cc@insightdataengineering.com for help.

If your code must be compiled to run (e.g., javac, make), that compilation (as well as the execution) of your code must be specified in the `run.sh` script of your code repository. 

For Python programmers, you can use Python 2 or Python 3. If you use the former, specify `python` in your `run.sh` script, or if you use the later, specify `python3`, which defaults to Python 3.5.2. Other options that could be use are `python3.7` or `python3.8`.

