"""
The set-covering problem
Book: Grokking Algorithms
Chapter 8: Greedy Algorithms

Suppose you're starting a radio show. You want to reach listeners in all 50 states.
You have to decide what stations to play on to reach all those listeners.
It costs money to be on each station, so you're trying to minimize the number of stations you play on.
You have a list of stations.
Each station covers a region, and there's overlap.

station | states
kone -> id, nv, ut
ktwo -> wa, id, mt
kthree -> or, nv, ca
kfour -> nv, ut
kfive -> ca, az

How do you figure out the smallest set of stations you can play on to cover all 50 states?
"""
