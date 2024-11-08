class Solution(object):
    def twoSum(self, nums, target):
      # Создаем пустой словарь для хранения значений и их индексов
      indices = {}

      # Проходим по каждому элементу массива, используя его индекс и значение
      for i, num in enumerate(nums):
          # Находим число, которое нужно добавить к текущему числу, чтобы получить target
          complement = target - num
        
          # Проверяем, есть ли это число в словаре
          if complement in indices:
            # Если да, то возвращаем индексы найденной пары
            return [indices[complement], i]
        
          # Если нет, то добавляем текущее число и его индекс в словарь
          indices[num] = i
