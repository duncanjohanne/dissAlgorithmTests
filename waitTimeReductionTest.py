import time
from functions import dataObj
from main import cRoutine, abRoutine

#iteraing through videos to detect vehicle counts
# if __name__ == "__main__":
#     for i in range(0, 10):
#         video = 'videos/{vid}.mp4'.format(vid=i+1)
#         cRoutine(dataObj, video)
#         print(i)
#         print("Total Count : {count}".format(count=dataObj.getCcount()))
#         print("------------------------------------------------------------------------------")

# 1 -38
# 2 - 27
# 3 - 50
# 4 - 68
# 5 - 20
# 6 - 49
# 7 - 23
# 8 - 20
# 9 - 20
# 10 - 41

#controlling executions with the above vehicle counts

#calculating wait time without external data inclusions
#both lanes allocated 30 second slots
# video 4 for AB and video 8 for C
# object per second equals 0.8
# for AB - 68*0.8 = 54 seconds | AB would require two 30 second slots to clear traffic
# for C  - 20*0.8 = 16 seconds | C would require one 30 second slot -- 30 -16 = 14 second wait time
# Wait time = 14 seconds

#calculating wait time with external data inclusions
# if __name__ == "__main__":
#     abVid = 'videos/4.mp4'
#     abRoutine(dataObj, abVid)
#     cVid = 'videos/8.mp4'
#     cRoutine(dataObj, cVid)

#     print("--------------------------------------------------------------------------------------------")
#     print('''
#     First Slot Delays
#     AB Delay : {aD}
#     C Delay  : {cD}
#     -----------------------------------
#     Objects pass on AB Slot : {abO}
#     Object Pass on C Slot   : {cO}
#     -----------------------------------
#     '''.format(aD=dataObj.getABdelay(), cD=dataObj.getCdelay(), abO=round(dataObj.getABdelay()/0.8,2), cO=round(dataObj.getCdelay()/0.8,2)))

#from running the above code results are outlined below
#    First Slot Delays
#     AB Delay : 44.0
#     C Delay  : 16.0
#     -----------------------------------
#     Objects pass on AB Slot : 55.0
#     Object Pass on C Slot   : 20.0
#     -----------------------------------
# C has been given the time it requires to clear traffic
# Wait time = o seconds
