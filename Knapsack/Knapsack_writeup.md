# Knapsack 0-1

## Mock Problem
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item, In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines. The first line consists of N the number of items. The second line consists of W, the maximum capacity of the knapsack. In the next  line are N space separated positive integers denoting the values of the N items and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.


Output:

Print the maximum possible value you can get with the given conditions that you can obtain for each test case in a new line.


Constraints:

1≤T≤100

1≤N≤100

1≤W≤100

1≤wt[i]≤100

1≤v[i]≤100


Example:

Input: <br>
1 <br>
3 <br>
4 <br>
1 2 3 <br>
4 5 1 <br>
Output: <br>
3

## The Solution

#### Dynamic Programming/ Build a Grid

We start off by sorting the items by weight. The start building a grid with the weights descending on the Y-axis and the weight from 0-W on the X-axis
<table>
<tr>
<td>Weight -></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td>
</tr>
<tr>
<td>Items(v, w)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td>
</tr>
<tr>
<td>3, 1</td></td><td></td><td></td><td></td><td></td><td></td>
</tr>
<tr>
<td>1, 4</td></td><td></td><td></td><td></td><td></td><td></td>
</tr>
<tr>
<td>2, 5</td></td><td></td><td></td><td></td><td></td><td></td>
</tr>
</table>

Then we start with the first weight, 0 and the first item, (3,1). How many of this item can we fit into a bag with max weight 0? None. This is the obvious result regards of the item combination </br>
So we will go ahead and populate the table

<table>
<tr>
<td>Weight -></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td>
</tr>
<tr>
<td>Items(v, w)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td>
</tr>
<tr>
<td>3, 1</td></td><td>0</td><td></td><td></td><td></td><td></td>
</tr>
<tr>
<td>1, 4</td></td><td>0</td><td></td><td></td><td></td><td></td>
</tr>
<tr>
<td>2, 5</td></td><td>0</td><td></td><td></td><td></td><td></td>
</tr>
</table>

Next iteration. We move to a weight of 1. We can add the item of 1. Here we need to ask ourselves if adding this item is will increase our value more than ignoring it. <br>
In this case yes it will. We do this for the rest of the weights and the first item resulting in:

<table>
<tr>
<td>Weight -></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td>
</tr>
<tr>
<td>Items(v, w)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td>
</tr>
<tr>
<td>3, 1</td></td><td>0</td><td>3</td><td>3</td><td>3</td><td>3</td>
</tr>
<tr>
<td>1, 4</td></td><td>0</td><td></td><td></td><td></td><td></td>
</tr>
<tr>
<td>2, 5</td></td><td>0</td><td></td><td></td><td></td><td></td>
</tr>
</table>

Now for item number 2. With a weight of 1, we perform a max of the value we can get with the current item, + the max value we can get with our current items weight minus the total weight, and </br>
the value we get if we don't use this item. So in this case we would get max(3, 3). Because we can't include our item so we default to the highest without our item which is the one directly above.

But, for example we had a max weight of 7 and our item was (2,4), then we would be maxing (2 + max_value_of_weight_3) and the maximum value without including the (2,4) item which is simply <br>
moving up one on the grid.

Back to our main example, we cannot use our item until a weight of 4. So we populate the grid:
<table>
<tr>
<td>Weight -></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td>
</tr>
<tr>
<td>Items(v, w)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td>
</tr>
<tr>
<td>3, 1</td></td><td>0</td><td>3</td><td>3</td><td>3</td><td>3</td>
</tr>
<tr>
<td>1, 4</td></td><td>0</td><td>3</td><td>3</td><td>3</td><td></td>
</tr>
<tr>
<td>2, 5</td></td><td>0</td><td></td><td></td><td></td><td></td>
</tr>
</table>

Now with a weight of 4 and our current item is the (1,4). We max a value of 1 + max_value_of_weight_0 (because 4-0 is 0) and the value without using that item, which is 3. <br>
Again we populate.

<table>
<tr>
<td>Weight -></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td>
</tr>
<tr>
<td>Items(v, w)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td>
</tr>
<tr>
<td>3, 1</td></td><td>0</td><td>3</td><td>3</td><td>3</td><td>3</td>
</tr>
<tr>
<td>1, 4</td></td><td>0</td><td>3</td><td>3</td><td>3</td><td>3</td>
</tr>
<tr>
<td>2, 5</td></td><td>0</td><td></td><td></td><td></td><td></td>
</tr>
</table>

Now for (2,5) it is fairly apparent that a weight of 5 will not fit so we will just populate

<table>
<tr>
<td>Weight -></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td>
</tr>
<tr>
<td>Items(v, w)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td>
</tr>
<tr>
<td>3, 1</td></td><td>0</td><td>3</td><td>3</td><td>3</td><td>3</td>
</tr>
<tr>
<td>1, 4</td></td><td>0</td><td>3</td><td>3</td><td>3</td><td>3</td>
</tr>
<tr>
<td>2, 5</td></td><td>0</td><td>3</td><td>3</td><td>3</td><td>3</td>
</tr>
</table>

A much more varied value example can be found here: <a href='https://www.youtube.com/watch?v=8LusJS5-AGo' target='_blank' >https://www.youtube.com/watch?v=8LusJS5-AGo</a>

## C++ Implementation

```c++
/* A Naive recursive implementation of 0-1 Knapsack problem */
#include<stdio.h>

// A utility function that returns maximum of two integers
int max(int a, int b) { return (a > b)? a : b; }

// Returns the maximum value that can be put in a knapsack of capacity W
int knapSack(int W, int wt[], int val[], int n)
{
   // Base Case
   if (n == 0 || W == 0)
       return 0;

   // If weight of the nth item is more than Knapsack capacity W, then
   // this item cannot be included in the optimal solution
   if (wt[n-1] > W)
       return knapSack(W, wt, val, n-1);

   // Return the maximum of two cases:
   // (1) nth item included
   // (2) not included
   else return max( val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                    knapSack(W, wt, val, n-1)
                  );
}

// Driver program to test above function
int main()
{
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int  W = 50;
    int n = sizeof(val)/sizeof(val[0]);
    printf("%d", knapSack(W, wt, val, n));
    return 0;
}
```

## Python Implementation

```Python
#A naive recursive implementation of 0-1 Knapsack Problem

# Returns the maximum value that can be put in a knapsack of
# capacity W
def knapSack(W , wt , val , n):

    # Base Case
    if n == 0 or W == 0 :
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
                   knapSack(W , wt , val , n-1))

# end of function knapSack

# To test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapSack(W , wt , val , n)

```
