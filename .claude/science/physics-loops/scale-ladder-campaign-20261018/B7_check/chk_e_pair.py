#!/usr/bin/env python3
"""(e): doubled-cell class = 48 dressed O_h about site 0 + even translations (fcc of x+y+z even).
  1. free fermions: folded k* fibre (24 dims) of random class-symmetric Hamiltonians -> level multiplicities;
  2. two-fermion site states M (antisymmetric 12x12) with U_g M U_g^T = chi_g M for all 48; Slater rank;
  3. pair product state symmetric: the lam.v sign enters squared; parity of x+y+z preserved by O_h;
     direct check on the L = 2 torus restricted to the two-particle-per-even-site pair operators.
  4. also: is the odd site's (1,0,0) site group class the same? and does the A2-type (w1-odd x odd translation)
     element belong to this class? (it does not; noted for scoping)"""
import itertools, sys
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__file__))
from chk_core import *

T4 = torus_ops(4)
kst = np.array([.5, -.5, .5]) * np.pi
even_t = [t for t in itertools.product(range(4), repeat=3) if sum(t) % 2 == 0]
Gs = [T4['G'](g) for g in ALL]
B2 = np.hstack([T4['bloch'](kst), T4['bloch'](-kst)])
for trial in range(3):
    rr = np.random.default_rng(100 + trial)
    A = rr.normal(size=(T4['n'],)*2) + 1j*rr.normal(size=(T4['n'],)*2)
    # make it short-ranged-ish isn't needed for a degeneracy test; symmetrise over the full finite group
    A = (A + A.conj().T) / 2
    A = sum(T4['T'](t) @ A @ T4['T'](t).T for t in even_t) / len(even_t)
    A = sum(G @ A @ G.T for G in Gs) / 48
    oddT = T4['T']((1, 0, 0))
    assert all(np.allclose(G @ A @ G.T, A) for G in Gs)
    sub = B2.conj().T @ A @ B2
    # invariance of span(k*, -k*) under A (even translations only)
    leak = np.linalg.norm(A @ B2 - B2 @ sub)
    print(f"trial {trial}: odd translation broken {not np.allclose(oddT @ A @ oddT.T, A)}; span(k*,-k*) invariant (leak {leak:.1e}); folded k* multiplicities {mults(np.linalg.eigvalsh(sub), 1e-8)}")

# 2-fermion site states
chars = {}
W1 = []
for g in PROPER:
    M = OH[g]
    p = [DIRS.index(rdir(M, d)) for d in DIRS]
    sgn = 1; p = list(p)
    for i in range(6):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; sgn = -sgn
    W1.append(0 if sgn == 1 else 1)
def w1(g): return W1[g] if g < 24 else W1[[h for h in PROPER if (OH[h] == -OH[g]).all()][0]]
# antisymmetric basis
pairs = list(itertools.combinations(range(12), 2))
def vec2mat(x):
    Mx = np.zeros((12, 12), complex)
    for (a, b), c in zip(pairs, x): Mx[a, b] = c; Mx[b, a] = -c
    return Mx
def mat2vec(Mx): return np.array([Mx[a, b] for a, b in pairs])
R2 = [np.array([mat2vec(UF[g] @ vec2mat(e) @ UF[g].T) for e in np.eye(66)]).T for g in ALL]
# check linear rep on pairs (projective signs cancel)
lin = all(np.allclose(R2[a] @ R2[b], R2[[c for c in ALL if (OH[c] == OH[a] @ OH[b]).all()][0]]) for a in ALL for b in ALL)
print("U(x)U on pairs is a LINEAR rep of O_h:", lin)
found = {}
for aa, bb in itertools.product((0, 1), repeat=2):
    chi = np.array([(-1.0) ** (aa * w1(g) + bb * (g >= 24)) for g in ALL])
    P = sum(c * R for c, R in zip(chi, R2)) / 48
    ev, V = np.linalg.eigh((P + P.conj().T) / 2)
    Vs = V[:, ev > 0.5]
    if Vs.shape[1]:
        ranks = []
        for j in range(Vs.shape[1]):
            ranks.append(int(np.sum(np.linalg.svd(vec2mat(Vs[:, j]), compute_uv=False) > 1e-9)))
        # minimal rank in the invariant subspace: random combos
        rr = np.random.default_rng(1)
        rmin = min(int(np.sum(np.linalg.svd(vec2mat(Vs @ (rr.normal(size=Vs.shape[1]) + 1j*rr.normal(size=Vs.shape[1]))), compute_uv=False) > 1e-9)) for _ in range(20))
        found[(aa, bb)] = (Vs.shape[1], ranks, rmin)
