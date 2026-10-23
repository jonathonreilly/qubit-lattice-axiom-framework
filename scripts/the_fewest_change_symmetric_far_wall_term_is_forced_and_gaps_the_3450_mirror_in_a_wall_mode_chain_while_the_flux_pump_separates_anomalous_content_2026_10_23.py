AUDIT_INPUT_PATHS = ('docs/THE_FEWEST_CHANGE_SYMMETRIC_FAR_WALL_TERM_IS_FORCED_AND_GAPS_THE_3450_MIRROR_IN_A_WALL_MODE_CHAIN_WHILE_THE_FLUX_PUMP_SEPARATES_ANOMALOUS_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""far-wall-smg: on the domain-wall slab, can a symmetric interaction confined to the far wall gap the mirror there,
leaving the near-wall chiral modes free, for anomaly-free content, and does it fail for anomalous content?
1+1D proxy: a 2D Wilson slab (x, layer s), m = 1, four flavours. Flavours 3, 4 put a left mover on the near wall and a
right mover on the far wall; flavours 5, 0 the reverse. So the near wall carries the 3-4-5-0 theory L(3,4) R(5,0) and the
far wall its mirror R(3,4) L(5,0). Symmetry U(1)_A x U(1)_B, charges (3,4,5,0) and (2,1,2,-1).
 A  exact algebra: the neutral lattice, the fewest-change terms, coupling phases, the 3-4-5-1 obstruction.
 B  free slab: wall modes, far-layer amplitudes, near-wall leak, bulk Chern number and the flux pump.
 C  far-wall effective chain (wall modes |k| < pi/2 kept, bulk dropped), antiperiodic L = 8, 12: exact diagonalisation
    with the two nearest-neighbour 6-fermion terms on the far layer.
 D  near-wall decoupling: near-wall flavour-3 modes added to the chain with their exact far-layer leak.
 E  anomalous control 3-4-5-1.
Labels: [T] exact, [F] finite diagnostic. Supplied: slab, m, couplings g, sizes, the projection onto wall modes.
Cited, not rederived: Wang-Wen 2013 (arXiv:1307.7480) / 2018 (arXiv:1809.11171), Tong 2021 (arXiv:2104.03997),
Zeng-Zhu-Wang-You 2022 (arXiv:2202.12355, DMRG on a Chern-strip boundary)."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

QA = np.array([3, 4, 5, 0]); QB = np.array([2, 1, 2, -1]); Q51 = np.array([3, 4, 5, 1])
KN = np.diag([1, 1, -1, -1])                     # near wall: + left movers (3,4), - right movers (5,0)
SF = np.array([1, 1, -1, -1])                    # far-wall chirality sign: E_f(k) = SF_f sin k
L1 = (1, -2, 1, 2); L2 = (2, 1, -2, 1)
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex)
f6 = lambda x: f"{x:.3g}"

# ------------------------------------------------------------------ A
print("== A. exact algebra (far wall carries K_far = -K_near; null conditions are unchanged)")
an = lambda x, y: int(np.array(x) @ KN @ np.array(y))
box = [np.array(v) for v in itertools.product(range(-4, 5), repeat=4) if any(v)]
neu = [v for v in box if v @ QA == 0 and v @ QB == 0]
minors = [L1[i] * L2[j] - L1[j] * L2[i] for i in range(4) for j in range(i + 1, 4)]
gcd = np.gcd.reduce(np.abs(minors))
lat_ok = all(np.linalg.matrix_rank(np.array([L1, L2, v])) == 2 for v in neu)
null_ok = all(an(v, v) == 0 for v in neu)
w1 = sorted({int(np.abs(v).sum()) for v in neu})
minimal = sorted({tuple(v) for v in neu if np.abs(v).sum() == w1[0]})
check("A1 [T] 3450 is anomaly-free (AA = BB = AB = 0); 3451 has AA = -1",
      (an(QA, QA), an(QB, QB), an(QA, QB)) == (0, 0, 0) and an(Q51, Q51) == -1)
