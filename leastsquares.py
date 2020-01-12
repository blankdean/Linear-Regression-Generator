# Dean Blank CS171-A ID:db3226

import sys
import csv

# Intro to program
print('\nWelcome to the Linear Regression Generator')

# Ask for file name to extract data
print('Enter File Name Containing Data: ', end='')
f = input()


x = 0  # used to calculate sum of x column in loop
y = 0  # used to calculate sum of y column in loop
count = 0  # used to count how much rows
m_num = 0  # for calculating numerator in slope
m_den = 0  # for calculating denominator of slope
xarray = []  # xarray
yarray = []  # yarray
i = 0  # used to create an array
est = []  # array for estimate
err = []  # array for error
tempt = 0  # to calculate mse
errorsum = 0


# Open file
try:
    with open(f, 'r') as csvfile:
        myfile = csv.reader(csvfile)
        
        # skip headers in file
        next(myfile)
        
        # create loop to go through rows
        for row in myfile:
            count += 1  # count number of rows
            
            # make sure all values in rows are numbers, otherwise exit program
            try:
                row[0] = float(row[0])
                row[1] = float(row[1])
            except ValueError as e:
                print('  Error: A value in the file cannot be read')
                sys.exit(0)
                
            x = x + float(row[0])  # Sum of all x values
            y = y + float(row[1])  # sum of all y values
            xarray.append(float(row[0]))
            yarray.append(float(row[1]))
            i += 1  # increment i to save in different parts of array
            
    # myfile.close()
    csvfile.close()
    
    xavg = float(x/count)  # average of x values
    yavg = float(y/count)  # average of y values
            
    for i in range(len(xarray)):
        m_num += (xarray[i]-xavg)*(yarray[i]-yavg)  # calculate numerator sum
        
        m_den += (xarray[i]-xavg)**2.0  # calculate denominator sum
        
    m = m_num/m_den
    b = yavg - (m*xavg)
    

    for i in range(len(xarray)):
        est.append((m*xarray[i]) + b)   # for estimated value
    
    
    # getting sum of error
    for i in range(len(xarray)):
        err.append(abs(yarray[i]-est[i]))   # creating array for error
    
    for i in range(len(err)):
        errorsum = errorsum + float(err[i])     # need to sum error values in array
        
        # caculating MSE
    for i in range(len(xarray)):
        tempt += (yarray[i]-est[i])**2.0  # for mse
        
    erroravg = round(errorsum/len(err), 5)  # calculating average error
    mse = tempt/(len(xarray)-2)  # mse value
    s = round(mse**0.5, 5)   # regression value
            
except FileNotFoundError as e:
    print('  Error: File could not be opened.')   # catch file name error
    sys.exit(0)
    
mrounded = round(m, 5)  # rounding m to 5 decimals
brounded = round(b, 5)  # rounding b to 5 decimals
    
if brounded >= 0:   # change usage of '+' or '-' in output below depending if b or m is positive or negative
    plus_minus = '+'
else:
    plus_minus = ''

print('\n  The Linear Regression Line is y = ' + str(mrounded) + '*x' + str(plus_minus) + str(brounded) + '.')
print('  Average Error for Known Values was +/-' + str(erroravg) + '.')
print('  Regression Standard Error for Known Values was ' + str(s) + '.')
print('  System Ready to make predictions.')
print("  To quit, type 'exit' as the year.")


# opening file to extract program headers
try:
    with open(f, 'r') as csvfile:
        myfile = csv.reader(csvfile)
        data = []
        for row in csvfile:
            values = row.split(',')
            for value in values:
                data.append(value)
        xheader = data[0]  # value for x header
        yheader = data[1]  # value for y header
        yheader = (yheader)
except FileNotFoundError as e:
    print('  Error: File could not be opened.')   # catch file name error
    sys.exit(0)
    csvfile.close()

yheader = yheader.strip()   # strip new line in header after split so it can be printed

# Ask for year
year = input('  Enter ' + str(xheader) + ': ')

while True:
    try:
        year = int(year)       # condition that year must be integer
        prediction = round(m*year + b, 5)
        print('  Prediction when ' + str(xheader) + ' = ' + str(year) + ' is '
        + str(yheader) + ' = ' + str(prediction) + '.')  # print prediction
        print('  ________________________________')
    except:
            if year == 'exit':        # exit program if input is exit
                sys.exit(0)
            else:
                print('  Input could not be understood. Please try again.')
                
    year = input('  Enter ' + str(xheader) + ': ')    # ask for input again
