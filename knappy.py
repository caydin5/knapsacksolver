from tabulate import tabulate
def knappy(W, wt, val):
    K = [[0 for x in range(W+1)] for x in range(len(val)+1)]
    #H = [i+1 for i in range(len(val))]
    H = [i for i in range(W+1)]
    H.insert(0,"V / W")
    VW = [str(val[k]) + " / " + str(wt[k]) for k in range(len(val))]

    for i in range(len(val)+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    ##Enhancements to table - Adding row headers (tabulate workaround)
    #for k in range(len(val)):
    #    K.insert(k, val[k])
    #print('[%s]' % '\n'.join(map(str, K[1:])))
    print(tabulate(K[1:], headers = H ,tablefmt = "fancy_grid",showindex=(VW),colalign=("center",)))
    #print (max(K[len(K)-1])-val[len(K)-2])
    #print(len(K)-2)
    #print(K[len(K)-1].index(63))
    return K[len(val)][W]

def custominp():
    try:
        #val2 = [1, 2, 5, 6]
        val2 = list(map(int, input("\nEnter values respectively: ").split()))
        wt2 = list(map(int, input("\nEnter weight of values respectively: ").split()))
        #W2 = 8
        W2 = int(input("\nEnter total weight: "))
        print('\nTotal value =', knappy(W2,wt2,val2))
    except:
        print("\nThere's been an error please try again")
        custominp()

val = [
    0,7,1,6,18,22,28
]
wt = [
    0,2,3,2,9,3,2
]
W = 11

        
print ('-'*87 +"\n|| " + '*'*81 + " ||\n|| " + '*'*22 + " Ultimate Dynamic Knapsack Solver! " + '*'*24 + " || \n|| " + '*'*81 + " ||\n" + '-'*87 + "\n")


if input("Please enter 1 if you would like to use default values or any other value, if otherwise:\n") == str(1):
    print('\nTotal value =', knappy(W,wt,val))
else:
    print(custominp())