def round_robin():
    #initalizing variables 
    processes = []
    arival_times = []
    service_times = []
    remaining_times = []
    completed = []
    quantum = 0
    context_switch = 0
    current_time = 0
    total_time = 0
    
    #user input for the following specifications of processes/roundrobin program
    process = int(input("total number of processes: "))
    for x in range(process):
        processes.append("P"+str(x+1))
    
    for x in processes:
        a_t = input("what is the arrival time for " + x + " ")
        arival_times.append(int(a_t))

    for x in processes:
        s_t = input("what is the service time for " + x + " ")
        service_times.append(int(s_t))
        remaining_times.append(int(s_t))
        total_time = total_time + int(s_t)
    
    for x in processes:
        completed.append(0)

    quantum = int(input("What is the Quantum? "))
    context_switch = int(input("What is the context switch? "))

    #combine all user inputs into single list for tracking the round robin service
    process_tracking = []
    for a,b,c,d,e in zip (processes, arival_times, service_times, remaining_times, completed):
        process_tracking.append([a,b,c,d,e])

    wait_time = []
    turnaround_time = []

    while total_time != 0:
        #look at each process remaining time
        for i in range (len(processes)):
            #less than quantum, but greater than 0
            if process_tracking[i][3] <= quantum and process_tracking[i][3] >= 0:
                current_time = current_time + process_tracking[i][3]
                total_time = total_time - process_tracking[i][3]
                #process is end
                process_tracking[i][3] = 0
            #greater than 0 (more than a quantums worth of time remaining in service time)
            elif process_tracking [i][3] >= 0:
                process_tracking[i][3] = process_tracking[i][3] - quantum
                total_time = total_time - quantum
                current_time = current_time + quantum
            #if no more service time remains, calculate wait time and turnaround time, and mark as complete
            if process_tracking[i][4] != 1 and process_tracking[i][3] == 0:
                wait_time.append(current_time - process_tracking[i][1] - process_tracking[i][2])
                turnaround_time.append(current_time - process_tracking[i][1])
                process_tracking[i][3] = 1

    #print output
    print("\n%-15s %-15s %-10s\n\n"%("Process", "Total Wait Time", "Turnaround Time"))
    for i in range(len(processes)):
        print("\t%-10d %-15.2f \t %-10.2f"%(i, wait_time[i], turnaround_time[i]))



round_robin()