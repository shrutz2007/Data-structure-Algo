def SelectionSort(list1):
    index_len=range(0,len(list1)-1)
    for i in index_len:
        min=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[min]:
                min=j
            if min!=i:
                list1[min],list1[i]=list1[i],list1[min]
    return list1
list1=list(map(int,input().split( )))
print(SelectionSort(list1))