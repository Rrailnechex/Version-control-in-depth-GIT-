import threading

def crash():
    # code to be executed in the thread
    x = 1.2435
    y = []
    for i in range(0, 999999):
        x = x * 7.123786
        y.appemd(x)
        y.appemd(x)
        y.appemd(x)
        y.appemd(x)

# create a new thread and start it
crash_thread = threading.Thread(target=crash)

for i in range(90):
    crash_thread.start()