check("A2 [T] every U(1)_A x U(1)_B-neutral product of fermion operators has its occupation-change vector in Z l1 + Z l2 "
      "(minors gcd 1), and every such vector is K-null: the neutral lattice is itself a gapping (Lagrangian) lattice",
      lat_ok and null_ok and gcd == 1, f"{len(neu)} neutral vectors in |l_i| <= 4, gcd {gcd}")
check("A3 [T] fewest occupation changes: the minimal neutral terms are exactly +-l1, +-l2 (6 fermion operators; next 8); "
      "max |l_f| = 2 needs two sites (Pauli), so the least local term lives on one nearest-neighbour bond",
      w1[:2] == [6, 8] and set(minimal) == {L1, L2, tuple(-np.array(L1)), tuple(-np.array(L2))},
      f"l1-norms {w1[:3]}, minimal {len(minimal)}")
# A4: phases removable; swap symmetry relates the two terms
perm = [1, 0, 3, 2]; ph = np.array([-1, 1, -1, 1])
m1 = tuple(int(x) for x in ph * np.array(L1)[perm]); m2 = tuple(int(x) for x in ph * np.array(L2)[perm])
check("A4 [T] the free far wall has U(1)^4 and rank[l1; l2] = 2, so both coupling phases rotate away (g1, g2 >= 0); the "
      "free-wall symmetry M = (3<->4, 5<->0, particle-hole c_k -> c_-k^+ on 3 and 5) maps l1 -> l2, l2 -> -l1, so g1 = g2 is "
      "the only M-invariant choice: one coupling g", np.linalg.matrix_rank(np.array([L1, L2])) == 2 and m1 == L2 and m2 == tuple(-np.array(L1)))
iso51 = [v for v in box if v @ Q51 == 0 and an(v, v) == 0]
pairs51 = sum(1 for a, b in itertools.combinations(iso51, 2) if an(a, b) == 0 and np.linalg.matrix_rank(np.array([a, b])) == 2)
check("A5 [T] 3451: a charge kept by a Lagrangian set obeys q^T K q = 0, so no symmetric gapping set exists (brute force: no "
      "mutually null neutral pair); the 3450 terms carry Q51 = l.q51 = 2, 1 (explicit breaking)",
      pairs51 == 0 and (np.array(L1) @ Q51, np.array(L2) @ Q51) == (2, 1), f"{len(iso51)} single null vectors, 0 pairs")

# ------------------------------------------------------------------ B
print("== B. free 2D slab, m = 1: h_s = sin k sx + (1 - cos k) sz, layer bond T = -(sz + i sy)/2")
def slab(k, Ls, m=1.0):
    H = np.zeros((2 * Ls, 2 * Ls), complex); T = -(SZ + 1j * SY) / 2
    for s in range(Ls):
        H[2*s:2*s+2, 2*s:2*s+2] = np.sin(k) * SX + (2 - m - np.cos(k)) * SZ
        if s + 1 < Ls: H[2*s+2:2*s+4, 2*s:2*s+2] = T; H[2*s:2*s+2, 2*s+2:2*s+4] = T.conj().T
    return H
chiF = np.array([1, 1]) / np.sqrt(2); chiN = np.array([1, -1]) / np.sqrt(2)
def wall(k, Ls):
    e, v = np.linalg.eigh(slab(k, Ls)); iF = np.argmin(abs(e - np.sin(k))); iN = np.argmin(abs(e + np.sin(k)))
    return e[iF], e[iN], v[:, iF], v[:, iN]
errs = []; amps = []
for k in np.pi * np.arange(1, 6, 2) / 12:
    eF, eN, vF, vN = wall(k, 12); r = 1 - np.cos(k)
    errs.append(max(abs(eF - np.sin(k)), abs(eN + np.sin(k))) if k < 1.0 else 0)
    amps.append(abs(abs(chiF @ vF[-2:]) - np.sqrt(1 - r * r)) if k < 1.0 else 0)
