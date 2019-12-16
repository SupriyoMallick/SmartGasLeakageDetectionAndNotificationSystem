from gpiozero import LED, Button
from time import sleep
from datetime import datetime as ds
import SendMail as sm
#Code build by Supriya Mallick - Email ID here.i.am.supriyo@gmail.com
button = Button(2)

while True:
    #to print current date time , use datetime module of python.
    # Gas Sensor used MQ Sensor. GPIO2 is connected with Gas Sensor's Analog output pin i.e. Pin 4.
    #button.when_pressed = print('Gas leaking !!!')
    print('Waiting for Gas detection.')
    button.wait_for_press()
    # to format the output in this way 23.Nov 2019 17:48:42, use below code.
    print(ds.now().strftime("%d.%b %Y %H:%M:%S"))
  # to format the output in iso fORMAT , USE below code.
    currts=str(ds.now().isoformat())
    print('Alert Gas Leaking !!!! @ '+currts)
    sm.sendEmail('Alert Gas Leaking !!!! @ '+currts,'This a alert notification, Some Gas Leakage has been detected in you house')
    #print(currts)
    sleep(1)
    
   
   