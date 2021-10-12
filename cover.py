# -*- coding: utf-8 -*-
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
    3. a python package called pylatex : I  install it  using Anaconda command prompt by typing: pip install pylatex 
    4. Be sure you have a latex compiler installed:    the most popular are  Miktex or TexLive
    
    You are allowed to modify this code without any restriction.
"""

#import numpy as np
import os
import subprocess
from csv import DictReader
#from csv import reader


# importing from a pylatex module if
# from pylatex import Document, Section, Subsection, Tabular
# from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
# from pylatex.utils import italic


Typedoc= 'cover'  # the name of the latex document you want to update automatically 
Myname='Afavi'  # update  with your name. the ouput file will be something like cover_Afavi

with open('addresses_1.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            print(row['Zip']) # just to check that it reads well the information in the csv file
         
            Inst= row['Institution']
            Dept= row['Department']
            Adr1= row['Address1']
            Adr2= row['Address2']
            Adr3= row['Address3']
            City= row['City']
            State= row['State']
            Zip= row['Zip']
            Country=row['Country']
            
            
            fin = open(str(Typedoc)+".tex", "r")   #   open the latex file  which is the type document typedoc
#read file contents to string
            fileout = fin.read()  #   read de file fin
           # Coverout =open("teaching.tex", "wt")
#replace all occurrences of the required string: replace in the original file the name of the instution, department, ...country
            fileout=  fileout.replace('INSTITUTION', Inst)
            fileout=   fileout.replace('DEPARTMENT', Dept)
            fileout=   fileout.replace('ADDRESS1', Adr1)
            fileout=   fileout.replace('ADDRESS2', Adr2)
            fileout=   fileout.replace('ADDRESS3', Adr3)
            fileout=   fileout.replace('CITY', City)
            fileout=   fileout.replace('STATE', State)
            fileout=   fileout.replace('ZIP', Zip)
            fileout=   fileout.replace('COUNTRY', Country ) 
            
#create  the output file  with name  filename
 
            filename =  str(Typedoc)+"_" +str(Myname)+"_"+ str(Inst)  #  the name of the new file
            filename= ''.join(filename.split())  #  removing all the white space in the filename
         
            fout= open(filename+".tex", "wt")   # create a new latex file called  filename to write in
            fout.write(fileout)   #  write  in the output file  the replaced typedoc in fileout
               #generate_pdf('DSS', clean_tex=False)
            fin.close()
            fout.close()
            # read the new file created  and compile it
            
             #finn = open(filename+".tex", "r")
             #os.system("pdflatex fin") # another way to compile a latex file using  os system need to import os
            subprocess.call(['pdflatex', filename+".tex"])
            os.remove (filename+".aux") #  remove latex generic file with extension aux log  tex and out
            os.remove (filename+".log")
            os.remove (filename+".out")
            os.remove (filename+".tex")
             #finn.close()
                   


