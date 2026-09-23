#!/usr/bin/env python3
"""J:derive:a-filled-level-of-one-sense-under-exclusion:a1 - worker w-jonathonsmac4f50-j3b8b.

Block 77's family (open PR #8612): one record's generator a0 + 2a sum_j cos k_j + sigma . sin k.
Block 78 / 80 (open PRs #8613, #8615): the Record axiom's exclusion (one record per site at a
time, whatever the coins) makes many records an interacting problem.

Exact parts use sympy / integers.  Parts labelled NUMERIC use floating point (numpy, scipy's
ARPACK) and are evidence, not proof.
"""
import itertools
import os
import sys
import time

import numpy as np
import sympy as sp
from scipy import ndimage
from scipy.sparse.linalg import LinearOperator, eigsh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from manyrec import Torus2D, HardCore, brute_hamiltonian, momentum_rho, point_symmetry, close_manifold  # noqa: E402

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


a, a0, mu = sp.symbols('a a0 mu', real=True)


def nodes(d):
    return list(itertools.product((0, 1), repeat=d))


def sense(n):
    # sign of det of the Jacobian of s = (sin k_1, ..., sin k_d) at k = pi n
    return int(sp.diag(*[sp.cos(sp.pi * nj) for nj in n]).det())


# ---------------------------------------------------------------- A1 levels and senses
ok = True
mult = {}
for d in (3, 2):
    for n in nodes(d):
        E = a0 + 2 * a * sum(sp.cos(sp.pi * nj) for nj in n)
        ok &= sp.simplify(E - (a0 + 2 * a * (d - 2 * sum(n)))) == 0
        ok &= sense(n) == (-1) ** sum(n)
        mult.setdefault(d, {}).setdefault(sum(n), set()).add(sense(n))
ok &= {m: len([n for n in nodes(3) if sum(n) == m]) for m in range(4)} == {0: 1, 1: 3, 2: 3, 3: 1}
ok &= all(len(v) == 1 for d in mult for v in mult[d].values())
check('A1', ok, "(a) EXACT: at the zeros k = pi n the family has energy a0 + 2a(d - 2|n|) and sense "
      "(-1)^|n| (sign of det of d(sin k)/dk): 3D levels 1:3:3:1 with senses +,-,+,- from the top "
      "(a > 0); the 2D slice 1:2:1 with senses +,-,+; every level of one sense (block 77 T1 restated)")


# ---------------------------------------------------------------- A2 gap content
def gap_table(d):
    lv = [d - 2 * m for m in range(d + 1)]          # level energies in units of 2a (a0 = 0), top first
    rows = []
    for g in range(d):
        hi, lo = lv[g], lv[g + 1]
        above = [n for n in nodes(d) if d - 2 * sum(n) >= hi]
        below = [n for n in nodes(d) if d - 2 * sum(n) <= lo]
        rows.append((len(above), sum(sense(n) for n in above), len(below), sum(sense(n) for n in below)))
    return rows


t3, t2 = gap_table(3), gap_table(2)
ok = t3 == [(1, 1, 7, -1), (4, -2, 4, 2), (7, 1, 1, -1)] and t2 == [(1, 1, 3, -1), (3, -1, 1, 1)]
ok &= all(r[1] + r[3] == 0 for r in t3 + t2)
check('A2', ok, "(a) EXACT COUNT (the index sum and the two-band flux relation ASSUMED, ATTEMPT step 2), THE CONTENT IS A PARTITION, NOT A NET SENSE: with mu in a gap, both bands' "
      "Fermi seas contain exactly the zeros below mu, so the degree of s/|s| on either band's Fermi "
      "surface (outward from the sea) is the sum of the senses below mu, the two bands' Berry fluxes "
      "through their surfaces are opposite, and the total (right minus left of all gapless content) is 0 "
      "in every gap for every a; zeros above | below mu: 3D top gap 1 species net +1 | 7 net -1, middle 4 "
      "net -2 | 4 net +2, bottom 7 net +1 | 1 net -1; 2D +1 | -1 and -1 | +1: the lens's 'single "
      "right-handed species' is the side above mu of the top gap",
      f"3D (#above, net above, #below, net below) = {t3}; 2D = {t2}")


