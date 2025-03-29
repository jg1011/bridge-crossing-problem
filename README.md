# The Old Bridge At Night Problem

In this repo we are concerned with a classical logical puzzle that falls under the umbrella of discrete optimisation. 

## Problem statement: 

Suppose there are $n \geq 1$ people wanting to cross a bridge. The group share one torch between them and it is dark, so a torch is required to cross the bridge. The bridge is old, so at most two people may be on the bridge at any given moment. Person $1 \leq i \leq n$ takes $\omega_i > 0$ minutes to cross the bridge. What is the fastest the entire group can make it to the other side of the bridge? 

Combinatorial questions such as "how strategies take between $a$ and $b$ minutes to complete" will also be of interest. 

## Solutions for small groups

If $n \leq 2$ the problem is trivial. If $n = 3$ the problem is still trivial. WLOG assume $\omega_1 \leq \omega_2 \leq \omega_3$, 
then it is best to send person $1$ and $2$ together first, have person $1$ return with the torch, and then to send 
$(1,3)$ across, taking a total time of $omega_1 + \omega_2 + \omega_3$. We could equivalently have sent $1$ and $3$ together first, having $1$ return then sending $1$ and $2$ across. 

If $n=4$, more work is already required. One strategy is the "escort strategy", a simple greedy approach. 

-> send (1,2) 
-> return (1)
-> send (1,3) 
-> return (1)
-> send (1,4)

This gives a total time of $2\omega_1 + \omega_2 + \omega_3 + \omega_4$. Seems logical, but what if $\omega_3 > \! \! > \omega_1, \omega_2$? We may gain significantly by pairing up $(3,4)$ and sacrificing some time on the returns. We call this strategy the "escort strategy". 

-> send (1,2)
-> return (1)
-> send (3,4)
-> return (2)
-> send (1,2)

This gives a total time $\omega_1 + 3\omega_2 + \omega_4$. Hence, the pair strategy outperforms the escort strategy when $\omega_3 > 2\omega_2 - \omega_1$. One can then verify that these two strategies form the optimal solution when $n=4$. 