#import check module here
import check

#import load_data module here
from load_data import *

def test_return_list():

    # test that student_school_list returns a list 
    check.equal(type(student_school_list('student-test.csv', 'B')), type([]))
    check.equal(type(student_school_list('student-test.csv', 'GP')), list)
    check.equal(type(student_school_list('student-test.csv', 'MB')), list)

    # test that student_age_list returns a list 
    check.equal(type(student_age_list('student-test.csv', 18)), list)
    check.equal(type(student_age_list('student-test.csv', 12)), type([]))
    check.equal(type(student_age_list('student-test.csv', 17.5)), type([]))

    # test that student_health_list returns a list 
    check.equal(type(student_health_list('student-test.csv', 5)), list)
    check.equal(type(student_health_list('student-test.csv', -1)), type([]))
    check.equal(type(student_health_list('student-test.csv', 0)), list)

    # test that student_failures_list returns a list 
    check.equal(type(student_failures_list('student-test.csv', 0)), list)
    check.equal(type(student_failures_list('student-test.csv', 1)), list)
    check.equal(type(student_failures_list('student-test.csv', -2)), type([]))

    # test that load_data returns a list 
    check.equal(type(load_data('student-test.csv', ("School", "GP"))), list)
    check.equal(type(load_data('student-test.csv', ("Age", 17))), list)
    check.equal(type(load_data('student-test.csv', ("Failures", 1))), list)
    check.equal(type(load_data('student-test.csv', ("School", 'MB'))), list)
    check.equal(type(load_data('student-test.csv', ("Health", 3))), list)
    check.equal(type(load_data('student-test.csv', ("Health", 2))), list)

    # test that add_average returns a list 
    check.equal(type(add_average(load_data("student-test.csv", ("School", "GP")))), list)
    check.equal(type(add_average(load_data("student-test.csv", ("Health", 0)))), list)
    check.equal(type(add_average(load_data("student-test.csv", ("Failures", 2)))), list)
    check.summary()

def test_return_list_correct_lenght():
    
    #test that student_school_list returns a list with the correct lenght
    check.equal(len(student_school_list("student-test.csv", "GP")), 3) 
    check.equal(len(student_school_list("student-test.csv", "MS")), 4)
    check.equal(len(student_school_list("student-test.csv", "MB")), 2)
    
    #test that student_age_list returns a list  with the correct lenght
    check.equal(len(student_age_list("student-test.csv", 18)), 4) 
    check.equal(len(student_age_list("student-test.csv", 15)), 3)
    check.equal(len(student_age_list("student-test.csv", 17)), 6)    
    
    #test that student_health_list returns a list  with the correct lenght 
    check.equal(len(student_health_list("student-test.csv", 3)), 8) 
    check.equal(len(student_health_list("student-test.csv", 5)), 3)
    check.equal(len(student_health_list("student-test.csv", 4)), 3)    
    
    #test that student_failures_list returns a list   with the correct lenght
    check.equal(len(student_failures_list("student-test.csv", 0)), 11) 
    check.equal(len(student_failures_list("student-test.csv", 1)), 1)
    check.equal(len(student_failures_list("student-test.csv", 2)), 2)    
    
    #test that load_data returns a list  with the correct lenght 
    check.equal(len(load_data("student-test.csv" , ("School", "GP"))), 3) 
    check.equal(len(load_data("student-test.csv" , ("Health", 3))), 8)
    check.equal(len(load_data("student-test.csv" , ("Failures", 2))), 2)
    check.equal(len(load_data("student-test.csv" , ("Age", 18))), 4)
    check.equal(len(load_data("student-test.csv" , ("School", "MS"))), 4)
    check.equal(len(load_data("student-test.csv" , ("Health", 5))), 3)

     #test that add_average returns a list with the correct lenght 
    check.equal(len(add_average(load_data("student-test.csv" , ("School", "GP")))), 3)
    check.equal(len(add_average(load_data("student-test.csv" , ("Health", 3)))), 8)
    check.equal(len(add_average(load_data("student-test.csv" , ("Age", 17)))), 6)
    check.summary()

