def alpha_beta(depth, node, alpha, beta, maximizing):
    if depth == 2:
        return [3, 5, 6, 9][node]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            value = alpha_beta(depth + 1, node * 2 + i,
                               alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            value = alpha_beta(depth + 1, node * 2 + i,
                               alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

print("Best value:", alpha_beta(0, 0, float('-inf'),
                                float('inf'), True))