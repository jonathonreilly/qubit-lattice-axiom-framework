#!/usr/bin/env python3
"""B7 (1): free-fermion filling constraints for the supplied corner fermion.

Symmetry classes: G  = translations + the 24 PSG-dressed site rotations (O about a site);
                  Gh = G + the PSG-dressed site inversion (O_h about a site).
Number-conserving one-fermion Hamiltonians H(k) = sum_d h_d e^{-ik.d}, filling nu per site (0..12).

Checks (PASS/FAIL):
  A  infinite-lattice reduction: every PSG lift is G_g|v,c> = (-1)^(lam.v + tau(c)) |gv, gc>; the
     Bloch relation U_g H(k) U_g^dag = H(gk + pi s_g) holds at random continuous k;
  B  the fibre representation is the SAME 12-dim projective rep U at every k; twisted, it is a 2O rep
     E1/2 + E5/2 + 2 G3/2 (central element -1);
  C  theorem (odd filling): at k* every level of every G-symmetric H has even multiplicity, so for odd
     nu the nu-th and (nu+1)-th levels at k* coincide;
  D  little-group scan of the affine action (grids N = 8, 12, 24);
  E  Wyckoff-position projective classes (exact operator algebra) for P432-type and Pm-3m-type
     site groups, cross-checked by commutant multiplicities on the L = 4 torus;
  F  constructive band insulators at the allowed fillings, gap certified by a Lipschitz bound;
  G  random-Hamiltonian scans (evidence);
  H  the runner Weyl model: node filling and global band ordering.
"""
import itertools, sys, time
from fractions import Fraction as Fr
import numpy as np
import b7_model as m

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)

def mults(ev, tol=1e-7):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    return out

t0 = time.time()
D = m.build(); OH = D['OH']; U = D['U']; lam = D['lam']; sh = D['shift']
PROPER = list(range(24)); ALL = list(range(48))
kst = np.array([1, -1, 1]) * np.pi / 2
rng = np.random.default_rng(20261018)

# ------------------------------------------------------------------ A
print("A. infinite-lattice reduction")
check("translation-invariant gauge reproduces the flux pattern; every O_h element has a PSG lift of the form "
      "(-1)^(lam.v + tau(c)) on the L = 4 torus", D['flux_ok'] and D['dec_ok'])
h0 = D['blocks_from'](D['H0mat'](-1.0, 0.2))
# a random O_h-invariant range-2 Hamiltonian built directly on the infinite lattice
hr = m.symmetrize(m.random_blocks(rng, 2), D, ALL)
ks = rng.uniform(-np.pi, np.pi, size=(20, 3)); okA = True
for h in (h0, hr):
    Hks = m.Hk(h, ks)
    for g in ALL:
        Hg = m.Hk(h, (OH[g] @ ks.T).T + np.pi * sh[g])
        okA &= np.allclose(Hg, U[g][None] @ Hks @ U[g].T[None], atol=1e-10)
# torus consistency: the L = 4 Bloch restriction of H0 equals H(k)
C = D['C']; L = 4; VERTS = D['VERTS']; CI = D['CI']
def Bloch(k):
    B = np.zeros((D['nV'], 12), complex)
    for a, (v, c) in enumerate(VERTS): B[a, CI[c]] = np.exp(1j * np.dot(k, v)) / np.sqrt(L ** 3)
    return B
kk = np.array([1, 2, 3]) * np.pi / 2
okT = np.allclose(Bloch(kk).conj().T @ D['H0mat'](-1.0, 0.2) @ Bloch(kk), m.Hk(h0, kk)[0])
check("Bloch relation U_g H(k) U_g^T = H(g k + pi s_g) for all 48 g at 20 random continuous k "
      "(supplied H0 and a random O_h-symmetric range-2 Hamiltonian); torus restriction agrees", okA and okT)

# ------------------------------------------------------------------ B
print("\nB. fibre representation")
O2 = m.two_O(D)
ch = [np.trace(M) for M in O2['lift']] if O2['lift'] is not None else None
dec = O2['decompose_chars'](ch) if ch is not None else None
centre = O2['lift'][[k for k in range(48) if np.allclose(O2['G2'][k], -np.eye(2))][0]] if ch else None
check("twisted fibre matrices i^{w1} U_R form a 2O representation, central element = -1, decomposition "
      "E1/2 + E5/2 + 2 G3/2 (k-independent: identical at every momentum and on site 0)",
      dec == {'E1/2': 1, 'E5/2': 1, 'G3/2': 2} and np.allclose(centre, -np.eye(12)), f"{dec}")

