from load_data import *
from sort import *
from curve_fit import *
from histogram import *

y = "Any"

while y != 'E' :

    main = input("Please enter the name of the file where your commands are stored \n:")
    file = open(main, "r")
    s = []
    
    #forms a list for each command, stores all in a list
    for line in file:
        line = line.strip().split(";")
        s.append((line))
    
    #forms a list containing,all commands to eb executed
    cmnds= []
    for first_ind in s:
        cmnds.append(first_ind[0])
       
    i = 0 #used to indicate the inx of command
    for command in cmnds:
        
        #Exits UI system, by breaking for loop then while loop
        if command == "E" or command == "e":
            y = command.upper()
            break
                
        if command == "l" or command =="L":
            
            if s[i][2] == 'School':
                data = load_data(s[i][1], (s[i][2], s[i][3]))                 
            
            elif s[i][2] == 'All':
                data = (load_data(s[i][1],(s[i][2], "any")))        
            
            else:
                val = int(s[i][3])
                data = load_data(s[i][1],(s[i][2],val))
                
            data = add_average(data)
            print("Data loaded") 
            i += 1
                
        elif command == "S" or command =="s":
            data = sort(data, s[i][2], s[i][1])
            print("Data Sorted.")
            
            if s[i][3] == "Y":
                print(data)
            i += 1    
    
        elif command == "C" or command == "c":
            deg = int(s[i][2])
            eqn = curve_fit(data, s[i][1], deg)
            print(eqn)
            i += 1
        
        elif command == "H" or command =="h":
            histogram(data, s[i][1])
            i += 1
    

