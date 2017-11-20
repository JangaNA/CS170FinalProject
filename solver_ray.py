import argparse
#my own imports
import time
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
    print("starting time")
    start = time.time()
    print("hello")
    end = time.time()
    print("time taken",end - start)

    not_assigned = set(wizards)
    curr_spot_assigning = 0
    curr_assignment = {}
    for wizard in wizards:
        curr_assignment[wizard] = -1

    def helper(ordering, curr_index):
        if curr_index == len(wizards) - 1:
            return ordering
        for wizard in not_assigned:
            ordering[wizard] = curr_index
            if satisfies_constraints(ordering, constraints):
                result = helper(ordering, curr_index + 1)
            else:
                continue
            if len(result) == len(wizards):
                return result
        return {}

    result = helper(curr_assignment, 0)
    if len(result) == 0:
        print("No Ordering Possible")
        return None
    else:
        result_sort = sorted(result, key=lambda k: d[k][0])
        return [elem[0] for elem in result_sort]

def satisfies_constraints(ordering, constraints):
    for constraint in constraints:
        first, second, third = ordering[costraint[0]], ordering[constraint[1]], ordering[constraint[2]]
        if first == -1 or second == -1 or third = -1:
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