#!/usr/bin/env python3
"""Exact checks for J:derive:the-walkers-side-of-the-clocks-algebra:a1 (worker w-macbookpro9927a-j04e2).

The walk of block 54 on the 6^3 torus in block 136's conventions: (T_a psi)(x) = psi(x + e_a),
S_a = (T_a - T_a^-1)/(2i), C_a = (T_a + T_a^-1)/2, H = sum_a sigma_a S_a, P_j = S_j C_j.
Densities (block 136): e(x) = Re psi^dag(x)(H psi)(x) [block 137's e_x = (Pi_x H + H Pi_x)/2],
e' = C1C2C3 e; P''_j = phi_j^T pi_j, phi_j^T = (1/2)(1 + T_j) prod_{l != j} C_l, pi_j = Re psi^dag P_j psi;
Q_j = C1C2C3 Q^b_j; P^B = (P'' + Q)/2 (blocks 136, 138).  Lapse-smeared walks: H[N] = sum N_x e_x
(arithmetic bond mean), H'[N] = sum N_x e'_x, H_G[N] = sqrt(N) H sqrt(N) (geometric mean).
Block 112's bond field: xi_j(x) = N_{x+e_j} M_x - N_x M_{x+e_j} (times K/(4 alpha)).
All arithmetic is exact over Q(i) (sparse matrices).  L = 6 so that two-step hops do not alias.
"""
import itertools, time
from fractions import Fraction as F
from sympy.polys.domains import QQ_I
t0=time.time()
Z,ONE,IM=QQ_I(0,0),QQ_I(1,0),QQ_I(0,1)
def q(a,b=0): return QQ_I(F(a),F(b))
def add(A,B,c=ONE):
    C={i:dict(r) for i,r in A.items()}
    for i,r in B.items():
        Ci=C.setdefault(i,{})
        for j,v in r.items(): Ci[j]=Ci.get(j,Z)+c*v
    return prune(C)
def prune(A): return {i:{j:v for j,v in r.items() if v!=Z} for i,r in A.items() if any(v!=Z for v in r.values())}
def mul(A,B):
    C={}
    for i,r in A.items():
        Ci={}
        for k,a in r.items():
            for j,b in B.get(k,{}).items(): Ci[j]=Ci.get(j,Z)+a*b
        if Ci: C[i]=Ci
    return prune(C)
def scal(A,c): return prune({i:{j:c*v for j,v in r.items()} for i,r in A.items()})
def dag(A):
    C={}
    for i,r in A.items():
        for j,v in r.items(): C.setdefault(j,{})[i]=QQ_I(v.x,-v.y)
    return C
def comm(A,B): return add(mul(A,B),mul(B,A),q(-1))
L=6
sites=list(itertools.product(range(L),repeat=3)); ix={s:i for i,s in enumerate(sites)}; Ns=len(sites)
def sh(s,a,d): t=list(s); t[a]=(t[a]+d)%L; return tuple(t)
SIG=[[[Z,ONE],[ONE,Z]],[[Z,q(0,-1)],[IM,Z]],[[ONE,Z],[Z,q(-1)]]]
def T(a):  # (T_a psi)(x) = psi(x+e_a): matrix <x|T|x+e_a> = 1 (coin identity)
    M={}
    for s in sites:
        i,j=ix[s],ix[sh(s,a,1)]
        for c in range(2): M.setdefault(2*i+c,{})[2*j+c]=ONE
    return M
def coin(a,A):  # sigma_a (x) A-site operator with coin identity -> sigma_a acting on coin
    M={}
    for i,r in A.items():
        si,ci=divmod(i,2)
        for j,v in r.items():
            sj,cj=divmod(j,2)
            if not (ci==0 and cj==0): continue
            for c2 in range(2):
                for d2 in range(2):
                    w=SIG[a][c2][d2]
                    if w!=Z: M.setdefault(2*si+c2,{})[2*sj+d2]=M.get(2*si+c2,{}).get(2*sj+d2,Z)+w*v
    return prune(M)
Ts=[T(a) for a in range(3)]; Ti=[dag(Ts[a]) for a in range(3)]
S=[scal(add(Ts[a],Ti[a],q(-1)),q(0,F(-1,2))) for a in range(3)]   # (T - T^-1)/(2i)
C=[scal(add(Ts[a],Ti[a]),q(F(1,2))) for a in range(3)]
H={}
for a in range(3): H=add(H,coin(a,S[a]))
P=[mul(S[a],C[a]) for a in range(3)]
def diag(f):  # site function -> operator
    return {2*ix[s]+c:{2*ix[s]+c:q(f[s])} for s in sites for c in range(2) if f[s]!=0}
