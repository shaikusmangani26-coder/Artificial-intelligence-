% Planets Database

planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).
planet(saturn, 6).
planet(uranus, 7).
planet(neptune, 8).

% Query to display all planets
display_planets :-
    planet(Name, Number),
    write(Name),
    write(' - Position: '),
    write(Number),
    nl,
    fail.
display_planets.

% Query to find a planet by its name
find_planet(Name) :-
    planet(Name, Number),
    write('Planet: '),
    write(Name),
    write(', Position: '),
    write(Number),
    nl.