# ---------------------------------------------------------------- A3 NUMERIC pockets and sheet degrees
def bands3(k, aa):
    c = np.cos(k).sum(axis=0)
    r = np.sqrt((np.sin(k) ** 2).sum(axis=0))
    return 2 * aa * c - r, 2 * aa * c + r


def periodic_label(mask):
    lab, n = ndimage.label(mask)
    parent = list(range(n + 1))

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    for ax in range(3):
        A, B = np.take(lab, 0, axis=ax), np.take(lab, -1, axis=ax)
        for u, v in zip(A.ravel(), B.ravel()):
            if u and v and find(u) != find(v):
                parent[find(u)] = find(v)
    roots = np.array([find(u) for u in range(n + 1)])
    lab2 = roots[lab]
    lab2[~mask] = 0
    return lab2, sorted(set(np.unique(lab2)) - {0})


def solid_angle(p, q, r):
    num = np.einsum('ij,ij->i', p, np.cross(q, r))
    den = 1 + np.einsum('ij,ij->i', p, q) + np.einsum('ij,ij->i', q, r) + np.einsum('ij,ij->i', r, p)
    return 2 * np.arctan2(num, den)


def degree(region, L):
    """degree of s/|s| on the boundary of a voxel region, oriented outward (sum of solid angles)."""
    h = 2 * np.pi / L
    tot = 0.0
    for ax in range(3):
        o = [q for q in range(3) if q != ax]
        orient = 1 if (o[0], o[1], ax) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1
        for sg in (+1, -1):
            faces = np.argwhere(region & ~np.roll(region, -sg, axis=ax))
            if len(faces) == 0:
                continue
            base = faces.astype(float)
            base[:, ax] += 0.5 + sg * 0.5
            S = []
            for (d1, d2) in [(0, 0), (1, 0), (1, 1), (0, 1)]:
                p = base.copy()
                p[:, o[0]] += d1
                p[:, o[1]] += d2
                v = np.sin(p * h)
                S.append(v / np.linalg.norm(v, axis=1, keepdims=True))
            tot += orient * sg * (solid_angle(S[0], S[1], S[2]) + solid_angle(S[0], S[2], S[3])).sum()
    return tot / (4 * np.pi)


def pockets(aa, m, L=64):
    h = 2 * np.pi / L
    g = (np.arange(L) + 0.5) * h
    k = np.array(np.meshgrid(g, g, g, indexing='ij'))
    Em, Ep = bands3(k, aa)
    rows = []
    for name, mask in (('holes', Em > m), ('electrons', Ep < m)):
        lab, ids = periodic_label(mask)
        for cid in ids:
            reg = lab == cid
            inside = [n for n in nodes(3) if reg[tuple(int(round(np.pi * nj / h - 0.5)) % L for nj in n)]]
            rows.append((name, inside, degree(reg, L)))
    return rows


ok = True
det = []
for m in (0.4, 0.0, -0.4):                       # mid-gaps at a = 1/10
    rows = pockets(0.1, m)
    ok &= len(rows) == 8 and sorted(tuple(r[1][0]) for r in rows) == sorted(nodes(3))
    ok &= all(len(r[1]) == 1 and abs(r[2] - sense(r[1][0])) < 1e-6 for r in rows)
    det.append(f"mu={m}: {sum(1 for r in rows if r[0] == 'holes')} hole + {sum(1 for r in rows if r[0] == 'electrons')} electron pockets")
