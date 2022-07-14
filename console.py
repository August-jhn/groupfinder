from group import *
import read_group
import draw_group
import draw_color_graph
import csv

#main directory for me: C:\Users\augus\IntroToPython\number_theory\number_theory_fun\groupfinder

DEBUG = False

HELPSCRIPT = """
/help -- creates a list of all commands you can type
/quit -- closes the program
/make_group [group name] [directory] -- makes a group that can now be played with.
 Once you name a group, you can always rename it using the /rename command. 
 Every group has a list of names. Any name should work
/list_elements [group name]
/make_cyclic_subgroup [group name for subgroup] [group name] [element]
/list_groups -- lists out all of the groups you've made, and all the ones that are already there
/find_left_coset [group name] [subgroup name] [element] -- finds the left coset for a certain element and lists it for you
/make_center [group name] [element] -- finds C(a) in an element 'a' in a group. This also adds a group to the list of groups


"""
GREETINGSCRIPT = """Welcome to August's 'group journal'
    
    My code is not in a super presentable state, so please don't look at it yet.
    Instead, I've made this simple interface so you can play with some of the basic
    things my program can do.

    for a list of commands, type /help
    to quit, type /quit
    """
#https://youtu.be/UZX5kH72Yx4 # use later to make into nice executable

def make_group_from_csv(directory,name):

    #try:

    def make_ordered_pairs(directory):
        """this function takes the csv file Cayley table and creates a dictionary of ordered pairs"""

        elements = [] #this will be a collection of all the elements in the group
        rows = [] #this will be the collection of all the rows in the Cayley table

        pairs = {} #this will be of the form {(a,b) : x}. As in ab = x

        with open(directory, 'r') as csvfile: #opens the csv file and then processes it into usable information
            csvreader = csv.reader(csvfile)

            elements = next(csvreader)
            elements = elements[1:]

            for row in csvreader:
                rows.append(row)
        for r in range(len(rows)): #turns that information into the final product
            for c in range(len(rows[0])):
                if c >= 0: 
                    a = elements[r]
                    b = elements[c-1]
                    pairs[(a,b)] = rows[r][c]
        
        return pairs, elements

    pairs,elements = make_ordered_pairs(directory)
    return Group(elements,pairs,name,DEBUG)
    
    #except:
    #    print("Failed to make group. Are you in the right directory?")

def main():
     # a dictionary of groups with keys of strings, group names
    """where the main stuff happens"""
    print(GREETINGSCRIPT)
    groups = {}

    while True:
        command = input("% ")
        if command == "/help":

            print(HELPSCRIPT)

        elif command == "/quit":

            break

        elif "/make_group " in command:
            print("making group")
            arguments = command.split(" ")
            if len(arguments) > 3:
                print("too many arguments")
            elif len(arguments) < 3:
                print("missing arguments")

            group_name = arguments[1]
            group_directory = arguments[2]
            the_group = make_group_from_csv(group_directory,group_name)

            if the_group is not None:
                groups[group_name] = the_group
            else:
                print("failed to make group, type /help for instructions")

        elif "/list_elements " in command:
            arguments = command.split(" ")
            the_group = None
                
            name = arguments[1]
            try:
                the_group = groups[name]
            except:
                print("not valid group name, type /list_groups for a list of existing groups")
            if the_group is not None:
                print(the_group.get_elements_set())
        elif "/make_cyclic_subgroup " in command:

            arguments = command.split(" ")
            name = arguments[1]
            element = arguments[2]
            the_group = None
            try:
                the_group = groups[name]
                if element in the_group.get_elements_set():
                    groups["<{}>".format(element)] = the_group.find_cyclic_group(element)
                    print("made cyclic subgroup {}".format("<{}>".format(element)))
                else:
                    print("invalid element")

            except:
                print("invalid group name")
        elif "/list_groups" == command:
            for group in groups:
                print(group) #refer to the __repr__ function in group.Group
            if len(groups) == 0:
                print("you don't have any groups! type make_group to make a group from a Cayley table")
        
        elif "/find_left_coset " in command:

            arguments = command.split(" ")
            group_name = arguments[1]
            subgroup_name = arguments[2]
            element = arguments[3]
            
            the_group = None

            try:
                the_group = groups[group_name]
                subgroup = groups[subgroup_name]
            except:
                print("invalid group name")

            if the_group is not None and subgroup in the_group.get_subgroups() and element in the_group.get_elements():
                print(the_group.find_left_coset(element,subgroup))

        elif "/find_center " in command:
            arguments = command.split(" ")
            name = arguments[1]
            element[2]

            the_group = None
            

            try:
                the_group = groups[name]
            except:
                print("invalid group name")

            if group is not None:
                print("this command is still in development")

        elif "/make_center " in command:

            arguments = command.split(" ")
            name = arguments[1]
            element = arguments[2]

            group = groups[name]
            center_elements = group.find_zenter(element)
            center_list = [e for e in center_elements]
            center = Group(center_list, group.get_pairs(), "C(a)",False)
            groups["C({a})".format(a = element)] = center
            print(center.get_elements_set())

        elif "/make_centralizer " in command:
            arguments = command.split(" ")
            name = arguments[1]

            group = groups[name]
            
            centralizer = Group([e for e in group.find_center()], group.get_pairs(), "Z(G)",False)
            groups["Z({G})".format(G = group)] = centralizer


        else:
            print("sorry, unknown command. Type /help for list of commands")

if __name__ == "__main__":
    main()