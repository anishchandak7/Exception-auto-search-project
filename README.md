# Stackoverflow-Auto-Search-Project or Exception - Auto - Search

Steps to follow:

Here in this project, i have tested two files, one is sample.py and another is test.py to check the project's working.
Before diving into the project, check the workflow.png to understand the working of auto-search file.

It's fun and learning project which helped me to understand some cool and handy features of stackoverflow api's and
python libraries. Thanks to https://www.crio.do/projects/ which has some great fun projects and guide for them.

Sample files used in this project are:
* sample.py
* test.py

auto_search.py:
  This file will take command and script type (here by default is python for now) and will fetch top 5 links of stackoverflow 
  for error occured in sample files.
 
 main.py: 
   This file will ask the user about the command and it will analyse the command and search for sample files if they exist, then it will
   check if error exist or not, if exist, then it will suggest the user stackoverflow links related to error and prompt the user what to 
   next.
   
   (NOTE: In main.py user will also be asked for sample files location, this can be modified in future as per the requirement.)
   
   Choices of what to next are:
   1. Open a specific link
   2. Open all at Once.
