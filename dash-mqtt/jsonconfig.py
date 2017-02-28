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
