
class Student_Record_Manager:
    name = ""
    student_id = 0
    courses_and_grades = dict()

    def string_to_integer(self):    #Nicht erforderlich für die Aufgabe gewesen, habe hier als Versuch mögliche String Eingaben von Zahlen in Integer umgewandelt
        try:
            for grades in self.courses_and_grades:
                self.courses_and_grades[grades] = int(self.courses_and_grades[grades])
            return self.courses_and_grades
        except:
            print("Put a valid number in as the grade ") #Ungültige Eingaben schließen das Programm
            exit()
    
    def tuples_to_dict(self):
        if type(self.courses_and_grades) != dict:   #Für den zweiten Teil der Aufgabe habe ich den Tuple über eine Funktion in eine Dict. umwandeln lassen
            dict_courses = dict()
            for i,j in self.courses_and_grades:
              dict_courses[i] = j

            self.courses_and_grades = dict_courses

        return self.courses_and_grades



    def __init__(self, name:str, student_id:int, courses_and_grades ):
        self.name = name
        self.student_id = student_id
        self.courses_and_grades = courses_and_grades
        
        self.courses_and_grades = self.tuples_to_dict()     #Fächer in Tuple-Form-> Dict.-Form
        self.courses_and_grades = self.string_to_integer()  #String-Zahlen -> Integer-Form 



    def get_average_grade(self):
        all_values = 0
        for grades in self.courses_and_grades.values(): # Fächer werden einzeln durchgegangen und die Values jedes Faches 
            all_values = all_values + grades            # zu einer einzigen Summe addiert

        # for i in self.courses_and_grades:
        #    all_values = all_values + self.courses_and_grades[i]   /Fand beide Varianten interessant und habe die deswegen drin gelassen
        return all_values/len(self.courses_and_grades) #Schritt gespart und direkt die gesamte Summe durch die Länge der Dict. geteilt
    
    def add_course_and_grade(self, course_name, grade):
        self.courses_and_grades[course_name] = grade #Neuer Name mit Neuer Note in DIct. rein
        return self.courses_and_grades
    
    def get_honors_courses(self, threshold = 90):
        honored_courses = dict() 
        for grades in self.courses_and_grades:               #Alle Fächer werden nach Noten überprüft und auf Bed. überprüft
            if self.courses_and_grades[grades] >= threshold: 
                honored_courses[grades] = self.courses_and_grades[grades] #Wenn Bed. erfüllt, kommt das Fach in Honored_c.-Dict. rein
        return honored_courses
    
    def get_unique_grades(self):
        common_courses = {"Math", "German", "English"}
        copy_courses = self.courses_and_grades
        for courses in common_courses:
            if courses in copy_courses:
                del copy_courses[courses]

        unique_courses = copy_courses
        return unique_courses
    
# Berks_grades = {'Math': 85, "German": 97, 'Science': "92", 'History': 78}

# Berk = Student_Record_Manager("Berk", 41334, Berks_grades)
# # print(Berk.get_average_grade())

# test = Berk.add_course_and_grade("AMED", 4)
# # print(test)
# # print(Berk.get_honors_courses())

# # print(Berk.get_unique_grades())    //Sind meine Test Eingaben, nicht wichtig für Assignment



#Aufgaben-Teil 2 Eingaben, Main Methode:
all_students = list()
Berko = Student_Record_Manager("Berk Büyükdeniz", "42352", [('Math', 85), ("German", 97),("Science", 92),('History', 78)])
Ahmed = Student_Record_Manager("Ahmed Talha Tekin", 4234, {"Biology" : 99, "Math": 10, "German": 89, "Spanish": "35"})
Memduh = Student_Record_Manager("Mamduh TALHA Köksal", 4234, {"English" : 55, "Math": "98", "History": "69", "P.E.": "5"})
all_students.append(Berko)
all_students.append(Ahmed)
all_students.append(Memduh)

for i in all_students:
    if i.get_average_grade() >=80:
        print(f"{i.name} has an excellent average of {i.get_average_grade()} and the following honor courses: {i.get_honors_courses()}")
    else: 
        i.add_course_and_grade("Study Skills", 100)
        print(i.name, " has a new course named: ", ["Study Skills"])
