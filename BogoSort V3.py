import time, math, random

def AverageTimeCalculation(array): #get average time per sort attempt
    averageTimeNum = []; averageTime = 0
    for i in range(100_000): #record 1 run time 100_000 times to get an good average
        passed = True; numLast = 0
        timeCalcStart = time.time() #records the current time then runs the array through the sorter
        for i in array:
            if numLast < i: #if array is (3, 4, 1, 51) and the last num is smaller then the next (3, 4) last is 3 next is 4 then we know its ok and can test the next (4, 1)
                numLast = i
            elif numLast > i: #if last num is larger than next num then its not sorted (4, 1)
                passed = False #if not sorrted then set to false and break out of the loop
                break
        if passed == False:
            random.shuffle(array)
            timeCalcEnd = time.time() #after array has been through the sorrter record the time after its been shuffled
            averageTimeNum.append(timeCalcEnd - timeCalcStart) #append the endTime - the startTime to get the time 1 run took
        elif passed == True: #if array was sorted during time calc then program ends
            print("The array was sorted during time calculation")
            print("Final Sorted array:",array)
            quit()
    for i in averageTimeNum: #calculate the average time 1 run takes
        averageTime = averageTime + i #add up all the values from the array of test times
    averageTime = averageTime / len(averageTimeNum) #divide the sum by the number of values to get the average
    PrintTimeToComplete(averageTime,array)

    '''
    the time calculation is affected by the speed of the computer that its being run on, 
    fast cpu means lower times, that also means that if the computer cpu is under high load when the program runs the time calculation then it might give a much higher time that normal. 
    time will vary a lot depending on the load on the cpu at the time of the calculations
    '''

def PrintTimeToComplete(averageTime,array): #use average time to calculate approximate time to completion based on the average bogoSort performance (n-1)n!
    time2Run = (len(array)-1)*math.factorial(len(array)) #approximate number of times the program will have to run, meaning 1 sort attempt
    print("Original Values:",array)
    print("Approximate number of attempts:", f"{time2Run:,d}")
    print("Chance to sort:",1/time2Run,"%")
    try: #for larger numbers it is possible for the time calculation to fail crashing the program
        if (((((time2Run*averageTime)/60)/60)/60)/24) < 365: #if time to completion is less than 1 year then it displays the time in days
            print("Approximate time to completion:",round((((((time2Run*averageTime)/60)/60)/60)/24),6),"days") #calculates the time in milliseconds then converts to seconds, min, hours, days
        else: #if time to completion is more than 1 year then it displays time in years
            try:
                print("Approximate time to completion:",round(((((((time2Run*averageTime)/60)/60)/60)/24)/365),6),"years")
            except Exception as e: #if calculation failed then print the reason
                print("Time calculation failed:",e)
    except Exception as e:
        print("Time calculation failed:",e)
    StartSort(array)

def StartSort(array):
    while True:
        start = str(input("Begin sort? y/n:"))
        if start.lower() == 'y':
            break
        elif start.lower() == 'n':
            quit()
        else:
            print("Enter only 'y' or 'n'")
    sortStartTime = time.time(); runCount = 0; countProgress = 0
    while True:
        passed = True; lastNum = 0
        if countProgress == 1: #every 100_000 attempts the program will update the processing bar
            print("Processing.  ",end='\r')
        elif countProgress == 100_000:
            print("Processing.. ",end='\r')
        elif countProgress == 200_000:
            print("Processing...",end='\r')
        elif countProgress == 300_000:
            countProgress = 0
        else:
            pass
        for i in array: #check if the array is sorted
            if lastNum < i:
                lastNum = i
            elif lastNum > i:
                passed = False
                break
        if passed == False: #if array is not sorted then shuffle the numbers in the array
            random.shuffle(array)
            runCount += 1
            countProgress += 1
        elif passed == True: #if array is sorted then print array, runtime, and number of attempts
            print("\nFinal sorted array:",array)
            print("Total runtime:",round(time.time()-sortStartTime,4),"seconds")
            print("Total attempts:",f"{runCount:,d}")
            input("Press enter to close")
            quit()

array = []
while True:
    try:
        for i in range(int(input("Enter number of values to generate:"))):
            array.append(random.randrange(1,101))
        break
    except:
        print("Must be valid integer")
AverageTimeCalculation(array)
