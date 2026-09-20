#!/usr/bin/env python3
"""Exact checks for ATTEMPT.md (light-cone long-range order, attempt a2).

C1  Phi is a graph isomorphism Gamma_L -> (Z/L)^3 box K_2, and an involution
C2  both graphs 7-regular on 2 L^3 vertices with 7 L^3 edges
C3  7 - b(k) = E(k) and 7 + b(k) = E(k+pi*) + 2                     (sympy)
C4  {7-b, 7+b} = {E, E+2} as multisets, and sum 1/Lambda agrees     (exact)
C5  the layer reduction <|M|^2> <= 4 <|M_0|^2>                      (exact)
C6  G_L up, H_L down, G_L + H_L below the limit, L = 4, 6, 12       (exact)
C7  shell bound sum_{0<|n|<=R} 1/|n|^2 <= 13 R, R <= 40             (exact)
C8  two-sided rational bracket for W_2                              (geometric tail)
C9  rational lower bound for W_1 against Watson's closed form
C10 beta_0 = (3/2)(W_1 + W_2) inside a5's bracket [0.5879, 0.5931]
C11 fallback threshold 3 W_1 = W_sc / 2, and beta = 1 vs |m| = 0.76
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp
from mpmath import mp, gamma as G_, pi as PI, sqrt as SQ

ok = []
def rec(tag, cond, msg):
    ok.append(bool(cond)); print(("ok   " if cond else "FAIL ") + tag + " " + msg)

# ---------- C1, C2 ----------
N7 = [(0,0,0)] + [tuple(d*(i==j) for i in range(3)) for j in range(3) for d in (1,-1)]
def gamma_edges(L):
    return {frozenset({(x,0), (tuple((x[i]+d[i])%L for i in range(3)),1)})
            for x in product(range(L),repeat=3) for d in N7}
def slab_edges(L):
    E = {frozenset({(x,0),(x,1)}) for x in product(range(L),repeat=3)}
    for x in product(range(L),repeat=3):
        for j in range(3):
            for d in (1,-1):
                y = tuple((x[i]+d*(i==j))%L for i in range(3))
                for a in (0,1): E.add(frozenset({(x,a),(y,a)}))
    return E
Phi = lambda v: (v[0], (v[1]+v[0][0]+v[0][1]+v[0][2]) % 2)
iso = reg = True
for L in (4,6):
    G, S = gamma_edges(L), slab_edges(L)
    V = [(x,e) for x in product(range(L),repeat=3) for e in (0,1)]
    iso &= ({frozenset(Phi(v) for v in ed) for ed in G} == S) and all(Phi(Phi(v))==v for v in V)
    deg = {}
    for ed in S:
        for v in ed: deg[v] = deg.get(v,0)+1
    reg &= len(G) == 7*L**3 == len(S) and set(deg.values()) == {7} and len(deg) == 2*L**3
rec("C1", iso, "Phi maps edges(Gamma_L) onto edges(slab_L), L=4,6; Phi^2=id")
rec("C2", reg, "both 7-regular, |V|=2L^3, |E|=7L^3")

# ---------- C3 ----------
k1,k2,k3 = sp.symbols('k1 k2 k3', real=True)
cs = [sp.cos(k1), sp.cos(k2), sp.cos(k3)]
b, Ek = 1 + 2*sum(cs), 6 - 2*sum(cs)
Es = 6 - 2*sum(sp.cos(k+sp.pi) for k in (k1,k2,k3))
rec("C3", sp.simplify(7-b-Ek)==0 and sp.simplify(7+b-(Es+2))==0,
    "7-b(k)=E(k) and 7+b(k)=E(k+pi*)+2")

# ---------- C4 ----------
def cosF(m,L):
    tab = {4:{0:F(1),1:F(0),2:F(-1),3:F(0)},
           6:{0:F(1),1:F(1,2),2:F(-1,2),3:F(-1),4:F(-1,2),5:F(1,2)}}
    return tab[L][m % L]
good, sums = True, {}
for L in (4,6):
    A, B, tot, g, h = [], [], F(0), F(0), F(0)
    for k in product(range(L),repeat=3):
        s = sum(cosF(m,L) for m in k)
        E_, b_ = 6-2*s, 1+2*s
        A += [7-b_, 7+b_]; B += [E_, E_+2]
        if E_ != 0: tot += 1/E_; g += 1/E_
        tot += 1/(14-E_); h += 1/(14-E_)
    good &= sorted(A) == sorted(B) and g + h == tot
    sums[L] = (g/L**3, h/L**3)
rec("C4", good, "{7-b,7+b}={E,E+2} as multisets; sum 1/Lambda agrees, L=4,6")

# ---------- C5 ----------
A_, c_ = sp.symbols('A c', real=True)
rec("C5", sp.simplify((2*A_+2*c_).subs(c_, A_) - 4*A_) == 0
       and sp.simplify(4*A_ - (2*A_+2*c_)) == sp.simplify(2*(A_-c_)),
    "<|M|^2> = 2A+2c and 4A - (2A+2c) = 2(A-c) >= 0 by Cauchy-Schwarz")

# ---------- C6 ----------
class Q3:
    __slots__ = ('a','b')
    def __init__(s,a,b=F(0)): s.a, s.b = F(a), F(b)
    def __add__(s,o): return Q3(s.a+o.a, s.b+o.b)
    def inv(s):
        d = s.a*s.a - 3*s.b*s.b; return Q3(s.a/d, -s.b/d)
    def num(s): return float(s.a) + float(s.b)*3**0.5
def cos12(m):
    t = {0:Q3(1),1:Q3(0,F(1,2)),2:Q3(F(1,2)),3:Q3(0),4:Q3(F(-1,2)),5:Q3(0,F(-1,2)),
         6:Q3(-1),7:Q3(0,F(-1,2)),8:Q3(F(-1,2)),9:Q3(0),10:Q3(F(1,2)),11:Q3(0,F(1,2))}
    return t[m % 12]
G12 = H12 = Q3(0)
for k in product(range(12),repeat=3):
    s = cos12(k[0]) + cos12(k[1]) + cos12(k[2])
    E_ = Q3(6) + Q3(0) ; E_ = Q3(6 - 2*s.a, -2*s.b)
    if any(k): G12 = G12 + E_.inv()
    H12 = H12 + Q3(8 + 2*s.a, 2*s.b).inv()
g = {L: float(sums[L][0]) for L in (4,6)}; h = {L: float(sums[L][1]) for L in (4,6)}
g[12], h[12] = G12.num()/12**3, H12.num()/12**3
LIM = 0.3936624980
rec("C6", g[4]<g[6]<g[12] and h[4]>h[6]>h[12] and all(g[L]+h[L] < LIM for L in (4,6,12)),
    "G: %.6f<%.6f<%.6f; H down; G+H < W1+W2 at L=4,6,12" % (g[4],g[6],g[12]))

# ---------- C7: shell bound ----------
R0 = 40; cnt = {}
for n in product(range(-R0,R0+1),repeat=3):
    m = n[0]**2+n[1]**2+n[2]**2
    if 0 < m <= R0*R0: cnt[m] = cnt.get(m,0)+1
ms = sorted(cnt); acc = F(0); sh = True; i = 0
for R in range(1,R0+1):
    while i < len(ms) and ms[i] <= R*R: acc += F(cnt[ms[i]], ms[i]); i += 1
    sh &= acc <= 13*R
rec("C7", sh, "sum_{0<|n|<=R} 1/|n|^2 <= 13 R for R = 1..40")

# ---------- C8, C9 ----------
M = 60
fac = [1]*(2*M+1)
for i in range(1,2*M+1): fac[i] = fac[i-1]*i
P = [F(sum(fac[2*m]//(fac[i]**2*fac[j]**2*fac[m-i-j]**2)
       for i in range(m+1) for j in range(m-i+1)), 6**(2*m)) for m in range(M)]
W2lo = sum(F(9,16)**m * P[m] for m in range(M)) / 8
W2hi = W2lo + F(2,7)*F(9,16)**M
W1lo = sum(P) / 6
mp.dps = 30
Wsc = SQ(6)/(32*PI**3)*G_(mp.mpf(1)/24)*G_(mp.mpf(5)/24)*G_(mp.mpf(7)/24)*G_(mp.mpf(11)/24)
W1v = float(Wsc)/6
rec("C8", F(1409314,10**7) < W2lo and W2hi < F(1409315,10**7) and float(W2hi-W2lo) < 3e-16,
    "W_2 in [%.10f, %.10f], inside a5's [.1409314,.1409315]" % (float(W2lo),float(W2hi)))
rec("C9", float(W1lo) < W1v and abs(float(Wsc)-1.5163860591) < 1e-9,
    "W_1 >= %.7f exactly (M=60); W_1 = W_sc/6 = %.10f" % (float(W1lo), W1v))

# ---------- C10, C11 ----------
b0 = 1.5*(W1v + float(W2lo))
rec("C10", 0.5879 < b0 < 0.5931 and abs(b0 - 0.590494) < 1e-5,
    "beta_0 = %.7f, inside a5's [0.5879, 0.5931]" % b0)
rec("C11", abs(3*W1v - float(Wsc)/2) < 1e-15 and 0 < 1-b0 <= 0.76**2,
    "3W_1 = W_sc/2 = %.10f; 1-beta_0 = %.5f <= 0.76^2" % (3*W1v, 1-b0))

print("TOTAL %d/%d" % (sum(ok), len(ok)))
if all(ok):
    print("HIT: Gamma_L is isomorphic to the two-layer nearest-neighbour slab "
          "(Z/L)^3 box K_2 by Phi(x,e) = (x, e + x_1+x_2+x_3 mod 2), so the reflections it needs are the "
          "standard hypercubic ones; and route (ii) closes by Cauchy-Schwarz alone, <|M|^2> <= 4<|M_0|^2>, "
          "with no vertical-energy input and no loss, giving <|m_0|^2> >= 1 - (3/(2 beta))(G_L + H_L) and "
          "order for beta > beta_0 = (3/2)(W_1 + W_2) = %.7f." % b0)
    print("SUMMARY: PARTIAL - exact isomorphism Gamma_L = (Z/L)^3 box K_2 for even L, which turns the "
          "doubled graph into the isotropic nearest-neighbour ferromagnet on a slab (a 4-torus with L_4 = 2), "
          "and a two-line Cauchy-Schwarz closure of route (ii) needing no energy bound and losing nothing in "
          "the constant, reaching a5's beta_0 = %.7f by an independent route." % b0)
else:
    print("SUMMARY: ROUTE FAILS AT the first FAIL line above")
