import math

def entropy(yes, no):
    total = yes + no
    result = 0
    for count in (yes, no):
        if count > 0:
            p = count / total
            result = result - p * math.log2(p)
    return result

# Counts from the table (Yes = habitable, No = not habitable)
total = 800
entropy_s = entropy(374, 426)

# Split on Size
i_size = (350 / total) * entropy(190, 160) + (450 / total) * entropy(184, 266)
gain_size = entropy_s - i_size

# Split on Orbit
i_orbit = (300 / total) * entropy(159, 141) + (500 / total) * entropy(215, 285)
gain_orbit = entropy_s - i_orbit

print("Entropy(S)   =", round(entropy_s, 4))
print("Gain(Size)   =", round(gain_size, 4))
print("Gain(Orbit)  =", round(gain_orbit, 4))

if gain_size > gain_orbit:
    print("Root node: Size")
else:
    print("Root node: Orbit")

# Decision tree learned (Size at the root, then Orbit)
def predict(size, orbit):
    if size == "Big":
        if orbit == "Near":
            return "No"    # Yes: 20, No: 130
        else:
            return "Yes"   # Yes: 170, No: 30
    else:
        if orbit == "Near":
            return "Yes"   # Yes: 139, No: 11
        else:
            return "No"    # Yes: 45, No: 255

print("a) Big, Far    ->", predict("Big", "Far"))
print("b) Small, Near ->", predict("Small", "Near"))