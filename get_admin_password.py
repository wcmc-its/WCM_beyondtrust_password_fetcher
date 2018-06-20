#!/usr/bin/python3

import requests
import configparser
import argparse
import getpass


#get some information from a local config file

config = configparser.ConfigParser()
config.read('get_admin_password.conf')

print(config.sections())

default = config['DEFAULT']
username = default['username']
admin_username = default['admin_username']
domain = default['domain']
server = default['server']
api_key = default['api_key']

#for key in default: print(key, default[key])
