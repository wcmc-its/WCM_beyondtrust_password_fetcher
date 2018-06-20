#!/usr/bin/python3

import requests, json
import configparser
import argparse
from getpass import getpass
from pprint import pprint


#get some information from a local config file

config = configparser.ConfigParser()
config.read('get_admin_password.conf')

#print(config.sections())

default = config['DEFAULT']
username = default['username']
admin_username = default['admin_username']
domain = default['domain']
server = default['server']
api_key = default['api_key']
verify_ssl = default.getboolean('verify_ssl')
#for key in default: print(key, default[key])

# post-processing for config
if not "https://" in server:
	server = "https://" + server

bt_user = domain + "\\" + username
# get users password
bt_user_password = getpass("please enter the password for " + bt_user + ": ")



# some commonly used API paths in the BT API
bt_api = { "SignAppin": "/BeyondTrust/api/public/v3/Auth/SignAppin",
	"ManagedAccounts": "/BeyondTrust/api/public/v3/ManagedAccounts",
	"SignOut": "/BeyondTrust/api/public/v3/Auth/SignOut" }



# build session object
bt_session = requests.Session()

# build request for initial auth
initial_auth_url = server + bt_api['SignAppin']
initial_auth_headers = {'Authorization': "PS-Auth key=" + api_key + "; runas=" + bt_user + ";"}

# make initial auth request
response = bt_session.post(initial_auth_url, headers=initial_auth_headers, verify=verify_ssl)

# make second auth request with password and duo push information
second_auth_url = server + bt_api['SignAppin']
second_auth_headers = {'Authorization': "PS-Auth key=" + api_key + "; runas=" + bt_user + "; challenge=push; pwd=[" + bt_user_password + "];"}

print("Please check your phone for a Duo authentication request")

response = bt_session.post(second_auth_url, headers=second_auth_headers, verify=verify_ssl)

pprint(response.status_code)
pprint(response.headers)
pprint(response.text)
