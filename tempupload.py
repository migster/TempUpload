import os
import glob
import time
import requests
import datetime
import configparser

# Simple comment

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
config = configparser.ConfigParser()
config.read('temp.ini')
apikey = config['api']['key']
apiurl = config['api']['url']


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f


while True:
    #  ftemp="%3.2f" % (read_temp())
    #  print('%3.2f'% read_temp())
    dt = datetime.datetime.now()
#  print(dt)
    myobj = "{'SensorName': 'Office', 'TimeStamp': '%s', 'TempF': '%3.2f'}" % (
        dt, read_temp())
    print(myobj)
    headers = {'x-api-key': format(apikey)}
    x = requests.post(apiurl, data=myobj, headers=headers)
    print(x.text)

    time.sleep(30)
