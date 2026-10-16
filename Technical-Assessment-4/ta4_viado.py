facts = {
    "temperature": 32,
    "raining": False,
    "humidity": 80,
    "person_present": True,
    "aircon_on": False
}


def rule1(facts):
    if facts["temperature"] > 30:
        return "Turn on the aircon"


def rule2(facts):
    if facts["humidity"] > 70:
        return "Turn on the fan"


def rule3(facts):
    if facts["person_present"] and not facts["raining"]:
        return "Open the window"


rules = [rule1, rule2, rule3]

actions = []

for rule in rules:
    result = rule(facts)
    if result:
        actions.append(result)


print("Rule-Based Reasoning Actions:")
for action in actions:
    print("-", action)


case_base = [
    {
        "problem": {"temperature": 32, "raining": False},
        "solution": "Turn on the aircon"
    },
    {
        "problem": {"temperature": 25, "raining": True},
        "solution": "Keep the windows closed"
    },
    {
        "problem": {"temperature": 30, "raining": False},
        "solution": "Open the window"
    }
]


new_problem = {
    "temperature": 32,
    "raining": False
}

best_case = None
best_score = 0

for case in case_base:
    score = 0

    for key in new_problem:
        if new_problem[key] == case["problem"][key]:
            score += 1

    if score > best_score:
        best_score = score
        best_case = case


solution = best_case["solution"]

print("\nCBR Reused Solution:")
print(solution)


change = input("Change the solution? (yes/no): ")

if change == "yes":
    solution = input("Enter new solution: ")


case_base.append({
    "problem": new_problem,
    "solution": solution
})

print("New case added to the case base.")