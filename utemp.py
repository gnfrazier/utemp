#!/usr/bin/python3


import dht
import machine

d = dht.DHT22(machine.Pin(4))


def get_measurements():
    d.measure()
    tempc = d.temperature()
    hum = d.humidity()
    temp = convert(tempc)

    return (temp, hum)


def convert(temp):
    tempf = (temp * 9) / 5 + 32

    return tempf


def main():
    data = get_measurements()

    print('It is {} degrees at {} percent humidity.'.format(data[0], data[1]))

if __name__ == '__main__':
    main()
