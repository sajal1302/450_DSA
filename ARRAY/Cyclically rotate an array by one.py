def rotate( arr, n):
    
    b=[]
    b.append(arr[n-1])
    
    for i in range(n-1):
        b.append(arr[i])
     
    
    for i in range(n):
        arr[i]=b[i]