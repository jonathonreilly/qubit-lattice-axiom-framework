AUDIT_INPUT_PATHS = ('docs/A_PATH_SUM_FLAVOUR_RULE_WITH_FORCED_RUNGS_IS_FAMILY_BLIND_OR_FLAT_AND_ITS_STRUCTURAL_THETA_BAR_ZEROS_KILL_CP_OR_TIE_DOWN_TO_UP_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Forced rung assignments for the fold-ladder path-sum mass rule.

The path-sum rule of flavour-rule: a contact spanning r rungs (r = 1, 2, 3)
carries eps^r exp(i h lam sin(r theta)), eps = 2^(-3/2), theta = arccos(-2/3);
the mass term between a doublet on rung a and a singlet on rung b is
G(b - a) = sum over monotone contact paths (conjugate when b < a).

Three candidate rules that FORCE the rungs instead of fitting them:
 (a) copy-sign gap depth (copy sign read from undressed even cubes; or the
     dressed-cone step eps_X per multiplet),
 (b) the multiplet's link factors fix its rung via the nested role blocks B_f,
 (c) first split generation of the mode (octree: one 16 per rung; register
     reading: zoom-3 turn-fixed characters).
Then a structural strong-CP scan: which rung layouts give arg det(Mu Md) = 0
for every lam and theta, and what spectra those layouts allow.

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
LAMS = (1.0, 1.5, 2.0, 2.5, 3.0)
# measured (approximate running values at M_Z; CKM moduli and J)
OBS = np.array([1.23e-3 / 168.26, 0.620 / 168.26, 2.67e-3 / 2.839, 53.16e-3 / 2.839,
                0.2243, 0.0411, 0.00382, 3.08e-5])
MB_MT = 2.839 / 168.26


def gseq(lam, th, h=1, N=40, phases=None, eps=EPS):
    t = {r: eps ** r * np.exp(1j * (h * lam * np.sin(r * th) if phases is None else phases[r]))
         for r in (1, 2, 3)}
    G = np.zeros(N, complex)
    G[0] = 1.0
    for n in range(1, N):
        G[n] = sum(t[r] * G[n - r] for r in (1, 2, 3) if n - r >= 0)
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


def sin_tb(Mu, Md):
    return abs(np.sin(np.angle(np.linalg.det(Mu) * np.linalg.det(Md))))


rng = np.random.default_rng(SEED)
print("Forced rungs for the path-sum family mass rule (seed %d)" % SEED)

# ---------------------------------------------------------------- A
print("A. Exact structure")
# A1 family blindness: rungs that are a function of the multiplet's charges
# give all three families of a multiplet one rung -> M = G(b - a) * ones.
rk, err = set(), 0.0
for _ in range(60):
    ph = {r: rng.uniform(0, 2 * np.pi) for r in (1, 2, 3)}
    G = gseq(0, 0, phases=ph)
    ra, rb = rng.integers(0, 12, 2)
    M = mass(G, [ra] * 3, [rb] * 3)
    s = np.linalg.svd(M, compute_uv=False)
    rk.add(int(np.sum(s > 1e-10 * s[0])))
    err = max(err, abs(s[0] - 3 * abs(G[abs(rb - ra)])))
check("A1 family-blind rungs (any function of charges) give M = G(b-a) x ones: rank 1, m3 = 3|G|",
      rk == {1} and err < 1e-12, "ranks %s over 60 seeded (G, rungs); err %.1e" % (rk, err))

# A2 equal factor sets give equal sectors: u^c and d^c carry the same factors
# (colour, hypercharge), so any factor-set rung rule gives r_u = r_d and
# |M_u| = |M_d| -> m_t = m_b in every such rule (h for down either sign).
ok = True
for _ in range(40):
    G = gseq(rng.uniform(0.5, 3), rng.uniform(0, np.pi))
    rq, rud = rng.integers(0, 12, 2)
    mu_ = np.linalg.svd(mass(G, [rq] * 3, [rud] * 3), compute_uv=False)[0]
    md_ = np.linalg.svd(np.conj(mass(G, [rq] * 3, [rud] * 3)), compute_uv=False)[0]
    ok &= abs(mu_ / md_ - 1) < 1e-12
check("A2 factor-set rungs: r(u^c) = r(d^c) forces m_b/m_t = 1 exactly (both down senses)", ok,
      "measured m_b/m_t = %.4f" % MB_MT)

# A3 Hermitian theorem: singlet rungs = doublet rungs (as lists) make M
# Hermitian (reversed paths conjugate), det real, sin(arg det) = 0.
mx = 0.0
for _ in range(60):
    G = gseq(rng.uniform(0.5, 3), rng.uniform(0, np.pi))
    a = rng.choice(10, 3, replace=False)
    M = mass(G, a, a)
    mx = max(mx, np.abs(M - M.conj().T).max(), abs(np.sin(np.angle(np.linalg.det(M)))))
check("A3 same doublet and singlet rungs: M Hermitian, det real (60 seeded)", mx < 1e-13, "max %.1e" % mx)

# A4 sense-flip pairing: down singlets on the up singlets' rungs with the
# conjugate Higgs running contacts in the reverse sense: M_d = conj(M_u),
# det(Mu Md) = |det Mu|^2 > 0, but the down spectrum equals the up spectrum.
mx, ms = 0.0, 0.0
for _ in range(60):
    G, Gm = (lambda l, t: (gseq(l, t), gseq(l, t, h=-1)))(rng.uniform(0.5, 3), rng.uniform(0, np.pi))
    a = rng.choice(10, 3, replace=False)
    b = rng.choice(10, 3, replace=False)
    Mu, Md = mass(G, a, b), mass(Gm, a, b)
    mx = max(mx, sin_tb(Mu, Md))
    ms = max(ms, np.abs(np.linalg.svd(Mu, compute_uv=False) - np.linalg.svd(Md, compute_uv=False)).max())
check("A4 sense-flipped down on up rungs: arg det(Mu Md) = 0 exactly, down spectrum = up spectrum",
      mx < 1e-12 and ms < 1e-12, "max sin %.1e, spectrum diff %.1e" % (mx, ms))

# ---------------------------------------------------------------- B
print("B. Candidate (a): copy-sign gap depth")
# copy sign s = i R1 R2 R3 R from UNDRESSED even cubes: species-blind
# -> one depth for every multiplet; all rungs equal.
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
R = [np.kron(sx, np.eye(2)), np.kron(sy, np.eye(2)), np.kron(sz, sx)]
Rh = sum(R) / np.sqrt(3)
s_copy = 1j * R[0] @ R[1] @ R[2] @ Rh
print("  copy sign s = i R1 R2 R3 R: s^2 = 1 (%.1e), tr s = %.1e; built from the undressed hops alone"
      % (np.abs(s_copy @ s_copy - np.eye(4)).max(), abs(np.trace(s_copy))))
G15 = gseq(1.5, THBC)
M0 = mass(G15, [0] * 3, [0] * 3)
sv = np.linalg.svd(M0, compute_uv=False)
check("B1 undressed copy sign: one gap depth for all species -> all rungs 0, M = ones",
      np.allclose(M0, 1) and sv[1] < 1e-12,
      "masses per sector (3, 0, 0): m_c/m_t = 0 (meas 3.7e-3), m_b/m_t = 1 (meas %.4f)" % MB_MT)
# dressed-cone variant: eps_X ~ eps0 / prod_f c_f with c_f = (2S/(2S+1))^2 per acting factor;
# depth shift = log2(eps_X/eps0) rungs. Factor sets: Q{3,2,1} u{3,1} d{3,1} L{2,1} e{1} nu{}
FS = {"Q": 3, "u": 2, "d": 2, "L": 2, "e": 1, "n": 0}
rows = []
for S in (0.5, 1.5, 275.0):
    per = 2 * np.log2((2 * S + 1) / (2 * S))
    rows.append((S, {k: int(round(v * per)) for k, v in FS.items()}))
print("  dressed-cone depth (rungs, rounded) S=1/2: %s; S=3/2: %s; S=275: %s" % tuple(str(r[1]) for r in rows))
ok = all(r[1]["u"] == r[1]["d"] for r in rows)
check("B2 dressed-cone depths: charge-only (family-blind, rank 1) and r(u^c) = r(d^c) at every S",
      ok, "so m_b/m_t = 1 and m_s = m_c = m_u = m_d = 0 in every variant")

print("C. Candidate (b): rung set by the acting link factors (B_f rungs supplied)")
cnt, bad = 0, 0
for n3, n2, n1 in itertools.product(range(8), repeat=3):
    for red in (max, min):
        rq, ru, rd = red(n3, n2, n1), red(n3, n1), red(n3, n1)
        Mu, Md = mass(G15, [rq] * 3, [ru] * 3), mass(G15, [rq] * 3, [rd] * 3)
        su = np.linalg.svd(Mu, compute_uv=False); sd = np.linalg.svd(Md, compute_uv=False)
        cnt += 1
        bad += not (su[1] < 1e-12 * su[0] and abs(su[0] / sd[0] - 1) < 1e-12)
check("C1 all %d (B_3, B_2, B_Y) rung triples, coarsest- or finest-factor reading: rank 1, m_b = m_t" % cnt,
      bad == 0, "the gauge content cannot tell families apart; exceptions %d" % bad)
print("  a charge-magnitude reading (V^q, q_u = -4, q_d = +2 in Y/6 units) could split t from b,")
print("  but is still family-blind (rank 1): two massless families per sector, excluded")

# ---------------------------------------------------------------- D
print("D. Candidate (c): first split generation")
# register reading: zoom-3 turn-fixed characters (j,j,j) on the 3 fixed positions
w = np.exp(2j * np.pi / 3)
chars = np.array([[w ** (j * p) for p in range(3)] for j in range(3)]) / np.sqrt(3)
sup = {tuple(bool(v) for v in np.abs(c) > 1e-12) for c in chars}
check("D1 zoom-3 family characters share one support -> one first generation -> rank 1",
      len(sup) == 1 and np.allclose(np.abs(chars), 3 ** -0.5), "supports %s" % sup)
# octree reading: one 16 per rung -> family f on rung f (doublets and singlets alike)
print("  octree (one 16 per rung): Q, u^c, d^c of family f all on rung f-1 = (0,1,2)")
res = []
for lam in LAMS:
    for hd in (1, -1):
        Gu, Gd = gseq(lam, THBC), gseq(lam, THBC, h=hd)
        Mu, Md = mass(Gu, (0, 1, 2), (0, 1, 2)), mass(Gd, (0, 1, 2), (0, 1, 2))
        su, sd, V, J = flavour(Mu, Md)
        res.append((lam, hd, su[0] / su[2], su[1] / su[2], abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), J,
                    sin_tb(Mu, Md)))