def test_return_correct_dict_inside_list():
    
    #test that student_school_list returns a correct dictionary inside the list 
    check.equal(student_school_list("student-test.csv", "GP")[0], ({'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}))
    check.equal(student_school_list("student-test.csv", "GP")[-1], ({'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}))
    check.equal(student_school_list("student-test.csv", "MS")[0], ({'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}))
    check.equal(student_school_list("student-test.csv", "CF")[-1], ({'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}))    
    check.equal(student_school_list("student-test.csv", "Random"), ([]))   
    
    #test that student_age_list returns a correct dictionary inside the list
    check.equal(student_age_list("student-test.csv", 18)[0], ({'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}))   
    check.equal(student_age_list("student-test.csv", 18)[-1], ({'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))   
    check.equal(student_age_list("student-test.csv", 15)[0], ({'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}))   
    check.equal(student_age_list("student-test.csv", 15)[-1], ({'School': 'CF', 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}))   
    check.equal(student_age_list("student-test.csv", 19), ([]))   
    check.equal(student_age_list("student-test.csv", 14), ([]))   
    
    #test that student_health_list returns a correct dictionary inside the list
    check.equal(student_health_list("student-test.csv", 5)[0], ({'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}))   
    check.equal(student_health_list("student-test.csv", 5)[-1], ({'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))  
    check.equal(student_health_list("student-test.csv", 3)[0], ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}))   
    check.equal(student_health_list("student-test.csv", 3)[-1], ({'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}))
    check.equal(student_health_list("student-test.csv", 1)[0], ({'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}))       
    check.equal(student_health_list("student-test.csv", 2), ([]))
    check.equal(student_health_list("student-test.csv", 6), ([]))   
    check.equal(student_health_list("student-test.csv", 0), ([]))   
    
    
    
    #test that student_failures_list returns a correct dictionary inside the list
    check.equal(student_failures_list("student-test.csv", 0)[0], ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}))
    check.equal(student_failures_list("student-test.csv", 0)[-1], ({'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))
    check.equal(student_failures_list("student-test.csv", 1)[0], ({'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}))
    check.equal(student_failures_list("student-test.csv", 2)[0], ({'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}))
    check.equal(student_failures_list("student-test.csv", 3)[0], ({'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}))
    check.equal(student_failures_list("student-test.csv", 4), ([]))
  
    #test that load_data returns a correct dictionary inside the list
    check.equal(load_data("student-test.csv",("All", 3))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failure': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data("student-test.csv",("All", 3))[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failure': 3, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})    
    check.equal(load_data("student-test.csv", ("Health", 3))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data("student-test.csv",("School", "MS"))[0], {'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10})
    check.equal(load_data("student-test.csv",("Failures", 3))[-1],  {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(load_data("student-test.csv",("Age", 18))[2], {'School': 'BD', 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12})
    check.equal(load_data("student-test.csv",("Bananas", 9)), [])
    
     #test that add_average returns a correct dictionary inside the list
    check.equal(add_average([{'School': 'MB', 'Age': 15, 'StudyTime': 1.0, 'Failure': 1, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}, 
                             {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failure': 5, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}]), 
                           ([{'School': 'MB', 'Age': 15, 'StudyTime': 1.0, 'Failure': 1, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33}, 
                             {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failure': 5, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7, 'G_Avg': 7.0}]))
    check.equal(add_average([{'G1': 10, 'G2': 2, 'G3': 40}]), ([{'G1': 10, 'G2': 2, 'G3': 40, 'G_Avg': 17.33}]))
    check.equal(add_average([{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}]),
                            [{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9, 'G_Avg': 9.33}])
    check.summary()

def test_add_average():

    check.equal(len(add_average(student_school_list("student-test.csv", "GP"))), 3)
    check.equal(len(add_average(student_health_list("student-test.csv", 3))), 8)
    check.equal(len(add_average(student_age_list("student-test.csv", 6))), 0)
    check.equal(len(add_average(student_failures_list("student-test.csv", 2))), 2)
    check.equal(len(add_average(load_data("student-test.csv", ("All",0)))), 15)
    
        
    #test that the function returns an empty list when it is called whith an empty list
    check.equal(add_average([]), [])
    
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one
    check.equal(len(add_average(student_school_list("student-test.csv", "GP"))[2]), 9)
    check.equal(len(add_average(student_failures_list("student-test.csv", 0))[-2]), 9)
    check.equal(len(add_average(student_age_list("student-test.csv", 17))[0]), 9)
    check.equal(len(add_average(student_health_list("student-test.csv", 5))[1]), 9)
    check.equal(len(add_average(load_data("student-test.csv", ("All",0)))[3]), 10)
            
    #test that the G_Avg value is properly calculated
    check.within(add_average(student_school_list("student-test.csv", "GP"))[0]['G_Avg'], 5.67, 0)
    check.within(add_average(student_failures_list("student-test.csv", 0))[3]['G_Avg'], 11.33, 0)
    check.within(add_average(student_age_list("student-test.csv", 17))[-1]['G_Avg'], 14.0, 0)
    check.within(add_average(student_health_list("student-test.csv", 5))[2]['G_Avg'], 8.33, 0)
    check.within(add_average(load_data("student-test.csv", ("All",0)))[5]['G_Avg'], 7.0, 0)
    
    check.summary()