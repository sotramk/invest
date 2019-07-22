#!/bin/python
# rewrite of loss_calc.py

stk = input('Stock symbol?')
stku = stk.upper()
prompt = 'What is the buy_price price?\n'
buy_price = input(prompt)
buy_price = float(buy_price)
firstTarget = buy_price * 1.05
firstTarget = round(firstTarget,2)
secoundTarget = buy_price  * 1.10
secoundTarget = round(secoundTarget,2)
thirdTarget = buy_price * 1.23
thirdTarget = round(thirdTarget,2)
print('For a purchase price of ',buy_price)
print('First target ',firstTarget)
txt1 = "First target -- {}".format(firstTarget)
print('Secound target ',secoundTarget)
txt2 = "Secound target -- {}".format(secoundTarget)
print('Third target ',thirdTarget)
txt3 = "Third target -- {}".format(thirdTarget)
pct = ( (.97, .96, .95, .94, .93, .92) )
y = 3

f = open("lcTest.txt", "a")
f.write("\n")
txt = "{} -- {}".format(stku,buy_price)
f.write(txt)
f.write("\n")
f.write(str(txt1))
f.write("\n")
f.write(str(txt2))
f.write("\n")
f.write(str(txt3))
f.write("\n")
f.write("\n")
for i in pct:
    x = i * buy_price
    x = float(x)
    x = round(x,2)
    print(y,'% --',round(x,2))
    txt = str(y) + '% --' + str(x)
    f.write(str(txt))
    f.write("\n")
    y = y + 1
f.close()

# Program to calculate the spread between prices

# Get information from user
prompt = 'What is the current price?\n'
target_price = input(prompt)
target_price = float(target_price)

# calculate percentage difference of prices
if buy_price > target_price:
    result = (buy_price / target_price - 1) * 100
    result = float(result)
else:
    result = (target_price / buy_price - 1) * 100
    result = float(result)
print('Difference is ',round(result,2),' percent')

