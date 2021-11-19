"""
.SYNOPSIS
  A program which extracts Cisco running configs from single dump file.
  
.DESCRIPTION
  Digests lines from input file and exports individual running configs devices/hosts that match start and end keys-terms. 
  Currently only searches for files in current directory.
  
.PARAMETER <Parameter_Name>
  None
    
.INPUTS
  session.log (Currently only searches in current directory)
  
.OUTPUTS
  ./configOutput/*-config.txt
  
.NOTES
  Version:        3.03
  Author:         Dennis Ozmert
  GitHub:         https://github.com/dozmert1
  Creation Date:  27/09/2021 @ 9:00am
  Last Updated:   27/10/2021
  Purpose/Change: Device config backup
  License:        GNU General Public License
  
.EXAMPLE
  .\configExtract-Cisco.py
 
.CITED WORK
  Generic works found on Google.
"""
# --------------------------------------------------
## Imports and values
#
import os
startCmd = 'sh run'#key used to find the new config lines
endCmd = 'exit'
fileInput = 'session.log' #Source file
destDir = 'configOutput' #Destination folder name
# --------------------------------------------------
## Functions
def outputDir(): 
    if os.path.exists(destDir):
        print('Destination directory already exists...')
    else:
        os.mkdir(destDir)
        print('Destination directory being created...')
#
def hostExtract(i):
    printMask = i.index('#')
    hostFound = (i[:printMask]) #Used to create output files
    currentDir = os.getcwd()
    saveDir = '/'+str(destDir)+'/'
    nameDir = hostFound+'' #Used to append to end of filename
    hostExtract.compDir = os.path.join(currentDir+saveDir+nameDir+'-config.txt') #Final output composition
    with open(hostExtract.compDir,'w+') as f0:
        f0.close()
#
def fileExtract(): 
    extractCount = 0
    global runCount #Temporary method to track count of extracted configs
    runCount = 0
    with open(fileInput,'r') as f1:
        for i in f1:
            if extractCount == 1:
                with open(hostExtract.compDir,'a') as f2:
                    f2.write(i)
            if startCmd in i:
                hostExtract(i)
                extractCount = 1
                runCount += 1
                with open(hostExtract.compDir,'a') as f2:
                    f2.write(i)
            elif endCmd in i:
                extractCount = 0
                with open(hostExtract.compDir,'a') as f2:
                    f2.close()
    return runCount
# --------------------------------------------------    
## Code start
print('Program starting...')
outputDir()                    
fileExtract()
print(runCount,'Hosts found using','"'+startCmd+'"','and','"'+endCmd+'".')
print('Program ending.')
# --------------------------------------------------
