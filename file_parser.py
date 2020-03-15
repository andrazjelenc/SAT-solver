class Parser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        num_of_variables = None
        num_of_clauses = None
        clauses_list = []

        with open(self.filename) as f:
            for line in f:
                line = line.strip()

                # skip empty lines and comment lines
                if len(line) == 0 or line.startswith('c'):
                    continue

                # header line
                # p cnf 64 453
                if line.startswith('p cnf'):
                    line_data = line.split(' ')
                    if len(line_data) != 4:
                        raise ValueError('Given file is not in correct format.')

                    num_of_variables = int(line_data[2])
                    num_of_clauses = int(line_data[3])
                    continue

                # clause line
                # 5 -1 4 0
                line_data = line.split(' ')
                if line_data[-1] != '0':
                    raise ValueError('Given file is not in correct format.')

                clauses_list.append([int(i) for i in line_data[:-1]])

            if num_of_clauses is None or num_of_variables is None:
                raise ValueError('Given file is not in correct format.')

            return num_of_variables, num_of_clauses, clauses_list


if __name__ == '__main__':
    try:
        p = Parser('examples/sudoku_mini.txt')
        num_of_variables, num_of_clauses, clauses_list = p.parse()
        print('Number of variables: {}'.format(num_of_variables))
        print('Number of clauses: {}'.format(num_of_clauses))
        for clause in clauses_list:
            print(clause)
    except:
        print("Something went wrong.")