How it works (short + useful explanation)

We use binary search on the smaller array.
We try to split both arrays into left and right halves such that:

left_max ≤ right_min across both arrays

once that condition holds, we found the correct partition

the median is either:

the max of the left side (if odd length), or

average of the max left and min right (if even)

This avoids merging—hence O(log(min(m,n))).
