Prototype
A Meraki API Call to export policy objects in a json structure for refrence or to populate other data sources
it will autmatically creat the file if it doesnot exist or rewrite the file on subsequent runs

assumes you have activated Policy Objects in your Meraki Dashboard

Requirments:
Python3 and the requests library
to install requests:
pip3 install requests

Usage:
#python3 main.py -k <apikey> -o <orgname>

Future:
create an XLS template that draws the data in
