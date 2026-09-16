total_visits = 0

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))
    total_visits += visits

print(f"Total visits for 5 days: {total_visits}")
