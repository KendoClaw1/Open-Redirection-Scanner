#!/usr/bin/python
#Twitter: https://twitter.com/KendoClaw1

import requests
import argparse
import os
import urllib
import socket
from urllib2 import urlopen, URLError, HTTPError
 
print """
########################
#                      #
#   Open Redirection   #
#       Scanner        #
#                      #
#   By: KendoClaw1     #
#                      #
########################
"""
print "To stop the script Press CTRL + C\n"


parser = argparse.ArgumentParser(description="Open Redirection Scanner")
parser.add_argument('-u',help="Url to test",metavar="URL")
parser.add_argument('-p',help="Parameter based scan (Uses a diffrent payload list),you must Specify a domain to be used in the payloads",metavar="domain.com")
parser.add_argument('-f',help="load URLs from a file (Optional)",metavar="FILEPATH")
parser.add_argument('-c',help="scan with a specific Cookie (Optional)",metavar="Cookie=value")
parser.add_argument('-v',help="Verbose mode", action='store_true')
args = parser.parse_args()


def main():
	global payloads
	if args.p:
		payloadfile = "payloadsparam.txt"
		with open(payloadfile,'r') as f:
			payloads = [m.strip() for m in f]
			payloads = [w.replace('WillBeReplaced.com',args.p) for w in payloads]
		
	else:
		payloadfile = "payloadsurl.txt"
		with open(payloadfile,'r') as k:
			payloads = [n.strip() for n in k]




	if args.f:
		domainlist = args.f
		scanlist(domainlist)
	elif args.u:
		urltoscan = args.u
		print "Scanning..."
		scanurl(urltoscan)
	else:
		print "Error: Please specify a domain or a file to scan"



def checkup(url):
	socket.setdefaulttimeout( 23 )  # timeout in seconds

	try :
	    response = urlopen( url )
	except HTTPError, e:
	    return "notvalid"
	except URLError, e:
	    return "notvalid"
	else :
	    html = response.read()
	    return "up"



def scanurl(url):
	if args.c:
		headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101","Cookie": args.c}
	else:
		headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101"}



	for payload in payloads:
		target = url+payload
		req = requests.get(target,headers=headers,allow_redirects=False)

		if args.v:
			print target+"  --"+str(req.status_code)

		if "Location" in req.headers and  urllib.unquote(payload).decode('utf8') in req.headers["Location"]:
			print "\nMay Be VULNERABLE: "+url + payload
			print "\nLanding Page: "+str(requests.get(target,headers=headers).url)


def scanlist(domains):
	if args.c:
		headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101","Cookie": args.c}
	else:
		headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101"}


	with open(domains,'r') as l:
		urls = [m.strip() for m in l]


	protocol = raw_input("Choose a protocol to be set in case a url in the file didn't have a specific protocol: \n1- HTTP\n2- HTTPS\n> ")
	if protocol == "1":
		protocol = "http://"
	elif protocol == "2":
		protocol = "https://"
	else:
		print "Unknown choice"
		exit()

	print "Scanning..."
	for url in urls:
		if url.startswith("http://") or url.startswith("https://"):
			bfr = url
		else:
			bfr = protocol+url

		if checkup(bfr) == "up":
			scanurl(bfr)
		else:
			print "Host: "+bfr+" is down."



try:
	main()
except KeyboardInterrupt:
	print "\nDone"
