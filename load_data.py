def student_school_list (filename: str, School: str): 
    """
    This function returns a dictonary which contains the age, studytime, 
    failures, health, absences and G1,G2,G3 of the students depending on what 
    schools they go to
    
    >>>student_school_list("student-mat.csv","GP")
    {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}
    {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}
    {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}
    {another element},
    …]
    
    >>>student_school_list("student-mat.csv","MK")
    []
    
    >>>student_school_list("student-mat.csv","CF")
    [{'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, 
    {'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}, 
    {'Age': 15, 'StudyTime': 2.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, 
    {another element},
    …]
    """
    
    students = []
    
    with open(filename, 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            line = line.strip().split(',')
            if str(line[header.index('School')]) == str(School):
                
                student =  {'Age': int(line[header.index('Age')]), 
                            
                            'StudyTime': float(line[header.index('StudyTime')]),
                            
                            'Failures': int(line[header.index('Failures')]),
                            
                            'Health': int(line[header.index('Health')]),
                            
                            'Absences':int(line[header.index('Absences')]),
                            
                            'G1': int(line[header.index('G1')]),
                            'G2': int(line[header.index('G2')]),
                            'G3': int(line[header.index('G3')])}
                
                students.append(student)
            
        return students

def student_health_list(filepath: str, health: int) -> list: 
    """
    Taking a giving data set and searches for people with the given health value 
    and adds them and all other information associated with them to the returned 
    list. 
    
    Preconditions: filepath must be a string, 0 <= health <= 5
    
    
    >>> student_health_list('student-mat.csv', 2) 
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, 
    {'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, 
    {another element},
    …]  

    >>>student_health_list("student-mat.csv",3)
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, 
    {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, 
    {another element},
    …]
    
    >>>student_health_list("student-mat.csv",12)
    []
    """
    File = open(filepath) 
    Read = File.readlines() 
    studentlist = [] 
    for i in Read[1:]: 
        subset = {}
        i = i.split(',')
        if int(i[4]) == health: 
            subset['School'] = str(i[0])
            subset['Age'] = int(i[1])
            subset['StudyTime'] = float(i[2])
            subset['Failures'] = int(i[3])
            subset['Absences'] = int(i[5])
            subset['G1'] = int(i[6])
            subset['G2'] = int(i[7])
            subset['G3'] = int(i[8])
            studentlist.append(subset)
       
    return studentlist 


def student_age_list (filename: str, age: int) -> list[str]:     
    """ Returns a list of students stored as a dictionary with the same age as the input paramter. 
    
    >>> student_age_list ('student-mat.csv', 15)
    [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}, 
    ...
    ]
    
    >>> student_age_list ('student-mat.csv', 18)
    [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element},
    ...
    ]

    >>> student_age_list ('student-mat.csv', 9)
    []
    """
    
    infile = open (filename, "r")
    wordlist = []


    for word_list in infile: 
        word_list = word_list.split(',')
        
        if word_list [1] == str(age):
            agelist = {'School' : str(word_list[0]), 'StudyTime': float(word_list[2]), 'Failures': int(word_list[3]),'Health': int(word_list[4]),'Absences': int(word_list[5]), 'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            wordlist += [(agelist)]
                
    infile.close()  
    return wordlist

def student_failures_list (csv_file: str, num_failures: int) -> list[dict]:
    """
    Returns a list composed of multiple dictionaries, each of the students with the set amount of faliures called in the second parameter.
    Adds all the other attributes of the student into a dictionary with attributes as keys an their elements as values.
    
    >>> student_failures_list('student-mat.csv', 0)
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 
     'G1': 12, 'G2': 13, 'G3': 14},
    {another element},
    … 
    ]
    
    >>>student_failures_list("student-mat.csv", 4)
    []
    
    >>>student_failures_list("student-mat.csv", 2)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 1, 'Health': 5, 'Absences': 14, 
    'G1': 6, 'G2': 9, 'G3': 8},
    {another element},
    … 
    ]
    """
    
    infile = open(csv_file)    
    answer = []
    count = 0    
     
    for line in infile:
        
        if 0 <= num_failures <= 3 and count > 0:
            y = line.split(',')           

            if int(y[3]) == num_failures: # postion of where the column of failures resides (in the row)
                answer.append({"School"    : str(y[0]),
                               "Age"       : int(y[1]),
                               "StudyTime" : float(y[2]),
                               "Health"    : int(y[4]),
                               "Absences"  : int(y[5]),
                               "G1"        : int(y[6]),
                               "G2"        : int(y[7]),
                               "G3"        : int(y[8])
                               })
        else:
            count += 1
    return answer

def load_data(a: [str], b: [tuple])-> list[dict]:
    
    """
    Returns the function call of the first value of the tuple called with the the tuples second value.
    Results in a list of dicitionaries of attributes excluding the ones called. 
    
    >>>load_data("student-mat.csv",("All", 3))
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, 
    {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, 
    {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, 
    {another element},
    … 
    ]
    
    >>>load_data("student-mat.csv",("G3", 18))
    Invalid Value
    []
    
    
    >>>load_data("student-mat.csv",("Health", 3))
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, 
    {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, 
    {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, 
    {'School': 'GP', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 12, 'G2': 12, 'G3': 11}, 
    {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 10, 'G2': 10, 'G3': 11}, 
    {another element},
    … 
    ]
    """
    skip_line = 0 
    load_set = []
    file = open(a)
    
    if b[0] == "All":
        
        for line in file:
            if skip_line != 0:
                g = line.split(',')
                load_set.append({"School"      : str(g[0]),
                                   "Age"       : int(g[1]),
                                   "StudyTime" : float(g[2]),
                                   "Failure"   : int(g[2]),
                                   "Health"    : int(g[4]),
                                   "Absences"  : int(g[5]),
                                   "G1"        : int(g[6]),
                                   "G2"        : int(g[7]),
                                   "G3"        : int(g[8])
                                   })
            else:
                skip_line += 1
                
        return load_set    
    
    elif b[0] == "School":
        return student_school_list(a,b[1]) 
    elif b[0] == "Health":
        return student_health_list(a, b[1])
    elif b[0] == "Failures":
        return student_failures_list(a, b[1])
    elif  b[0] == "Age":
        return student_age_list(a, b[1])    
    else:
        print("Invalid Value")
        return load_set
    
def add_average(studentlist: list) -> list: 
    """
    Returns an updated list with the privous sets now updated with an average of 
    of the grades inputed
    
    Preconditions: each dictionary in list must contain G1, G2 & G3 values. 
    
    >>>add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, 
    {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}])
    
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, 
    {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}]
    
    >>>add_average([{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, 
    {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}])

    [{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}, 
    {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}]

    """
    list1 = []
    
    for x in studentlist:
        G_Avg = round( ((x['G1'] + x['G2']+ x['G3']) / 3), 2)
        x.update({'G_Avg' : G_Avg})
        list1.append(x)
        
    return list1 
