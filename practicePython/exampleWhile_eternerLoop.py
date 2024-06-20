from datetime import datetime
currentTime = datetime.now().strftime('%c')

while True:
    print(currentTime)