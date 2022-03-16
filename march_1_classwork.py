import random
def arival_time():
    inter_arival_times = []
    for i in range(99):
        x = (random.randrange(4, 10))
        inter_arival_times.append(x)
    
    print("the inter arival times are: " + str(inter_arival_times))    
    print("\n")
    
    arival_times = [0] * 100
    for i in range(1,99):
        arival_times[i] = arival_times[i-1] + inter_arival_times[i-1]
    #last arival_time[] index was showing 0, this fixes that
    arival_times[99] = arival_times[98] + inter_arival_times[98]
    print("the arrival times are: " + str(arival_times))
    
def service_time():
    service_times = []
    for i in range(100):
        x = (random.randrange(2,6))
        service_times.append(x)
    print("The service times are: " + str(service_times))

arival_time()    
print("\n")
service_time()
