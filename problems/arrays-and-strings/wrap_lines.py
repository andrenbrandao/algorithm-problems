"""
 Connecting words with '-' as blank spaces, no exceeds maxLength                                                          i

 input: ["1p3acres", "is", "a", "good", "place", "to", "communicate"], 12
 output: {"1p3acres-is", "a-good-place", "to", "communicate"}



-- Algorithm --

string_builder = "1p3acres"
result = []

- Iterate over the words
- If we don't have any words, add it to our builder
- Otherwise, if len(string_builder)+1+len(new_word) <= maxLength, we add
the new word with a dash.
- Else, in the case we cannot add the new word, we save the current builder
in our result
and add the word to the new builder
- When we reach the last word, we might have a string builder left, so
we have to remember to add what is left in the result in case its length
is not zero

Time Complexity: O(n)
Space Complexity: O(n)
"""


def wrap_lines(words, max_length):
    result = []
    string_builder = ""

    for word in words:
        if len(string_builder) == 0:
            string_builder = word
        elif len(string_builder) + 1 + len(word) <= max_length:
            string_builder += "-" + word
        else:
            result.append(string_builder)
            string_builder = word

    if len(string_builder) != 0:
        result.append(string_builder)

    return result


def test(words, max_length, expected_answer):
    answer = wrap_lines(words, max_length)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


test(
    ["1p3acres", "is", "a", "good", "place", "to", "communicate"],
    12,
    ["1p3acres-is", "a-good-place", "to", "communicate"],
)
print("All tests passed!")
