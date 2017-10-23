#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import configparser
import pifacedigitalio as PFIO
  
APPNAME = os.path.splitext(os.path.basename(__file__))[0]
INIFILE = os.getenv('INIFILE', APPNAME + '.ini')

config = configparser.ConfigParser()
config.read(INIFILE)

MODULE = 'PFIO'

MQTT_HOST = config.get("global", "mqtt_host")
MQTT_PORT = config.getint("global", "mqtt_port")
MQTT_USERNAME = config.get("global", "mqtt_username")
MQTT_PASSWORD = config.get("global", "mqtt_password")
MQTT_CERT_PATH = config.get("global", "mqtt_cert_path")
MQTT_TLS_INSECURE = config.get("global", "mqtt_tls_insecure")
MQTT_TLS_PROTOCOL = config.get("global", "mqtt_tls_protocol")
MQTT_CLIENT_ID = config.get("global", "mqtt_client_id")
MQTT_TOPIC = config.get("global", "mqtt_topic")
MQTT_QOS = config.getint("global", "mqtt_qos")
MQTT_RETAIN = config.getboolean("global", "mqtt_retain")
MQTT_CLEAN_SESSION = config.getboolean("global", "mqtt_clean_session")
MQTT_LWT = config.get("global", "mqtt_lwt")

MONITOR_PINS = config.get("global", "monitor_pins", raw=True)
MONITOR_POLL = config.getfloat("global", "monitor_poll")

PINS = []
if MONITOR_PINS:
    PINS.extend(list(map(int, MONITOR_PINS.split(","))))

for PIN in PINS:
    PINS[PINS.index(PIN)] = [PIN, -1]
    
    
