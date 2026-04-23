class Solution:
    def findTwoElement(self, arr):
        new_set = set()
        length = len(arr)
        new_array = list()
        for i in arr:
            if i not in new_set:
                new_set.add(i)
            else:
                new_array.append(i)
                
        for j in range(1, length+1):
            if j not in new_set:
                new_array.append(j)
            
        return new_array
        
                

