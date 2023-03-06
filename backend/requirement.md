## Requirement for API

### Statistic Page

| API              | Which Table             | note                        | Return |
| ---------------- | ----------------------- | --------------------------- | ------ |
| getCityCount     | city                    |                             | int    |
| getClusterCount  | city                    |                             | int    |
| getDistrictCount | district                |                             | int    |
| getStationCount  | station                 |                             | int    |
| getTable         | ALL                     | param: table name           | list   |
| generateMap      | city, station, district | cascade visit through index | TBC    |
| filterAQI        |                         | 创建缓冲区保存数据          |        |