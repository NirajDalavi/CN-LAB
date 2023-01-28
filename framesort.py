class Frame:
    def __init__(self,num,data):
        self.frameNo = num
        self.data = data
    def __str__(self):
        return f"{self.frameNo}{self.data}"

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L=[]
    R=[]
    for i in range(0, n1):
            L.append( arr[l + i])
 
    for j in range(0, n2):
            R.append(arr[m + 1 + j])
 
    i = 0    
    j = 0    
    k = l   

    while i < n1 and j < n2:
        if L[i].frameNo <= R[j].frameNo:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

 
def mergeSort(arr, l, r):
    if l < r:
 
        m = l+(r-l)//2
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


if __name__ == "__main__":
    n=int(input("Enter the no of frames: "))
    frames=[]
    print("Enter frames no and data: ")
    for i in range(n):
        nums,data = input().split()
        nums = int(nums)
        frames.append(Frame(nums,data))
    print()
    print("Frames after sorting: ")
    mergeSort(frames,0,n-1)
    for i in frames:
        print(i.frameNo, i.data)
