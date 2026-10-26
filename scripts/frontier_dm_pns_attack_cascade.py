"""Supplied pns finite diagnostics; no global physical selection or PNS derivation."""

import math
import numpy as np
import scipy.optimize as opt
from collections import Counter

AUDIT_TIMEOUT_SEC = 1800

E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
GAMMA = 0.5
CHAMBER = E1   # q + delta >= sqrt(8/3)

TH12_NUFIT = math.radians(33.41)
TH13_NUFIT = math.radians(8.61)
TH23_NUFIT = math.radians(49.1)

BASIN1  = (0.657061, 0.933806, 0.715042)
BASIN2  = (28.006, 20.722, 5.012)
BASIN_X = (21.128264, 12.680028, 2.089235)
C_NEG_Q_NEG = (0.9985, 1.4299, -1.291)   # new; violates chamber
C_BASE_CONJ  = (0.4074, 0.8771, 0.4463)   # supplied positive-sine candidate; violates chamber

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, cond, detail=""):
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if cond else "FAIL"
    if cond: PASS_COUNT += 1
    else:    FAIL_COUNT += 1
    suffix = f"  [{detail}]" if detail else ""
    print(f"  {status}: {name}{suffix}")
    return cond


def H_base_matrix():
    return np.array([
        [0,              E1, -E1 - 1j * GAMMA],
        [E1,              0,             -E2],
        [-E1 + 1j * GAMMA, -E2,            0],
    ], dtype=complex)


def T_M():     return np.array([[1,0,0],[0,0,1],[0,1,0]], dtype=complex)
def T_delta(): return np.array([[0,-1,1],[-1,1,0],[1,0,-1]], dtype=complex)
def T_Q():     return np.array([[0,1,1],[1,0,1],[1,1,0]], dtype=complex)


def J_phys(m, d, q):
    return m * T_M() + d * T_delta() + q * T_Q()


def pmns_angles_and_sdcp(H, sigma):
    try:
        evals, evecs = np.linalg.eigh(H)
        V = evecs[np.array(sigma), :]
        s13 = float(np.clip(abs(V[0, 2]), 0.0, 1.0))
        th13 = math.asin(s13)
        c13 = math.cos(th13)
        th12 = math.atan2(abs(V[0, 1]), abs(V[0, 0]))
        th23 = math.atan2(abs(V[1, 2]), abs(V[2, 2]))
        if c13 < 1e-12:
            return th12, th13, th23, 0.0
        Jcp = float(np.imag(V[0, 0] * V[1, 1] * V[0, 1].conj() * V[1, 0].conj()))
        denom = (math.sin(th12) * math.cos(th12) * s13
                 * c13 ** 2 * math.sin(th23) * math.cos(th23))
        sdcp = Jcp / denom if abs(denom) > 1e-15 else 0.0
        return th12, th13, th23, sdcp
    except Exception:
        return 0.0, 0.0, 0.0, 0.0


def chi2_210(m, d, q, enforce_chamber=True):
    if enforce_chamber and (q + d) < CHAMBER - 1e-6:
        return 1e10
    H = H_base_matrix() + J_phys(m, d, q)
    th12, th13, th23, _ = pmns_angles_and_sdcp(H, [2, 1, 0])
    return (0.7 * (th12 - TH12_NUFIT) ** 2
            + 4.0 * (th13 - TH13_NUFIT) ** 2
            + 1.5 * (th23 - TH23_NUFIT) ** 2)


Hb = H_base_matrix()


print("\nT1: Attack vector 1 — eigenvalue monotonicity (INCONCLUSIVE)")
J1 = J_phys(*BASIN1)
ts = np.linspace(0, 1, 1000)
tracks = np.array([np.sort(np.linalg.eigvalsh(Hb + t * J1)) for t in ts])

for i in range(3):
    track = tracks[:, i]
    monotone = np.all(np.diff(track) >= -1e-12) or np.all(np.diff(track) <= 1e-12)
    check(f"Eigenvalue {i} nonmonotone on sampled path", not monotone,
          f"min={track.min():.4f}, max={track.max():.4f}")

hf_sign_changes = False
for t0 in np.linspace(0, 1, 20):
    H = Hb + t0 * J1
    _, evecs = np.linalg.eigh(H)
    hf = [np.sign(np.real(evecs[:, k].conj() @ J1 @ evecs[:, k])) for k in range(3)]
    if len(set(int(s) for s in hf)) > 1:
        hf_sign_changes = True
        break

check("Sampled HF signs differ across modes at some sampled time",
      hf_sign_changes,
      "ATTACK VECTOR 1: SAMPLED ROUTE LIMIT — HF signs differ across modes; this does not prove nonmonotonic tracks")

