import time


class DPLLSolver:
    def __init__(self, clauses_list):
        self.clauses_list = clauses_list

    def solve(self):
        start_time = time.time()
        self.clauses_list.sort(key=len, reverse=True)
        status, solution = DPLLSolver._get_solution(self.clauses_list, dict())
        stop_time = time.time()
        return status, solution, stop_time - start_time

    @staticmethod
    def _get_solution(clauses_list, pre_fixed_org):
        pre_fixed = dict(pre_fixed_org)
        while True:
            #dict of keys that can be fixed
            keys = DPLLSolver._get_fixed_keys(clauses_list)

            if keys == False:
                return False, None

            if len(keys) == 0:
                break

            pre_fixed.update(keys)
            # simplify clauses according fixed keys
            clauses_list = DPLLSolver._remove_vars(keys, clauses_list)

        status = DPLLSolver._get_status(clauses_list)
        if status == True:
            return True, pre_fixed
        elif status == False:
            return False, None

        # Recursion
        key = next(iter(clauses_list[0])) # get first variable

        #Suppose key is True
        clauses_list.append({key: True})
        status, solution = DPLLSolver._get_solution(clauses_list, pre_fixed)
        if status == True:
            return True, solution

        #Suppose key is False
        del clauses_list[-1]
        clauses_list.append({key: False})
        return DPLLSolver._get_solution(clauses_list, pre_fixed)


    @staticmethod
    def _get_fixed_keys(clauses_list):
        # Get keys that are alone in clause and there fore must be fixed
        single_keys = dict()
        for clause in clauses_list:
            if len(clause) > 1:
                continue
            for key in clause:
                value = clause[key]
                if key not in single_keys:
                    single_keys[key] = value
                elif value != single_keys[key]:
                    return False

        pure_keys = dict()
        for clause in clauses_list:
            for key in clause:
                if key not in single_keys:
                    value = clause[key]
                    if key not in pure_keys:
                        pure_keys[key] = value
                    elif value != pure_keys[key]:
                        pure_keys[key] = None

        for key in list(pure_keys):
            if pure_keys[key] is None:
                del pure_keys[key]

        return {**single_keys, **pure_keys}

    @staticmethod
    def _remove_vars(vars, clauses_list):
        new_clauses_list = []
        for clause in clauses_list:
            new_clause = dict()
            for var in clause:
                if var not in vars:
                    #prepisi vrednost
                    new_clause[var] = clause[var]
                    continue

                vars_value = vars[var]
                local_value = clause[var]

                if vars_value == local_value:
                    #brisi clause
                    new_clause = None
                    break
                else:
                    continue
            if new_clause is not None:
                new_clauses_list.append(new_clause)

        return new_clauses_list

    @staticmethod
    def _get_status(clauses_list):
        if len(clauses_list) == 0:
            return True # Solved

        for clause in clauses_list:
            if len(clause) == 0:
                return False # Cannot be solved

        return None # We are not yet finished
