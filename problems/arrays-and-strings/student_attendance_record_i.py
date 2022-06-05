"""
LeetCode 551. Student Attendance Record I
https://leetcode.com/problems/student-attendance-record-i/
"""

"""
Student is NOT eligible if:

- Has 2 or more 'A' absent days
- Has 3 or more consecutive "L" late days

Algorithm:

- Iterate over the string
- Keep count of "A"s. If it is greater than or equal to 2, return False
- When an "L" is found, keep counting the consecutive L. If we count 3, return False.
If we find another letter, set the L count to 0.
- Return true if the rules above are not met.

Time Complexity: O(n)
Space Complexity: O(1)


       i
PPALLPLA

absent_days = 1
late_consecutive_days = 1

i
LALL
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_days = 0
        late_consecutive_days = 0

        for day in s:
            if day == "A":
                absent_days += 1

                if absent_days >= 2:
                    return False

            if day == "L":
                late_consecutive_days += 1

                if late_consecutive_days >= 3:
                    return False

            else:
                late_consecutive_days = 0

        return True