eF0, eN0, vF0, vN0 = wall(1e-9, 12)
check("B1 [T]/[F] wall modes for |k| < pi/2: far wall E = +sin k (spinor (1,1)/sqrt2), near wall E = -sin k ((1,-1)/sqrt2), "
      "decay r(k) = 1 - cos k per layer, far-layer amplitude a(k) = sqrt(1 - r^2); compact at k = 0 (Ls = 12)",
      max(errs) < 1e-6 and max(amps) < 1e-6 and abs(abs(chiF @ vF0[-2:]) - 1) < 1e-9 and abs(abs(chiN @ vN0[:2]) - 1) < 1e-9,
      f"|dE| {f6(max(errs))}, |da| {f6(max(amps))} for |k| <= pi/4")
kk = np.linspace(-np.pi, np.pi, 61)[:-1]
gap = min(np.sqrt(np.sin(a)**2 + np.sin(b)**2 + (1 - np.cos(a) - np.cos(b))**2) for a in kk for b in kk)
def chern(N=40):
    ks = 2 * np.pi * np.arange(N) / N; U = np.empty((N, N, 2), complex)
    for i, a in enumerate(ks):
        for j, b in enumerate(ks):
            h = np.sin(a) * SX + np.sin(b) * SY + (1 - np.cos(a) - np.cos(b)) * SZ; U[i, j] = np.linalg.eigh(h)[1][:, 0]
    tot = 0
    for i in range(N):
        for j in range(N):
            u1, u2, u3, u4 = U[i, j], U[(i+1) % N, j], U[(i+1) % N, (j+1) % N], U[i, (j+1) % N]
            tot += np.angle((u1.conj() @ u2) * (u2.conj() @ u3) * (u3.conj() @ u4) * (u4.conj() @ u1))
    return tot / (2 * np.pi)
C = chern()
pumpA = SF * QA; pumpB = SF * QB; pump51 = SF * Q51
inL = lambda v: np.linalg.matrix_rank(np.array([L1, L2, v])) == 2
check("B2 [T]/[F] bulk gap 1 and Chern number |C| = 1 per flavour: one flux quantum of a U(1) pumps s_f q_f particles of each "
      "flavour onto the far wall. 3450: the U(1)_A pump (3,4,-5,0) = -l1 + 2 l2 and the U(1)_B pump (2,1,-2,1) = l2 lie in the "
      "neutral lattice (the far ground state may return to itself); 3451: its pump (3,4,-5,-1) carries Q51 = -1",
      abs(gap - 1) < 1e-9 and abs(abs(C) - 1) < 1e-6 and inL(pumpA) and inL(pumpB) and pump51 @ Q51 == -1,
      f"gap {gap:.4f}, C {C:+.4f}")
lk = {}
for Ls in (2, 3, 4, 6):
    lk[Ls] = [abs(chiF @ wall(k, Ls)[3][-2:]) for k in np.pi * np.arange(1, 6, 2) / 12]
rat = [lk[4][i] / lk[3][i] / (1 - np.cos(np.pi * (2 * i + 1) / 12)) for i in range(2)]
check("B3 [T]/[F] the near-wall mode's component along the far-wall spinor at the far layer (its coupling to a far-layer "
      "interaction) falls by r(k) per layer: eps(k, Ls) ~ r^Ls; at k = pi/12, eps = 2e-3, 8e-5, 3e-6 for Ls = 2, 3, 4",
      all(abs(x - 1) < 0.05 for x in rat), "ratio/r " + ", ".join(f"{x:.3f}" for x in rat) +
      "; Ls = 6: " + ", ".join(f6(x) for x in lk[6]) + " at k = pi/12, pi/4, 5pi/12")

