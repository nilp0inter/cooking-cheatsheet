from dataclasses import dataclass
import csv
import json


#
# Some dataclasses to reference the keys in the JSON file
#
@dataclass
class KeyNames:
    fruit_optimal_season: str = "Frutas en temporada óptima"
    fruit_entering_or_leaving_season: str = "Frutas entrando/saliendo de temporada"
    vegetable_optimal_season: str = "Verduras en temporada óptima"
    vegetable_entering_or_leaving_season: str = "Verduras entrando/saliendo de temporada"


@dataclass
class MonthNames:
    january: str = "Enero"
    february: str = "Febrero"
    march: str = "Marzo"
    april: str = "Abril"
    may: str = "Mayo"
    june: str = "Junio"
    july: str = "Julio"
    august: str = "Agosto"
    september: str = "Septiembre"
    october: str = "Octubre"
    november: str = "Noviembre"
    december: str = "Diciembre"


#
# The data to be written to the calendar
#
@dataclass
class SeasonalData:
    optimal_season: str = "+"
    entering_or_leaving_season: str = "-"
    out_of_season: str = " "

#
# Some constants to help with the data processing
#
months = [MonthNames.january, MonthNames.february, MonthNames.march, MonthNames.april, MonthNames.may, MonthNames.june,
          MonthNames.july, MonthNames.august, MonthNames.september, MonthNames.october, MonthNames.november,
          MonthNames.december]
fruit_keys = [KeyNames.fruit_optimal_season, KeyNames.fruit_entering_or_leaving_season]
vegetable_keys = [KeyNames.vegetable_optimal_season, KeyNames.vegetable_entering_or_leaving_season]

data = json.load(open('./spain-seasonal.json', 'r'))

#
# Create the list of vegetables and fruits
#
vegetables = set()
fruits = set()
for month in months:
    for key in vegetable_keys:
        vegetables |= set(data[month][key])
    for key in fruit_keys:
        fruits |= set(data[month][key])
vegetables = list(sorted(vegetables))
fruits = list(sorted(fruits))

#
# Create the vegetable and fruit calendars
#
vegetables_calendar = dict()
for month in months:
    vegetables_calendar[month] = dict()
    for vegetable in vegetables:
        if vegetable in data[month][KeyNames.vegetable_optimal_season]:
            vegetables_calendar[month][vegetable] = SeasonalData.optimal_season
        elif vegetable in data[month][KeyNames.vegetable_entering_or_leaving_season]:
            vegetables_calendar[month][vegetable] = SeasonalData.entering_or_leaving_season
        else:
            vegetables_calendar[month][vegetable] = SeasonalData.out_of_season

fruit_calendar = dict()
for month in months:
    fruit_calendar[month] = dict()
    for fruit in fruits:
        if fruit in data[month][KeyNames.fruit_optimal_season]:
            fruit_calendar[month][fruit] = SeasonalData.optimal_season
        elif fruit in data[month][KeyNames.fruit_entering_or_leaving_season]:
            fruit_calendar[month][fruit] = SeasonalData.entering_or_leaving_season
        else:
            fruit_calendar[month][fruit] = SeasonalData.out_of_season

#
# Write the calendars to CSV files
#
csv_file = open('vegetables.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow([''] + months)
for vegetable in vegetables:
    csv_writer.writerow([vegetable] + [vegetables_calendar[month][vegetable] for month in months])
csv_file.close()


csv_file = open('fruits.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow([''] + months)
for fruit in fruits:
    csv_writer.writerow([fruit] + [fruit_calendar[month][fruit] for month in months])
csv_file.close()
