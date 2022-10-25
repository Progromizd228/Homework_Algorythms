# Сложность алгоритма - O(logN), поскольку мы делим целое число на 2 всякий раз, когда получаем четное число. 
# Затем каждое нечетное число преобразуется в четное путем вычитания из него 1. 
# Сложность алгоритма - логарифмическая.

class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0               # Объявляем счётчик шагов.
        while num > 0:          # Выполняем цикл, пока не доведём число до нуля.
            if num % 2 == 0:    # Если число чётное - делим его на два.
                print ('Step ', steps+1, '): ', int(num), ' is even; divide by 2 and obtain', int(num/2), '.')
                num /= 2 
            else:               # Если число нечётное - отнимаем от него единицу.
                print ('Step ', steps+1, '): ', int(num), ' is odd; subtract 1 and obtain', int(num-1), '.')
                num -=1 
            steps += 1          # После каждой иттерации увеличиваем счётчик шагов на 1.
        return steps            # Возвращаем количество шагов, затраченных на доведение числа до нуля.

ans = Solution()
print(ans.numberOfSteps(14))
print(ans.numberOfSteps(8))