# ------------------------------------------------------------------ C
print("\nC. odd filling at k*")
fixed_all = all(np.allclose(np.exp(1j * (OH[g] @ kst + np.pi * sh[g] - kst)), 1) for g in PROPER)
okC = True; ex = []
for r_, cplx, s in ((1, True, 1.0), (2, True, 3.0), (3, False, 10.0), (2, True, 0.01)):
    for trial in range(3):
        h = m.add(h0, m.symmetrize(m.random_blocks(rng, r_, cplx), D, PROPER), 1.0, s)
        ev = np.linalg.eigvalsh(m.Hk(h, kst)[0])
        okC &= all(abs(ev[n] - ev[n - 1]) < 1e-8 * max(1, np.abs(ev).max()) for n in (1, 3, 5, 7, 9, 11))
        ex.append(mults(ev, 1e-8 * max(1, np.abs(ev).max())))
check("k* is fixed by all 24 dressed rotations; for 12 random G-symmetric Hamiltonians (range 1-3, strength "
      "0.01-10, real and complex) E_nu(k*) = E_{nu+1}(k*) for every odd nu", fixed_all and okC, f"multiplicities e.g. {ex[:3]}")

# ------------------------------------------------------------------ D
print("\nD. little groups of the affine action")
def little(k, idx):
    return [g for g in idx if np.allclose(np.exp(1j * (OH[g] @ k + np.pi * sh[g] - k)), 1, atol=1e-9)]
def irrep_dims(gs, seed=0):
    X = np.random.default_rng(seed).normal(size=(12, 12)) + 1j * np.random.default_rng(seed + 1).normal(size=(12, 12))
    X = X + X.conj().T
    Y = sum(U[g] @ X @ U[g].T for g in gs) / len(gs)
    return mults(np.linalg.eigvalsh(Y))
summary = {}
for N in (8, 12, 24):
    for k in m.kgrid(N):
        for lab, idx in (('O', PROPER), ('Oh', ALL)):
            gs = little(k, idx)
            if len(gs) == 1: continue
            dm = irrep_dims(gs)
            key = (lab, len(gs), min(dm), int(np.gcd.reduce(dm)))
            summary.setdefault(key, set()).add(tuple(np.round(((k + np.pi) % (2 * np.pi) - np.pi) / np.pi, 4)))
full_O = summary.get(('O', 24, 2, 2), set())
print("   (group, |little group|, min level multiplicity, gcd) -> number of grid momenta")
for key in sorted(summary): print("   ", key, len(summary[key]), sorted(summary[key])[:4], '...' if len(summary[key]) > 4 else '')
check("on grids N = 8, 12, 24 the only momenta fixed by all of O are +-k* (units of pi: +-(1/2,-1/2,1/2))",
      full_O == {(0.5, -0.5, 0.5), (-0.5, 0.5, -0.5)}, f"{sorted(full_O)}")
gcd4 = [k for k in summary if k[0] == 'Oh' and k[3] % 4 == 0]
check("with inversion, no grid momentum has all level multiplicities divisible by 4 (no momentum-space "
      "obstruction to nu = 2 mod 4)", not gcd4, f"Oh keys with gcd 4: {gcd4}")

# ------------------------------------------------------------------ E
print("\nE. Wyckoff projective classes (exact operator algebra)")
def op(g, t):
    return (OH[g], np.array(t, int), lam[g] % 2, U[g].astype(complex), 1.0 + 0j)
def comp(o2, o1):   # o2 after o1
    M2, t2, l2, U2, p2 = o2; M1, t1, l1, U1, p1 = o1
    return (M2 @ M1, M2 @ t1 + t2, (l1 + M1.T @ l2) % 2, U2 @ U1, p1 * p2 * (-1.0) ** int(np.dot(l2, t1)))
