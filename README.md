# Latex-with-Python-
"""
Created on Mon Oct 11 20:43:43 2021

@author: Ghislain Afavi, Ph.D. Candidate in economics, University of Montreal

This python script updates a latex file automatically to include a job-related information
like the type of institution, the position, etc.
Comments are welcome to ghislain.afavi@umontreal. Web site: https://sites.google.com/view/ghislain-afavi/home"

To be  able to run this file, you will need:
    
    1. a CSV  file containing the related keys information about the position. Here it is addresses_1.csv (see line 39). The information in the CSV is not a true one.
    2. a latex file. Here it is cover.tex (see line 36). You can change the information to update from line 63 to 71. 
    The information to update is key sensitive. I want to acknowledge that the latex file format is not mine. 
    Any latex file should work.
    3. a python package called pylatex: I  install it  using Anaconda command prompt by typing: pip install pylatex 
    4. Be sure you have a latex compiler installed:    the most popular are  Miktex or TexLive
    
    You are allowed to modify this code without any restriction.
"""
