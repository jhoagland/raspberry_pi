import xml.etree.ElementTree as ET
import os
import urllib2
import time




xml_file = urllib2.urlopen('http://web.mta.info/status/serviceStatus.txt')
root = ET.parse(xml_file).getroot()

p_lines = []
p_status = []
for lines in root.findall('.//line'):
	p_lines.append(lines.find('name').text)
	p_status.append(lines.find('status').text)

print p_lines[p_lines.index('ACE')]
print p_status[p_lines.index('ACE')]
