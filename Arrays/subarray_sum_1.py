'''
Given an unsorted array of non-negative integers
find a contiguous subarray which adds to a given number.

'''

def sub_sum(arr,sum):
    n   = len(arr)
    import pdb;pdb.set_trace()
    start = 0

    curr_sum = arr[0]
    
    for i in range(1,n):

        if curr_sum > sum and start < i-1:
            curr_sum  = curr_sum - arr[start]

            start +=1

        if curr_sum == sum:
            print(f"contiguous subarray is {arr[start:i]}")
            return
        if i<n:
            curr_sum  = curr_sum + arr[i]

    print("no subrrays found")
    return

arr = [15, 2, 4, 8, 9, 5, 10] 
sum = 23

print(sub_sum(arr,sum))

