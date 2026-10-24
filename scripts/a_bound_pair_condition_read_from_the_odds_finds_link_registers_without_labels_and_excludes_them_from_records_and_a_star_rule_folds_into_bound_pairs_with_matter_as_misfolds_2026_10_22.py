AUDIT_INPUT_PATHS = ('docs/A_BOUND_PAIR_CONDITION_READ_FROM_THE_ODDS_FINDS_LINK_REGISTERS_WITHOUT_LABELS_AND_EXCLUDES_THEM_FROM_RECORDS_AND_A_STAR_RULE_FOLDS_INTO_BOUND_PAIRS_WITH_MATTER_AS_MISFOLDS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Neighbourhood roles: roles and record exclusion read from the odds of a
site's neighbourhood instead of a layout (finite runner, seeded).

Sections
  A  covariance of the role reading (1D ring, 2D 3x3 torus), and uniform odds
     give uniform roles (a free sea has no register sites)
  B  a fold: a uniform star rule (projector on total spin 3/2 of every site's
     nearest-neighbour star) whose zero-phase states are the bound-pair
     coverings; uniqueness, funnel, misfolds (defects) and the period-3 layout
  C  record exclusion: a bound site's lock would fix its partner; quantum-link
     cross-check (rishons found without labels); multi-site register ends
  D  record rate against Born statistics and the arrow, with the actual
     configuration moved by the fewest-change transport (exact LP)
Qubits: occupied = 1.  A 'bound' site x: some face-mirror pair of sets
(A containing x, A' its mirror across a bond, |A| <= 2) has n_A + n_A' definite
while n_A is not.  Supplied: the star rule, sizes, tau, seeds, tolerances.
"""
import time
import numpy as np
from scipy.optimize import linprog

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0
TOL = 1e-10


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}  {vals}")


def popc(s):
    return bin(s).count("1")


def sector(N, k):
    st = [s for s in range(1 << N) if popc(s) == k]
    return st, {s: i for i, s in enumerate(st)}


def bits(st, N):
    return np.array([[(s >> x) & 1 for x in range(N)] for s in st], float)


def star_P(st, idx, a, b, c):
    """projector on total spin 3/2 of sites a,b,c: 1/2 + (2/3)(SaSb+SbSc+SaSc)."""
    D = len(st)
    P = np.eye(D) * 0.5
    for (i, j) in ((a, b), (b, c), (a, c)):
        for n, s in enumerate(st):
            bi, bj = (s >> i) & 1, (s >> j) & 1
            P[n, n] += (2 / 3) * (0.25 if bi == bj else -0.25)
            if bi != bj:
                P[idx[s ^ (1 << i) ^ (1 << j)], n] += (2 / 3) * 0.5
    return P


def cover(st, N, pairs, free):
    """product of singlets on pairs (amplitude +-1/sqrt2) and fixed free bits."""
    v = np.zeros(len(st))
    for n, s in enumerate(st):
        a = 1.0
        for (x, y) in pairs:
            bx, by = (s >> x) & 1, (s >> y) & 1
            a *= 0 if bx == by else (1 if bx else -1) / np.sqrt(2)
        for x, b in free.items():
            a *= ((s >> x) & 1) == b
        v[n] = a
    return v / np.linalg.norm(v)


def roles(p, B, nbr):
    """from occupation odds p over configs: graded c_x = max |corr| with a
    neighbour; sharp bound flag from face-mirror set pairs (sizes 1, 2)."""
    N = B.shape[1]
    m = p @ B
    C = (B * p[:, None]).T @ B - np.outer(m, m)
    var = np.diag(C)
    c = np.zeros(N)
    bound = np.zeros(N, bool)
    for x in range(N):
        for (y, A, Am) in nbr[x]:
            if var[x] > TOL and var[y] > TOL:
                c[x] = max(c[x], abs(C[x, y]) / np.sqrt(var[x] * var[y]))
            sA = B[:, A].sum(1)
            sT = sA + B[:, Am].sum(1)
            vA = p @ sA ** 2 - (p @ sA) ** 2
            vT = p @ sT ** 2 - (p @ sT) ** 2
            if vA > TOL and vT < TOL:
                bound[x] = True
    return c, bound, var


def ring_nbr(N, open_=False):
    nb = []
    for x in range(N):
        L = []
        for d in (1, -1):
            y = x + d
            if open_ and not (0 <= y < N):
                continue
            y %= N
            L.append((y, [x], [y]))
            xm, y2 = x - d, x + 2 * d
            if not open_ or (0 <= xm < N and 0 <= y2 < N):
                L.append((y, [x, xm % N], [y, y2 % N]))
            xp, y3 = x + d, x + 3 * d
            if not open_ or (0 <= xp < N and 0 <= y3 < N):
                L.append((y, [x, xp % N], [(x + 2 * d) % N, y3 % N]))
        nb.append(L)
    return nb


def permute(psi, st, idx, perm):
    out = np.zeros_like(psi)
    for n, s in enumerate(st):
        t = 0
        for x in range(len(perm)):
            if (s >> x) & 1:
                t |= 1 << perm[x]
        out[idx[t]] = psi[n]
    return out


# ---------------------------------------------------------------- A
print("== A. covariance; uniform odds give uniform roles")
N = 8
st, idx = sector(N, 4)
B8 = bits(st, N)
nb8 = ring_nbr(N)
psiD = cover(st, N, [(0, 1), (2, 3), (4, 5), (6, 7)], {})
psiR = RNG.standard_normal(len(st)) + 1j * RNG.standard_normal(len(st))
psiR = 0.3 * psiR / np.linalg.norm(psiR) + psiD
psiR /= np.linalg.norm(psiR)
err = 0.0
for psi in (psiD, psiR):
    c0, b0, _ = roles(abs(psi) ** 2, B8, nb8)
    for perm in ([(x + 1) % N for x in range(N)], [(-x) % N for x in range(N)]):
        c1, b1, _ = roles(abs(permute(psi, st, idx, perm)) ** 2, B8, nb8)
        err = max(err, max(abs(c1[perm[x]] - c0[x]) for x in range(N)),
                  max(float(b1[perm[x]] != b0[x]) for x in range(N)))
# 2D 3x3 torus, all 512 configs
L2 = 3
st2 = list(range(1 << 9))
idx2 = {s: s for s in st2}
B2 = bits(st2, 9)
site = lambda i, j: (i % L2) * L2 + (j % L2)
nb2 = []
for i in range(L2):
    for j in range(L2):
        Ls = []
        for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            y = site(i + di, j + dj)
            Ls.append((y, [site(i, j)], [y]))
        nb2.append(Ls)
psi2 = RNG.standard_normal(512) + 1j * RNG.standard_normal(512)
psi2 /= np.linalg.norm(psi2)
c0, _, _ = roles(abs(psi2) ** 2, B2, nb2)
err2 = 0.0
for g in (lambda i, j: (i + 1, j), lambda i, j: (i, j + 1), lambda i, j: (-j, i)):
    perm = [site(*g(x // L2, x % L2)) for x in range(9)]
    c1, _, _ = roles(abs(permute(psi2, st2, idx2, perm)) ** 2, B2, nb2)
    err2 = max(err2, max(abs(c1[perm[x]] - c0[x]) for x in range(9)))
check(err < 1e-12 and err2 < 1e-12, "A1 [T+D]",
      "the role reading is one functional of each site's neighbourhood odds, so it commutes with translations, the ring "
      "reflection and the square's quarter turn: no site is privileged by the reading",
      f"max mismatch 1D {err:.0e} (cover + random), 2D 3x3 {err2:.0e}")
# A2 free sea (XX ring N=10 half filled): unique ground state, uniform roles, no bound site
N = 10
st, idx = sector(N, 5)
B10 = bits(st, N)
H = np.zeros((len(st), len(st)))
for x in range(N):
    y = (x + 1) % N
    for n, s in enumerate(st):
        if ((s >> x) & 1) != ((s >> y) & 1):
            H[idx[s ^ (1 << x) ^ (1 << y)], n] -= 0.5
w, V = np.linalg.eigh(H)
c, bd, _ = roles(V[:, 0] ** 2, B10, ring_nbr(N))
check(w[1] - w[0] > 1e-6 and np.ptp(c) < 1e-10 and not bd.any(), "A2 [T+D]",
      "translation-invariant odds give every site the same role; the half-filled sea (the update's vacuum in 1D) has no "
      "bound site, so a layout can only come from odds that break translations",
      f"gap {w[1]-w[0]:.3f}; c_x = {c[0]:.4f} at all sites (infinite-ring value 4/pi^2 = {4/np.pi**2:.4f}); bound 0/{N}")

# ---------------------------------------------------------------- B
print("== B. a fold: uniform star rule H = sum_x P_3/2(x-1,x,x+1)")
degs = {}
for N in (8, 10, 12):
    st, idx = sector(N, N // 2)
    H = sum(star_P(st, idx, (x - 1) % N, x, (x + 1) % N) for x in range(N))
    w = np.linalg.eigvalsh(H)
    degs[N] = (int((abs(w) < 1e-9).sum()), w[w > 1e-9][0])
    if N == 10:
        H10, st10, idx10 = H, st, idx
        wv, Vv = np.linalg.eigh(H)
De = cover(st10, 10, [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)], {})
Do = cover(st10, 10, [(1, 2), (3, 4), (5, 6), (7, 8), (9, 0)], {})
ce, be, _ = roles(De ** 2, B10, ring_nbr(10))
check(all(d[0] == 2 for d in degs.values()) and np.linalg.norm(H10 @ De) < 1e-12 and be.all() and np.allclose(ce, 1),
      "B1 [T+D]", "the star rule's zero-phase states are exactly the two bound-pair coverings (one is the other translated): "
      "the fold is unique up to a lattice translation, gapped, and in it every site is bound (all register, no matter)",
      "zero modes/gap " + ", ".join(f"N={n}: {d[0]}/{d[1]:.3f}" for n, d in degs.items()) + f"; overlap <De|Do> = {De@Do:.4f} = 2^(1-N/2)")
# funnel: imaginary-time flow from random starts; selection between the two folds
G = np.linalg.qr(np.stack([De, Do], 1))[0]
fid, sharp = [], 0
for r in range(20):
    v = RNG.standard_normal(len(st10))
    v = Vv @ (np.exp(-30 * wv) * (Vv.T @ v))
    v /= np.linalg.norm(v)
    fid.append(np.linalg.norm(G.T @ v) ** 2)
    _, bb, _ = roles(v ** 2, B10, ring_nbr(10))
    sharp += bb.all()
check(min(fid) > 1 - 1e-9 and sharp == 0, "B2 [D]",
      "funnel: every random start flows into the two-fold manifold, but lands in a superposition of both folds, where no "
      "pair sum is definite; the odds do not choose a fold (records, which never condition odds, cannot either)",
      f"20 starts: min fidelity {min(fid):.12f}; starts landing in one sharp fold {sharp}/20")
# misfolds: odd ring forces one defect; defects are free sites, spin 1/2, mobile, Z2 domain walls
st9, idx9 = sector(9, 5)
B9 = bits(st9, 9)
H9 = sum(star_P(st9, idx9, (x - 1) % 9, x, (x + 1) % 9) for x in range(9))
w9 = np.linalg.eigvalsh(H9)
D1 = cover(st9, 9, [(0, 1), (2, 3), (5, 6), (7, 8)], {4: 1})
c1, b1, _ = roles(D1 ** 2, B9, ring_nbr(9))
st10b, idx10b = sector(10, 6)
H10b = sum(star_P(st10b, idx10b, (x - 1) % 10, x, (x + 1) % 10) for x in range(10))
w10b = np.linalg.eigvalsh(H10b)
check(w9[0] > 1e-6 and (~b1).sum() == 1 and not b1[4] and c1[4] < 1e-12, "B3 [T+D]",
      "a misfold is a domain wall between the two folds: an odd ring must carry one; at the wall one site is free "
      "(no definite pair sum, corr 0), i.e. a matter site carried by the configuration, a spin-1/2 doublet that moves "
      "(band below) and on an even ring appears only in pairs (wall number mod 2 is conserved)",
      f"N=9: E0 {w9[0]:.4f}, lowest 9 span {w9[8]-w9[0]:.4f}; free sites in the wall cover {(~b1).sum()}/9; "
      f"N=10 two-wall E0 {w10b[0]:.4f}; <H> of the cover {D1@H9@D1:.4f}")
# period-3 layout [pair, free] (matter at block centres): three free up spins per 9 sites
lay = {}
for N3 in (9, 12):
    k3 = N3 // 3
    st3, idx3 = sector(N3, 2 * k3)
    H3 = sum(star_P(st3, idx3, (x - 1) % N3, x, (x + 1) % N3) for x in range(N3))
    w3, V3 = np.linalg.eigh(H3)
    Cs = [cover(st3, N3, [((3 * k + a) % N3, (3 * k + a + 1) % N3) for k in range(k3)],
                {(3 * k + a + 2) % N3: 1 for k in range(k3)}) for a in range(3)]
    Gc = np.linalg.qr(np.stack(Cs, 1))[0]
    ng = int((w3 < w3[0] + 1e-9).sum())
    lay[N3] = (np.linalg.norm(Gc.T @ V3[:, :ng]) ** 2 / ng, 3 / len(st3), Cs[0] @ H3 @ Cs[0], w3[0], w3[ng] - w3[0], ng)
check(all(v[0] > 0.8 and v[2] > v[3] + 1e-3 for v in lay.values()), "B4 [D]",
      "at defect density 1/3 (aligned walls) the familiar period-3 layout (bound pair, free site: matter at the block "
      "centre) is the most likely domain of the lowest states (mean over the degenerate set), far above a random state's share, but not stationary: "
      "it is the fold's dominant configuration, not an exact eigen-domain; the density itself is supplied",
      "; ".join(f"N={n}: weight {v[0]:.3f} (random {v[1]:.3f}), <H> {v[2]:.3f} vs E0 {v[3]:.3f}, gap {v[4]:.3f}, ground mult {v[5]}" for n, v in lay.items()))
# 2D: Klein-type star rule zero modes include every dimer covering -> count coverings of LxL tori


def dimer_count(L):
    from functools import lru_cache
    full = (1 << L) - 1

    def fills(col_in):
        res = []

        def rec(i, occ, out):
            if i == L:
                res.append(out)
                return
            if occ >> i & 1:
                rec(i + 1, occ, out)
                return
            rec(i + 1, occ | 1 << i, out | 1 << i)
            j = (i + 1) % L
            if not (occ >> j & 1) and j != i and (j > i or i == L - 1):
                rec(i + 1, occ | 1 << i | 1 << j, out)
        rec(0, col_in, 0)
        return res
    T = {s: fills(s) for s in range(1 << L)}
    tot = 0
    for s0 in range(1 << L):
        vec = {s0: 1}
        for _ in range(L):
            nv = {}
            for s, a in vec.items():
                for o in T[s]:
                    nv[o] = nv.get(o, 0) + a
            vec = nv
        tot += vec.get(s0, 0)
    return tot


dc = {L: dimer_count(L) for L in (4, 6)}
ent = {L: np.log(n) / L ** 2 for L, n in dc.items()}
check(dc[4] > 2 and ent[6] > 0.2, "B5 [T+D]",
      "in two (and three) dimensions the star rule's zero-phase manifold contains every nearest-neighbour pair covering: "
      "the fold is NOT unique, the landscape has a flat bottom with entropy per site near Catalan/pi (0.2916); a "
      "selection rule is needed (count of coverings, a lower bound on the misfold-free folds)",
      f"coverings 4x4 torus {dc[4]}, 6x6 {dc[6]}; ln(count)/site {ent[4]:.3f}, {ent[6]:.3f}")

# ---------------------------------------------------------------- C
print("== C. record exclusion read from the same condition")
p = De ** 2
lockfix = []
for x in range(10):
    y = x + 1 if x % 2 == 0 else x - 1
    for v in (0, 1):
        sel = B10[:, x] == v
        q = p[sel] / p[sel].sum()
        lockfix.append(abs(q @ B10[sel, y] - (1 - v)) < 1e-12)
p1 = D1 ** 2
okfree = True
for v in (0, 1):
    sel = B9[:, 4] == v
    if p1[sel].sum() < 1e-12:
        continue
    q = p1[sel] / p1[sel].sum()
    for y in (3, 5):
        okfree &= 0.01 < q @ B9[sel, y] < 0.99
m4 = p1 @ B9[:, 4]
check(all(lockfix) and okfree, "C1 [T+D]",
      "a record locks exactly one admissible local possibility: locking a bound site's occupation fixes its partner's "
      "(conditional support one value), so it would lock two; locking the free site fixes no neighbour (both values "
      "stay supported). Bound sites therefore carry no record; the free (defect) site can",
      f"pair partner fixed in {sum(lockfix)}/20 locks; wall site P(n=1) {m4:.2f}, neighbours stay open")
# quantum-link cross-check: 1D U(1) link model, S=1/2, ring of 4 matter sites (12 modes)
Lq = 4
M = [3 * j for j in range(Lq)]
RP = [3 * j + 1 for j in range(Lq)]
RM = [(3 * j - 1) % (3 * Lq) for j in range(Lq)]
NQ = 3 * Lq
gauss = lambda s: tuple(((s >> M[j]) & 1) + ((s >> RM[j]) & 1) + ((s >> RP[j]) & 1) for j in range(Lq))
okcfg = [s for s in range(1 << NQ) if all(((s >> RP[j]) & 1) + ((s >> RM[(j + 1) % Lq]) & 1) == 1 for j in range(Lq))]
secs = {}
for s in okcfg:
    secs.setdefault(gauss(s), []).append(s)
gsel = max(secs, key=lambda g: (len(secs[g]), g))
stq = secs[gsel]
iq = {s: i for i, s in enumerate(stq)}


def fop(s, i, dag):
    occ = (s >> i) & 1
    if occ == dag:
        return None, 0
    return s ^ (1 << i), (-1) ** popc(s & ((1 << i) - 1))


Hq = np.zeros((len(stq), len(stq)))
for j in range(Lq):
    k = (j + 1) % Lq
    for n, s in enumerate(stq):
        t, sg = s, 1
        for (i, dg) in ((M[k], 0), (RM[k], 1), (RP[j], 0), (M[j], 1)):
            t, a = fop(t, i, dg) if t is not None else (None, 0)
            sg *= a
        if t is not None and t in iq:
            Hq[iq[t], n] -= sg
            Hq[n, iq[t]] -= sg
    for n, s in enumerate(stq):
        Hq[n, n] += 0.5 * (-1) ** j * ((s >> M[j]) & 1)
wq, Vq = np.linalg.eigh(Hq)
Bq = bits(stq, NQ)
cq, bq, vq = roles(Vq[:, 0] ** 2, Bq, ring_nbr(NQ))
rish = sorted(RP + RM)
gaussdef = all(np.ptp([gauss(s)[j] for s in stq]) == 0 for j in range(Lq))
check(all(bq[r] for r in rish) and not any(bq[m] for m in M) and all(vq[m] > 1e-6 for m in M) and gaussdef,
      "C2 [T+D]", "in a quantum-link ground state the condition, read with no labels, finds exactly the rishons (one unit "
      "bound across the face) and not the matter sites, although each matter site's Gauss cluster (itself and two rishons) "
      "is also definite: a Gauss cluster is not a face-mirror pair, so matter stays recordable",
      f"Gauss sector {gsel}, dim {len(stq)}; bound: rishons {sum(bq[r] for r in rish)}/{len(rish)}, matter "
      f"{sum(bq[m] for m in M)}/{Lq} (matter var {min(vq[m] for m in M):.3f})")
# multi-site ends: two sites per end (spin-1 link), plus a free site
Ne = 5
ste = list(range(1 << Ne))
Be = bits(ste, Ne)
psiE = np.zeros(32, complex)
for s in ste:
    if ((s >> 0) & 1) + ((s >> 1) & 1) + ((s >> 2) & 1) + ((s >> 3) & 1) == 2:
        psiE[s] = RNG.standard_normal() + 1j * RNG.standard_normal()
pE = abs(psiE) ** 2
pE = np.array([pE[s & 15] * (0.36 if not (s >> 4) & 1 else 0.64) for s in ste])
pE /= pE.sum()
nbE = ring_nbr(Ne, open_=True)
cE, bE, _ = roles(pE, Be, nbE)
check(bE[:4].all() and not bE[4], "C3 [T+D]",
      "register ends of several sites (sites 0,1 | 2,3, two per end, total two units) are bound through the face-mirror "
      "set pair though no single site is; a free neighbour is not: the same condition covers edge-type registers whose "
      "ends hold a shared total",
      f"bound {bE.astype(int).tolist()}; max single-site |corr| at the ends {cE[:4].max():.2f}")

# ---------------------------------------------------------------- D
print("== D. record rate vs Born and the arrow (open N=9 chain, one wall)")
N = 9
st, idx = sector(N, 5)
Bd = bits(st, N)
nbd = ring_nbr(N, open_=True)
tau = 1.0
Pst = {x: star_P(st, idx, x - 1, x, x + 1) for x in range(1, N - 1)}
groups = [[1, 4, 7], [2, 5], [3, 6]]
Ug = []
for g in groups:
    U = np.eye(len(st), dtype=complex)
    for x in g:
        U = (np.eye(len(st)) + (np.exp(-1j * tau) - 1) * Pst[x]) @ U
    Ug.append(U)
psi = cover(st, N, [(0, 1), (2, 3), (5, 6), (7, 8)], {4: 1}).astype(complex)
T = 12
ham = np.array([[popc(a ^ b) for b in st] for a in st], float)
psis, couplings, nbound = [psi], [], []
for t in range(T):
    U = Ug[t % 3]
    new = U @ psis[-1]
    p0, p1_ = abs(psis[-1]) ** 2, abs(new) ** 2
    sup = abs(U) > 1e-12
    I0, I1 = np.nonzero(p0 > 1e-14)[0], np.nonzero(p1_ > 1e-14)[0]
    mask = sup[np.ix_(I1, I0)]
    vi = np.argwhere(mask.T)
    nv = len(vi)
    Aeq = np.zeros((len(I0) + len(I1), nv))
    Aeq[vi[:, 0], np.arange(nv)] = 1
    Aeq[len(I0) + vi[:, 1], np.arange(nv)] = 1
    cost = ham[np.ix_(I0, I1)][vi[:, 0], vi[:, 1]]
    res = linprog(cost, A_eq=Aeq, b_eq=np.r_[p0[I0], p1_[I1]], bounds=(0, None), method="highs")
    Pi = np.zeros((len(st), len(st)))
    Pi[I0[vi[:, 0]], I1[vi[:, 1]]] = res.x
    couplings.append(Pi)
    psis.append(new)
marg_err = max(abs(couplings[t].sum(0) - abs(psis[t + 1]) ** 2).max() for t in range(T))
R = [roles(abs(v) ** 2, Bd, nbd) for v in psis]
nb_t = [int(r[1].sum()) for r in R]
check(marg_err < 1e-9 and nb_t[0] == 8 and nb_t[-1] < nb_t[0], "D1 [T+D]",
      "with local star gates the fold is stationary; bound pairs stay exactly bound until the wall's light cone reaches "
      "them, then lose their definite sum: roles change only inside the defect's cone; transport marginals are exact",
      f"bound sites per half-tick {nb_t}; transport marginal error {marg_err:.1e}")
K = 4000
cfg = np.zeros((K, T + 1), int)
p0 = abs(psis[0]) ** 2
cfg[:, 0] = RNG.choice(len(st), size=K, p=p0 / p0.sum())
for t in range(T):
    Pi = couplings[t]
    rows = Pi / np.maximum(Pi.sum(1, keepdims=True), 1e-300)
    cum = np.cumsum(rows, 1)
    u = RNG.random(K)
    cfg[:, t + 1] = np.minimum((cum[cfg[:, t]] < u[:, None]).sum(1), len(st) - 1)
occ = Bd[cfg].astype(int)  # K x (T+1) x N
free = np.array([~r[1] for r in R])  # (T+1) x N
cgr = np.array([r[0] for r in R])
born = np.array([abs(v) ** 2 @ Bd for v in psis])


def run(rule):
    last = -np.ones((K, N), int)
    nrec = np.zeros(T + 1)
    zmax, zbias = 0.0, 0.0
    was = np.zeros(N, bool)
    for t in range(T + 1):
        a = occ[:, t, :]
        if rule == "R1":
            form = np.broadcast_to(free[t], (K, N)).copy()
        elif rule == "R3":
            ch = a != occ[:, t - 1, :] if t else np.ones((K, N), bool)
            form = (ch | (free[t] & ~was)[None, :] | (last < 0)) & free[t][None, :]
        elif rule == "R2":
            form = np.broadcast_to(free[t] & ~was, (K, N)).copy()
        elif rule == "R0":
            form = (last < 0) & free[t][None, :]
        elif rule == "cfg":
            nbx = np.zeros((K, N), bool)
            nbx[:, 1:] |= a[:, :-1] != a[:, 1:]
            nbx[:, :-1] |= a[:, 1:] != a[:, :-1]
            form = free[t][None, :] & ~nbx
        elif rule == "grad":
            form = RNG.random((K, N)) < (1 - cgr[t])[None, :]
        last = np.where(form, a, last)
        nrec[t] = form.sum() / K
        was = was | free[t]
        for x in range(N):
            f = form[:, x]
            if rule in ("cfg", "grad") and f.sum() > 200:
                pb = born[t, x]
                fr = a[f, x].mean()
                s = np.sqrt(max(pb * (1 - pb), 1e-12) / f.sum())
                zbias = max(zbias, abs(fr - pb) / s if pb * (1 - pb) > 1e-9 else (0 if abs(fr - pb) < 1e-12 else 1e9))
            h = last[:, x] >= 0
            if free[t, x] and h.sum() > 200:
                pb = born[t, x]
                fr = last[h, x].mean()
                s = np.sqrt(max(pb * (1 - pb), 1e-12) / h.sum())
                zmax = max(zmax, abs(fr - pb) / s if pb * (1 - pb) > 1e-9 else (0 if abs(fr - pb) < 1e-12 else 1e9))
    return zmax, zbias, np.cumsum(nrec)


out = {r: run(r) for r in ("R1", "R3", "R2", "R0", "cfg", "grad")}
z = {r: out[r][0] for r in out}
mono = all(np.all(np.diff(out[r][2]) >= 0) for r in out)
check(z["R1"] < 5 and z["R3"] < 5 and z["R2"] > 8 and z["R0"] > 8 and mono, "D2 [D]",
      "Born: reading each free site's latest record reproduces the Born marginal when a record forms every half-tick (R1) "
      "or whenever the occupation changes or the site turns free (R3, the fewest-change rate); records only when the "
      "neighbourhood condition changes (R2) or once ever (R0) go stale. Record counts never fall (the arrow) in every rule",
      f"max z: R1 {z['R1']:.1f}, R3 {z['R3']:.1f}, R2 {z['R2']:.1f}, R0 {z['R0']:.1f}; records by t=12: "
      + ", ".join(f"{r} {out[r][2][-1]:.1f}" for r in ("R1", "R3", "R2", "R0")))
check(out["grad"][1] < 5 and out["cfg"][1] > 8, "D3 [T+D]",
      "exclusion must be read from the odds, never from the actual configuration: an odds-read formation chance "
      "(1 - max|corr|) leaves recorded values Born; excluding sites whose actual neighbour holds the opposite value biases them",
      f"recorded-value bias z: odds-read graded {out['grad'][1]:.1f}; configuration-read {out['cfg'][1]:.1f}")
print("supplied: star rule (B-D), link model w=1, m=0.5 (C2), sizes, tau=1, K=4000, tolerance 1e-10, seed 20261022")
print(f"runtime {time.time()-T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
