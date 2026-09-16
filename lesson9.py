total_visits = 0
day = 1

while day <= 5:
    visits = int(input(f"Enter visits for day {day}: "))
    total_visits = total_visits + visits
    day = day + 1

print(f"Total visits for 5 days: {total_visits}")
