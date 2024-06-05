class Solution(object):
    def commonChars(self, words):
        return reduce(lambda a, b: a & b, map(Counter, words)).elements()