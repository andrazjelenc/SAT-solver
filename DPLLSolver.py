from copy import deepcopy


class DPLLSolver:
    def __init__(self, clauses_dict, vars_dict):
        self.clauses_dict = clauses_dict
        self.vars_dict = vars_dict

    def solve(self):
        return DPLLSolver._get_solution(self.clauses_dict, self.vars_dict)


    @staticmethod
    def _get_solution(clauses_dict, vars_dict):
        
        keys = DPLLSolver._sort_vars(vars_dict)
        for key in keys:
            clauses_dict_new, vars_dict_new = DPLLSolver._remove_var(key, clauses_dict, vars_dict)
            status = DPLLSolver._get_status(clauses_dict_new)

            if status is None:
                res_status, res_solution = DPLLSolver._get_solution(clauses_dict_new, vars_dict_new)
                if res_status == True:
                    return True, res_solution + [key]
            elif status == True:
                return True, [key]

        return False, None


    @staticmethod
    def _remove_var(var, clauses_dict, vars_dict):
        clauses_dict_new = deepcopy(clauses_dict)
        vars_dict_new = deepcopy(vars_dict)

        # remove clauses that contains var
        for clause in vars_dict[var]:
            # Remove this clause from list of clauses for every var
            for other_var in clauses_dict_new[clause]:
                vars_dict_new[other_var].remove(clause)

            del clauses_dict_new[clause]

        # from clauses that contains -var remove it
        for clause in vars_dict_new[-var]:
            clauses_dict_new[clause].remove(-var)

        # from var_dict_new remove var and -var
        del vars_dict_new[var]
        del vars_dict_new[-var]

        return clauses_dict_new, vars_dict_new

    @staticmethod
    def _sort_vars(vars_dict):
        return sorted(vars_dict, key=lambda k: len(vars_dict[k]), reverse=True)

    @staticmethod
    def _get_status(clauses_dict):
        if not clauses_dict:
            return True # solved

        for i in clauses_dict:
            if len(clauses_dict[i]) == 0:
                return False # cannot be solved

        return None #We are not yet finished