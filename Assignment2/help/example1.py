# source <(pysmt-install --env)
from pysmt.shortcuts import Symbol, And, Not, is_sat

P = Symbol("Pa")
Q = Symbol("Qa")
f = And(P, Not(Q))
print(is_sat(f))
print(f)