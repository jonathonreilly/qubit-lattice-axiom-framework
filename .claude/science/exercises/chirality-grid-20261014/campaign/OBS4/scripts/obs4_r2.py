"""OBS-4 C3 + R1b + R3 + R4 numbers:
 C3  normalisation cross-checks: INP/UTfit C4 rows -> HKZ 1209.1397 Table 2 Yukawa rows at m_h = 125 GeV;
     own direct bag-parameter computation (FLAG 2024 B4^K, LO running) of the same rows.
 R1b own direct dm_K, eps_K, dm_Bd, dm_Bs, dm_D for B-gen/B-gen120 (D3, equal vevs) -> M*_direct vs M*_INP.
 R1c cancellation (tuning) measure at the vev-optimised point.
 R3  H/A split robustness against UTfit 0707.0636 Table 4 C2 and C4 rows.
 R4  h-alignment requirement (125 GeV h with a small heavy-direction admixture eps) against HKZ rows;
     carrier-mass ceiling of the Z2xZ2 potential (tree level, perturbative)."""
import numpy as np
from scipy.optimize import brentq
from obs4_core import *
from obs4_r1 import realisations, physical, vev_dicts, minimise, worst
P = lambda *a: print(*a, flush=True)

# ---------------- C3
P("C3. normalisation cross-checks at m_h = 125 GeV (real scalar, L = -Y_ij qbar_L^i q_R^j h + h.c.; C4 = -Y_ij Y_ji^*/m_h^2)")
mh = 125.0
UT4 = {'K_Re': 3.6e-15, 'K_Im': 1.8e-17, 'D': 4.8e-14, 'Bd': 2.1e-13, 'Bs': 1.6e-11}   # UTfit 0707.0636 Tab.4 |C4| (GeV^-2; K_Im: larger side)
HKZ = {'K_Re': 5.6e-11, 'K_Im': 2.8e-13, 'D': 7.5e-10, 'Bd': 3.3e-9, 'Bs': 2.5e-7}      # HKZ Table 2 |Y_ij Y_ji| rows (K: max |side|)
INPL = {'K_Re': 1.8e4, 'K_Im': 3.2e5, 'D': 6.2e3, 'Bd': 1.9e3, 'Bs': 3.7e2}           # INP Table 1 LR rows (Re rows for D, Bd)
for k in HKZ:
    ut = UT4[k] * mh**2; inp = mh**2 / (INPL[k] * 1e3)**2
    P(f"  {k:5s}: HKZ published {HKZ[k]:.2e} | from UTfit |C4| {ut:.2e} (ratio {ut/HKZ[k]:.2f}) | from INP Lambda {inp:.2e} (ratio {inp/HKZ[k]:.2f})")
# own direct: largest |Re| / |Im| of Y_ij Y_ji^* allowed at m_h = 125 GeV
for Pm, rows in (('K', ('dmK', 'epsK')), ('D', ('dmD', 'phiD')), ('Bd', ('dmBd',)), ('Bs', ('dmBs',))):
    for r in rows:
        unit = {'dmK': 1.0, 'epsK': 1j, 'dmD': 1.0, 'phiD': 1j, 'dmBd': 1.0, 'dmBs': 1.0}[r]
        val = direct_ratios(unit / mh**2, Pm, mh)[r]
        P(f"  own direct ({Pm}, {r}): allowed |{'Im' if unit == 1j else 'Re'} Y Y*| at 125 GeV = {1/val:.2e}   (LO running factor {run_C4(mh, MESON[Pm]['mu']):.3f})")
P(f"  matrix elements <Q4> (GeV^4): " + ", ".join(f"{k} {me_Q4(k):.4e}" for k in MESON))