rows = pockets(1.0, 4.0)                          # a = 1, mid top gap
big = sorted((r[0], len(r[1]), round(r[2], 6)) for r in rows)
ok &= big == [('electrons', 7, -1.0), ('holes', 1, 1.0)]
ok &= [r[1] for r in rows if r[0] == 'holes'] == [[(0, 0, 0)]]
det.append(f"a=1, mu=4: {big}")
check('A3', ok, "(a) NUMERIC (64^3 grid; degrees by solid-angle sums): at a = 1/10 every gap has EIGHT "
      "pockets, one per species, each of degree equal to its species' sense - all eight species are "
      "gapless, four of each sense; at a = 1 in the top gap the only species enclosed is the top one, by "
      "TWO sheets (the lower band's, degree +1 from the node; the upper band's, whose sea holds the other "
      "seven zeros, degree -1): the 'single right-handed species' of the lens, with both branches at the "
      "Fermi level and opposite Berry flux", '; '.join(det))

# ---------------------------------------------------------------- A4 cone comparator
expr = sp.expand(sum((-1) ** m * sp.binomial(3, m) * (mu - a0 - 2 * a * (3 - 2 * m)) ** 3 for m in range(4)))
moments = [sum((-1) ** m * sp.binomial(3, m) * (3 - 2 * m) ** p for m in range(4)) for p in range(4)]
check('A4', expr == -384 * a ** 3 and moments == [0, 0, 0, 48],
      "(a) EXACT IDENTITY, CONE COMPARATOR: sum_i chi_i (mu - E_i)^3 = -384 a^3 for EVERY mu (the moments "
      "sum chi E^p vanish for p = 0, 1, 2), so in the Weyl-cone comparator (unit isotropic cones, "
      "N_i = (mu - E_i)^3/(6 pi^2)) the chiral density sum chi_i N_i = -64 a^3/pi^2 is the same at every "
      "Fermi level: the a-term, not the filling, sets it", f"expansion {expr}; moments {moments}")


# ---------------------------------------------------------------- B1 spectral symmetry
ok = True
for d in (3, 2):
    k = sp.symbols(f'k1:{d + 1}', real=True)
    c, s2 = sum(sp.cos(x) for x in k), sum(sp.sin(x) ** 2 for x in k)
    cp, s2p = sum(sp.cos(x + sp.pi) for x in k), sum(sp.sin(x + sp.pi) ** 2 for x in k)
    ok &= sp.simplify((a0 + 2 * a * cp + sp.sqrt(s2p)) - a0 + (a0 + 2 * a * c - sp.sqrt(s2) - a0)) == 0
    ok &= sp.simplify((a0 + 2 * a * cp - sp.sqrt(s2p)) - a0 + (a0 + 2 * a * c + sp.sqrt(s2) - a0)) == 0
check('B1', ok, "(b) EXACT: k -> k + pi(1,...,1) sends E_+(k) - a0 to -(E_-(k) - a0) and E_- to -E_+, so "
      "the one-record spectrum on Z^d and on every even torus is symmetric about a0: exactly half of the "
      "2 N_s states lie on each side (states at a0 split evenly)")


# ---------------------------------------------------------------- B2 free fillings against the exclusion
def torus_energies(d, L, aa):
    ks = [sp.Rational(2 * m, L) * sp.pi for m in range(L)]
    E = []
    for k in itertools.product(ks, repeat=d):
        c = sp.nsimplify(sum(sp.cos(x) for x in k))
        s2 = sp.nsimplify(sum(sp.sin(x) ** 2 for x in k))
        E += [2 * aa * c + sp.sqrt(s2), 2 * aa * c - sp.sqrt(s2)]
    return E


ok = True
det = []
for d, L, aa, want in ((3, 4, sp.Rational(1, 12), [70, 64, 58]), (2, 4, sp.Rational(1, 8), [18, 14])):
    E = torus_energies(d, L, aa)
    lv = [2 * aa * (d - 2 * m) for m in range(d + 1)]
    got = []
    for g in range(d):
        hi, lo = lv[g], lv[g + 1]
        ok &= not any((e - lo) > 0 and (hi - e) > 0 for e in E)     # no state strictly inside the gap
        got.append(sum(1 for e in E if ((hi + lo) / 2 - e) > 0))
    ok &= got == want
    det.append(f"{L}^{d} torus (a = {aa}): gaps top->bottom need {got} records on {L ** d} sites")
