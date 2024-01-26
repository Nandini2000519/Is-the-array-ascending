arr = list(map(int, input().split()))  # taking the input list/array and storing it in 'arr'
count = []
for i in range(len(arr)-1):
    if(arr[i]>=arr[i+1]): # checking if the first element is smaller than the next element
        count.append(0)  # if the second element is smaller than the previous one '0' is added to 'count'
        
    else:
        count.append(1)  # if the first element is smaller than next then '1' is appended to 'count'
        

if all(x==1 for x in count): # checking if the 'count' list is all 1's i.e,. all the elements are in ascending
    print("True")
else:
    print("False")