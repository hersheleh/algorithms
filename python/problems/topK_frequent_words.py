from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = {}
        for word in words:
            if word_freq.get(word) is None:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
        sorted_words = sorted(word_freq, reverse=True)
        k_subset = sorted_words[:k]
        return k_subset


if __name__ == '__main__':
    S = Solution()

    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(S.topKFrequent(words, k))
