Prototype
A Meraki API Call to export policy objects in a json structure for refrence or to populate other data sources
it will autmatically create the output file if not present or rewrite the file on subsequent runs.

assumes you have activated Policy Objects in your Meraki Dashboard

Requirments:
Python 3 with the pathlib and requests libraries

to install the libraries:
pip3 install requests
pip3 install pathlib

Getting Started:
To obtain your orginizations name (we will get the ID for you since sometimes we have multiple orgs!) 
navigate to Orginization -> Settings -> Name

To obtain a valid API key follow the instructions at the following link:
https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API

To Activate Policy Objects in your Orginization:
https://documentation.meraki.com/MX/Firewall_and_Traffic_Shaping/Network_Objects_Configuration_Guide

Script Usage:
python3 main.py -k apikey -o orginization_name


  
  [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/johshea/export_Mpolicy_objects)
  
