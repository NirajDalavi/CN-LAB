class Frame:
    def __init__(self, num, data):
        self.frameNo = num
        self.data = data
    def __str__(self):
        return f"{self.frameNo} {self.data}"
def sort(frames):
    for j in range(len(frames)-1):
        for i in range(len(frames)-j-1):
            if frames[i].frameNo > frames[i+1].frameNo:
                frames[i] ,frames[i+1] = frames[i+1] ,frames[i]


if __name__=="__main__":
    n=int(input("Enter the number of frames: "))
    frames=[]
    print("Enter frame number and data(for): ")
    for i in range(n):
        nums,data=input().split(" ")
        nums=int(nums)
        frames.append(Frame(nums,data))
    sort(frames)
    print()
    print("Frames after sorting:")
    for i in frames:
        print(i)
