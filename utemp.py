#!/usr/bin/python3


import dht
import machine

dht = dht.DH22(machine.Pin(4))


def get_measurments():
    dht.measure()
    tempc = dht.temperature()
    hum = dht.humidity()
    temp = convert(tempc)

    return (temp, humidity)


def convert(temp):
    tempf = (temp * 9) / 5 + 32

    return tempf

main():
    data = get_measurments()

    print('It is {} degrees at {} percent humidity.'.format(data[0], data[1])

if __name__ == '__main__':
    main()
