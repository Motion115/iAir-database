def AQI_calculator(indicators: dict) -> int:
    # this does not entirely fit the time elapse requirement in Chinese standard HJ633-2012
    # https://www.mee.gov.cn/ywgz/fgbz/bz/bzwb/jcffbz/201203/t20120302_224166.shtml
    def IAQI_calculator(item: str, value: float) -> int:
        # if item is PM2.5
        if item == 'PM2.5':
            if value <= 35:
                result = (50 - 0) / (35 - 0) * (value - 0) + 0
            elif value <= 75:
                result = (100 - 50) / (75 - 35) * (value - 35) + 50
            elif value <= 115:
                result = (150 - 100) / (115 - 75) * (value - 75) + 100
            elif value <= 150:
                result = (200 - 150) / (150 - 115) * (value - 115) + 150
            elif value <= 250:
                result = (300 - 200) / (250 - 150) * (value - 150) + 200
            elif value <= 400:
                result = (400 - 300) / (350 - 250) * (value - 250) + 300
            else:
                result = (500 - 400) / (500 - 350) * (value - 350) + 400
            return int(result)
        # if item is PM10
        elif item == 'PM10':
            if value <= 50:
                result = (50 - 0) / (50 - 0) * (value - 0) + 0
            elif value <= 150:
                result = (100 - 50) / (150 - 50) * (value - 50) + 50
            elif value <= 250:
                result = (150 - 100) / (250 - 150) * (value - 150) + 100
            elif value <= 350:
                result = (200 - 150) / (350 - 250) * (value - 250) + 150
            elif value <= 420:
                result = (300 - 200) / (420 - 350) * (value - 350) + 200
            elif value <= 500:
                result = (400 - 300) / (500 - 420) * (value - 420) + 300
            else:
                result = (500 - 400) / (600 - 500) * (value - 500) + 400
            return int(result)
        # if item is SO2 (combining 24hr & 1hr std)
        elif item == 'SO2':
            if value <= 150:
                result = (50 - 0) / (150 - 0) * (value - 0) + 0
            elif value <= 500:
                result = (100 - 50) / (500 - 150) * (value - 150) + 50
            elif value <= 650:
                result = (150 - 100) / (650 - 500) * (value - 500) + 100
            elif value <= 800:
                result = (200 - 150) / (800 - 650) * (value - 650) + 150
            elif value <= 1600:
                result = (300 - 200) / (1600 - 800) * (value - 800) + 200
            else:
                result = (500 - 300) / (2100 - 1600) * (value - 1600) + 300
            return int(result)
        # if item is NO2 (1hr std)
        elif item == 'NO2':
            if value <= 100:
                result = (50 - 0) / (100 - 0) * (value - 0) + 0
            elif value <= 200:
                result = (100 - 50) / (200 - 100) * (value - 100) + 50
            elif value <= 700:
                result = (150 - 100) / (700 - 200) * (value - 200) + 100
            elif value <= 1200:
                result = (200 - 150) / (1200 - 700) * (value - 700) + 150
            elif value <= 2340:
                result = (300 - 200) / (2340 - 1200) * (value - 1200) + 200
            elif value <= 3090:
                result = (400 - 300) / (3090 - 2340) * (value - 2340) + 300
            else:
                result = (500 - 400) / (3840 - 3090) * (value - 3090) + 400
            return int(result)
        # if item is O3 (1hr std)
        elif item == 'O3':
            if value <= 160:
                result = (50 - 0) / (160 - 0) * (value - 0) + 0
            elif value <= 200:
                result = (100 - 50) / (200 - 160) * (value - 160) + 50
            elif value <= 300:
                result = (150 - 100) / (300 - 200) * (value - 200) + 100
            elif value <= 400:
                result = (200 - 150) / (400 - 300) * (value - 300) + 150
            elif value <= 800:
                result = (300 - 200) / (800 - 400) * (value - 400) + 200
            elif value <= 1000:
                result = (400 - 300) / (1000 - 800) * (value - 800) + 300
            else:
                result = (500 - 400) / (1200 - 1000) * (value - 1000) + 400
            return int(result)
        # if item is CO (1hr std)
        elif item == 'CO':
            if value <= 5:
                result = (50 - 0) / (5 - 0) * (value - 0) + 0
            elif value <= 10:
                result = (100 - 50) / (10 - 5) * (value - 5) + 50
            elif value <= 35:
                result = (150 - 100) / (35 - 10) * (value - 10) + 100
            elif value <= 60:
                result = (200 - 150) / (60 - 35) * (value - 35) + 150
            elif value <= 90:
                result = (300 - 200) / (90 - 60) * (value - 60) + 200
            elif value <= 120:
                result = (400 - 300) / (120 - 90) * (value - 90) + 300
            else:
                result = (500 - 400) / (150 - 120) * (value - 120) + 400
            return int(result)
        else:
            # since we only take maximum IAQI, thus if there exist a wrong input, it doesn't matter
            print("Error FROM utils.IAQI_calculator; wrong item name")
            return 0
    # calulate AQI
    AQI = 0
    for item in indicators:
        AQI = max(AQI, IAQI_calculator(item, indicators[item]))
    return AQI

'''
if __name__ == '__main__':
    # test
    indicators = {
        'PM2.5': 88,
        'PM10': 88,
        'SO2': 88,
        'NO2': 88,
        'O3': 88,
        'CO': 88
    }
    result = AQI_calculator(indicators)
    print(result)
'''
