import numpy as np
from scipy import ndimage
import sys
import glob
import os
import math
import pandas as pd



trans_file = raw_input('Enter the name of the file containing the transmitter info (including the extension):')
rec_file = raw_input('Enter the name of the file containing the receiver info (including the extension):')

#Reads in the info for all transmitters, i.e. NAME, LATITUDE, LONGITUDE, from a single text file
house_df = pd.read_csv(str(trans_file),names =['Farm', 'Lat', 'Long'], delim_whitespace=True) 
dish_df = pd.read_csv(str(rec_file),names =['Dish', 'D_Long', 'D_Lat'], delim_whitespace=True) 


trans_height = raw_input('Enter the height of the transmitter/s along with the unit of meters, example 3m:')
rec_height = raw_input('Enter the height of the receiver/s along with the unit of meters, example 10m:')

out_file = raw_input('Enter the name of the output/results file (including the extension):')

#---------------------------------create qth files---------------------------------------------------------------------
#this function creates .qth files for each farm house Tx
def create_qth_file():

  for i in range(len(house_df['Farm'])): 
    Farm_name = house_df['Farm'][i] 
    Lat = house_df['Lat'][i]
    Long = 360.0 - house_df['Long'][i]
    Height = str(trans_height)                                                                                  
    
    with open(str(Farm_name)+'.qth', 'w') as house_file:
      house_file.write(str(Farm_name)+'\n')
      house_file.write(str(Lat)+'\n')
      house_file.write(str(Long)+'\n')
      house_file.write(Height)
      
  return
  
#create_qth_file()             #calls the function to create .qth files for the transmitters



#this function creates .qth files for each dish Rx
def create_qth_file_dish():

  for i in range(len(dish_df['Dish'])): 
    Dish_name = dish_df['Dish'][i] 
    Dish_Lat = dish_df['D_Lat'][i]
    Dish_Long = 360.0 - dish_df['D_Long'][i]
    Dish_Height = str(rec_height)                                                                                
    
    with open(str(Dish_name)+'.qth', 'w') as dish_file:
      dish_file.write(str(Dish_name)+'\n')
      dish_file.write(str(Dish_Lat)+'\n')
      dish_file.write(str(Dish_Long)+'\n')
      dish_file.write(Dish_Height)
      
  return
  
#create_qth_file_dish()          #calls the function to create .qth files for the dishes 


#-------------------------------------put dish qth files in a python list------------------------------------------------------

#This searches for all files with a .qth extension in the folder called 'Dish_info'
#dishes = [f.split('/')[1] for f in glob.glob("Dish_info/*.qth")]




#creates column names in a python panda dataframe

Tx_cols = ['Transmitter', 'Tx location', 'Tx elevation', 'Tx height','Tx height above avg terrain', 'Distance to Rx','Azimuth to Rx', 'Depression angle to Rx', 'Dep angle to first obstruction from Tx']

Tx_df = pd.DataFrame(columns=Tx_cols)

Rx_cols = ['Receiver', 'Rx location', 'Rx Elevation', 'Rx height',' Rx height above avg terrain', 'Distance to Tx', 'Azimuth to Tx', 'Depression angle to Tx',
'Dep angle to first obstruction from Rx']

Rx_df = pd.DataFrame(columns=Rx_cols)

ITM_cols = ['Earth Dielectric Constant', 'Earth Conductivity', 'Atmospheric Bending Constant', 'Frequency', 'Radio Climate', 'Polarization',
    'Fraction of Situations', 'Fraction of Time', 'Transmitter ERP', 'Transmitter EIRP']
    
ITM_df = pd.DataFrame(columns=ITM_cols) 

Summary_cols = ['FSPL', 'Longley-Rice PL','Attenuation due to terrain', 'Field strength at Rx', 'Signal power level at Rx', 'Signal power density at Rx',
'Voltage across 50ohm dipole at Rx', 'Voltage across 75ohm dipole at Rx']

Summary_df = pd.DataFrame(columns=Summary_cols)


#*****************************************iterate splat calls***********************************************************
#***********************************************************************************************************************
no_of_houses = input('Enter the number of transmitters: ')
no_of_dishes = input('Enter the number of receivers: ')



Tx_missing_header = open('header_info_missing_Tx', 'w')
Rx_missing_header = open('header_info_missing_Rx', 'w')

#headers which are sometimes missing in the SPLAT output file
problem_headers_Tx= ['Antenna height above average terrain','Depression angle to the first obstruction']
problem_headers_Rx= ['Antenna height above average terrain','Elevation angle to the first obstruction']


