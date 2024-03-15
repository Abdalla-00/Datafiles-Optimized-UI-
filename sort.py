def sort_students_age_bubble(lst_dict: list, order: str)-> list:    
    """
    This functions takes two parameters, a list of dictionaries and a string,
    the string has to be either "A" or "D" which represent ascending and 
    descesnding respectively
    
    sort_students_age_bubble([{"Age": 10}, {"Age":19}], "D")
    [{'Age': 19}, {'Age': 10}]
    
    sort_students_age_bubble([{"Age": 10, "Health":"5"}, {"Age":19, "Health":"2"}], "D")
    [{'Age': 19, 'Health': '2'}, {'Age': 10, 'Health': '5'}]
    
    sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    Age" key is not present.
    [{'School': 'GP'}, {'School': 'MS'}]
    """   
    if not all("Age" in i for i in lst_dict):
        print('"Age" key is not present.')
        return lst_dict
    
    else:
        n = len(lst_dict)
        for i in range(n):
            swap_made = False
            for j in range(n - i - 1):
                if order == "A":
                    if lst_dict[j]["Age"] > lst_dict[j + 1]["Age"]:
                        
                        lst_dict[j], lst_dict[j + 1] = lst_dict[j + 1], lst_dict[j]
                        swap_made = True
                elif order == "D":
                    if lst_dict[j]["Age"] < lst_dict[j + 1]["Age"]:
                       
                        lst_dict[j], lst_dict[j + 1] = lst_dict[j + 1], lst_dict[j]
                        swap_made = True
                        
                else:
                    return ('"invalid parameter, use only "A" or "D"')
            if not swap_made: 
                break
        return lst_dict

def sort_students_time_selection(dicts: list[dict], order: str) -> list:
    
    '''
    Returns A sorted list depending on each student's "StudyTime". Indicated in an ascending or 
    Descending by the second parameter. If a student doesn't have a "StudyTime" key, the fn indicates
    that the key isn't present.
    
    >>> sort_students_time_selection ( [{"StudyTime":10.2,"School":"GP"},
                                        {"StudyTime":19.1,"School":"MS"}], "D")
    
    [{"StudyTime": 19.1, "School":"MS"}, {"StudyTime":10.2, "School":"GP"}]

    >>>sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    
    >>>sort_students_time_selection([{"StudyTime":19.1,"School":"MS"},{"School":"GP"},
                                     {"StudyTime": "watermelon!!"}], "D")
    
    "StudyTime" key is not present
    [{'StudyTime': 19.1, 'School': 'MS'}, {'School': 'GP'}, {'StudyTime': 'watermelon!!'}]
    '''
    
    #checks to make sure all dictionaries in list have key named "StudyTime"
    for ind in range(len(dicts)):
        
        if "StudyTime" not in dicts[ind]:
            print('"StudyTime" key is not present')
            return dicts
        
    #sorting list
    
    #Ascending sorting
    if order == "A":
        
        for i in range(len(dicts)):
    
            min_idx = i
            for j in range(i+1, len(dicts)):
                if dicts[min_idx]["StudyTime"] > dicts[j]["StudyTime"]:
                    min_idx = j

            dicts[i], dicts[min_idx] =  dicts[min_idx], dicts[i]  
        return dicts
    
    #Descending sorting    
    elif order == "D":
        
        for i in range(len(dicts)):
    
            min_idx = i
            for j in range(i+1, len(dicts)):
                if dicts[min_idx]["StudyTime"] < dicts[j]["StudyTime"]:
                    min_idx = j

            dicts[i], dicts[min_idx] =  dicts[min_idx], dicts[i]
        return dicts

