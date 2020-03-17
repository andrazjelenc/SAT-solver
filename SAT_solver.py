import argparse

from file_parser import Parser
from DPLLSolver import DPLLSolver


def get_args():
    args_parser = argparse.ArgumentParser(description='Solve SAT problem.')
    args_parser.add_argument('infile', help='Input file name with CNF formula in Dimacs format.')
    args_parser.add_argument('outfile', default="", nargs='?', help='Write solution to provided output file (optional).')
    return args_parser.parse_args()


def report_solution(solution, output_filename, message=""):
    if output_filename:
        with open(output_filename, 'w+') as f:
            f.write(solution)
    else:
        print(solution)
        if message:
            print(message)


def main():
    args = get_args()
    p = Parser(args.infile)

    # [{1:True, 5:False},...,{12:True, 5:True, 11:False}]
    clauses_list = p.parse()

    s = DPLLSolver(clauses_list)
    status, solution, timing = s.solve()

    if status:
        solution_string = " ".join(str(key) if value else str(-key)
                                   for key, value in solution.items())
        report_solution(solution_string, args.outfile)
    else:
        report_solution("0", args.outfile, message="Satisfying valuation not found.")

    # print(status)
    # print(solution)
    # print(timing)


if __name__ == '__main__':
    main()
