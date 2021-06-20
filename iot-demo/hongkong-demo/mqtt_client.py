import sys
import time
import logging
import random
import threading
import queue
import json
from importlib import import_module
from demo_routes import points
import paho.mqtt.client as mqtt
import pdb

#MQTT_PORT = 8181
MQTT_PORT = 1883

# allow overriding the config file
print(len(sys.argv))
if len(sys.argv) > 1:
    configfile = import_module(sys.argv[1])
else:
    configfile = import_module("config")

config = configfile.Config()

NUM_ROUTES = 4
NUM_BIKES = 16
UPDATE_PERIOD = 10

########################################################################
# Logging
########################################################################
log = logging.getLogger()
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s:%(name)s: %(message)s')
ch.setFormatter(fmt)
log.addHandler(ch)
########################################################################

class Bike():
    def __init__(self, num):
        self.num = num
        self.mqtt = None
        self.step = 0
        self.step_dir = 1
        self.lat = 0
        self.lon = 0
        self.battery = 100
        self.charging = True
        self.lock = False
        self.infected = False

def http_message_handler(bike, body):
    print("Bike %d %sed" % (bike.num, value))
    bike.lock = (value == "True")

def do_update(bike):
    bikenum = bike.num
    step = bike.step
# teguh data is reversed, index 0 is lon and index 1 is lat
    pos = { "lat": points[bikenum % NUM_ROUTES][step][1],
            "lon": points[bikenum % NUM_ROUTES][step][0],
            "lck": bike.lock }
    posjson = json.dumps(pos)
    print("Bike No "+str(bikenum)+" "+str(posjson))

    bike.mqtt.publish("v1/devices/me/telemetry", posjson)

    if bike.step_dir > 0:
        step += 1
        if step == len(points[bikenum % NUM_ROUTES]):
            step -= 1
            bike.step_dir = -1
    else:
        step -= 1
        if step < 0:
            step = 0
            bike.step_dir = 1
    bike.step = step

bikenum = int(sys.argv[2])

def on_connect(client, userdata, flags, rc):
    log.info("Connected with result code "+str(rc))


def on_message():
    pass

if True:
    #import pdb;pdb.set_trace()
    log.info("Connecting to MQTT broker")
    bike = Bike(bikenum)
    bike.mqtt = mqtt.Client(client_id="bike%03d" % bikenum)
    bike.mqtt.on_connect = on_connect
    bike.mqtt.on_message = on_message
    bike.mqtt.loop_start()

    bike.mqtt.username_pw_set("bike%03d" % bikenum)
    bike.mqtt.connect("mqtt.recycle.com", MQTT_PORT, 60)
    time.sleep(1)

    bike.step = random.randint(0, len(points[bikenum % NUM_ROUTES]))
    step_dir = [-1,1][random.randrange(2)]

    # get current infected state
#    try:
#        bike.infected = (rsp["con"] == "True")
#    except:
#        bike.infected = False

    while True:
        do_update(bike)
        time.sleep(2)
