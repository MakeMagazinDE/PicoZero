# Anzeige der inneren (!) Temperatur des RP2040 Chips auf Website
# mit 'Ansicht->Drucken' (Plotter auch in Thonny)
import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

# Anpassen!
ssid     = 'SSID'
password = 'GEHEIM'

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Warte auf WLAN...')
        sleep(1)

    ip = wlan.ifconfig()[0]
    print(f'Server IP: {ip}')
    return ip

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def webpage(temperature, state):
    # HTML, alle 5s Refresh
    html = f"""
            <!DOCTYPE html>
            <meta http-equiv="refresh" content="5" >
            <html>
            <form action="./lighton">
            <input type="submit" value="LED an" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="LED aus" />
            </form>
            <p>LED is {state}</p>
            <p>Temperatur: {temperature:.1f} &deg;C</p>
            </body>
            </html>
            """
    return str(html)


def serve(connection):
    #Starte Webserver
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
            state = 'ON'
        elif request =='/lightoff?':
            pico_led.off()
            state = 'OFF'
        temperature = pico_temp_sensor.temp
        print(temperature)
        html = webpage(temperature, state)
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()


