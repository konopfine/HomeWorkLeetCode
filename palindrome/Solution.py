class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Отрицательные числа и числа, оканчивающиеся на 0 (кроме 0), не могут быть палиндромами
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Число - палиндром, если x равно reversed_half (для четного числа цифр)
        # или если x равен reversed_half // 10 (для нечетного числа цифр)
        return x == reversed_half or x == reversed_half // 10