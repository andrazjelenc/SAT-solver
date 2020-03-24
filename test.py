from file_parser import Parser
from DPLLSolver import DPLLSolver


def check_solutions(sol1, sol2):
    keys1 = set(sol1)
    keys2 = set(sol2)

    len1 = len(keys1)
    len2 = len(keys2)
    len_intersect = 0
    for key in keys1.intersection(keys2):
        len_intersect += 1
        if sol1[key] != sol2[key]:
            print('Error: key {} has the wrong value. Our solution: {} - legit: {}'.format(key, sol1[key], sol2[key]))
            return False

    # print("Size of our solution is {}, size of legit solution is {}. All okey in intersection, where is {} keys".format(len1, len2, len_intersect))
    return True


# sudoku hard
p = Parser('examples/sudoku_hard.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/sudoku_hard_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"Sudoku hard:\t{timing:.4f}s\t{result}")

# sudoku eazy
p = Parser('examples/sudoku_eazy.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/sudoku_eazy_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"Sudoku easy:\t{timing:.4f}s\t{result}")


# sudoku mini
p = Parser('examples/sudoku_mini.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/sudoku_mini_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"Sudoku mini:\t{timing:.4f}s\t{result}")


# sudoku 16x16
p = Parser('examples/sudoku_16x16.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/sudoku_16x16_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"Sudoku 16x16:\t{timing:.4f}s\t{result}")


# sudoku 124
p = Parser('examples/sudoku_124.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/sudoku_124_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"Sudoku 124:\t{timing:.4f}s\t{result}")


# sudoku 150
p = Parser('examples/sudoku_150.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/sudoku_150_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"Sudoku 150:\t{timing:.4f}s\t{result}")


# sudoku extra hard
p = Parser('examples/sudoku_extra.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/sudoku_extra_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"Sudoku extra:\t{timing:.4f}s\t{result}")

# 8_queens
p = Parser('examples/8_queens.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/8_queens_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"8 queens:\t{timing:.4f}s\t{result}")


# 3 coloring
p = Parser('examples/3_coloring.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/3_coloring_solution.txt')
legit_solution = p.parse_solution()

result = solution == None
print(f"3 coloring:\t{timing:.4f}s\t{result}")


# 4 coloring
p = Parser('examples/4_coloring.txt')
clauses_list = p.parse()
s = DPLLSolver(clauses_list)
status, solution, timing = s.solve()
p = Parser('examples/4_coloring_solution.txt')
legit_solution = p.parse_solution()

result = check_solutions(solution, legit_solution)
print(f"4 coloring:\t{timing:.4f}s\t{result}")
