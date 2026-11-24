% Symptoms
symptom(engine_not_starting).
symptom(battery_low).
symptom(no_fuel).
symptom(flat_tyre).

% Fault diagnosis rules
fault(battery_problem) :-
    symptom(engine_not_starting),
    symptom(battery_low).

fault(fuel_problem) :-
    symptom(engine_not_starting),
    symptom(no_fuel).

fault(tyre_problem) :-
    symptom(flat_tyre).

% Display diagnosis
diagnose :-
    fault(X),
    write('Possible Fault: '), write(X), nl,
    fail.
diagnose.