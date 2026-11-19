#!/usr/bin/env python3
"""slab-thickness-scale (R2): can one integer Ls (with m, xi) set v/M_P, v' and the fermion hierarchy?

Supplied: M_P, v, v' window, m_nu bound, M_Z running masses (Xing-Zhang-Zhou 2011), Wilson slab of chiral-tick-form.
Criteria fixed in criteria_pre_run.txt before this runner was written. Seeded; numpy only.
"""
import math
import numpy as np

AUDIT_TIMEOUT_SEC = 120
SEED = 20261024
rng = np.random.default_rng(SEED)
PASS = 0
FAIL = 0


def check(name, ok, info=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))


# ---------- supplied numbers ----------
M_P = 1.22e19          # GeV, cutoff a = l_P (supplied)
V_EW = 246.0           # GeV
VP_LO, VP_HI = 1e8, 1e11   # face-swap-parity window (supplied bounds)
MNU = 0.45e-9          # GeV, KATRIN direct bound (supplied)
MASS = {  # GeV at M_Z, Xing-Zhang-Zhou 2011 (supplied)
    "e": (0.486570e-3, 0.1027181, 1.74624),
    "u": (1.38e-3, 0.638, 172.1),
    "d": (2.82e-3, 0.057, 2.86),
}

# ---------- 0. the slab overlap |1-m|^Ls (rederived numerically at k = 0) ----------
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]])
s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2)
G4 = np.kron(s2, I2)
G5 = np.kron(s3, I2)
A = (G5 + 1j * G4) / 2


def slab_k0(m, Ls):
    H = np.zeros((4 * Ls, 4 * Ls), complex)
    for s in range(Ls):
        H[4 * s:4 * s + 4, 4 * s:4 * s + 4] = (m - 1.0) * G5  # sum_i cos(0) G5 + (m-4) G5
    for s in range(Ls - 1):
        H[4 * (s + 1):4 * (s + 2), 4 * s:4 * s + 4] = A
        H[4 * s:4 * s + 4, 4 * (s + 1):4 * (s + 2)] = A.conj().T
    return H


print("== 0. slab overlap (Wilson slab, k = 0) ==")
for m in (0.6, 1.0):
    gaps = []
    for Ls in (6, 8, 10, 12):
        ev = np.sort(np.abs(np.linalg.eigvalsh(slab_k0(m, Ls))))
        gaps.append(ev[0])
    if m == 1.0:
        check("m=1 compact wall: zero-mode splitting exactly 0", max(gaps) < 1e-12, "max %.1e" % max(gaps))
    else:
        ratio = (gaps[-1] / gaps[-2]) ** 0.5
        check("m=0.6 splitting ratio per layer = |1-m| = 0.4", abs(ratio - 0.4) < 4e-3, "ratio %.4f" % ratio)
xi = 1 / math.log(1 / 0.4)
print("  xi(m=0.6) = %.3f layers; only rule-distinguished point m = 1 (window centre) gives xi = 0" % xi)

# ---------- Q1. electroweak / Planck ----------
print("== Q1. v/M_P from the overlap ==")
target = V_EW / M_P
Lneed = -math.log(target)
Ls06 = Lneed / math.log(1 / 0.4)
print("  v/M_P = %.2e, Ls/xi needed = %.2f, Ls at m=0.6 = %.2f" % (target, Lneed, Ls06))
# degeneracy: for every integer Ls there is an m in (0,2) with |1-m|^Ls = v/M_P exactly
ms = [1 - target ** (1.0 / L) for L in (10, 20, 42, 80)]
check("m-Ls degeneracy: each Ls in {10,20,42,80} has an exact m in (0,2)", all(0 < x < 2 for x in ms),
      "m = " + ", ".join("%.3f" % x for x in ms))
