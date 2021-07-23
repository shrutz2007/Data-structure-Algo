def BubbleSort(list1):
    index=len(list1)-1
    sorted=False
    while not sorted:
        sorted=True
        for i in range(0,index):
            if list1[i]>list1[i+1]:
                sorted=False
                list1[i],list1[i+1]=list1[i+1],list1[i]
    return list1
list1=list(map(int,input("Enter the list : ").split()))
print(BubbleSort(list1))