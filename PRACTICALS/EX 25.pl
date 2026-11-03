% Disease and Diet Suggestions

diet(diabetes, 'Low sugar foods, vegetables, whole grains').
diet(obesity, 'Low calorie foods, fruits, vegetables').
diet(blood_pressure, 'Low salt foods, fruits, vegetables').
diet(heart_disease, 'Low fat foods, oats, green vegetables').
diet(anemia, 'Iron rich foods, spinach, dates, beans').

% Rule to suggest diet

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).

% Display diet suggestion

recommend(Disease) :-
    diet(Disease, Diet),
    write('Disease: '),
    write(Disease),
    nl,
    write('Suggested Diet: '),
    write(Diet).