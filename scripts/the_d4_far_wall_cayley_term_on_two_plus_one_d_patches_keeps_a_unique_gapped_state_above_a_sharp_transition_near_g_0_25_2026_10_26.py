AUDIT_INPUT_PATHS = ('docs/THE_D4_FAR_WALL_CAYLEY_TERM_ON_TWO_PLUS_ONE_D_PATCHES_KEEPS_A_UNIQUE_GAPPED_STATE_ABOVE_A_SHARP_TRANSITION_NEAR_G_0_25_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-far-wall-2plus1: does the Cayley far-wall gap of the D4 root-line chain survive with two transverse directions?
 A  geometry: time root u_t; the D4 points with u_t.x = 0 form a cubic lattice of 3 orthogonal roots n1, n2, n3; hops
    i psi^+ Gamma_k psi', Gamma_k = i g(u_t) g(n_k); a frame U with Gamma1 = sz x 1, Gamma2 = sx x 1, g5 = 1 x tz.
    The hop conserves n_A, n_B (A = g5 -1, the far-wall chirality; B = g5 +1); Omega moves both by 2: sectors (Q, n_A mod 2).
 B  1x4 chain gate with the earlier chain twist (live) and 1x6 (embedded).
 C  2x2 patch, all sectors, g scan (live); free baseline; avoided-crossing minimum.
 D  2x3 patch (1,352,540-state sectors, Kronecker matvec): one live sector; the rest embedded [R] from scratch runs.
Labels: [T] exact, [F] finite diagnostic, [R] embedded result (same code, scratch/drive.py, 2026-10-26, laptop, < 950 MB).
Supplied: the 4-mode spinor register, the Cayley form and weight, the naive Dirac hop t = 1, the Z4 twist, g."""
AUDIT_TIMEOUT_SEC = 120
import time, resource
T0 = time.time()
import os, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
pc = lambda a: np.bitwise_count(a).astype(np.int64)
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
g5 = gm[0] @ gm[1] @ gm[2] @ gm[3]; g5 = g5 / np.sqrt((g5 @ g5)[0, 0]); gv = lambda v: np.einsum('m,mab->ab', v, gm)
ut = np.array([1, 1, 0, 0]) / np.sqrt(2)
NV = [np.array([0, 0, 1, 1]) / np.sqrt(2), np.array([0, 0, 1, -1]) / np.sqrt(2), np.array([1, -1, 0, 0]) / np.sqrt(2)]
GAM = [1j * gv(ut) @ gv(n) for n in NV]
def frame():
    # U: columns (c,m) -> c*2+m ; Gamma1 = sz x 1, Gamma2 = sx x 1, g5 = 1 x tz
    w, V = np.linalg.eigh(GAM[0]); Pp = V[:, w > 0]          # Gamma1 = +1 space, commutes with g5
    w5, V5 = np.linalg.eigh(Pp.conj().T @ g5 @ Pp); e = Pp @ V5  # order g5 = -1, +1
    f = GAM[1] @ e; U = np.column_stack([e[:, 0], e[:, 1], f[:, 0], f[:, 1]]); return U, w5
U, W5 = frame()
GP = [U.conj().T @ G @ U for G in GAM]
def species_gamma(k, m): return GP[k][np.ix_([m, 2 + m], [m, 2 + m])]
class Species:
    def __init__(s, dims, twist, m):
        # dims = (Lx, Ly); twist[k] = 2-vector of phases (c = 0, 1) on wraps in direction k; m = species (A=0, B=1)
        Lx, Ly = dims; Ns = Lx * Ly; s.Ns = Ns; Nm = 2 * Ns; s.Nm = Nm
        site = lambda x, y: (x % Lx) * Ly + (y % Ly); h = np.zeros((Nm, Nm), complex)
        for x in range(Lx):
            for y in range(Ly):
                for k, (dx, dy, L) in enumerate([(1, 0, Lx), (0, 1, Ly)]):
                    if L == 1: continue
                    a, b = site(x, y), site(x + dx, y + dy); wrap = (x + dx >= Lx) if k == 0 else (y + dy >= Ly)
                    G = species_gamma(k, m); T = np.diag(twist[k]) if wrap else np.eye(2); M = 1j * G @ T
                    for c in range(2):
                        for c2 in range(2):
                            h[2 * a + c, 2 * b + c2] += M[c, c2]; h[2 * b + c2, 2 * a + c] += np.conj(M[c, c2])
        s.hsp = h; s.cfg = {}
        allc = np.arange(1 << Nm, dtype=np.int64); cnt = pc(allc)
        for n in range(Nm + 1): s.cfg[n] = allc[cnt == n]
        s.H = {}; s.P = {}; s.al = {}
        for n in range(Nm + 1):
            S = s.cfg[n]; D = len(S); r, c, v = [], [], []
            for p, q in zip(*np.nonzero(np.abs(h) > 1e-14)):
                if p == q:
                    o = np.nonzero((S >> p) & 1)[0]; r.append(o); c.append(o); v.append(np.full(len(o), h[p, p])); continue
                ok = ((S >> q) & 1 == 1) & ((S >> p) & 1 == 0); st = S[ok]; lo, hi = min(p, q), max(p, q)
                sg = 1 - 2 * (pc(st & (((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1))) & 1)
                r.append(np.searchsorted(S, st ^ (1 << p) ^ (1 << q))); c.append(np.nonzero(ok)[0]); v.append(h[p, q] * sg)
            s.H[n] = sp.csr_matrix((np.concatenate(v) if v else [], (np.concatenate(r) if r else [], np.concatenate(c) if c else [])), shape=(D, D))
            occ = np.stack([((S >> (2 * x)) & 1) + ((S >> (2 * x + 1)) & 1) for x in range(Ns)], 1); s.al[n] = 1 - occ
            if n >= 2:
                T_ = s.cfg[n - 2]; mats = []
                for x in range(Ns):
                    ok = ((S >> (2 * x)) & 3) == 3; st = S[ok]
                    mats.append(sp.csr_matrix((-np.ones(len(st)), (np.searchsorted(T_, st ^ (3 << (2 * x))), np.nonzero(ok)[0])), shape=(len(T_), D)))
                s.P[n] = mats
class Sector:
    def __init__(s, A, B, Q, par, g, model):
        s.A, s.B, s.g, s.model = A, B, g, model; s.blocks = []; off = 0
        for nA in range(A.Nm + 1):
            nB = nA - Q
            if nA % 2 != par or nB < 0 or nB > B.Nm: continue
            sh = (len(A.cfg[nA]), len(B.cfg[nB])); s.blocks.append((nA, nB, off, sh)); off += sh[0] * sh[1]
        s.dim = off; s.idx = {(b[0], b[1]): i for i, b in enumerate(s.blocks)}; s.D = []
        for nA, nB, o, sh in s.blocks:
            if model == 'Cay':
                aa, bb = A.al[nA], B.al[nB]
                Dg = (np.sum(1 - 2 * aa ** 2, 1)[:, None] + np.sum(1 - 2 * bb ** 2, 1)[None, :] - 4.0 * aa @ bb.T) * g
            else: Dg = np.zeros(sh)
            s.D.append(Dg)
    def mv(s, v):
        v = np.asarray(v).ravel(); out = np.zeros(s.dim, complex); A, B, g = s.A, s.B, s.g
        V = [v[o:o + sh[0] * sh[1]].reshape(sh) for (_, _, o, sh) in s.blocks]
        W = [out[o:o + sh[0] * sh[1]].reshape(sh) for (_, _, o, sh) in s.blocks]
        for i, (nA, nB, o, sh) in enumerate(s.blocks):
            W[i] += A.H[nA] @ V[i] + (B.H[nB] @ V[i].T).T + s.D[i] * V[i]
            j = s.idx.get((nA - 2, nB - 2))
            if j is not None and g != 0:
                for x in range(A.Ns):
                    PA, PB = A.P[nA][x], B.P[nB][x]
                    W[j] += 8 * g * (PA @ (PB @ V[i].T).T)
                    W[i] += 8 * g * (PA.T @ (PB.T @ V[j].T).T)
        return out
    def low(s, k):
        if s.dim <= 600:
            M = np.column_stack([s.mv(e) for e in np.eye(s.dim)]); return np.linalg.eigvalsh(M)[:k]
        op = sla.LinearOperator((s.dim, s.dim), matvec=s.mv, dtype=complex)
        return np.sort(sla.eigsh(op, k=k, which='SA', tol=1e-8, ncv=20 if k == 1 else 32, v0=np.random.default_rng(7).standard_normal(s.dim) + 0j)[0])
def gap(dims, tw, g, model, Qs):
    A = Species(dims, tw, 0); B = Species(dims, tw, 1); lv = {}
    for Q in Qs:
        for par in (0, 1):
            sc = Sector(A, B, Q, par, g, model)
            if sc.dim: lv[(Q, par)] = sc.low(2)
    E0 = min(l[0] for l in lv.values()); k0 = min(lv, key=lambda q: lv[q][0])
    ex = {q: (l[0] if q != k0 else l[1]) - E0 for q, l in lv.items()}
    return min(ex.values()), E0, k0, ex, A
NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(("PASS" if ok else "FAIL") + f" {name}" + (f": {info}" if info else ""))
print("== A. geometry and exact structure")
R24 = {v for v in itertools.product([1, -1, 0], repeat=4) if sum(map(abs, v)) == 2}; perp = [np.array(r) for r in R24 if abs(np.dot(r, ut * np.sqrt(2))) < 1e-12]
G = np.array([[np.dot(a, b) for b in perp] for a in perp])
check("A1 [T] D4 has 24 roots; 6 are orthogonal to u_t, = +-n1, +-n2, +-n3, mutually orthogonal: the wall slice is cubic",
      len(R24) == 24 and len(perp) == 6 and np.count_nonzero(np.abs(G) > 1e-12) == 12)
ac = max(np.abs(GAM[i] @ GAM[j] + GAM[j] @ GAM[i] - 2 * (i == j) * np.eye(4)).max() for i in range(3) for j in range(3))
her = max(np.abs(Gm - Gm.conj().T).max() for Gm in GAM)
sz, sx, sy = np.diag([1., -1]), np.array([[0., 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]); tz = np.diag([1., -1])
fr = max(np.abs(GP[0] - np.kron(sz, I2)).max(), np.abs(GP[1] - np.kron(sx, I2)).max(), np.abs(U.conj().T @ g5 @ U + np.kron(I2, tz)).max(),
         np.abs(GP[2] + np.kron(sy, tz)).max(), np.abs(U.conj().T @ U - np.eye(4)).max())
check("A2 [T] Gamma_k Hermitian, {Gamma_i, Gamma_j} = 2 delta_ij; frame U: Gamma1 = sz x 1, Gamma2 = sx x 1, Gamma3 = -sy x tz, g5 = -(1 x tz)",
      max(ac, her, fr) < 1e-12, f"{max(ac, her, fr):.0e}")
print("  => the in-plane hop acts on the Clifford factor only: n_A (far-wall Weyl, g5 = -1) and n_B conserved; Omega = P_A P_B")
print("     moves both by 2; the full 3D wall hop keeps the same split (Gamma3 diagonal in A/B). Z4 twist i*1 commutes with all.")
print("== B. chain gate (Lx = 4, Ly = 1; earlier twist (-i, +i) on Gamma1 = (+1, -1))")
ot = [np.array([-1j, 1j]), None]
gC = gap((4, 1), ot, 0.25, 'Cay', range(-3, 4))[0]; gR = gap((4, 1), ot, 0.25, 'ReO', range(-3, 4))[0]; g0 = gap((4, 1), ot, 0.0, 'Cay', range(-3, 4))[0]
check("B1 [F] 1x4: Cayley g = 0.25 gap 2.719, Re Omega 1.130, free 2 sin(pi/8) (d4-far-wall-gapping chain values)",
      abs(gC - 2.719) < 2e-3 and abs(gR - 1.130) < 2e-3 and abs(g0 - 2 * np.sin(np.pi / 8)) < 1e-8, f"{gC:.4f}, {gR:.4f}, {g0:.4f}")
E16 = {'E0': -23.127646, (0, 1): -20.425261, (1, 0): -20.337801, (1, 1): -20.337801, (2, 0): -20.425261, (2, 1): -18.187930}
d16 = min(v for k, v in E16.items() if k != 'E0') - E16['E0']
check("B2 [R] 1x6 (same code, 1.35e6-state sectors): Cayley g = 0.25 lowest excitation 2.702 (chain value)", abs(d16 - 2.702) < 2e-3, f"{d16:.4f}")
print("== C. 2x2 patch (twist i on every wrap), all sectors Q = -8..8")
vt = [np.array([1j, 1j])] * 2; res2 = {}
for mo, g in [('Cay', 0.0), ('Cay', .125), ('Cay', .25), ('Cay', .35), ('Cay', .5), ('Cay', 1.0), ('ReO', .25), ('ReO', .5), ('ReO', 1.0)]:
    d, E0, k0, ex, A2 = gap((2, 2), vt, g, mo, range(-8, 9)); res2[(mo, g)] = (d, E0, k0, ex)
    lowQ = min(ex, key=ex.get)
    print(f"  {mo} g={g:<5} gap {d:7.4f}  E0/site {E0 / 4:8.4f}  GS sector {k0}  lowest excitation in {lowQ}  GS-sector E1 {ex[k0]:.4f}")
eps2 = np.abs(np.linalg.eigvalsh(A2.hsp)); fr2 = 2 * np.sqrt(2 * np.sin(np.pi / 4) ** 2)
check("C1 [F] g = 0: patch gap = free min|eps| = 2 sqrt(sin^2 k1 + sin^2 k2), k = pi/4 (twisted, no zero mode)", abs(res2[('Cay', 0.0)][0] - fr2) < 1e-8 and abs(eps2.min() - fr2) < 1e-8, f"{fr2:.4f}")
check("C2 [F] ground state unique in every run, in sector (Q, par) = (0, 0); lowest excitations in |Q| <= 1 (justifies |Q| <= 2 at 2x3)",
      all(r[2] == (0, 0) and r[0] > 0.5 for r in res2.values()) and all(abs(min(r[3], key=r[3].get)[0]) <= 1 for r in res2.values()))
A = Species((2, 2), vt, 0); B = Species((2, 2), vt, 1)
gs = np.arange(0.24, 0.271, 0.0025); ins = [(lambda s: s[1] - s[0])(Sector(A, B, 0, 0, g, 'Cay').low(2)) for g in gs]; im = int(np.argmin(ins))
check("C3 [F] 2x2 Cayley: GS-sector gap has an avoided-crossing minimum near g = 0.255 (min 0.877): the crossover from the free-like",
      0.25 <= gs[im] <= 0.26 and abs(min(ins) - 0.877) < 0.01, f"g {gs[im]:.4f}, min {min(ins):.4f}")
print("     state to the on-site Cayley state; the 1x4 chain's crossover is at g ~ 0.11 (GS-sector gap minimum 1.24)")
print("== D. 2x3 patch (sectors |Q| <= 2; gaps relative to E0 in (0,0)) [R], one live check")
EMB = {0.125: (-23.847473, 2.674, 2.620, 1.666, 3.211), 0.25: (-25.126719, 0.290, 1.352, 1.407, 2.369),
       0.35: (-32.040371, 3.182, 3.848, 3.447, 4.328), 0.5: (-43.774396, 6.196, 6.719, 5.599, 7.028)}
SCAN = {0.225: 0.690, 0.235: 0.323, 0.2375: 0.226, 0.24: 0.126, 0.2425: 0.024, 0.2435: 0.017, 0.2445: 0.058, 0.25: 0.290, 0.26: 0.721, 0.275: 1.362, 0.3: 2.175}
A3 = Species((2, 3), vt, 0); B3 = Species((2, 3), vt, 1); live = Sector(A3, B3, 0, 0, 0.5, 'Cay').low(1)[0]
check("D1 [F] live: 2x3 Cayley g = 0.5 ground energy in the 1,352,540-state sector reproduces the embedded value", abs(live - EMB[0.5][0]) < 1e-5, f"{live:.6f}")
fr3 = 2 * np.sqrt(np.sin(np.pi / 4) ** 2 + np.sin(np.pi / 6) ** 2); e3 = np.abs(np.linalg.eigvalsh(A3.hsp)).min()
check("D2 [T] free 2x3: min|eps| = 2 sqrt(1/2 + 1/4) = 1.732 (finite-size; nodes at k in {0, pi}^2: 4 cones x 2 species, gapless as L -> inf)", abs(e3 - fr3) < 1e-10, f"{e3:.4f}")
print("  g      gap(2x2) gap(2x3) ratio  2x3/free  E0/site 2x2 2x3   class (pre-set)")
cls = {}
for g in (0.125, 0.25, 0.35, 0.5):
    d2 = res2[('Cay', g)][0]; e = EMB[g]; d3 = min(e[1:]); r = d3 / d2; fr = 2.0
    c = 'OPEN-LIKE' if r >= 0.9 and d3 >= 1.2 * fr3 else ('CLOSING' if abs(r / (fr3 / fr) - 1) < 0.05 or d3 < fr3 else 'INCONCLUSIVE'); cls[g] = c
    print(f"  {g:<6} {d2:7.3f} {d3:8.3f}  {r:5.3f}  {d3 / fr3:6.3f}   {res2[('Cay', g)][1] / 4:7.3f} {e[0] / 6:7.3f}   {c}")
print("  2x3 GS-sector gap scan: " + ", ".join(f"{k}:{v}" for k, v in SCAN.items()))
check("D3 [F] the GS-sector minimum sharpens from 0.877 (2x2, g 0.255) to <= 0.017 (2x3, g 0.2435): a sharp transition at g_x ~ 0.24-0.26",
      min(SCAN.values()) < 0.02 and 0.24 < min(SCAN, key=SCAN.get) < 0.25)
check("D4 [F] pre-set class: g = 0.25 CLOSING (it sits on the transition at these sizes); g = 0.125 CLOSING (free-like, ratio = free ratio);"
      " g = 0.35 and 0.5 OPEN-LIKE (gap flat or growing, >= 1.8 x free, unique ground state)",
      cls == {0.125: 'CLOSING', 0.25: 'CLOSING', 0.35: 'OPEN-LIKE', 0.5: 'OPEN-LIKE'})
print("  2D vs 1D at g = 0.5: gap 5.599 (2x3) vs 6.054 (1x6): the strong-coupling gap survives the second direction (-8%).")
print("  Not run: 2x4 (3.0e8 states; 3.8e7 per momentum, ~0.6 GB/vector: Mac mini feasible), 3x3 (4.5e9: beyond ED).")
print("Verdict (pre-set): at g = 0.25 CLOSES at these sizes (g = 0.25 is the 2D transition); Cayley gap SURVIVES for g >= 0.35.")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.0f} MB")
print(f"TOTAL: PASS={NP} FAIL={NF}")
