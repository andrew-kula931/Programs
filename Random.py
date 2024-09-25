import random

hours = random.randint(0,23)
minutes = random.randint(0,59)

if (minutes < 10):
    minutes = '0' + str(minutes)
    
print(str(hours) + ':' + str(minutes))