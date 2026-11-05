AUDIT_INPUT_PATHS = ('docs/THE_FAMILY_IMAGE_OF_THE_TWO_TILINGS_IS_S3_AND_INVERSION_CLOSED_ZOOM_CHARGES_HAVE_AT_MOST_TWO_SPURION_DISTANCES_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""family-charge-search: is there a family grading with three distinct pairwise spurion distances
(a Froggatt-Nielsen-capable charge) in the rules' structure, keeping three light families?

A  point groups of CL-1's two tilings, and which A4/S4 triplets exist (exact, enumerated)
B  zoom-b families: fixed positions, conserved characters, three-distance triples, the turn-anomaly filter (exact)
C  textures for the viable gradings: tropical exponents (exact) and fit-free ensembles vs measurement [E]
D  lepton mixing from the residual symmetries that do exist, and the A4 (tribimaximal) reading [E]
Tags: [T] exact/enumerated, [E] finite ensemble or estimate, [M] measured input.
"""
import itertools, heapq, time
import numpy as np

AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261022)
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

# ---------------- A: point groups ----------------
print("== A. symmetry of CL-1's two tilings (cubes {0,1}^3+2n even, +(1,1,1) odd)")
SP = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[i, p[i]] = s[i]
        SP.append(R)
def tiling_action(R, centre2):
    """doubled coords: X -> c + R(X - c). Returns 'AA' (even->even, odd->odd), 'AB' (swap) or None."""
    c = np.array(centre2)
    out = set()
    for par in (0, 1):
        for n in itertools.product(range(-1, 2), repeat=3):
            m = 2 * np.array(n) + par
            pts = [2 * (m + np.array(v)) for v in itertools.product((0, 1), repeat=3)]
            img = [c + R @ (X - c) for X in pts]
            if any(np.any(x % 2) for x in img): return None
            img = [x // 2 for x in img]; mn = np.min(img, axis=0)
            if {tuple(x - mn) for x in img} != set(itertools.product((0, 1), repeat=3)): return None
            q = mn % 2
            if not (np.all(q == q[0])): return None
            out.add((par, int(q[0])))
    if out == {(0, 0), (1, 1)}: return "AA"
    if out == {(0, 1), (1, 0)}: return "AB"
    return None
site = [tiling_action(R, (0, 0, 0)) for R in SP]; cube = [tiling_action(R, (1, 1, 1)) for R in SP]
nS = sum(a is not None for a in site); nSA = site.count("AA"); nC = sum(a is not None for a in cube); nCA = cube.count("AA")
check("[T] about a site the tilings keep only the signed permutations with equal signs, D3d (12), and only C3v (6) keeps "
      "even cubes even (the copy mass); about a cube centre all 48 of O_h keep both tilings and even cubes even",
      (nS, nSA, nC, nCA) == (12, 6, 48, 48), f"site {nS}/{nSA}, cube centre {nC}/{nCA}")
rot = [R for R in SP if round(np.linalg.det(R)) == 1]
Tgrp = [R for R in rot if np.prod([R[i, j] for i in range(3) for j in range(3) if R[i, j]]) == 1 and
        round(np.linalg.det(np.abs(R))) == 1]
site_rot = [R for R, a in zip(SP, site) if a is not None and round(np.linalg.det(R)) == 1]
TinS = sum(any(np.array_equal(R, S) for S in site_rot) for R in Tgrp)
check("[T] the tetrahedral rotations T = A4 (12) meet the site group only in the turn C3 about (1,1,1): A4/S4 is not "
      "a site symmetry; it is one only about a cube centre", len(Tgrp) == 12 and TinS == 3, f"|T|={len(Tgrp)}, |T cap site|={TinS}")
def irr_norm(chis): return np.mean(np.array(chis) ** 2)
diags = [np.array(d) for d in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))]
def diag_perm_char(R):
    return sum(any(np.array_equal(R @ d, s * d) for s in (1, -1)) for d in diags)
chi_d = [diag_perm_char(R) - 1 for R in Tgrp]; chi_v = [np.trace(R) for R in Tgrp]; chi_ax = [np.trace(np.abs(R)) for R in Tgrp]
check("[T] cube-centred A4 triplets: the four body diagonals give 1 + 3 with the 3 irreducible (<chi,chi> = 1), the "
      "signed axes (the hop vector) give an irreducible 3, while the unsigned axes give 1 + 1' + 1'' (<chi,chi> = 3): "
      "permuted axes are the Z_3 characters again, since the Klein four-group acts trivially on them",
      np.isclose(irr_norm(chi_d), 1) and np.isclose(irr_norm(chi_v), 1) and np.isclose(irr_norm(chi_ax), 3),
      f"<chi,chi>_T: diagonals-1 {irr_norm(chi_d):.0f}, signed axes {irr_norm(chi_v):.0f}, unsigned axes {irr_norm(chi_ax):.0f}")
ok = True
for R in rot:
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    ok &= np.isclose((np.trace(R) - np.trace(np.abs(R))) * np.cos(th / 2), 0)
check("[T] with spin 1/2 attached, E1/2 x T1 and E1/2 x (A1 + E) have equal characters on the binary octahedral group "
      "(they differ only on half-turns, where chi_1/2 = 0): the lattice spectrum cannot tell a signed-axis triplet from "
      "permuted axes; the low-energy Dirac operator decides, and the cubic-cell result (Dirac walk x 1_F) gives F = A1+E",
      ok, "all 24 rotations")
w = np.exp(2j * np.pi / 3)
Tr = np.diag([1, w ** 2, w]); Inv = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], complex)
G = [np.eye(3, dtype=complex)]
while True:
    new = [g @ h for g in G for h in (Tr, Inv)]
    add = [x for x in new if not any(np.allclose(x, y) for y in G)]
    if not add: break
    G += [x for i, x in enumerate(add) if not any(np.allclose(x, y) for y in add[:i])]
chiG = [np.trace(g) for g in G]; nab = not np.allclose(Tr @ Inv, Inv @ Tr)
check("[T] on the zoom-3 families (characters (j,j,j)) the site space group acts through T(2e_i) and the cube-centred "
      "inversion j -> -j only (C3 and the mirrors fix each family): the image is S3 with 3 = 1 + 2, no A4 or S4 triplet, "
      "and families 1, 2 form the degenerate doublet", len(G) == 6 and nab and np.isclose(np.mean(np.abs(chiG) ** 2), 2),
      f"|image| = {len(G)}, nonabelian {nab}, <chi,chi> = {np.mean(np.abs(chiG) ** 2):.0f}")

# ---------------- B: zoom-b families ----------------
print("== B. families at zoom b")
ok = True; rows = []
for b in range(2, 13):
    pts = list(itertools.product(range(b), repeat=3)); fixed = [x for x in pts if x == (x[1], x[2], x[0])]
    bp = len({(2 * x[0]) % b for x in fixed})
    ok &= len(fixed) == b and (b ** 3 - b) % 3 == 0 and bp == b // np.gcd(b, 2)
    rows.append((b, len(fixed), bp))
check("[T] at zoom b the turn fixes exactly the b diagonal positions (the rest are three-cycles), all with the same "
      "turn charge, so b chiral families; CL-1's period 2 conserves only b' = b/gcd(b,2) characters of T(2e_i) on them "
      "(for even b, positions j and j+b/2 are one character: CL-1's two copies)", ok,
      "(b, fixed, b') " + " ".join(f"{r[0]}:{r[1]},{r[2]}" for r in rows[:8]))
def ndist(S, N): return len({min((a - c) % N, (c - a) % N) for a, c in itertools.combinations(S, 2)})
first = min(N for N in range(2, 20) if any(ndist(S, N) == 3 for S in itertools.combinations(range(N), 3)))
sym_max = max(ndist(S, N) for N in range(3, 40) for S in itertools.combinations(range(N), 3)
              if {(-s) % N for s in S} == set(S))
check("[T] three distinct cyclic distances first occur in Z_6 ({0,1,3}); in every Z_N (N < 40) a negation-closed "
      "triple has at most two, so with the tick's k -> -k (inversion) unbroken no zoom gives a tower",
      first == 6 and sym_max == 2, f"first N = {first}, max distances of negation-closed triples = {sym_max}")
viable = [b for b in range(3, 31) if b % 3 == 0 and b // np.gcd(b, 2) >= 6]
check("[T] filter (register's conditional count rule: the turn-SU(2) anomaly 4N mod 3 must vanish for the light and for "
      "any gapped set, and b' >= 6): zoom 7 has 4*7 = 1 mod 3 and fails; the smallest viable zooms are 9 (Z_9) and 12 "
      "(Z_6); both need b - 3 chiral families removed by a family-selective symmetric gapping term no law supplies",
      viable[:3] == [9, 12, 15] and (4 * 7) % 3 == 1, f"viable b <= 30: {viable}")
print("   [M] measured light families: Z width N_nu = 2.984 +- 0.008; a 4th chiral family is excluded by Higgs rates")

# ---------------- C: textures ----------------
print("== C. textures: M_ij ~ eps^f(qQ_i - qR_j +- h), f = spurion distance, H~ = i s2 H^* carries -h")
def dijkstra(N, steps):
    dist = {0: 0.0}; pq = [(0.0, 0)]
    while pq:
        d, x = heapq.heappop(pq)
        if d > dist.get(x, 1e9): continue
        for c, wt in steps:
            y = (x + c) % N
            if d + wt < dist.get(y, 1e9) - 1e-12: dist[y] = d + wt; heapq.heappush(pq, (d + wt, y))
    return dist
def E_of(SQ, SR, h, N, f): return np.array([[f[(a - c + h) % N] for c in SR] for a in SQ])
def trop(E):
    a1 = E.min()
    a12 = min(E[i, k] + E[j, l] for i, j in itertools.combinations(range(3), 2) for k, l in itertools.permutations(range(3), 2))
    a123 = min(sum(E[i, p[i]] for i in range(3)) for p in itertools.permutations(range(3)))
    return a1, a12 - a1, a123 - a12
LAWS = {9: dict(unit=dijkstra(9, [(1, 1.), (8, 1.)]), graded=dijkstra(9, [(3, 1.), (6, 1.), (1, 2.), (8, 2.)])),
        6: dict(unit=dijkstra(6, [(1, 1.), (5, 1.)])), 15: dict(unit=dijkstra(15, [(1, 1.), (14, 1.)]))}
TRI = {N: [S for S in itertools.combinations(range(N), 3) if S[0] == 0 and ndist(S, N) == 3] for N in LAWS}
ok = True; best_up = 0; bnd = True
for N, laws in LAWS.items():
    for f in laws.values():
        for S in TRI[N]:
            for h in range(N):
                Eu = E_of(S, S, h, N, f); Ed = E_of(S, S, -h, N, f)
                ok &= np.array_equal(Ed, Eu.T) and trop(Eu) == trop(Ed)
                tu = trop(Eu); bnd &= tu[2] - tu[0] <= 3 * max(f.values()) + 1e-9
                best_up = max(best_up, tu[2] - tu[0])
check("[T] one triple for doublets and singlets (as positions force) and one Higgs: E_d = E_u^T exactly, so up and down "
      "have identical leading mass exponents for every triple, h and spurion law; the diagonal costs f(h) in both, so "
      "log_eps(m1/m3) <= 3 max f", ok and bnd, f"max log_eps(m1/m3) at one triple: {best_up:.0f} (Z_6, Z_9, Z_15)")
MEAS = dict(u32=7e-3, u21=1e-5 / 7e-3, d32=2e-2, d21=1e-3 / 2e-2, Vus=0.225, Vcb=0.042, Vub=0.0037)
print("   [M] targets as in zoom-tower: m_t:m_c:m_u 1:7e-3:1e-5, m_b:m_s:m_d 1:2e-2:1e-3, |V| .225/.042/.0037; "
      f"up/down hierarchy ratio (m_u m_c/m_t^2)/(m_d m_s/m_b^2) = {1e-5 * 7e-3 / (1e-3 * 2e-2):.1e}")
W = np.log10(3.0); NS = 100
def coeff(*sh): return np.exp(rng.uniform(np.log(1 / 3), np.log(3), sh)) * np.exp(2j * np.pi * rng.uniform(size=sh))
def obs(Eu, Ed, eps, ns=NS):
    Mu = coeff(ns, 3, 3) * eps ** Eu; Md = coeff(ns, 3, 3) * eps ** Ed
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)
    V = np.abs(np.conj(np.swapaxes(Uu, 1, 2)) @ Ud)
    return dict(u32=su[:, 1] / su[:, 0], u21=su[:, 2] / su[:, 1], d32=sd[:, 1] / sd[:, 0], d21=sd[:, 2] / sd[:, 1],
                Vus=V[:, 2, 1], Vcb=V[:, 1, 0], Vub=V[:, 2, 0])
def score(o):
    hq = np.all([np.abs(np.log10(o[k] / MEAS[k])) < W for k in MEAS], axis=0)
    hm = np.all([np.abs(np.log10(o[k] / MEAS[k])) < W for k in ("u32", "u21", "d32", "d21")], axis=0)
    return hq.mean(), hm.mean(), sum(np.log10(np.median(o[k]) / MEAS[k]) ** 2 for k in MEAS)
def canon(S, N): return min(tuple(sorted((x + t) % N for x in S)) for t in range(N))
CL = {N: sorted({canon(S, N) for S in TRI[N]}) for N in TRI}
fx = {N: max(LAWS[N]["unit"].values()) for N in LAWS}
okc = True; mx = {}
for N in (9, 15):
    f = LAWS[N]["unit"]; m = 0
    trip = list(itertools.product(CL[N], repeat=2))
    for SQ, SR in trip:
        for h in range(N):
            E = E_of(SQ, SR, h, N, f); E = E - E.min(); t3 = trop(E)
            okc &= t3[1] + t3[2] <= 2 * fx[N] + 1e-9; m = max(m, t3[1] + t3[2])
    mx[N] = m
need = {e: np.log(7e-8) / np.log(e) for e in (0.22, 1 / 3)}
check("[T] cyclic ceiling: in Z_N every entry costs at most floor(N/2) above the cheapest, so the permutation through "
      "the cheapest entry bounds log_eps(m1 m2/m3^2) <= 2 floor(N/2) for ANY doublet and singlet triples and h; the up "
      "quarks need 10.9 (eps 0.22) or 15.0 (eps 1/3) at leading order, so Z_9 and Z_6 cannot hold the up tower and the "
      "anomaly-filtered zooms that can start at b = 15 (eps 0.22) or b = 21 (eps 1/3)",
      okc and mx[9] <= 8 and need[0.22] > 8,
      f"max log_eps(m1m2/m3^2): Z_9 {mx[9]:.0f}, Z_15 {mx[15]:.0f}; classes Z_9 {len(CL[9])}, Z_15 {len(CL[15])}")
cellsA = []
for N, laws in LAWS.items():
    for ln, f in laws.items():
        for S in CL[N]:
            for h in range(N):
                Eu = E_of(S, S, h, N, f); Ed = E_of(S, S, -h, N, f)
                for eps in (1 / 3, 0.22):
                    cellsA.append((score(obs(Eu - Eu.min(), Ed - Ed.min(), eps)), N, ln, S, h, eps))
bA = max(cellsA, key=lambda c: (c[0][0], -c[0][2])); bAc = min(cellsA, key=lambda c: c[0][2])
bAm = max(c[0][1] for c in cellsA)
FN = obs(np.add.outer([3, 2, 0], [4, 1, 0]).astype(float), np.add.outer([3, 2, 0], [1, 0, 0]).astype(float), 0.22, 2000)
sF = score(FN); AN = score(obs(np.zeros((3, 3)), np.zeros((3, 3)), 0.22, 2000))
check("[E] rule-shaped grading (one three-distance triple for all fields, one Higgs, Z_6/Z_9/Z_15, unit or rung-graded "
      "spurions, eps in {1/3, 0.22}): no cell reaches the supplied-U(1) control; up and down cannot differ",
      bA[0][0] < 0.5 * sF[0], f"{len(cellsA)} cells x {NS}; best joint {bA[0][0]:.3f}, best mass-only {bAm:.3f}; "
      f"best chi {bAc[0][2]:.2f} (Z_{bAc[1]},S={bAc[3]},h={bAc[4]}); FN control joint {sF[0]:.3f} mass {sF[1]:.3f} "
      f"chi {sF[2]:.2f}; anarchy joint {AN[0]:.3f}")
# maximal supply: independent light triples for Q, u^c, d^c (translation classes; a common shift is absorbed in h)
res = {}
for N, nmax in ((9, None), (15, 40000)):
    f = LAWS[N]["unit"]; allc = [(a, b_, c, h) for a in CL[N] for b_ in CL[N] for c in CL[N] for h in range(N)]
    if nmax: allc = [allc[i] for i in rng.choice(len(allc), nmax, replace=False)]
    r = []
    for SQ, Su, Sd, h in allc:
        Eu = E_of(SQ, Su, h, N, f); Ed = E_of(SQ, Sd, -h, N, f)
        r.append((score(obs(Eu - Eu.min(), Ed - Ed.min(), 0.22, 40))[0], SQ, Su, Sd, h))
    res[N] = r
rate = {N: np.array([x[0] for x in r]) for N, r in res.items()}; b15 = max(res[15], key=lambda x: x[0])
check("[E] with independent supplied triples for Q, u^c, d^c (eps 0.22): Z_9 never hits (the ceiling), while Z_15 can "
      "(it is then a supplied cyclic FN charge); the hit fraction over cells is the look-elsewhere price",
      rate[9].max() == 0 and rate[15].max() > 0,
      f"Z_9: {len(rate[9])} cells, max {rate[9].max():.3f}; Z_15: {len(rate[15])} sampled of {len(CL[15]) ** 3 * 15}, "
      f"max {b15[0]:.3f} (Q{b15[1]} u{b15[2]} d{b15[3]} h={b15[4]}), cells with any hit {np.mean(rate[15] > 0):.4f}, "
      f">= half control {np.mean(rate[15] >= 0.5 * sF[0]):.4f}")

# ---------------- D: leptons ----------------
print("== D. lepton mixing [M approx: s12^2 0.307(12), s13^2 0.0220(6), s23^2 0.45-0.58 (octant)]")
s12, s13 = (1 / 3, 0.307, 0.012), (0.0, 0.0220, 0.0006)
pull12 = (s12[0] - s12[1]) / s12[2]; pull13 = (s13[0] - s13[1]) / s13[2]
check("[E] tribimaximal (exact A4 residuals, which need an A4 triplet the site group lacks): s12^2 = 1/3, s23^2 = 1/2, "
      "s13 = 0 is excluded by theta13", abs(pull13) > 30, f"pulls: s12^2 {pull12:+.1f} sigma, s13^2 {pull13:+.0f} sigma")
P = np.array([[w ** (-j * x) for x in range(3)] for j in range(3)]) / np.sqrt(3)
anti = P @ np.array([0, 1, -1]) / np.sqrt(2)
check("[E] the residual groups that do exist (charged leptons keep the family Z_3, neutrinos keep inversion, or the "
      "reverse) fix a column or row (0, 1/sqrt2, 1/sqrt2): a zero in the mixing matrix, whose smallest measured entry is "
      "|U_e3| = 0.148; pure character-vs-position mixing gives all |U|^2 = 1/3",
      np.allclose(np.abs(anti), [0, 1 / np.sqrt(2), 1 / np.sqrt(2)]) and abs(pull13) > 30,
      f"|anti| in characters {np.round(np.abs(anti), 3)}; best placement (zero at U_e3): s13^2 = 0, {pull13:+.0f} sigma")
print(f"runtime {time.time() - t0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
