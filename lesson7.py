visit_count = int(input("Enter today's visit count: "))
leave_status = input("Are you on leave? (yes/no): ")

if leave_status == "no":
    if visit_count >= 8:
        print("Active and target achieved")
    else:
        print("Active but target not achieved")
else:
    print("You are on leave")
