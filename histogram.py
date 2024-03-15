from load_data import *
import matplotlib.pyplot as plt

def histogram(lst_dict: list, attr: str):
    
    """
    This function produces a histogram based on the list of dictionaries given 
    and the string which acts as the attribute
    
    the input should look something like:
    
    lst_dict = [
    {"School": "GP", "Health": 3, "G_Avg": 3.5},
    {"School": "MB", "Health": 2, "G_Avg": 2.8},
    {"School": "MB", "Health": 4, "G_Avg": 3.9},
    {"School": "GP", "Health": 1, "G_Avg": 2.1},
    {"School": "GP", "Health": 2, "G_Avg": 3.2},
    {"School": "GP", "Health": 3, "G_Avg": 3.6} ]
    

    histogram(lst_dict, "School")

    this will produce a histogram with G_Avg as the attribute on the x-axis and
    the # of students that the G_Avg value corresponds to on the y-axis.
    
    if you were to input School as the attribute instead then it would display
    what number of students go to their corresponding schools
    
    """
    
    attr_values = {}
    
    for i in lst_dict:
        if attr in i:
            values = i[attr]
            if type(values) == int or type(values) == float:
                values = int(values)
                attr_values.setdefault(values, 0)
            else:
                attr_values.setdefault(values, 0)
    
    for n in lst_dict:
        if attr in n:
            value = n[attr]
            if type(value) == float:
                value = int(value)
            attr_values[value] += 1
     
    plt.bar(attr_values.keys(), attr_values.values(), align='center')
    plt.xlabel(attr)
    plt.ylabel('# of Students')
    plt.title('Histogram')
    plt.show()
    
    return None