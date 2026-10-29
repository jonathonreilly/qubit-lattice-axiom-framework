#!/usr/bin/env python3
# h2_55_a2 — replacement controls for h2_55_a gate A3 (criteria: h2_55_a2_criteria.md, written before this script).
import sympy as sp
P = sp.symbols('p1:5', real=True); R4 = range(4)
d = lambda a, b: 1 if a == b else 0
def TI(mu, nu, rh, si): return P[mu]*P[rh]*d(nu, si) - P[mu]*P[si]*d(nu, rh) - P[nu]*P[rh]*d(mu, si) + P[nu]*P[si]*d(mu, rh)
def Tbad(mu, nu, rh, si): return P[mu]*P[rh]*d(nu, si) + P[mu]*P[si]*d(nu, rh) - P[nu]*P[rh]*d(mu, si) + P[nu]*P[si]*d(mu, rh)
def II(mu, nu, rh, si): return d(mu, rh)*d(nu, si) - d(mu, si)*d(nu, rh)
def vv(lam, mu, nu): return P[mu]*d(nu, lam) - P[nu]*d(mu, lam)
def gram_ok(T): return all(sp.expand(T(a,b,c,e) - sum(vv(l,a,b)*vv(l,c,e) for l in R4)) == 0 for a in R4 for b in R4 for c in R4 for e in R4)
def Bi_nonzero(S): return any(sp.expand(sum(sp.LeviCivita(l, m, n, k)*P[m]*S(n, k, r, s) for m in R4 for n in R4 for k in R4)) != 0 for l in R4 for r in R4 for s in R4)
def AS(S): return lambda a,b,c,e: S(a,b,c,e) - S(b,a,c,e) - S(a,b,e,c) + S(b,a,e,c)
res = []
g1 = gram_ok(TI); print(('PASS' if g1 else 'FAIL'), 'G1 Gram form of T^I'); res.append(g1)
g2 = (not Bi_nonzero(TI)) and Bi_nonzero(II); print(('PASS' if g2 else 'FAIL'), 'G2 Bi[T^I]=0, Bi[I]!=0'); res.append(g2)
c1 = Bi_nonzero(lambda a,b,c,e: TI(a,b,c,e) + II(a,b,c,e)); print(('FIRES' if c1 else 'DOES-NOT-FIRE'), 'C1 Bi[T^I + I] != 0'); res.append(c1)
c2 = not gram_ok(Tbad); print(('FIRES' if c2 else 'DOES-NOT-FIRE'), "C2 sign-flipped T' fails the Gram identity"); res.append(c2)
c3 = Bi_nonzero(AS(lambda a,b,c,e: d(a,c)*d(b,e))); print(('FIRES' if c3 else 'DOES-NOT-FIRE'), 'C3 Bi[antisym dd(mr)(ns)] != 0'); res.append(c3)
print('VERDICT:', 'PASS' if all(res) else 'FAIL')
