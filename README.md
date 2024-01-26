**Problem**: Write a function to check if a given array is sorted in ascending order.
**Solution:**
  1. Started by going through each element of the array.
  2. Compared each element with its adjacent one.
  3. Checked if the current element is less than or equal to the next one.
  4. While iterating, found if an element greater than the next one, it indicates a break in ascending order.Kept track of this condition during the iteration.
  5. After iterating through all elements, checked the tracking variable. If it remains in the initial state (indicating no break in ascending order), the array is sorted.
  6. Otherwise, there was a break, and the array is not sorted.
