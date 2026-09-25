#!/usr/bin/env python3
"""Conditional supplied clock diagnostics; see paired note for finite-window limits and premise boundaries.
Menu-dephasing factorization is not a framework admission or readout theorem.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys

import numpy as np
from scipy.linalg import expm

AUDIT_INPUT_PATHS = ['docs/FORMATION_RATE_FUNCTIONS_THE_AXIOM_TEXT_ADMITS_RECORD_DETERMINED_CLOCKS_REDUCE_TO_THE_CONSTANT_CLOCK_BETWEEN_NEIGHBOUR_RECORDS_AND_STATE_READING_CLOCKS_SPLIT_BY_MENU_DEPHASING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RECORD_FORMATION_CLOCK_IN_THE_CLAUSE_THE_FIELD_ALIGNED_MENU_S_ODDS_DO_NOT_DEPEND_ON_WHEN_RECORDS_FORM_BOUNDED_THEOREM_NOTE_2026-09-24.md']
AUDIT_TIMEOUT_SEC = 600

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1.0 + 0j, -1.0])
SIG = [X, Y, Z]
rng = np.random.default_rng(924)


def unit(v):
    v = np.asarray(v, dtype=float)
    return v / np.linalg.norm(v)


# ------------------------------------------------ the landed isolated-site model (supplied)
J = 1.0
q_rec = unit([0.6, 0.0, 0.8])                     # content of the recorded neighbours
hvec = J * q_rec                                  # H = (1/2) h.sigma
hhat = unit(hvec)
w = np.linalg.norm(hvec)                          # precession frequency
r0 = unit([0.5, 0.6, 0.4]) * 0.8                  # landed initial conditional Bloch vector
T, dt = 60.0, 2e-3
ts = np.arange(0, T + dt / 2, dt)
hax = unit([0.3, -0.5, 0.8])
tilt_landed = unit(hhat + 0.9 * unit(np.cross(hax, [1, 0, 0])))   # the landed runner's tilted menu (built from hax)
p_perp = unit(np.cross(hhat, [1, 0, 0]))                           # a menu perpendicular to the field
e2 = np.cross(hhat, p_perp)                                        # completes {p_perp, e2} in the transverse plane


def precess(r_init):
    """Exact precession r(t) = r_par + cos(wt) r_perp + sin(wt) hhat x r_perp (dr/dt = h x r)."""
    rpar = (r_init @ hhat) * hhat
    rperp = r_init - rpar
    c, s = np.cos(w * ts)[:, None], np.sin(w * ts)[:, None]
    return rpar[None, :] + c * rperp[None, :] + s * np.cross(hhat, rperp)[None, :]


def laplace_bloch(r_init, f0):
    """Closed form of the formation-weighted Bloch vector for a constant clock f0 as T -> infinity."""
    rpar = (r_init @ hhat) * hhat
    rperp = r_init - rpar
    return rpar + f0 ** 2 / (f0 ** 2 + w ** 2) * rperp + f0 * w / (f0 ** 2 + w ** 2) * np.cross(hhat, rperp)


def formation_density(f):
    assert np.all(np.isfinite(f)) and np.all(f >= 0), "hazards must be finite and nonnegative"
    F = np.concatenate([[0.0], np.cumsum(0.5 * (f[1:] + f[:-1]) * dt)])
    surv = np.exp(-F)
    return f * surv, surv[-1]


def recorded(rtraj, p, f):
    """Recorded odds of +p conditional on formation before T, survival at T, conditional mean formation time."""
    dens, s_end = formation_density(f)
    mass = np.trapezoid(dens, dx=dt)
    assert mass > 0
    dens = dens / mass
    odds = 0.5 * (1 + rtraj @ p)
    return np.trapezoid(dens * odds, dx=dt), s_end, np.trapezoid(dens * ts, dx=dt)


# ------------------------------------------------ the clock classes (rates as functions of the trajectory and menu)
P_LAW_PLUS = 0.75                                  # supplied law-level odds along the field for the diagnostic (D-law-value)


def law_functionals(pplus):
    p = np.array([pplus, 1 - pplus])
    ent = float(-(p[p > 0] * np.log2(p[p > 0])).sum())
    return {"law: entropy": ent, "law: support size": float((p > 0).sum()), "law: 1/max": float(1 / p.max())}


LAW = law_functionals(P_LAW_PLUS)
ones = np.ones(len(ts))
CLOCKS = {
    "constant": lambda r, p: np.ones(len(r)),
    "law: entropy": lambda r, p: LAW["law: entropy"] * np.ones(len(r)),
    "law: support size": lambda r, p: LAW["law: support size"] * np.ones(len(r)),
    "law: 1/max": lambda r, p: LAW["law: 1/max"] * np.ones(len(r)),
    "odds (1+r.p)/2": lambda r, p: 0.5 * (1 + r @ p),
    "alignment 2(r.p)^2": lambda r, p: 2 * (r @ p) ** 2,
    "purity |r|^2": lambda r, p: np.sum(r * r, axis=1),
    "coherence 1+4|rho+-|^2": lambda r, p: 1 + np.sum(r * r, axis=1) - (r @ p) ** 2,
}
REGISTERED = ["constant", "law: entropy", "law: support size", "law: 1/max", "odds (1+r.p)/2", "alignment 2(r.p)^2"]
STATE = ["purity |r|^2", "coherence 1+4|rho+-|^2"]

# ------------------------------------------------ 1. covariance of record-determined functionals under the 24 proper rotations
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if abs(np.linalg.det(R) - 1) < 1e-12:
            ROTS.append(R)


def field_law(records):
    """Supplied law along the field of the records: odds P_LAW_PLUS on +hhat(records); returns (axis, p_plus)."""
    h = sum(records, np.zeros(3))
    return unit(h), P_LAW_PLUS


def lab_z_component(axis, pplus):
    """A labelled functional: the law's odds of the +z possibility, (1 + (2 pplus - 1) axis.z)/2."""
    return 0.5 * (1 + (2 * pplus - 1) * axis[2])


