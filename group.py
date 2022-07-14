class Group:

    def __init__(self,elements,pairs,name = None,debug_mode = True):
        """takes two input, elements and pairs
        elements-- an array of all elements in the group
        pairs-- a dictionary of 2-tuples to elements"""
        self.elements = elements
        self.order = len(elements)
        self.pairs = pairs
        self.debug_mode = debug_mode
        self.subgroups = [] #normally this will be a set
        self.subgroups_set = set()
        self.elements_set = set() #sometimes its useful to have elements as a set rather than an array
        self.name = name
        self.names = [name]
        self.inverses = {}
        self.center = []
        self.normal_subgroups = []
        self.internal_direct_product_reps = set() # a set of k-tuples, if (A,B,C) is an element, then G = A X B X C
        self.check_abelian()
        for e in self.elements:
            
            self.elements_set.add(e)
        self.subgroups.append(self)
        idint, self.identity = self.check_identity()

        #self.is_group = self.check_group()

        #if not self.is_group:
        #    print("not a group")

    def __repr__(self):
        if self.name == None:
            return str(self.elements_set)
        else:
            title = self.name
            for i in range(1,len(self.names)):
                title = title + "=" + self.names[i]
            return title

########## basic group stuff

    def check_identity(self):
        """output:
        identity_prop -- a bool
        identity -- a char"""

        for e1 in self.elements: #checks if each element is the identity, stops if identity prop is satisfied
            identity = True
            for e2 in self.elements:
                if not (self.pairs[(e1,e2)] == e2 and self.pairs[(e2,e1)] == e2):
                    identity = False
            if identity:
                self.identity = e1
                return True, e1
                

        return False, None

    def check_inverse(self,identity = None):
        """checks to see if eache"""
        if identity == None:
            identity = self.check_identity()[1]
        inverses = True
        for e1 in self.elements:
            has_inverse = False
            for e2 in self.elements:
                if self.pairs[(e1,e2)] == 'z':
                    has_inverse = True
                    self.inverses[e1] = e2
            if not has_inverse:
                inverses = False
        return inverses

    def check_isomorophic(self, group):
        """checks to see if the two groups are isomorophic
        THIS ONE DOESN"T WORK!"""
        domain = self.get_elements_set()
        codomain = group.get_elements_set()
        if len(domain) != len(codomain):
            return False
        possible_orders = []
        for i in range(1,len(domain)):
            if len(domain) % i == 0:
                possible_orders.append(i)

        orders_domain = {}
        orders_codomain = {}
        for e in domain:
            orders_domain[len()]
        #orders_to_elements = find_all_orders()

    def find_normalizer(self,subgroup):
        """finds the set of elements in the group such that xHx^-1 = H
        takes one argument, a Group
        returns Group, adds to subgroups"""
        norm = set()
        norm_list = []
        
        for x in self.get_elements:
            conj = set()
            pairs = self.get_pairs()
            els = subgroup.get_elements_set()
            for h in els:
                conj_el = pairs[(pairs[(x,h)],self.get_inverse(x))]
                conj.add(conj_el)
            if conj == els:
                norm.add(x)
        
        for x in norm:
            if x not in norm_list:
                norm_list.append(x)

        return Group(norm_list,self.pairs,"N({})".format(subgroup))

    def check_closed(self):
        """checks that the closrue property is satisfied
        returns: boolean"""
        closed = True
        pair_tuples = self.pairs.keys()
        for pair in pair_tuples:
            if self.pairs[pair] not in self.elements:
                closed = False
        return closed

    def check_associative(self):
        return True

    def check_group(self):
        """checks to see if this is a group"""
        closed = self.check_closed()
        inverse = self.check_inverse()
        identity, self.identity = self.check_identity()
        associative = self.check_associative()
        group = closed and inverse and identity and associative
        return group


#### generators and color graphs

    def check_generator(self, gen):
        """takes one argument, a set,
        returns a boolean"""
        els = set()

        els = gen.copy()
        for e in gen:
            els |= self.find_cyclic_group(e).get_elements_set()
        gen = els
        
        def check_reached(element):
            for e1 in gen:
                for e2 in gen:
                    if self.get_pairs()[(e1,e2)] == element:
                        return True
            return False

        for e in self.get_elements():
            if not check_reached(e):
                return False
        return True

    def make_color_graph(self,gen):
        """takes one argument, returns set of 2-tuples, as well as a dictionary whose keys 
        are characters/elements that correspond to a number, the degree of the vertex corresponding to that element"""
        if not self.check_generator(gen):
            print("error, set not a generator")
            return None
        edges = set()
        degrees = {}
        for e1 in self.get_elements():
            for e2 in gen:
                e3 = self.get_pairs()[(e1,e2)]
                edges.add((e2,e3))
        for e in self.get_elements():
            deg = 0
            for edge in edges:
                if edge[1] == e:
                    deg += 1
            degrees[e] = deg
        return edges, degrees

