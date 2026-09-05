import random
import time

def getRandomdate(startdate, enddate):
    print("random Date form : ",startdate, " and ", enddate)
    randomGenrator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startdate,dateFormat))
    endTime = time.mktime(time.strptime(enddate,dateFormat))

    randomtime = startTime + randomGenrator*(endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomDate

print("random date : ",getRandomdate("1/1/2026", "12/12/2026"))



