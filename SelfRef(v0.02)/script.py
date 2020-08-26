# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:40:35 2020

@author: Yuri
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:42:41 2020

@author: Yuri
        
"""
#import numpy as np
import csv
import time
from filter_codes import filter_event_cal
from filter_codes import filter_event_pg
from filter_codes import event_count

# import random
from datetime import datetime as dt 

seconds_since_epoch=time.time()  #1469182681.709
utc_date=dt.utcfromtimestamp(seconds_since_epoch) #datetime.datetime(2016, 7, 22, 10, 18, 1, 709000
str_date=str(utc_date)

today = dt.now()
dates = dt.strftime(today, '%m_%d_%Y') 
date_string=str(dates)
#text logs
file_name="logs/data_log"+date_string+".text"
file_name1="logs/data_list"+date_string+".text"
Fn=open(file_name,"a")
#csv logs
csvfile_name="csv_data/csvdata_log"+date_string+".csv"
csvFile=open(csvfile_name, "w",newline="")
writer=csv.writer(csvFile)
heading=["Thought","Type","Date"]
writer.writerow(heading)
def help_commands():
    print("---This is the list of commands and their definitions---\n")
    print("1) update event - executes an input command to take event to focus on \n")
    print("2) v data - gets your valid data or relevant thoughts data and feeds the script\n")
    print("3) iv data - gets your invalid data or irrelevant thought data and feeds the script\n")
    print("4) show pg - saves a copy of a pie graph image containing your invalid and valid thoughts in the image file  \n")
    print("5) show cal pg - saves a copy of a pie graph comparing all the valid thoughts relating to your to do list in the image file\n\n")
    print("6) q - terminates the script\n")
    print("---The script updates user records in realtime via user input---")
    time.sleep(5)
def efilter(y,ls):
    return list(filter(lambda x:x==y, ls))
def nefilter(y,ls):
    return list(filter(lambda x:x!=y, ls))
#This is the thoughts
class thought(object):
    def __init__(self,_type,descrp,_date):
         self._type = _type
         self.descrp = descrp
         self._date = _date   
            #This code splits the data
         def split_data(self):
            if _type=="good":
                valid_data.append(descrp)
            elif _type=="bad":
                invalid_data.append(descrp)
            elif _type=="event":
                focus_thoughts.append(descrp)
         split_data(self)  
    
#This is the mind that generates thoughts
class Mind(object):
    def generate_thought(self,_type,descrp,date):
        return thought(_type, descrp,date)
def pen(INFO,new_com,type_com,current_time):
    with open(file_name1,  "w") as f:
        f.write(">Date: "+date_string+"\n")
        f.write("Invalid: {}".format(len(invalid_data))+"\n")
        f.write("Valid: {}".format(len(valid_data))+"\n")
        f.write("Total data: {}".format(len(valid_data)+len(invalid_data))+"\n")
        f.write("EVENT data\n")
        f.write("event_data=[")
        for aa in focus_thoughts:
            f.write('"'+aa+'"'+",")
        f.write("]\n")
        
        f.write("INVALID thoughts\n")
        f.write("invalid_thoughts=[")
        for aa in invalid_data:
            f.write('"'+aa+'"'+",")
        f.write("]\n")
        f.write("VALID thoughts\n")
        f.write("valid_thoughts=[")
        for aa in valid_data:
            f.write('"'+aa+'"'+",")
        f.write('""'+"]")
        f.close()
    f=open(file_name,"a")
    f.write("\nDescrpt: {}".format(new_com)+"\nType: {}".format(type_com)+"\nDate: {}".format(current_time))
    writer.writerow(INFO)
    f.close()
    print(">===csv input saved===")
    pass
#This function writes down records
def write_file(new_com, type_com, current_time):
    INFO=[new_com, type_com, current_time]
    if type_com=="good":
        pen(INFO,new_com,type_com,current_time)
    elif type_com=="bad":
        pen(INFO,new_com,type_com,current_time)
    elif type_com=="event":
        pen(INFO,new_com,type_com,current_time)

focus_thoughts_data=[]
focus_thoughts=[]

#This is how we encode the values
base_filter=[]

valid_thoughts_data=[]
valid_data=[]

invalid_thoughts_data=[]
invalid_data=[]

#This is the brain variables
brain=Mind()
types=["good","bad"]
command=""

def pie_graph(command, valid_data, invalid_data,focus_thoughts):
    if command=="show pg":
        filter_event_pg(valid_data,invalid_data)
    elif command=="show cal pg":
        filter_event_cal(valid_data,focus_thoughts, invalid_data)
def self_ref():
    print(">initiating program")
    print(">Module imported [COMPLETE]")
    time.sleep(1.5)
    print(">Type 'help' to view commands")
    time.sleep(3)
    command=""
    while command!="q":
        #_____updates the graph constantly_____
        #______opening lines______
        filter_event_cal(valid_data,focus_thoughts, invalid_data)
        filter_event_pg(valid_data,invalid_data)
        #______ending lines______
        
        #These codes constantly updates time
        #______opening lines______
        from datetime import datetime as dt 
        seconds_since_epoch=time.time()  #1469182681.709
        utc_date=dt.utcfromtimestamp(seconds_since_epoch) #datetime.datetime(2016, 7, 22, 10, 18, 1, 709000
        str_date=str(utc_date)
        invalid_thoughts_score=0
        valid_thoughts_score=0
        today = dt.now()
        dates = dt.strftime(today, '%m_%d_%Y') 
        date_string=str(dates)
        #______ending lines______
       
        print("Events to focus")
        event_count(focus_thoughts)
        current_time=today
        print(">enter command")
        command=input(">")
        if command=="v data":
            print(">enter valid data")
            new_com=input(">")
            valid_thoughts_data.append(brain.generate_thought("good", new_com, current_time))
            write_file(new_com, "good", current_time)
            
        elif command=="iv data":
            print(">enter invalid data")
            new_com=input(">")
            invalid_thoughts_data.append(brain.generate_thought("bad", new_com, current_time))
            write_file(new_com, "bad", current_time)
           
            
        elif command=="update event":
            print(">Enter event to focus")
            new_com=input(">")
            focus_thoughts_data.append(brain.generate_thought("event", new_com, current_time))
            write_file(new_com, "event", current_time)
        elif command==pie_graph(command, valid_data, invalid_data,focus_thoughts):
           pass
        elif command in valid_data in focus_thoughts:
            write_file(command, "event", current_time)
        elif command in valid_data:
            write_file(command, "good", current_time)
            valid_data.append(command)
        elif command in invalid_data:
            write_file(command, "bad", current_time)
            invalid_data.append(command)
        elif command in focus_thoughts:
            write_file(command, "event", current_time)
            valid_data.append(command)
        elif command=="help":
            help_commands()

self_ref()
#print(valid_data)