#############    cosets and conjugates
        
    def find_left_coset(self, element,subgroup):
        """takes two arguments, a character and a group,
        returns a set"""
        left_coset = set()
        for e in subgroup.get_elements():
            left_coset.add(self.pairs[(element,e)])
        return left_coset

    def check_normal_subgroup(self, subgroup):
        """checks to see if the subgroup is normal or not"""
        for e in self.get_elements():
            if not self.find_right_coset(e, subgroup) == self.find_left_coset(e,subgroup): #using an equivalent condition if normal subgorups
                return False
        return True

    def find_normal_subgroups(self):
        """sorts through all known subgorups and checks if they are normal
        If they are, it adds them to the list of normal subgroups"""
        for subgroup in self.get_subgroups():
            if self.check_normal_subgroup(subgroup):
                self.normal_subgroups.append(subgroup)
            
    def make_set_product(self, sets):
        """takes two sets, finds the set product according the the groups pairs.
        Returns a set"""
        prod = set()
        if len(sets) == 1:
            return sets[0]
        else:
            for i in range(len(sets)):
                pass# working here

        
    def check_internal_direct_product(self,subgroups):
        """checks to see if the sets listed form an internal direct product
        Takes a list of subgroups"""
        prod = set()
        prod = prod.union(prod,self.make_set_product)

    def find_right_coset(self,element, subgroup):
        """takes one argument, a character,
        returns a set"""
        right_coset = set()
        for e in subgroup.get_elements():
            right_coset.add(self.pairs[(e,element)])
        return right_coset

    def find_conjugate(self,element,subgroup):
        """takes three arguments:
        element- the element under which the subgroup is being conjugated
        subgroup- the subgroup being conjugated
        
        returns a set and a group"""
        conjugate = set()

        element_inverse = self.inverses[element]

        for e in subgroup.get_elements():
            conjugate.add(self.get_pairs()[(self.get_pairs()[(element,e)],element_inverse)])

        elements_array = []
        conjugate_pairs = {}

        for e in conjugate:
            elements_array.append(e)
            conjugate_pairs[e] = self.get_pairs()[e]

        conjugate_group = Group(elements_array,conjugate_pairs,"{a}{H}{i}".format(a = element,H = subgroup,b = element_inverse))
        return conjugate,conjugate_group

########################## geters and seters
        
    def get_inverses(self):
        """returns the dictionary of element inverses"""
        return self.inverses

    def get_elements(self):
        return self.elements

    def get_elements_set(self):
        return self.elements_set

    def get_pairs(self):
        return self.pairs

    def get_subgroups(self):
        return self.subgroups

    def get_inverse(self,element):
        return self.inverses[element]

    def get_identity(self):
        return self.identity

    def get_name(self):
        return self.name

    def get_abelian(self):
        return self.abelian

##########################

  

    def find_zenter(self, a):
        
        """this function finds the centeralizer of a given element"""
        zenter = []
        for b in self.elements:
            if self.pairs[(a,b)] == self.pairs[(b,a)]:
                zenter.append(b)

        zenter_pairs = {}
        for e1 in zenter:
            for e2 in zenter:
                zenter_pairs[(e1,e2)] = self.pairs[(e1,e2)]
        zenter_group = Group(zenter, zenter_pairs,"C({})".format(a))
        self.add_subgroup(zenter_group)
        return zenter

    def find_center(self):
        center = []

        for b in self.elements:
            if self.find_zenter(b) == self.elements:
                center.append(b)
        self.center = center
        center_pairs = {}
        for e1 in center:
            for e2 in center:
                center_pairs[(e1,e2)] = self.pairs[(e1,e2)]
        center_group =Group(center,center_pairs,"Z({})".format(self.name))
        self.add_subgroup(center_group)

        return center        

    def find_cyclic_group(self, a):
        """takes a string, returns a set"""
        cycle = set()
        cycle_array = []
        cycle_pairs = {}
        g = a
        for i in range(self.order):
            if g in cycle:
                break
            cycle.add(g)
            g = self.pairs[(g,a)]
        for e1 in cycle:
            cycle_array.append(e1)
            for e2 in cycle:
                cycle_pairs[(e1,e2)] = self.pairs[(e1,e2)]

        cyclic_group = CyclicGroup(cycle_array,cycle_pairs,[a],"<{}>".format(a),True)
        self.add_subgroup(cyclic_group)

        return cyclic_group


    def find_cyclic_subgroups(self):
        cyclic_groups = []
        for element in self.elements:
            cyclic_groups.append(self.find_cyclic_group(element))
        for g in cyclic_groups:
            if g not in self.subgroups_set:
                
                self.add_subgroup(g)

        return cyclic_groups

    def create_subgroup_lattice(self):
        """creates the subgroup lattice,
        returns a list of ordered pairs containing groups"""
        

    def already_subgroup(self,subgroup):
        """checks to see whether a subgroup is already listed. If so, it doesn't add it to the list, but does add the NAME of that subgroup to the list, i.e. <a> = <l>"""
        for sub in self.subgroups:

            if subgroup.get_elements_set() == sub.get_elements_set():

                if sub.get_name() not in subgroup.names:
                    subgroup.names.append(sub.get_name())

                if subgroup.get_name() not in sub.names:
                    sub.names.append(subgroup.get_name())

                return True
            
                
        return False

    def add_subgroup(self,subgroup):
        """takes one argument: a Group
        returns a boolean, strangely enough
        The idea here is that it checks to see if a group is a subgroup, 
        and then adds it to the list of known subgroups"""
        if self.check_subgroup(subgroup):
            inthere= self.already_subgroup(subgroup)
            if not inthere:
                self.subgroups.append(subgroup)
            
            return True
        else:
            return False

    def list_known_subgroups(self):
        """prints the known subgroups on the console"""
        for sugbroup in self.get_subgroups():
            print(sugbroup)
        
    def create_subgroup_tree(self):
        """Recursively creates the subgroup node tree"""
        for subgroup in self.subgroups:
            if subgroup != self: #otherwise we'd have an infinite loop
                for sub in self.subgroups:
                    subgroup.add_subgroup(sub)
                    subgroup.create_subgroup_tree()
    
    def check_subgroup(self,subgroup):
        """takes one argument: a group
        returns a boolean,
        uses the finite subgroup test"""
        return subgroup.get_elements_set().issubset(self.get_elements_set()) and subgroup.check_closed()
    
    def check_abelian(self):
        """checks to see if the group is abelian"""
        for e1 in self.get_elements():
            for e2 in self.get_elements():
                if self.get_pairs()[(e1,e2)] != self.get_pairs()[(e2,e1)]:
                    self.abelian = False
                    return False
        self.abelian = True
        return True
        

