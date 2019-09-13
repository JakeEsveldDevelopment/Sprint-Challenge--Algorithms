#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n) - This will be linear time because it is adding the square of the input to a counter until the counter is equal to the cube of an input. This will always count for n number of loops.


b)O(log(n)) - This will be the mathematical equivalent of a binary search. The funciton is multiplying the baseline by 2 every time it iterates. This will make it scale very quickly for large numbers. This will also make the computation time n to the square root of 2 which is what log2(n) is.


edit: O(nLog(n)

c)O(nLog(n)) - This will loop as many times as the input has value, but this will also do some extra computation in passing the variables back up the stack. This is the baseline complexity for most recursive methods. Will loops n times and then return back up the stack to return in the original.

edit: O(n)

## Exercise II

This would be the perfect problem to use a binary search. You would start halfway up the building, and throw an egg off. If the egg breaks, then you treat that as the top of the building and go to the middle again. If the egg doesn't break, you treat that as the bottom of the building and go to the middle of the top half. You continue this process with each step, going down if it breaks, or going up if it doesn't break. You will eventually find the spot that represents f. The complexity for this would be O(log(n)) because it would take n to the square root of 2 amount of times to find the answer no matter the size of the input.

psuedocode:

def findF(building, breakingEdge):
    middle = building // 2
    if middle == breakingEdge:
        return middle
    elif middle > breakingEdge:
        findF(building[:middle], breakingEdge)
    else:
        findF(building[middle:], breakingEdge)


