% Facts
bird(parrot).
bird(pigeon).
bird(eagle).
bird(ostrich).
bird(penguin).
bird(sparrow).

% Rules
can_fly(X) :-
    bird(X),
    X \= ostrich,
    X \= penguin.

cannot_fly(X) :-
    bird(X),
    (X = ostrich; X = penguin).