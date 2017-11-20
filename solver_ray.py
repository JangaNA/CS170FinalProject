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
	

    def count_calls(fn):
    	def _counting(*args, **kwargs):
            _counting.calls += 1
            return fn(*args, **kwargs)
        _counting.calls = 0
        return _counting

    not_assigned = set(wizards)
    curr_spot_assigning = 0
    curr_assignment = {}
    for wizard in wizards:
        curr_assignment[wizard] = -1
    
    @count_calls
    def helper(ordering, curr_index, remaining):
	if helper.calls % 1000 == 0:
	    print("number of timmes called", helper.calls)
	    print("time elapsed", time.time() - start)
	if curr_index == len(wizards) - 1:
            return ordering
        for wizard in remaining:
            ordering[wizard] = curr_index
	    if satisfies_constraints(ordering, constraints):    
		new_remaining = remaining.copy()
		new_remaining.remove(wizard)
	        result = helper(ordering.copy(), curr_index + 1, new_remaining)
		if len(result) == len(wizards):
                    return result
	    ordering[wizard] = -1
        return {}
    helper.num_calls = 0
    result = helper(curr_assignment, 0, not_assigned)
    print("am i high")
    if len(result) == 0:
        print("No Ordering Possible")
        return None
    else:
    	print("found an ordering")
    	num_cons = 0
    	for constraint in constraints:
    	    if satisfies_constraints(result, constraints):
    		num_cons += 1
    	print("number cons satisfied", num_cons)
        result_sort = sorted(result, key=result.get)
        print(numSat(constraints,result_sort))
        return result_sort
def numSat(constraints,output):
    satisfied=0
    for cond in constraints:
        first, second, third = cond[0], cond[1], cond[2]
	if cond[0] == -1 or cond[1] == -1 or cond[2] == -1:
	    satisfied+=1
	    continue	 
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
    num_sat = 0
    for constraint in constraints:
        first, second, third = ordering[constraint[0]], ordering[constraint[1]], ordering[constraint[2]]
        if first == -1 or second == -1 or third == -1:
            num_sat += 1
        else:
            if not ((first < third and third < second) or (third < first and second < third)):
		num_sat += 1
    return num_sat == len(constraints)

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
