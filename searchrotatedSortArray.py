'''
search O(logn) => binary Search 
- > known that the array is sorted but rotated 

l  r => l < target < r 

[ 4, 5, 6, 7, 0, 1, 2 ]
[ less | mid | greater Equal ]
target is 5 


'''

def binarySearch(arr , l , r, target):
    while (l < r):
        mid  = l +(r - l)/2 
        
        if arr[mid ] == target: 
            return mid
        
        if arr[mid ] > target:
            r = mid 
        
        if arr[mid ] < target:
            l = mid 
    
    return -1

def searchRotatedSortedArray(arr , target ): 
    l , r  , start , index = 0 , len(arr)-1 , 0 , -1
    while( l < r ):
        mid = l +(r - l)/2
        if arr[mid] > arr[r]:
            l = mid + 1
        else:
            r = mid
    start = r
    
    l , r = 0 , len(arr) - 1
    if (target >=  arr[start]  and target < arr[r]):
        l = start 
    else:
        r = start
    print(l,r)
    return binarySearch(arr , l , r , target)

    # print(mid)


    # return index


testcase , target  = [ 4,5,6,7, 0 , 1 ,2 ] , 0


print("Expected %d and solution %d"%( 
    4, searchRotatedSortedArray(testcase , 0)))
print("Expected %d and solution %d"%( 
    -1, searchRotatedSortedArray(testcase , 3)))