records0 = [q_rec, q_rec]
base_axis, base_p = field_law(records0)
sym_dev, lab_dev = 0.0, 0.0
for R in ROTS:
    ax, pp = field_law([R @ q for q in records0])
    sym_dev = max(sym_dev, max(abs(law_functionals(pp)[k] - LAW[k]) for k in LAW))
    lab_dev = max(lab_dev, abs(lab_z_component(ax, pp) - lab_z_component(base_axis, base_p)))
check("finite check: covariance: relabelling-invariant functionals of the law-level distribution are fixed under the 24 proper cubic rotations; a labelled component is not",
      len(ROTS) == 24 and sym_dev < 1e-12 and lab_dev > 0.1,
      f"{len(ROTS)} rotations; entropy/support/1/max change by at most {sym_dev:.0e}; the +z odds change by up to {lab_dev:.3f}")

# ------------------------------------------------ 2. the register criterion: invariance under menu dephasing
NPTS = 400
rs = rng.normal(size=(NPTS, 3))
rs *= (rng.random(NPTS) ** (1 / 3) / np.linalg.norm(rs, axis=1))[:, None]         # uniform in the Bloch ball
p_rand = unit(rng.normal(size=3))
deph = (rs @ p_rand)[:, None] * p_rand[None, :]                                    # Delta_p(rho): keeps only r.p
dev = {}
for name, fn in CLOCKS.items():
    dev[name] = float(np.abs(fn(rs, p_rand) - fn(deph, p_rand)).max())
check("finite check: register criterion: constant, law, odds and alignment clocks are invariant under menu dephasing; purity and coherence clocks are not",
      all(dev[n] < 1e-12 for n in REGISTERED) and all(dev[n] > 0.1 for n in STATE),
      "max |f(rho) - f(Delta_p rho)| over 400 states: " + "; ".join(f"{n} {dev[n]:.0e}" if dev[n] < 1e-12 else f"{n} {dev[n]:.3f}" for n in CLOCKS))

