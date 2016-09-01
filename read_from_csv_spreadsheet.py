import csv

with open('read_from_csv_spreadsheet_example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)

    dates = []
    colors = []


    for row in readCSV:
#      print(row)
#      print(row[0])
#      print(row[0],row[1])
###
        color = row[3]
        date = row[0]
        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

## error handling
    try:
        whatColor = input('What color do you whish to know the date of?')

        if whatColor in colors:
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print('The date of',whatColor,'is the date:', theDate)
        else:
            print('Color not found, or is not a color')

    except Exception as e:
        print(e)

    print('continuing')



