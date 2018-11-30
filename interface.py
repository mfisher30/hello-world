import re
interface = "Hardware is CSR vNIC, address is 0050.5602.59d7 (bia 0050.5602.59d7)"
mac = re.search('0050.56', interface)
print "There is a device with OUI:"
print (mac.group(0))