for i in range(no_of_dishes):
  for j in range(no_of_houses):
   # print "###################################",str(house_df['Farm'][j]),"################################"
   
    os.system("splat -t "+str(house_df['Farm'][j])+" -r "+str(dish_df['Dish'][i])+" -metric"+" -olditm")

    output_files_list = [ f for f in glob.glob("*.txt") if '-to-' in f]

    #for output_file in output_files_list:
    with open (output_files_list[0], 'r') as stuff:
     contents = stuff.read()

    info = [word.strip() for word in (contents.split('Mode of propagation: Longley-Rice model error number:')[0].split('---------------------------------------------------------------------------'))]
  
    Tx_info = info[1]
    Rx_info = info[2]
    ITM_info = info[3]
    Summary_info = info[4]
    
    #print output_file[0]
    Tx_vals = [word.strip().split(':')[1] for word in Tx_info.strip().split('\n')]
    Tx_header = [word.strip().split(':')[0] for word in Tx_info.strip().split('\n')]
    

    if problem_headers_Tx[1] not in Tx_header:    
      Tx_missing_header.write(str(j) + '\n')
      Tx_missing_header.write(str(problem_headers_Tx)+  str(len(problem_headers_Tx)) + '\n')
      Tx_missing_header.write(str(Tx_cols)+  str(len(Tx_cols)) + '\n')
      Tx_missing_header.write(str(Tx_header)+  str(len(Tx_header)) + '\n\n\n')
 
    
    Rx_vals = [word.strip().split(':')[1] for word in Rx_info.strip().split('\n')]
    Rx_header = [word.strip().split(':')[0] for word in Rx_info.strip().split('\n')]
  
    if problem_headers_Rx[1] not in Rx_header:    
      Rx_missing_header.write(str(j) + '\n')
      Rx_missing_header.write(str(problem_headers_Rx)+  str(len(problem_headers_Rx)) + '\n')
      Rx_missing_header.write(str(Rx_cols)+  str(len(Rx_cols)) + '\n')
      Rx_missing_header.write(str(Rx_header)+  str(len(Rx_header)) + '\n\n\n')
  
  
    ITM_first_split = [word for word in ITM_info.strip().split('\n')[2::]]
    ITM_vals = [word.split(':')[1] for word in ITM_first_split]
   
    Summary_first_split = [word for word in Summary_info.strip().split('\n')[2::]]
    Summary_vals = [word.split(':')[1] for word in Summary_first_split]
  
    # All is well
    if (len(Tx_vals)==9):
        Tx_df.loc[len(Tx_df)] = Tx_vals
    # One col is missing i.e.   first problematic header, replaced with zeroes
    elif (len(Tx_vals)==8 and problem_headers_Tx[0] not in Tx_header):
        Tx_vals.insert(4,'0 meter')
        Tx_df.loc[len(Tx_df)] = Tx_vals
    # One col is missing i.e.   second problematic header, replaced with zeroes
    elif (len(Tx_vals)==8 and problem_headers_Tx[1] not in Tx_header):
        Tx_vals.insert(8,'0 degrees')
        Tx_df.loc[len(Tx_df)] = Tx_vals
    # Two cols are missing i.e.   first and second problematic header, replaced with zeroes
    elif (len(Tx_vals)==7):
        Tx_vals.insert(4,'0 meters')
        Tx_vals.insert(8,'0 degrees')
        Tx_df.loc[len(Tx_df)] = Tx_vals


    # All is well
    if (len(Rx_vals)==9):
        Rx_df.loc[len(Rx_df)] = Rx_vals
    # One col is missing i.e.   first problematic header, replaced with zeroes
    elif (len(Rx_vals)==8 and problem_headers_Rx[0] not in Rx_header):
        Rx_vals.insert(4,'0 meters')
        Rx_df.loc[len(Rx_df)] = Rx_vals
    # One col is missing i.e.   second problematic header, replaced with zeroes
    elif (len(Rx_vals)==8 and problem_headers_Rx[1] not in Rx_header):
        Rx_vals.insert(8,'0 degrees')
        Rx_df.loc[len(Rx_df)] = Rx_vals
    # Two cols are missing i.e.   first and second problematic header, replaced with zeroes
    elif (len(Rx_vals)==7):
        Rx_vals.insert(4,'0 meters')
        Rx_vals.insert(8,'0 degrees')
        Rx_df.loc[len(Rx_df)] = Rx_vals
      
    ITM_df.loc[len(ITM_df)] = ITM_vals
    Summary_df.loc[len(Summary_df)] = Summary_vals
    
    Results_df = pd.concat([Rx_df,Tx_df,ITM_df,Summary_df], axis=1)
    Results_df.to_csv(str(out_file))                                                               

    # deletes the splat output files
    site_file = [ f for f in glob.glob("*.txt") if 'site_report' in f]
    os.remove(output_files_list[0])
    os.remove(site_file[0])
    
    
    