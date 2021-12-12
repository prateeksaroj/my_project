def selection_sort(input):
   for i in range(len(input)):
      min = i
      for j in range( i+1, len(input)):
         if input[j] < input[min]:
            min = j
# Swap the minimum value with the compared value
   #input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
      if(min!=i):
         {
            swap(input[i],input[min])
         }

'''
def print_sorted_element(l):
   for i in range(len(l)):
      print("%d" %l[i])
'''






def swap(x,y):
   temp=x
   x=y
   y=temp

l = [19, 2, 31, 45, 30, 11, 121, 27]
selection_sort(l)
print(l)

