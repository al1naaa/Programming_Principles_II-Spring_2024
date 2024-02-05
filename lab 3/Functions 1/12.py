def his(arr):
    for i in range(len(arr)):
        print(arr[i]*'*')
    
his(list(map(int, input().split())))