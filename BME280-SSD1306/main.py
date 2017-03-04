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

import machine
import bme280
import ssd1306
import time
from umqtt.simple import MQTTClient
import jsonconfig


config = jsonconfig.config()

mqtt_id = config['mqtt_id']
mqtt_user = config['mqtt_user']
mqtt_pass = config['mqtt_pass']
mqtt_server = config['mqtt_server']

topic1 = config['topic1']
topic2 = config['topic2']
topic3 = config['topic3']
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)


def tem_hum_press():
    try:
        t, p, h = bme.values
        return t, p, h
    except Exception as e:
        return -1, -1, -1


def mqtt_pub(topic, data=None):
    try:
        client = MQTTClient(client_id=mqtt_id, server=mqtt_server, user=mqtt_user, password=mqtt_pass)
        client.connect()
        client.publish(topic, data)
        time.sleep_ms(200)
        client.disconnect()
    except Exception as e:
        print("Exception: " + e)
        pass


def main():
    while True:
            t, p, h = tem_hum_press()
            oled.fill(0)
            oled.text("Temp: " + t + " F", 0, 0)
            oled.text("P: " + p + " hPa", 0, 10)
            oled.text("Hum: " + h + " %", 0, 20)
            oled.show()
            mqtt_pub(topic1, str(t))
            mqtt_pub(topic2, str(h))
            mqtt_pub(topic3, str(p))
            time.sleep(60)
            oled.fill(0)
            oled.show()
            time.sleep(540)
main()
