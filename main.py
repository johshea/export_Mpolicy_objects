##################################################################################################
#Prototype
#A Meraki API Call to export policy objects in a json structure for refrence or to populate other data sources
#it will autmatically creat the file if it doesnot exist or rewrite the file on subsequent runs
#
#assumes you have activated Policy Objects in your Meraki Dashboard
#
#Requirments:
#Python3 and the requests library
#to install requests:
#pip3 install requests
#
#Usage:
#python3 main.py -k <apikey> -o <orgname>
#
#Future:
#create an XLS template that draws the data in
###################################################################################################



import requests
import json, sys, getopt


def getorgId(arg_orgname):
    org_response = requests.request("GET", f'{m_baseUrl}/organizations/', headers=m_headers)
    org = org_response.json()
    for row in org:
        if row['name'] == arg_orgname:
            orgid = row['id']
            print("Org" + " " + row['name'] + " " + "found.")
        else:
            print("Exception: This Org does not match:" + ' ' + row['name'] + ' ' + 'Is not the orginization specified!')

    return orgid




def getpolobjects(orgid):
    results = []
    try:
       r = requests.request("GET", f'{m_baseUrl}/organizations/{orgid}/policyObjects', headers=m_headers)
       if r.status_code == 200:
           raw = r.json()
           for i in raw:
               results.append(i)

       while 'next' in r.links:
           r = requests.get(r.links['next']['url'],
                            headers=m_headers)
           # print(r.links)
           raw = r.json()
           for i in raw:
               results.append(i)

       return(results)

    # print (len(results))
    except:
        print('ERROR 02: Unable to contact Meraki cloud')
        print('API response: {}'.format(r.status_code))



#def getpolobj()


def main(argv):
    global arg_apikey
    global m_baseUrl
    global m_headers
    global arg_orgname

    arg_apikey = None
    arg_orgname = None

    try:
        opts, args = getopt.getopt(argv, 'k:o:')
    except getopt.GetoptError:
        sys.exit(0)

    for opt, arg in opts:
        if opt == '-k':
            arg_apikey = arg
        elif opt == '-o':
            arg_orgname = arg

    if arg_apikey is None or arg_orgname is None:
        print('Please specify the required values!')
        sys.exit(0)

    # set needed vlaues from env_vars
    m_headers = {'X-Cisco-Meraki-API-Key': arg_apikey}
    m_baseUrl = 'https://api.meraki.com/api/v1'

    orgid = getorgId(arg_orgname)

    polobjects = getpolobjects(orgid)

    #polobjects_json = json.dumps(polobjects, indent=4, sort_keys=True)

    with open('obj_export.json', 'w', ) as jsonFile:
        json.dump(polobjects, jsonFile, indent=4, sort_keys=True)


if __name__ == '__main__':
    main(sys.argv[1:])