class CyclicGroup(Group):
    def __init__(self,elements,pairs,generators,name = None,debug_mode = False):
        Group.__init__(self, elements,pairs,name,debug_mode)
        self.generator = set()

def test():

    import read_group
    import draw_color_graph
    print("""

    Since I've actually started to run low on time, as things have gotten quite busy
    I haven't been able to get the fancy interface I had started to work. Just to give a general 
    run-through of what my program can do, I've decided to create a quick test
    function that demonsrtrates the main things my program currently does.
    Feel free to play the console.py file, but keep in mind that it's currently nowhere near where I'd hoped it would be

    """)
    print("""
    
    first, the program takes a Cayley table in the form of a csv file. 
    This is what the program is currently doing.
    The information gets processed as a Group, which is a class I've made that does some of the things groups do
    
    """)
    pairs,elements = read_group.make_ordered_pairs("group_51_table.csv")
    group = Group(elements, pairs, "G51", False)
    if group.check_group():
        print("the group passed all the requirements to be a group!")
        print("It has order "  + str(len(group.get_elements_set())))
    if group.get_abelian():
        print("The group is abelian!")
    else:
        print("The group is not abelian!")

    done = False
    input("Enter any key to see how you can see where elements operate to")
    while not done:
        if input("press E to see all the elements, or any other key to skip: ") == "E":
            print(group.get_elements_set())
        first_element = input("enter the first element: ")
        second_element = input("enter the second element: ")
        if first_element in group.get_elements() and second_element in group.get_elements():
            print("{A} * {B} = {C}".format(A = first_element, B = second_element, C = group.get_pairs()[(first_element,second_element)]))
            if input("press Q to go on to the next thing, or press any other key to try another element combo: ") == "Q":
                done = True
        else:
            print("not an element, try something else!")
    print("You can also find a whole bunch of other stuff, for example...")
    print("The identity is {I}".format(I = group.get_identity()))
    print("The center of the group is {C}".format(C = group.find_center()))
    print("The cyclic and centers for each element are: ")
    for element in group.get_elements():
        print("<{a}> = ".format(a = element) + str(group.find_cyclic_group(element).get_elements_set()))
        centralizer_set = set()
        for e in group.find_zenter(element):
            centralizer_set.add(e)
        print("C({a}) = ".format(a = element) + str(centralizer_set))
        input("press any key to see for the next element: ")
    input("""
    So far, here are the known subgroups (press any key to continue): 
    """)
    group.list_known_subgroups()
    input("""
    You can also generate a cayley graph for any group. Note that the subgroups are themselves instantiations of the Group class.
    After doing section leading, I now realize that many problems could have been resolved by using factory methods, but it's 
    probably too late now

    Press any key to continue: 
    """)

    print("Here is the Cayley graph for the group, with the generating set being the set containing p,t,x,f,g")
    cyclic_subgroup_a = None
    for subgroup in group.get_subgroups():
        if "<a>" in subgroup.get_name():
            cyclic_subgroup_a = subgroup
            break
    gen = set({'p','t','x','f','g'})
    graph,naw = group.make_color_graph(gen)
    print(graph)
    print(type(group))
    draw_color_graph.draw_graph(group,gen,graph,200,-100)

if __name__ == "__main__":
    test()