check('B2', ok, "(b) EXACT, THE LENS'S FILLING DOES NOT EXIST UNDER EXCLUSION: the exclusion allows at most "
      "one record per site, N <= N_s, while by B1 a Fermi level in the top gap needs more: at least N_s + 6 "
      "in 3D (the second level's six states lie between a0 and mu) and N_s + 2 in 2D (half the middle "
      "level's four) on every even torus; the middle 3D gap is one record per site on the 4^3 torus; only the bottom gap is "
      "reachable", '; '.join(det))


# ---------------------------------------------------------------- B3 the jam
ok = True
lat43 = Torus2D(4, 3)
jam = HardCore(lat43, 12, 0.3, 0.17, -1)
ok &= len(jam.hops) == 0 and jam.dim == 4096
rng = np.random.default_rng(3)
v = rng.normal(size=jam.dim) + 1j * rng.normal(size=jam.dim)
v /= np.linalg.norm(v)
ok &= np.array_equal(jam.matvec(v), 0.3 * 12 * v)
D = jam.one_body_dm(v[:, None])[0]
off = max(abs(D[2 * x + al, 2 * y + be]) for x in range(12) for y in range(12) if x != y for al in range(2) for be in range(2))
ok &= off == 0
nk = [np.trace(r).real for r in momentum_rho(lat43, D).values()]
ok &= max(abs(q - 1) for q in nk) < 1e-12
for sg in (-1, 1):
    ok &= len(HardCore(Torus2D(4, 4), 16, 0.0, 0.125, sg).hops) == 0
check('B3', ok, "(b) EXACT, THE JAM: with one record on every site every move needs an empty target, so "
      "the compressed generator is a0 N times the identity on all 2^N coin configurations and every "
      "off-site one-body element <c^dag_x c_y> (x != y) vanishes: n(k) = 1 at every k for every state - "
      "no species is singled out (block 85 T2(b) has the zero generator at a0 = 0)",
      f"4x3, 12 records: 4096 states, no moves, max |<c^dag_x c_y>| (x != y) = {off}, n(k) = 1 at all 12 k; 4x4, 16 records: no moves")


# ---------------------------------------------------------------- B4 the many-record code
ok = True
det = []
lat33 = Torus2D(3, 3)
for N in (1, 2, 3):
    for sg in (-1, 1):
        hc = HardCore(lat33, N, 0.3, 0.17, sg)
        states, Hb = brute_hamiltonian(lat33, N, 0.3, 0.17, sg)
        idx = {s: i for i, s in enumerate(states)}
        perm = [idx[t] for t in hc.modes()]
        ok &= np.array_equal(hc.dense(), Hb[np.ix_(perm, perm)])
lat44 = Torus2D(4, 4)
tr = {}
for sg in (-1, 1):
    H = HardCore(lat44, 2, 0.0, 0.0, sg).dense()
    tr[sg] = (np.trace(H @ H).real / 480, np.trace(H @ H @ H @ H).real / 480)
ok &= abs(tr[-1][0] - 28 / 15) < 1e-12 and abs(tr[1][0] - 28 / 15) < 1e-12
ok &= abs(tr[-1][1] - 119 / 15) < 1e-12 and abs(tr[1][1] - 39 / 5) < 1e-12
check('B4', ok, "(b) CHECKED: the many-record generator used below equals, entry by entry, an independent "
      "construction (mode tuples, Jordan-Wigner signs) on the 3x3 torus for 1-3 records and both exchange "
      "signs, and reproduces block 78's 4x4 two-record traces (tr H^2/dim = 28/15 for either sign; tr H^4/dim "
      "= 119/15 antisymmetric, 39/5 symmetric)",
      f"4x4 traces: {tr[-1][0]:.10f}, {tr[-1][1]:.10f} (anti), {tr[1][1]:.10f} (sym)")


