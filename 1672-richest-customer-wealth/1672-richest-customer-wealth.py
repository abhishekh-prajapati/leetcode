class Solution(object):
    def maximumWealth(self, accounts):
        max_value = 0
        for customer in accounts:
            total = 0
            for money in customer:
                total += money
            if total > max_value:
                max_value = total
        return max_value