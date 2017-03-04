"""
 * The MIT License (MIT)
 *
 * Copyright (c) 2017 Chris Smolen
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
"""
import os
import json


def config():
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
    try:
        if os.stat('config.json')[0] > 0:       # Used instead of os.path.isfile() as it does not exist in MicroPython
            with open('config.json') as config:
                config = json.load(config)
            return config
    except OSError:
        with open('config.json', 'w') as createfile:
            createfile.write(json.dumps(CONFIG_DEFAULT))
            with open('config.json') as config:
                config = json.load(config)
        return config


def dash():
    DASH_DEFAULT = {
        "DASH_DEVICE_1": "XX:XX:XX:XX:XX:XX",
        "DASH_DEVICE_2": "XX:XX:XX:XX:XX:XX",
        "DASH_DEVICE_3": "XX:XX:XX:XX:XX:XX",
        "DASH_DEVICE_4": "XX:XX:XX:XX:XX:XX",
        "DASH_DEVICE_5": "XX:XX:XX:XX:XX:XX",
        "DASH_DEVICE_6": "XX:XX:XX:XX:XX:XX"
    }
    try:
        if os.stat('dash.json')[0] > 0:
            with open('dash.json') as config:
                config = json.load(config)
            return config
    except OSError:
        with open('dash.json', 'w') as createfile:
            createfile.write(json.dumps(DASH_DEFAULT))
            with open('dash.json') as dash:
                dash = json.load(dash)
        return dash
