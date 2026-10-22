def display_processes(processes, coordinator):
    print("Active Processes:", processes)
    print("Current Coordinator:", coordinator)


def election(processes, failed_process):
    print("\nElection started by P" + str(failed_process))

    higher_processes = []

    for process in processes:
        if process > failed_process:
            higher_processes.append(process)

    if len(higher_processes) == 0:
        coordinator = max(processes)
        print("No higher process is active.")
        print("P" + str(coordinator) + " becomes the coordinator.")
        return coordinator

    for process in higher_processes:
        print("P" + str(failed_process) +
              " sends Election message to P" + str(process))

    print("\nHigher processes respond:")
    
    for process in higher_processes:
        print("P" + str(process) + " -> OK")

    coordinator = max(processes)

    print("\nP" + str(coordinator) +
          " has the highest process ID.")

    print("P" + str(coordinator) +
          " announces itself as the new Coordinator.")

    return coordinator


# TEST CASE 1
print("\n TEST CASE 1 ")

processes = [1, 2, 3, 4, 5]
coordinator = 5

display_processes(processes, coordinator)


# TEST CASE 2
print("\n TEST CASE 2 ")

print("Coordinator P5 has failed.")

processes = [1, 2, 3, 4]
failed_process = 2

coordinator = election(processes, failed_process)

print("\nNew Coordinator: P" + str(coordinator))


# TEST CASE 3
print("\n TEST CASE 3 ")

print("Coordinator P4 has failed.")

processes = [1, 2, 3]
failed_process = 1

coordinator = election(processes, failed_process)

print("\nNew Coordinator: P" + str(coordinator))