# handson_4
# Problem_0:

The function call stack for fib(5) is fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1) -> fib(0) -> fib(1) -> fib(2) -> fib(1) -> fib(0) -> fib(3) -> fib(2) -> fib(1) -> fib(0) -> fib(1) . 

Meaning fib(5) calls fib(4),fib(3)

fib(4) calls fib(3) and fib(2)

fib(3) calls fib(2) and fib(1)

fib(2) calls fib(1) and fib(0)

fib(1) returns 1

fib(0) returns 0

fib(2)= fib(1) + fib(0) = 1+0=1

fib(3) = fib(2) + fib(1) = 1+1=2

fib(4) = fib(3) + fib(2) = 2 +1 =3

fib(5) = fib(4) + fib(3) = 3+2 = 5

# Problem_1:

Time Complexity:

for the given problem first given k array are merged into a single array the run time for that is 0(K) then  merge sort is used so the run time of the merge sort is O(mlogm), where m=K*N given K sorted arrays of size N each
Time complexity = O(k)+O(mlogm) 
from the above equation the time complexity of the problem is O(NlogN)

Way's to improve :

Use Insertion Sort for Small Subarrays: Instead of continuing to split the array until it's down to single elements, you can stop the recursion when the subarray size is below a certain threshold (commonly between 5 to 15 elements) and switch to a different sorting algorithm like insertion sort. Insertion sort is efficient for small arrays and has a lower overhead compared to merge sort for such sizes.

Optimize Merging Step: During the merge step, you can optimize the process by checking if the last element of the left subarray is smaller than or equal to the first element of the right subarray. If this condition is true, you can skip the merge process because the arrays are already in sorted order.

# Problem_2:

Time Complexity:

for the given problem first a pointer will be iterated over the given array (it takes N amount of time) then it is checked wether the pointer is not in the array "res"(it takes N amount of time)
Time complexity= O(N*N)=O(N^2)

Way's to improve:

Use a Dictionary: You can use a dictionary to track the occurrences of each element in the array. This approach avoids iterating through the entire list for each element and can be more efficient.

Use a Set: Instead of using a list res to store unique elements, you can use a set. Sets in Python have an average time complexity of O(1) for membership tests, which can significantly improve the performance, especially for larger arrays.

