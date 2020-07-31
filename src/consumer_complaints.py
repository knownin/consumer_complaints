""" Goal: For this challenge, we want to know for each financial product and year,
 the total number of complaints, number of companies receiving a complaint, 
 and the highest percentage of complaints directed at a single company.
 """

import csv
import os

"product_year={(product,year): [complaints_count, company_count, {company_name: frequency of the complaints at the company, ...}]}"
"inside, complaints_count: # of complaints received for that product and year."
"inside, company_count: the # of distinct companies receiving a complaint for the product and year."
product_year=dict()

#first, we read the input file and extract the parameters into the right locations of the variable created above.
with open("./input/complaints.csv", "rU") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  #skip the first title line.
    for lines in csv_reader:
      #(lines[0], lines [1], lines[7]) are the three columns to our interest: date, product, company.      
      product = lines[1].lower()
      company = lines[7].lower()
      year = lines[0][0:4]
      if (product, year) not in product_year.keys(): #case 1: product and year is not recorded yet.
        product_year[(product, year)] = [1,1,{company:1}]        
      else: #Case 2: if the product/year is already present in the dict.
        product_year[(product, year)][0]+=1 #we increment the corresponding value of the # of complaints for this combino
      	if company not in product_year[(product, year)][2].keys(): #Case 2.1: if the company that receives the complaint is new for the product/year.         
          product_year[(product, year)][1]+=1
          product_year[(product, year)][2][company]=1
        else: #Case 2.2: the company is already present in the dict for the product/year, so we increment its count for percentage in company_name_count, but leave the company_count.
      		product_year[(product, year)][2][company]+=1

#Second, we write the raw analysis result into the output file: 
with open('unsortedreport.csv', 'w') as file:
    writer = csv.writer(file)
    for key in product_year: 
      maxfrequency = max (product_year[key][2].values()) # find the max of frequencies of complaints received by one company for the given product/year.
      maxrf = int(round(maxfrequency / float(product_year[key][0]), 2)*100) 		  
      writer.writerow([key[0],int(key[1]), product_year[key][0], product_year[key][1], maxrf])
  
#Third, we sort the unsortedreport.csv first by first column[product]; then by second column [year]:
with open('unsortedreport.csv', mode='rt') as f, open('./output/report.csv', 'w') as final:
    writer = csv.writer(final, delimiter=',')
    reader = csv.reader(f, delimiter=',')
    sorted2 = sorted(reader, key=lambda column: (column[0], int(column[1])))        
    for row in sorted2:
        writer.writerow(row)

#Last, we remove the unsorted version of the output csv file. 
os.remove('unsortedreport.csv')  
