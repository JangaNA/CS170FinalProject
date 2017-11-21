import argparse
#my own imports
import time
import itertools
import random

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
    random.shuffle(wizards)
    assignment = wizards
    scores = {}
    loop_counter = 0
    prev_max = 0
    while not numSat(constraints, assignment,0) == len(constraints):
        print("numSat", numSat(constraints, assignment, 0))
        loop_counter += 1
        if loop_counter % 10 == 0:
            print("loops",loop_counter)
            print("time taken", time.time()-start)
	scores = {}
	#unsatisfied = unsatisfiedConstraints(constraints, assignment)
	#wizUnsat = set()
	#for constraint in unsatisfied:
	#    wizUnsat.add(constraint[0])
	#print("num wixUnsat", len(wizUnsat))
	max_sat = 0
        for i in range(len(wizards)):
            for j in range(len(wizards)):
                if (i != j) and ((j,i) not in scores):
                    temp = assignment[i]
                    assignment[i] = assignment[j]
                    assignment[j] = temp
                    score = numSat(constraints,assignment,max_sat)
                    scores[(i,j)] = score
		    temp = assignment[i]
                    assignment[i] = assignment[j]
                    assignment[j] = temp
		    if scores[(i,j)] > max_sat:
			max_sat = score
        max_score_swap = max(scores, key=scores.get)
        if max_score_swap == prev_max:
            print("RESHUFFLING")
            random.shuffle(assignment)
        prev_max = max_score_swap
	prev_score = scores[max_score_swap]
        temp = assignment[max_score_swap[0]]
        assignment[max_score_swap[0]] = assignment[max_score_swap[1]]
        assignment[max_score_swap[1]] = temp
    print("Solved BITCH! numSat:", numSat(constraints, assignment))
    return assignment

def unsatisfiedConstraints(constraints, output):
    unsatisfied = []
    for cond in constraints:
	if inRange(cond,output):
	    unsatisfied.append(cond)
    return unsatisfied

def numSat(constraints,output,currMax):
    satisfied=0
    remaining=len(constraints)
    for cond in constraints:
        if satisfied + remaining < currMax:
	    return 0
        if not inRange(cond,output):
            satisfied+=1
	remaining += 1
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
