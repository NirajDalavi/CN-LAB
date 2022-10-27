n=int(input("Enter the number of frames: "))
frames=[]
print("Enter frame number and data(for): ")
for i in range(n):
    nums,data=input().split(" ")
    nums=int(nums)
    frames.append([nums,data])
frames.sort()
print(frames)
