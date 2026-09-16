visit_count = int(input("Enter today's visit count: "))
leave_status = input("Are you on leave? (yes/no): ")

if visit_count >= 8 and leave_status == "no":
    print("Target achieved and active")
elif leave_status == "yes":
    print("You are on leave")
else:
    print("Target not achieved")
