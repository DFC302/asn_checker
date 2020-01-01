# ASN Checker

# Description:
Check the autonomous system number (ASN) of an IP/URL.

# Installation
git clone https://github.com/DFC302/asn_checker.git \
cd asn_checker \
sudo pip3 install -r requirements.txt \
sudo chmod 755 asn_checker.py

**Create an alias** \
alias [alias name]='python3 [path to asn_checker.py]' \
**EXAMPLE: alias asn_checker='python3 ~/tools/asn_checker/asn_checker.py'

# Usage
```
usage: asn_checker.py [-h] [--ip IP] [--url URL] [--details]

optional arguments:
  -h, --help  show this help message and exit
  --ip IP     Check ASN number from IP.
  --url URL   Check ASN number from URL.
  --details   Display detailed information for ASN.
```
**Use standard output redirection to write results to a file**\
**EXAMPLE: asn_checker.py --url example.com --details >> asn_details_example_com.txt**

# Author
Matthew Greer

# Version
Version: 0.1.0
