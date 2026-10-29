data = [2, 4, 10, 12, 3, 20, 30, 11, 25]

m1, m2 = 4, 11

for i in range(1, 4):
    c1, c2 = [], []

    for x in data:
        if abs(x - m1) <= abs(x - m2):
            c1.append(x)
        else:
            c2.append(x)

    print("Iteration", i)
    print("C1 =", c1)
    print("C2 =", c2)

    m1 = sum(c1) / len(c1)
    m2 = sum(c2) / len(c2)

    print("M1 =", m1)
    print("M2 =", m2)
    print()