import random, time, math, copy

def arrayGen(arrayValues):
    arraySort = []
    timeEst = (arrayValues - 1) * math.factorial(arrayValues)
    for i in range(arrayValues):
        arraySort.append(random.randrange(1,101))
    arrayStart = copy.deepcopy(arraySort)
    #Calculate average time to sort and then shuffle again
    averageTime = []
    print("Calculating approximate time to completion. This may take a few moments.")
    run = 0; milestone = 5_000_000; time69 = time.time()
    for i in range(500_000):
        lastNum = 0; sorted = True
        time10 = time.time()
        run += 1
        for i in arraySort:
            if lastNum < i:
                lastNum = i
            elif lastNum > i:
                sorted = False
                break
        if sorted == False:
            if run == milestone:
                pass
            random.shuffle(arraySort)
            time20 = time.time()
            averageTime.append(abs(time10-time20))
        else:
            time699 = time.time()
            print("The array was sorted while calculating the time to sort it...")
            print("Total Runtime:",round(abs(time69-time699),4),"seconds")
            print("Total attempts:",run)
            print("Original array:",arrayStart)
            print("Final Sorted array:",arraySort)
            input("Press enter to close the program.")
            quit()
    result = 0
    for i in averageTime:
        result = float(result) + float(i)
    try:
        average = result / len(averageTime)
    except Exception as ee:
        print("Average time per attempt:",ee,"seconds")
    #End of average time calculation
    arraySort = arrayStart
    print("\nOriginal Array:",arraySort)
    print("AVERAGE Bogosort performance for",f"{arrayValues:,d}","values:")
    print("Average time per attempt:",average,"seconds")
    print("Approximate number of attempts:",f"{timeEst:,d}")
    print("Chance to sort:",1/timeEst,"%")

    try:
        if (((((timeEst*average)/60)/60)/60)/24) <= 365:
            print("Approximate time to completion:", round((((((timeEst*average)/60)/60)/60)/24),6), "days")
        else:
            try:
                print("Approximate time to completion:", round(((((((timeEst*average)/60)/60)/60)/24)/365),2), "years")
            except Exception as e: 
                print("Approximate time to completion: Error:",e)
    except Exception as eee:
        print("Approximate time to completion: Error:",eee)
    return arraySort

def arraySort(arraySort):
    time0 = time.time(); timesRun = 0; milestone = 5_000_000
    print()
    while True:
        lastNum = 0; sorted = True
        timesRun += 1
        for i in arraySort:
            if lastNum < i:
                lastNum = i
            elif lastNum > i:
                sorted = False
                break
        if sorted == False:
            if timesRun == milestone:
                time2 = time.time()
                print("\rSort attempts so far:",f"{timesRun:,d}","     Runtime:",round(abs(time0-time2),4),"seconds or",round(abs(time0-time2)/60,2),"minutes or",round(abs(time0-time2)/3600,2),"hours          ",end='\r')
                milestone += 5_000_000
            random.shuffle(arraySort)
        else:
            time1 = time.time()
            print("Total Runtime:",round(abs(time0-time1),4),"seconds")
            print("Total sort attempts:",f"{timesRun:,d}")
            print("Final Sorted Array:",arraySort)
            input("Press enter to close the program.")
            quit()

print("WARNING: Lists with more than 1 value may take literally forever to sort...")
arraySort(arrayGen(int(input("Enter number of values to sort:"))))