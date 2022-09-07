# -*- coding: utf-8 -*-
"""
Design and implement a class to represent professors and scheduled
courses
▪  A professor is described by:
▪   Name good
▪   Courses the professor is allowed to teach good
▪   Courses the professor is scheduled to teach during the semesters good
▪  Operations on professors:
▪   Add/Remove a course the professor is allowed to teach (e.g. ISI300)good
▪   Add/Remove a course for a semester as a pair <semester,course> (e.g. Sp19,ISI300)
▪   Remove all scheduled courses for a given semester
▪   Remove all scheduled courses for a given course
▪  Note:
▪   A prof can be scheduled to teach a course for a semester only if the course being 
assigned to the prof is one of those the professor is allowed to teach

"""

class Professor:
    def __init__(self,Name):
        self.__Name=Name
        self.__Allowed_Courses=[]
        self.__Semester=[]
    
    #setters
    def set_Name(self,Name):
        self.__Name=Name
        
    def set_Allowed_Courses(self,course):
        self.__Allowed_Courses.append(course)
    
    def set_semester(self,semester):
        self.__Semester=semester
        
    def set_Semester_Courses(self,semester,course):
        if (course in self.__Allowed_Courses):
            self.__Semester.append((semester,course))
        else:
            print("Professor Cannot teach the course",course)
        
        
    #getters
    def get_Name(self):
        print("Professor Name: ",self.__Name)
    
    def get_Allowed_Courses(self):
        print("Allowed Courses to teach",self.__Allowed_Courses)
    
    def get_Semester_Courses(self):  
            return self.__Semester

            
            
    def remove_Allowed_Courses(self,Courses):
        for i in range(len(self.__Allowed_Courses)):
            if(self.__Allowed_Courses[i]==Courses):
                self.__Allowed_Courses.remove(Courses)
                print("Removed",Courses)
            break

    def remove_Semester_Courses(self,semester,courses):
            if((semester,courses) in self.__Semester):
                self.__Semester.remove((semester,courses))
            print("Removed",courses," from ",semester)
            

Cap=Professor("Cappellari")
Cap.set_Name("John")
Cap.set_Allowed_Courses("ISI 300")
Cap.set_Allowed_Courses("CSC 315")
Cap.set_Allowed_Courses("ISI 315")

#good




Cap.set_Semester_Courses("Fall 2021","ISI 300")
Cap.set_Semester_Courses("Spring 2022","CSC 315")
Cap.set_Semester_Courses("Fall 2021","ISI 315")

Cap.get_Name()
Cap.get_Allowed_Courses()
print("Printing the semester courses ", Cap.get_Semester_Courses())
Cap.remove_Allowed_Courses("ISI 300")
Cap.get_Allowed_Courses()
Cap.remove_Semester_Courses("Fall 2021","ISI 300")
print("Printing the semester courses the second time ", Cap.get_Semester_Courses())