# ------------------------------------------------ 3. constant clock closed form on the isolated site
rt = precess(r0)
rho0 = 0.5 * (I2 + sum(r0[a] * SIG[a] for a in range(3)))
H1 = 0.5 * sum(hvec[a] * SIG[a] for a in range(3))
U = expm(-1j * H1 * 1.37)
rho_t = U @ rho0 @ U.conj().T
prec_dev = np.abs(np.array([np.trace(rho_t @ SIG[a]).real for a in range(3)]) - precess(r0)[int(round(1.37 / dt))]).max()
cf_dev, landed = 0.0, []
for f0 in (1.0, r0 @ r0, 2.0, 0.5):
    for p in (tilt_landed, p_perp, hhat):
        P_num, s_end, _ = recorded(rt, p, f0 * ones)
        P_cf = 0.5 * (1 + laplace_bloch(r0, f0) @ p)
        cf_dev = max(cf_dev, abs(P_num - P_cf))
    landed.append(0.5 * (1 + laplace_bloch(r0, f0) @ tilt_landed))
born0 = 0.5 * (1 + r0 @ tilt_landed)
deph0 = 0.5 * (1 + (r0 @ hhat) * (hhat @ tilt_landed))
fast = 0.5 * (1 + laplace_bloch(r0, 1e3) @ tilt_landed)
slow = 0.5 * (1 + laplace_bloch(r0, 1e-3) @ tilt_landed)
check("finite check: constant clock: recorded odds equal (1 + r_f.p)/2 with the Laplace-transformed Bloch vector r_f; landed tilted values reproduced; fast and slow infinite-window limits",
      prec_dev < 1e-9 and cf_dev < 1e-5 and abs(landed[0] - 0.8437) < 5e-4 and abs(landed[1] - 0.8154) < 5e-4
      and abs(fast - born0) < 2e-3 and abs(slow - deph0) < 2e-3,
      f"precession vs expm {prec_dev:.0e}; trapezoid vs closed form at most {cf_dev:.0e} over 4 rates x 3 menus; landed tilted menu: "
      f"f=1 gives {landed[0]:.4f}, f=|r0|^2={r0 @ r0:.2f} gives {landed[1]:.4f}; limits on that menu: f=1e3 {fast:.4f} vs initial odds {born0:.4f}, "
      f"f=1e-3 {slow:.4f} vs field-dephased odds {deph0:.4f}; dt = {dt:.0e}, T = {T:.0f}; the landed tilt vector has cosine {tilt_landed @ hhat:.3f} to the field "
      f"(its construction vector has cosine {unit(np.cross(hax, [1, 0, 0])) @ hhat:.3f} to the field, so it is not the perpendicular direction)")

# ------------------------------------------------ 4. record-determined clocks reduce to the constant clock at their value
red_dev = 0.0
for name in ("law: entropy", "law: support size", "law: 1/max"):
    for p in (tilt_landed, hhat):
        Pl = recorded(rt, p, CLOCKS[name](rt, p))[0]
        Pc = recorded(rt, p, LAW[name] * ones)[0]
        red_dev = max(red_dev, abs(Pl - Pc))
tilt_vals = {n: recorded(rt, tilt_landed, CLOCKS[n](rt, tilt_landed))[0] for n in CLOCKS}
check("finite check: record-determined clocks: between neighbour record events each equals the constant clock at its value (isolated site, both menus)",
      red_dev < 1e-12,
      f"rates entropy {LAW['law: entropy']:.4f}, support {LAW['law: support size']:.0f}, 1/max {LAW['law: 1/max']:.4f} at supplied law odds {P_LAW_PLUS}; "
      f"odds differ from the constant clock at the same value by at most {red_dev:.0e}; tilted-menu odds by class: "
      + ", ".join(f"{n} {tilt_vals[n]:.4f}" for n in ("constant", "law: entropy", "law: 1/max", "odds (1+r.p)/2", "alignment 2(r.p)^2", "purity |r|^2", "coherence 1+4|rho+-|^2")))