print("1-dim reps on site pair space (w1 sign, improper sign): (dim, ranks of basis vectors, generic rank)", found)
# Slater pair exists iff some invariant subspace of dim 2 for the one-particle rep: O_h commutant dims
rr = np.random.default_rng(3)
X = rr.normal(size=(12, 12)) + 1j*rr.normal(size=(12, 12)); X = X + X.conj().T
print("one-particle O_h site irreps:", mults(np.linalg.eigvalsh(sum(UF[g] @ X @ UF[g].T for g in ALL) / 48), 1e-8))
# a rank-2 element of an invariant pair line would be a Slater pair: check exhaustively that the invariant lines have no rank-2 member
# (for dim-2 invariant spaces, rank of a x + b y as function of (a,b): check min over a grid on CP^1)
for key, (dim, _, _) in found.items():
    chi = np.array([(-1.0) ** (key[0] * w1(g) + key[1] * (g >= 24)) for g in ALL])
    P = sum(c * R for c, R in zip(chi, R2)) / 48; ev, V = np.linalg.eigh((P + P.conj().T)/2); Vs = V[:, ev > 0.5]
    best = 99
    for th in np.linspace(0, np.pi, 61):
        for ph in np.linspace(0, 2*np.pi, 61):
            c = np.zeros(dim, complex); c[0] = np.cos(th/2)
            if dim > 1: c[1] = np.sin(th/2) * np.exp(1j*ph)
            if dim > 2: c[2:] = 0
            s = np.linalg.svd(vec2mat(Vs @ c), compute_uv=False)
            best = min(best, int(np.sum(s > 1e-3 * s[0])))
    print(f"   char {key}: min numerical rank over a CP^1 grid of the first two basis vectors = {best}")

# parity preservation and the lam-sign squared
print("O_h preserves parity of x+y+z:", all((sum(OH[g] @ np.array(v)) - sum(v)) % 2 == 0 for g in ALL for v in itertools.product(range(-2, 3), repeat=3)))
# pair operator transformation on L=4 torus: build P_v^dag coefficient matrix on 768 modes, check G P_v G^-1 = chi P_{Rv}
key = sorted(found)[0]
chi = np.array([(-1.0) ** (key[0] * w1(g) + key[1] * (g >= 24)) for g in ALL])
P = sum(c * R for c, R in zip(chi, R2)) / 48; ev, V = np.linalg.eigh((P + P.conj().T)/2); psi = V[:, ev > 0.5][:, 0]
Msite = vec2mat(psi)
si = T4['si']; n = T4['n']
def pair_big(v):
    K = np.zeros((n, n), complex); i = si[tuple(x % 4 for x in v)]
    K[12*i:12*i+12, 12*i:12*i+12] = Msite; return K
ok = True
for g in ALL:
    G = T4['G'](g)
    for v in [(0,0,0), (1,1,0), (2,1,3), (1,0,1)]:
        Rv = tuple(int(x) % 4 for x in OH[g] @ np.array(v))
        # G c^dag_i G^-1 = sum_j G_ji c^dag_j  => coefficient matrix K -> G K G^T
        ok &= np.allclose(G @ pair_big(v) @ G.T, chi[g] * pair_big(Rv))
print(f"pair operators: G_g P_v^dag G_g^-1 = chi_g P_(Rv)^dag for all 48 g on sample even sites (char {key}):", ok)
