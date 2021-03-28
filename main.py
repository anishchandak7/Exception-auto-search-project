# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:30:16 2021

@author: anish chandak
"""

from auto_search import fetch_links
import webbrowser
import time

global links
global chrome_path
import os

# Allows the user to select a specific link in chrome browser
def open_specific_link():
    
    link_number = int(input("Link number: "))
    
    link_number = link_number-1
    
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
    
    if(link_number>=0 and link_number<len(links)):
        
        browser = webbrowser.get('chrome')
        time.sleep(2)
        browser.open_new_tab(links[link_number])
    else:
        print("Wrong link selected!!!")
        return

# Allows the user to open all the links at once in same browser.
def open_all_at_once():
    
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'    
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
    
    browser = webbrowser.get('chrome')
    
    for link in links:
        browser.open_new_tab(link)
    

if __name__ == '__main__':
    
    users_cmd = input("Enter your command:\n")
    l = users_cmd.strip().split()
    script_type,file_name = l[0],l[1]
    
    file_path = input("Give file path:\n")
    file_path_files = os.listdir(file_path)
    
    # print(file_path_files)
    
    if file_name in file_path_files:
        links = fetch_links(test_cmd=users_cmd,script_type=script_type)
    else:
        print("USING DEFAULT TEST FILE!!!")
        # User can fetch the related stackoverflow link either mentioning the command
        # Here command is already specified, user can test it with different scripts using test_cmd parameter.
        links = fetch_links()
        # Display top 5 suggested links 
    print('\n')
    print('*'*20 + ' Suggested links '+'*'*20)
    print('\n')
    for i in range(len(links)):
        print(str(i+1)+'.',links[i])
    
    print('\n')
    # User is provided with options what he wants to do next:
    while(True):
        
        print('1. Open specific link')
        print('2. Open all at Once')
        print('3. Exit')
        print('\n')
        
        switcher = {
            1:open_specific_link(),
            2:open_all_at_once()
            }
        
        # User's choice
        choice = int(input('Your input: '))
        
        if(choice==3):
            break
        
        print(switcher[choice])
    