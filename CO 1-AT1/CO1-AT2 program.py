class ExamScheduler:
    def __init__(self):
        self.variables = ['A', 'B', 'C', 'D', 'E']
        self.slots = ['Slot1', 'Slot2', 'Slot3']
        self.conflicts = {
            'A': ['B', 'C'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D', 'E'],
            'D': ['B', 'C', 'E'],
            'E': ['C', 'D']
        }
        
    def is_consistent(self, var, value, assignment):
        for neighbor in self.conflicts[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    # 1. Plain Backtracking Search
    def solve_plain_backtracking(self):
        self.plain_attempts = 0
        self.plain_backtracks = 0
        assignment = {}
        
        def backtrack():
            if len(assignment) == len(self.variables):
                return assignment
            
            unassigned = [v for v in self.variables if v not in assignment]
            var = unassigned[0]  # Static order
            
            for value in self.slots:
                self.plain_attempts += 1
                if self.is_consistent(var, value, assignment):
                    assignment[var] = value
                    result = backtrack()
                    if result is not None:
                        return result
                    del assignment[var]
                    self.plain_backtracks += 1
            return None

        solution = backtrack()
        return solution, self.plain_attempts, self.plain_backtracks

    # 2. Backtracking with Forward Checking
    def solve_forward_checking(self):
        self.fc_attempts = 0
        self.fc_backtracks = 0
        domains = {v: list(self.slots) for v in self.variables}
        assignment = {}

        def backtrack_fc(current_domains):
            if len(assignment) == len(self.variables):
                return assignment

            unassigned = [v for v in self.variables if v not in assignment]
            var = unassigned[0]  # Static order

            for value in list(current_domains[var]):
                self.fc_attempts += 1
                assignment[var] = value
                
                # Forward checking step
                new_domains = {v: list(current_domains[v]) for v in self.variables}
                new_domains[var] = [value]
                
                legal = True
                for neighbor in self.conflicts[var]:
                    if neighbor not in assignment:
                        if value in new_domains[neighbor]:
                            new_domains[neighbor].remove(value)
                        if len(new_domains[neighbor]) == 0:
                            legal = False
                            break
                
                if legal:
                    result = backtrack_fc(new_domains)
                    if result is not None:
                        return result
                
                del assignment[var]
                self.fc_backtracks += 1
                
            return None

        solution = backtrack_fc(domains)
        return solution, self.fc_attempts, self.fc_backtracks


# Run and Compare
scheduler = ExamScheduler()

sol_plain, att_plain, bt_plain = scheduler.solve_plain_backtracking()
sol_fc, att_fc, bt_fc = scheduler.solve_forward_checking()

print("=== PLAIN BACKTRACKING ===")
print("Final Schedule:", sol_plain)
print(f"Assignment Attempts: {att_plain}")
print(f"Backtracks: {bt_plain}\n")

print("=== FORWARD CHECKING ===")
print("Final Schedule:", sol_fc)
print(f"Assignment Attempts: {att_fc}")
print(f"Backtracks: {bt_fc}")
