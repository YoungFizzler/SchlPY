import time

score = 81
curr_time = time.strftime("%H:%M:%S", time.localtime())
if score > 80:
    print("Timestamp: " + curr_time + " with status code: " + "PASS")
