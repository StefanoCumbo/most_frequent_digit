"""

You are working with data collected from various sensors. Given an array of nonnegative integers readings representing the sensor readings,
 transform the array by repeatedly replacing each element with the sum of its digits. 
 Continue this transformation until every element is a single digit. Return the most occurring digit in the final array. 
 In case of a tie, return the highest digit.

Note: You are not expected to provide the most optimal solution,
 but a solution with time complexity not worse than O(readings. length?) will fit within the execution time limit.



Example

For readings = [123, 456, 789, 101] , the output should be
solution (readings) = 6
Explanation:
15
16
17
• The sum of digits for
123
is 1 + 2
• The sum of digits for 456 is 4 + 5 +
10 1 + 5 = 6
and further

"""

class Solution:
    def mostFrequentDigit(self, readings):

    



def test_solution():
    sol = Solution()

    # Example test case
    readings = [123, 456, 789, 101]
    assert sol.mostFrequentDigit(readings) == 6, "Test 1 failed"

    # Single element
    readings = [999]
    assert sol.mostFrequentDigit(readings) == 9, "Test 2 failed"

    # All reduce to same digit
    readings = [12, 21, 30]  # -> [3,3,3]
    assert sol.mostFrequentDigit(readings) == 3, "Test 3 failed"

    # All reduce to 1
    readings = [19, 28, 55, 46]  # -> [1,1,1,1]
    assert sol.mostFrequentDigit(readings) == 1, "Test 4 failed"

    # All reduce to 2
    readings = [29, 38, 47, 56]  # -> [2,2,2,2]
    assert sol.mostFrequentDigit(readings) == 2, "Test 5 failed"

    # Mixed digits with clear winner
    readings = [123, 456, 789, 111]  # -> [6,6,6,3]
    assert sol.mostFrequentDigit(readings) == 6, "Test 6 failed"

    print("✅ All tests passed!")

if __name__ == "__main__":
    test_solution()


