import sympy as sp
from wsym import construct, P2, W
D = sp.Symbol("D")
M, Delta = construct([[sp.Integer(0), sp.Integer(1)], [sp.Integer(1), D]])
tr = M[0][0] + M[1][1]
print("tr  =", tr.as_expr())
print("D^2 =", (Delta * Delta).as_expr())
print("tr / Delta:", sp.div(tr.as_expr(), Delta.as_expr(), *W, modulus=2))
