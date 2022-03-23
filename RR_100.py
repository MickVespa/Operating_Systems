#clock time == current_time
#total_time = total service time from all processes
import random
from prettytable import PrettyTable
def round_robin():
    ############################################## INITALIZE VARRIABLES #################################################
    
    #user input for total processes
    process = int(input("total number of processes: "))
        
    # The structure of the list:
    #[Process Number, Arival Time, Service Time, Remaining Service Time, Completed]
    process_tracking = [ [0]*5 for i in range(process)]
    quantum = 0
    context_switch = 0
    current_time = 0
    total_time = 0
    
    #convert processes to "Pn" format
    for x in range(process):
        process_tracking[x][0] = x+1
    
    #generate inter_arival times randomly
    inter_arival_times = []
    for i in range(process - 1):
        x = (random.randrange(4, 10))
        inter_arival_times.append(x)
    
    print("the inter arival times are: " + str(inter_arival_times))    
    print("\n")

    #calculate arival times for each process based on inter_arival times
    arival_times = [0] * process
    for i in range(1,process):
        arival_times[i] = arival_times[i-1] + inter_arival_times[i-1]
    print("the arrival times are: " + str(arival_times))
    print("\n")

    
    # Move calculated arival times into matrix tracker (process_tracking[][1])
    for x in range (process):
        process_tracking[x][1] = arival_times[x]

    # Generate Service times randomly
    service_times = []
    for i in range(process):
        x = (random.randrange(2,6))
        service_times.append(x)
    print("The service times are: " + str(service_times))
    print("\n")

    # Add generated service times (and remaining time) to matrix tracker (process_tracking[x][2AND3])
    for x in range (process):
        process_tracking[x][2] = service_times[x]
        process_tracking[x][3] = service_times[x]
        #also track total needed service time
        total_time = total_time + service_times[x]

    #Calculate average inter arival and service time
    avg_inter = sum(inter_arival_times) / len(inter_arival_times)
    avg_service = sum(service_times) / len(service_times)

    #delete lists to save memory 
    del service_times
    del inter_arival_times
    del arival_times
        

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

    cycle = 0 # used to track the loop through all processes 
    ready_queue = set() # make ready queue a set to keep from adding duplicate IDs

    #################################################### TIME BEGINS ###############################################################
    
    while total_time != 0:
        #look at each process remaining time
        for i in range (process): 
            #verify the process has arrived and the process is NOT completed
            if process_tracking[i][1] <= current_time and process_tracking[i][4] != 1:
                ready_queue.add(i)
            
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
                    #remove process from ready queue AND reset cycle to 0
                    ready_queue.remove(i)
                    cycle = 0
                    #add context switch time for removing process from running state
                    current_time = current_time + context_switch

            
            #pass time if waiting for new process while ready queue is empty
            if len(ready_queue) == 0 and cycle >= process:
                current_time = current_time + 1
                cycle = 0
            
            # prevent endless loop looking for ready processes
            cycle = cycle + 1
            #if current process has completed quantum, and there are multiple processes in the ready list, switch process and apply CS time
            if i in ready_queue and len(ready_queue) > 1:
                current_time = current_time + context_switch
            
    
    ######################################################## DISPLAY RESULTS #######################################################################

    avg_turnAround = sum(turnaround_time) / len(turnaround_time)
    avg_wait = sum(wait_time) / len(wait_time)
    

    x = PrettyTable()
    x.field_names = ["Process ID", "Start Time", "End Time", "Inital Wait Time", "Total Wait Time", "TurnAround Time"]
    for i in range(process):
        x.add_row([process_tracking[i][0], start_time[i], end_time[i], inital_wait[i], wait_time[i], turnaround_time[i]])
     
    print(x)
    print("\n")
    print("Average Interarrival time: " + str(avg_inter) )
    print("Average Service times " + str(avg_service))
    print("Average Turnaround Time: " + str(avg_turnAround))
    print("Average Total Wait Time: " + str(avg_wait))

round_robin()
