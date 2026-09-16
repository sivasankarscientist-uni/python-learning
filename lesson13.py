lowest_visits = None

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))

    if lowest_visits is None or visits < lowest_visits:
        lowest_visits = visits

print(f"Lowest visits in 5 days: {lowest_visits}")
