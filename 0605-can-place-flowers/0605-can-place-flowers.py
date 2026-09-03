class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0

        for i in range(len(flowerbed)):
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            current_empty = flowerbed[i] == 0
            right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            if left_empty and current_empty and right_empty:
                flowerbed[i] = 1
                count += 1

        return count >= n