# Program: Marks Calculator
# Author: Bhavya Sharma
# Marks Calculator for Exam Result

# Student Details
name = input("Enter Name: ")
student_class = int(input("Enter Class: "))

if student_class <=8 :
    section = input("Enter Section: ")
    # m Input
    print("\nEnter maximum Marks for each subject:")                #byBhavyaSharma
    m_comp = int(float(input("Computer: ")))
    m_ma = int(float(input("Mathematics: ")))
    m_sc = int(float(input("Science: ")))
    m_ss = int(float(input("Social Studies: ")))
    m_eng = int(float(input("English: ")))
    m_s = int(float(input("Sanskrit: ")))                                        #byBhavyaSharma
    m_h =  int(float(input("Hindi: ")))            
    # Score Input
    print("\nEnter Marks You Obtained:")
    c = int(float(input("Computer: ")))
    ma = int(float(input("Mathematics: ")))
    sc = int(float(input("Science: ")))
    ss = int(float(input("Social Studies: ")))
    eng = int(float(input("English: ")))                                        #byBhavyaSharma
    s= int(float(input("Sanskrit: ")))
    h=  int(float(input("Hindi: ")))
    # Net Calculations
    total_m = m_comp + m_ma + m_sc + m_ss + m_eng + m_s + m_h
    total_obtained = c + ma + sc + ss + eng + s + h                                            #byBhavyaSharma
    percentage = (total_obtained / total_m) * 100
    # Final Output
    print( name, "of" , student_class , section , "has scored totally" , total_obtained , "out of" , total_m , "and final score is", percentage , "%")
    print("\n")
    print("Program Ends Here")                                         #byBhavyaSharma

else:
    section = input("Enter Section: ")
    # m Input                                                                                    #byBhavyaSharma
    print("\nEnter maximum Marks for each subject:")
    m_ai = int(float(input("AI or IT: ")))
    m_ma = int(float(input("Mathematics: ")))
    m_sc = int(float(input("Science: ")))                                                                        #byBhavyaSharma
    m_ss = int(float(input("Social Studies: ")))
    m_eng = int(float(input("English: ")))                                                                                                                                        #byBhavyaSharma                    
    m_l = int(float(input("Sanskrit/Hindi: ")))                                                                                                                                   #byBhavyaSharma 
    # Score Input                                                                                                            #byBhavyaSharma
    print("\nEnter Marks Obtained:")
    ai = int(float(input("AI or IT: ")))
    ma = int(float(input("Mathematics: ")))
    sc = int(float(input("Science: ")))
    ss = int(float(input("Social Studies: ")))
    eng = int(float(input("English: ")))
    l = int(float(input("Sanskrit/Hindi: ")))                                                    #byBhavyaSharma
    # Net Calculations
    total_m = m_ai + m_ma + m_sc + m_ss + m_eng + m_l
    total_obtained = ai + ma + sc + ss + eng + l                                                                                                                                  #byBhavyaSharma      
    percentage = (total_obtained / total_m) * 100                                                        #byBhavyaSharma                                                          #byBhavyaSharma
    # Final Output                                                                                                                                                                #byBhavyaSharma
    print( name, "of" , student_class , section , "has scored totally" , total_obtained , "out of" , total_m , "and final score is", percentage , "%")                            #byBhavyaSharma
    print("\n")                                                        #byBhavyaSharma                                                                                            #byBhavyaSharma
    print("Program Ends Here")
