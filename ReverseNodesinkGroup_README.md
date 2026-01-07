Reverse Nodes in k-Group – Explanation

This solution reverses a singly linked list in groups of size k, modifying only the node pointers and not the values. 
If the number of remaining nodes at the end of the list is less than k, those nodes are left unchanged. 
The algorithm works in-place and uses constant extra space.

The approach begins by creating a dummy node that points to the head of the list. 
This dummy node simplifies edge cases, especially when the first group of nodes needs to be reversed. 
A pointer called group_prev is used to track the node just before the current group of k nodes.

The algorithm runs in a loop, processing one group at a time. 
For each iteration, it first checks whether there are at least k nodes remaining in the list. 
This is done by moving a pointer forward k times from group_prev. 
If at any point the pointer becomes null, it means fewer than k nodes remain, and the algorithm stops, returning the modified list.

Once a valid group of k nodes is confirmed, the algorithm stores the node immediately after the group. 
This node marks where the reversed group should reconnect to the rest of the list.

The reversal is then performed using three pointers. 
The current pointer starts at the first node of the group, and a previous pointer starts at the node following the group. 
Each node in the group has its next pointer redirected to the previous node, effectively reversing the direction of the links. 
This continues until all k nodes in the group are reversed.

After the reversal is complete, the algorithm reconnects the reversed group back into the list. 
The node before the group is linked to the new head of the reversed group, and the pointer tracking the previous group is moved to the end of the reversed section. 
This prepares the algorithm to process the next group of k nodes.

This process repeats until the entire list has been processed. 
The final result is a linked list where nodes are reversed in groups of k, achieved in linear time and constant extra space.
