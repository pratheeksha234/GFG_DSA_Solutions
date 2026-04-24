class Solution:
	def minJumps(self, arr):
	    
	    # code here
	    n = len(arr)
	    if arr[0] == 0:
	        return -1
	    if n == 1:
	        return 0
	    jumps = 1
	    current_end = arr[0]
	    farthest = arr[0]
	    for i in range(1, n):
	        if current_end>= n - 1:
                return jumps
	        farthest = max(farthest, i + arr[i])
	        if i>farthest:
	                return -1
	        if i == current_end:
	            jumps+=1
	            current_end = farthest
	            if current_end >= len(arr)-1:
	                return jumps
	    return -1
