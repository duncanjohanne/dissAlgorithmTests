from main import *

if __name__ == '__main__':
    print("Test - Object Detection Without Video Splitting")
    print('v1...')
    time.sleep(3)

    start = time.perf_counter()

    videoFileName = "X:/Documents/roman/diss/2103/videos/3.mp4"
    
    count = getNumberofObjectsDetected('522_8165.mp4')
    count += getNumberofObjectsDetected('522_8210.mp4')
    count += getNumberofObjectsDetected('522_9241.mp4')
    dataObj.setCcount(count)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected  : "+str(dataObj.getCcount()))
    print("Total Execution Time : "+str(end))
    
    
    print('v2...')
    time.sleep(3)

    start = time.perf_counter()

    videoFileName = "X:/Documents/roman/diss/2103/videos/3.mp4"
    
    count = getNumberofObjDetected('522_8165.mp4')
    count += getNumberofObjDetected('522_8210.mp4')
    count += getNumberofObjDetected('522_9241.mp4')
    dataObj.setCcount(count)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected  : "+str(dataObj.getCcount()))
    print("Total Execution Time : "+str(end))
    
    
    print("Test - Object Detection With Video Splitting")
    print('Sequential...')
    print('v1...')
    time.sleep(3)

    start = time.perf_counter()

    videoFileName = "X:/Documents/roman/diss/2103/videos/3.mp4"
    fileNames = []
    count = 0
    for i in range(0,2):
        fileNames.append(videoFrameProcessing(videoFileName, count, count+10))
        count+=10
    count = []
    for i in fileNames:
        count.append(getNumberofObjectsDetected(i))
    dataObj.setCcount(count)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected  : "+str(dataObj.getCcount()))
    print("Total Execution Time : "+str(end))
    
    
    print('v2...')
    time.sleep(3)

    start = time.perf_counter()

    videoFileName = "X:/Documents/roman/diss/2103/videos/3.mp4"
    fileNames = []
    count = 0
    for i in range(0,2):
        fileNames.append(videoFrameProcessing(videoFileName, count, count+10))
        count+=10
    count = []
    for i in fileNames:
        count.append(getNumberofObjDetected(i))
    dataObj.setCcount(count)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected  : "+str(dataObj.getCcount()))
    print("Total Execution Time : "+str(end))
    
    print("Test - Object Detection With Video Splitting")
    print('Parallel...')
    print('v1...')
    time.sleep(3)

    start = time.perf_counter()

    videoFileName = "X:/Documents/roman/diss/2103/videos/3.mp4"
    fileNames = startIter(30, videoFileName)
    count = startDetections(fileNames)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected  : "+str(count))
    print("Total Execution Time : "+str(end))
    
    
    print('v2...')
    time.sleep(3)

    start = time.perf_counter()

    videoFileName = "X:/Documents/roman/diss/2103/videos/3.mp4"
    fileNames = startIter(30, videoFileName)
    count = startDetectionsv2(fileNames)
    dataObj.setCcount(count)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected  : "+str(dataObj.getCcount()))
    print("Total Execution Time : "+str(end))