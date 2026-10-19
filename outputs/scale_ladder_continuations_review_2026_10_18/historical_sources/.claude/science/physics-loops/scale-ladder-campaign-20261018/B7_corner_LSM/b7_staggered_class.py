#!/usr/bin/env python3
"""B7 (4): the doubled-cell class of the cross-rung note, item 4 (site rotations + site inversion + translations
up to the staggered sign, i.e. even translations kept) -- a free-fermion obstruction that is NOT a many-body one.

  S1  free fermions: the folded fibre at k* (k* and -k* identified, 24 states) carries the twisted O_h class with
      only 4-dim irreps, so every level of every symmetric Hamiltonian there has multiplicity divisible by 4
      (random uniform + staggered symmetric Hamiltonians on the L = 4 torus).  Hence 2 mod 4 fermions per doubled
      cell (odd nu per site, including the node filling nu = 1) admit no Slater band insulator in this class.
  S2  many-body: a product of O_h-invariant two-fermion site states on the even sublattice (vacuum on the odd one)
      is invariant under every symmetry of this class and is the unique gapped ground state of a commuting-projector
      Hamiltonian at nu = 1 per site: an interaction-enabled symmetric SRE insulator.  No LSM obstruction here.
  S3  contrast: with all translations kept (classes G, Gh) odd nu IS obstructed many-body (b7_many_body_lsm.py M2).
"""
import itertools, sys, time
import numpy as np
import b7_model as m

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)
def mults(ev, tol=1e-8):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    return out

t0 = time.time()
D = m.build(); C = D['C']; OH = D['OH']; U = D['U']; lam = D['lam']
L = 4; VERTS = D['VERTS']; nV = D['nV']; CI = D['CI']; VID = C['VID']
rng = np.random.default_rng(5)
kst = np.array([1, -1, 1]) * np.pi / 2
P_ = [C['psg_sign'](lambda q, M=M: C['rot_vert'](M, q), D['u']) for M in OH]
def opmat(g):
    P, s = P_[g]; M = np.zeros((nV, nV)); M[P, np.arange(nV)] = (-1.0) ** s; return M
def transmat(t):
    T = np.zeros((nV, nV))
    for a, (v, c) in enumerate(VERTS): T[VID[(tuple((x + y) % L for x, y in zip(v, t)), c)], a] = 1
    return T
def real_space(h, stag):
    """sum_v sum_d [stag ? (-1)^(x+y+z of v) : 1] h_d |v + d><v|, Hermitised."""
    H = np.zeros((nV, nV), complex)
    for a0, (v, c) in enumerate(VERTS):
        if c != D['CORN'][0]: continue
        sg = (-1.0) ** sum(v) if stag else 1.0
        for d, B in h.items():
            w = tuple((x + y) % L for x, y in zip(v, d))
            rows = [VID[(w, cc)] for cc in D['CORN']]; cols = [VID[(v, cc)] for cc in D['CORN']]
            H[np.ix_(rows, cols)] += sg * B
    return (H + H.conj().T) / 2
def Bloch(k):
    B = np.zeros((nV, 12), complex)
    for a, (v, c) in enumerate(VERTS): B[a, CI[c]] = np.exp(1j * np.dot(k, v)) / np.sqrt(L ** 3)
    return B
B2 = np.hstack([Bloch(kst), Bloch(-kst)])
Gs = [opmat(g) for g in range(48)]; Tev = [transmat(t) for t in ((1, 1, 0), (0, 1, 1), (2, 0, 0))]; Todd = transmat((1, 0, 0))
h0 = D['blocks_from'](D['H0mat'](-1.0, 0.2))
print("S1. free fermions in the doubled-cell O_h class")
ok_sym = True; ok4 = True; info = []; ok_break = True
for trial in range(4):
    hu = m.symmetrize(m.random_blocks(rng, 1), D, list(range(48)))
    hst = m.symmetrize(m.random_blocks(rng, 1), D, list(range(48)))
    H = real_space(m.add(h0, hu, 1.0, 0.5), False) + 0.5 * real_space(hst, True)
    ok_sym &= all(np.allclose(G @ H @ G.T, H, atol=1e-10) for G in Gs) and all(np.allclose(T @ H @ T.T, H) for T in Tev)
    ok_break &= not np.allclose(Todd @ H @ Todd.T, H)
    ev = np.linalg.eigvalsh(B2.conj().T @ H @ B2); mm = mults(ev); info.append(mm)
    ok4 &= all(x % 4 == 0 for x in mm)
