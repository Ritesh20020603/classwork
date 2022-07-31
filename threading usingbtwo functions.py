from threading import *
import time
def f1(n):
    for x in range(n):
        time.sleep
        print(current_thread().name,x)
t1=Thread(target=f1,args=[5],name='thread1')
t1.start()
def f2(n):
    for x in range(6,11):
        print(current_thread().name,x)
t1=Thread(target=f2,name='thread2')
t1.start()