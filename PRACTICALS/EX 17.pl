
% Database containing Name and Date of Birth (DOB)

person(rahul, '2004-05-12').
person(priya, '2005-08-20').
person(amit, '2003-11-15').
person(sneha, '2004-02-25').
person(arun, '2005-06-10').

% Rules to retrieve information
get_dob(Name, DOB) :-
    person(Name, DOB).

get_name(DOB, Name) :-
    person(Name, DOB).
