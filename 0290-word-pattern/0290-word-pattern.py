class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter in pattern_to_word:
                if pattern_to_word[letter] != word:
                    return False

            if word in word_to_pattern:
                if word_to_pattern[word] != letter:
                    return False

            pattern_to_word[letter] = word
            word_to_pattern[word] = letter

        return True