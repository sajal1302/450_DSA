class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        a=[]
        b=[]
        c=[]
        for i in arr:
            if i > 0:
                a.append(i)
            else:
                b.append(i)
        
        a.extend(b)    
        for i in range(n):
            arr[i]=a[i]
            
        return arr