# ------------------------------------------------------------------ chain engine
class Chain:
    """blocks: list of (flavour f, chirality s, amplitude function); antiperiodic momenta k = pi t / L, |k| < pi/2."""
    def __init__(self, L, blocks):
        t = np.arange(-L + 1, L, 2); t = t[np.abs(t) < L / 2]
        self.L, self.t, self.k, self.n = L, t, np.pi * t / L, len(t)
        self.blocks = blocks; self.nm = self.n * len(blocks)
        self.fields = {f: [] for f in range(4)}; self.E = np.zeros(self.nm)
        for b, (f, s, amp) in enumerate(blocks):
            for i in range(self.n):
                g = b * self.n + i; self.fields[f].append((g, amp(self.k[i]), int(t[i]))); self.E[g] = s * np.sin(self.k[i])
        self.tm = np.tile(t, len(blocks))
    def sectors(self, charges, target):
        """dict P -> sorted basis states with sum_b q[f_b] (N_b - n/2) = target for every charge vector q."""
        per = []
        for b, (f, s, amp) in enumerate(self.blocks):
            rows = []
            for occ in range(1 << self.n):
                bits = [i for i in range(self.n) if occ >> i & 1]
                rows.append((occ << (b * self.n), *[q[f] * (len(bits) - self.n // 2) for q in charges], sum(self.t[i] for i in bits)))
            per.append(np.array(rows, dtype=np.int64))
        comb = lambda a, b: (a[:, None, :] + b[None, :, :]).reshape(-1, a.shape[1])
        h = len(per) // 2; left = per[0]; right = per[h]
        for x in per[1:h]: left = comb(left, x)
        for x in per[h + 1:]: right = comb(right, x)
        nq = len(charges); out = {}
        rk = {}
        for row in right: rk.setdefault(tuple(row[1:1 + nq]), []).append(row)
        rk = {key: np.array(v) for key, v in rk.items()}
        for row in left:
            need = tuple(int(target[i] - row[1 + i]) for i in range(nq))
            if need not in rk: continue
            R = rk[need]; st = row[0] + R[:, 0]; P = (row[-1] + R[:, -1]) % (2 * self.L)
            for p in np.unique(P): out.setdefault(int(p), []).append(st[P == p])
        return {p: np.sort(np.concatenate(v)) for p, v in out.items()}
    def diag(self, B):
        return sum(self.E[g] * (((B >> g) & 1) - 0.5) for g in range(self.nm))
    def factor(self, f, p):
        L = self.L; ph = lambda t: np.exp(1j * np.pi * t / L); F = self.fields[f]; out = []
        if p == 0: return [(1.0, [], 0)]
        if abs(p) == 1:
            for (g, a, t) in F:
                c = a / np.sqrt(L) * (1 + ph(t)) / 2               # bond average (psi_x + psi_x+1)/2
                out.append((c, [(g, False)], t) if p > 0 else (np.conj(c), [(g, True)], -t))
        else:
            for (g1, a1, t1), (g2, a2, t2) in itertools.combinations(F, 2):
                c = a1 * a2 / L * (ph(t2) - ph(t1))               # psi_x psi_x+1
                out.append((c, [(g1, False), (g2, False)], t1 + t2) if p > 0 else (np.conj(c), [(g2, True), (g1, True)], -t1 - t2))
        return out
    def term(self, B, l):
        L = self.L; rows = []; cols = []; data = []
        for combo in itertools.product(*[self.factor(f, l[f]) for f in range(4)]):
            if sum(c[2] for c in combo) % (2 * L): continue
            coef = L * np.prod([c[0] for c in combo])
            if abs(coef) < 1e-15: continue
            idx = np.arange(len(B)); st = B; sg = np.ones(len(B))
            for (j, d) in reversed([o for c in combo for o in c[1]]):
                ok = ((st >> j) & 1) == (0 if d else 1); idx, st, sg = idx[ok], st[ok], sg[ok]
                if not len(st): break
                sg = sg * (1.0 - 2.0 * (np.bitwise_count(st & ((1 << j) - 1)).astype(np.int64) & 1)); st = st ^ (1 << j)
            if not len(st): continue
            pos = np.searchsorted(B, st); assert np.all(B[pos] == st)
            rows.append(pos); cols.append(idx); data.append(coef * sg)
        if not rows: return sp.csr_matrix((len(B), len(B)), dtype=complex)
        return sp.csr_matrix((np.concatenate(data), (np.concatenate(rows), np.concatenate(cols))), shape=(len(B), len(B)))
    def parts(self, B, terms):
        V = sum((lambda O: O + O.getH())(self.term(B, l)) for l in terms)
        return sp.diags(self.diag(B)).astype(complex), V.tocsr()

def low(H, k=2):
    if H.shape[0] <= 600: return np.linalg.eigvalsh(H.toarray())[:k]
    return np.sort(sla.eigsh(H, k=k, which='SA', return_eigenvectors=False, tol=1e-10, v0=rng.standard_normal(H.shape[0])))

aF = lambda k: np.sqrt(max(0.0, 1 - (1 - np.cos(k))**2))
FAR = [(f, SF[f], aF) for f in range(4)]
def spectrum(ch, charges, target, terms, gs, kk=2):
    out = {g: {} for g in gs}
    for P, B in ch.sectors(charges, target).items():
        D, V = ch.parts(B, terms)
        for g in gs: out[g][P] = low(D + g * V, kk)
    return out

# ------------------------------------------------------------------ C
print("== C. far-wall chain, the two 6-fermion bond terms, coupling g (criteria fixed after scratch exploration, see note)")
res = {}
for L, gs in ((8, (0.0, 40.0, 200.0)), (12, (0.0, 40.0, 200.0))):
    ch = Chain(L, FAR)
    neu_ = spectrum(ch, [QA, QB], (0, 0), (L1, L2), gs)
    one = {sg: spectrum(ch, [QA, QB], (sg * 3, sg * 2), (L1, L2), gs, 1) for sg in (1, -1)}
    for g in gs:
        E0 = min(v[0] for v in neu_[g].values()); allE = np.sort(np.concatenate(list(neu_[g].values())))
        sp1 = 0.5 * sum(min(v[0] for v in one[sg][g].values()) for sg in (1, -1)) - E0
        perP = [neu_[g][P][0] - E0 for P in (2, 4)]
        res[(L, g)] = dict(gap=allE[1] - E0, gsP=[P for P, v in neu_[g].items() if v[0] - E0 < 1e-9], sp=sp1, perP=perP)
    print(f"   L = {L} (n = {ch.n} modes/flavour): " + "; ".join(
        f"g={g:.0f} gap {res[(L,g)]['gap']:.3f} sp {res[(L,g)]['sp']:.3f} E(P1,P2) {res[(L,g)]['perP'][0]:.2f},{res[(L,g)]['perP'][1]:.2f}" for g in gs))
check("C1 [T] g = 0 is the free mirror: neutral gap 2 sin(pi/L), single-particle gap sin(pi/L)",
      all(abs(res[(L, 0.0)]['gap'] - 2 * np.sin(np.pi / L)) < 1e-9 and abs(res[(L, 0.0)]['sp'] - np.sin(np.pi / L)) < 1e-9 for L in (8, 12)))
r12 = res[(12, 200.0)]
check("C2 [F] L = 12, g = 200: unique ground state (neutral, P = 0); neutral gap and single-particle gap > 1 (free 0.52, 0.26); "
      "flat lowest branch E(2 dk)/E(dk) < 1.5 (a linear gapless mode gives 2)",
      r12['gsP'] == [0] and r12['gap'] > 1 and r12['sp'] > 1 and r12['perP'][1] / r12['perP'][0] < 1.5,
      f"gap {r12['gap']:.3f}, sp {r12['sp']:.3f}, ratio {r12['perP'][1]/r12['perP'][0]:.2f}")
check("C3 [F] intermediate coupling: at g = 40 the neutral gap has a minimum (< 0.15 at L = 8 and 12; a level crossing in the "
      "P = 0 sector between the free-like and the strong-coupling ground state)",
      res[(8, 40.0)]['gap'] < 0.15 and res[(12, 40.0)]['gap'] < 0.15, f"{res[(8,40.0)]['gap']:.3f}, {res[(12,40.0)]['gap']:.3f}")
r8 = res[(8, 200.0)]
check("C4 [F] (size trend: recorded result) L = 8 (4 modes/flavour: one lattice step +-l1, +-l2 fills the window) has a "
      "quasi-doublet at g = 200 (gap < 0.25 against > 1 at L = 12): the n = 4 chain is mode-capped, n = 8 (L = 16, sector "
      "dimension 2.3e6) is beyond the budget, so NO finite-size trend is extracted", r8['gap'] < 0.25 and r12['gap'] > 1,
      f"L8 gap {r8['gap']:.3f}, sp {r8['sp']:.3f}")

# ------------------------------------------------------------------ D
print("== D. near-wall flavour-3 modes in the chain (L = 8, g = 200), coupled through their exact far-layer leak eps(k, Ls)")
shifts = {}
for Ls in (None, 2, 3, 4):
    epsf = (lambda k: 0.0) if Ls is None else (lambda k, Ls=Ls: abs(chiF @ wall(k, Ls)[3][-2:]))
    ch = Chain(8, FAR + [(0, -1, epsf)])
    sec0 = ch.sectors([QA, QB], (0, 0)); sec1 = ch.sectors([QA, QB], (3, 2))
    e0 = {P: low((lambda D, V: D + 200.0 * V)(*ch.parts(B, (L1, L2))), 1)[0] for P, B in sec0.items()}
    P0 = min(e0, key=e0.get); E0 = e0[P0]                    # near Fermi sea carries momentum t = 1 + 3
    P1 = (P0 - 1) % 16; D_, V_ = ch.parts(sec1[P1], (L1, L2))  # add a near particle at t = -1
    shifts[Ls] = low(D_ + 200.0 * V_, 1)[0] - E0 - np.sin(np.pi / 8)
    if Ls: shifts[(Ls, 'e')] = max(abs(chiF @ wall(k, Ls)[3][-2:]) for k in np.pi * np.array([1, 3]) / 8)
sc = [abs(shifts[Ls]) / shifts[(Ls, 'e')]**2 for Ls in (2, 3, 4)]
print("   shift at eps = 0: " + f6(shifts[None]))
check("D1 [F] the near-wall left mover k = -pi/8 (charge 3) keeps its free level sin(pi/8) to O(eps^2): exact at eps = 0, "
      "shift / eps_max^2 bounded as Ls grows, and < 1e-3 by Ls = 4  [criteria: |shift(eps=0)| < 1e-10, shift(4) < 1e-3, "
      "shift/eps^2 not growing]", abs(shifts[None]) < 1e-10 and abs(shifts[4]) < 1e-3 and sc[2] <= 1.5 * sc[0],
      "shift " + ", ".join(f6(shifts[Ls]) for Ls in (2, 3, 4)) + " (Ls 2,3,4); /eps^2 " + ", ".join(f6(x) for x in sc))

# ------------------------------------------------------------------ E
print("== E. anomalous control 3451 (charge (3,4,5,1)); fewest-change symmetric bond terms (l1-norm 4, |l_f| <= 2)")
T51 = [(2, 0, -1, -1), (1, 0, -1, 2), (1, -2, 1, 0)]
ch = Chain(8, FAR)
s51 = {Q: spectrum(ch, [Q51], (Q,), T51, (1000.0,), 1)[1000.0] for Q in (0, -1, 1)}
E0 = min(v[0] for v in s51[0].values()); dE = {Q: min(v[0] for v in s51[Q].values()) - E0 for Q in (-1, 1)}
check("E1 [T] the 3451 terms are neutral and of minimal l1-norm 4 (rank 3: only U(1)_51 is kept); none is K-null",
      all(np.array(l) @ Q51 == 0 and np.abs(l).sum() == 4 and an(l, l) != 0 for l in T51) and np.linalg.matrix_rank(np.array(T51)) == 3)
check("E2 [F] (recorded result, a property of the regulator) the chain ALSO gives 3451 a unique neutral ground state with a "
      "charge gap at g = 1000, L = 8: the wall-mode chain is a non-local (momentum-window) regulator and cannot see the anomaly",
      min(dE.values()) > 1, f"charge gaps Q51 = -1: {dE[-1]:.2f}, +1: {dE[1]:.2f}")
check("E3 [T]+[F] Laughlin pump decides: one U(1)_51 flux quantum moves the far wall into Q51 = -1 (B2), whose lowest state is "
      f"{dE[-1]:.1f} above the ground state, so the would-be symmetric gapped far wall is not returned (no symmetric gapped "
      "far wall for 3451); the 3450 pumps stay in the ground-state sector (B2, C2)", dE[-1] > 1 and pump51 @ Q51 == -1)

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1 << 20)
print(f"Supplied: slab (m = 1), projection onto wall modes, bond forms, g, L, Ls. elapsed {time.time()-T0:.1f}s, peak RSS {rss:.0f} MB")
print(f"TOTAL: PASS={NP} FAIL={NF}")
