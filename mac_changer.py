import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="mac", help="new mac address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.mac

print("[+] Changing mac address to a new mac " + interface + "  " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
