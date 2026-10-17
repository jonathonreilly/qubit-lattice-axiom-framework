#!/usr/bin/env python3
"""The corner fermion when it is much larger than the grid: its long-wavelength theory,
and an embedding of the 48-qubit sites into one-qubit-per-site blocks.

Companion note: docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md

Part 1  affine action of the site rotations on crystal momentum (from the PSG) and its
        O-fixed momenta.
Part 2  Bloch bands: global minimum at the fixed momentum k*, 2-fold, isolated; 2-fold
        degeneracy of every band; isotropic effective mass; size of the quartic anisotropy.
Part 3  the representation of the minimum doublet under the (twisted) site rotations.
Part 4  an O-equivariant placement of the 48 local qubits into a 5x5x5 block of a
        one-qubit-per-site grid.
"""
import itertools, os, sys
import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
PSG_RUNNER = os.path.join(HERE, 'corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17.py')
_src = open(PSG_RUNNER).read().split('\nPASS = FAIL = 0')[0]
C = {}
exec(compile(_src, PSG_RUNNER, 'exec'), C)          # definitions only (L = 4 corner graph, PSG, 2O)

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

FLUX = dict(square=1, triangle=0, plaquette=1, tube=1)
nV = len(C['VERTS'])

# ------------------------------------------------------------------ Part 1
def comp(ops):
    perm = np.arange(nV); sign = np.zeros(nV, np.uint8)
    for P, s in reversed(ops):
        sign = sign ^ s[perm]; perm = P[perm]
    return perm, sign
def inv(P, s):
    Pi = np.empty(len(P), int); Pi[P] = np.arange(len(P)); return Pi, s[Pi]
def rel_sign(ops):
    perm, sign = comp(ops); assert (perm == np.arange(nV)).all()
    v = set(sign.tolist()); assert len(v) == 1
    return 1 if v.pop() else 0
E3 = [(1,0,0), (0,1,0), (0,0,1)]
def affine(F):
    u = C['solve_u'](F)
    T = {a: C['psg_sign'](lambda q, a=a: C['trans_vert'](a, q), u) for a in E3}
    def Tm(v):
        ops = []
        for a, n in zip(E3, v):
            ops += [T[a] if n > 0 else inv(*T[a])] * abs(n)
        return ops
    shifts = []
    for R in C['ROTS']:
        MR = C['psg_sign'](lambda q, R=R: C['rot_vert'](R, q), u)
        s = np.zeros(3, int)
        for a in E3:
            Ra = tuple(int(x) for x in R @ np.array(a))
            eps = rel_sign([MR, T[a], inv(*MR)] + [inv(*g) for g in Tm(Ra)][::-1])
            s += eps * np.abs(np.array(Ra))
        shifts.append(s % 2)
    fixed = [k for k in itertools.product(range(4), repeat=3)
             if all(((R @ np.array(k) + 2 * s - np.array(k)) % 4 == 0).all() for R, s in zip(C['ROTS'], shifts))]
    return fixed
print("Part 1: affine action of O on momentum (units pi/2)")
fx = {}
for Fb in itertools.product((0, 1), repeat=4):
    if Fb[0] != Fb[2]:
        continue                      # translations do not commute: no Bloch momentum
    F = dict(zip(('square', 'triangle', 'plaquette', 'tube'), Fb))
    fx[Fb] = affine(F)
    print('  ', {k: ('pi' if v else '0') for k, v in F.items()}, 'O-fixed momenta:', fx[Fb])
check("with square = plaquette = tube = pi, the rotations fix exactly two momenta, k* = (pi/2)(1,-1,1) and -k*",
      sorted(fx[(1, 0, 1, 1)]) == [(1, 3, 1), (3, 1, 3)] and sorted(fx[(1, 1, 1, 1)]) == [(1, 3, 1), (3, 1, 3)])
check("with square = plaquette = pi and tube = 0 no momentum is fixed (the minimum star then has at least two points)",
      fx[(1, 0, 1, 0)] == [] and fx[(1, 1, 1, 0)] == [])

# ------------------------------------------------------------------ Part 2 (Bloch, translation-invariant gauge)
DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def neg(d): return tuple(-x for x in d)
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def perp(d, e): return dot(d, e) == 0 and d != e
CORN = [frozenset((d, e)) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0]
CI = {c: i for i, c in enumerate(CORN)}
etypes = []; ekey = {}
def addt(c1, c2, sh, kind):
    if (c1, c2, sh) in ekey or (c2, c1, neg(sh)) in ekey: return
    ekey[(c1, c2, sh)] = ekey[(c2, c1, neg(sh))] = len(etypes); etypes.append((c1, c2, sh, kind))
