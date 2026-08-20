# Smart Manufacturing using Predicate Logic

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

for machine, status in machines.items():

    print(machine, ":", status)

    if status == "Active":
        print("  Producing =", True)

    elif status == "Maintenance":
        print("  Producing =", False)

print("\nProduction Status:")

for machine, status in machines.items():

    if status == "Active":
        print(machine, "is Producing")
    else:
        print(machine, "is NOT Producing")
