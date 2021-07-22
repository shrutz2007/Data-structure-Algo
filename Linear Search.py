# Linear Search Timecomplexity O(n)

def LinearSearch(list1,key):
    for i in range(len(list1)):
        if(key==list1[i]):
            print("Element found",i)
            break
    else:
        print("Element not found",i)
list1=[1,2,3,4,5,6]
key=int(input("Enter the key of element  : "))
LinearSearch(list1,key)