# ---------------------------------------------------------------- B5 NUMERIC 14 records on the 4x4 slice
def free_zero_occupations(lat, N, aa):
    h = lat.one_record(0.0, aa)
    e, U = np.linalg.eigh(h)
    ok_gap = e[N] - e[N - 1] > 1e-9
    D = U[:, :N].conj() @ U[:, :N].T              # D[i, j] = <c^dag_i c_j>
    R = momentum_rho(lat, D)
    return ok_gap, {kk: np.trace(R[kk]).real / 2 for kk in ((2, 2), (2, 0), (0, 2), (0, 0))}


ok = True
det = []
steps = {}
E14 = {}
for sg in (-1, 1):
    for aa in (1 / 8, 1 / 16):
        t0 = time.time()
        hc = HardCore(lat44, 14, 0.0, aa, sg)
        op = LinearOperator((hc.dim, hc.dim), matvec=hc.matvec, dtype=complex)
        r = np.random.default_rng(11)
        v0 = r.normal(size=hc.dim) + 1j * r.normal(size=hc.dim)
        w, V = eigsh(op, k=4, which='SA', v0=v0, tol=1e-10, ncv=20)
        o = np.argsort(w)
        w, V = w[o], V[:, o]
        g0 = int(np.sum(np.abs(w - w[0]) < 1e-6))
        # the full ground manifold: close ARPACK's ground vectors under the slice's rotation and reflection
        Vg, res = close_manifold(hc, V[:, :g0], point_symmetry(lat44, aa), w[0])
        g = Vg.shape[1]
        ok &= res < 1e-5
        # crystal momentum of the ground manifold
        M1 = Vg.conj().T @ np.column_stack([hc.translate(Vg[:, i], 1, 0) for i in range(g)])
        M2 = Vg.conj().T @ np.column_stack([hc.translate(Vg[:, i], 0, 1) for i in range(g)])
        mom = (np.allclose(np.linalg.eigvals(M1), -1), np.allclose(np.linalg.eigvals(M2), -1))
        D = hc.one_body_dm(Vg).mean(axis=0)
        R = momentum_rho(lat44, D)
        occ = {kk: np.trace(R[kk]).real / 2 for kk in ((2, 2), (2, 0), (0, 2), (0, 0))}   # per state
        gap_ok, free = free_zero_occupations(lat44, 14, aa)
        o3, o2, o2b, o1 = occ[(2, 2)], occ[(2, 0)], occ[(0, 2)], occ[(0, 0)]
        ok &= abs(np.trace(D).real - 14) < 1e-8 and gap_ok and mom == (True, True)
        ok &= abs(o2 - o2b) < 1e-8 and o3 > o2 > o1 and (o3 - o1) < 0.08
        ok &= abs(free[(2, 2)] - 1) < 1e-9 and max(abs(free[kk]) for kk in ((2, 0), (0, 2), (0, 0))) < 1e-9
        steps[(sg, aa)] = (o3 - o2, o2 - o1)
        E14[(sg, aa)] = w[0]
        det.append(f"{'anti' if sg < 0 else 'sym'} a={aa}: E0={w[0]:.6f} (x{g}, residual {res:.0e}, next {(w[g0] if g0 < len(w) else float('nan')):.6f}, momentum (pi,pi)), per-state "
                   f"occupation at the zeros (pi,pi)/(pi,0)/(0,0) = {o3:.3f}/{o2:.3f}/{o1:.3f} [free 1/0/0] "
                   f"({time.time() - t0:.0f}s)")
ratios = []
for sg in (-1, 1):
    for i in range(2):
        rt = steps[(sg, 1 / 8)][i] / steps[(sg, 1 / 16)][i]
        ratios.append(round(rt, 2))
        ok &= 1.5 < rt < 3.0
