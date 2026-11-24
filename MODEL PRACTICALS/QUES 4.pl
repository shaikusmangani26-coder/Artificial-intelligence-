% Employee facts
employee(john).
employee(alice).
employee(bob).
employee(david).
employee(ravi).

% Department facts
department(it).
department(hr).
department(finance).

% Department relationships
works_in(john, it).
works_in(alice, it).
works_in(bob, hr).
works_in(david, finance).
works_in(ravi, hr).

% Manager facts
manager(john).
manager(bob).

% Reporting relationships
reports_to(alice, john).
reports_to(ravi, bob).
reports_to(david, bob).

% Rules
find_manager(E, M) :-
    reports_to(E, M).

find_department(E, D) :-
    works_in(E, D).

employees_under(M, E) :-
    reports_to(E, M).