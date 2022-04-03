"""
Given an array of arrays of words (List[List[str]]) arr, create a function that
returns all the possible phrases that can be made, a phrase is made by
concatenating one word from each array of arr, and separating them by spaces.

For example, if arr has 3 arrays, a phrase will be a word from arr[0] + a space
+ a word from arr[1] + a space + a word from arr[2].

Example 1:
input:  arr = [['I', 'You', 'They'], ['love', 'hate'], ['food', 'games']]
output: ['I love food', 'I love games', 'I hate food', 'I hate games',
'You love food', 'You love games', 'You hate food', 'You hate games', 'They love food',
'They love games', 'They hate food', 'They hate games']</p>
"""

"""
I You They
love hate
food games

            ""
      /         |  \
        I      You They  m words
   /        \
  love     hate          m^2 words
 /   \      /  \
food games food games    m^3 words


-- WRONG
Time Complexity: O(2^n) where n is the longest string
Space Complexity: O(height)
--
Time Complexity: O(m^n) where n is the height, m is the number of words in a row

Return all possible phrases.
So, we need to recursively form all phrases.

Base case:
- n == height: return

Recursive Step:
- Start with an empty list
- Choose one of the next words and add it to the list
- Repeat until we have reached the end of a tree
- Join the words and add them to the result

- Pop the elements from the tree when returning from the recursive step

"""


def phrases(arr):
    result = []
    height = len(arr)

    def helper(arr, currentWords, currentHeight):
        if currentHeight == height:
            result.append(" ".join(currentWords))
            return

        for word in arr[currentHeight]:
            currentWords.append(word)
            helper(arr, currentWords, currentHeight + 1)
            currentWords.pop()

    helper(arr, [], 0)
    return result
