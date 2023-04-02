#                            WORKING WITH DATA IN PYTHON

readdata = open("textfile.txt". "r") 
#r: open for reading
#w: open for writing, truncating the file first
#x: open for exclusive creating(fails if file exists)
#a: open for writing
#b: open in binary mode
#t: open in text mode
#+: open for updating

print(readdata.read())
readdata.close() #dont forget to close a file after you are done

with open("textfile.txt", "r") as data: #with doesn't require direct assignment to variable and automatically closes the file
    print(data.read())

with open("textfile.txt", "a+") as data:
    data.write('\nFourth line added by Python')


#                                   PARSING WITH DATA

#                    Comma-Seperated Values(CSV)
import csv
from os import fchdir, pipe
samplefile = open('routerlist.csv')
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)
sampledata
#[['router1', '192.168.10.1', 'Nashville'], 
# ['router2','192.168.20.1', 'Tampa'], 
# ['router3', '192.168.30.1', 'San Jose ']]

import csv
with open("routerlist.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        location = row[2]
        ip = row[1]
        print(f"{device} is in {location.rstript()} and has IP {ip}.")
#router1 is in Nashville and has IP 192.168.10.1
#router2 is in Tampa and has IP 192.168.20.1
#router1 is in San Jose and has IP 192.168.30.1

import csv
print("Please add a new router to the list")
hostname = input("What is the hostname? ")
ip = input("What is the ip addess? ")
location = input("What is the location? ")

router = [hostname, ip, location]

with open("routerlist.csv", "a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(router)
#Please add a new router to the list
#What is the hostname? router4
#What is the ip address? 192.168.40.1
#What is the location? London








#                         JSON (Javascript Object Notation)

#Data structure. Can be used for any proggramming language. Easily readable. Used in Web services
{
    "interface": {       #interface is main data object. its value is multiple key/value pairs
        "name": "GigabitEthernet1",
        "description": "Router Uplink",
        "enabled": true,
        "ipv4": {
            "address": [
                {
                    "ip": "192.168.1.1",
                    "netmask": "255.255.255.0"
                }
        }
    }
}

load() #allows you to import native JSOn and convert it to a Python dictionary from a file
loads() #will import JSON data from a string for parsing and manipulating within your program
dump() #is used to write JSON data from Python objects to a file
dumps() #allows you to take JSON dictionary data and convert it to serialized string for parsin and manipulating within Python

import json
with open("json_sample.json") as data:
    json_data = data.read()
json_dict = json.loads(json_data)   

type(json_dict)
#<class 'dict'>
print(json_dict)
{'interface': {'name': 'GigabitEthernet1', 'description':
'Router Uplink', 'enabled': True, 'ipv4': {'address':
[{'ip': '192.168.0.2', 'netmask': '255.255.255.0'}]}}}

json_dict["interface"]["description"] = "Backup Link"

print(json_dict)
{'interface': {'name': 'GigabitEthernet1', 'description':
'Backup link', 'enabled': True, 'ipv4': {'address':
[{'ip': '192.168.0.2', 'netmask': '255.255.255.0'}]}}}

with open("json_sample.json", "w") as fh: #saving the file
    json.dump(json_dict, fh, indent = 4) #indent makes it easier to read






#                      XML (Extensible Markup Language)

#Heavily used in configuration automation. Looks like HTML syntax. Used for data transport and storage between web services and APIs
<device> #tree structure. device is root element. parent-child relationship between elements
    <Hostname>Rtr01</Hostname> #hostname, ipv4 and ipv6 are child elements.
    <IPv4>192.168.1.5</IP4>
    <IPv6> </IPv6>
 </device>

 <?xml version="1.0" encoding="UTF-8" ?> #YANG Model represented in XML
<interface xmlns="ietf-interfaces">      #In XML order of key/value pairs matters
  <name>GigabitEthernet2</name>
  <description>Wide Area Network</description>
  <enabled>true</enabled>
  <ipv4>
    <address>
      <ip>192.168.1.5</ip>
      <netmask>255.255.255.0</netmask>
    </address>
  </ipv4>
</interface>



import xmltodict
with open("xml_sample.xml") as data:
    xml_example = data.read()
xlm_dict = xmltodict.parse(xml_example)

print(xml_dict)
OrderedDict([('interface', OrderedDict([('@xmlns', 'ietf-interfaces'), ('name',
'GigabitEthernet2'), ('description', 'Wide Area Network'), ('enabled', 'true'),
('ipv4', OrderedDict([('address', OrderedDict([('ip', '192.168.0.2'), ('netmask',
'255.255.255.0')]))]))]))])

xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3”

print(xmltodict.unparse(xml_dict, pretty=True)) #unparse to see changes. #pretty=true to make it easier to read
<?xml version="1.0" encoding="utf-8"?>
<interface xmlns="ietf-interfaces">
     <name>GigabitEthernet2</name>
     <description>Wide Area Network</description>
     <enabled>true</enabled>
     <ipv4>
        <address>
              <ip>192.168.55.3</ip>
              <netmask>255.255.255.0</netmask>
         </address>
     </ipv4>
</interface>

with open("xml_sample.xml", "w") as data: #to write these changes back to your original file
    data.write(xmltodict.unparse(xml_dict, pretty=True)) 



#                     YAML (YAML Ain't Markup Language)
#Extremely popular human-readable format for constructing configuration files and storing data
#It's built like JSON syntax but with host features(such as comments). Has minimal syntax

interface:
  name: GigabitEthernet2
  description: Wide Area Network
  enabled: true
  ipv4:
    address:
    - ip: 172.16.0.2
      netmask: 255.255.255.0


addresses:  #Can use '-' to identify elements
  - ip: 172.16.0.2
    netmask: 255.255.255.0
  - ip: 172.16.0.3
    netmask: 255.255.255.0
  - ip: 172.16.0.4
    netmask: 255.255.255.0

yaml.load #convert from YAML objects into python
yaml.dump #convert python objects back to YAML


import yaml
with open("yaml_sample.yaml") as data: #YAML lists automatically become Python lists
    yaml_sample = data.read()

yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader) 

yaml_dict
{'interface': {'name': 'GigabitEthernet2', 'description': 'Wide 
Area Network', 'enabled': True, 'ipv4': {'address': [{'ip':
'192.168.0.2', 'netmask': '255.255.255.0'}]}}}

