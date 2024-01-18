#open file
file = open("WeatherDataCLL.csv", "r")
#min and max
lines = file.readlines()
#print(lines)
lines.pop(0)
minTemp = 1000
maxTemp = 0
for i in lines:
    line = i.split(",")
    if line[6] != "" and line[6] != "\n":
        minLine = int(line[6])
        if minLine < minTemp:
            minTemp = minLine
    if line[5] != "" and line[5] != "\n":
        maxLine = int(line[5])
        if maxLine > maxTemp:
            maxTemp = maxLine
print(f'10-year maximum temperature: {maxTemp} F')
print(f'10-year minimum temperature: {minTemp} F')
#average for month and year
monthDict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

monthIn = input("Please enter a month: ")
year = int(input("Please enter a year: "))

month = monthDict[monthIn]
dayCount = 0
avgTemp = 0
avgHum = 0
avgWind = 0
avgPrec = 0

for i in lines:
    line = i.split(',')
    date = line[0]
    dateSplit = date.split('/')
    if int(dateSplit[0]) == month and int(dateSplit[2]) == year:
        if line[4] != "":
            avgTemp += float(line[4])
        if line[3] != "":
            avgHum += float(line[3])
        if line[1] != "":
            avgWind += float(line[1])
        if line[2] != "":
            if float(line[2]) > 0:
                avgPrec += 1
        dayCount += 1
        
print(f'For {monthIn} {year}:')
print(f'Mean average daily temperature: {avgTemp/dayCount: .1f} F')
print(f'Mean relative humidity: {avgHum/dayCount: .1f}%')
print(f'Mean daily wind speed: {avgWind/dayCount: .2f} mph')
print(f'Percentage of days with precipitation: {(avgPrec/dayCount)*100:.1f}%')

