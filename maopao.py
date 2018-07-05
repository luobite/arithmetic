def bubble_sort(n):
    for i in range(len(n)-1):
        counte=0
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
                counte+=1
        if 0==counte:
            return
if __name__ == "__main__":
    list=[1,3,2,4,6,5,0,9,7]
    bubble_sort(list)
    print list