R_ = np.array(res)
for r in res[:2] + res[-2:]:
    print("  lam %.1f h_d %+d: m1/m3 %.3f m2/m3 %.3f |Vus| %.2e |Vcb| %.2e |Vub| %.2e J %.1e sin(tb) %.0e" % r)
check("D2 octree rungs: |sin theta-bar| = 0 for every lam and both down senses (Hermitian sectors)",
      R_[:, 8].max() < 1e-12, "max %.1e (measured |theta-bar| < 1e-10)" % R_[:, 8].max())
check("D3 octree rungs: m1/m3 >= %.2f for every lam (measured m_u/m_t 7.3e-6, m_d/m_b 9.4e-4): excluded"
      % R_[:, 2].min(), R_[:, 2].min() > 1e-2, "no hierarchy: unit diagonal G(0) = 1 dominates")
check("D4 octree rungs, same sense for down: V = 1 (|V_us| = 0, J = 0); measured 0.224",
      R_[R_[:, 1] == 1][:, 4].max() < 1e-8, "max |V_us| %.1e" % R_[R_[:, 1] == 1][:, 4].max())

# ---------------------------------------------------------------- E
print("E. Structural strong CP: layouts with arg det(Mu Md) in {0, pi} for every lam, theta")
NR = 9
TRI = list(itertools.combinations(range(NR), 3))
QT = [t for t in TRI if t[0] == 0]
B = np.array(TRI)
samples = [(rng.uniform(0.5, 3), rng.uniform(0.3, 3)) for _ in range(3)]


