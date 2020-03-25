#!/usr/bin/python3

# accept commands from the cli
import argparse
# we want to work with json
import json
def main():
    inventory = {} # create a dict called inventory
    if args.list: # if a user pass --list to our script
        inventory = example_inventory() # run the function example_inventory
    elif args.host: # not implimented, if a user passes --host to our script
        inventory = empty_inventory()
    else: # if the user does not pass a flag
        inventory = empty_inventory()
    print(json.dumps(inventory))   # print inventory dict as JSON on the screen
# this would actually be our auditing logic
def example_inventory():  
    return {
        'group': {
            'hosts': ['centurylink-webserver']
            },
        '_meta': {
            'hostvars': {
                'centurylink-webserver': {
                    'ansible_connection': 'local',
                    'ansible_host': 'localhost'}}}}

def empty_inventory():
    return {}
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action = 'store_true')
    parser.add_argument('--host', action = 'store')
    args = parser.parse_args()
    main()
