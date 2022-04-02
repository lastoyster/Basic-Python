simpsonfamily = [
    ('Homer',50),
    ('Marge',45),
    ('Bart',11),
    ('Lisa', 9),
    ('Maggie', 1)
]

_name_ = input('Enter name: ').lower().capitalize()
while _name_.Lower() not in [i[0].lower() for i in simpsonfamily]:
    print('this name not in simpsonfamily')
    _name_ = input('Enter name: ').lower().capitalize()
else:
        for name, age in simpsonfamily:
                if _name_ == name:
                    print(_name_, age, sep=' is ')
                    break
