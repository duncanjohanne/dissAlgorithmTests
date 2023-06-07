from functions import *
import time

if __name__ == '__main__':
    # print('Version1')
    # print("Object detection w/o ")
    # start = time.perf_counter()
    # count = getNumberofObjectsDetected("X:/Documents/roman/diss/2103/2of28233.mp4")
    # count += getNumberofObjectsDetected("X:/Documents/roman/diss/2103/55_2020.mp4")
    # count += getNumberofObjectsDetected("X:/Documents/roman/diss/2103/55_2716.mp4")
    # print("Objects detected : "+str(count))
    # print("Total Execution TIme : "+str(time.perf_counter()-start))



    # print("Object detection w  ")
    # start = time.perf_counter()
    # inputs = ["X:/Documents/roman/diss/2103/2of28233.mp4","X:/Documents/roman/diss/2103/55_2020.mp4","X:/Documents/roman/diss/2103/55_2716.mp4"]
    # with Pool(3) as p:
    #     result = p.map(getNumberofObjectsDetected, inputs)
    # print("Objects detected : "+str(result))
    # print("Total Execution TIme : "+str(time.perf_counter()-start))

    # print('Version2')
    # print("Object detection w/o ")
    start = time.perf_counter()
    # count = getNumberofObjDetected("X:/Documents/roman/diss/2103/2of28233.mp4")
    # count += getNumberofObjDetected("X:/Documents/roman/diss/2103/55_2020.mp4")
    # count += getNumberofObjDetected("X:/Documents/roman/diss/2103/55_2716.mp4")
    count = []
    count.append(videoFrameProcessing("X:/Documents/roman/diss/2103/videos/1.mp4", 0, 10))
    count.append(videoFrameProcessing("X:/Documents/roman/diss/2103/videos/1.mp4", 10, 20))
    count.append(videoFrameProcessing("X:/Documents/roman/diss/2103/videos/1.mp4", 20, 30))
    # print("Objects detected : "+str(count))
    print("Filenames : "+str(count))
    print("Total Execution TIme : "+str(time.perf_counter()-start))



    print("Object detection w  ")
    start = time.perf_counter()
    inputs = ["X:/Documents/roman/diss/2103/videos/1.mp4","X:/Documents/roman/diss/2103/55_2020.mp4","X:/Documents/roman/diss/2103/55_2716.mp4"]
    input = [(inputs[0], 0, 10), (inputs[0], 10, 20), (inputs[0], 20, 30)]
    with Pool(3) as p:
        result = p.starmap(videoFrameProcessing, input)
    # print("Objects detected : "+str(result))
    print("Filenames : "+str(result))
    print("Total Execution TIme : "+str(time.perf_counter()-start))