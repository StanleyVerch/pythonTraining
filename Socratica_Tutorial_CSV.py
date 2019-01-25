# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:02:14 2019

@author: Stanley
"""
dataFile = 'Google Stock Market Data.csv'
lines = [line for line in open(dataFile)]
print(lines[0])
print(lines[1])

print(lines[0].strip())
print(lines[0].strip().split(','))
dataset= [line.strip().split(',') for line in open(dataFile)]
print(dataset[0])
print(dataset[1])


file = open(dataFile)

for line in file:
    print(line,end='')
file.close()

import csv
from datetime import datetime

print(dir(csv)) # what is in csv module

print("\n\ncsv file")
with open(dataFile,'r', newline='') as csvFile:
    reader = csv.reader(csvFile)
    header =  next(reader)
    data =[row for row in reader]
    print(header)
    print(data[0])
        
print("\n\ncsv file")
data = []
with open('Google Stock Market Data.csv','r') as csvFile:
    reader = csv.DictReader(csvFile)
    for line in reader:
        date = datetime.strptime(line['Date'],'%m/%d/%Y')
        high = float(line['High'])
        low = float(line['Low'])
        close = float(line['Close'])
        volume = float(line['Volume'])
        adjClose = float(line['Adj Close'])
        data.append([date,high,low,close,volume,adjClose])
        
with open('GoogleReturns.csv', 'w',newline='') as csv_out:
    writer = csv.writer(csv_out)
    writer.writerow(["Date","Return"])
    
    for i in range(len(data)-1):
        todays_row = data[i]
        yesterdays_row = data[i+1]
        todays_date = todays_row[0]
        todays_price = todays_row[-1]
        yesterdays_price = yesterdays_row[-1]
        daily_return =  (todays_price - yesterdays_price)/yesterdays_price;
        formatted_date = datetime.strftime(todays_date,'%m/%d/%Y')
        writer.writerow([formatted_date,daily_return])
    