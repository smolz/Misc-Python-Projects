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
import time
import dht
import machine
from umqtt.simple import MQTTClient
import jsonconfig

config = jsonconfig.config()

d = dht.DHT22(machine.Pin(5))
topic1 = b"config['topic1']"
topic2 = b"config['topic2']"


def MQTTpub(topic, data=None):
    try:
        client = MQTTClient(client_id="config['mqtt_id']", server="config['mqtt_server']", user="config['mqtt_user']",
                        password="config['mqtt_pass']", port=1883)
        client.connect()
        client.publish(topic, data)
        sleep_ms(200)
        client.disconnect()
    except Exception as e:
        pass


def TempHum():
    try:
        d.measure()
        t = 9.0 / 5.0 * d.temperature() + 32
        h = d.humidity()
        return (t, h)
    except Exception as e:
        return (-1, -1)

while True:
    (t, h) = TempHum()
    MQTTpub(topic1, str(t))
    MQTTpub(topic2, str(h))
    time.sleep(5)
