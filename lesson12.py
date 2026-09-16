highest_visits = 0

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))

    if visits > highest_visits:
        highest_visits = visits

print(f"Highest visits in 5 days: {highest_visits}")
