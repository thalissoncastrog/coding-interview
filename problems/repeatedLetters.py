def repeatedLetters(word):
    wordset = set(word);

    return len(word) != len(wordset);

# Time complexity: O(n)
# Space complexity: O(n)

# Test cases
# Test case 1

result = repeatedLetters("hello");
print(result);

result = repeatedLetters("helo");
print(result);

