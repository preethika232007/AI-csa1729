from itertools import permutations

def solve_cryptarithmetic():
    letters = 'SENDMORY'

    for p in permutations('0123456789', 8):
        d = dict(zip(letters, p))

        if d['S'] == '0' or d['M'] == '0':
            continue

        send = int(''.join(d[c] for c in 'SEND'))
        more = int(''.join(d[c] for c in 'MORE'))
        money = int(''.join(d[c] for c in 'MONEY'))

        if send + more == money:
            print(d)
            print(send, '+', more, '=', money)
            return

solve_cryptarithmetic()