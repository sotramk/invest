#!/bin/python

# Program to calculate the spread between two prices

# Get information from user

prompt = 'What is the current price?\n'
currentPrice = input(prompt)
currentPrice = float(currentPrice)
prompt = 'What is the target price?\n'
targetPrice = input(prompt)
targetPrice = float(targetPrice)

# calculate percentage difference of prices
if currentPrice > targetPrice:
    result = (currentPrice / targetPrice - 1) * 100
    result = float(result)
else:
    result = (targetPrice / currentPrice - 1) * 100
    result = float(result)
print('Difference is ',round(result,2),' percent')

