import glob
import os
import pandas as pd

def Automated(Txin, Rxin, NoTran, NoRec, Transh, Rech, Outname):
    print("We left")
    #============================= Inputs =========================================
    Txinput = Txin                                                          #CHANGE TRANSMITTER FILE NAME
    Rxinput = Rxin                                                          #CHANGE RECEIVER FILE NAME
    Receiverheight = Rech                                                          #Change Receiver height
    Transmitterheight = Transh
    numtrans = NoTran
    numrec = NoRec
    Outfilename = Outname
    
    #======================== Read in Files ======================================
    
    house_df = pd.read_csv(Txinput,names =['Farm', 'Long', 'Lat'])#delim_whitespace=True)   
    dish_df = pd.read_csv(Rxinput,names =['Dish','D_Long','D_Lat'])#delim_whitespace=True)    
    
    #=========== Creates QTH Files from input Tx Files ============================
    def create_qth_file():
      for i in range(len(house_df['Farm'])): 
        Farm_name = house_df['Farm'][i] 
        Lat = house_df['Lat'][i]
        Long = 360.0 - house_df['Long'][i]
        Height = Transmitterheight                                                                                   
        
        with open(str(Farm_name)+'.qth', 'w') as house_file:
          house_file.write(str(Farm_name)+'\n')
          house_file.write(str(Lat)+'\n')
          house_file.write(str(Long)+'\n')
          house_file.write(Height)
      return
      
    create_qth_file()             
    
    #=========== Creates QTH Files from input Rx Files ============================
    def create_qth_file_dish():
      for i in range(len(dish_df['Dish'])): 
        Dish_name = dish_df['Dish'][i] 
        Dish_Lat = dish_df['D_Lat'][i]
        Dish_Long = 360.0 - dish_df['D_Long'][i]
        Dish_Height = Receiverheight                                                                                
        
        with open(str(Dish_name)+'.qth', 'w') as dish_file:
          dish_file.write(str(Dish_name)+'\n')
          dish_file.write(str(Dish_Lat)+'\n')
          dish_file.write(str(Dish_Long)+'\n')
          dish_file.write(Dish_Height)
      return
      
    create_qth_file_dish()          #calls the function to create .qth files for the dishes 
    
    #=========== Creates Pana Dataframe with headings ============================
    
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
    
    no_of_houses = numtrans
    no_of_dishes = numrec
    
    Tx_missing_header = open('header_info_missing_Tx', 'w')
    Rx_missing_header = open('header_info_missing_Rx', 'w')
    problem_headers_Tx= ['Antenna height above average terrain','Depression angle to the first obstruction']
    problem_headers_Rx= ['Antenna height above average terrain','Elevation angle to the first obstruction']
    
    #======================== Iteration Loops =====================================
    
    for i in range(no_of_dishes):
      for j in range(no_of_houses):
       
        os.system("splat -t "+str(house_df['Farm'][j])+" -r "+str(dish_df['Dish'][i])+" -metric"+" -olditm" +" -kml"+" -H "+str(dish_df['Dish'][i])+" -nf"+" -m 1400" )
        output_files_list = [ f for f in glob.glob("*.txt") if '-to-' in f]
    
        with open (output_files_list[0], encoding = "latin-1") as stuff:
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
        Results_df.to_csv(Outfilename)                                                                #!!!!!!!!!!!!!!CHANGE OUTPUT FILE NAME
    
    #======================Delete Filese =======================================
        site_file = [ f for f in glob.glob("*.txt") if 'site_report' in f]
        os.remove(output_files_list[0])
        os.remove(site_file[0])
    
    
    
