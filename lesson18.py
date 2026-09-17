visits_list = []

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))
    visits_list.append(visits)

print(f"All visit counts: {visits_list}")
print(f"First day visits: {visits_list[0]}")
print(f"Last day visits: {visits_list[-1]}")
print(f"Total visits: {sum(visits_list)}")
