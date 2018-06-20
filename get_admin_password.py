#!/usr/bin/python

import requests
import configparser
import argparse
import getpass


#get some information from a local config file

config = configparser.ConfigParser()
config.read('get_admin_password.conf')

default = config['DEFAULT']
username = default['user']
server = default['server']
api_key = default['api_key']
