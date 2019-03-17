# source <(pysmt-install --env)
from pysmt.shortcuts import *

P = Symbol("Pa")
f = And(P, Not(P))
Q = Symbol("Q")
f1 = Implies(f, Q)
print(is_sat(f1))

stack = []
print(stack[-1])