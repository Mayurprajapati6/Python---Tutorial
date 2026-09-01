tea_varities = ["Black", "Green", "Oolong", '"White']
print(tea_varities)
print(tea_varities[1])  -> "Green"
print(tea_varities[-1]) -> "White"
print(tea_varities[1:3]) -> ["Green", "Oolong"]

tea_varities[3] = "Herbal" -> it will change 3 index string with new value in tea_varities list

tea_varities[1:3] = ["Masala", "Pink"] ( change index 1 and 2 chai value with this new array value)

tea_varities = ["Black", "Green", "Oolong", '"White']

tea_varities.append("Herbal") 
tea_varities.pop() # remove last value
tea_varities.remove("Green") # to remove any specific index value
tea_varities.insert(position, value_to_insert) -> tea_varities.insert(1, "pink") # to insert value at particular index

tea_varities_copy = tea_varities.copy() # both have same value but both point to different reference

squared_num = [x**2 for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
range(10) means 0 to 9







