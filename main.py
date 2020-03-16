from file_parser import Parser
from DPLLSolver import DPLLSolver


def main():
    p = Parser('examples/sudoku_hard.txt')

    # [{1:True, 5:False},...,{12:True, 5:True, 11:False}]
    clauses_list = p.parse()

    s = DPLLSolver(clauses_list)
    status, solution, timing = s.solve()

    print(status)
    print(solution)
    print(timing)


if __name__ == '__main__':
    main()