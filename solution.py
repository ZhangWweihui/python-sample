class Solution:

    def is_valid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        middle = int(len(s) / 2)
        for i in range(0, middle):
            m = middle - i - 1
            n = middle + i
            flag = self.is_match(s, m, n)
            if flag is False:
                return False
        return True

    def is_match(self, s: str, m, n) -> bool:
        left = s[m:m + 1]
        right = s[n:n + 1]
        if (left == '(' and right == ')') \
                or (left == '[' and right == ']') \
                or (left == '{' and right == '}'):
            return True
        return False

    def is_valid2(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        middle = int(len(s) / 2)
        for i in range(0, middle):
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if len(s) == 0:
                return True
        return False

    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        middle = int(len(s) / 2)
        for i in range(0, middle + 1):
            if s[i:i + 1] != s[len(s) - 1 - i:len(s) - i]:
                return False
        return True

    def index_of(self, haystack: str, needle: str) -> int:
        if needle == '' or haystack == needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        flags = []
        for i,s in enumerate(haystack):
           if s == needle[0:1] and len(haystack)-i >= len(needle):
               flags.append(i)
        if len(flags) == 0:
            return -1
        for f in flags:
            if haystack[f:f+len(needle)] == needle:
                return f
        return -1


if __name__ == '__main__':
    # print('()[]{}'.replace('()', '').replace('[]', '').replace('{}', ''))
    # print(Solution().is_valid2('[](((([[[{()}]]])))){}()['))
    # print(Solution().is_palindrome(1234567654321))
    # for i,s in enumerate('abc'):
    #    print(i,s)
    print(Solution().index_of('abcersdgdsgdsgsdgfsdfgsdfg', 'gdsgd'))
