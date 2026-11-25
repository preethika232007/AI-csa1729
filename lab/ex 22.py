def minimax(depth, is_max):
    scores = [10, -10, 5, -5]

    if depth == 2:
        return max(scores) if is_max else min(scores)

    if is_max:
        best = float('-inf')
        for score in scores:
            best = max(best, score)
        return best
    else:
        best = float('inf')
        for score in scores:
            best = min(best, score)
        return best

print("Best score:", minimax(2, True))