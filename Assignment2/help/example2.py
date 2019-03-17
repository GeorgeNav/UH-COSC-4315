from pysmt.shortcuts import Symbol, And, Iff, Not, is_sat

P = Symbol("P") # Default type is Boolean
Q = Symbol("Q")
prop1 = And(P, Not(Q))
prop2 = Iff(Not(P), Not(Q))
f = And(prop1, prop2)
print(f)
print(is_sat(f))