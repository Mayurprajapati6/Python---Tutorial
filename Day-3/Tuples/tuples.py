tea_types = ("Black", "Green", "Oolong")

tea_types[0] -> "Black"
tea_types[-1] -> "Oolong"
tea_types[1:] -> ('Green', "Oolong")

tea_types[0] = "Lemon" # Not possible since tuples are immutable means you can't reassigned

len(tea_types) # to find len

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types # ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')

more_tea = ("Herbal", "Earl Grey", "Herbal")
more_tea.count("Herbal") -> 2

type(tea_types) -> tuple 


# all other things will be same as list

