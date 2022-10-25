# Сложность - O(N logN)

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        d = {}
        m = 10**20                      # Объявляем минимум как бесконечность.
        arr.sort()                      # Сортируем список в порядке возрастания.

        for i in range(1, len(arr)):    # Проходимся циклом по элементам массива.
            dif = abs(arr[i]-arr[i-1])  # Считаем модуль разницы двух элементов.
            m = min(m, dif)             # Считаем минимальную разницу. Поскольку по умолчанию m = бесконечность, первая разница будет минимальной.
            if dif in d:                # Добавляем пары элементов в новый массив.
                d[dif].append([arr[i-1],arr[i]])
            else:
                d[dif] = [[arr[i-1],arr[i]]]     
        
        return d[m]                     # Возвращаем массив только тех элементов, у которых модуль разницы равен значению минимальной разницы после всех итераций прохождения по массиву.

ans = Solution()
print (ans.minimumAbsDifference([4,2,1,3]))
print (ans.minimumAbsDifference([1,3,6,10,15]))
print (ans.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))