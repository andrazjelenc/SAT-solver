class DPLLSolver:
    def __init__(self, clauses_dict, vars_dict):
        self.clauses_dict = clauses_dict
        self.vars_dict = vars_dict

    def solve(self):
        raise NotImplementedError