check("random uniform + staggered Hamiltonians invariant under the 48 dressed O_h operators and the even translations "
      "(odd translations broken)", ok_sym and ok_break)
check("every level of the folded 24-state fibre at k* has multiplicity divisible by 4, so 2 mod 4 fermions per doubled "
      "cell (odd nu per site) admit no Slater band insulator in this class", ok4, f"multiplicities {info[0]}")
# representation-theoretic reason: the twisted O_h class on the fibre has only 4-dim irreps
X = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)); X = X + X.conj().T
dims = sorted(set(mults(np.linalg.eigvalsh(sum(U[g] @ X @ U[g].T for g in range(48)) / 48), 1e-7)))
check("reason: the dressed O_h operators (inversion anticommuting with the w1-odd rotations) have only 4-dim irreps "
      "on the 12-dim fibre; on the folded fibre inversion pairs k* with -k* and the same class acts", dims == [4], f"{dims}")

print("\nS2. many-body: interaction-enabled symmetric product state at nu = 1 per site")
# O_h-invariant 2-fermion site state, built by projection in the 66-dim N = 2 sector
pairs = list(itertools.combinations(range(12), 2)); pi_ = {p: i for i, p in enumerate(pairs)}
def two_body(Um):
    """action of a monomial one-particle unitary on the antisymmetrised pair basis c_a^dag c_b^dag (a < b)."""
    M = np.zeros((66, 66), complex)
    img = [int(np.nonzero(np.abs(Um[:, c]) > 1e-12)[0][0]) for c in range(12)]
    for (a, b), i in pi_.items():
        ia, ib = img[a], img[b]; amp = Um[ia, a] * Um[ib, b]
        if ia < ib: M[pi_[(ia, ib)], i] += amp
        else: M[pi_[(ib, ia)], i] -= amp
    return M
T2 = [two_body(U[g].astype(complex)) for g in range(48)]
# on N = 2 the dressed operators form a linear representation of O_h; look for any 1-dim character
# chi(g) = (-1)^(a w1(R_g) + b [g improper]), (a, b) in {0,1}^2 (A1g, A2g, A1u, A2u)
found = []
for a_, b_ in itertools.product((0, 1), repeat=2):
    chi = [(-1.0) ** (a_ * D['W1'][g % 24] + b_ * (g >= 24)) for g in range(48)]
    Pm = sum(c * T for c, T in zip(chi, T2)) / 48
    ev, V = np.linalg.eigh((Pm + Pm.conj().T) / 2)
    if (ev > 0.5).any(): found.append(((a_, b_), V[:, ev > 0.5], chi))
(ab_, inv, chi) = found[0]
psi = inv[:, 0]
print(f"   1-dim characters (a: w1 sign, b: improper sign) present on N = 2: {[(f[0], f[1].shape[1]) for f in found]}")
ok_inv = inv.shape[1] > 0 and all(np.allclose(T @ psi, c * psi) for T, c in zip(T2, chi))
# Slater check: is psi a single Slater determinant? (rank of the 12x12 antisymmetric coefficient matrix)
Amat = np.zeros((12, 12), complex)
for (a, b), i in pi_.items(): Amat[a, b] = psi[i]; Amat[b, a] = -psi[i]
rank = int(np.sum(np.linalg.svd(Amat, compute_uv=False) > 1e-9))
check("the 66-dim two-fermion site space contains states in a 1-dim representation of the dressed O_h operators; "
      "the chosen one has antisymmetric coefficient rank > 2, i.e. it is not a Slater determinant", ok_inv and rank > 2,
      f"invariant dimension {inv.shape[1]}, coefficient rank {rank}")
# symmetry of the product state on the even sublattice: dressed operators map even sites to even sites and the
# site-dependent sign (-1)^(lam.v N_v) is +1 for N_v = 2; even translations map even sites to even sites.
parity_ok = all((sum(OH[g] @ np.array(v)) - sum(v)) % 2 == 0 for g in range(48) for v in itertools.product(range(-2, 3), repeat=3))
check("the product state (psi on every even site, vacuum on every odd site) is mapped to itself (as a ray) by all 48 dressed O_h "
      "operators and the even translations; H = sum_even (1 - |psi><psi|) + sum_odd N_v is a symmetric commuting-projector "
      "Hamiltonian with this unique ground state, gap 1, filling 1 per site", ok_inv and parity_ok)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   ({time.time() - t0:.0f} s)")
sys.exit(1 if FAIL else 0)
