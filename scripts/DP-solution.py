### dynamic programming solution to the n-crossing problem ###

import numpy as np

# Note this solution is not unique
def DP_solution(omega: np.array, n: int) -> tuple[np.array, int]:
    ## DP step ##
    def cross_slowest_two(i) -> int:
        nonlocal t # bring t into scope
        if 2*omega[0] + omega[n-2] + omega[n-1] < omega[0] + 2*omega[1] + omega[n-1]:
            moves[i:i+4] = [(1, n), (1, None), (1, n-1), (1, None)]
            t += 2*omega[0] + omega[n-2] + omega[n-1]
        else:
            moves[i:i+4] = [(1,2), (1, None), (n-1, n), (2, None)]
            t += omega[0] + 2*omega[1] + omega[n-1]
            
    t = 0 # keep track of time in optimal solution 
    # optimal strategy has 2n - 3 moves so we may preallocate space
    # we denote return moves by (i, None)
    moves = np.empty(shape = 2*n - 3, dtype=object)
    i = 0 # keep track of number of moves for array replacement

    while n > 3:
        cross_slowest_two(i)
        n -= 2
        i += 4
        
    if n == 3:
        moves[i : i + 3] = np.array([(1,3), (1, None), (1,2)])
        t += omega[2] + omega[0] + omega[2]
    else: 
        moves[i] = (1, 2)
        t += omega[1]
    
    return (moves, t)