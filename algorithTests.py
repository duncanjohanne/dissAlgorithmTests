from main import *

if __name__ == '__main__':
    print("Test - Overall Execution")
    print('Sequential...')
    time.sleep(3)

    start = time.perf_counter()
    videoFileName, videoLength = handleVideoInput(dataObj.getABdelay(), "X:/Documents/roman/diss/2103/videos/1.mp4")
    fileNames = []
    count = 0
    for i in range(0,2):
        fileNames.append(videoFrameProcessing(videoFileName, count, count+10))
        count+=10
    count = []
    for i in fileNames:
        count.append(getNumberofObjectsDetected(i))
    dataObj.setABcount(sum(count))

    videoFileName, videoLength = handleVideoInput(dataObj.getABdelay(), "X:/Documents/roman/diss/2103/videos/3.mp4")
    fileNames = []
    count = 0
    for i in range(0,2):
        fileNames.append(videoFrameProcessing(videoFileName, count, count+10))
        count+=10
    count = []
    for i in fileNames:
        count.append(getNumberofObjectsDetected(i))
    dataObj.setCcount(sum(count))
    startCalculations(dataObj)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected for side AB : "+str(dataObj.getABcount()))
    print("Objects Detected for side C : "+str(dataObj.getCcount()))
    print("AB Delay : "+str(dataObj.getABdelay()))
    print("C Delay: "+str(dataObj.getCdelay()))
    print("Total Execution Time : "+str(end))

    print('---------------------------------------------------------------------------------------------------------')

    print('Parallel...')
    time.sleep(3)

    start = time.perf_counter()
    abRoutine(dataObj, "X:/Documents/roman/diss/2103/videos/1.mp4")
    print("Objects Detected for side AB : "+str(dataObj.getABcount()))
    # print("Objects Detected for side C : "+str(dataObj.getCcount()))
    abRoutine(dataObj, "X:/Documents/roman/diss/2103/videos/3.mp4")
    # cRoutine(dataObj, "X:/Documents/roman/diss/2103/videos/1.mp4")
    startCalculations(dataObj)
    end = round(time.perf_counter()-start, 2)

    # print("Objects Detected for side AB : "+str(dataObj.getABcount()))
    print("Objects Detected for side C : "+str(dataObj.getCcount()))
    print("AB Delay : "+str(dataObj.getABdelay()))
    print("C Delay: "+str(dataObj.getCdelay()))
    print("Total Execution Time : "+str(end))

    print('---------------------------------------------------------------------------------------------------------')

    print('Test - Object Detection v1')
    print('Sequential...')
    time.sleep(3)

    start = time.perf_counter()
    count = getNumberofObjectsDetected('521_5820.mp4')
    count += getNumberofObjectsDetected('521_5856.mp4')
    count += getNumberofObjectsDetected('521_6747.mp4')
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected : "+str(count))
    print("Total Execution Time : "+str(end))

    print('Parallel...')
    time.sleep(3)

    start = time.perf_counter()
    count = 0
    filesnames = ['521_5820.mp4', '521_5856.mp4', '521_6747.mp4']
    with Pool(3) as p:
        count = p.map(getNumberofObjectsDetected, filesnames)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected : "+str(sum(count)))
    print("Total Execution Time : "+str(end))

    print('Test - Object Detection v2')
    print('Sequential...')
    time.sleep(3)

    start = time.perf_counter()
    count = getNumberofObjDetected('521_5820.mp4')
    count += getNumberofObjDetected('521_5856.mp4')
    count += getNumberofObjDetected('521_6747.mp4')
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected : "+str(count))
    print("Total Execution Time : "+str(end))

    print('Parallel...')
    time.sleep(3)

    start = time.perf_counter()
    count = 0
    filesnames = ['521_5820.mp4', '521_5856.mp4', '521_6747.mp4']
    with Pool(3) as p:
        count = p.map(getNumberofObjDetected, filesnames)
    end = round(time.perf_counter()-start, 2)

    print("Objects Detected : "+str(count))
    print("Total Execution Time : "+str(end))

    print('Test - Video Splitting')
    print('Sequential...')
    time.sleep(3)

    start = time.perf_counter()
    fileNames = []
    count = 0
    for i in range(0,2):
        fileNames.append(videoFrameProcessing("X:/Documents/roman/diss/2103/videos/1.mp4", count, count+10))
        count+=10
    end = round(time.perf_counter()-start, 2)
    print("Total Execution Time : "+str(end))


    print('Parallel')
    time.sleep(3)
    start = time.perf_counter()
    _ = startIter(30, 'videos/3.mp4')
    end = round(time.perf_counter()-start, 2)
    print("Total Execution Time : "+str(end))
