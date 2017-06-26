import xml.etree.ElementTree as ET
import os
import urllib2
import time
import sys
import time

url = 'http://web.mta.info/status/serviceStatus.txt'

def get_status(xml_file, line_requested):
	root = ET.parse(xml_file).getroot()
	p_lines = []
	p_status = []

	for lines in root.findall('.//line'):
		p_lines.append(lines.find('name').text)
		p_status.append(lines.find('status').text)

	print p_lines[p_lines.index(line_requested)]
	print p_status[p_lines.index(line_requested)]
	print time.strftime("%m-%d-%y %H:%M:%S")

	return;

def main(url):
	try:
		while True:
			xml_loc = urllib2.urlopen(url)
			get_status(xml_loc,'ACE')
			time.sleep(5)
	except KeyboardInterrupt:
		print "You stopped it."
		sys.exit(0)

if __name__ == "__main__":
	main(url)