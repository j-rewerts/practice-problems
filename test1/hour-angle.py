import datetime

def getAngle(clockTime):
	hourAngle = (360 / 12) * clockTime.hour
	minuteAngle = (360 / 60) * clockTime.minute
	return abs(hourAngle-minuteAngle)

print(getAngle(datetime.datetime.now()))