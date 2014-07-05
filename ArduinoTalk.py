import serial as ser
import time
import math
import weather
import datetime


def send(conn,flag,message):

    conn.write(flag.encode('ascii'))
    conn.write(message.encode('ascii'))

def get_cur_time():

    return str(math.floor(time.time()))

def get_temp():
    temp,weather = weather.weather_now()

    return temp

def get_weather():
    temp,weather = weather.weather_now()

    return weather
    


if __name__ == '__main__':
        

    TIMEFLAG = 't'
    TEMPFLAG = 'd'
    WEATHERFLAG = 'w'

    COM_PORT = 6 #Depends on what port the Arduino is plugged into
    BAUD = 2400 #Board is a bit picky about connecting sometimes.
                #Changing the BAUD seems to help

    conn = ser.Serial(port = COM_PORT,baudrate = BAUD)

    start = ''
    while not start:
        start = conn.readline()


    #send initial batch
    
    send(conn,TIMEFLAG,get_cur_time())
    send(conn,TEMPFLAG,get_temp())
    send(conn,WEATHERFLAG,get_weather())

    #note the time, to prevent overcalling weather.com
    _time = datetime.datetime.now()

    while 1:
        time.sleep(.5)
        #there has to be some waiting, to prevent overwhelming the
        #buffer in the attendant C code on the Arduino
        
        send(conn,TIMEFLAG,get_cur_time())
        if (datetime.datetime.now().minute - _time.minute) >= 3:
            #ok to query weather
            send(conn,TEMPFLAG,get_temp())
            send(conn,WEATHERFLAG,get_weather())
            
            

        

