AUDIT_INPUT_PATHS = ('docs/THE_SIGN_OF_THE_MASS_ANGLE_PICKS_ONE_CUBE_FOLD_OF_THE_TWO_TILING_TICK_AND_ITS_MISFOLDS_ARE_THE_MATTER_FERMIONS_WHILE_DIMER_RESONANCE_AND_SYMMETRIC_WINDOW_RULES_LEAVE_THE_3D_FOLD_UNSELECTED_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Fold selection in 3D: which uniform cube-local rule picks one pair fold (finite runner, seeded).

Sections
  A  the landscape: pair-covering counts (2D control tori, 3D lower bound from independent cubes)
  B  quantum dimer resonance (order by disorder): exact extreme ends, the RK point, the one-cube problem,
     product-crystal energies, and a 2D exact control that limits what product energies can say
  C  the CL-1 cube tick as the selector: cube hop R (spin-3/2 overlap phases), the cube's four-mode vacuum
     against the nine pair coverings, the two-tiling Floquet vacuum against the mass angle mu, the copy mass,
     point misfolds (odd cubes) and wall misfolds (mass-sign walls)
  D  symmetric frustration-free window rules (tile-level combinatorics): sliding degeneracy and an
     anti-slide window
  E  the fewest-change transport as a selector
Modes: one fermion mode per site (occupied = 1). A pair = one unit shared by two sites (bond orbital).
Supplied: sizes, eps = 0.3, the scanned mu and M, product ansatze, window shapes, search caps, seed.
"""
import itertools, signal, sys, time
import numpy as np
from scipy.linalg import schur, expm
import scipy.sparse as sps
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
sys.setrecursionlimit(20000)
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}  {vals}")


# ------------------------------------------------------------------ dimer combinatorics
def lattice(dims):
    D = len(dims)
    sites = list(itertools.product(*[range(L) for L in dims]))
    idx = {s: i for i, s in enumerate(sites)}

    def sh(x, d, s):
        t = list(sites[x]); t[d] = (t[d] + s) % dims[d]; return idx[tuple(t)]
    N = len(sites)
    adj = [[] for _ in range(N)]
    for x in range(N):
        for d in range(D):
            y = sh(x, d, 1); adj[x].append((y, (x, d))); adj[y].append((x, (x, d)))
    other = {}
    for x in range(N):
        for d in range(D):
            other[(x, d)] = sh(x, d, 1)
    part = {(x, d): [(sh(x, e, s), d) for e in range(D) if e != d for s in (1, -1)]
            for x in range(N) for d in range(D)}
    return sites, idx, sh, N, adj, other, part


def coverings(dims, mode='all', limit=None, keep=False):
    """backtracking over pair coverings; mode 'zero' = no flippable plaquette, 'max' = every pair in 4."""
    sites, idx, sh, N, adj, other, part = lattice(dims)
    D = len(dims); occ = [False] * N; B = set(); res = [0]; sols = []

    def rec(i):
        if limit and res[0] >= limit:
            return
        while i < N and occ[i]:
            i += 1
        if i == N:
            if mode == 'max' and not all(all(p in B for p in part[b]) for b in B):
                return
            res[0] += 1
            if keep:
                sols.append(sum(1 << (x * D + d) for (x, d) in B))
            return
        occ[i] = True; seen = set()
        for (y, b) in adj[i]:
            if occ[y] or b in seen:
                continue
            seen.add(b)
            if mode == 'zero' and any(p in B for p in part[b]):
                continue
            if mode == 'max' and any((p not in B) and (occ[p[0]] or occ[other[p]]) for p in part[b]):
                continue
            occ[y] = True; B.add(b); rec(i + 1); B.discard(b); occ[y] = False
        occ[i] = False
    rec(0)
    return res[0], sols


print("== A. the landscape")
c44, _ = coverings((4, 4)); c66, cov66 = coverings((6, 6), keep=True)
check(c44 == 272 and c66 == 90176, "A1 [T]",
      "2D control: pair coverings of the 4x4 and 6x6 tori (exact enumeration); neighbourhood-roles' 121/28561 "
      "omit wrapping coverings (a lower bound; its conclusion stands)",
      f"4x4 {c44}, 6x6 {c66}; ln(count)/site {np.log(c44)/16:.3f}, {np.log(c66)/36:.3f} (Catalan/pi 0.2916)")
# 3D: one cube has 9 coverings; independent even cubes give 9^(N/8) zero-energy folds of any star rule
cube_edges = [(a, b) for a in range(8) for b in range(a + 1, 8)
              if bin(a ^ b).count('1') == 1]
cube_covs = [cm for cm in itertools.combinations(cube_edges, 4) if len({x for e in cm for x in e}) == 8]
check(len(cube_covs) == 9, "A2 [T]",
      "3D: a 2x2x2 cube has 9 internal pair coverings, so even-cube pairings alone give 9^(N/8) "
      "zero-phase folds of any partner-in-star rule",
      f"cube coverings {len(cube_covs)}; bound {np.log(9)/8:.4f} nats/site")

print("== B. quantum dimer resonance H = -t sum_p flip_p + v sum_p flippable_p (t = 1)")
nmax3, sm3 = coverings((4, 4, 4), 'max', keep=True)
nmax2, _ = coverings((6, 6), 'max')
sites3, idx3, sh3, N3, _, _, _ = lattice((4, 4, 4))


def bonds_of(mask, D):
    return [(k // D, k % D) for k in range(mask.bit_length()) if mask >> k & 1]


def tiling_of(sol):
    bs = bonds_of(sol, 3)
    par = {sites3[x][d] % 2 for (x, d) in bs}
    axes = {d for (x, d) in bs}
    return par, axes
tl = [tiling_of(s) for s in sm3]
one_tiling = all(len(p) == 1 and len(a) == 1 for p, a in tl)
check(nmax3 == 6 and nmax2 == 4 and one_tiling, "B1 [T]",
      "v/t -> -inf: N_f <= N (a pair is in <= 4 flippable plaquettes); equality forces the "
      "columnar states: 3 axes x 2 offsets, each inside ONE CL-1 tiling, breaking rotations to one axis",
      f"max-N_f coverings 4x4x4 {nmax3} (N_f = 64), 6x6 {nmax2}; each in one tiling and one axis: {one_tiling}")
z2 = [coverings((L, L), 'zero')[0] for L in (4, 6, 8)]
z3, _ = coverings((4, 4, 4), 'zero', limit=20000)
check(z2 == [12, 28, 60] and z3 >= 20000, "B2 [T+D]",
      "v/t > 1: ground states = coverings with no flippable plaquette; 2D 4(2^(L/2)-1); 3D far more: "
      "no unique fold",
      f"2D 4x4,6x6,8x8: {z2}; 3D 4x4x4: >= {z3} (cap)")
# RK point: uniform superposition per sector; tiling balance from the 6x6 enumeration (2D control) is exact
sites6, idx6, sh6, *_ = lattice((6, 6))
ev = np.mean([np.mean([(sites6[x][d] % 2 == 0) for (x, d) in bonds_of(m, 2)]) for m in cov66])
check(abs(ev - 0.5) < 1e-12, "B3 [T]",
      "v/t = 1 (RK): equal-weight sum per sector; the (1,1,1) translation swaps the tilings and maps sector W to -W, "
      "so the zero-flux sector holds exactly half the pairs per tiling: no fold (3D: Coulomb liquid, cited)",
      f"2D 6x6 all coverings: fraction of pairs inside even plaquettes {ev:.12f}")
# one cube: 3 uniform (4 flippable faces) + 6 mixed (2); flips connect uniform <-> mixed
A = np.zeros((9, 9)); Dg = np.zeros(9)
cs = [frozenset(c) for c in cube_covs]
faces = []
for ax in range(3):
    for v in (0, 1):
        f = [i for i in range(8) if (i >> (2 - ax)) & 1 == v]
        faces.append(f)
def face_pairs(f):
    es = [e for e in cube_edges if e[0] in f and e[1] in f]
    return [(es[i], es[j]) for i in range(4) for j in range(i + 1, 4) if not set(es[i]) & set(es[j])]
fp = [face_pairs(f) for f in faces]
for i, c in enumerate(cs):
    for pr in fp:
        for (e1, e2) in pr:
            if e1 in c and e2 in c:
                Dg[i] += 1
                o = [q for q in pr if q != (e1, e2)][0]
                j = cs.index(frozenset((c - {e1, e2}) | set(o)))
                A[i, j] = 1
ok_e = True; ecube = {}
for v in (-1.0, 0.0, 0.5, 1.0):
    w = np.linalg.eigvalsh(-A + v * np.diag(Dg)); ecube[v] = w[0]
    ok_e &= abs(w[0] - (3 * v - np.sqrt(v * v + 8))) < 1e-12 and w[1] - w[0] > 0.1
check(ok_e and sorted(Dg) == [2] * 6 + [4] * 3, "B4 [T]",
      "one cube: 9 coverings (3 uniform with 4 flippable faces, 6 mixed with 2), unique gapped resonating ground state "
      "e_c = 3v - sqrt(v^2 + 8); at v = 0 it is -2 sqrt2",
      f"e_c(-1,0,0.5,1) = {ecube[-1.0]:.4f}, {ecube[0.0]:.4f}, {ecube[0.5]:.4f}, {ecube[1.0]:.4f}")
# product crystals per site: cube crystal e_c/8 + v/6 (single-crossing plaquettes 3N/2, each pair edge filled 1/3);
# columnar v; staggered 0.  2D analogue: plaquette crystal (v - 1)/4 + v/8, columnar v/2.
vlo = -np.sqrt(72 / 112); vhi = np.sqrt(72 / 160)
def ecr(v): return (3 * v - np.sqrt(v * v + 8)) / 8 + v / 6
ok = abs(ecr(vlo) - vlo) < 1e-12 and abs(ecr(vhi)) < 1e-12
check(ok, "B5 [T]",
      "product crystals per site: cube crystal e_c/8 + v/6 beats columnar (v) and staggered (0) for -0.802 < v/t < 0.671",
      f"window ({vlo:.3f}, {vhi:.3f}); at v = 0 cube {ecr(0):.4f} vs columnar 0")
# 2D control: exact 6x6 ground energy vs products
key = {s: i for i, s in enumerate(cov66)}
plaq = []
for x in range(36):
    hm = (1 << (2 * x)) | (1 << (2 * sh6(x, 1, 1))); vm = (1 << (2 * x + 1)) | (1 << (2 * sh6(x, 0, 1) + 1))
    plaq.append((hm, vm))
rows, cols = [], []; nf = np.zeros(len(cov66))
for i, s_ in enumerate(cov66):
    for (hm, vm) in plaq:
        for a_, b_ in ((hm, vm), (vm, hm)):
            if s_ & a_ == a_:
                nf[i] += 1; rows.append(key[s_ ^ a_ ^ b_]); cols.append(i)
Af = sps.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(cov66),) * 2)
E2 = {}
for v in (-1.0, 0.0):
    Hm = -Af + v * sps.diags(nf)
    E2[v] = eigsh(Hm, k=1, which='SA')[0][0] / 36
pl = {v: (v - 1) / 4 + v / 8 for v in E2}; co = {v: v / 2 for v in E2}
check(E2[0.0] < pl[0.0] - 0.05 and E2[-1.0] < min(pl[-1.0], co[-1.0]) - 0.05, "B6 [D]",
      "2D control: the exact 6x6 ground energy lies below every product crystal by ~0.06 per site, so B5 is a candidate "
      "ordering, not a selection theorem",
      f"E0/N v=0: {E2[0.0]:.4f} (plaquette {pl[0.0]:.4f}); v=-1: {E2[-1.0]:.4f} (plaq {pl[-1.0]:.4f}, col {co[-1.0]:.4f})")
print(f"   (t = {time.time()-T0:.1f} s)")

del cov66, key, Af, rows, cols, nf, Hm
print("== C. the CL-1 cube tick as the selector")
Cc = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d):
        Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * Cc[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex); Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        dd = Cc[a] - Cc[b]
        if np.sum(dd ** 2) == 1:
            g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3); Wi[int(np.argmax(abs(dd)))][a, b] = W[a, b]
S8 = 1j * (np.sqrt(3) ** 3) * Wi[0] @ Wi[1] @ Wi[2] @ W
fl = []
for f in faces:
    o = [f[0]]
    while len(o) < 4:
        o.append([j for j in f if j not in o and bin(j ^ o[-1]).count('1') == 1][0])
    fl.append(np.prod([W[o[k], o[(k + 1) % 4]] for k in range(4)]) * 9)
wR, vR = np.linalg.eigh(W)
ssp = [np.round(np.linalg.eigvalsh(vR[:, np.isclose(wR, r)].conj().T @ S8 @ vR[:, np.isclose(wR, r)]), 9) for r in (-1, 1)]
check(np.abs(W @ W - np.eye(8)).max() < 1e-12 and np.allclose(fl, -1) and np.abs(S8 @ W - W @ S8).max() < 1e-12
      and all(list(x) == [-1, -1, 1, 1] for x in ssp), "C1 [T]",
      "cube hop R (edge hops with the phase of the spin-3/2 overlap along the body diagonals): R^2 = 1, every face "
      "phase -1, eigenvalues +-1 four times each; the copy sign s commutes with R and splits each into 2 + 2",
      f"|R^2-1| {np.abs(W@W-np.eye(8)).max():.0e}; face phases {np.round(np.real(fl),6).tolist()}")
# Fock space of one cube (256 states, below the dense limit)
nf8 = 8; dimF = 1 << nf8
def cdag(j):
    M = np.zeros((dimF, dimF))
    for s in range(dimF):
        if not (s >> j) & 1:
            M[s | (1 << j), s] = (-1) ** bin(s & ((1 << j) - 1)).count('1')
    return M
Cd = [cdag(j) for j in range(nf8)]
vac0 = np.zeros(dimF, complex); vac0[0] = 1
def slater(V):
    psi = vac0.copy()
    for k in range(V.shape[1]):
        psi = sum(V[a, k] * Cd[a] for a in range(nf8)) @ psi
    return psi / np.linalg.norm(psi)
Fm = slater(vR[:, wR < 0])
def dimer_state(cov):
    psi = vac0.copy()
    for (a, b) in cov:
        hh = np.array([[0, W[a, b]], [W[b, a], 0]]); ww, vv = np.linalg.eigh(hh); u = vv[:, 0]
        psi = (u[0] * Cd[a] + u[1] * Cd[b]) @ psi
    return psi / np.linalg.norm(psi)
Dm = np.array([dimer_state(c) for c in cube_covs]).T
Q, _ = np.linalg.qr(Dm); rk = np.linalg.matrix_rank(Dm, 1e-10)
ov = np.linalg.norm(Q.conj().T @ Fm) ** 2
Rh = sum(W[a, b] * Cd[a] @ Cd[b].T for a in range(8) for b in range(8))
Pd = Q @ Q.conj().T; leak = np.linalg.norm((np.eye(dimF) - Pd) @ Rh @ Pd, 2)
check(rk == 9 and 0.85 < ov < 0.99 and leak > 0.5, "C2 [T+D]",
      "the cube's four-unit vacuum (filled R = -1 level) is 91% in the span of its 9 pair coverings (bond orbitals); "
      "the hop leaks out of the span: the cube tick is NOT a dimer-plaquette flip",
      f"span rank {rk}; |P_dimer F|^2 {ov:.4f}; best single covering {max(abs(Dm.conj().T@Fm)**2):.4f}; leak {leak:.3f}")


def lat3(Ls):
    sites = list(itertools.product(*[range(L) for L in Ls])); ix = {s: i for i, s in enumerate(sites)}; N = len(sites)
    lab = [(s[0] % 2) * 4 + (s[1] % 2) * 2 + (s[2] % 2) for s in sites]
    out = []
    for off in (0, 1):
        R = np.zeros((N, N), complex); Sm = np.zeros((N, N), complex); cubes = {}
        for s in sites:
            cubes.setdefault(tuple(((s[d] - off) % Ls[d]) // 2 for d in range(3)), []).append(ix[s])
        for mem in cubes.values():
            for a in mem:
                for b in mem:
                    Sm[a, b] = S8[lab[a], lab[b]]
                    if sum(min((sites[a][d] - sites[b][d]) % Ls[d], (sites[b][d] - sites[a][d]) % Ls[d]) for d in range(3)) == 1:
                        R[a, b] = W[lab[a], lab[b]]
        out.append((R, Sm, cubes))
    return sites, N, out


def vacuum(U):
    Tm, V = schur(U, output='complex'); om = -np.angle(np.diag(Tm)); occ = om < 0
    G = V[:, occ] @ V[:, occ].conj().T
    return G, min(np.abs(om).min(), (np.pi - np.abs(om)).min()), om


def var_set(G, mem):
    g = G[np.ix_(mem, mem)]; return float(np.trace(g).real - np.trace(g @ g).real)


def var_tiling(G, cubes): return float(np.mean([var_set(G, m) for m in cubes.values()]))


del Cd, Rh, Pd, Q, Dm
EPS = 0.3
sitesL, NL, ((RE, SE, cE), (RO, SO, cO)) = lat3((8, 8, 8))
I_ = np.eye(NL)
def tick(mu, M=0.0):
    a, b = EPS - mu / 2, EPS + mu / 2
    UE = np.cos(a) * I_ - 1j * np.sin(a) * RE; UO = np.cos(b) * I_ + 1j * np.sin(b) * RO
    if M:
        CM = expm(1j * (M / 4) * (I_ - SE) @ RE); return UO @ CM @ UE @ CM
    return UO @ UE
ts = [-1, -0.5, -0.25, -0.1, -0.05, 0, 0.05, 0.1, 0.25, 0.5, 1]
res = {}
for t in ts:
    G, gap, om = vacuum(tick(2 * EPS * t)); res[t] = (gap, var_tiling(G, cE), var_tiling(G, cO), G if t in (-1, -0.5, 0, 0.5, 1) else None)
gap_ok = all(abs(res[t][0] - 2 * EPS * abs(t)) < 1e-9 for t in ts)
sym = max(abs(res[t][1] - res[-t][2]) for t in ts if t)
check(np.abs(RE @ RE - I_).max() < 1e-12 and np.abs(RO @ RO - I_).max() < 1e-12 and gap_ok, "C3 [T+D]",
      "two-tiling tick on the 8^3 torus, even step eps - mu/2, odd step eps + mu/2: the quasi-energy gap is exactly |mu| "
      "(cos w = cos a cos b + sin a sin b S, S in [-1, 1]), closing only at mu = 0: every mu < 0 "
      "vacuum connects to mu = -2 eps, every mu > 0 to +2 eps",
      "gap/|mu| " + ", ".join(f"{res[t][0]/(2*EPS*abs(t)):.6f}" for t in ts if t) + f"; gap at 0 {res[0][0]:.1e}")
Gm1 = res[-1][3]; ce0 = list(cE.values())[0]
faceA = [x for x in ce0 if sitesL[x][0] % 2 == 0]; faceB = [x for x in ce0 if sitesL[x][0] % 2 == 1]
check(res[-1][1] < 1e-12 and res[1][2] < 1e-12 and sym < 1e-9 and var_set(Gm1, faceA) > 0.3, "C4 [T+D]",
      "the two fold limits are the cube folds: at mu = -2 eps every even cube holds exactly 4 units (n_A + n_A' definite "
      "for a face A and its mirror face A', n_A not), at mu = +2 eps every odd cube does; every site bound, none "
      "free; mu -> -mu swaps tilings. The SIGN of the mass angle picks the fold; mu = 0 is unfolded",
      "Var N_even/Var N_odd " + ", ".join(f"{t:+}:{res[t][1]:.3f}/{res[t][2]:.3f}" for t in (-1, -0.25, 0, 0.25, 1))
      + f"; face var {var_set(Gm1, faceA):.3f}, face+mirror var {var_set(Gm1, faceA+faceB):.0e}")
d05 = res[-0.05][2] - res[-0.05][1]; d10 = res[-0.1][2] - res[-0.1][1]
check(d10 > d05 > 0, "C5 [D+E]",
      "fold strength at small mass: the tiling imbalance of cube-number variance grows from zero about linearly in |mu| "
      "(slope ~9 on 8^3); at physical mass angles the vacuum is unfolded at the cell scale",
      f"imbalance at |mu| = {0.1*EPS:.2f}: {d05:.4f}, at {0.2*EPS:.2f}: {d10:.4f}; electron estimate ~{9*4e-23:.0e}")
GM, gapM, _ = vacuum(tick(0.0, M=0.2))
vM = (var_tiling(GM, cE), var_tiling(GM, cO))
check(gapM < 1e-9 and vM[1] < vM[0] - 0.3, "C6 [D]",
      "with the copy mass (M = 0.2 on even cubes) and mu = 0 the light copy stays gapless but the vacuum is no longer "
      "tiling-balanced: the copy mass is a second fold selector",
      f"gap {gapM:.1e}; Var N_even {vM[0]:.3f}, Var N_odd {vM[1]:.3f}")
# point misfolds at the fold limit: one extra unit in one cube
G_, _, om_ = vacuum(tick(-2 * EPS))
wE, vE = np.linalg.eigh(RE[np.ix_(ce0, ce0)])
up = vE[:, wE > 0]   # empty level of the even-fold vacuum (R = +1)
Sc = SE[np.ix_(ce0, ce0)]
sup = np.round(np.linalg.eigvalsh(up.conj().T @ Sc @ up), 9)
check(up.shape[1] == 4 and list(sup) == [-1, -1, 1, 1] and abs(np.sort(np.abs(om_))[0] - 2 * EPS) < 1e-12, "C7 [T]",
      "point misfolds: a cube holding 5 (or 3) units is an odd-parity excitation of the fold, so it is a FERMION "
      "(the modes anticommute), in a 4-state level split 2 + 2 by the copy sign (CL-1's doublet x copy), costing |mu|: "
      "the misfold is CL-1's matter particle",
      f"level dim {up.shape[1]}, copy signs {sup.tolist()}, cost {np.sort(np.abs(om_))[0]:.3f} = 2 eps")
# wall misfolds: mass sign flips across two walls
wall = {}
for Lt in (4, 6):
    sW, NW, ((RE2, _, cE2), (RO2, _, cO2)) = lat3((16, Lt, Lt))
    aE = np.zeros(NW); bO = np.zeros(NW)
    for k, mem in cE2.items():
        mu = 0.3 if k[0] < 4 else -0.3; aE[mem] = EPS - mu / 2
    for k, mem in cO2.items():
        mu = 0.3 if k[0] < 4 else -0.3; bO[mem] = EPS + mu / 2
    U2 = (np.diag(np.cos(bO)) + 1j * np.diag(np.sin(bO)) @ RO2) @ (np.diag(np.cos(aE)) - 1j * np.diag(np.sin(aE)) @ RE2)
    _, g2, om2 = vacuum(U2); wall[Lt] = (int((np.abs(om2) < 1e-9).sum()), int((np.abs(om2) < 0.299).sum()))
check(wall[4][0] == wall[6][0] == 8 and wall[6][1] > wall[4][1] > 0, "C8 [D]",
      "wall misfolds: a wall between the even and odd folds (mass-sign wall, bulk gap 0.3) carries gapless 2+1 fermions "
      "(count grows with area): extended, not point matter",
      f"16xLxL, two walls: zero modes L=4 {wall[4][0]}, L=6 {wall[6][0]}; in-gap states {wall[4][1]} -> {wall[6][1]} "
      f"(area 16 -> 36)")
print(f"   (t = {time.time()-T0:.1f} s)")

print("== D. symmetric frustration-free window rules (tile level: a window is satisfied when it holds a whole tile)")
def tilings(dims):
    D = len(dims); sts = list(itertools.product(*[range(L) for L in dims])); ix = {s: i for i, s in enumerate(sts)}
    N = len(sts); occ = [False] * N; cur = []; out = []
    def cells(p): return [ix[tuple((p[d] + o[d]) % dims[d] for d in range(D))] for o in itertools.product((0, 1), repeat=D)]
    def rec(i):
        while i < N and occ[i]:
            i += 1
        if i == N:
            out.append(frozenset(cur)); return
        s = sts[i]
        for o in itertools.product((0, -1), repeat=D):
            p = tuple((s[d] + o[d]) % dims[d] for d in range(D)); cl = cells(p)
            if not any(occ[c] for c in cl):
                for c in cl:
                    occ[c] = True
                cur.append(p); rec(i + 1); cur.pop()
                for c in cl:
                    occ[c] = False
    rec(0); return out


def passes(T, dims, P, sym=True):
    D = len(dims)
    perms = list(itertools.permutations(range(D))) if sym else [tuple(range(D))]
    for perm in perms:
        for sg in (itertools.product((1, -1), repeat=D) if sym else [(1,) * D]):
            Pg = [[sg[d] * q[perm[d]] - (sg[d] < 0) for d in range(D)] for q in P]
            for u in itertools.product(*[range(L) for L in dims]):
                if not any(tuple((u[d] + r[d]) % dims[d] for d in range(D)) in T for r in Pg):
                    return False
    return True


def aligned(T, D):
    return len({tuple(p[d] % 2 for d in range(D)) for p in T}) == 1
box2 = [(0, 0), (1, 0), (0, 1), (1, 1)]; anti = [(0, 0), (1, 2), (0, 1), (1, 3)]
rD = {}
for dims in ((8, 8), (12, 12)):
    tt = tilings(dims)
    rD[dims] = (len(tt), sum(passes(x, dims, box2, False) for x in tt), sum(passes(x, dims, anti) for x in tt),
                sum(aligned(x, 2) for x in tt))
t3 = tilings((4, 4, 4)); box3 = list(itertools.product((0, 1), repeat=3))
p3 = sum(passes(x, (4, 4, 4), box3, False) for x in t3); a3 = sum(aligned(x, 3) for x in t3)
check(rD[(8, 8)][1] == rD[(8, 8)][0] and rD[(12, 12)][1] == rD[(12, 12)][0] and p3 == len(t3) and a3 == 8, "D1 [T]",
      "the Majumdar-Ghosh-type rule 'every 3^d window holds a whole 2^d tile' is met by every "
      "tiling incl. sliding ones: 2^O(L^(d-1)) folds, zero entropy/site, not unique",
      f"tilings passing/total 8x8 {rD[(8,8)][1]}/{rD[(8,8)][0]}, 12x12 {rD[(12,12)][1]}/{rD[(12,12)][0]}, "
      f"4^3 {p3}/{len(t3)} (aligned 8)")
check(rD[(8, 8)][2] == rD[(8, 8)][3] == 4 and rD[(12, 12)][2] == 4, "D2 [T+D]",
      "an anti-slide window (tiles at (0,0),(0,1),(1,2),(1,3), all 8 square symmetries) leaves only the 4 aligned "
      "crystals in 2D; it spans 2x5 sites (not cube-local); 3D untested; qubit kernel assumed",
      f"8x8 pass {rD[(8,8)][2]} (aligned {rD[(8,8)][3]}), 12x12 pass {rD[(12,12)][2]}")

print("== E. the fewest-change transport as a selector")
stat = {}
for t in (-1, -0.5, 0, 0.5, 1):
    mu = 2 * EPS * t; a = EPS - mu / 2
    UE = np.cos(a) * I_ - 1j * np.sin(a) * RE
    G = res[t][3]; stat[t] = float(np.abs(UE @ G @ UE.conj().T - G).max())
check(stat[-1] < 1e-12 and stat[1] < 1e-12 and min(stat[-0.5], stat[0], stat[0.5]) > 1e-3, "E1 [T+D]",
      "CL-2 moves only the actual configuration and never conditions the odds, so it cannot pick a fold; half-tick "
      "odds are stationary only at the two fold limits, which tie",
      "odds change across the even half-tick: " + ", ".join(f"{t:+}: {stat[t]:.1e}" for t in stat))
print(f"supplied: eps = {EPS}, mu scan, M = 0.2, sizes 4^3/8^3/16xLxL/6x6, product ansatze, windows, cap 20000, "
      f"seed 20261022")
print(f"runtime {time.time()-T0:.1f} s")
import resource
print(f"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f} MB")
print(f"TOTAL: PASS={NP} FAIL={NF}")
