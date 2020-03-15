from copy import deepcopy
import time


class DPLLSolver:
    def __init__(self, clauses_dict, vars_dict):
        self.clauses_dict = clauses_dict
        self.vars_dict = vars_dict

    def solve(self):
        start_time = time.time()
        status, solution = DPLLSolver._get_solution(self.clauses_dict, self.vars_dict)
        stop_time = time.time()
        return status, solution, stop_time - start_time

    @staticmethod
    def _get_solution(clauses_dict, vars_dict):
        key = DPLLSolver._get_fixed_key(clauses_dict, vars_dict)
        copy = False
        if key is not None:
            keys = [key]
        else:
            keys = DPLLSolver._sort_vars(vars_dict)
            copy = True

        for key in keys:
            if copy == True:
                clauses_dict_new = deepcopy(clauses_dict)
                vars_dict_new = deepcopy(vars_dict)
            else:
                clauses_dict_new = clauses_dict
                vars_dict_new = vars_dict

            clauses_dict_new, vars_dict_new = DPLLSolver._remove_var(key, clauses_dict_new, vars_dict_new)

            status = DPLLSolver._get_status(clauses_dict_new)

            if status is None:
                res_status, res_solution = DPLLSolver._get_solution(clauses_dict_new, vars_dict_new)
                if res_status == True:
                    return True, res_solution + [key]
            elif status == True:
                return True, [key]

        return False, None

    @staticmethod
    def _get_fixed_key(clauses_dict, vars_dict):
        # Find all variables that are alone in some clause
        for i in clauses_dict:
            if len(clauses_dict[i]) == 1:
                (el,) = clauses_dict[i]
                return el

        # Find all variables that there is not -var in any clause
        for var in vars_dict:
            if len(vars_dict[var]) > 0 and len(vars_dict[-var]) == 0:
                return var

        return None


    @staticmethod
    def _remove_var(var, clauses_dict, vars_dict):
        # remove clauses that contains var
        for clause in list(vars_dict[var]):
            # Remove this clause from list of clauses for every var
            for other_var in clauses_dict[clause]:
                vars_dict[other_var].remove(clause)

            del clauses_dict[clause]

        # from clauses that contains -var remove it
        for clause in vars_dict[-var]:
            clauses_dict[clause].remove(-var)

        # from var_dict_new remove var and -var
        del vars_dict[var]
        del vars_dict[-var]

        return clauses_dict, vars_dict

    @staticmethod
    def _sort_vars(vars_dict):
        return sorted((var for var in vars_dict if len(vars_dict[var]) > 0), key=lambda k: len(vars_dict[k]), reverse=True)

    @staticmethod
    def _get_status(clauses_dict):
        if not bool(clauses_dict):
            return True # solved

        for i in clauses_dict:
            if len(clauses_dict[i]) == 0:
                return False # cannot be solved

        return None #We are not yet finished