## Data Preprocess

### Process

2 steps: preprocess.py, then tableSplit.py

### Files

1. preprocess.py

   Drop Chinese name, drop duplicate values & check null values

2. tableSplit.py

   This is for meteorology.csv and weatherforecast.csv only. The original dataset did not distinguish district_id & city_id, an unacceptable format for database design. Therefore, it should be separated into 2 individual tables.

> data2dml.py is deprecated for the function can be performed in mySQL directly

### Data

1. **csv original** folder: the author's original data
2. **csv new** folder: the transformed data, with meteorology.csv and weatherforecast.csv not used in application.

Original data can be found AT: [data](https://www.microsoft.com/en-us/research/uploads/prod/2016/02/Data-1.zip)，if needed, you can run the above program yourself (its a bit big for github sync).