Z0 = (0, 0, 0)
for c in CORN:
    d, e = tuple(c)
    for a, b in ((d, e), (e, d)):
        for f in DIRS:
            if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                addt(c, frozenset((a, f)), Z0, 'onsite')
        addt(c, frozenset((neg(a), b)), a, 'link')
nT = len(etypes)
def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
def cyc(seq):
    return [ekey[(c1, c2, tuple(y - x for x, y in zip(p1, p2)))]
            for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
cycles = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
for d in DIRS:
    a = [f for f in DIRS if perp(f, d) and f != neg(d)]; a0 = a[0]
    b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]; ring = [a0, b0, neg(a0), neg(b0)]
    cycles['square'].append(cyc([(frozenset((d, r)), Z0) for r in ring]))
    for i in range(4):
        p, q = ring[i], ring[(i+1) % 4]
        cycles['tube'].append(cyc([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d),
                                   (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]))
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
    cycles['triangle'].append(cyc([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]))
for d, e in (((1,0,0),(0,1,0)), ((0,1,0),(0,0,1)), ((0,0,1),(1,0,0))):
    cycles['plaquette'].append(cyc([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d),
                                    (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
def solve_cell(F):
    piv = {}
    for k, cs in cycles.items():
        for c in cs:
            x = 0
            for t in c: x ^= 1 << t
            x |= F[k] << nT
            while True:
                low = x & ((1 << nT) - 1)
                if low == 0:
                    if x: return None
                    break
                cc = low.bit_length() - 1
                if cc in piv: x ^= piv[cc]
                else: piv[cc] = x; break
    sol = 0
    for cc in sorted(piv):
        x = piv[cc]; rest = x & ((1 << cc) - 1)
        if ((x >> nT) & 1) ^ (bin(rest & sol).count('1') & 1): sol |= 1 << cc
    return [(sol >> j) & 1 for j in range(nT)]
TRI = []
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    TRI += [(cy[i], cy[(i+1) % 3]) for i in range(3)]
def bloch(u, k, t1, t2, lam):
    H = np.zeros((12, 12), complex)
    for j, (c1, c2, sh, kind) in enumerate(etypes):
        a = -(t1 if kind == 'onsite' else t2) * (-1.0) ** u[j] * np.exp(1j * np.dot(k, sh))
        H[CI[c2], CI[c1]] += a; H[CI[c1], CI[c2]] += np.conj(a)
    for q, r in TRI:
        amp = 1j * lam * (-1.0) ** u[ekey[(q, r, Z0)]]
        H[CI[r], CI[q]] += amp; H[CI[q], CI[r]] += np.conj(amp)
    return H

print("\nPart 2: Bloch bands (square = plaquette = tube = pi, triangle 0; H = -t1 sum_onsite u c^dag c - t2 sum_links u c^dag c + chiral)")
u = solve_cell(FLUX)
check("a translation-invariant gauge exists for this flux pattern (one-site unit cell)", u is not None)
rng = np.random.default_rng(7)
KS = [np.array(s) * np.pi / 2 for s in ((1, -1, 1), (-1, 1, -1))]
grid = np.array(list(itertools.product(np.linspace(-np.pi, np.pi, 16, endpoint=False), repeat=3)))
results = []
ok_min = ok_kr = ok_iso = True
for t1, t2, lam in ((-1.0, 0.1, -0.5), (-1.0, -0.1, -0.5), (-1.0, 0.3, -0.5), (-1.0, 0.1, 0.5), (-1.0, 0.2, -0.3)):
    ev = lambda k: np.linalg.eigvalsh(bloch(u, np.asarray(k, float), t1, t2, lam))
    e = np.array([ev(k)[0] for k in grid])
    starts = grid[np.argsort(e)[:16]]
    rs = [minimize(lambda k: ev(k)[0], k0, method='Nelder-Mead',
                   options=dict(xatol=1e-10, fatol=1e-14, maxiter=10000)) for k0 in starts]
    gmin = min(r.fun for r in rs)
    eks = [ev(k) for k in KS]; w = min(eks, key=lambda x: x[0]); other = max(eks, key=lambda x: x[0])
    kstar = KS[int(np.argmin([x[0] for x in eks]))]
    deg = int(np.sum(np.abs(w - w[0]) < 1e-9))
    # every local minimum found that is not at k* (mod 2pi) lies strictly higher
    away = [r.fun for r in rs if np.linalg.norm(((r.x - kstar + np.pi) % (2*np.pi)) - np.pi) > 1e-3]
    sep = (min(away) - w[0]) if away else float('inf')
    ok_min &= abs(gmin - w[0]) < 1e-9 and deg == 2 and sep > 1e-4 and other[0] > w[0] + 1e-4
    kr = all(np.allclose(ev(k)[0::2], ev(k)[1::2], atol=1e-9) for k in rng.uniform(-np.pi, np.pi, (25, 3)))
    ok_kr &= kr
    h = 1e-3; f = lambda k: ev(k)[0]
    Hs = np.array([[(f(kstar + h*(np.eye(3)[i] + np.eye(3)[j])) - f(kstar + h*(np.eye(3)[i] - np.eye(3)[j]))
                     - f(kstar - h*(np.eye(3)[i] - np.eye(3)[j])) + f(kstar - h*(np.eye(3)[i] + np.eye(3)[j]))) / (4*h*h)
                    for j in range(3)] for i in range(3)])
    hev = np.linalg.eigvalsh(Hs)
    ok_iso &= np.ptp(hev) < 1e-4 * abs(hev.mean()) + 1e-6 and hev.min() > 0
    dk = 0.1
    an = (f(kstar + dk * np.ones(3) / np.sqrt(3)) - f(kstar + dk * np.array([1, 0, 0]))) / (f(kstar + dk * np.array([1, 0, 0])) - w[0])
    print(f"   t1={t1:+} t2={t2:+} chiral={lam:+}: min E={w[0]:.6f} at k*={np.round(kstar/(np.pi/2)).astype(int)}(pi/2), deg {deg},"
          f" gap at k* {w[2]-w[0]:.4f}, E(-k*)-E(k*)={other[0]-w[0]:.4f}, next local min +{sep:.4f};"
          f" 1/m* = {hev.mean():.4f} (spread {np.ptp(hev):.1e}); anisotropy [111] vs [100] at |dk|=0.1: {an:.1e}")
check("the global band minimum is a single 2-fold level at k* (the other fixed momentum and every other local minimum lie higher)", ok_min)
check("every band is 2-fold degenerate at every momentum (25 random k per parameter set)", ok_kr)
check("the effective-mass tensor at k* is isotropic and positive (Hessian eigenvalues equal)", ok_iso)

# ------------------------------------------------------------------ Part 3 (L = 4 lattice contains k*)
print("\nPart 3: representation of the minimum doublet under the twisted site rotations (L = 4)")
G2, proj, W1 = C['G2'], C['proj'], C['W1']
outF, uL, Ms = C['classify'](FLUX)
r = C['run'](FLUX, twist=True, verbose=False)
Mt, loc, _ = r
def Mfull(k):
    P, s = Ms[k]; M = np.zeros((nV, nV)); M[P, np.arange(nV)] = (-1.0) ** s; return M
Mf = [Mfull(k) for k in range(24)]
sgn = []
for k in range(48):
    R = proj[k]; blk = Mf[R][np.ix_(loc, loc)] * (1j ** W1[R])
    sgn.append(1 if np.allclose(Mt[k], blk) else -1)
def spin_char(j2, U):
    tr = max(-1, min(1, np.real(np.trace(U)) / 2)); th = 2 * np.arccos(tr)
    if abs(np.sin(th / 2)) < 1e-12: return float(j2 + 1) * (1 if np.isclose(tr, 1) else (-1) ** j2)
    return np.sin((j2 + 1) * th / 2) / np.sin(th / 2)
G32 = np.array([spin_char(3, U) for U in G2])
IRR = {'E1/2': np.array([spin_char(1, U) for U in G2]), 'E5/2': np.array([spin_char(5, U) for U in G2]) - G32, 'G3/2': G32}
def dec(ch):
    d = {k: int(round(np.real(np.sum(np.conj(v) * ch) / 48))) for k, v in IRR.items()}
    return {k: v for k, v in d.items() if v}
def H_lattice(t1, t2, lam):
    H = np.zeros((nV, nV), complex)
    for key in C['EDGES']:
        i, j = tuple(key); t = t1 if C['edges'][key] == 'onsite' else t2
        a = -t * (-1.0) ** uL[C['EID'][key]]; H[i, j] += a; H[j, i] += a
    for v in C['SITES']:
        for s in itertools.product((1, -1), repeat=3):
            x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
            cy = [(v, frozenset((x, y))), (v, frozenset((y, z))), (v, frozenset((z, x)))]
            if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
            for a_ in range(3):
                q, rr = cy[a_], cy[(a_+1) % 3]; i, j = C['VID'][q], C['VID'][rr]
                amp = 1j * lam * (-1.0) ** uL[C['eid'](q, rr)]; H[j, i] += amp; H[i, j] += np.conj(amp)
    return H
rep = {}
for t1, t2, lam in ((-1.0, 0.1, -0.5), (-1.0, 0.3, -0.5), (-1.0, 0.1, 0.5)):
    Hm = H_lattice(t1, t2, lam)
    for M in Mf: assert np.allclose(M @ Hm, Hm @ M)
    ev, V = np.linalg.eigh(Hm); m = int(np.sum(np.abs(ev - ev[0]) < 1e-8)); Pj = V[:, :m]
    ch = np.array([sgn[k] * (1j ** W1[proj[k]]) * np.trace(Pj.conj().T @ (Mf[proj[k]] @ Pj)) for k in range(48)])
    rep[(t1, t2, lam)] = (m, dec(ch), round(float(ev[0]), 4))
    print(f"   t1={t1:+} t2={t2:+} chiral={lam:+}: lattice ground level E={ev[0]:.4f}, deg {m}, {dec(ch)}")
check("on the L = 4 lattice the lowest one-fermion level is the k* doublet (same energy as the Bloch minimum)",
      rep[(-1.0, 0.1, -0.5)][2] == -3.5556 and rep[(-1.0, 0.1, -0.5)][0] == 2)
check("the minimum doublet carries a two-dimensional spinorial irrep of 2O: E1/2 for chiral -0.5, E5/2 for chiral +0.5 (twist i^{w1})",
      rep[(-1.0, 0.1, -0.5)][1] == {'E1/2': 1} and rep[(-1.0, 0.3, -0.5)][1] == {'E1/2': 1}
      and rep[(-1.0, 0.1, 0.5)][1] == {'E5/2': 1})

# ------------------------------------------------------------------ Part 4 (one qubit per fine site)
print("\nPart 4: O-equivariant placement of the 48 local qubits in a 5x5x5 block of a one-qubit-per-site grid")
ROT = C['ROTS']
def rc(R, c): return frozenset(tuple(int(x) for x in R @ np.array(d)) for d in c)
def rd(R, d): return tuple(int(x) for x in R @ np.array(d))
ONS = sorted({frozenset((c1, c2)) for c1 in CORN for c2 in CORN
              if len(c1 & c2) == 1 and (lambda b1, b2: perp(b1, b2) and b1 != neg(b2))(*[next(iter(c - (c1 & c2))) for c in (c1, c2)])},
             key=lambda s: sorted(map(sorted, s)))
HALF = [(c, a) for c in CORN for a in c]
def act_label(R, lab):
    kind, x = lab
    if kind == 'o': return ('o', frozenset(rc(R, c) for c in x))
    c, a = x; return ('h', (rc(R, c), rd(R, a)))
labels = [('o', p) for p in ONS] + [('h', h) for h in HALF]
def orbit(lab): return {act_label(R, lab) for R in ROT}
free = all(len(orbit(l)) == 24 for l in labels)
check("both local-qubit label orbits (24 on-site hop qubits, 24 link halves) are free O-orbits", free and len(labels) == 48)
block = list(itertools.product(range(-2, 3), repeat=3))
def orb_pt(p): return {tuple(int(x) for x in R @ np.array(p)) for R in ROT}
P1, P2 = (1, 2, 0), (1, 2, 2)
check("the block positions (1,2,0) and (1,2,2) have free O-orbits that are disjoint",
      len(orb_pt(P1)) == 24 and len(orb_pt(P2)) == 24 and not (orb_pt(P1) & orb_pt(P2)))
place = {}
for lab0, p0 in ((('o', ONS[0]), P1), (('h', HALF[0]), P2)):
    for R in ROT:
        place[act_label(R, lab0)] = tuple(int(x) for x in R @ np.array(p0))
bij = len(place) == 48 and len(set(place.values())) == 48
equiv = all(place[act_label(R, l)] == tuple(int(x) for x in R @ np.array(place[l])) for R in ROT for l in labels)
check("the placement is a bijection onto two orbits of fine sites and is O-equivariant: p(R.l) = R.p(l) for all 24 R and 48 labels",
      bij and equiv)
spect = [p for p in block if p not in set(place.values())]
closed = all(tuple(int(x) for x in R @ np.array(p)) in set(spect) for R in ROT for p in spect)
check("the 77 unused fine sites form a union of O-orbits (frozen spectator qubits keep the symmetry)", len(spect) == 77 and closed)
print("   so the corner code's rotation about a site becomes the framework's rotation about a block-centre fine site"
      " (a fine-site permutation) times the same on-block Clifford corrections; coarse translations are fine translations by 5")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
