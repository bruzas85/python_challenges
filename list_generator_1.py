'''Работа с генераторами списков 2'''
lst = [
    ('Sidorov', 1995),
    ('Ivanov', 1985),
    ('Kaluzir', 2004),
    ('Bruzas', 1996),
    ('Arhipov', 2018),
]
b = [elem [0] for elem in lst]
print(b)