def sym(Dg,A): return scal(add(mul(Dg,A),mul(A,Dg)),q(F(1,2)))
def avgC(f,axes):   # apply C_l for l in axes to a site field
    for l in axes:
        f={s:(f[sh(s,l,1)]+f[sh(s,l,-1)])/2 for s in sites}
    return f
def HA(N): return sym(diag(N),H)            # sum_x N_x e_x (arithmetic bond mean)
def HAbar(N): return HA(avgC(N,[0,1,2]))    # sum_x N_x e'_x, e' = C1C2C3 e
def RB(xi):   # sum_{x,j} xi_j(x) P^B_j(x) as an operator, P^B = (P'' + Q)/2
    R={}
    for j in range(3):
        f={s:xi[j][s] for s in sites}
        # P'' part: sum_x xi(x) (phi_j^T pi_j)(x) = sum_y (phi_j xi)(y) pi_j(y), phi_j = (1/2)(1+T_j^-1) prod_{l!=j} C_l
        g=avgC(f,[l for l in range(3) if l!=j])
        w={s:(g[s]+g[sh(s,j,-1)])/2 for s in sites}
        Ppart=sym(diag(w),P[j])
        # Q part: sum_x xi(x) (C1C2C3 Q^b_j)(x) = sum_y u(y) Q^b_j(y), u = C1C2C3 xi
        u=avgC(f,[0,1,2])
        U={}
        for s in sites:
            if u[s]==0: continue
            i,k=ix[sh(s,j,1)],ix[s]
            for c2 in range(2):
                for d2 in range(2):
                    v=SIG[j][c2][d2]
                    if v!=Z: U.setdefault(2*i+c2,{})[2*k+d2]=q(u[s])*v
        A=add(mul(U,H),mul(H,U))
        Qpart=scal(add(A,dag(A)),q(F(1,4)))
        R=add(R,add(scal(Ppart,q(F(1,2))),scal(Qpart,q(F(1,2)))))
    return R

RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


def ratio(A, B):
    """the unique c with A = c B, or None"""
    r = None
    keys = set((i, j) for i, row in A.items() for j in row) | set((i, j) for i, row in B.items() for j in row)
    for (i, j) in keys:
        a = A.get(i, {}).get(j, Z)
        b = B.get(i, {}).get(j, Z)
        if b == Z:
            if a != Z:
                return None
            continue
        rr = a / b
        if r is None:
            r = rr
        elif rr != r:
            return None
    return r


def nnz(A):
    return sum(len(r) for r in A.values())


def xi(M, N):
    return [{s: N[sh(s, j, 1)] * M[s] - N[s] * M[sh(s, j, 1)] for s in sites} for j in range(3)]


import random
random.seed(20260925)
herm = all(H.get(j, {}).get(i, Z) == QQ_I(v.x, -v.y) for i, r in H.items() for j, v in r.items())
H2 = mul(H, H)
SS = {}
for a in range(3):
    SS = add(SS, mul(S[a], S[a]))
check("X1", herm and H2 == SS and all(P[a] == dag(P[a]) for a in range(3)),
      "construction: H Hermitian, H^2 = sum_a S_a^2 exactly (the sigma_a anticommute), P_j = S_j C_j Hermitian")

one = {s: F(1) for s in sites}
g = {s: F(random.randint(-5, 5), random.randint(1, 4)) for s in sites}
grad_g = [{s: g[sh(s, j, 1)] - g[s] for s in sites} for j in range(3)]
lhs_bar = scal(comm(H, HAbar(g)), IM)                     # first order of i[H'[M], H'[N]] at M = 1, N = 1 + g
lhs_u = scal(comm(H, HA(g)), IM)                          # same with block 137's e (and the geometric rule)
R = RB(grad_g)
okX2 = nnz(add(lhs_bar, R, q(-1))) == 0 and ratio(lhs_bar, R) == q(1)
check("X2", okX2, "first order, averaged density: i[H, sum_x g_x e'_x] = sum_{x,j} (g_{x+e_j} - g_x) P^B_j(x) exactly "
      "(block 136 T1/T2 as operator identities), so i[H'[M], H'[N]] and sum xi(M,N).P^B agree at first order in "
      "the departures iff K/(4 alpha) = 1")
okX3 = ratio(lhs_u, R) is None and nnz(lhs_u) > 0
check("X3", okX3, "first order, block 137's density (arithmetic, and the geometric rule, equal at first order): "
      "i[H, sum_x g_x e_x] is not c sum grad g . P^B for any c: the landed P^B is the current of e' = C1C2C3 e, "
      "not of e, so no normalization closes the walker's bracket even at first order")
