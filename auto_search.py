# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:57:35 2021

@author: anish chandak
"""

# Necessary Imports

from subprocess import Popen, PIPE
import requests

def execute(cmd):
    
    # Splits the command on ' ' and convert it into list.
    command = cmd.split()
    # Popen takes command in the form of list, then we created 
    # standard PIPEline for output and error stream.
    proc = Popen(command, stdout=PIPE, stderr= PIPE)
    # calling communicate method to run the process which will return us
    # standard process output and error.
    stdout,stderr = proc.communicate()
    # Then we return the stdout and stderr 
    return stdout,stderr

def fetch_json(error_message,tag = 'python'):
    
    # API's URL 
    URL = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged="+tag+"&intitle="+error_message+"&site=stackoverflow"
    
    # Performing a get request to fetch the result in req variable.
    try:
        req = requests.get(url = URL)
    except:
        return {}
    
    # Returning the result in JSON format.
    return req.json()

def fetch_links(test_cmd = None,script_type = 'python'):
    
    # test_cmd = "python sample.py"
    stdout, stderr = execute(test_cmd)
    error_message = stderr.decode("UTF-8").strip().split("\r\n")
    
    json_output = fetch_json(error_message=error_message[-1],tag = script_type)
    
    links = []
    count = 5
    for item in json_output['items']:
        
        if(item['is_answered']==True and count>0 and script_type in item['tags']):
            links.append(item['link'])
            count-=1
    return links
        
        
    