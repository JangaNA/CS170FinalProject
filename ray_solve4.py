import argparse
#my own imports
import time
import itertools
import random
import numpy as np

"""
======================================================================
  Complete the following function.
======================================================================
"""

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    print("starting time")
    start = time.time()
    print("hello")
    end = time.time()
    print("time taken",end - start)
    random.shuffle(wizards)
    assignment = wizards
    loop_counter = 0
    temperature = 10.0
    while not numSat(constraints, assignment) == len(constraints):
        loop_counter += 1
        if loop_counter % 500 == 0:
            print("numSat", numSat(constraints, assignment))
            print("loops",loop_counter)
            print("time taken", time.time()-start)
        a = random.sample([i for i in range(len(wizards))], 1)
        b = random.sample([i for i in range(len(wizards))], 1)
        new_assignment = swap(assignment, a[0], b[0])
        delta = numSat(constraints, assignment) - numSat(constraints, new_assignment)
        if delta < 0:
            print("delta negative")
            assignment = new_assignment
        else: 
            # print("sample greater than expo")
            sample = random.uniform(0.0,1.0)
            expo = np.exp(-1*float(delta) / temperature)
            if sample < expo:
                # print("sample less than expo")
                assignment = new_assignment
        temperature -= 0.2

    print("Solved BITCH! numSat:", numSat(constraints, assignment))
    return assignment

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    return array

def numSat(constraints,output):
    satisfied=0
    for cond in constraints:
         if not inRange(cond,output):
          satisfied+=1
    return satisfied
#returns true if 3rd element between first two
def inRange(cond,output):
    first=output.index(cond[0])
    second=output.index(cond[1])
    subject=output.index(cond[2])
    if first<second:
     if subject in range(first,second):
         return True
    if second<first:
     if subject in range(second,first):
         return True
    return False
def satisfies_constraints(ordering, constraints):
    for constraint in constraints:
        first, second, third = ordering[constraint[0]], ordering[constraint[1]], ordering[constraint[2]]
        if first == -1 or second == -1 or third == -1:
            return True
        else:
            return not ((first < second and second < third) or (first > second and second > third))

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)
                
    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)