print("\nT2: Attack vector 3 — Cl(3) spectral lower bound (SAMPLED ROUTE LIMIT)")
for gen_name, gen in [("T_M", T_M()), ("T_delta", T_delta()), ("T_Q", T_Q())]:
    evals = np.linalg.eigvalsh(gen)
    psd = np.all(evals >= -1e-10)
    check(f"Generator {gen_name} is NOT positive semi-definite", not psd,
          f"eigenvalues={evals}")

J1_evals = np.linalg.eigvalsh(J1)
check("J_phys (Basin 1) is NOT positive semi-definite", not np.all(J1_evals >= -1e-10),
      f"J eigenvalues={J1_evals}")


print("\nT3: Attack vector 2 — chamber constraint (POSITIVE PARTIAL RESULT)")
print(f"  Chamber threshold: q + delta >= sqrt(8/3) = {CHAMBER:.6f}")

for name, p, expected_pass in [
    ("Basin 1", BASIN1, True), ("Basin 2", BASIN2, True), ("Basin X", BASIN_X, True),
    ("C_neg q<0 (NEW)", C_NEG_Q_NEG, False), ("C_base conj (NEW)", C_BASE_CONJ, False),
]:
    m, d, q = p
    val = q + d
    ok = val >= CHAMBER - 1e-6
    if expected_pass:
        check(f"Chamber satisfied: {name} (q+d={val:.4f})", ok)
    else:
        check(f"Chamber VIOLATED (as expected): {name} (q+d={val:.4f})", not ok)

check("C_neg q<0 solution EXCLUDED by chamber constraint",
      C_NEG_Q_NEG[1] + C_NEG_Q_NEG[2] < CHAMBER,
      f"q+d={C_NEG_Q_NEG[1]+C_NEG_Q_NEG[2]:.4f} < {CHAMBER:.4f}")

check("C_base supplied positive-sine candidate EXCLUDED by chamber constraint",
      C_BASE_CONJ[1] + C_BASE_CONJ[2] < CHAMBER,
      f"q+d={C_BASE_CONJ[1]+C_BASE_CONJ[2]:.4f} < {CHAMBER:.4f}")

H_qneg = Hb + J_phys(*C_NEG_Q_NEG)
th12q, th13q, th23q, sdcpq = pmns_angles_and_sdcp(H_qneg, [2, 1, 0])
chi2_qneg = chi2_210(*C_NEG_Q_NEG, enforce_chamber=False)
check("C_neg q<0 fits PMNS angles (chi^2 ~ 0, unconstrained)",
      chi2_qneg < 1e-5, f"chi^2={chi2_qneg:.2e}")
det_qneg = np.real(np.linalg.det(H_qneg))
check("C_neg q<0 is in C_neg (det < 0)", det_qneg < 0, f"det={det_qneg:.4f}")
check("Chamber excludes this C_neg solution: q+d < sqrt(8/3)",
      C_NEG_Q_NEG[1] + C_NEG_Q_NEG[2] < CHAMBER - 1e-3)

print("\nT4: supplied positive-sine candidate of Basin 1 excluded by chamber")
H_conj = Hb + J_phys(*C_BASE_CONJ)
th12c, th13c, th23c, sdcpc = pmns_angles_and_sdcp(H_conj, [2, 1, 0])
chi2_conj = chi2_210(*C_BASE_CONJ, enforce_chamber=False)
det_conj = np.real(np.linalg.det(H_conj))

check("supplied positive-sine candidate fits PMNS angles (chi^2 ~ 0, unconstrained)",
      chi2_conj < 1e-3, f"chi^2={chi2_conj:.2e}")
check("supplied positive-sine candidate is C_base (det > 0)", det_conj > 0, f"det={det_conj:.4f}")
check("supplied positive-sine candidate has sin(dcp) > 0 (fails the supplied negative-sign cut)",
      sdcpc > 0, f"sin(dcp)={sdcpc:.4f}")
check("supplied positive-sine candidate excluded by chamber (q+d < sqrt(8/3))",
      C_BASE_CONJ[1] + C_BASE_CONJ[2] < CHAMBER - 1e-3)

print("\nT5: C_neg + chamber + sin(dcp) audit (2000-seed scan)")
np.random.seed(999)
neg_sdcp_neg_found = 0
neg_sdcp_pos_found = 0

