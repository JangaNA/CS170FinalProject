import argparse
import random
import threading
from multiprocessing.dummy import Pool as ThreadPool 
import itertools

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
    def findsubsets(S,m):
        return set(itertools.permutations(S, m))
    lst=[]
    for i in findsubsets(wizards,3):
        lst.append(list(i))
    #returns false if a condition is not met
    def checkCons(constraints,output):
        for cond in constraints:
            if cond[0] in output and cond[1] in output and cond[2] in output: 
                if inRange(cond,output):
                    return False
        return True
    lst=[x for x in lst if checkCons(constraints,x)]
    # lst=[x for x in lst if checkCons(constraints,x)]
    print(len(lst))
    counter=3
    newlst=[]
    while counter<=4:
        for elem in lst:
            for w in wizards:
                if w not in elem and checkCons(constraints, elem+[w]):
                    newlst.append(elem+[w])
        lst=newlst
        counter+=1
    print(numSat(lst[0]))
    return lst[0]

    # finds best ordering in a random sample
    
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