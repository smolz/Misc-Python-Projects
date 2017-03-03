import machine
import bme280
import ssd1306
import time

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)


def get_data():
    t, p, h = bme.values
    return (t, p, h)


def main():
    while True:
        get_data()
        Display_OLED(t, p, h)
        time.sleep(5)


def Display_OLED(t, p, h):
    oled.fill(0)
    oled.show()
    oled.text(t, 0, 0)
    oled.text(p, 0, 10)
    oled.text(h, 0, 20)
    oled.show()