# ---------------- R1b / R1c / R3 / R4 on B-gen, B-gen120
R = realisations()
for name in ('B-gen(as fitted)', 'B-gen120(as fitted)'):
    Mu, Md, cj = physical(*R[name]); mb = mass_basis(Mu, Md); Pu, Pd = carrier_hats(Mu, Md, mb)
    P(f"\n=== {name}{' [conjugated]' if cj else ''}")
    for scale in (1.0, 0.5):
        vu, vd = vev_dicts('D3', np.ones(4))
        zs = {'K': pair_sum(Pd, vd, 1, 0), 'D': pair_sum(Pu, vu, 1, 0), 'Bd': pair_sum(Pd, vd, 2, 0), 'Bs': pair_sum(Pd, vd, 2, 1)}
        zs = {k: v * scale**2 for k, v in zs.items()}
        P(f"  [scale x{scale}, D3 equal vevs] sum_K Yhat_ij Yhat_ji^*: " + ", ".join(f"{k} {v:.3e}" for k, v in zs.items()))
        # direct M*: solve ratio(M) = 1 per observable
        Ms = {}
        for Pm in ('K', 'D', 'Bd', 'Bs'):
            for r, val in direct_ratios(zs[Pm] / 1.0**2, Pm, 1.0).items():
                f = lambda lM: np.log(direct_ratios(zs[Pm] / np.exp(lM)**2, Pm, np.exp(lM))[r])
                Ms[r] = np.exp(brentq(f, np.log(10.0), np.log(1e12))) / 1e3 if f(np.log(10.0)) > 0 else 0.0
        inp = mstar_rows(Pu, Pd, vu, vd, scale)
        P(f"  [scale x{scale}] M*_direct (TeV): " + ", ".join(f"{k} {v:.2e}" for k, v in Ms.items()) + f"  | M*_INP max {max(inp.values()):.2e} TeV")
        # R3: H/A split (A decoupled) against UTfit C2 and C4 rows, at M = 1 TeV: required M
        sq = {'K': ('d', 1, 0), 'D': ('u', 1, 0), 'Bd': ('d', 2, 0), 'Bs': ('d', 2, 1)}
        UT2 = {'K_Re': 1.9e-14, 'K_Im': 9.3e-17, 'D': 1.6e-13, 'Bd': 7.2e-13, 'Bs': 5.6e-11}
        out = []
        for k, (sec, i, j) in sq.items():
            Ph, vv = (Pu, vu) if sec == 'u' else (Pd, vd)
            c2a = sum(Ph[K][i, j]**2 / vv[K]**2 for K in CARRIERS) * scale**2 / 4      # (qbar_L q_R)^2 coefficient x M^2
            c2b = sum(np.conj(Ph[K][j, i])**2 / vv[K]**2 for K in CARRIERS) * scale**2 / 4
            c4 = zs[k] / 2
            for lab, c, rows in (('C2', max(abs(c2a), abs(c2b)), UT2), ('C4', abs(c4), UT4)):
                if k == 'K':
                    cc = c2a if abs(c2a) > abs(c2b) else c2b
                    cc = cc if lab == 'C2' else c4
                    out.append(f"{k}{lab}Re {np.sqrt(abs(cc.real)/rows['K_Re'])/1e3:.2e}")
                    out.append(f"{k}{lab}Im {np.sqrt(abs(cc.imag)/rows['K_Im'])/1e3:.2e}")
                else:
                    out.append(f"{k}{lab} {np.sqrt(c/rows[k])/1e3:.2e}")
        P(f"  [scale x{scale}] R3 H only (A decoupled), required M_H (TeV) vs UTfit Table 4: " + ", ".join(out))
    # R1c: tuning at the optimised-vev point (D3, scale 1)
    m, r, vu_m, vd_m, mc = minimise(Pu, Pd, 'D3', 1.0, Mu, Md, nstart=30)
    P(f"  R1c optimised D3 point: M* = {m:.2e} TeV, vevs {[round(vu_m[k], 2) for k in CARRIERS]}")
    for k, (sec, i, j) in (('K', ('d', 1, 0)), ('D', ('u', 1, 0)), ('Bd', ('d', 2, 0)), ('Bs', ('d', 2, 1))):
        Ph, vv = (Pu, vu_m) if sec == 'u' else (Pd, vd_m)
        terms = np.array([Ph[K][i, j] * np.conj(Ph[K][j, i]) / vv[K]**2 for K in CARRIERS])
        tot = terms.sum()
        P(f"    {k}: |sum| = {abs(tot):.3e}, sum|terms| = {np.abs(terms).sum():.3e}, cancellation |sum|/sum|.| = {abs(tot)/np.abs(terms).sum():.2e}; "
          f"Re/Im parts: {tot.real:+.2e} {tot.imag:+.2e}")
    # sensitivity: 1% random perturbations of the optimal vevs
    rng = np.random.default_rng(7); base = np.array([vu_m[k] for k in CARRIERS]); ms = []
    for s in range(200):
        t = base * (1 + 0.01 * rng.standard_normal(4)); ms.append(worst(Pu, Pd, 'D3', t, 1.0, Mu, Md, pen=False)[0])
    ms = np.array(ms)
    P(f"    1% vev jitter: M* median {np.median(ms):.2e} TeV, 90th pct {np.percentile(ms, 90):.2e} TeV (optimum {m:.2e})")
    # R4: h alignment. h = cos(e) H1 + sin(e) Hk, Hk = heavy Higgs-basis direction; real-h coupling = sin(e) N_k / sqrt2
    vu, vd = vev_dicts('D3', np.ones(4)); vvec = np.array([vu[K] for K in CARRIERS]) / VEV
    # heavy directions: orthonormal complement of vvec
    Q, _ = np.linalg.qr(np.column_stack([vvec, np.eye(4)[:, :3]])); heavy = [Q[:, n] * np.sign(Q[0, n] or 1) for n in range(1, 4)]
    for n, u in enumerate(heavy):
        Nu = sum(u[a] * Pu[K] / vu[K] for a, K in enumerate(CARRIERS)); Nd = sum(u[a] * Pd[K] / vd[K] for a, K in enumerate(CARRIERS))
        lim = []
        for k, (N, i, j, b) in (('K_Re', (Nd, 1, 0, HKZ['K_Re'])), ('K_Im', (Nd, 1, 0, HKZ['K_Im'])), ('D', (Nu, 1, 0, HKZ['D'])),
                                 ('Bd', (Nd, 2, 0, HKZ['Bd'])), ('Bs', (Nd, 2, 1, HKZ['Bs']))):
            z = N[i, j] * np.conj(N[j, i]) / 2
            x = abs(z.real) if k == 'K_Re' else (abs(z.imag) if k == 'K_Im' else abs(z))
            lim.append((np.sqrt(b / x) if x > 0 else np.inf, k))
        e, k = min(lim)
        P(f"  R4 h-alignment, heavy direction {n}: max misalignment sin(e) = {e:.2e} (binding row {k})")

