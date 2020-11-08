#  Bubble Sort
#  Sorts an array of numbers in ascending order.
#  Input Sequence a[1], a[2],...a[n]
#  Output Sequence is in ascending order
#
#  a := [1,5,7,8,]
#
#  For i: = 0 to n - 1
#  For j:= i + 1 to n
#       swapped := False
#       if (a[j] < a[i])
#           temp := a[i]
#           a[i] := a[j]
#           a[j] := temp
#       End-If
#  End-For
#  End-For

# Worst Case Complexity O(n^2)
# Best Case Complexity  O(n^2)
# Average Case Complexity O(n^2)



def bubblesort(sequence):
    for i, num in enumerate(sequence):
        for j in range(i+1,len(sequence)):
            if sequence[j] < sequence[i]:
                temp = sequence[i]
                sequence[i] = sequence[j]
                sequence[j] = temp
