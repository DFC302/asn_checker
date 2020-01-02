#!/usr/bin/env python3

import requests
import socket
import sys
import argparse
import subprocess

def options():
	parser = argparse.ArgumentParser()
	# Allow user to search via IP
	parser.add_argument(
		"--ip",
		help="Check ASN number from IP.",
		action="store",
	)
	# Allow user to search via URL
	parser.add_argument(
		"--url",
		help="Check ASN number from URL.",
		action="store",
	)
	# Normal options just display ASN
	# However, user can add --details option to print more information regarding the IP/URL
	parser.add_argument(
		"--details",
		help="Display detailed information for ASN.",
		action="store_true",
	)
	# if no arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	return args

def parse_ip():
	try:
		if options().url:
			url = options().url.strip("http://").strip("https://")
			ip = socket.gethostbyname(url)
			return ip
	
		elif options().ip:
			ip = options().ip
			return ip

	except socket.gaierror:
		print("\nERROR: Host not recognized!\n")
		sys.exit(1)

def grab_asn():
	try:
		ip = parse_ip()
		api_url = f"https://api.iptoasn.com/v1/as/ip/{ip}"
		response = requests.get(api_url)
		data = response.json()

		# data filters
		announced = data["announced"]
		country_code = data["as_country_code"]
		description = data["as_description"]
		ASN = data["as_number"]
		first_IP = data["first_ip"]
		IP = data["ip"]
		last_IP = data["last_ip"]

		# command to grab cidr's
		cmd = f"whois -h whois.radb.net -- '-i origin AS{ASN}' | grep -Eo '([0-9.]+){{4}}/[0-9]+' | sort -u"

		if not options().details:
			print(f"ASN:\t{ASN}")

		elif options().details:
			print("\n")
			print(f"Announced:   \t{announced}") #9
			print(f"Country Code:\t{country_code}") #13
			print(f"Description: \t{description}") #12
			print(f"ASN:         \t{ASN}") #4
			print(f"Starting IP: \t{first_IP}") #12
			print(f"Ending IP:   \t{last_IP}") #10
			print(f"IP Searched: \t{IP}") #12

			print(f"\nIP's associated with ASN: {ASN}\n")
			print(subprocess.check_output(cmd, shell=True).decode())

	except ValueError:
		print("ERROR! ASN could not be parsed!")
		print("Make sure you did not accidentially put URL for IP or vice versa.")
		sys.exit(1)

def main():
	grab_asn()

if __name__ == "__main__":
	main()

		
