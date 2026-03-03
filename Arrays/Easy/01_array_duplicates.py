class Solution:
    def findDuplicates(self, arr):
        # code here
        seen = set()
        duplicates = list()
        
        for i in arr:
            if i in seen:
                duplicates.append(i)
            else:
                seen.add(i)
        return duplicates
                
                

                
        
