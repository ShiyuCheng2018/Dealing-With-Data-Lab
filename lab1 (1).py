'''
ISTA 131
Lab 1 08/23
This lab will provide practice with functions, strings, loops, 
lists, dictionaries, and classes.
'''


class ClassObj:
    def __init__(self, dept, num, day, start_time):
        '''
        The ClassObj class represents a single University class. 
        It should have to methods: an init and a repr.
        It has four instance variables, all with defualt arguments of the empty string.
        dept: the 2 to 4-letter department code (ex. ISTA)
        num the 3-digit class number (ex. 131)
        day: the days the course lecture meets (ex. TTh, MWF, MW, etc.)
        start_time: the hour and minute lecture starts (ex. 3:00)
        Write the class to check if each variable exists (hint: 
        the empty string is None), and if not, take user input for each.

        The ClassObj should also have a repr function. When printed, 
        it should look like this:
        ISTA 131: MW at 9:30
        '''

        if (dept != None):
            self.dept = dept
        if (num != None):
            self.num = num
        if (day != None):
            self.day = day
        if (start_time != None):
            self.start_time = start_time

    def __repr__(self):
        return self.dept + " " + self.num + ": " + self.day + " at " + self.start_time


def scheduler():
    '''
    This function returns a list of ClassObjs. It asks the user if 
    they would like to add a class, and repeats the process until 
    the user says no. Be sure to account for capitalization!
    '''

    class_array = []
    answer = input("would you like to add a class?")
    while (answer.lower() == "yes"):
        dept = input("Please type dept :")
        num = input("please type num :")
        day = input("please type day :")
        start_time = input("please type start_time :")
        my_class = ClassObj(dept, num, day, start_time)
        class_array.append(my_class)
        answer = input("would you like to add a class? ")

    return class_array


def course_to_classes(class_array):
    '''
    This function takes a schedule (list of ClassObjs) as its sole parameter. It 
    returns a dictionary with the dept code as the key mapping 
    to a list of course numbers. 

    Example: {ISTA: [116, 130], RELI: [271], ENG: [110]}
    '''
    classes_dict = {}
    for my_class in class_array:

        if classes_dict.__contains__(my_class.dept):
            classes_dict[my_class.dept].append(my_class.num)
        else:
            classes_dict[my_class.dept] = [my_class.num]

    return classes_dict


def main():
    '''
    Create and print a schedule and schedule dictionary.
    '''
    print("###################################")
    my_scheduler = scheduler()
    print("###################################")
    print("...................................")
    print(my_scheduler)
    print("...................................")
    print(course_to_classes(my_scheduler))


if __name__ == '__main__':
    main()
