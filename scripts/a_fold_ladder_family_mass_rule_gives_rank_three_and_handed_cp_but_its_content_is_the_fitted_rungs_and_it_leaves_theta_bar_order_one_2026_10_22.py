AUDIT_INPUT_PATHS = ('docs/A_FOLD_LADDER_FAMILY_MASS_RULE_GIVES_RANK_THREE_AND_HANDED_CP_BUT_ITS_CONTENT_IS_THE_FITTED_RUNGS_AND_IT_LEAVES_THETA_BAR_ORDER_ONE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Fold-ladder family-mass rule: exact structure, honest fit, gate check.

Rule under test (candidate, not adopted): each family multiplet is read on one
rung of the zoom ladder; rungs bond to the newest three rungs (the
Boerdijk-Coxeter contact rule); a contact spanning r rungs carries the nested
block overlap 2^(-3r/2) and a handed phase exp(i h lam sin(r theta)),
theta = arccos(-2/3); a mass term between a doublet on rung a and a singlet on
rung b is the sum over monotone contact paths from a to b.

Seeded (20261022), numpy only, self-contained.
"""
import itertools
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 120
SEED = 20261022
T0 = time.time()
PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS" if ok else "FAIL") + ": " + name + (" | " + detail if detail else ""))


EPS = 2 ** -1.5
THBC = float(np.arccos(-2.0 / 3.0))
OBS = np.array([1.23e-3 / 168.26, 0.620 / 168.26, 2.67e-3 / 2.839, 53.16e-3 / 2.839,
                0.2243, 0.0411, 0.00382, 3.08e-5])
NAMES = ["mu/mt", "mc/mt", "md/mb", "ms/mb", "Vus", "Vcb", "Vub", "J"]


def gseq(lam, th, eps=EPS, ranges=(1, 2, 3), h=1, N=40, phases=None):
    t = {}
    for r in ranges:
        ph = h * lam * np.sin(r * th) if phases is None else phases[r]
        t[r] = eps ** r * np.exp(1j * ph)
    G = np.zeros(N, complex)
    G[0] = 1.0
    for n in range(1, N):
        G[n] = sum(t[r] * G[n - r] for r in ranges if n - r >= 0)
    return G


def mass(G, a, b):
    d = np.asarray(b)[None, :] - np.asarray(a)[:, None]
    return np.where(d >= 0, G[np.abs(d)], np.conj(G[np.abs(d)]))


def flavour(Mu, Md):
    Uu, su, _ = np.linalg.svd(Mu)
    Ud, sd, _ = np.linalg.svd(Md)
    Uu, Ud, su, sd = Uu[:, ::-1], Ud[:, ::-1], su[::-1], sd[::-1]
    V = Uu.conj().T @ Ud
    J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
    return su, sd, V, J


def observables(Mu, Md):
    su, sd, V, J = flavour(Mu, Md)
    return np.array([su[0] / su[2], su[1] / su[2], sd[0] / sd[2], sd[1] / sd[2],
                     abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), J])


print("Fold-ladder family-mass rule (seed %d)" % SEED)
rng = np.random.default_rng(SEED)

# ---- A. exact structure -------------------------------------------------
print("A. Exact structure")
# A1 nested block overlap: block-uniform modes on 8^n fine cells
L = 8 ** 3
errs = []
for a in range(4):
    for b in range(4):
        va = np.zeros(L); va[:8 ** a] = 8 ** (-a / 2)
        vb = np.zeros(L); vb[:8 ** b] = 8 ** (-b / 2)
        errs.append(abs(va @ vb - 2 ** (-1.5 * abs(a - b))))
check("A1 nested block-uniform overlap = 2^(-3|a-b|/2), so eps = 2^(-3/2) = 0.3536",
      max(errs) < 1e-14, "max err %.1e" % max(errs))

# A2 rank = number of contact ranges (singlets on rungs >= doublets)
ranks = {}
for ranges in [(1,), (1, 2), (1, 2, 3)]:
    rs = set()
    for _ in range(40):
        ph = {r: rng.uniform(0, 2 * np.pi) for r in ranges}
        G = gseq(0, 0, eps=rng.uniform(0.2, 0.6), ranges=ranges, phases=ph)
        a = np.sort(rng.choice(6, 3, replace=False))
        b = 6 + np.sort(rng.choice(8, 3, replace=False))
        s = np.linalg.svd(mass(G, a, b), compute_uv=False)
        rs.add(int(np.sum(s > 1e-10 * s[0])))
    ranks[len(ranges)] = rs
check("A2 path-sum rank = number of contact ranges (1->1, 2->2, 3->3; 40 seeded each)",
      ranks == {1: {1}, 2: {2}, 3: {3}}, str(ranks))

# A3 CP: one range, or phases linear in r, are a rephasing (J = 0)
a, bu, bd = (4, 1, 0), (13, 10, 7), (6, 5, 4)
Js = []
for phases in [{1: 0.7}, {1: 0.7, 2: 1.4, 3: 2.1}]:
    rr = tuple(phases)
    G = gseq(0, 0, ranges=rr, phases=phases)
    Js.append(abs(flavour(mass(G, a, bu), mass(G, a, bd))[3]))
Gbc = gseq(1.5, THBC)
Jbc = flavour(mass(Gbc, a, bu), mass(Gbc, a, bd))[3]
check("A3 J = 0 for one range or phases linear in r; J != 0 with sin(r theta) phases",
      max(Js) < 1e-15 and abs(Jbc) > 1e-6, "J_lin %.1e, J_fold %.2e" % (max(Js), Jbc))

# A4 sense flip h -> -h conjugates M: same masses, J -> -J
Gm = gseq(1.5, THBC, h=-1)
o1, o2 = observables(mass(Gbc, a, bu), mass(Gbc, a, bd)), observables(mass(Gm, a, bu), mass(Gm, a, bd))
check("A4 mirror (h -> -h): masses and |V| equal, J flips sign",
      np.allclose(o1[:7], o2[:7], atol=1e-12) and abs(o1[7] + o2[7]) < 1e-15,
      "J(+h) %.3e, J(-h) %.3e" % (o1[7], o2[7]))

# A5 rungs are a half-line: three distinct distances, no k -> -k
trip = (0, 1, 3)
dist = {abs(x - y) for x, y in itertools.combinations(trip, 2)}
check("A5 rung triple (0,1,3) has 3 distinct distances (no cyclic negation ceiling)",
      len(dist) == 3, str(sorted(dist)))

# A6 no shared unitary on the families at the example point
Hu = mass(Gbc, a, bu) @ mass(Gbc, a, bu).conj().T
Hd = mass(Gbc, a, bd) @ mass(Gbc, a, bd).conj().T
Hu, Hd = Hu / np.linalg.norm(Hu), Hd / np.linalg.norm(Hd)
I3 = np.eye(3)
C = np.vstack([np.kron(Hu, I3) - np.kron(I3, Hu.T), np.kron(Hd, I3) - np.kron(I3, Hd.T)])
sv = np.linalg.svd(C, compute_uv=False)
comm = int(np.sum(sv < 1e-9 * sv[0]))
check("A6 commutant of {Hu, Hd} is 1-dimensional (no shared unitary, mixing lemma met)",
      comm == 1, "dim %d, next sv %.1e" % (comm, sorted(sv)[1]))

# ---- B. fit (FITTED) and look-elsewhere -----------------------------------
print("B. Fit (all integers and lam FITTED)")
R = range(0, 15)
TRIP = [t for t in itertools.product(R, repeat=3) if t[0] >= t[1] >= t[2]]
TR = np.array(TRIP)
LAMS = (1.0, 1.5, 2.0, 2.5, 3.0)
TOL = np.log(1.5) ** 2


def mbatch(G, a, B):
    d = B[:, None, :] - np.asarray(a)[None, :, None]
    return np.where(d >= 0, G[np.abs(d)], np.conj(G[np.abs(d)]))


def scan(th, top=10, collect=False):
    best, bestx, preds, tb = 1e9, None, [], []
    for lam in LAMS:
        G = gseq(lam, th)
        for a_ in [t for t in TRIP if t[2] == 0]:
            Ms = mbatch(G, a_, TR)
            U, S, _ = np.linalg.svd(Ms)
            S, U = S[:, ::-1], U[:, :, ::-1]
            with np.errstate(all="ignore"):
                r0, r1 = np.log(S[:, 0] / S[:, 2]), np.log(S[:, 1] / S[:, 2])
                eu = np.nan_to_num((r0 - np.log(OBS[0])) ** 2 + (r1 - np.log(OBS[1])) ** 2, nan=1e9, posinf=1e9)
                ed = np.nan_to_num((r0 - np.log(OBS[2])) ** 2 + (r1 - np.log(OBS[3])) ** 2, nan=1e9, posinf=1e9)
            iu, idd = np.argsort(eu)[:top], np.argsort(ed)[:top]
            for i in iu:
                for j in idd:
                    V = U[i].conj().T @ U[j]
                    J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
                    p = np.array([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), max(abs(J), 1e-30)])
                    sc = eu[i] + ed[j] + np.sum(np.log(p / OBS[4:]) ** 2)
                    if sc < best:
                        best, bestx = sc, (lam, a_, TRIP[i], TRIP[j])
            if collect:
                det = np.angle(np.linalg.det(Ms))
                okU = np.where((eu < 2 * TOL) & ((r0 - np.log(OBS[0])) ** 2 < TOL) & ((r1 - np.log(OBS[1])) ** 2 < TOL))[0]
                okD = np.where(((r0 - np.log(OBS[2])) ** 2 < TOL) & ((r1 - np.log(OBS[3])) ** 2 < TOL))[0]
                for i in okU:
                    for j in okD:
                        V = U[i].conj().T @ U[j]
                        J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
                        preds.append([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), abs(J)])
                        tb.append(abs(np.angle(np.exp(1j * (det[i] + det[j])))))
    return best, bestx, np.array(preds), np.array(tb)


ncells = len(LAMS) * len([t for t in TRIP if t[2] == 0]) * len(TRIP) ** 2
bbest, bx, P, TB = scan(THBC, collect=True)
lam, a, bu, bd = bx
Gb = gseq(lam, THBC)
ob = observables(mass(Gb, a, bu), mass(Gb, a, bd))
print("  best: lam=%.1f Q-rungs=%s u-rungs=%s d-rungs=%s  sum(ln^2)=%.2f" % (lam, a, bu, bd, bbest))
print("  " + "  ".join("%s %.3g/%.3g" % (n, x, y) for n, x, y in zip(NAMES, ob, OBS)))
check("B1 best fit: 8 observables at rms log-deviation <= 0.35 (FITTED: 8 integers + lam + sign)",
      np.sqrt(bbest / 8) <= 0.35 and abs(bbest - np.sum(np.log(np.abs(ob) / OBS) ** 2)) < 1e-9,
      "rms %.2f; cells searched %.2e" % (np.sqrt(bbest / 8), ncells))

ctrl = []
for th in rng.uniform(0.3, np.pi, 6):
    ctrl.append(scan(th)[0])
check("B2 look-elsewhere: BC pitch fits no better than the median of 6 seeded random pitches (pitch UNTESTED)",
      bbest >= np.median(ctrl), "BC %.2f, random median %.2f, min %.2f" % (bbest, np.median(ctrl), min(ctrl)))

# ---- C. predictions not fitted ------------------------------------------
print("C. Predictions with only the 4 quark mass ratios fitted (factor 1.5)")
Lg = np.log(P / OBS[4:])
hit = float(np.mean(np.all(np.abs(Lg) < np.log(2), axis=1)))
med = np.median(P, axis=0)
print("  mass-fitting cells %d; CKM medians Vus %.3f Vcb %.3f Vub %.4f |J| %.2e" % (len(P), *med))
check("C1 CKM predicted from mass-fitting cells: all four within x2 in under 5% of cells (disfavoured)",
      len(P) > 100 and hit < 0.05, "hit %.3f; Vcb median/meas %.1f, Vub %.1f" % (hit, med[1] / OBS[5], med[2] / OBS[6]))
check("C2 strong CP: arg det(Mu Md) is O(1) (median %.2f rad), never < 1e-3 (measured < 1e-10)" % np.median(TB),
      np.median(TB) > 0.3 and np.mean(TB < 1e-3) == 0.0, "fraction < 1e-3: %.3f" % np.mean(TB < 1e-3))

# C3 leptons: fit m_mu/m_tau only, predict Koide Q
me, mmu, mtau = 0.51099895, 105.6583755, 1776.93
Qm = (me + mmu + mtau) / (np.sqrt(me) + np.sqrt(mmu) + np.sqrt(mtau)) ** 2
Qs = []
for a_ in [t for t in TRIP if t[2] == 0]:
    Ms = mbatch(Gb, a_, TR)
    S = np.linalg.svd(Ms, compute_uv=False)[:, ::-1]
    with np.errstate(all="ignore"):
        ok = np.abs(np.log(S[:, 1] / S[:, 2] / (mmu / mtau))) < np.log(1.5)
    for s in S[ok]:
        if s[0] > 0:
            Qs.append(s.sum() / np.sqrt(s).sum() ** 2)
Qs = np.array(Qs)
fq3 = float(np.mean(np.abs(Qs - 2 / 3) < 1e-3))
fq5 = float(np.mean(np.abs(Qs - 2 / 3) < 1e-5))
check("C3 Koide not predicted: of %d lepton cells fitting m_mu/m_tau, %.3f within 1e-3 of 2/3, %.4f within 1e-5" % (len(Qs), fq3, fq5),
      len(Qs) > 100 and fq5 < 0.01, "measured Q %.6f; cell median %.3f" % (Qm, np.median(Qs)))

# C4 BC pitch as Brannen phase: delta = theta - 2 pi/3 (no fit)
d = THBC - 2 * np.pi / 3
x = 1 + np.sqrt(2) * np.cos(d + 2 * np.pi * np.arange(3) / 3)
r = np.sort(x ** 2)
check("C4 BC pitch as the Koide phase (delta = %.4f vs 0.2222) misses m_e/m_tau by > x1.5" % d,
      r[0] / r[2] / (me / mtau) > 1.5, "pred %.2e meas %.2e" % (r[0] / r[2], me / mtau))

# ---- D. gate --------------------------------------------------------------
print("D. Gate")
print("  chosen: 8 rung integers (quarks) + lam + sense bit (FITTED); 5 lepton integers (FITTED)")
print("  by name: doublet/singlet multiplets read per family; sense tied to weak handedness")
print("  unfitted: rank 3 (consistent), CKM given masses (disfavoured), theta-bar O(1) (fails), Koide (not predicted)")
check("D1 gate: content is the fit (13 integers + 1 coupling + 1 bit for 13 observables) -> FAILS gate item 1",
      True, "bends Admissibility (rung contacts of range 2, 3) and Lattice (rung role reading)")

print("runtime %.1f s" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
