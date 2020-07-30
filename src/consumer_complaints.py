""" Goal: For this challenge, we want to know for each financial product and year,
 the total number of complaints, number of companies receiving a complaint, 
 and the highest percentage of complaints directed at a single company.
 """

import csv
import os

#keep track all unique combinaiton of product/year.
product_year=[]
# of complaints received for that product and year of the same index.
complaints_count=[]
#the number of distinct companies receiving a complaint for the product and year of the same index.
company_count=[]
#each element corresponds to a dict of all diffrent companies receiving the corresponding product/year complaints with its complaint count.
company_name_count=[]

#first, we read the input file and extract the parameters into the variables created above.
with open("complaints.csv", "rU") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  #skip the first line.
    for lines in csv_reader:
      #(lines[0], lines [1], lines[7]) are the three columns to out interest: date, product, company.      
      
      if (lines[1], lines[0][0:4]) not in product_year: #case 1: product and year is not recorded yet.
        product_year.append((lines[1],lines[0][0:4]))
      	complaints_count.append(1)
      	company_count.append(1)
      	company_name_count.append({lines[7]:1})
        
      else: #Case 2: that is if the product/year is already present in the list.
        complaints_count[product_year.index((lines[1], lines[0][0:4]))]+=1 #we increment the corresponding value of the # of complaints for this combino
      	if lines[7] not in company_name_count[product_year.index((lines[1], lines[0][0:4]))].keys(): #Case 2.1: if the company that receives the complaint is new for the product/year.     		
      		company_name_count[product_year.index((lines[1], lines[0][0:4]))][lines[7]] = 1
      		company_count[product_year.index((lines[1], lines[0][0:4]))]+=1
        else: #Case 2.2: the company is already present in the complaint list for the product/year, so we increment its count for percentage in company_name_count, but leave the company_count.
      		company_name_count[product_year.index((lines[1], lines[0][0:4]))][lines[7]]+=1


#Second, we write the raw analysis result into the output file: 
with open('unsortedreport.csv', 'w') as file:
    writer = csv.writer(file)
    for i in range(len(product_year)): 
		maxfrequency = max(company_name_count[i].values())
		maxrf = int(round(maxfrequency / float(complaints_count[i]), 2)*100) 
		writer.writerow([product_year[i][0], int(product_year[i][1]), complaints_count[i], company_count[i], maxrf])


#Third, we sort the unsortedreport.csv first by first column[product]; then by second column [year]:

with open('unsortedreport.csv', mode='rt') as f, open('report.csv', 'w') as final:
    writer = csv.writer(final, delimiter=',')
    reader = csv.reader(f, delimiter=',')
    sorted2 = sorted(reader, key=lambda column: (column[0], int(column[1])))        
    for row in sorted2:
        writer.writerow(row)

#Last, we remove the unsorted version of the output csv file. 
os.remove('unsortedreport.csv')  