# threading class is imported for implementing multi threading, class needs to inherhit class thread in order
#to implement threading
#time module is imported for using sleep function
# there is always a main thread on which the execution is happening, but with Thread, now 2 more threads
# are spawned, hence there are total of 3 threads now

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
sleep(.3)  # to cause delay
t2 = Hi()

t1.start()   #start will spawn a new thread, but for this run function should be implemented
t2.start()
t1.join()   # wait for the thread t1 and t2 join the main thread
t2.join()
print("Bye") #print is being executed by the main thread, hence when join statements are removed, Bye is
#printed before hello hi finishes printing