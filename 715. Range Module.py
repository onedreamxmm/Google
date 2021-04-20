'''
A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).
Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
Note:

A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.

'''

'''
bisect.bisect_left(a, x, lo=0, hi=len(a))
Locate the insertion point for x in a to maintain sorted order. The parameters lo and hi may be used to specify a subset of the list which should be considered; by default the entire list is used. If x is already present in a, the insertion point will be before (to the left of) any existing entries. The return value is suitable for use as the first parameter to list.insert() assuming that a is already sorted.

The returned insertion point i partitions the array a into two halves so that all(val < x for val in a[lo:i]) for the left side and all(val >= x for val in a[i:hi]) for the right side.

bisect.bisect_right(a, x, lo=0, hi=len(a))
bisect.bisect(a, x, lo=0, hi=len(a))
Similar to bisect_left(), but returns an insertion point which comes after (to the right of) any existing entries of x in a.

The returned insertion point i partitions the array a into two halves so that all(val <= x for val in a[lo:i]) for the left side and all(val > x for val in a[i:hi]) for the right side.
'''

from bisect import bisect_left as bl, bisect_right as br

class RangeModule:
    def __init__(self):
        self.track = []

    def addRange(self, left, right):
        i, j = bl(self.track, left), br(self.track, right)
        self.track[i:j] = [left]*(i%2 == 0) + [right]*(j%2 == 0)

    def queryRange(self, left, right):
        i, j = br(self.track, left), bl(self.track, right)
        return i == j and i%2 == 1

    def removeRange(self, left, right):
        i, j = bl(self.track, left), br(self.track, right)
        self.track[i:j] = [left]*(i%2 == 1) + [right]*(j%2 == 1)

'''
Explanation of this algorithm
Typically problems like these require us to use a data structure like TreeMap (from Java) but for those of us using python, there is no such inbuilt data structure. And looking at this top solution in python, I was very confused as to how that works.

I'll try to explain how the algorithm works. The only thing we should understand clearly before understanding this solution is how bisect_left and bisect_right work in python. bisect_left gives the position of the first index where the element can be inserted and bisect_right gives the position of the last index where the element can be inserted. Note that if the item we are trying to search for is not present in the array, both bisect_left and bisect_right will return the same result.
eg : bl([1,2,3], 2) ==> 1 whereas br([1,2,3], 2) ==> 2
but for bl([1,2,4], 3) ==> 2 and br([1,2,4], 3) ==> 2

Now coming to the problem at hand, we internally represent the covered ranges by a single array _X. Think of this as a number line in which the even elements represent the beginning of a range and odd elements represent the end of the range. By definition of the range, we should maintain even number of elements in the array _X.

For e.g : _X = [10, 15, 20, 25] means the covered ranges are [10, 15) and [20, 25)

AddRange
If we want to add a range i.e addRange, we look at the bisect_left of left on the array and bisect_right of right on _X. We need to do this because the opening of the range (i.e left) has to preceed any other range which is closing at the same point. Similarly for the closing of the range i.e right, we have to keep in mind any other ranges opening at that point.

In the example above of _X = [10, 15, 20, 25], lets say if we want to add a range [14, 22), then at the end of the function, _X should look as follows [10, 25]..

For this to happen, we rely on i = bisect_left(...) and j=bisect_right(...).

What does it mean if i is odd ? If i is odd, that means that preceding element is an even element and the opening of the range is part of some other range. Similarly if j is odd, that also means if it is part of some other range and we need not create a new entry for it.

Next, what does it mean if i ie even ? This means that this point is not covered by any existing range and we have to create a new entry for it. Similar thing holds true for j (for j it would mean that we would have overwrite an exiting range).

The only other thing we have to pay attention to is to collapse all the other intermediate values of opening and closing points in the new interval. We accomplish this by collapsing the array self._X[i:j] = ...

RemoveRange
The intuition behind removeRange is similar to addRange, but the only difference is we have to perform the operation when i and j are odd instead of even. This is because while removing, if i is even, this means that it is not covered by any existing range and we need not perform any action (except possibly collapsing the ranges). Similar logic holds truee for j as well.

QueryRange
While querying for a range, we similarly get i and j values and we check for two conditions.

(i) Both i and j are same. i.e there is no range boundary in between left and right. if there is a range boundary, that means atleast some part of the range is not covered.
(ii) They should be odd. This means that a range has been opened by a preceeding even element and yet to be closed by the element at the i (or j)'th position.

If both (i) and (ii) are met, then we can say that the range is completely covered.

We do bisect_right(self._X, left) (and similarly bisect_left(self._X, right))because we want to be as conservative as we can.

For e.g if _X = [10,15], and we are querying for say [15, 20), then bisect_left(_X, left) would give us 1 . Which means that there is some part of the interval covered. but 15 is not covered in the range.

Time Complexity
We see that in addRange and removeRange, we are rewriting the array partially (can potentially rewrite the entire array). So their Time Complexity is O(n). For queryRange, the time complexity is O(logn) as the only thing we are doing is binary searches.

SpaceComplexity
O(n) for storing 2n points of the range.
'''