def ratio(oa, ob):
    Ma, ta, la, Ua, pa = oa; Mb, tb, lb, Ub, pb = ob
    assert (Ma == Mb).all() and (ta == tb).all() and ((la - lb) % 2 == 0).all()
    X = pa * Ua; Y = pb * Ub; r = np.vdot(Y.ravel(), X.ravel()) / np.vdot(Y.ravel(), Y.ravel())
    assert np.allclose(X, r * Y); return r
def site_group(w, idx):
    out = []
    for g in idx:
        Mw = [sum(int(OH[g][i, j]) * w[j] for j in range(3)) for i in range(3)]
        t = [w[i] - Mw[i] for i in range(3)]
        if all(x.denominator == 1 for x in t): out.append((g, [int(x) for x in t]))
    return out
def wclass(w, idx):
    S = site_group(w, idx); ops = [op(g, t) for g, t in S]; bad = []
    for (a, oa), (b, ob) in itertools.combinations(list(enumerate(ops)), 2):
        ab, ba = comp(oa, ob), comp(ob, oa)
        if (ab[0] == ba[0]).all() and (ab[1] == ba[1]).all():
            r = ratio(ab, ba)
            if not np.isclose(r, 1): bad.append((S[a][0], S[b][0], np.round(r, 6)))
    return S, bad
x, y, z = Fr(1, 7), Fr(2, 9), Fr(3, 11); h_ = Fr(1, 2); o_ = Fr(0)
WY_O = {'1a': (o_, o_, o_), '1b': (h_, h_, h_), '3c': (o_, h_, h_), '3d': (h_, o_, o_), '6e': (x, o_, o_),
        '6f': (x, h_, h_), '8g': (x, x, x), '12h': (x, h_, o_), '12i': (o_, y, y), '12j': (h_, y, y), '24k': (x, y, z)}
WY_OH = dict(WY_O); del WY_OH['24k']
WY_OH.update({'24k': (o_, y, z), '24l': (h_, y, z), '24m': (x, x, z), '48n': (x, y, z)})

# independent numerical cross-check on the L = 4 torus: commutant multiplicities of the site group
P_ = [C['psg_sign'](lambda q, M=M: C['rot_vert'](M, q), D['u']) for M in OH]
def torus_op(g, t):
    """monomial operator T_t G_g on the L = 4 torus as (image index, sign) per vertex"""
    P, s = P_[g]; VID = C['VID']
    img = np.array([VID[(tuple((vi + ti) % L for vi, ti in zip(VERTS[P[a]][0], t)), VERTS[P[a]][1])] for a in range(D['nV'])])
    return img, (-1.0) ** s
def torus_dims(S, seed=3):
    ops = [torus_op(g, t) for g, t in S]
    Rr = np.random.default_rng(seed); X = Rr.normal(size=(D['nV'],) * 2) + 1j * Rr.normal(size=(D['nV'],) * 2); X = X + X.conj().T
    Y = np.zeros_like(X)
    for img, sg in ops:
        Z = np.zeros_like(X); Z[np.ix_(img, img)] = X * np.outer(sg, sg); Y += Z
    Y /= len(ops)
    return sorted(set(mults(np.linalg.eigvalsh(Y), 1e-8)))
def free_orbit(S):
    ops = [torus_op(g, t)[0] for g, t in S]
    return any(len({int(img[a]) for img in ops}) == len(S) for a in range(D['nV']))

res = {}
for lab, WY, idx in (('P432-type (G)', WY_O, PROPER), ('Pm-3m-type (Gh)', WY_OH, ALL)):
    print(f"   {lab}:")
    for name, w in WY.items():
        S, bad = wclass(w, idx); mult = len(idx) // len(S)
        dims = torus_dims(S) if len(S) > 1 and int(name[:-1]) % 2 == 1 or name in ('6e', '6f') else None
        fo = free_orbit(S) if dims is not None else None
        res[(lab, name)] = (mult, len(S), bool(bad), dims, fo)
        print(f"     {name:4s} multiplicity {mult:2d}  |site group| {len(S):2d}  class {'NONTRIVIAL' if bad else 'trivial'}"
              f"  anticommuting pairs {len(bad)}" + (f"  torus irrep dims {dims} (free orbit {fo})" if dims else ''))
