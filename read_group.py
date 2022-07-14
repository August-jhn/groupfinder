import csv
from group import *
import draw_group
import draw_color_graph

def get_file():
    print("welcome to the group finder reader, please enter csv file name for Cayley table")
    file_found = False

    while not file_found:
        try:
            return open(input("enter name here: "),mode = "r")
        except:
            key  = input("file not found, please press any key to try again or type 'Q' to quit\n")
            if key == 'Q':
                file_found = True



def make_ordered_pairs(table_name):
    """this function takes the csv file Cayley table and creates a dictionary of ordered pairs"""

    elements = [] #this will be a collection of all the elements in the group
    rows = [] #this will be the collection of all the rows in the Cayley table

    pairs = {} #this will be of the form {(a,b) : x}. As in ab = x

    with open(table_name, 'r') as csvfile: #opens the csv file and then processes it into usable information
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

def check_closed(pairs, elements):
    """checks the closrue property"""
    closed = True
    for pair in pairs:
        if pairs[pair] not in elements:
            closed = False
            #print(pair)
    return closed

def check_inverse(pairs,elements):
    inverses = True
    for e1 in elements:
        has_inverse = False
        for e2 in elements:
            if pairs[(e1,e2)] == 'z':
                has_inverse = True
        if not has_inverse:
            inverses = False
    return inverses

def find_center_element(pairs, elements, a):
    """this function finds the center of a given element"""
    center = []
    for b in elements:
        if pairs[(a,b)] == pairs[(b,a)]:
            center.append(b)
    return center

def find_inverse_element(pairs, elements, a):
    """this function finds the inverse of a given element"""
    tries = 0
    while True:
        for e in elements:
            if pairs[(a,e)] == 'z':
                return e
        if tries > len(elements):
            return None
        
        tries += 1

def find_center(pairs,elements):
    center = []
    for a in elements:
        if find_center_element(pairs,elements, a) == elements:
            center.append(a)
    return center

def find_cyclic_group(pairs,elements, a):
    """finds the cyclic group of an element and its order"""
    cycle = {a}
    na = pairs[(a,a)]
    order = 1
    while na != a:
        order += 1
        cycle.add(na)
        na = pairs[(na,a)]
        if len(cycle) > len(elements):
            return cycle, None
    return cycle, order

def sort_cylcic_groups(pairs, elements):
    cycles = [find_cyclic_group(pairs,elements,e) for e in elements]
    cycles_filtered = []
    for i in range(len(cycles)):
        in_there = False
        for j in range(i):
            if cycles[i] == cycles[j] and i != j:
                in_there = True
        if not in_there:
            cycles_filtered.append((elements[i],cycles[i]))
    return cycles_filtered
            
def sort_centralizers(pairs,elements):
    centralizers = []
    centralizers_sets = []
    for e in elements:
        centralizer = find_center_element(pairs,elements,e)
        crset = set()
        for element in centralizer:
            crset.add(element)
        if crset not in centralizers_sets and len(crset) < len(elements):
            centralizers.append((e,centralizer, len(crset)))
            centralizers_sets.append(crset)
    return centralizers


if __name__ == "__main__":
    def check_stuff():
        pairs, elements = make_ordered_pairs("group_51_table.csv")
        print("closed: " +str(check_closed(pairs,elements)))
        print("Inverse property: "  + str(check_inverse(pairs,elements)))
        print(find_center_element(pairs, elements, 'v'))
        for e in elements:
            print("the center of", e, "is: ", find_center_element(pairs, elements, e))
            print("the cyclic subgroup and order of ", e, "is", find_cyclic_group(pairs, elements, e))
        print("the group's center is: ", find_center(pairs,elements))
        for e in elements:
            print("the inverse of", e, "is",find_inverse_element(pairs, elements, e))
        print(sort_cylcic_groups(pairs,elements))
        print(sort_centralizers(pairs,elements))
        
        group = Group(elements,pairs,"G51",True)
        print(group.check_group())
        #draw_group.draw_group(group, 300,.75,True)
        print(group.find_zenter('a'))
        print(group.find_cyclic_subgroups())
        print(group.find_center())

        


        def find_generator(group):
            for e1 in group.get_elements():
                for e2 in group.get_elements():
                    for e3 in group.get_elements():
                        gen = set({e1,e2,e3})
                        if group.get_identity() not in gen and group.check_generator(gen):
                            print(gen)
                            return gen

        pairs, elements = make_ordered_pairs("mystery_group_big.csv")
        group = Group(elements,pairs,"M30",False)
        #e = 'a'
        #for element in group.get_elements():
        #    if group.find_cyclic_group(element).order > group.find_cyclic_group(e).order:
        #        e = element
        #group = group.find_cyclic_group(e)
        #print(group)
        gen = find_generator(group)  
        #print(group.check_generator(gen))
        #print(type(gen))
        graph,degrees = group.make_color_graph(gen)
        #print(degrees)
        draw_color_graph.draw_graph(group,gen,graph,350,-200)
        #try this one! {'p', 'g', 'l', 'a','v','c','x','p','l','z','d','h'}
        for e in elements:
            group.find_cyclic_group(e)
        
        group.create_subgroup_tree()
        #group.check_isomorophic(group)
        print("done")
        #print(group.get_subgroups())
        #print(group.get_subgroups()[2].get_subgroups()[3].get_subgroups()[0].get_subgroups()[0].get_subgroups()[0])
        print(('a',set({'a', (1)})))
    check_stuff()