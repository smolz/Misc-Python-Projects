"""
MIT License

Copyright (c) 2017 Chris Smolen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import logging  # for the following line

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # suppress IPV6 warning on startup

from scapy.all import *  # for sniffing for the ARP packets
import time
import paho.mqtt.client as mqtt
import jsonconfig

last_time = {}
buttons = jsonconfig.dash()


def arp_display(pkt):
    if not pkt.haslayer(Ether):
        return
    # print(pkt[Ether].src, pkt.summary())

    # ignore additional packets received within min_interval seconds
    mac = pkt[Ether].src
    min_interval = 5  # seconds
    global lasttime
    if not (mac in last_time):
        interval = min_interval + 1  # we haven't see this; generate a fire
    else:
        interval = time.time() - last_time[mac]

    if interval >= min_interval:
        last_time[mac] = time.time()
        if mac == buttons['greenies']:
            mqttc.publish('dash/greenies', "ON")
        elif mac == buttons['puffs']:
            mqttc.publish('dash/puffs', "ON")
        elif mac == buttons['smart']:
            mqttc.publish('dash/smart', "ON")
        elif mac == buttons['nerf']:
            mqttc.publish('dash/nerf', "ON")
        elif mac == buttons['glad']:
            mqttc.publish('dash/glad', "ON")
        elif mac == buttons['bounty']:
            mqttc.publish('dash/bounty', "ON")
        else:
            pass


if __name__ == '__main__':
    config = jsonconfig.config()
    mqtt_user = config["mqtt_user"]
    mqtt_pass = config["mqtt_pass"]
    mqtt_host = config["mqtt_server"]
    mqttc = mqtt.Client()
    print('Init done.')
    mqttc.username_pw_set(mqtt_user, password=mqtt_pass)
    mqttc.connect(mqtt_host)
    mqttc.loop_start()
    f = " or ".join(["ether host " + buttons[button] for button in buttons])
    # print(f)
    print(sniff(iface="wlan0", prn=arp_display, filter=f, store=0))
