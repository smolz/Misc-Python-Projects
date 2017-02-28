# Second way to not have passwords, etc. in a script
## For MicroPython
For MicroPython when you run the `jsonconfig.config()` function it will check to see if the file 'config.json' exists in the file system and if not it will create a template file called 'config.json' that can be modified, or you can just modify and save the below as 'config.json':
```
{
"wifi_ssid": "YOURSSID",
"wifi_pass": "YOUR_PASSWORD",
"topic1": "YOUR_MQTTT_TOPIC",
"topic2": "YOUR_MQTT_TOPIC",
"mqtt_id": "NAME_FOR_DEVICE",
"mqtt_server": "MQTT_SERVER_IP_OR_HOST",
"mqtt_user": "MQTT_USERNAME",
"mqtt_pass": "MQTT_PASSWORD"
}
```
- Here is a template for boot.py that calls `jsonconfig.config()` and returns a dictionary.

```
    import gc
    import machine
    import jsonconfig   # Import jsonconfig.py file


    def do_connect():
        config = jsonconfig.config()        # Set variable "config" to dictionary returned from jsonconfig.contig() function
        wifi_ssid = config["wifi_ssid"]     # Set variable to value of key
        wifi_pass = config["wifi_pass"]     # Set variable to value of key
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(wifi_ssid, wifi_pass)
            while not sta_if.isconnected():
                machine.idle()
        print('network config:', sta_if.ifconfig())

    gc.collect()
    do_connect()```

- Create file 'jsonconfig.py'

```
import os
import json

CONFIG_DEFAULT = {
    "wifi_ssid": "YOURSSID",
    "wifi_pass": "YOUR_PASSWORD",
    "topic1": "YOUR_MQTTT_TOPIC",
    "topic2": "YOUR_MQTT_TOPIC",
    "mqtt_id": "NAME_FOR_DEVICE",
    "mqtt_server": "MQTT_SERVER_IP_OR_HOST",
    "mqtt_user": "MQTT_USERNAME",
    "mqtt_pass": "MQTT_PASSWORD"
}


def config():
    try:
        if os.stat('config.json')[0] > 0:
            with open('config.json') as config:
                config = json.load(config)
            return config
    except OSError:
        with open('config.json', 'w') as createfile:
            createfile.write(json.dumps(CONFIG_DEFAULT))
            with open('config.json') as config:
                config = json.load(config)
        return config
```

## For regular Python
For Python when you run the `jsonconfig.config()` function it will check to see if the file 'config.json' exists in the file system and if not it will create a template file called 'config.json' that can be modified, or you can just modify and save the below as 'config.json':

```
{
"wifi_ssid": "YOURSSID",
"wifi_pass": "YOUR_PASSWORD",
"topic1": "YOUR_MQTTT_TOPIC",
"topic2": "YOUR_MQTT_TOPIC",
"mqtt_id": "NAME_FOR_DEVICE",
"mqtt_server": "MQTT_SERVER_IP_OR_HOST",
"mqtt_user": "MQTT_USERNAME",
"mqtt_pass": "MQTT_PASSWORD"
}
```
The only difference between Python and MicroPython implementations is the use of the `os.path.isfile()` function to check whether the file exists or not as this function is not available in MicroPython.

- jsonconfig.py file:

```
import os.path
import json

CONFIG_DEFAULT = {
    "wifi_ssid": "YOURSSID",
    "wifi_pass": "YOUR_PASSWORD",
    "topic1": "YOUR_MQTTT_TOPIC",
    "topic2": "YOUR_MQTT_TOPIC",
    "mqtt_id": "NAME_FOR_DEVICE",
    "mqtt_server": "MQTT_SERVER_IP_OR_HOST",
    "mqtt_user": "MQTT_USERNAME",
    "mqtt_pass": "MQTT_PASSWORD"
}

DASH_DEFAULT = {
    "DASH_DEVICE_1": "XX:XX:XX:XX:XX:XX",
    "DASH_DEVICE_2": "XX:XX:XX:XX:XX:XX",
    "DASH_DEVICE_3": "XX:XX:XX:XX:XX:XX",
    "DASH_DEVICE_4": "XX:XX:XX:XX:XX:XX",
    "DASH_DEVICE_5": "XX:XX:XX:XX:XX:XX",
    "DASH_DEVICE_6": "XX:XX:XX:XX:XX:XX"
}


def config():
    if not os.path.isfile('config.json'):                   # Used to check if the file exists or not
        with open('config.json', 'w') as createfile:
            createfile.write(json.dumps(CONFIG_DEFAULT))
            with open('config.json') as config:
                config = json.load(config)
            return config
    else:
        with open('config.json') as config:
            config = json.load(config)
        return config


def dash():
    if not os.path.isfile('dash.json'):
        with open('dash.json', 'w') as createfile:
            createfile.write(json.dumps(DASH_DEFAULT))
            with open('dash.json') as dash:
                dash = json.load(dash)
            return dash
    else:
        with open('config.json') as dash:
            dash = json.load(dash)
        return dash
```
