total_visits = 0

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))
    total_visits += visits

average_visits = total_visits / 5

print(f"Total visits: {total_visits}")
print(f"Average visits: {average_visits}")