# ------------------------------------------------ 5. witness pair on the perpendicular menu; formation time on the field menu
a, b, c = r0 @ p_perp, r0 @ e2, r0 @ hhat
rB = 0.2 * hhat + a * p_perp + b * e2                     # same transverse components, different field component
rtA, rtB = rt, precess(rB)
odds_dev = np.abs((rtA @ p_perp) - (rtB @ p_perp)).max()
coh_A = np.sqrt(np.sum(rtA * rtA, axis=1) - (rtA @ p_perp) ** 2) / 2      # |rho_{+-}| in the menu basis
coh_B = np.sqrt(np.sum(rtB * rtB, axis=1) - (rtB @ p_perp) ** 2) / 2
coh_gap = np.abs(coh_A - coh_B).min()
PA = {n: recorded(rtA, p_perp, CLOCKS[n](rtA, p_perp))[0] for n in CLOCKS}
PB = {n: recorded(rtB, p_perp, CLOCKS[n](rtB, p_perp))[0] for n in CLOCKS}
same = max(abs(PA[n] - PB[n]) for n in REGISTERED)
diff = {n: PA[n] - PB[n] for n in STATE}
# field menu: same field component, different transverse magnitude -> same odds, different purity-clock formation time
rC = c * hhat + 0.5 * (a * p_perp + b * e2)
rtC = precess(rC)
fld = {n: (recorded(rtA, hhat, CLOCKS[n](rtA, hhat)), recorded(rtC, hhat, CLOCKS[n](rtC, hhat))) for n in CLOCKS}
fld_odds_dev = max(abs(fld[n][0][0] - fld[n][1][0]) for n in CLOCKS)
tau_same = max(abs(fld[n][0][2] - fld[n][1][2]) for n in REGISTERED)
tau_pur = (fld["purity |r|^2"][0][2], fld["purity |r|^2"][1][2])
check("finite check: witness pair: identical menu odds at every time and different menu coherence give identical odds for fixed-menu-diagonal clocks and different odds for state-reading clocks",
      odds_dev < 1e-12 and coh_gap > 0.05 and same < 1e-12 and all(abs(d) > 0.005 for d in diff.values())
      and fld_odds_dev < 1e-9 and tau_same < 1e-9 and abs(tau_pur[0] - tau_pur[1]) > 0.1,
      f"perpendicular menu: |odds_A(t) - odds_B(t)| at most {odds_dev:.0e}; |rho+-| differs by at least {coh_gap:.3f}; fixed-menu-diagonal clocks differ by at most "
      f"{same:.0e} (constant {PA['constant']:.4f}); purity {PA['purity |r|^2']:.4f} vs {PB['purity |r|^2']:.4f} (gap {diff['purity |r|^2']:+.4f}); coherence "
      f"{PA['coherence 1+4|rho+-|^2']:.4f} vs {PB['coherence 1+4|rho+-|^2']:.4f} (gap {diff['coherence 1+4|rho+-|^2']:+.4f}). Field menu, same r.h, transverse halved: "
      f"odds differ by at most {fld_odds_dev:.0e} for all clocks; fixed-menu-diagonal mean formation times differ by at most {tau_same:.0e}; purity clock times "
      f"{tau_pur[0]:.3f} vs {tau_pur[1]:.3f}")

# ------------------------------------------------ 6. two-qubit model: an unrecorded partner
sA = [np.kron(s, I2) for s in SIG]
sB = [np.kron(I2, s) for s in SIG]
H2 = 0.5 * sum(hvec[a_] * sA[a_] for a_ in range(3)) + 0.25 * J * sum(sA[a_] @ sB[a_] for a_ in range(3))
rB0 = unit([-0.4, 0.3, 0.5]) * 0.9
rho2 = np.kron(0.5 * (I2 + sum(r0[a_] * SIG[a_] for a_ in range(3))), 0.5 * (I2 + sum(rB0[a_] * SIG[a_] for a_ in range(3))))
U2 = expm(-1j * H2 * dt)
rA = np.zeros((len(ts), 3))
st = rho2.copy()
for i in range(len(ts)):
    rA[i] = [np.trace(st @ sA[a_]).real for a_ in range(3)]
    st = U2 @ st @ U2.conj().T
varA = np.abs(rA @ hhat - r0 @ hhat).max()
P2 = {n: recorded(rA, hhat, CLOCKS[n](rA, hhat)) for n in CLOCKS}
two_law = {}
for n in ("law: entropy", "law: support size", "law: 1/max"):
    two_law[n] = abs(P2[n][0] - recorded(rA, hhat, LAW[n] * ones)[0])
