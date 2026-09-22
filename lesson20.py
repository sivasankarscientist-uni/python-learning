visits_list = []

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))
    visits_list.append(visits)

target = int(input("Enter target visits: "))

count = 0

for visits in visits_list:
    if visits >= target:
        count += 1

print(f"All visit counts: {visits_list}")
print(f"Target: {target}")
print(f"Days that achieved target: {count}")
