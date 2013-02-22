import math

powerDigit = 0
powerString = ""
powerTotal = 0

powerDigit = pow(2, 1000)

powerString =  str(powerDigit)

for x in powerString:
    powerTotal = powerTotal + int(x)
 
print powerTotal