dep = {n: P2[n][0] - P2["constant"][0] for n in ("odds (1+r.p)/2", "alignment 2(r.p)^2", "purity |r|^2", "coherence 1+4|rho+-|^2")}
surv2 = max(P2[n][1] for n in CLOCKS)
check("finite check: two-qubit model: record-determined clocks still equal the constant clock at their value; odds-reading and state-reading clocks depart (landed values reproduced)",
      varA > 0.2 and max(two_law.values()) < 1e-12 and all(abs(d) > 1e-4 for d in dep.values()) and surv2 < 1e-6
      and abs(P2["constant"][0] - 0.7197) < 5e-4 and abs(P2["purity |r|^2"][0] - 0.7204) < 5e-4
      and abs(P2["odds (1+r.p)/2"][0] - 0.7242) < 5e-4 and abs(P2["alignment 2(r.p)^2"][0] - 0.7535) < 5e-4,
      f"r_A.h varies by {varA:.3f}; law clocks vs constant clock at their value at most {max(two_law.values()):.0e}; field-menu odds: constant "
      f"{P2['constant'][0]:.4f}, law/entropy {P2['law: entropy'][0]:.4f}, law/1/max {P2['law: 1/max'][0]:.4f}, odds {P2['odds (1+r.p)/2'][0]:.4f}, alignment "
      f"{P2['alignment 2(r.p)^2'][0]:.4f}, purity {P2['purity |r|^2'][0]:.4f}, coherence {P2['coherence 1+4|rho+-|^2'][0]:.4f}; largest survival at T={T:.0f} is {surv2:.0e}")

# ------------------------------------------------ 7. an explicit-time clock
beta = np.pi / 2                                            # linear hazard beta t with unit mean formation time
f_lin = beta * ts
P_lin_t, s_lin, tau_lin = recorded(rt, tilt_landed, f_lin)
P_lin_h = recorded(rt, hhat, f_lin)[0]
P_con_t = recorded(rt, tilt_landed, ones)[0]
check("finite check: explicit-time clock: a linear hazard with unit mean formation time departs from the constant clock on the tilted menu and agrees on the field menu",
      abs(tau_lin - 1) < 1e-3 and abs(P_lin_t - P_con_t) > 0.005 and abs(P_lin_h - 0.5 * (1 + r0 @ hhat)) < 1e-9 and s_lin < 1e-12,
      f"mean formation time {tau_lin:.4f}; tilted-menu odds {P_lin_t:.4f} vs constant clock {P_con_t:.4f}; field-menu odds {P_lin_h:.4f} = (1 + r0.h)/2")

# Independent of the infinite-window helper: integrate the finite exponential exactly.
def finite_window_bloch(r_init, f0, horizon):
    assert f0 > 0 and horizon > 0
    z = f0 * (-np.expm1((-f0+1j*w)*horizon)) / ((f0-1j*w)*(-np.expm1(-f0*horizon)))
    parallel=(r_init@hhat)*hhat
    transverse=r_init-parallel
    return parallel+z.real*transverse+z.imag*np.cross(hhat,transverse)

horizon=1.3;small=1e-7
z_uniform=np.expm1(1j*w*horizon)/(1j*w*horizon)
parallel=(r0@hhat)*hhat;transverse=r0-parallel
uniform=parallel+z_uniform.real*transverse+z_uniform.imag*np.cross(hhat,transverse)
finite_slow=finite_window_bloch(r0,small,horizon)
check("finite check: finite-window slow rate approaches a time average, not field dephasing",
      np.linalg.norm(finite_slow-uniform)<1e-7 and np.linalg.norm(finite_slow-parallel)>.1,
      f"uniform-average residual {np.linalg.norm(finite_slow-uniform):.1e}; dephased difference {np.linalg.norm(finite_slow-parallel):.3f}")
check("finite check: oriented-odds rate fails unordered-menu swap; even alignment passes",
      abs(CLOCKS["odds (1+r.p)/2"](r0[None,:],hhat)[0]-CLOCKS["odds (1+r.p)/2"](r0[None,:],-hhat)[0])>.1
      and np.allclose(CLOCKS["alignment 2(r.p)^2"](r0[None,:],hhat),CLOCKS["alignment 2(r.p)^2"](r0[None,:],-hhat)))

print('per_element: Rate functions are classified by menu dephasing and rotation invariance.')
print('per_site: Isolated precession, closed-form constant-clock odds and witness pairs are tested.')
print('per_mode: checked and not executed - no normal-mode or continuum clock limit is claimed.')
print('per_block: One- and two-site trajectories under the supplied clause are tested.')
print('lattice_wide: checked and not executed - no many-site formation law is claimed.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
