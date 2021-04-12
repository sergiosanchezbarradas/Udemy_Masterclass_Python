# from common_vars import shapes
import datetime

date_now = datetime.datetime.now()
print("Sydney Time:{}.".format(str(date_now)))
mexico_time = date_now - datetime.timedelta(minutes=960)
quilla_time = date_now - datetime.timedelta(minutes=960)
LA_time = date_now - datetime.timedelta(minutes=1020)
NY_time = date_now - datetime.timedelta(minutes=840)

print("Mexico Time:{}.".format(mexico_time))
print("Barran Time:{}".format(quilla_time))
print("LA     Time:{}".format(LA_time))
print("NY     Time:{}".format(NY_time))
print()
import time


curr_time = time.localtime()
curr_clock = time.strftime("%H:%M:%S", curr_time)

print(curr_clock)
