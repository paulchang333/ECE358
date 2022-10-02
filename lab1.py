import math
import random
import statistics

def expoRanVar(lam):
  U = random.random()
  x = -1*(1/lam)*math.log(1-U)
  return x

class DES:
  def __init__ (self,event,time,length = 0,service_time = 0):
    self.event = event
    self.time = time
    self.length = length
    self.service_Time = service_time
    
    

# class packet:


# lis = []
# for i in range(0,1000):
#   lis.append(expoRanVar(75))
# print (statistics.mean(lis))
# print (statistics.variance(lis))

DES_lis = []

EN = 0
P_idle = 0
P_loss = 0

# provided to us 
c = 1000000
l = 2000
# p = 20
# K = finite buffer size

# lamda = (c/l)*p
lamda = 75
arrival_time = 0
dept_time = 0
obs_time = 0

# code to generate arrival event
while arrival_time < 10 or obs_time < 10:
  
  #creating arrival event
  if (arrival_time < 10):
    packet_length = round(expoRanVar(1/lamda))
    packet_arrival_time = expoRanVar(lamda) + arrival_time
    packet_service_time = packet_length/c
    obj = DES ("arrival",packet_arrival_time,packet_length,packet_service_time)
    DES_lis.append(obj)
    arrival_time = packet_arrival_time
    
    if (dept_time > arrival_time):
      dept_time += packet_service_time
      obj1 = DES ("departure",dept_time)
      DES_lis.append(obj1)
    else :
      dept_time = arrival_time + packet_service_time
      obj2 = DES ("departure",dept_time)
      DES_lis.append(obj2)
    
  #creating observer event
  if (obs_time < 10):
    packet_obs_time = expoRanVar(5*lamda) + obs_time
    obj = DES ("observer",packet_obs_time)
    DES_lis.append(obj)
    obs_time = packet_obs_time
  
    
DES_lis.sort(key = lambda x:x.time)

for i in DES_lis:
    print ("type: " +i.event + "time: ", i.time)

T = 1000
eventTypeArr = [] # for organizing event types choronologically
eventTimeArr = [] # for organizing event times chronologically
bufferSize = 0
n_a = 0 # no of arrival events
n_d = 0 # no of departure events
n_o = 0 # no of observer events
total_events = 0 # no of all events
last_departure_time = 0
bufferSizeArray = [] # counting the buffer size when observer is detected
sumOfBufferSize = 0 # intermediate variable to find En
En = 0
idleTime = 0 #intermediate variable to find Pidle
Pidle = 0

for i in range (T): # runs from 0 to 999

    while len(DES_lis) and i == math.floor(DES_lis[0].time):
        
        eventTypeArr.append(DES_lis[0].event)
        eventTimeArr.append(DES_lis[0].time)
        
        if (DES_lis[0].event == "arrival"):
            n_a += 1
        elif (DES_lis[0].event == "departure"):
            n_d += 1
            last_departure_time = DES_lis[0].time
        elif (DES_lis[0].event == "observer"):
            n_o += 1
            bufferSize = n_a - n_d
            bufferSizeArray.append(bufferSize)
        
        # 0.8% error case, when arrival is followed with an arrival, fix when 5% edge case is too eh
        if ((n_a == n_d + 1) and n_d != 0):
            idleTime += DES_lis[0].time - last_departure_time

        DES_lis.pop(0)

for i in range (len(bufferSizeArray)):
    sumOfBufferSize += bufferSizeArray[i]

for i in range (len(eventTypeArr)):
    print(str(eventTypeArr[i]) + " " + str(eventTimeArr[i]))

En = sumOfBufferSize / len(bufferSizeArray)

Pidle = idleTime / T

print(En)
print(Pidle)

