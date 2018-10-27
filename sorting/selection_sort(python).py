'''
Selection Sort
'''

def selectionSort(list):
   for iterator in range(len(list)-1,0,-1):
       max=0
       for position in range(1,iterator+1):
           if list[position]>list[max]:
               max = position

       temp = list[iterator]
       list[iterator] = list[max]
       list[max] = temp

list = [14,46,43,27,57,41,45,21,70]
selectionSort(list)
print(list)