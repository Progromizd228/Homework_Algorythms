# Мы перебираем строку S (камни) один раз, поэтому временная сложность - O(n).

class Solution:
    def numJewelsInStones(self, J, S):
        return sum(x in J for x in S) # Находим и возвращаем сумму элементов списка J в списке S.


ans = Solution()
print (ans.numJewelsInStones("aA", "aAAbbbb"))
print (ans.numJewelsInStones("z", "ZZ"))