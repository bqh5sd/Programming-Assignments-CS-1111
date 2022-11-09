#Omid Akbari
#bqh5sd
from urllib.request import urlopen

def departments(dept):
    '''
    The purpose of this function is to open the file for the specified class in a certain department so that
    we can use it for two classes from different departments
    :param dept: Takes in the name of the department
    :return: Returns the data for that department
    '''
    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + dept
    web_data = urlopen(url)
    data = web_data.read().decode('utf-8').strip().split('\n')
    return data

def instructor_lectures(department, instructor):
    '''
    Purpose of this function is to return a list of all the course names for the lectures taught by a given instructor within the
    given department
    :param department: This parameter takes in the department the class is in 
    :param instructor: This parameter takes in the name of the instructor in interest
    :return: This function will return all the lecture class names that the instructor teaches within the specified department
    '''
    final_data = departments(department)
    list_of_courses = []
    for line in range(len(final_data)):
        current_line = final_data[line].split("|")
        if "Lecture" in current_line[5]:
            if current_line[0] in department:
                if instructor in current_line[4]:
                    if current_line[3] not in list_of_courses:
                        list_of_courses += [current_line[3]]
                elif "/" in current_line[4]:
                    if current_line[3] not in list_of_courses:
                        list_of_courses += [current_line[3]]
    return list_of_courses



def compatible_classes(first_class, second_class, needs_open_space=False):
    '''
    The purpose of this function is to return True if the two given classes are compatible within the same schedule and False
    otherwise
    :param first_class: This parameter takes the name of the class, the class number and the class section for the first class
    :param second_class: This parameter takes in the name of the second class with the class number and the class section
    :param needs_open_space: This parameter takes in a boolean and determines whether the function should check the class size
    availability. This parameter is defaulted to false unless otherwise changed when calling this function
    :return: This function will return whether the first and second class are compatible with each other depending on when the
    classes start and end and on the days they occur
    '''

    #Check departments for both classes
    dept = first_class.split()[0]
    dept2 = second_class.split()[0]

    class_1_days = []
    class_2_days = []
    class1_start_time = 0
    class1_end_time = 0
    class2_start_time = 0
    class2_end_time = 0

    # First class
    for line in range(len(departments(dept))):
        data_final = departments(dept)
        current_line = data_final[line].split("|")
        new_line = current_line[0] + " " + current_line[1] + "-" + current_line[2]
        if new_line == first_class:
            if needs_open_space == True:
                if int(current_line[15]) < int(current_line[16]):
                    #Cheeck days which are class happens on
                    for days in range(7,12):
                        if current_line[days] == "true":
                            class_1_days += [days]
                    #cheeck for the start and end times
                    class1_start_time = int(current_line[12])
                    class1_end_time = int(current_line[13])
                    if class1_end_time > 1259:
                        class1_end_time -= 1200
                    if class1_start_time > 1259:
                        class1_start_time -= 1200
                else:
                    return False
            else:
                for days in range(7, 12):
                    if current_line[days] == "true":
                        class_1_days += [days]
                #Cheeck for the start and end times
                class1_start_time = int(current_line[12])
                class1_end_time = int(current_line[13])
                if class1_end_time > 1259:
                    class1_end_time -= 1200
                if class1_start_time > 1259:
                    class1_start_time -= 1200

    #Second class
    for line in range(len(departments(dept2))):
        data_final = departments(dept2)
        current_line = data_final[line].split("|")
        new_line = current_line[0] + " " + current_line[1] + "-" + current_line[2]
        if new_line == second_class:
            if needs_open_space == True:
                if int(current_line[15]) < int(current_line[16]):
                    # Check days which are class happens on
                    for days2 in range(7, 12):
                        if current_line[days2] == "true":
                            class_2_days += [days2]
                    # cheeck for the start and end times
                    class2_start_time = int(current_line[12])
                    class2_end_time = int(current_line[13])
                    if class2_end_time > 1259:
                        class2_end_time -= 1200
                    if class2_start_time > 1259:
                        class2_start_time -= 1200
                else:
                    return False
            else:
                # Cheeck days which are class happens on
                for days2 in range(7, 12):
                    if current_line[days2] == "true":
                        class_2_days += [days2]
                # cheeck for the start and end times
                class2_start_time = int(current_line[12])
                class2_end_time = int(current_line[13])
                if class2_end_time > 1259:
                    class2_end_time -= 1200
                if class2_start_time > 1259:
                    class2_start_time -= 1200

    #Compare day and time
    for days in class_1_days:
        if days in class_2_days:
            if class1_start_time <= class2_start_time <= class1_end_time or class2_start_time <= class1_start_time <= class2_end_time:
                return False
            else:
                return True
        else:
            return True

