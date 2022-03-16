#clock time == current_time
import random
from prettytable import PrettyTable
def round_robin():
    #user input for total processes
    process = int(input("total number of processes: "))
    
    #initalizing variables 
    
    # The structure of the list:
    #[Process Number, Arival Time, Service Time, Remaining Service Time, Completed]
    process_tracking = [ [0]*5 for i in range(process)]
    quantum = 0
    context_switch = 0
    current_time = 0
    total_time = 0
    
    #convert processes to "Pn" format
    for x in range(process):
        process_tracking[x][0] = ("P"+str(x+1))
    
    #generate inter_arival times randomly
    inter_arival_times = []
    for i in range(process - 1):
        x = (random.randrange(4, 10))
        inter_arival_times.append(x)

    #calculate arival times for each process based on inter_arival times
    arival_times = [0] * process
    for i in range(1,process):
        arival_times[i] = arival_times[i-1] + inter_arival_times[i-1]
    
    # Move calculated arival times into matrix tracker (process_tracking[][1])
    for x in range (process):
        process_tracking[x][1] = arival_times[x]

    # Generate Service times randomly
    service_times = []
    for i in range(process):
        x = (random.randrange(2,6))
        service_times.append(x)

    # Add generated service times (and remaining time) to matrix tracker (process_tracking[x][2AND3])
    for x in range (process):
        process_tracking[x][2] = service_times[x]
        process_tracking[x][3] = service_times[x]
        #also track total needed service time
        total_time = total_time + service_times[x]
        

    #user input for Quantum and Context Switch Time
    quantum = int(input("What is the Quantum? "))
    context_switch = int(input("What is the context switch? "))

    #Initalize Gantt Chart Output Values 
    wait_time = [0] * process
    turnaround_time = [0] * process
    start_time = [0] * process
    inital_wait = [0] * process
    end_time = [0] * process
    completed = [0] * process

    # The structure of the list:
    #[Process Number, Arival Time, Service Time, Remaining Service Time, Completed]

    #total_time = total service time from all processes
    while total_time != 0:
        #look at each process remaining time
        for i in range (process):        
            #verify the process has arrived and the process is NOT completed
            if process_tracking[i][1] <= current_time and process_tracking[i][4] != 1:

                #less than quantum, but greater than 0
                if process_tracking[i][3] <= quantum and process_tracking[i][3] >= 0:
                    #first time process runs, assign the start time and inital wait
                    if process_tracking[i][2] == process_tracking[i][3]:
                        start_time[i] = current_time
                        inital_wait[i] = start_time[i] - process_tracking[i][1]
                    
                    #update current time and total_time
                    current_time = current_time + process_tracking[i][3]
                    total_time = total_time - process_tracking[i][3]
                    #process is complete, remaining time = 0
                    process_tracking[i][3] = 0
                    
                #greater than 0 (more than a quantums worth of time remaining in service time)
                elif process_tracking [i][3] >= 0:
                    #first time process runs, note the start time and calulate inital wait
                    if process_tracking[i][2] == process_tracking[i][3]:
                        start_time[i] = current_time
                        inital_wait[i] = start_time[i] - process_tracking[i][1]

                    #update current_time, total_time and remaining_time
                    process_tracking[i][3] = process_tracking[i][3] - quantum
                    total_time = total_time - quantum
                    current_time = current_time + quantum
                    
                #if no more service time remains and process is NOT marked complete
                if process_tracking[i][4] != 1 and process_tracking[i][3] == 0:
                    # Calculate wait time and turnaround time
                    # Wait Time = (current time - arival time - service time)
                    # Turnaround Time = (current time - arival time)
                    
                    waitTime = current_time - process_tracking[i][1] - process_tracking[i][2]
                    turnTime = current_time - process_tracking[i][1]
                    
                    #assign values to Gannt Chart output variables 
                    wait_time[i] = waitTime
                    turnaround_time[i] = turnTime
                    
                    #mark process as complete and assign end time as current time
                    process_tracking[i][4] = 1
                    completed[i] = 1 
                    end_time[i] = current_time

                #factor in the context switch time into current time (atleast 2 remaining processes required)
                if sum(completed) < process - 1:
                    current_time = current_time + context_switch
                    
                #special case for the last progress, need to acount for final context switch
                if sum(completed) == process:
                    end_time[i] = end_time[i] + context_switch
                    turnaround_time[i] = turnaround_time[i] + context_switch
                    wait_time[i] = wait_time[i] + context_switch

    x = PrettyTable()
    x.field_names = ["Process ID", "Start Time", "End Time", "Inital Wait Time", "Total Wait Time", "TurnAround Time"]
    for i in range(process):
        x.add_row([process_tracking[i][0], start_time[i], end_time[i], inital_wait[i], wait_time[i], turnaround_time[i]])
     
    print(x)

round_robin()
