# Сложность алгоритма - O(logN), поскольку мы делим целое число на 2 всякий раз, когда получаем четное число.
# Затем каждое нечетное число преобразуется в четное путем добавления к нему единицы.
# Сложность алгоритма - логарифмическая.

class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0                 # Объявляем счётчик матчей.
        steps = 0               # Объявляем счётчик шагов.
        while n > 1:            # Выполняем цикл, пока не останется 1 команда.
            res += n // 2       # Увеличиваем счётчик матчей по формуле: количество команд / 2 (без остатка).
            if n % 2 == 0:      # Если кол-во команд чётное.
                print ('Round', steps+1,': Teams =', int(n), ', Matches =', int(n//2), ', and', int(n//2), 'teams advance.')
                n = n // 2
            else:               # Если кол-во команд нечётное.
                print ('Round', steps+1,': Teams =', int(n), ', Matches =', int(n//2), ', and', int(n//2+1), 'teams advance.')
                n = n // 2 + 1
            steps += 1
        return res

ans = Solution()

print(ans.numberOfMatches(7))
print(ans.numberOfMatches(14))