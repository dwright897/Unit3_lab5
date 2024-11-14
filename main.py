# Dalton Wright
# 11/13/24
# Bubble sort

def bubble_sort(unsorted_list):
  length = len(unsorted_list)
  for i in range(length-1):
    swaped = False
    for num in range(length -i -1):
      if unsorted_list[num] > unsorted_list[num+1]:
        unsorted_list[num], unsorted_list[num+1] = unsorted_list[num+1], unsorted_list[num]
        swaped = True
    if not swaped:
      break
  return unsorted_list

def main():
  unsorted_list = [50, 7, 2, 122, 12, 51, 9, 11, 3]

  print(f"Unsorted array: {unsorted_list}")
  sorted_list = bubble_sort(unsorted_list)
  
  print (f"Sorted array: {sorted_list}")

if __name__=="__main__":
  main()