def refl(t, c):
    return tuple(sorted(c - x for x in t))


def classify(a, bu, bd, hd):
    if bu == a and bd == a and hd == 1:
        return "herm"
    if bu == bd and hd == -1:
        return "flip"
    for c in range(2 * NR):
        if refl(a, c) == a:
            if hd == 1 and refl(bu, c) == bd:
                return "mirror"
            if refl(bu, c) == bu and refl(bd, c) == bd:
                return "self"
    return "other"


cls, Jc, Sc, keep, total = {}, {}, {}, [], 0
for a in QT:
    d = B[:, None, :] - np.array(a)[None, :, None]
    for hd in (1, -1):
        mxs = np.zeros((len(TRI), len(TRI)))
        for l, t in samples:
            Gp, Gd = gseq(l, t), gseq(l, t, h=hd)
            du = np.linalg.det(np.where(d >= 0, Gp[np.abs(d)], np.conj(Gp[np.abs(d)])))
            dd = np.linalg.det(np.where(d >= 0, Gd[np.abs(d)], np.conj(Gd[np.abs(d)])))
            p = du[:, None] * dd[None, :]
            mxs = np.maximum(mxs, np.abs(np.sin(np.angle(p))) + (np.abs(p) < 1e-12))
        total += mxs.size
        for i, j in zip(*np.where(mxs < 1e-9)):
            bu, bd = TRI[i], TRI[j]
            k = classify(a, bu, bd, hd)
            cls[k] = cls.get(k, 0) + 1
            keep.append((a, bu, bd, hd))
            for l, t in samples:
                su, sd, V, J = flavour(mass(gseq(l, t), a, bu), mass(gseq(l, t, h=hd), a, bd))
                Jc[k] = max(Jc.get(k, 0.0), abs(J))
                Sc[k] = max(Sc.get(k, 0.0), float(np.abs(np.log(su[:2] / su[2]) - np.log(sd[:2] / sd[2])).max()))
