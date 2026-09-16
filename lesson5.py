visit_count = int(input("Enter today's visit count: "))

if visit_count == 8:
    print("Exactly target achieved")
elif visit_count > 8:
    print("Target exceeded")
else:
    print("Target not achieved")
