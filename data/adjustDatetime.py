import pandas as pd

def timeTransform(x):
    content = x
    # split content with " "
    content = content.split(" ")
    # for content[0], split with "-"; for content[1], split with ":"
    content[0] = content[0].split("-")
    content[1] = content[1].split(":")
    # concatenate the content
    content = content[0] + content[1]
    # join content with noting
    content = "".join(content)
    return content


def changeDatetime(src, fileName, timeColumnName):
    # read csv file with all columns viewed as string
    data = pd.read_csv(src + fileName, dtype = str)
    # change column timeColumnName to a sql time format
    data[timeColumnName] = data[timeColumnName].apply(lambda x: timeTransform(x))
    # write to csv
    data.to_csv(src + "n_" + fileName, index = False)

if __name__ == '__main__':
    src = "./data/csv new/"
    changeDatetime(src, "meteorology_c.csv", "time")
    changeDatetime(src, "meteorology_d.csv.", "time")
    #changeDatetime(src, "airquality.csv", "time")
    timeList = ["time_forecast", "time_future"]
    for timeType in timeList:
        changeDatetime(src, "weatherforecast_d.csv", timeType)
        changeDatetime(src, "weatherforecast_c.csv", timeType)