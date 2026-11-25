from copy import deepcopy

class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def solve(self):
        return self.backtrack({})

    def backtrack(self, assignments):
        if len(assignments) == len(self.variables):
            return assignments

        var = self.select_unassigned_variable(assignments)

        for value in self.domains[var]:
            new_assignments = deepcopy(assignments)
            new_assignments[var] = value

            if self.is_consistent(new_assignments):
                result = self.backtrack(new_assignments)

                if result is not None:
                    return result

        return None

    def select_unassigned_variable(self, assignments):
        for var in self.variables:
            if var not in assignments:
                return var

    def is_consistent(self, assignments):
        for a, b in self.constraints:
            if a in assignments and b in assignments:
                if assignments[a] == assignments[b]:
                    return False
        return True


def map_coloring():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

    domains = {
        var: ['r', 'g', 'b'] for var in variables
    }

    constraints = [
        ('WA', 'NT'),
        ('WA', 'SA'),
        ('NT', 'SA'),
        ('NT', 'Q'),
        ('SA', 'Q'),
        ('SA', 'NSW'),
        ('SA', 'V'),
        ('Q', 'NSW'),
        ('NSW', 'V')
    ]

    csp = CSP(variables, domains, constraints)
    result = csp.solve()

    if result is not None:
        print(result)
    else:
        print("No solution found")


map_coloring()