def sort_students_g_avg_insertion(dic_list: list[dict], order: str) -> list[dict]:
    """
    takes two input a list of dictionaries and a string (“A” or “D”) to determine 
    if the students will be sorted in ascending or descending order based on their 
    'G_Avg' attribute. If 'G_Avg' is not in the dictionary then it will return a 
    statment informing that it is not present
    
    Preconditions:
    
    Examples:
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "D")
    [{'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}]
    
    >>> sort_students_g_avg_insertion( [{"G_Av":7.2,"School":"GP"}, {"G_Av":9.1,"School":"MS"}], "A")
    "G_Avg" key is not present
    [{'G_Av': 7.2, 'School': 'GP'}, {'G_Av': 9.1, 'School': 'MS'}]
    
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "c")
    'invalid order key'
    """
    for i in range(len(dic_list)):
        if dic_list[i].get('G_Avg') == None:
            print('"G_Avg" key is not present')
            return dic_list

        if order == 'A':
            for i in range(1, len(dic_list)):
    
                key = dic_list[i]
                key1 = dic_list[i]["G_Avg"]
            
                # Move elements of arr[0..i-1], that
                # are greater than key, to one position
                # ahead of their current position
                j = i-1
                while j >= 0  and  key1 < dic_list[j]["G_Avg"]:
                    dic_list[j + 1] = dic_list[j]
                    j -= 1
                dic_list[j + 1] = key
            return dic_list

        elif order == 'D':
            for i in range(1, len(dic_list)):
        
                key = dic_list[i]
                key1 = dic_list[i]["G_Avg"]
        
                # Move elements of arr[0..i-1], that
                # are greater than key, to one position
                # ahead of their current position
                j = i-1
                while j >= 0  and  key1 > dic_list[j]["G_Avg"]:
                    dic_list[j + 1] = dic_list[j]
                    j -= 1
                dic_list[j + 1] = key
            return dic_list

    else:
        return 'invalid order key'

#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(A: list, B: str) -> list: 
    """Returns a a new list sorted either in asending order or desending order, 
    or Returns that the Failures key was not present. 
    
    Preconditions: B must be either "A" or "D" . A must be a list of dictionarys
    
    >>> sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    
    [{"Failures": 19, "School":"MS"}, {"Failures":10, "School":"GP"}]
    
    >>> sort_students_failures_bubble([{"School":"GP"}, {"School":"MS"}], "D"}])

    "Failures" key is not present.
    [{"School":"GP"}, {"School":"MS"}]

    >>> sort_students_failures_bubble([{"age":18}, {"age":15}], "A"}]}
    
    "Failures" key is not present.
    [{"age":"18"}, {"age":"15"}]
    
    """
    aux = []
    
    if not all("Failures" in i for i in A):
        print("'Failures' key is not present.") 
        return A 
        
    else:
        sawp = True
        while sawp:
            sawp = False
            if B == "A": 
                for i in range(len(A)-1):
                    if A[i]["Failures"] > A[i+1]["Failures"]: 
                        aux = A[i]
                        A[i] = A[i+1] 
                        A[i+1] = aux 
                        sawp = True
                        
            if B == "D": 
                for i in range(len(A)-1):
                    if A[i]["Failures"] < A[i+1]["Failures"]: 
                        aux = A[i]
                        A[i] = A[i+1] 
                        A[i+1] = aux 
                        sawp = True            
        return A    

def sort(dict_list: list[dict], direction: str, attr: str) -> list[dict]:
    """
    Returns a list of dicts depending on which attribute they want the list the list sorted by,
    and which direction they want it in (ascending/Descending).
    
    Preconditions: 2nd parameter either takes A/D for direction.
    
    >>>sort([{"School":"GP"}, {"School":"MS"}], "A", "Age")
    
    "Age" key is not present.
    [{'School': 'GP'}, {'School': 'MS'}]
    
    >>>sort([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS" }], "D", "Failures")
    
    [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]
    
    >>>sort([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS" }], "D", "APPLES")
    
    Cannot be sorted by APPLES
    [{'Failures': 10, 'School': 'GP'}, {'Failures': 19, 'School': 'MS'}]

    
    """
    
    attributes = ["Age", "StudyTime","G_Avg", "Failures"]
    if attr not in attributes:
        print("Cannot be sorted by {0}". format(attr))
        return dict_list
    
    elif attr == "Age":
        return sort_students_age_bubble(dict_list, direction)
    
    elif attr == "StudyTime":
        return sort_students_time_selection(dict_list, direction)
    
    elif attr == "G_Avg":
        return sort_students_g_avg_insertion(dict_list, direction)    
     
    elif attr == "Failures":
        return  sort_students_failures_bubble(dict_list, direction)      

