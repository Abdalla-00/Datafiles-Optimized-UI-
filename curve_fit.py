import matplotlib
import numpy as np
import scipy

def curve_fit(data: list[dict], key: str, deg: int) -> str:
    """
    Takes a list of dictionaries, a string, and an integer to
    return a string representation of the equation of best fit
    for the average of "G_Avg"
    
    Preconditions: 
    "G_Avg" in data
    Values in data are integers
    
    Examples:
    >>>curve_fit([{"Age": 10, "G_Avg": 10}, {"Age": 12, "G_Avg": 14}], "G_Avg", 3)
    '1.0x +-0.0'
    >>>curve_fit([{'G_Avg': 80, 'Math': 1}, {'G_Avg': 90, 'Math': 2}, {'G_Avg': 85, 'Math': 1}, {'G_Avg': 95, 'Math': 3},{'G_Avg': 75, 'Math': 2},{'G_Avg': 80, 'Math': 1}], "Math", 2)
    '0.0x^2+1.0x+0.0'
    >>>curve_fit([{'G_Avg': 69, 'Age': 16}, {'G_Avg': 24, 'Age': 15}, {'G_Avg': 37, 'Age': 18}, {'G_Avg': 101, 'Age': 3},{'G_Avg': 12, 'Age': 12},{'G_Avg': 18, "Age": 1}], "G_Avg", 3)
    '0.0x^3+-0.0x^2+1.0x+-0.0'
    """

    #Takes it from the dictionary and puts it into two lists
    averages = [eachvalue['G_Avg'] for eachvalue in data]
    keyinfo = [eachvalue[key] for eachvalue in data]
    new_data = []

    for i in range(len(averages)):
        new_data.append({keyinfo[i]: averages[i]})

    grouped_new_data = {}

    #Takes each entry in each list and groups them into a dictionary
    #groups them if there are multiple y's for each x
    for eachvalue in new_data:
        for key in new_data:
            for key, value in eachvalue.items():
                if key in grouped_new_data:
                    grouped_new_data[key].append(value)
                else:
                    grouped_new_data[key] = [value]

    average_data = {key: sum(value) / len(value) for key, value in grouped_new_data.items()}

    x = list(average_data.keys())
    y = list(average_data.values())
    string = ""

    if len(x) > deg + 1:
        degree = deg

    else:
        degree = len(x) - 1

    #Makes an expression using polyfit for certain cases
    coeffecients = np.polyfit(x, y, degree)
    order = len(coeffecients) - 1

    for each_num in coeffecients:
        if order == 1:
            string += str(round(each_num, 2)) + 'x' + '+'

        elif order > 1:
            string += str(round(each_num, 2)) + 'x' + '^' + str(order) + '+'

        else:
            string += str(round(each_num, 2))

        order -= 1

    return string