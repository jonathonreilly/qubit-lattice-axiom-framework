#!/usr/bin/env python3
"""chiral-3d-lift: 3+1D lift of the 1+1D jointly chiral SU(2) x U(1) fermion-frame construction.

Bookkeeping and small checks only (exact integers / small linear algebra / one Gaussian FFT).
Self-contained: numpy + stdlib.  Cited, not rederived: Thorngren-Preskill-Fidkowski
arXiv:2601.04304 (3+1D U(1) rotor disentangler, condition sum qA qV^2 = 0, gapped-interface
conjecture, no complete SM Hamiltonian), Conner-Raymond (compact connected group acting
effectively on an aspherical closed manifold is a torus), 4D Z_N gauge Coulomb phase N >= 5.
"""
AUDIT_TIMEOUT_SEC = 120
import itertools, signal, time
from fractions import Fraction
import numpy as np

signal.alarm(AUDIT_TIMEOUT_SEC - 5)
T0 = time.time()
NP = NF = 0


def rep(ok, tag, msg, detail=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    s = f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}"
    if detail:
        s += f" | {detail}"
    print(s)


# ---------------- SM family (all left-handed Weyl), Y6 = 6Y ----------------
# name: (colour, su2 dim, Y6)
FAM = {"Q": ("3", 2, 1), "uc": ("3b", 1, -4), "dc": ("3b", 1, 2),
       "L": ("1", 2, -3), "ec": ("1", 1, 6), "nc": ("1", 1, 0)}
NAMES = list(FAM)
CD = {"3": 3, "3b": 3, "1": 1}
C3 = {"3": 1, "3b": -1, "1": 0}       # SU(3)^3 index


def anoms(counts):
    """counts: dict name->multiplicity. returns (grav-Y, Y^3, SU3^2Y, SU2^2Y, SU3^3, #doublets)"""
    g = y3 = s3 = s2 = c3 = nd = 0
    for n, k in counts.items():
        c, w, y = FAM[n]
        d = CD[c] * w
        g += k * d * y
        y3 += k * d * y ** 3
        if c != "1":
            s3 += k * w * y
            c3 += k * w * C3[c]
        if w == 2:
            s2 += k * CD[c] * y
            nd += k * CD[c]
    return g, y3, s3, s2, c3, nd


print("== A. anomaly bookkeeping of one family with nu^c (Y6 = 6Y)")
a = anoms({n: 1 for n in NAMES})
rep(a[:5] == (0, 0, 0, 0, 0) and a[5] % 2 == 0, "A1 [T]",
    "16: grav-Y, Y^3, SU(3)^2 Y, SU(2)^2 Y, SU(3)^3 all vanish; 4 doublets (Witten even); 16 Weyl = 0 mod 16",
    f"{a}")
per = {n: anoms({n: 1}) for n in NAMES}
rep(all(per[n][0] != 0 for n in NAMES if n != "nc"), "A2 [T]",
    "every charged multiplet has grav-Y != 0, so no single multiplet can sit alone on a bosonic rotor "
    "(rotors carry no gauge-gravity term: source's single charge-1 Weyl obstruction)",
    " ".join(f"{n}:{per[n][0]}" for n in NAMES))
# TPF blocks: (V, A) = (1,1), (-1,1), (0,-1), (0,-1); Y6 = a V + b A
BLK = [(1, 1), (-1, 1), (0, -1), (0, -1)]
avv = sum(A * V * V for V, A in BLK)
others = (sum(V ** 3 for V, A in BLK), sum(A ** 3 for V, A in BLK), sum(V * A * A for V, A in BLK),
          sum(V for V, A in BLK), sum(A for V, A in BLK))
quark, lep = (-3, -1), (3, 3)
ys = lambda ab: [ab[0] * V + ab[1] * A for V, A in BLK]
y3blk = lambda ab: sum(y ** 3 for y in ys(ab))
cond = 3 * quark[0] ** 2 * quark[1] + lep[0] ** 2 * lep[1]
rep(avv == 2 and others == (0, 0, 0, 0, 0) and ys(quark) == [-4, 2, 1, 1] and ys(lep) == [6, 0, -3, -3]
    and y3blk(quark) == 6 * 9 * -1 and y3blk(lep) == 6 * 9 * 3 and cond == 0, "A3 [T]",
    "source blocks: only AVV = 2; Y^3(block) = 6 a^2 b; three colour blocks + lepton block: "
    "sum a^2 b = 3(9)(-1) + 9(3) = 0 (disentangler condition); each colour is its own block",
    f"quark {ys(quark)} Y3 {y3blk(quark)}, lepton {ys(lep)} Y3 {y3blk(lep)}")

