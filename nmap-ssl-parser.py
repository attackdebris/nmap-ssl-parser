#!/usr/bin/env python
#
# nmap-ssl-parser version 0.2
#
# https://github.com/attackdebris/auto-sslscan
#
# Base code credit: https://github.com/DanMcInerney/nmap-parser/blob/master/nmap-parser.py 
#

import subprocess
import sys
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
 
instructions =  "nmap-ssl-parser - v0.2 ( https://github.com/attackdebris/nmap-ssl-parser )\n" +\
                "\nUSAGE: nmap-ssl-parser.py [nmap-ouput.xml] [outputfile]"

if len(sys.argv) <3 or sys.argv[1] == "-h" or sys.argv[1] == "--h" or sys.argv[1] == "-help" or sys.argv[1] == "--help":
        print instructions
        sys.exit()
elif len(sys.argv) >3:
	print instructions
	sys.exit()
elif len(sys.argv) ==3:
	nmapxml = sys.argv[1]
	myfile = sys.argv[2]
	f = open(myfile, 'w')
	f.close
	print 'nmap-ssl-parser - v0.2 ( https://github.com/attackdebris/nmap-ssl-parser )\n'

def report_parser(report):
    ''' Parse the Nmap XML report '''
    for host in report.hosts:
        ip = host.address

            # Get the port and service
            # objects in host.services are NmapService objects
	for s in host.services:
            # Check if port is open
		if s.open():
			serv = s.service
                	port = s.port
	        	tunnel = s.tunnel

                	# Perform some action on the data
                	print_data(ip, port, tunnel)

def print_data(ip, port, tunnel):
	''' Do something with the nmap data '''
	if tunnel != '':
		f = open(myfile, 'a+')
		print >> f, '{0}:{1}'.format(ip,port) 
		f.close

def end():
	print 'Results saved to: {}'.format(myfile)	

def main():
    report = NmapParser.parse_fromfile(nmapxml)
    report_parser(report)
    end()

main()
