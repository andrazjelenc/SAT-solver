from file_parser import Parser
from DPLLSolver import DPLLSolver


def check_solutions(sol1, sol2):
    keys1 = set(sol1)
    keys2 = set(sol2)

    len_intersect = 0
    for key in keys1.intersection(keys2):
        len_intersect += 1
        if sol1[key] != sol2[key]:
            print('Error: key {} has the wrong value. Our solution: {} - legit: {}'.format(key, sol1[key], sol2[key]))
            return False

    # print("Size of our solution is {}, size of legit solution is {}. All okey in intersection, where is {} keys".format(len1, len2, len_intersect))
    return True


# sudoku 16x16
p = Parser('example/sudoku_16x16_hard.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('example/sudoku_16x16_hard_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"Sudoku :\t{timing:.4f}s\t{result}")
