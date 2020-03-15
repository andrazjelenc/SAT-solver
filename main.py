from file_parser import Parser
from DPLLSolver import DPLLSolver


def construct_dict_of_vars(num_of_variables, clauses_dict):
    result = dict()

    for var in range(1, num_of_variables + 1):
        lst = set()
        lst_neg = set()
        for i in clauses_dict:
            if var in clauses_dict[i]:
                lst.add(i)
            if -var in clauses_dict[i]:
                lst_neg.add(i)
        result[var] = lst
        result[-var] = lst_neg

    return result


def main():
    p = Parser('examples/sudoku_hard.txt')

    # variables from 1 to num_of_variables inclusive
    # int, int, list of (list of ints)
    num_of_variables, num_of_clauses, clauses_list = p.parse()

    # construct dict of clauses
    # clause num -> clause set of variables
    clauses_dict = dict(zip(range(1, num_of_clauses+1), clauses_list))

    # construct dict of vars
    # var num -> set of clauses that contains this var
    # - var num -> set of clauses that contins neg of this var
    vars_dict = construct_dict_of_vars(num_of_variables, clauses_dict)

    s = DPLLSolver(clauses_dict, vars_dict)
    status, result, time = s.solve()

    print(status)
    print(result)
    print("Solving took {} seconds".format(round(time,3)))


if __name__ == '__main__':
    main()