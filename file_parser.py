class Parser:
    def __init__(self, filename):
        self.filename = filename

    def parse_solution(self):
        result = dict()
        with open(self.filename) as f:
            line = f.readlines()[0]
            line = line.strip()
            line_data = line.split(' ')
            for var in line_data:
                var = int(var)
                var_abs = abs(var)
                if var > 0:
                    result[var_abs] = True
                else:
                    result[var_abs] = False
        return result

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
                clause = dict()
                for val in line_data[:-1]:
                    val = int(val)
                    val_abs = abs(val)
                    if val > 0:
                        clause[val_abs] = True
                    else:
                        clause[val_abs] = False

                clauses_list.append(clause)

            if num_of_clauses is None or num_of_variables is None:
                raise ValueError('Given file is not in correct format.')

            return clauses_list
