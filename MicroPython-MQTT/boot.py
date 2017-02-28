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


# ---End Wifi Config---

gc.collect()
do_connect()