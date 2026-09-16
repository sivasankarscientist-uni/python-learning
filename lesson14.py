achieved_days = 0

for day in range(1, 6):
    visits = int(input(f"Enter visits for day {day}: "))

    if visits >= 8:
        achieved_days += 1

print(f"Target achieved for {achieved_days} days")

