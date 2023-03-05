## Data Preprocess

### Process

2 steps: preprocess.py, tableSplit.py, adjustDatetime.py

### Files

1. preprocess.py

   Drop Chinese name, drop duplicate values & check null values

2. tableSplit.py

   This is for meteorology.csv and weatherforecast.csv only. The original dataset did not distinguish district_id & city_id, an unacceptable format for database design. Therefore, it should be separated into 2 individual tables.
   
3. adjustDatetime.py

   Change the date time to the uniform style of a string of non-splitted numbers (i.e. 2023-03-05 20:20:20 to 20230305202020)

> data2dml.py is deprecated for the function can be performed in mySQL directly

### Data

1. **csv original** folder: the author's original data
2. **csv new** folder: the transformed data, with meteorology.csv and weatherforecast.csv not used in application.

Original data can be found AT: [data](https://www.microsoft.com/en-us/research/uploads/prod/2016/02/Data-1.zip)，if needed, you can run the above program yourself (its a bit big for github sync).