oddO = [n for n in WY_O if res[('P432-type (G)', n)][0] % 2 == 1]
check("G: the odd-multiplicity Wyckoff positions are exactly 1a, 1b, 3c, 3d and all four carry the nontrivial "
      "class (some commuting pair of dressed operators anticommutes); torus commutant gives only even irrep dims there",
      sorted(oddO) == ['1a', '1b', '3c', '3d'] and all(res[('P432-type (G)', n)][2] and res[('P432-type (G)', n)][4]
          and all(d % 2 == 0 for d in res[('P432-type (G)', n)][3]) for n in oddO))
check("G: cross-check of the algebra: positions with cyclic site groups (6e, 6f) carry the trivial class and the "
      "torus commutant shows 1-dim irreps", all(not res[('P432-type (G)', n)][2] and 1 in res[('P432-type (G)', n)][3] for n in ('6e', '6f')))
r1a = res[('Pm-3m-type (Gh)', '1a')]; r1b = res[('Pm-3m-type (Gh)', '1b')]
print(f"   Gh 1a irrep dims {r1a[3]}, 1b irrep dims {r1b[3]}, 3c {res[('Pm-3m-type (Gh)', '3c')][3]}, "
      f"3d {res[('Pm-3m-type (Gh)', '3d')][3]}, 6e {res[('Pm-3m-type (Gh)', '6e')][3]}, 6f {res[('Pm-3m-type (Gh)', '6f')][3]}")
check("Gh: the site (1a) carries only 4-dimensional irreps (inversion exchanges E1/2 and E5/2), so on-site "
      "Slater-determinant atomic insulators have nu in {0, 4, 8, 12} only", r1a[3] == [4])

# ------------------------------------------------------------------ F
print("\nF. constructive band insulators with certified gaps")
def certified_gap(h, nu, N=24):
    ks = m.kgrid(N); E = np.linalg.eigvalsh(m.Hk(h, ks))
    lo, hi = E[:, nu - 1].max(), E[:, nu].min()
    dist = np.sqrt(3) * np.pi / N
    return hi - lo, hi - lo - 2 * m.lipschitz(h) * dist
def irrep_projectors(gs):
    X = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)); X = X + X.conj().T
    Y = sum(U[g] @ X @ U[g].T for g in gs) / len(gs); ev, V = np.linalg.eigh(Y)
    blocks = []; i = 0
    for d in mults(ev): blocks.append(V[:, i:i + d]); i += d
    return blocks
def onsite_insulator(gs, nu):
    """On-site Hamiltonian filling irreducible blocks of the site representation up to nu (if possible)."""
    B = irrep_projectors(gs)
    for sub in itertools.product((0, 1), repeat=len(B)):
        if sum(b.shape[1] for b, s in zip(B, sub) if s) == nu:
            Hs = sum((-1.0 if s else 1.0) * (b @ b.conj().T) for b, s in zip(B, sub))
            return Hs
    return None
okF = True; info = []
for nu in range(0 + 2, 12, 2):
    Hs = onsite_insulator(PROPER, nu)
    if Hs is None: okF = False; info.append((nu, None)); continue
    pert = m.symmetrize(m.random_blocks(rng, 1), D, PROPER); pn = max(np.abs(B).max() for B in pert.values())
    h = m.add({(0, 0, 0): Hs}, pert, 1.0, 0.02 / pn)
    gg, cert = certified_gap(h, nu); okF &= cert > 0; info.append((nu, round(gg, 3), round(cert, 3)))
check("G: for every even nu in 2..10 an on-site atomic Hamiltonian plus a random G-symmetric range-1 hopping has a "
      "certified global gap (grid N = 24 gap minus Lipschitz bound > 0)", okF, f"(nu, grid gap, certified) {info}")

# Gh: nu = 4, 8 on site; nu = 2 mod 4 via Wannier orbitals at other positions
okF2 = True; info2 = []
for nu in (4, 8):
    Hs = onsite_insulator(ALL, nu)
    pert = m.symmetrize(m.random_blocks(rng, 1), D, ALL); pn = max(np.abs(B).max() for B in pert.values())
    h = m.add({(0, 0, 0): Hs}, pert, 1.0, 0.02 / pn); gg, cert = certified_gap(h, nu); okF2 &= cert > 0; info2.append((nu, round(cert, 3)))
