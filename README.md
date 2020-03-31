# SAT solver

SAT solver takes SAT problem defined in conjunctive normal form and attempts to find some satisfying valuation. If such valuation is found it is returned, otherwise solver returns a single value of 0.

## Running the solver
Solver can be ran as: `python SAT_solver.py <input filename> [output filename]`

SAT solver takes input file that contains CNF formula (in Dimacs format) of SAT problem to solve.
Solution can be printed to STDOUT (default) or written to file.

Example calls:
+ CNF formula is stored in file '*my_cnf.txt*':
`python SAT_solver.py my_cnf.txt`

+ CNF formula is stored in '*my_cnf.txt*', solution should be written to '*solution.txt*':
`python SAT_solver.py my_cnf.txt solution.txt`

## Optimization
At the beginning solver orders input clauses by number of literals in descending order.
Solver's branching is implemented so as to choose the first literal of the first clause, set it to True and recursively run the solving algorithm. If no satisfiable valuation is found it tries again, this time setting the chosen literal to False.
One optimization we tried was to choose the literal that occurs most often in current formula. The attempt turned out to be unsuccessful as the execution time of our test cases had doubled. We are aware that our test cases are small and the results could be different on larger cases. Still, we decided to abandon this idea due to uncertainty.
