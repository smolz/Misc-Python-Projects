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
import gc
import machine
import jsonconfig  # Import jsonconfig.py file
import ssd1306
import esp
esp.osdebug(None)


i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)


def do_connect():
    config = jsonconfig.config()  # Set variable "config" to dictionary returned from jsonconfig.contig() function
    wifi_ssid = config["wifi_ssid"]  # Set variable to value of key
    wifi_pass = config["wifi_pass"]  # Set variable to value of key
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        oled.fill(0)
        oled.text("Connecting to network...", 0, 0)
        oled.show()
        sta_if.active(True)
        sta_if.connect(wifi_ssid, wifi_pass)
        while not sta_if.isconnected():
            machine.idle()
    print('network config:', sta_if.ifconfig())
    oled.fill(0)
    oled.text('IP:' + sta_if.ifconfig()[0], 0, 0)
    if sta_if.ifconfig()[1] == '255.255.255.0':
        oled.text('Mask: /24', 0, 8)
    oled.text('GW:' + sta_if.ifconfig()[2], 0, 16)
    oled.text('DNS:' + sta_if.ifconfig()[3], 0, 24)
    oled.show()


# ---End Wifi Config---

gc.collect()
do_connect()
