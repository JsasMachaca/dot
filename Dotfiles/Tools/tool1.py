import subprocess
from time import sleep
import optparse


def argumentos():
    print(f"Se cambiará la dirección MAC de la interfaz {interface} ")
    parser = optparse.OptionParser()
    parser.add_option("-m", "--macchange", dest="new", help="-m [param] ingresa como parametro una direccion mac")
    sleep(3)
    return parser.parse_args()

 
def procedure(interface, new):
    subprocess.call(["ifconfig", interface])
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig",interface, "hw", "ether", new])
    subprocess.call(["ifconfig", interface, "up"])
    sleep(4)
    print("\n Se ha cambiado con éxtio \n Mostrando cambios... \n \n")
    sleep(3)
    subprocess.call(["ifconfig", interface])


interface = "wlx2887ba3ad640"
a = argumentos()
sleep(3)
print("Iniciando... \n")
(options, arguments) = a
sleep(3)
procedure(interface, options.new)