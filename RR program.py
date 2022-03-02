#TODO   
    #initalize list[][] (for loops to take user input)
    #start time
    #inital wait time
    #remove processes from queue after comleted total_time
    #clock time == current_time

def round_robin():
    #initalizing variables 
    process = int(input("total number of processes: "))
    process_tracking = [ [0]*5 for i in range(process)]
    quantum = 0
    context_switch = 0
    current_time = 0
    total_time = 0
    
    #user input for the following specifications of processes/roundrobin program
    for x in range(process):
        process_tracking[x][0] = ("P"+str(x+1))
    
    for x in range(process):
        a_t = int(input("what is the arrival time for P" + str(x+1) + " "))
        process_tracking[x][1] = a_t  

    for x in range(process):
        s_t = int(input("what is the service time for P" + str(x+1) + " "))
        process_tracking[x][2] = s_t
        process_tracking[x][3] = s_t
        total_time = total_time + int(s_t)

    quantum = int(input("What is the Quantum? "))
    context_switch = int(input("What is the context switch? "))

    wait_time = [0] * process
    turnaround_time = [0] * process
    start_time = [0] * process
    inital_wait = [0] * process
    end_time = [0] * process
    completed = [0] * process

#[Process Number, Arival Time, Service Time, Remaining Service Time, Completed]

    while total_time != 0:
        #look at each process remaining time
        for i in range (process):        
            #verify the process has arrived and the process is NOT completed
            if process_tracking[i][1] <= current_time and process_tracking[i][4] != 1:

                #less than quantum, but greater than 0
                if process_tracking[i][3] <= quantum and process_tracking[i][3] >= 0:
                    #if this is first time process runs, note the start time and calculate inital wait
                    if process_tracking[i][2] == process_tracking[i][3]:
                        start_time[i] = current_time
                        inital_wait[i] = start_time[i] - process_tracking[i][1]

                    current_time = current_time + process_tracking[i][3]
                    total_time = total_time - process_tracking[i][3]
                    #process is end
                    process_tracking[i][3] = 0
                #greater than 0 (more than a quantums worth of time remaining in service time)
                elif process_tracking [i][3] >= 0:
                    #if this is first time process runs, note the start time and calulate inital wait
                    if process_tracking[i][2] == process_tracking[i][3]:
                        start_time[i] = current_time
                        inital_wait[i] = start_time[i] - process_tracking[i][1]

                    process_tracking[i][3] = process_tracking[i][3] - quantum
                    total_time = total_time - quantum
                    current_time = current_time + quantum
                #if no more service time remains, calculate wait time and turnaround time, and mark as complete
                if process_tracking[i][4] != 1 and process_tracking[i][3] == 0:
                    waitTime = current_time - process_tracking[i][1] - process_tracking[i][2]
                    wait_time[i] = waitTime
                    turnTime = current_time - process_tracking[i][1]
                    turnaround_time[i] = turnTime
                    process_tracking[i][4] = 1
                    completed[i] = 1 
                    end_time[i] = current_time

                #factor in the context switch time into current time (atleast 2 remaining processes required)
                if sum(completed) < process - 1:
                    current_time = current_time + context_switch
                #account for the last contextswitch operation 
                if sum(completed) == process:
                    end_time[i] = end_time[i] + context_switch
                    turnaround_time[i] = turnaround_time[i] + context_switch
                    wait_time[i] = wait_time[i] + context_switch


    #print output
    for i in range(process):
        print(process_tracking[i][0]) 
        print(start_time[i])
        print(end_time[i])
        print(inital_wait[i])
        print(wait_time[i])
        print(turnaround_time[i])
        print("\n")




round_robin()
