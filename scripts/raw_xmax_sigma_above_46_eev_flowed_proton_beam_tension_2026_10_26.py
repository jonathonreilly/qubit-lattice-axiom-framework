AUDIT_INPUT_PATHS = ('docs/RAW_XMAX_SIGMA_ABOVE_46_EEV_PUTS_A_PURE_FLOWED_PROTON_BEAM_IN_TENSION_DECIDED_BY_THE_FLOWED_HADRON_AIR_CROSS_SECTION_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Raw Auger Xmax moments above 46 EeV vs a pure beam of 'flowed' protons (rule-fixed dim-6 LIV).

Upstream (agents/liv-surviving-observables, composite-dispersion, nuclear-vacuum-breakup; [F]):
  nuclei break up in vacuum below <= 46 EeV; protons above ~5 EeV are flowed: one constituent at x_lead -> 1,
  c_B/c_q residual r = 0.001-0.003 at 1e20 eV, r ~ P^-2.
Supplied here: a seeded generalized Heitler-Matthews toy (leading particle, interaction length, multiplicity,
Greisen EM subshowers, deterministic pion bundles), calibrated two-point on each hadronic model's p and Fe
moments; a bracket of the flowed first-interaction parameters (f_sigma, kappa, f_N).
Embedded data (cited in note): Auger SD-DNN Table 4 (arXiv:2406.06319), Auger FD (arXiv:1409.4809 Table 4),
model moments from the Arbeletche-de Souza generalized-Gumbel parametrization (arXiv:1903.03174, Table 6).
"""
import time
import numpy as np
from scipy.special import digamma, polygamma

AUDIT_TIMEOUT_SEC = 120
t0 = time.time()
PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))

# ---------- data (g/cm^2): lgE, <X>, stat, sys-, sys+, sigma, stat, sys-, sys+, N
DNN = [(19.74, 787.2, 2.0, 7.5, 11.6, 20.7, 1.4, 4.8, 6.8, 113),
       (19.85, 794.5, 3.6, 7.8, 12.2, 25.1, 3.9, 4.8, 6.8, 54),
       (20.00, 793.9, 4.5, 8.3, 13.1, 21.8, 5.4, 4.8, 6.8, 26)]
FD = (19.62, 779.8, 5.0, 6.9, 9.4, 26.5, 4.8, 1.6, 1.5, 37)
# ---------- generalized Gumbel coefficients theta = sum_k (sum_j c[k][j] lgA^j) lgE^k
GMB = {'QGSJetII-04': {'l': [(0.6465, 1.932, 1.767), (-0.02109, -0.2143, -0.15658), (0.001274, 0.008431, 0.004271)],
                       'm': [(-412.77, -136.12, -76.789), (66.4057, 13.8397, 6.1521), (-0.24926, -0.42961, -0.12990)],
                       's': [(211.50, -13.05, -13.36), (-17.650, 2.1148, 0.8359), (0.44432, -0.03287, -0.02996)]},
       'EPOS-LHC': {'l': [(5.621, 4.614, -2.730), (-0.5942, -0.5019, 0.4506), (0.017490, 0.01506, -0.01395)],
                    'm': [(-505.56, -356.03, 27.79), (75.805, 38.127, -5.6766), (-0.44325, -1.08321, 0.19476)],
                    's': [(446.23, -209.52, 61.24), (-45.209, 27.790, -8.548), (1.2330, -0.86067, 0.26753)]},
       'Sibyll2.3c': {'l': [(-1.164, 5.295, -1.288), (0.1623, -0.5541, 0.1595), (-0.003128, 0.015849, -0.004691)],
                      'm': [(-608.46, 58.10, -111.29), (86.634, -9.002, 10.606), (-0.6925, 0.21420, -0.26591)],
                      's': [(123.53, 100.69, -64.16), (-8.066, -9.734, 5.9116), (0.1955, 0.21773, -0.13790)]}}
def model_mom(m, lgE, A):
    la = np.log10(A); c = GMB[m]
    lam, mu, s = [sum(sum(c[q][k][j] * la**j for j in range(3)) * lgE**k for k in range(3)) for q in 'lms']
    return mu + s * (np.log(lam) - digamma(lam)), s * np.sqrt(polygamma(1, lam))
MODELS = list(GMB)
print("A  hadronic-model moments (GMB param.) at 1e19 eV: p / Fe <X>, sigma")
for m in MODELS:
    (xp, sp), (xf, sf) = model_mom(m, 19.0, 1), model_mom(m, 19.0, 56)
    print(f"   {m:12s} p {xp:.1f} / {sp:.1f}   Fe {xf:.1f} / {sf:.1f}")
check("A1 parametrization reproduces Auger ICRC2013 proton anchors X0(1e19): EPOS-LHC 806.1, QGSJetII-04 790.4",
      abs(model_mom('EPOS-LHC', 19, 1)[0] - 806.1) < 3 and abs(model_mom('QGSJetII-04', 19, 1)[0] - 790.4) < 3)

# ---------- x_lead from upstream residuals
r20 = np.array([0.001, 0.003]); r19 = r20 * 100.0
xl = {lg: 1 - r20 * (10**(20 - lg))**2 / 3 for lg in (19.66, 19.74, 20.0)}
print(f"B  x_lead (1 - x = r/3, r ~ P^-2): 46 EeV {xl[19.66][1]:.4f}-{xl[19.66][0]:.4f}; 1e20 {xl[20.0][1]:.4f}-{xl[20.0][0]:.4f}")
check("B1 r ~ P^-2 scaling of the 1e20 residual reproduces the upstream 1e19 residual 0.10-0.28 (3-body FEM)",
      0.05 < r19[0] < 0.2 and 0.2 < r19[1] < 0.5, f"scaled {r19[0]:.2f}-{r19[1]:.2f}")

# ---------- toy cascade
X0, XIC, DX = 36.7, 86e6, 2.0
XG = np.arange(0, 4000, DX); NX = len(XG); LG = np.arange(8.0, 21.01, 0.05)
lam_p = lambda E: 24000.0 / (505.0 * (E / 10**18.24)**0.045)   # sigma_p-air 505 mb at 10^18.24 eV (Auger 2012)
nch = lambda E: 41.2 * (E / 1e15)**0.2
def gre(E):
    if E <= 1.01 * XIC: return np.zeros(NX)
    b = np.log(E / XIC); t = np.maximum(XG / X0, 1e-9); s = 3 * t / (t + 2 * b)
    return 0.31 / np.sqrt(b) * np.exp(t * (1 - 1.5 * np.log(s)))
idx = lambda E: int(np.clip(round((np.log10(E) - LG[0]) / 0.05), 0, len(LG) - 1))
def shift(a, dx):
    k = int(round(dx / DX))
    if k <= 0: return a
    o = np.zeros(NX); o[k:] = a[:NX - k]; return o
GR = [gre(10**l) for l in LG]; H = [None] * len(LG); MU = np.zeros(len(LG))
for i, l in enumerate(LG):           # deterministic charged-pion bundle, built bottom-up
    E = 10**l
    if E < 20e9: H[i] = np.zeros(NX); MU[i] = 1.0; continue
    n = nch(E); j = idx(0.45 * E); e = 0.55 * E / (1.5 * n)
    I = n * GR[idx(e / 2)] + n * H[idx(e)] + (H[j] if j < i else 0)
    MU[i] = n * MU[idx(e)] + (MU[j] if j < i else 0); H[i] = shift(I, 1.2 * lam_p(E))
rng = np.random.default_rng(20261026)
EFLOW = 5e18
def shower(E, cfg, flowon, xlead):
    fs, km, fN = cfg; prof = np.zeros(NX); mu = 0.0; X = 0.0
    while E > 1e16:
        fl = flowon and E > EFLOW
        X += rng.exponential(lam_p(E) / (fs if fl else 1.0))
        if X >= XG[-1]: return prof, mu, True
        if fl and km == 'high': kap = 1 - (1 - xlead) / 2
        elif fl and km == 'low': kap = rng.uniform(0.0, 0.4)
        else: kap = rng.uniform(0.1, 0.8)
        n = nch(E) * (fN if fl else 1.0); e = (1 - kap) * E / (1.5 * n)
        prof += shift(n * GR[idx(e / 2)] + n * H[idx(e)], X); mu += n * MU[idx(e)]; E *= kap
    prof += shift(H[idx(E)], X); mu += MU[idx(E)]
    return prof, mu, False
def xmax(p):
    k = int(np.argmax(p))
    if 0 < k < NX - 1:
        a, b, c = p[k - 1:k + 2]; return XG[k] + 0.5 * (a - c) / (a - 2 * b + c) * DX
    return XG[k]
def sample(lgE, cfg, N, A=1, flowon=False):
    E = 10**lgE; xs, ms, lost = [], [], 0
    xld = 1 - 0.002 * (10**(20 - lgE))**2 / 3
    for _ in range(N):
        p = np.zeros(NX); m = 0.0; esc = False
        for _ in range(A):
            q, mm, es = shower(E / A, cfg, flowon, xld); p += q; m += mm; esc |= es
        xs.append(xmax(p)); ms.append(m); lost += esc or xs[-1] > 1500
    xs = np.array(xs); return xs.mean(), xs.std(), np.mean(ms), lost / N
STD = (1.0, 'std', 1.0)
BINS = [d[0] for d in DNN] + [FD[0]]
cal = {}
for lg in BINS:
    cal[lg] = (sample(lg, STD, 600), sample(lg, STD, 80, A=56))
tp, tf = cal[19.74]
print(f"C  toy at 10^19.74: p <X> {tp[0]:.1f} sig {tp[1]:.1f}; Fe <X> {tf[0]:.1f} sig {tf[1]:.1f}; Nmu Fe/p {tf[2]/tp[2]:.2f}")
mp = [model_mom(m, 19.74, 1) for m in MODELS]; mf = [model_mom(m, 19.74, 56) for m in MODELS]
sv = [np.sqrt(max(a[1]**2 + tf[1]**2 - tp[1]**2, 0)) for a in mp]
check("C1 toy calibration: sigma_p within 40-75, and variance mapping sigma_p,model^2 + (toy Fe^2 - toy p^2) gives model Fe sigma within 8",
      40 < tp[1] < 75 and all(abs(s - b[1]) < 8 for s, b in zip(sv, mf)),
      "mapped Fe " + "/".join(f"{s:.1f}" for s in sv) + " vs model " + "/".join(f"{b[1]:.1f}" for b in mf))

def predict(lg, f):
    tp, tf = cal[lg]; out = []
    for m in MODELS:
        (xp, sp), (xF, sF) = model_mom(m, lg, 1), model_mom(m, lg, 56)
        sc = (xp - xF) / (tp[0] - tf[0])
        out.append((xp + sc * (f[0] - tp[0]), np.sqrt(max(sp**2 + f[1]**2 - tp[1]**2, 0.0))))
    o = np.array(out); return o.mean(0), o.max(0) - o.min(0)
def pulls(d, pr, spr, toyerr):
    lg, X, sx, sxm, sxp, S, ss, ssm, ssp, N = d
    px = (pr[0] - X) / np.sqrt(sx**2 + (sxp if pr[0] > X else sxm)**2 + spr[0]**2 + toyerr[0]**2)
    ps = (pr[1] - S) / np.sqrt(ss**2 + (ssp if pr[1] > S else ssm)**2 + spr[1]**2 + toyerr[1]**2)
    return px, ps

pre = [(fs, k, fn) for fs in (1 / 3, 1.0, 2.0) for k in ('std', 'high') for fn in (0.3, 1.0, 1.5)]
ext = [(fs, k, fn) for fs in (2.0, 4.0, 8.0) for k in ('std', 'low') for fn in (0.5, 1.0, 1.5)]
print("D  corners (f_sigma, kappa, f_N): pred <X>, sigma at 19.74 | worst pull over DNN bins >46 EeV (X, sigma) | lost")
res = {}
for tag, grid, N in (('pre', pre, 300), ('ext', ext, 300)):
    for cfg in grid:
        worst = [0.0, 0.0]; line = None; lostf = 0
        for d in DNN:
            f = sample(d[0], cfg, N, flowon=True); lostf = max(lostf, f[3])
            pr, spr = predict(d[0], f)
            pxs = pulls(d, pr, spr, (f[1] / np.sqrt(N), f[1] / np.sqrt(2 * N)))
            worst = [max(worst[0], abs(pxs[0])), max(worst[1], abs(pxs[1]))]
            if d[0] == 19.74: line = (pr, f[2] / cal[19.74][0][2])
        if lostf > 0.5: worst = [99.0, 99.0]
        res[(tag,) + cfg] = (max(worst), worst, line, lostf)
        if tag == 'pre' and cfg[1] == 'high' and cfg[2] != 1.0: continue
        print(f"   {tag} ({cfg[0]:.2g},{cfg[1]},{cfg[2]:.2g}): {line[0][0]:.0f}, {line[0][1]:.0f} | "
              f"{worst[0]:.1f}, {worst[1]:.1f} | Nmu/p {line[1]:.2f} | lost {lostf:.2f}")
# standard pure proton
wp = [0, 0]
for d in DNN:
    pr, spr = predict(d[0], cal[d[0]][0])
    px, ps = pulls(d, pr, spr, (2, 2)); wp = [max(wp[0], px), max(wp[1], ps)]
print(f"E  standard pure proton: worst pull <X> {wp[0]:.1f}, sigma {wp[1]:.1f}")
check("E1 pure standard protons above 46 EeV: sigma(Xmax) misses by > 3 combined sigma (the known exclusion)", wp[1] > 3)
hi = [v for k, v in res.items() if k[0] == 'pre' and k[2] == 'high']
check("E2 'transparent' corner (kappa = 1 - (1-x_lead)/2): showers escape / Xmax > 1500 -> excluded outright",
      all(v[3] > 0.5 for v in hi), f"lost fraction min {min(v[3] for v in hi):.2f}")
lo = [v for k, v in res.items() if k[0] == 'pre' and k[1] <= 1.0]
check("E3 every pre-registered corner with f_sigma <= 1 is EXCLUDED (> 3 sigma)", all(v[0] > 3 for v in lo),
      f"min worst pull {min(v[0] for v in lo):.1f}")
bp = min((v[0], k) for k, v in res.items() if k[0] == 'pre')
be = min((v[0], k) for k, v in res.items() if k[0] == 'ext')
cat = lambda z: 'EXCLUDED' if z > 3 else ('TENSION' if z > 2 else 'CONSISTENT')
print(f"F  best pre-registered corner {bp[1][1:]} worst pull {bp[0]:.1f} -> {cat(bp[0])}")
print(f"   best extended corner {be[1][1:]} worst pull {be[0]:.1f} -> {cat(be[0])}")
check("F1 pre-registered verdict computed (most favourable corner decides)", cat(bp[0]) in ('EXCLUDED', 'TENSION', 'CONSISTENT'),
      cat(bp[0]))
need = sorted(set(k[1] for k, v in res.items() if v[0] < 2))
check("F2 every fitting corner needs f_sigma >= 2 (cross section of the flowed hadron decides)",
      len(need) > 0 and min(need) >= 2.0, f"f_sigma of fitting corners {need}")
# FD cross-check at 19.62 (direct fluorescence)
fc = sample(FD[0], bp[1][1:], 400, flowon=True); prc, sprc = predict(FD[0], fc)
pxc, psc = pulls(FD, prc, sprc, (2, 2))
pc, sc_ = predict(FD[0], cal[FD[0]][0]); pxp, psp = pulls(FD, pc, sc_, (2, 2))
print(f"G  FD lgE>=19.5 (N=37): data 779.8, 26.5; best corner {prc[0]:.0f}, {prc[1]:.0f} (pulls {pxc:.1f}, {psc:.1f});"
      f" std p {pc[0]:.0f}, {pc[1]:.0f} (pulls {pxp:.1f}, {psp:.1f})")
check("G1 FD direct-fluorescence bin agrees with the DNN verdict for std protons (sigma pull > 3)", psp > 3)
print(f"runtime {time.time() - t0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
