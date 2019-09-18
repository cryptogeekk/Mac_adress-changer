import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, type --help for more options ")
    elif not options.mac:
        parser.error("[-] Please specify a mac , type --help for more options")
    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing mac address to a new mac " + interface + "  " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # print(ifconfig_result)

    macAdress_searchResult = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if macAdress_searchResult:
        print(macAdress_searchResult.group(0))
    else:
        print("[-] Could not read mac address...")

    return macAdress_searchResult.group(0)


(options, arguments) = get_arguments()
initial_mac=get_current_mac(options.interface)
print("The initial mac adresss of " + options.interface + " is " + initial_mac)
change_mac(options.interface, options.mac)
Current_mac = get_current_mac(options.interface)

# print("Current mac= " + str(Current_mac))
if Current_mac == options.mac:
    print("[+] The mac address was successfully changed to  " + Current_mac)
else:
    print("[-] Sorry the mac address donot changed")
