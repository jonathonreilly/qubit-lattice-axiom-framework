#!/usr/bin/env python3
"""Exact complementary probe: two genuine physical fibers, Gaussian-integer entries."""
import json,time
import sympy as s
import explore_fibers as model
x=s.symbols('x');out=[];polys=[]
for phase in (s.S.One,s.I):
 start=time.perf_counter()
 A=s.zeros(len(model.Q),len(model.P))
 for i,j,c,power in model.terms:A[i,j]-=1 if c is None else phase**power
 H=-A.conjugate().T*A
 p=H.charpoly(x).as_poly();polys.append(p)
 row={'common_chord_phase':str(phase),'matrix_hermitian':H==H.conjugate().T,'characteristic_coefficients':[str(c) for c in p.all_coeffs()],'factorization':str(s.factor(p.as_expr())),'elapsed_seconds':time.perf_counter()-start}
 out.append(row)
g=s.gcd(*polys)
print(json.dumps({'fibers':out,'gcd':str(g.as_expr())},indent=2))
assert g.degree()==0