# second order and exactness: delta lapses two steps apart along an axis (and, as a side fact, on a face diagonal)
u = (2, 2, 2)
v = sh(u, 0, 2)
M = {s: F(1 if s == u else 0) for s in sites}
N = {s: F(1 if s == v else 0) for s in sites}
xs = xi(M, N)
zero_xi = all(xs[j][s] == 0 for j in range(3) for s in sites)
Bu = scal(comm(HA(M), HA(N)), IM)
Bb = scal(comm(HAbar(M), HAbar(N)), IM)
vd = sh(sh(u, 0, 1), 1, 1)
Nd = {s: F(1 if s == vd else 0) for s in sites}
Bd = scal(comm(HA(M), HA(Nd)), IM)
ok4 = zero_xi and nnz(Bu) > 0 and nnz(Bb) > 0 and nnz(Bd) == 0
check("X4", ok4, f"exact closure fails, lowest order two for the averaged density: delta lapses at u and u + 2e_1 give "
      f"xi(M, N) = 0 on every bond, but i[H[M], H[N]] has {nnz(Bu)} and i[H'[M], H'[N]] {nnz(Bb)} nonzero entries; the "
      f"bracket is bilinear, so this is the departures' second-order term B(m, n) at m = delta_u, n = delta_v; "
      f"(on a face diagonal u, u + e_1 + e_2 the two paths give sigma_1 sigma_2 and sigma_2 sigma_1 and cancel: "
      f"the bracket is 0 there)")
# the straight two-step coefficient for the arithmetic rule
m = {s: F(random.randint(-6, 6), random.randint(1, 5)) for s in sites}
n = {s: F(random.randint(-6, 6), random.randint(1, 5)) for s in sites}
Bmn = scal(comm(HA(m), HA(n)), IM)
okX5 = True
nres = 0
for a in range(3):
    for x0 in sites:
        x1, x2 = sh(x0, a, 1), sh(x0, a, 2)
        m0, m1, m2 = m[x0], m[x1], m[x2]
        n0, n1, n2 = n[x0], n[x1], n[x2]
        full = (m0 * n1 - m1 * n0) + (m1 * n2 - m2 * n1) + (m0 * n2 - m2 * n0)
        for c in range(2):
            elem = Bmn.get(2 * ix[x0] + c, {}).get(2 * ix[x2] + c, Z)
            okX5 = okX5 and elem == q(0, -F(1, 16)) * q(full)
            off = Bmn.get(2 * ix[x0] + c, {}).get(2 * ix[x2] + 1 - c, Z)
            okX5 = okX5 and off == Z
        nres += (m0 * n2 - m2 * n0) != 0
kappa = "-i/16"
okX5 = okX5 and nres > 0
check("X5", okX5, f"straight two-step coefficient (arithmetic rule), at every site and on all three axes for generic "
      f"rational m, n: <x|i[H[m], H[n]]|x + 2e_a> = -(i/16)[(m0 n1 - m1 n0) + (m1 n2 - m2 n1) + (m0 n2 - m2 n0)] "
      f"times the coin identity: the two bonds' xi plus a second-neighbour term (m0 n2 - m2 n0) that no "
      f"nearest-bond xi can produce")

npass = sum(ok for _, ok in RES)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass}  ({time.time() - t0:.0f} s)")
if npass == len(RES):
    print("SUMMARY: COUNTEREXAMPLE the walker's clock algebra does not close on sum xi(M,N).P^B exactly: with block "
          "137's density e (arithmetic or geometric bond mean) it fails already at first order in the lapse "
          "departures for every normalization, because the landed P^B is the current of the averaged density "
          "e' = C1C2C3 e; with e' it closes exactly at first order iff K/(4 alpha) = 1 (alpha = K/4) and fails at "
          "second order, witnessed by delta lapses two steps apart (xi = 0, bracket nonzero); on a straight two-step "
          "path the arithmetic rule leaves a second-neighbour term (m0 n2 - m2 n0).")
    print("HIT: on the 6^3 torus, exactly over Q(i): i[H, sum g e'] = sum_{x,j}(g_{x+e_j} - g_x) P^B_j (block 136 T1/T2 "
          "as operator identities), so the walker's lapse bracket matches block 112's xi(M,N).P^B at first order "
          "iff K/(4 alpha) = 1 when the lapse couples to e' = C1C2C3 e, while with block 137's e (arithmetic or "
          "geometric mean) no normalization matches even at first order; exact closure fails at second order: "
          "delta lapses at u and u + 2e_1 give xi = 0 but a nonzero bracket, and the two-step "
          "element carries (m0 n2 - m2 n0) beyond the bonds' xi.")
else:
    print("SUMMARY: ROUTE FAILS AT a failed check above")
