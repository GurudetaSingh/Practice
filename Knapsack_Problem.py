# Given n elem each of weight and profit, determine maximum profit that can be obtained by selecting subset of elements weighing no more than w
def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits,
                                            capacity-weights[idx], idx+1)
        return max(option1, option2)
      
      
# Overcoming inefficiency
def max_profit_dp(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n):
        for c in range(1, capacity + 1):
            if weights[i] > c:
                table[i+1][c+1] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c], 
                                    profits[i] + table[i][c-weights[i]])
    return table[-1][-1]
