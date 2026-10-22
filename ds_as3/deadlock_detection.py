def display(wait_for):
    print("Waiting Relationships:")
    
    for process in wait_for:
        if wait_for[process] is None:
            print(f"{process} -> None")
        else:
            print(f"{process} -> {wait_for[process]}")


def detect_deadlock(wait_for):
    for start in wait_for:
        current = start
        visited = set()

        while current is not None:

            if current in visited:
                return True

            visited.add(current)

            if current not in wait_for:
                break

            current = wait_for[current]

    return False

# TEST CASE 1 - NO DEADLOCK

print("\n TEST CASE 1 ")

wait_for = {
    "P1": "P2",
    "P2": "P3",
    "P3": None
}

display(wait_for)

if detect_deadlock(wait_for):
    print("Deadlock Detected!")
else:
    print("No Deadlock")


# TEST CASE 2 - TWO PROCESS DEADLOCK

print("\n TEST CASE 2 ")

wait_for = {
    "P1": "P2",
    "P2": "P1"
}

display(wait_for)

if detect_deadlock(wait_for):
    print("Deadlock Detected!")
else:
    print("No Deadlock")


# TEST CASE 3 - THREE PROCESS DEADLOCK

print("\n TEST CASE 3 ")

wait_for = {
    "P1": "P2",
    "P2": "P3",
    "P3": "P1"
}

display(wait_for)

if detect_deadlock(wait_for):
    print("Deadlock Detected!")
else:
    print("No Deadlock")


# TEST CASE 4 - MULTIPLE INDEPENDENT PROCESSES

print("\n TEST CASE 4 ")

wait_for = {
    "P1": "P2",
    "P2": None,
    "P3": "P4",
    "P4": None
}

display(wait_for)

if detect_deadlock(wait_for):
    print("Deadlock Detected!")
else:
    print("No Deadlock")


# TEST CASE 5 - DEADLOCK AND RECOVERY

print("\n TEST CASE 5 ")

wait_for = {
    "P1": "P2",
    "P2": "P3",
    "P3": "P1"
}

display(wait_for)

if detect_deadlock(wait_for):

    print("Deadlock Detected!")

    print("Recovery: Terminating P1")

    # Remove P1
    del wait_for["P1"]

    # P2 was waiting for P3, P3 was waiting for P1.
    # After P1 is terminated, P3 no longer waits.
    for process in wait_for:
        if wait_for[process] == "P1":
            wait_for[process] = None

    print("\nAfter Recovery:")

    display(wait_for)

    if detect_deadlock(wait_for):
        print("Deadlock still exists!")
    else:
        print("Deadlock Resolved!")

else:
    print("No Deadlock")