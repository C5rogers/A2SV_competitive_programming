class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def get_signature(word):
            return ''.join(sorted(set(word)))

        signature_to_count = {}
        similar_pairs = 0

        for word in words:
            signature = get_signature(word)
            similar_pairs += signature_to_count.get(signature, 0)
            signature_to_count[signature] = signature_to_count.get(signature, 0) + 1

        return similar_pairs