check("Gh: nu = 4, 8 realised by on-site atomic insulators plus symmetric hopping, certified gaps", okF2, f"{info2}")

print("   Gh nu = 2, 6, 10 (off-site Wannier bands): see b7_inversion_wannier.py")

# ------------------------------------------------------------------ G
print("\nG. random-Hamiltonian scans (evidence; N = 16 grid, contains k*)")
ks16 = m.kgrid(16)
for lab, idx in (('G', PROPER), ('Gh', ALL)):
    gapped = np.zeros(13, int); n = 0; min_odd_gap = []
    for trial in range(40):
        r_ = 1 + trial % 2; s = [0.1, 0.3, 1.0, 3.0][trial % 4]
        h = m.add(h0, m.symmetrize(m.random_blocks(rng, r_, trial % 3 != 0), D, idx), 1.0, s)
        E = np.linalg.eigvalsh(m.Hk(h, ks16)); n += 1
        for nu in range(1, 12):
            gap = E[:, nu].min() - E[:, nu - 1].max()
            if gap > 1e-9: gapped[nu] += 1
            if nu % 2: min_odd_gap.append(gap)
    print(f"   {lab}: gapped samples per nu (1..11) out of {n}: {gapped[1:12].tolist()}; max odd-nu indirect gap {max(min_odd_gap):.2e}")
    check(f"{lab}: no random symmetric dispersive Hamiltonian is gapped at any odd nu", all(gapped[nu] == 0 for nu in range(1, 12, 2)))

# ------------------------------------------------------------------ H
print("\nH. the runner Weyl model (t1 = -1, t2 = 0.2, X strength 0.05)")
VID = C['VID']; loc0 = D['loc0']; CORN = D['CORN']; DIRS = D['DIRS']
def dmod(x_): return ((x_ + 1) % L) - 1
nbr = [VID[(tuple(x_ % L for x_ in d), c)] for d in [(0,0,0)] + list(DIRS) for c in CORN]
rngX = np.random.default_rng(0)
A = np.zeros((D['nV'], D['nV']))
for i in loc0:
    for j in nbr:
        v, w_ = VERTS[i][0], VERTS[j][0]
        if i != j and sum(abs(dmod(b - a)) for a, b in zip(v, w_)) <= 1: A[i, j] = rngX.normal()
A = A - A.T
Af = 1j * A
hT = {}
for a_, b_ in zip(*np.nonzero(Af)):
    (va, ca), (vb, cb) = VERTS[a_], VERTS[b_]
    d = tuple(dmod(p - q) for p, q in zip(va, vb))
    hT.setdefault(d, np.zeros((12, 12), complex))[CI[ca], CI[cb]] += Af[a_, b_]
hX = m.symmetrize(hT, D, ALL)
hX = {d: B / max(np.abs(BB).max() for BB in hX.values()) for d, B in hX.items()}
hW = m.add(h0, hX, 1.0, 0.05)
EK = np.linalg.eigvalsh(m.Hk(hW, kst)[0]); EN = EK[0]
ks = m.kgrid(48); E = np.linalg.eigvalsh(m.Hk(hW, ks))
below = (E < EN - 1e-12).sum() / len(ks)
print(f"   levels at k*: {np.round(EK[:6], 4)}; node energy E_N = {EN:.5f}")
print(f"   band 1 range [{E[:,0].min():.4f}, {E[:,0].max():.4f}], band 2 [{E[:,1].min():.4f}, {E[:,1].max():.4f}], band 3 [{E[:,2].min():.4f}, {E[:,2].max():.4f}]")
print(f"   states below E_N per site (N = 48 grid): {below:.4f}")
check("the Weyl node at k* is the lowest level there (a doublet), so the node sits between bands 1 and 2: "
      "node filling nu = 1 (odd) -> forced gapless by C", abs(EK[1] - EK[0]) < 1e-9 and EK[2] - EK[1] > 1e-3)
gap12 = E[:, 2].min() - E[:, 1].max()
print(f"   indirect gap between bands 2 and 3 (nu = 2): {gap12:.4f}; between 1 and 2 (nu = 1): {E[:,1].min() - E[:,0].max():.4f}")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   ({time.time() - t0:.0f} s)")
sys.exit(1 if FAIL else 0)
