# Problem Statement: 

Suppose $N$ people cross an old bridge at night. Due to the bridge's age, at most two people can cross at one time. 
Due to the darkness, a torch is required to cross the bridge. There is only one torch to be shared among the $N$ people, and to stay in lit conditions each pair that crosses must walk at the speed of the slower person in said pair. Suppose person $1 \leq i \leq N$ takes $2^i$ minutes to cross. 

- What is the fastest time the $N$ people can cross the bridge?

# Repo Outline 

This repo is simply an investigation, I am yet to solve this problem. The cases I have solved are $\dots$

- $N = 3$ : $14$
- $N = 4$ : $30$
- $N = 5$ : $56$
- $N = 6$ : $104$ (could be $102$, LB of $100$ shown to be impossible and $104$ solution found)

Pairing up the two slowest people to cross seems to always be optimal, which makes sense intuitively. I have not yet found a nice way to argue this fact. No recursions are jumping out at me either :(

Intuitively, I'd guess the optimal sequence of moves looks like 

- $(\{1, 2\}, \{1\})$
- $(\{N, N-1\}, \{2\})$ 
- $(\{1, 2\}, \{1\})$
- $(\{N-2, N-3\}, \{2\})$

$\qquad \vdots \qquad \vdots \qquad \vdots$ 

- $(\{1,2\}, \emptyset)$

Pls prove. 