for _ in range(2000):
    m = np.random.uniform(0.5, 50.0)
    d = np.random.uniform(0.0, 30.0)
    q_min = CHAMBER - d
    q = np.random.uniform(q_min, q_min + 20.0)
    if q + d < CHAMBER:
        continue
    H0 = Hb + J_phys(m, d, q)
    if np.real(np.linalg.det(H0)) >= 0:
        continue
    _, _, _, sdcp0 = pmns_angles_and_sdcp(H0, [2, 1, 0])
    if sdcp0 >= 0:
        continue
    try:
        res = opt.minimize(
            lambda x: chi2_210(x[0], x[1], x[2], enforce_chamber=True),
            [m, d, q],
            method="Nelder-Mead",
            options={"xatol": 1e-8, "fatol": 1e-12, "maxiter": 6000},
        )
        if res.fun < 1e-5:
            m2, d2, q2 = res.x
            if q2 + d2 < CHAMBER - 1e-4:
                continue
            H2 = Hb + J_phys(m2, d2, q2)
            det2 = np.real(np.linalg.det(H2))
            if det2 >= 0:
                continue
            _, _, _, sdcp2 = pmns_angles_and_sdcp(H2, [2, 1, 0])
            if sdcp2 < 0:
                neg_sdcp_neg_found += 1
            else:
                neg_sdcp_pos_found += 1
    except Exception:
        pass

check(f"2000-seed scan: no C_neg+chamber chi^2=0 solutions found with sin(dcp) < 0",
      neg_sdcp_neg_found == 0,
      f"found={neg_sdcp_neg_found} negative-sign, {neg_sdcp_pos_found} nonnegative-sign")
check("No negative-sign fitted C_neg candidate found in this finite search",
      neg_sdcp_neg_found == 0,
      "empirical scan — no counter-example found in 2000 random C_neg starting points")

for name, p in [("Basin 2", BASIN2), ("Basin X", BASIN_X)]:
    H = Hb + J_phys(*p)
    _, _, _, sdcp = pmns_angles_and_sdcp(H, [2, 1, 0])
    det = np.real(np.linalg.det(H))
    in_chamber = p[1] + p[2] >= CHAMBER - 1e-6
    check(f"{name}: in chamber={in_chamber}, sin(dcp)={sdcp:.4f} > 0 (fails the supplied negative-sign cut)",
          in_chamber and sdcp > 0)

print("\nT6: Attack vector 5 — sampled determinant on the supplied Basin 1 segment")
ts_dense = np.linspace(0, 1, 5000)
dets_basin1 = np.array([np.real(np.linalg.det(Hb + t * J1)) for t in ts_dense])
min_det_basin1 = dets_basin1.min()
t_min = ts_dense[np.argmin(dets_basin1)]

check(f"Basin 1 linear path: min det = {min_det_basin1:.4f} > 0 (sampled determinant positive)",
      min_det_basin1 > 0)
check("Basin 1 min det > 0.87 (sampled comparison threshold)",
      min_det_basin1 > 0.87, f"min at t={t_min:.3f}")

min_abs_eval = min(
    np.min(np.abs(np.linalg.eigvalsh(Hb + t * J1))) for t in ts_dense[::10]
)
check(f"Min |eigenvalue| along Basin 1 path = {min_abs_eval:.4f} > 0.3",
      min_abs_eval > 0.3)


print("\nT7: Sigma-chain PNS conditional theorem")

for name, p in [("Basin 2", BASIN2), ("Basin X", BASIN_X)]:
    H = Hb + J_phys(*p)
    _, _, _, sdcp = pmns_angles_and_sdcp(H, [2, 1, 0])
    check(f"Sigma-chain step 2: {name} sin(dcp)={sdcp:.4f} > 0 (fails the supplied negative-sign cut)",
          sdcp > 0)

check("Supplied Basin-1 determinant samples remain positive",
      min_det_basin1 > 0)


print("\nT8: Supplied segments with determinant sign changes")



for name, p in [("Basin 2", BASIN2), ("Basin X", BASIN_X)]:
    J_test = J_phys(*p)
    dets_test = np.array(
        [np.real(np.linalg.det(Hb + t * J_test)) for t in np.linspace(0, 1, 500)]
    )
    has_crossing = np.any(np.diff(np.sign(dets_test)) != 0)
    check(
        f"Algebraic structure allows det=0 crossing: {name} (supplied generators and imposed chamber)",
        has_crossing,
        "this supplied chart segment has a sign-changing determinant",
    )


print("\nT9: Attack vector summary")

print('Finite search and sampled path diagnostics only; no exhaustive physical selector follows.')
print(f"\n{'=' * 60}")
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
if FAIL_COUNT == 0:
    print("STATUS: ALL PASS — listed finite diagnostics passed")
else:
    print("STATUS: FAILURES — see above")
print(f"{'=' * 60}")

print('PNS is an explicit path assumption; measurements and finite searches do not establish it.')
raise SystemExit(1 if FAIL_COUNT else 0)