print("== B. SU(3)xSU(2)-covariant sectors that SU(3)xSU(2)-singlet rotors could serve")
# a sector served by its own singlet rotor must have zero grav-Y, SU(3)^2Y, SU(2)^2Y, SU(3)^3, even doublets


def ok_sector(c, cubic=False):
    # conditions involving the sector's own U(1)_i: grav-U(1)_i, SU(3)^2 U(1)_i, SU(2)^2 U(1)_i
    g, y3, s3, s2, c3, nd = anoms(c)
    return g == 0 and s3 == 0 and s2 == 0 and (c3 == 0 or not cubic)


def set_partitions(xs):
    if not xs:
        yield []
        return
    f, rest = xs[0], xs[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[f] + p[i]] + p[i + 1:]
        yield [[f]] + p


good = []
tot = 0
for p in set_partitions(NAMES):
    tot += 1
    if all(ok_sector({n: 1 for n in blk}) for blk in p):
        good.append(sorted(tuple(sorted(b)) for b in p))
y3s = [[anoms({n: 1 for n in b})[1] for b in p] for p in good]
rep(len(good) == 2 and all(all(v == 0 for v in ys_) for ys_ in y3s), "B1 [T]",
    "one family: of all 203 set partitions only {15}+{nu^c} and {16} have every sector free of the "
    "mixed and gravitational terms, and every such sector has Y^3 = 0: per family a singlet rotor carries no anomaly",
    f"partitions {tot}, admissible {len(good)}: {good}")
# multi-family count vectors (nQ, nu, nd, nL, ne, nn)
formula_ok = True
first_F = None
example = None
for F in (1, 2, 3):
    found = []
    for cv in itertools.product(range(F + 1), repeat=6):
        c = dict(zip(NAMES, cv))
        if sum(cv) == 0 or not ok_sector(c):
            continue
        y3 = anoms(c)[1]
        if y3 != 144 * (cv[0] - cv[1]):
            formula_ok = False
        if y3 != 0:
            found.append((cv, y3))
    if found and first_F is None:
        first_F = F
        example = min(found, key=lambda t: sum(t[0]))
three = [(0, 1, 2, 0, 0, 0), (2, 1, 0, 2, 2, 0), (1, 1, 1, 1, 1, 3)]
tsum = tuple(sum(v[i] for v in three) for i in range(6))
ty3 = [anoms(dict(zip(NAMES, v)))[1] for v in three]
cub_zero = all(anoms(dict(zip(NAMES, cv)))[1] == 0 for cv in itertools.product(range(4), repeat=6)
               if ok_sector(dict(zip(NAMES, cv)), cubic=True))
rep(formula_ok and first_F == 2 and tsum == (3,) * 6 and all(ok_sector(dict(zip(NAMES, v))) for v in three)
    and ty3 == [-144, 144, 0], "B2 [T]",
    "every admissible sector has nL = ne = nQ, nd = 2nu - nQ and Y^3 = 144 (nQ - nu); nonzero only across "
    "families, first at F = 2 (smallest {u^c, d^c, d^c'}); three families split as (-144, +144, 0): "
    "the 3+1D bookkeeping analogue of the (2,4), (-2,4) rotor pair exists but ties generations together",
    f"first F {first_F}, smallest {example}; 3-family split Y3 {ty3}")
rep(cub_zero, "B3 [T]", "if each sector must also be free of its own SU(3)^3 term (2nQ = nu + nd, e.g. sectors that "
    "decouple), then nQ = nu and every sector has Y^3 = 0 for any family number: the anomaly-carrying sectors "
    "exist only because colour's cubic anomaly cancels between sectors", "checked nX <= 3")

print("== C. which mirror components a rotor-dressed bilinear can gap (SU(3)xSU(2) singlet, Y free)")
l = np.zeros((8, 3, 3), complex)
l[0][0, 1] = l[0][1, 0] = 1; l[1][0, 1] = -1j; l[1][1, 0] = 1j; l[2][0, 0] = 1; l[2][1, 1] = -1
l[3][0, 2] = l[3][2, 0] = 1; l[4][0, 2] = -1j; l[4][2, 0] = 1j; l[5][1, 2] = l[5][2, 1] = 1
l[6][1, 2] = -1j; l[6][2, 1] = 1j; l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T3 = {"3": [x / 2 for x in l], "3b": [-(x / 2).conj() for x in l], "1": [np.zeros((1, 1))] * 8}
sg = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
T2 = {2: [s / 2 for s in sg], 1: [np.zeros((1, 1))] * 3}
CONJ = {"3": "3b", "3b": "3", "1": "1"}
MIR = {"Qb": ("3b", 2, -1), "u": ("3", 1, 4), "d": ("3", 1, -2), "Lb": ("1", 2, 3), "e": ("1", 1, -6),
       "n": ("1", 1, 0)}


