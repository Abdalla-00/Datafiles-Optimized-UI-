from load_data import *
from sort import *
from curve_fit import *
from histogram import *



inp = ''
data = []
load_atts = ('All', 'Failures', 'Age', 'Health', 'School')
sorting_atts = ('Age', 'StudyTime', 'Failures', 'G_Avg')
curve_atts = ('G_Avg', 'StudyTime', 'Failures', 'Age', 'Health', 'Absences')

while inp.upper() != "E":
    print("The available commands are:\n")
    print("\tL)oad Data")
    print("\tS)ort Data")
    print("\tC)urve Fit")
    print("\tH)istogram")
    print("\tE)xit\n")
    inp = input("Please type your command: ")
    
    if inp.upper() == 'L':
        name_of_file = input("Please enter the name of the file: ")
        att = input("Please enter the attribute to use as a filter: ")

        while att not in load_atts:
            print('Invalid attribute')
            att = input("Please enter the attribute to use as a filter: ")
        
        if att != 'All':
            val = input("Please enter the value of the attribute: ")
            
            if att == 'School':
                data = load_data(name_of_file, (att, val))                          
            else:
                data = load_data(name_of_file, (att, int(val)))
                
        elif att == 'All':
            data = load_data(name_of_file, (att, 'any'))            
            
        data = add_average(data)
        if data == []:
            print("Input is invalid. Please try again.\n")
        else:
            print("Data loaded") 
            
            
    elif inp.upper() == 'S':
        if data == []:
            print("File not loaded. Please load a file first.")
        else:
            print("Please enter the attribute you want to use for sorting: ")
            att1 = input("'Age'  'StudyTime' 'Failures'  'G_avg'\n: ")
            
            while att1 not in sorting_atts:
                print('Invalid attribute')
                att1 = input("Please enter the attribute you want to use as a filter: ")
            else:
                order = input("Ascending (A) or Descending (D) order: ")
                data = sort(data, order, att1)
                ans = input("Data Sorted. Do you want to display the data?: ")
                if ans.upper() == 'Y':
                    print(data)
        
    elif inp.upper() == 'C':
        if data == []:
            print("File not loaded. Please load a file first.")
        else:
            att2 = input("Please enter the attribute you want to use to find the best fit for G_Avg: ")
            
            while att2 not in curve_atts:
                print('Invalid attribute')
                att2 = input("Please enter the attribute you want to use to find the best fit for G_Avg: ")

            pol_order = input("Please enter the order of the polynomial to be fitted: ")
            print(curve_fit(data, att2, int(pol_order)))
        
    elif inp.upper() == 'H':
        if data == []:
            print("File not loaded. Please load a file first.")
        else:
            att3 = input("Please enter the attribute you want to use for plotting: ")
            print(histogram(data, att3))
            
    elif inp.upper() == 'E':
        break
    
    else: 
        print("Invalid command")