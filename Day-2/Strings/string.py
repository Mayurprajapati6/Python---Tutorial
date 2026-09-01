chai = "Masala Chai"

print(chai.lower()) -> masal chai
print(chai.upper()) -> MASALA CHAI 

chai = "  Masala Chai  "
print(chai.strip()) -> Masala Chai
print(chai.replace("Masala", "Lemon")) -> Lemon Chai
print(chai) -> "Masal Chai" # string are immutable 

chai = "Lemon, Ginger, Masala, Mint"
# conver string to list in some basis by default it split based on space
print(chai.split(", ")) -> ['Lemon', 'Ginger', 'Masala', 'Mint']

print(chai.find("Chai")) -> 7 (index)
print(chai.find("M"))    -> 0 (index)

chai = "Masala Chai Chai Chai"
print(chai.count("Chai")) -> 3

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order) -> I ordered {} cups of {} chai
print(order.format(quantity, chai_type)) -> I ordered 2 cups of Masala chai

chai_variety = ["Lemon", "Masala", "Ginger"]
# list to string convert
print("".join(chai_variety)) -> LemonMasalaGinger
print(" ".join(chai_variety)) -> Lemon Masala Ginger
print("-".join(chai_variety)) -> Lemon-Masala-Ginger

chai = "Masala Chai"
print(len(chai)) -> 11

chai = "He said, \"Masala chai is awesome\" "
print(chai) -> "He said, "Masala chai is awesome" "

chai = r"c:\user\pwd" (r = raw string)
print(chai) -> c:\user\pwd

chai = "c:\user\pwd"
print(chai) -> c:\user\pwd

chai = "Masala Chai"
print("Masala" in chai) -> True