yaml_dict["interface"]["name"] = "GigabitEthernet1"
yaml_dict
{'interface': {'name': 'GigabitEthernet1', 'description': 'Wide 
Area Network', 'enabled': True, 'ipv4': {'address': [{'ip':
'192.168.0.2', 'netmask': '255.255.255.0'}]}}}

with open("yaml_sample.yaml", "w") as data: #saving changes to the file
    data.write(yaml.dump(yaml_dict, default_flow_style=False))





#                          ERROR HANDLING IN PYTHON
#try-except-else-finally 

x = 0
While True:
    try:
        filename = input("Which file would you like to open? :")
        with open(filename, "r") as fh: #fh is an object
            file_data = fh.read()
    except FileNotFoundError:
        print(f'Sorry, {filename} doesn't exist! Please try again. ')
    else:
        print(file_data)
        x = 0
        break
    finally: #finally loop runs regardless of whether an exception occurs each time through the loop
        x += 1
        if x==3:
            print('Wrong filename 3 times.\nCheck name and Rerun.')
            break

#Which file would you like to open? :test
#Sorry, test doesn't exist! Please try again.
#Which file would you like to open? :test.txt
#Test file with some text.
#Two lines long.



#                     TEST-DRIVEN DEVELOPMENT (TDD) (in notability)

#The goal is to streamline the development process by focusing on only making changes or adding code that satisfies the goal of the test


#                                        UNIT TESTING

#Conducted on small, functional aspects of code. 
#Lowest level software testing. only a single function of the code is tested
#Unit: smallest testable part of your code
#Integration test: Tests how one software component works with the rest of the application.
#Functional test(end-to-end test): Broadest in scope from testing persective. Entire system is tested

from math import pi
def area_of_circle(r):
    return pi*(r**2)

import unittest
from areacircle import area_of_circle
from math import pi
class Test_Area_of_Circle_input(unittest.TestCase):
    def test_area(self):   
        # Test radius >= 0
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertALmostEqual(area_of_circle(3.5), pi * (3.5**2))

python -m unittest test_areacircle.py #to run the test
if __name__ == '__main__': #also can add this to test_areacircle.py
    unittest.main()     #__main__ special case is an attribute for all python scripts run from command line)
#Ran 1 test in 0.000s
#OK

def test_values(self):
    #Test that bad values are caught
    self.assertRaises(ValueError, area_of_circle, -1)
#“FAIL: test_values (__main__.Test_Area_of_Circle_input)

from math import pi
def area_of_circle(r):
    if r < 0:
       raise ValueError('Negative radius value error') #to give error for negative values
    return pi*(r**2)