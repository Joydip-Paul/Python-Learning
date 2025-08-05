# POWERFUL LOOPS

# Loop through a string
for char in "KAMAN ASA":
    print(char)

print()  # blank line

# Loop through a list
my_gf_list = ["Subhashree", "Bidda Sinha", "Katrina", "Sunny Leon"]
for gf in my_gf_list:
    print(gf)

print()  # blank line

# Loop with enumerate
for index, gf in enumerate(my_gf_list):
    print(index, gf)

print()  # blank line

# While loop with break
count = 0
while True:
    print("COUNT IS:", count)
    count += 10
    if count == 50:
        break