#Omid Akbar
#bqh5sd
from urllib.request import urlopen

def departments(class_name):
    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + class_name
    web_data = urlopen(url)
    data = web_data.read().decode('utf-8').strip().split('\n')
    return data


def instructor_lectures(department, instructor):
    '''
    Purpose of this function is to return a list of all the course names for the lectures taught by a given instructor within the
    given department
    :param department:
    :param instructor:
    :return:
    '''
    print(department)
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
    :param first_class:
    :param second_class:
    :param needs_open_space:
    :return:
    '''

    dept = first_class.split()[0]

    data_final = departments(dept)

    class_1_days = []
    class_2_days = []
    class1_start_time = 0
    class1_end_time = 0
    class2_start_time = 0
    class2_end_time = 0

    for line in range(len(data_final)):
        current_line = data_final[line].split("|")
        new_line = current_line[0] + " " + current_line[1] + "-" + current_line[2]
        #first class
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
                # cheeck for the start and end times
                class1_start_time = int(current_line[12])
                class1_end_time = int(current_line[13])
                if class1_end_time > 1259:
                    class1_end_time -= 1200
                if class1_start_time > 1259:
                    class1_start_time -= 1200

        #Second class
        if new_line == second_class:
            if needs_open_space == True:
                print(current_line[15])
                print(current_line[16])
                if int(current_line[15]) > int(current_line[16]):
                    print("TEST")
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

#print(compatible_classes("CS 1110-001", "MATH 1160-001", True))

#print(compatible_classes("CS 1110-001", "CS 2110-001", True))
