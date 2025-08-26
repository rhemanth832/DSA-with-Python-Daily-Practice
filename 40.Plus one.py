class Solution(object):
    def plusone(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        return list(map(int, str(int(''.join(map(str, digits))) + 1)))

    #(OR)
def plusones(digits):
    return list(map(int, str(int("".join(map(str, digits)))+1)))
digits=[1, 4, 8]
print(plusones(digits))
