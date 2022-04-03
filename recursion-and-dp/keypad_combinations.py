"""
Given a string keys that contains the keys that we pressed in a phone keypad,
create a function that returns all the possible combinations of characters that can be made.
Keypad keys and the characters that they can make:

0: +, 1: . , 2: ABC, 3: DEF, 4: GHI, 5: JKL, 6: MNO, 7: PQRS, 8: TUV, 9: WXYZ
"""


"""
0: [+]
1: [.]
2: [A,B,C]
3: [D,E,F]
...

Lets create a hashmap to map the keys to the values.

Input: "29"

Given an input, we need to create all possibilities.

      ""
     /              \  \
    A               B  C  3
  /  \  \  \       /
 W    X  Y Z      W X..   4*3

For each digit we have to try all possible ways.

Base case:
- position > len(keys): add the path and return

Recursive Step:
- Start with an empty string -> empty list
- For each possible character of digit, add the character to a possible path
- Recursively go down the tree
- When we have gone through all digits we append the current path to our result
- Pop the last element from the path

Since we have a maximum of 4 characters for every digit.

Time Complexity: O(4^n) being n the number of keys
Space Complexity: O(n) because we go down a tree the length of keys

Since we have to find all possible ways, we cannot do better than this.

"""


def keypadCombinations(keys):
    key_to_char = {
        "0": ["+"],
        "1": ["."],
        "2": ["A", "B", "C"],
        "3": ["D", "E", "F"],
        "4": ["G", "H", "I"],
        "5": ["J", "K", "L"],
        "6": ["M", "N", "O"],
        "7": ["P", "Q", "R", "S"],
        "8": ["T", "U", "V"],
        "9": ["W", "X", "Y", "Z"],
    }

    result = []

    def getAllPossibleCombs(keys, pos, current_path):
        if pos == len(keys):
            result.append("".join(current_path))  # O(n)
            return

        current_key = keys[pos]
        for char in key_to_char[current_key]:  # 4
            current_path.append(char)  # 1
            getAllPossibleCombs(keys, pos + 1, current_path)  # T(n-1)
            current_path.pop()  # 1

    getAllPossibleCombs(keys, 0, [])
    return result


"""
Complexity Analysis

T(0) = n

T(n) = 4( T(n-1) + 2 )
T(n) = 4T(n-1) + 8
     = 4( 4T(n-2) + 8 ) + 8
     = 4^2*T(n-2) + 4*8 + 8
     = 4^2*(4T(n-3) + 8) + 4*8 + 8
     = 4^3*T(n-3) + 8*4^2 + 8* 4 + 8
     = 4^k*T(n-k) + 8*4^(k-1) + 8*4^(k-2) + 8^(k-3) .. + 8
     = 4^n*T(0) + 8*4^(n-1) + ... + 8
     = 4^n*n + 8^4....
     = O(n*4^n)
"""
