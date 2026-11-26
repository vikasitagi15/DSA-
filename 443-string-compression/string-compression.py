class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
       
        write = 0
        n = len(chars)
        i = 0

        while i < n:
            start = i

            while i + 1 < n and chars[i] == chars[i + 1]:
                i += 1

            count = i - start + 1

            chars[write] = chars[start]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            i += 1

        return write