# ---------------- R4: carrier-mass ceiling (tree level), PREREG rule 9
P("\nR4. carrier-mass ceiling of the Z2xZ2 potential (tree level)")
m_off_u = 0.3334 * MU[2]                          # B-gen up off-diagonal mass entry, GeV
for lam_y, lam4 in ((np.sqrt(4 * np.pi), 4 * np.pi), (np.sqrt(4 * np.pi), 8 * np.pi)):
    vx = m_off_u / lam_y
    prod = ((VEV**2 - vx**2) / 3) ** 1.5
    Mx = np.sqrt(lam4 * prod / vx)
    P(f"  Yukawa <= {lam_y:.2f}, quartic <= {lam4:.1f}: seesaw carrier v_x >= {vx:.1f} GeV, M_x <= {Mx/1e3:.2f} TeV; "
      f"others ~ sqrt(lambda) v <= {np.sqrt(lam4)*VEV/1e3:.2f} TeV")
    # all three heavy at once: (Mx My Mz)^2 <= lam^3 * max(v0^3 vx vy vz)
    pm = (0.5 ** 1.5) * ((1 / 6) ** 1.5) * VEV**6
    P(f"    all three carriers heavy simultaneously: geometric-mean mass <= {np.sqrt(np.cbrt(lam4**3 * pm))/1e3:.2f} TeV")
