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







  

  

  
  
