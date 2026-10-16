import numpy as np, sympy as sp
from walks import *
np.set_printoptions(linewidth=200, suppress=True)
for ci in [0,3]:
    D = class_D(ci)
    # exact commutant via sympy
    syms = sp.symbols('x0:64'); X = sp.Matrix(8,8,syms)
    eqs = []
    for M in D.values():
        Ms = sp.Matrix(M.tolist())
        eqs += list(Ms*X - X*Ms)
    sol = sp.solve(eqs, syms, dict=True)[0]
    Xs = X.subs(sol)
    free = sorted(Xs.free_symbols, key=lambda s: int(str(s)[1:]))
    print("class", ci, "free", free)
    for f in free:
        B = Xs.subs({g: (1 if g == f else 0) for g in free})
        print(f); print(np.array(B.tolist(), dtype=int))
