not_achieved_days = 0

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))

    if visits < 8:
        not_achieved_days += 1

print(f"Target not achieved for {not_achieved_days} days")
