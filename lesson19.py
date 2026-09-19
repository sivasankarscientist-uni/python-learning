visits_list = []

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))
    visits_list.append(visits)

highest_visits = max(visits_list)
lowest_visits = min(visits_list)

print(f"All visit counts: {visits_list}")
print(f"Highest visits: {highest_visits}")
print(f"Lowest visits: {lowest_visits}")
