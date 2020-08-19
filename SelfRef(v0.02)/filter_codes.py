# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:41:38 2020

@author: Yuri
"""
#_____This code is under construction, I will add more to alter the data_____
import matplotlib.pyplot as plt
from datetime import datetime as dt 
today = dt.now()
dates = dt.strftime(today, '%m_%d_%Y') 

date_string=str(dates)
#These is how the data will eat itself up until the code mutilates the list
def efilter(y,ls):
    return list(filter(lambda x:x==y, ls))
def nefilter(y,ls):
    return list(filter(lambda x:x!=y, ls))
def filter_event_cal(valid_data,focus_thoughts, invalid_data):

    try:
        #Filtered
        new_list=nefilter(focus_thoughts[0],valid_data)
        filter_0=efilter(focus_thoughts[0],valid_data)
        langs=[ '+Valid data',str(filter_0[0])]
        students=[len(new_list),len(filter_0)]
        print("===First filter===")
        print(len(new_list))
        print(len(valid_data))
        print(len(filter_0))
        
    except IndexError:
        langs=[""]
        students=[0]
        print("Insuffciant data")
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[1],new_list)
        filter_1=efilter(focus_thoughts[1],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0]]
        students=[len(new_list),len(filter_0),len(filter_1)]
        print("\n")
        print("===Second filter===")
        print(len(filter_1))
        print(len(new_list))
        
        
    except IndexError:
        pass
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[2],new_list)
        filter_2=efilter(focus_thoughts[2],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2)]
        print("\n")
        print("===Third filter===")
        print(len(filter_2))
        print(len(new_list))
        
        
    except IndexError:
        pass
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[3],new_list)
        filter_3=efilter(focus_thoughts[3],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3)]
        print("\n")
        print("===fourth filter===")
        print(len(filter_3))
        print(len(new_list))
        
        
    except IndexError:
        pass
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[4],new_list)
        filter_4=efilter(focus_thoughts[4],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4)]
        print("\n")
        print("===fifth filter===")
        print(len(filter_4))
        print(len(new_list))
        
        
    except IndexError:
        pass
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[5],new_list)
        filter_5=efilter(focus_thoughts[5],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5)]
        print("\n")
        print("===sixth filter===")
        print(len(filter_5))
        print(len(new_list))
        
        
    except IndexError:
        pass
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[6],new_list)
        filter_6=efilter(focus_thoughts[6],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6)]
        print("\n")
        print("===seventh filter===")
        print(len(filter_6))
        print(len(new_list))
        
        
    except IndexError:
        pass
  #eight
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[7],new_list)
        filter_7=efilter(focus_thoughts[7],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0],filter_7[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6),len(filter_7)]
        print("\n")
        print("===eight filter===")
        print(len(filter_7))
        print(len(new_list))
        
        
    except IndexError:
        pass
  #ninth
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[8],new_list)
        filter_8=efilter(focus_thoughts[8],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0],filter_7[0],filter_8[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6),len(filter_7),len(filter_8)]
        print("\n")
        print("===ninth filter===")
        print(len(filter_8))
        print(len(new_list))
        
        
    except IndexError:
        pass
  #tenth
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[9],new_list)
        filter_9=efilter(focus_thoughts[9],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0],filter_7[0],filter_8[0],filter_9[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6),len(filter_7),len(filter_8),len(filter_9)]
        print("\n")
        print("===tenth filter===")
        print(len(filter_9))
        print(len(new_list))
        
        
    except IndexError:
        pass
  #eleventh filter
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[10],new_list)
        filter_10=efilter(focus_thoughts[10],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0],filter_7[0],filter_8[0],filter_9[0],filter_10[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6),len(filter_7),len(filter_8),len(filter_9),len(filter_10)]
        print("\n")
        print("===eleventh filter===")
        print(len(filter_10))
        print(len(new_list))
        
        
    except IndexError:
        pass 
  #12 filter
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[11],new_list)
        filter_11=efilter(focus_thoughts[11],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0],filter_7[0],filter_8[0],filter_9[0],filter_10[0],filter_11[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6),len(filter_7),len(filter_8),len(filter_9),len(filter_10),len(filter_11)]
        print("\n")
        print("===12 filter===")
        print(len(filter_11))
        print(len(new_list))
    except IndexError:
        pass  
  #13filter
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[12],new_list)
        filter_12=efilter(focus_thoughts[12],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0],filter_7[0],filter_8[0],filter_9[0],filter_10[0],filter_11[0],filter_12[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6),len(filter_7),len(filter_8),len(filter_9),len(filter_10),len(filter_11),len(filter_12)]
        print("\n")
        print("===13 filter===")
        print(len(filter_12))
        print(len(new_list))
        
        
        
    except IndexError:
        pass         
  #14filter
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[13],new_list)
        filter_13=efilter(focus_thoughts[13],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0],filter_7[0],filter_8[0],filter_9[0],filter_10[0],filter_11[0],filter_12[0],filter_13[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6),len(filter_7),len(filter_8),len(filter_9),len(filter_10),len(filter_11),len(filter_12),len(filter_13)]
        print("\n")
        print("===14 filter===")
        print(len(filter_13))
        print(len(new_list))

    except IndexError:
        pass 
  #15filter
    try:
                #Filtered
        new_list=nefilter(focus_thoughts[14],new_list)
        filter_14=efilter(focus_thoughts[14],valid_data)
        langs=[ '+Valid data',str(filter_0[0]), filter_1[0],filter_2[0],filter_3[0],filter_4[0],filter_5[0],filter_6[0],filter_7[0],filter_8[0],filter_9[0],filter_10[0],filter_11[0],filter_12[0],filter_13[0],filter_14[0]]
        students=[len(new_list),len(filter_0),len(filter_1),len(filter_2),len(filter_3),len(filter_4),len(filter_5),len(filter_6),len(filter_7),len(filter_8),len(filter_9),len(filter_10),len(filter_11),len(filter_12),len(filter_13),len(filter_14)]
        print("\n")
        print("===15 filter===")
        print(len(filter_14))
        print(len(new_list))

    except IndexError:
        pass 

    langs.append('Invalid data')
    students.append(len(invalid_data))

    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])
    ax.axis('equal')
    # langs=[ '+Valid data',str(filter_0[0]),str(filter_1[0])]
    # students=[len(vT1),len(filter_0),len(filter_1)]
    ax.pie(students, labels=langs,autopct='%1.2f%%')
   
    plt.title='survival rate'
    plt.savefig("images/calpie_grap"+date_string+".png")
    plt.close()
   


def filter_event_pg(valid_data,invalid_data):
    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])
    ax.axis('equal')
    langs=[ 'Valid data','Invalid data']
    students=[len(valid_data),len(invalid_data)]
    ax.pie(students, labels=langs,autopct='%1.2f%%')
    plt.savefig("images/pie_grap"+date_string+".png")
    plt.close()
   
#filter_event_cal(valid_data,focus_thoughts)
"""
this code counts the events, due to the complications of installing sklearn on pydroid and use 
the preprocessing module, I created our own :), that can go up to 15 events cause nobody
can upscale their focus quantity than that far per day =). 15 is the limit
"""
#_____opening lines_____

#filter_event_cal(valid_data,focus_thoughts)
"""
this code counts the events, due to the complications of installing sklearn on pydroid and use 
the preprocessing module, I created our own, that can go up to 15 events cause nobody
can upscale their focus quantity than that far per day =). 15 is the limit
"""
#_____opening lines_____

def event_count(focus_thoughts):
    one=""
    two=""
    three=""
    four=""
    five=""
    six=""
    seven=""
    eight=""
    nine=""
    onezero=""
    oneone=""
    onetwo=""
    onethree=""
    onefour=""
    onefive=""
    count_15=[" 1)","2)","3)","4)","5)","6)","7)","8)","9)","10)","11)","12)","13)","14)","15)"]
    try:
        one=count_15[0]+" {}".format(focus_thoughts[0])
    except IndexError:    
        pass
    try:
        two=count_15[1]+" {}".format(focus_thoughts[1])
    except IndexError:    
        pass
    try:
        three=count_15[2]+" {}".format(focus_thoughts[2])
    except IndexError:    
        pass
    try:
        four=count_15[3]+" {}".format(focus_thoughts[3])
    except IndexError:    
        pass
    try:
        five=count_15[4]+" {}".format(focus_thoughts[4])
    except IndexError:    
        pass
    try:
        six=count_15[5]+" {}".format(focus_thoughts[5])
    except IndexError:    
        pass
    try:
        seven=count_15[6]+" {}".format(focus_thoughts[6])
    except IndexError:    
        pass
    try:
        eight=count_15[7]+" {}".format(focus_thoughts[7])
    except IndexError:    
        pass
    try:
        nine=count_15[8]+" {}".format(focus_thoughts[8])
    except IndexError:    
        pass
    try:
        onezero=count_15[9]+" {}".format(focus_thoughts[9])
    except IndexError:    
        pass
    try:
        oneone=count_15[10]+" {}".format(focus_thoughts[10])
    except IndexError:    
        pass
    try:
        onetwo=count_15[11]+" {}".format(focus_thoughts[11])
    except IndexError:    
        pass
    try:
        onethree=count_15[12]+" {}".format(focus_thoughts[12])
    except IndexError:    
        pass
    try:
        onefour=count_15[13]+" {}".format(focus_thoughts[13])
    except IndexError:    
        pass
    try:
        onefive=count_15[14]+" {}".format(focus_thoughts[14])
    except IndexError:    
        pass
    return print(one,"\n",two,"\n",three,"\n",four,five,six,seven,eight,nine,onezero,oneone, onetwo,onethree,onefour,onefive)

#_____closing lines______

#_____closing lines______