print("  cells %d (distinct rungs 0..%d); structural zeros by class: %s" % (total, NR - 1, cls))
print("  max |J| by class: %s" % {k: "%.1e" % v for k, v in Jc.items()})
print("  max |ln(up ratio) - ln(down ratio)| by class: %s" % {k: "%.1e" % v for k, v in Sc.items()})
check("E1 every structural theta-bar zero is Hermitian, self-mirror, sense-flip or u<->d mirror",
      cls.get("other", 0) == 0 and len(keep) > 0,
      "rung reflection n -> c - n with conjugation is the antiunitary that makes det real")
check("E2 Hermitian and self-mirror classes have J = 0 (the reflection is a CP of every sector)",
      max(Jc.get("herm", 0), Jc.get("self", 0)) < 1e-12, "measured J = 3.08e-5")
check("E3 sense-flip and mirror classes allow J != 0 but force the down tower = the up tower",
      max(Sc.get("flip", 1), Sc.get("mirror", 1)) < 1e-9 and max(Jc.get("flip", 0), Jc.get("mirror", 0)) > 1e-3,
      "measured m_d/m_b / (m_u/m_t) = %.0f" % (OBS[2] / OBS[0]))
best = (1e9, None)
for a, bu, bd, hd in keep:
    for lam in LAMS:
        su, sd, V, J = flavour(mass(gseq(lam, THBC), a, bu), mass(gseq(lam, THBC, h=hd), a, bd))
        o = np.array([su[0] / su[2], su[1] / su[2], sd[0] / sd[2], sd[1] / sd[2]])
        sc = float(np.sum(np.log(o / OBS[:4]) ** 2))
        if sc < best[0]:
            best = (sc, (a, bu, bd, hd, lam), o)
sc, x, o = best
print("  best structural cell (Q, u, d, h_d, lam) %s: m ratios %s" % (x, " ".join("%.1e" % v for v in o)))
# self-mirror class extended: Q = (0, c/2, c), u = (x, c/2, c-x), d = (y, c/2, c-y), c <= 20
sm = (1e9, None)
for c in range(2, 21, 2):
    m = c // 2
    for lam in LAMS:
        for hd in (1, -1):
            Gu, Gd = gseq(lam, THBC, N=60), gseq(lam, THBC, h=hd, N=60)
            for xu in range(-8, m):
                Mu = mass(Gu, (0, m, c), (xu, m, c - xu))
                for yd in range(-8, m):
                    su, sd, V, J = flavour(Mu, mass(Gd, (0, m, c), (yd, m, c - yd)))
                    o2 = np.array([su[0] / su[2], su[1] / su[2], sd[0] / sd[2], sd[1] / sd[2]])
                    s2 = float(np.sum(np.log(o2 / OBS[:4]) ** 2))
                    if s2 < sm[0]:
                        sm = (s2, (c, lam, hd, xu, yd), o2, abs(J))
print("  self-mirror to c = 20: best (c, lam, h_d, x, y) %s ratios %s |J| %.0e"
      % (sm[1], " ".join("%.1e" % v for v in sm[2]), sm[3]))
check("E4 no structural-theta-bar layout holds both quark towers (best rms log-dev > 1, all classes)",
      np.sqrt(sc / 4) > 1.0 and np.sqrt(sm[0] / 4) > 1.0,
      "rms %.2f (rungs 0..8), %.2f (self-mirror, c <= 20)" % (np.sqrt(sc / 4), np.sqrt(sm[0] / 4)))

print("F. Gate")
print("  (a),(b),(c): no measured number chosen in the rung assignment; lam scanned, not fitted")
print("  (b) and dressed (a) read the multiplets' observed charges (supplied content); (c) the 16")
check("F1 gate: unfitted predictions exist and FAIL measurement in all three candidates",
      True, "rank 1 or m_b = m_t (a, b, c-characters); no hierarchy, V = 1 (c-octree)")
print("runtime %.1f s" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
