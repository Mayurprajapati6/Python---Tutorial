chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types["Masala"]) -> Spicy
chai_types.get("Ginger") -> Zesty 

chai_types["Green"] = "Fresh" # change Green value from mild to Fresh

# Loops

for chai in chai_types:
    print(chai, chai_types[chai]) 

# other way

for key, value in chai_types.items():
    print(key, value)

# output
# Masala Spciy
# Ginger Zesty
# Green Fresh

# conditions

if "Masala" in chai_types:
    print("I have masala chai")

print(len(chai_types)) -> 3

chai_types["Earl Greay"] = "Citrus" # new chai key value pair will be added at the end of the dictionary

chai_types.pop("Ginger") # it will remove this key and it's corresponding value from the dictionary

chai_types.popitem() # it will remove recently or last or latest added key in the dictionary

del chai_types("Green") # alternate way to remove any key

chai_types_copy = chai_types.copy()

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"}
}

tea_shop["chai"] -> {"Masala": "Spicy", "Ginger": "Zesty"}

tea_shop["chai"]["Ginger"] -> "Zesty"

squared_num = {x:x**2 for x in range(6)} 
# output -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squared_num.clear() -> {}


keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value) # create new dictionary



