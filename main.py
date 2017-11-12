#! /usr/bin/python
import mraa
import time

from spark_bot import *

print (mraa.getVersion())
x = mraa.Gpio(29)
x.dir(mraa.DIR_OUT)
#but = 5
L = spark_init()

while True:
    #but = x.read()
    #print(but)
    x.write(1)
    time.sleep(0.2)
    x.write(0)
    time.sleep(0.2)
    spark_send(L[0], L[1], "Emergency situation, please go check the patient")
