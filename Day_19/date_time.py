import datetime

currentTime = datetime.datetime.now()

print(currentTime)

print("Current Year: "+str(currentTime.year))

print("Current Month: "+str(currentTime.month))

print(currentTime.strftime("%A %d %B %Y"))
