import time

def getTime(dateSplit, timeSplit):
    # return time.strftime("%d" + dateSplit + "%m" + dateSplit + "%y %H" + timeSplit + "%M" + timeSplit + "%S")
    return time.strftime("%y" + dateSplit + "%m" + dateSplit + "%d %H" + timeSplit + "%M" + timeSplit + "%S")