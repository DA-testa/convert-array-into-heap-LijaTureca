# python3
import re

def build_heap(arr):
    n = len(arr)
    swaps = []
    for i in range(n//2, -1, -1):
        j = i
        while j < n:
            left = 2*j + 1
            right = 2*j + 2
            smallest = j
            if left < n and arr[left] < arr[smallest]:
                smallest = left
            if right < n and arr[right] < arr[smallest]:
                smallest = right
            if smallest != j:
                arr[j], arr[smallest] = arr[smallest], arr[j]
                swaps.append((j, smallest))
                
                j = smallest
            else:
                break
    return  len(swaps), swaps



def main():
    command=input()
    arr=[]
    if 'I' in command:
     o= int(input())
     for_arr=input()
     num=re.split(' ',for_arr)
     for x in num: 
        arr.append(int(x))
    

    
    if 'F' in command:
        file=input()
        name="tests/"+file
        if 'a' in file:
            print("wrong file name")
        else:
         with open(name,"r") as file:
                o=int(file.readline())
                lines=file.readlines()
                numbers=lines[1:]
                for numbers in lines:
                    num=re.split(' ',numbers)
                    for x in num:
                     arr.append(int(x))
    
                    
    num_swaps, swaps = build_heap(arr)

    print(num_swaps)
    print('\n'.join([f"{i} {j}" for i, j in swaps]))
    


if __name__ == "__main__":
    main()