det.append(f"steps' ratios a = 1/8 over a = 1/16: {ratios}")
check('B5', ok, "(b) EXECUTED, NOT CLAIMED (NUMERIC): the reachable mirror of the lens's filling - 14 "
      "records on the 4x4 slice, the free sea's bottom gap, where the free sea has the (pi,pi) species "
      "(sense +) full and the other three empty - has under exclusion, for either exchange sign and a = 1/8, "
      "1/16, a ground manifold (ARPACK's lowest vectors closed under the slice's rotation and reflection) at crystal momentum (pi,pi) whose per-state occupations at the four zeros differ "
      "by less than 0.08 (free: by 1), ordered by level energy across both senses, the differences "
      "shrinking with a (ratios 1.5-3 when a halves): no species is singled out, the free content is not of one sense and does not "
      "survive", '; '.join(det))


# ---------------------------------------------------------------- B6 NUMERIC the same chemical potential
ok = True
det = []
for sg in (-1, 1):
    aa = 1 / 8
    hc = HardCore(lat44, 15, 0.0, aa, sg)
    op = LinearOperator((hc.dim, hc.dim), matvec=hc.matvec, dtype=complex)
    r = np.random.default_rng(5)
    w15 = np.sort(eigsh(op, k=3, which='SA', v0=r.normal(size=hc.dim) + 1j * r.normal(size=hc.dim),
                        tol=1e-10, ncv=16)[0])[0]
    mu15 = w15 - E14[(sg, aa)]                 # cost of the 15th record
    mu16 = (0.0 - E14[(sg, aa)]) / 2          # the jam's energy is a0 N = 0: mean cost of the last two
    ok &= mu15 > 4 * aa + 0.5 and mu16 > 4 * aa + 0.5
    det.append(f"{'anti' if sg < 0 else 'sym'}: E0(15) = {w15:.6f}, E0(15) - E0(14) = {mu15:.3f}, (E0(16) - E0(14))/2 = {mu16:.3f} against 4a = 0.5")
check('B6', ok, "(b) EXECUTED, NOT CLAIMED (NUMERIC): read the lens's filling instead as a chemical potential "
      "in the free top gap (0, 4a): on the 4x4 slice at a = 1/8 the hard-core ground state then holds at "
      "most 14 records, for either exchange sign - adding a 15th record or filling to the jam costs more "
      "than 4a by a margin above 0.5 - so the same chemical potential also lands at or below the bottom "
      "gap's filling", '; '.join(det))

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
s18 = steps[(-1, 1 / 8)]
print("SUMMARY: PARTIAL, exact: the free content at a Fermi level between block 77's levels is a partition "
      "of the species (above | below mu: 3D +1|-1, -2|+2, +1|-1), its net sense (the sum of the Fermi "
      "surfaces' Berry fluxes) is 0 in every gap for every a, and in the Weyl-cone comparator the chiral "
      "density -64a^3/pi^2 does not depend on the filling; under the Record axiom's exclusion the top-gap "
      "filling does not exist (the spectrum is symmetric about a0, so it needs more records than sites: "
      "70 on 64 on the 4^3 torus), the middle 3D gap is the jam (generator a0 N, n(k) = 1), and on the "
      "4x4 slice the reachable bottom-gap filling (14 records) has, executed for both exchange signs, "
      f"occupations at the four zeros within 0.08 of each other (steps {s18[0]:.3f}, {s18[1]:.3f} per state "
      "at a = 1/8, antisymmetric) against the free sea's 1/0/0")
if all(RESULTS):
    print("HIT: for block 77's family a0 + 2a sum cos k + sigma . sin k: (i) at every Fermi level between its "
          "levels, on Z^3 and every even torus, both bands' Fermi seas contain the same zeros, so the Fermi "
          "surfaces' Berry fluxes sum to zero and the gapless content is a partition of the species by level "
          "(above | below mu: +1|-1, -2|+2, +1|-1), never a net sense; (ii) the spectrum is symmetric about a0, "
          "so a Fermi level in the top gap needs more records than sites (at least N_s + 6 in 3D; 70 on the "
          "64-site 4^3 torus): under the Record axiom's exclusion that filling does not exist, the middle gap "
          "on the 4^3 torus is exactly one record per site, where every move is blocked and n(k) = 1 at every "
          "k, and only the bottom gap is reachable")