m_free = True  # chiral-tick-form: 'm and th are free inside the gapped window'
q1 = "FIT (m free; one number, one effective real)" if m_free else "candidate prediction"
# residual-mass consistency
mres = M_P * target
Lnu = -math.log(MNU / M_P)
check("residual mass if overlap = v/M_P equals v (computed)", abs(mres - V_EW) < 1e-9, "m_res = %.0f GeV" % mres)
ok_ident = mres < MNU
print("  m_nu bound needs Ls/xi >= %.1f; v needs Ls/xi = %.1f -> identification %s" %
      (Lnu, Lneed, "consistent" if ok_ident else "INCONSISTENT (light-mirror Dirac mass ~ v)"))
pmax = Lneed / Lnu
print("  any v/M_P = overlap^p must have p <= %.3f (power chosen, not forced)" % pmax)
check("Q1 verdict logic applied", True, q1 + "; overlap = v/M_P " + ("OK" if ok_ident else "EXCLUDED"))

# ---------- Q2. mirror scale ----------
print("== Q2. v' = M_P (v/M_P)^r ==")
r_lo = math.log(VP_HI / M_P) / math.log(target)
r_hi = math.log(VP_LO / M_P) / math.log(target)
vp_half = math.sqrt(V_EW * M_P)
print("  window -> r in [%.3f, %.3f]; r = 1/2 gives v' = %.2e GeV" % (r_lo, r_hi, vp_half))
p_log = (math.log(VP_HI) - math.log(VP_LO)) / (math.log(M_P) - math.log(V_EW))
rats = sorted({(p // math.gcd(p, q), q // math.gcd(p, q)) for q in range(2, 7) for p in range(1, q)})
inwin = [f"{p}/{q}" for p, q in rats if r_lo <= p / q <= r_hi]
f_rat = len(inwin) / len(rats)
print("  log-uniform chance %.3f; rationals q<=6 in window: %s (%d/%d = %.3f)" %
      (p_log, ",".join(inwin), len(inwin), len(rats), f_rat))
r_forced = False  # no rule found that forces r = 1/2 (a mid-slab channel is a choice)
q2 = "PREDICTION" if (r_forced and p_log < 0.05 and f_rat < 0.05) else "COINCIDENCE LEVEL (two parameters)"
check("r=1/2 lands in the window (computed)", VP_LO <= vp_half <= VP_HI)
check("Q2 verdict logic applied", True, q2)

# ---------- Q3. fermion hierarchy, integer depths, one base ----------
print("== Q3. integer depths, one base b ==")
x = []
for k in ("e", "u", "d"):
    m1, m2, m3 = MASS[k]
    x += [math.log(m3 / m1), math.log(m3 / m2)]
x = np.array(x)
print("  targets ln(m3/m1), ln(m3/m2): " + " ".join("%.2f" % t for t in x))
Lmin, Lmax = x.max() / 42.0, 3.0
Lg = np.exp(np.linspace(math.log(Lmin), math.log(Lmax), 6000))


def stat_scan(X):  # X: (n, 6) -> min over L of mean frac distance, argmin L
    out = np.empty(X.shape[0])
    arg = np.empty(X.shape[0])
    for i0 in range(0, X.shape[0], 100):
        Z = X[i0:i0 + 100, None, :] / Lg[None, :, None]
        S = np.abs(Z - np.round(Z)).mean(axis=2)
        out[i0:i0 + 100] = S.min(axis=1)
        arg[i0:i0 + 100] = Lg[S.argmin(axis=1)]
    return out, arg


def stat_fixed(X, Ls_list):
    best = np.full(X.shape[0], np.inf)
    for L in Ls_list:
        Z = X / L
        best = np.minimum(best, np.abs(Z - np.round(Z)).mean(axis=1))
    return best


S_obs, L_obs = stat_scan(x[None, :])
S_obs, L_obs = S_obs[0], L_obs[0]
d_obs = np.round(x / L_obs).astype(int)
N = 4000
Xj = x[None, :] * rng.uniform(0.5, 1.5, size=(N, 6))
Xu = rng.uniform(0.5, 12.0, size=(N, 6))
Sj, _ = stat_scan(Xj)
Su, _ = stat_scan(Xu)
p_j = (np.sum(Sj <= S_obs) + 1) / (N + 1)
p_u = (np.sum(Su <= S_obs) + 1) / (N + 1)
print("  scanned: min S = %.3f at b = %.3f (depth diffs %s); null median S %.3f" %
      (S_obs, math.exp(-L_obs), d_obs.tolist(), np.median(Sj)))
print("  p(jitter null) = %.3f, p(uniform null) = %.3f" % (p_j, p_u))
check("scan null computed (N=4000, seeded)", np.isfinite(p_j) and np.isfinite(p_u))
L04 = math.log(1 / 0.4)
S04 = stat_fixed(x[None, :], [L04])[0]
p04 = (np.sum(stat_fixed(Xj, [L04]) <= S04) + 1) / (N + 1)
Lc = [c * L04 for c in (1, 2, 3, 4)]
Sc = stat_fixed(x[None, :], Lc)[0]
pc = (np.sum(stat_fixed(Xj, Lc) <= Sc) + 1) / (N + 1)
print("  fixed b=0.4: S = %.3f, depths %s, p = %.3f" % (S04, np.round(x / L04).astype(int).tolist(), p04))
print("  b=0.4^c, c=1..4: S = %.3f, p = %.3f" % (Sc, pc))
q3 = "COMPRESSES" if min(p_j, p04, pc) < 0.01 else "FIT ONLY"
check("Q3 verdict logic applied", True, q3 + " (1 real + 6 integers + 3 norms vs 9 masses)")
# info count: integer depths cost log2(range) bits each; compare to residual precision gained
bits_int = 6 * math.log2(d_obs.max() + 1)
print("  depth codes cost ~%.0f bits; mean |ln| residual %.3f vs %.3f expected for random targets at that b" %
      (bits_int, S_obs * L_obs, 0.25 * L_obs))
# rank lemma on the Wilson slab: one-layer channel -> rank 1
b = 0.4
z = np.arange(12)
Phi = np.array([b ** np.abs(z - a) for a in (0, 2, 5)])
Chi = np.array([b ** np.abs(z - a) for a in (11, 8, 6)])
Y1 = np.outer(Phi[:, 4], Chi[:, 4])
Yf = Phi @ Chi.T
sv1 = np.linalg.svd(Y1, compute_uv=False)
svf = np.linalg.svd(Yf, compute_uv=False)
check("one-layer Higgs channel gives rank 1", sv1[1] / sv1[0] < 1e-12, "sv ratio %.1e" % (sv1[1] / sv1[0]))
print("  flat channel, CHOSEN positions (0,2,5)/(11,8,6): sv %s" % " ".join("%.1e" % s for s in svf))

# ---------- Q4. forced depths d_k = k*Delta ----------
print("== Q4. forced equal spacing ==")
g = {k: MASS[k][1] ** 2 / (MASS[k][0] * MASS[k][2]) for k in MASS}
print("  m2^2/(m1 m3): " + ", ".join("%s %.2f" % (k, g[k]) for k in g))
r31 = [math.log(MASS[k][2] / MASS[k][0]) for k in MASS]
print("  ln(m3/m1) per sector (must be equal): " + " ".join("%.2f" % t for t in r31))
q4ok = all(0.5 <= g[k] <= 2.0 for k in g)
check("Q4 verdict logic applied", True, "equal spacing " + ("PASSES" if q4ok else "FALSIFIED"))

overall = "COMPRESSES" if q3 == "COMPRESSES" else ("FAILS" if (not ok_ident or not q4ok) else "FIT ONLY")
print("VERDICT: Q1 %s | Q2 %s | Q3 %s | Q4 %s -> %s (forced versions fail; free versions are fits)" %
      ("FIT" if m_free else "PRED", "COINC", q3, "FALSIFIED" if not q4ok else "OK",
       "FIT ONLY / FAILS-when-forced" if overall == "FAILS" else overall))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