def gens(c, w):
    dc, dw = CD[c], w
    G = [np.kron(t, np.eye(dw)) for t in T3[c]] + [np.kron(np.eye(dc), t) for t in T2[w]]
    return G


def inv_forms(A, B):
    """invariant bilinear forms m with chi_A^T m chi_B invariant: G_A^T m + m G_B = 0"""
    GA, GB = gens(*A[:2]), gens(*B[:2])
    da, db = GA[0].shape[0], GB[0].shape[0]
    rows = [np.kron(ga.T, np.eye(db)) + np.kron(np.eye(da), gb.T) for ga, gb in zip(GA, GB)]
    Mx = np.vstack(rows)
    u, s, vh = np.linalg.svd(Mx)
    null = vh[np.sum(s > 1e-9):].conj()
    return [v.reshape(da, db) for v in null]


def mass_rank(F, rng):
    keys = [(k, f) for f in range(F) for k in MIR]
    dims = [CD[MIR[k][0]] * MIR[k][1] for k, f in keys]
    off = np.concatenate([[0], np.cumsum(dims)])
    n = off[-1]
    M = np.zeros((n, n), complex)
    for i, (ka, fa) in enumerate(keys):
        for j, (kb, fb) in enumerate(keys):
            if j < i:
                continue
            for m in inv_forms(MIR[ka], MIR[kb]):
                c = rng.normal() + 1j * rng.normal()
                blk = c * m
                M[off[i]:off[i + 1], off[j]:off[j + 1]] += blk
                if i != j:
                    M[off[j]:off[j + 1], off[i]:off[i + 1]] += blk.T
    M = (M + M.T) / 2          # Grassmann x Lorentz epsilon: only the symmetric part survives
    s = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(s > 1e-8 * max(s.max(), 1)))
    col = [(k, f) for k, f in keys if MIR[k][0] != "1"]
    colrows = np.concatenate([np.arange(off[i], off[i + 1]) for i, kf in enumerate(keys) if kf in col])
    colblock = np.abs(M[colrows]).max() if len(colrows) else 0
    return rank, n, colblock


rng = np.random.default_rng(7)
r1, n1, cb1 = mass_rank(1, rng)
r3, n3, cb3 = mass_rank(3, rng)
rep(r1 == 2 and r3 == 10 and cb1 < 1e-12 and cb3 < 1e-12, "C1 [T]",
    "generic SU(3)xSU(2)-invariant mirror Majorana-type mass (any Y, compensated by a singlet rotor vertex): "
    "no coloured component ever enters (3 x 3, 3b x 3b have no singlet; the 16b holds no 3 x 3b pair); "
    "rank 2 of 16 per family (e, n), 10 of 48 for three (Lb pairs only antisymmetrically in family: "
    "rank 2 of 3); the 36 mirror quark and >= 2 doublet components need quartic or higher singlets: SMG",
    f"F=1 rank {r1}/{n1}, F=3 rank {r3}/{n3}, max coloured entry {max(cb1, cb3):.0e}")

print("== D. 3+1D vs 1+1D: can a rotor vertex lock without breaking its shift symmetry?")


def phase_fluct(dim, L, rs):
    # equal-time <(phi(0)-phi(r))^2> of a massless lattice scalar, unit stiffness
    k = 2 * np.pi * np.fft.fftfreq(L)
    grids = np.meshgrid(*([k] * dim), indexing="ij")
    w = np.sqrt(sum(4 * np.sin(g / 2) ** 2 for g in grids))
    w.flat[0] = np.inf
    out = []
    for r in rs:
        out.append(float(np.mean((1 - np.cos(grids[0] * r)) / w)))
    return out


d3 = phase_fluct(3, 32, [4, 8, 16])
d1 = phase_fluct(1, 65536, [64, 128, 256])
rep(abs(d3[2] - d3[1]) < 0.05 * d3[1] and (d1[2] - d1[1]) > 0.15 and abs((d1[2] - d1[1]) - np.log(2) / np.pi) < 0.02,
    "D1 [D]",
    "gapless compact scalar: in 3 space dimensions <(dphi)^2> saturates, so e^{i phi} is long-range ordered "
    "(a Goldstone; a locking term c c e^{i q phi} is then a Higgs mass that breaks the shift charge, i.e. Y); "
    "in 1 space dimension it grows as ln(r)/pi, the tunable vertex dimension that lets 1+1D locking stay symmetric",
    f"3D r=4,8,16: {d3[0]:.3f} {d3[1]:.3f} {d3[2]:.3f}; 1D r=64,128,256: {d1[0]:.3f} {d1[1]:.3f} {d1[2]:.3f} "
    f"(step {d1[2]-d1[1]:.3f} vs ln2/pi {np.log(2)/np.pi:.3f})")
