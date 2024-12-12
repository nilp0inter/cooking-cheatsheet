This directory contains a calendar of seasonal fruits and vegetables in Spain.

The data source is [a PDF from green peace](https://es.greenpeace.org/es/frutas-verduras-temporada/calendario/),
after [some massaging with ChatGPT](https://chatgpt.com/share/675b6454-1d50-800d-add4-47e60b586ebc) I obtained `seasonal.json` which contains the same data in JSON format.
Using the `as_csv.py` script in this very folder I created `fruits.csv` and `vegetables.csv` that then was imported into this [calendar in spreadsheet format](https://docs.google.com/spreadsheets/d/16v9Sa2WIs6JM4Oy_43-3Bo9MzwyI33rsjHAaprFrRG4/edit?usp=sharing).

The result is render in `calendar.pdf`