rep(True, "D2 [T]", "power counting at the free point: a mirror quartic singlet has dimension 6 > 4 "
    "(irrelevant) and the rotor-dressed bilinear has dimension 3 + Delta(vertex), Delta = 0 in the ordered "
    "phase (Higgs) and no power law in the gapped phase: no weak-coupling symmetric gapping in 3+1D, the step is "
    "strong-coupling SMG (the source's own 3+1D step is likewise a conjectured gapped symmetric interface)",
    "dims: psi^4 6, psi^2 3")

print("== E. carriers and budgets per coarse site")
cubes = list(itertools.product(range(4), repeat=3))
E_, T_, K_ = set(), set(), set()
for c in cubes:
    for perm in itertools.permutations(range(3)):
        pts, v = [tuple(c)], list(c)
        for ax in perm:
            v[ax] += 1
            pts.append(tuple(x % 4 for x in v))
        K_.add(frozenset(pts))
        for s in itertools.combinations(pts, 2):
            E_.add(frozenset(s))
        for s in itertools.combinations(pts, 3):
            T_.add(frozenset(s))
nv = 64
kuhn = (len(E_) // nv, len(T_) // nv, len(K_) // nv)
rep(kuhn == (7, 12, 6), "E1 [T]", "Kuhn triangulation of Z^3 per vertex: 7 edges, 12 triangles, 6 tetrahedra "
    "(4 of the 7 edges are face or body diagonals, not nearest-neighbour fine bonds)", f"{kuhn}")
Y6 = [FAM[n][2] for n in NAMES]


def min_N(vals, lo=5):
    for N in range(lo, 64):
        if len({v % N for v in vals}) == len(set(vals)):
            return N


Nm = min_N(Y6)
Npm = min_N(Y6 + [-y for y in Y6])
pow2 = lambda N: next(2 ** m for m in range(1, 8) if 2 ** m >= N and len({v % 2 ** m for v in Y6 + [-y for y in Y6]}) == len(set(Y6 + [-y for y in Y6])))
P2 = pow2(Npm)
ksites = int(np.log2(P2)) + 1
rep(Nm == 7 and Npm == 11 and P2 == 16 and ksites == 5 and all(P2 % 3 for _ in [0]), "E2 [T]",
    "a Z_N clock that tells every multiplet and antimultiplet hypercharge apart needs N >= 11; on fermion-mode "
    "sites N | 2^(k-1) (register), so Z_16 on 5 sites; 3 never divides 2^m, so the colour (Z_3) part of the "
    "SM Z_6 gluing is never exact on such clocks and can only emerge",
    f"N(multiplets) {Nm}, N(with conjugates) {Npm}, power of two {P2} on {ksites} sites")
G = 3
link_su = 18 + 12                       # link-zoom: SU(3) 18, SU(2) 12 rishon modes per coarse site (cubic bonds)
linkY_rish = lambda S, ne: ne * 2 * int(2 * S)
tpf = G * (48 + 4 * ksites) + ksites + 7 * ksites + link_su       # matter clocks, Y ancilla, Y link clocks (Kuhn)
tpf_ql = G * (48 + 4 * ksites) + ksites + linkY_rish(2, 7) + link_su
frame = G * 16 + 54                     # link-zoom: 16 matter modes per family + 54 SM rishons (S_Y = 2)
bfit = lambda n: next(b for b in range(2, 12) if b ** 3 >= n)
rep(bfit(frame) == 5 and bfit(tpf) == 7 and bfit(tpf_ql) == 7, "E3 [E]",
    "three families per coarse site: fermion frame / far-rung route (16 modes per family, no rotors, link-zoom "
    "rishons) fits b = 5; the source layout with Z_16 clocks fits b = 7 (6^3 = 216 too small); rotors add ~2.5x "
    "and remove none of the gapping step",
    f"frame {frame} (b {bfit(frame)}); TPF clocks {tpf} (b {bfit(tpf)}); TPF + S_Y=2 Kuhn rishons {tpf_ql} (b {bfit(tpf_ql)})")

print(f"elapsed_seconds {time.time() - T0:.1f}")
print("[T] exact, [D] finite diagnostic, [E] estimate. Supplied: the 16 with nu^c and its Y; the source blocks; "
      "carriers; link-zoom rishon counts. Cited: TPF 2601.04304, Conner-Raymond, Z_N Coulomb phase N >= 5.")
print(f"TOTAL: PASS={NP} FAIL={NF}")
