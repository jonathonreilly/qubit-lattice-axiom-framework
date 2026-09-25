#!/usr/bin/env python3
"""A formation clock inside the dynamics clause: on the field-aligned menu the recorded odds do not depend on when
records form; on other menus, or with an unrecorded neighbour, the rate function biases them.

Setting (all supplied, none adopted): the Heisenberg point of the dynamics clause (the supplied companion construction), records acting
as fields on their unrecorded neighbours (the supplied companion construction), the compression update with odds Tr(P_q rho) (open PRs
9083, 9085), and a formation clock (D-form): each unrecorded site carries a memoryless clock whose rate is a
function f of the site's conditional state rho = (1 + r.sigma)/2. Supplied model, finite diagnostics, no physical
reading.

1. Covariance classifies the rate functions. Among polynomials of degree at most two in the Bloch vector r, the
   invariants are spanned by {1, |r|^2} under every internal rotation (possibility covariance); by
   {1, |r|^2, r.h, (r.h)^2} when a physical axis h (the record field) is present; and by {1, |r|^2, (r.n)^2} for an
   unordered antipodal menu axis n. Numerical Reynolds averaging over the groups.
2. Isolated site (all neighbours recorded): the site is a qubit in the field h of their contents and its Bloch
   vector precesses about h, so r.h is conserved. For four rate functions (constant, purity |r|^2, the aligned
   odds (1 + r.p)/2, and 2 (r.p)^2) the recorded frequency on the menu along h equals (1 + r.h)/2 to 1e-9,
   whatever the clock (frequencies conditional on a record forming). On a menu tilted from h the recorded
   frequencies differ between the clocks (spread reported), and the mean formation time depends on the state for
   state-dependent rates.
3. The recorded law is a trace rule of one formation-weighted state rho_f = integral p_f(tau) rho(tau) dtau, a valid
   state for every clock (|r_f| <= 1 checked); the clocks differ only through rho_f.
4. With an unrecorded neighbour (site A with one recorded neighbour and one unrecorded partner B under the
   Heisenberg bond), r_A.h is not conserved, and the recorded frequency on the field menu depends on the clock
   (spread reported). So the clock-independence of the odds is exactly the isolated-site case of the supplied companion construction.
5. A ring of six qubits with clocks at every site, field-aligned menus where a recorded neighbour exists and a
   supplied axis elsewhere, run to full recording: stack frequencies of the aligned outcome for the four clocks
   with Monte Carlo errors, as a finite diagnostic.

Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys

import numpy as np
from scipy.linalg import expm

AUDIT_INPUT_PATHS = ('docs/RECORD_FORMATION_CLOCK_IN_THE_CLAUSE_THE_FIELD_ALIGNED_MENU_S_ODDS_DO_NOT_DEPEND_ON_WHEN_RECORDS_FORM_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
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


def rot(axis, ang):
    """Rotation matrix about a unit axis."""
    a = unit(axis)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def random_rotation():
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    w, x, y, z = q
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


# ------------------------------------------------ 1. covariant rate functions
def monomials(r):
    x, y, z = r
    return np.array([1, x, y, z, x * x, y * y, z * z, x * y, x * z, y * z])


def invariant_dimension(group_sample, npts=60):
    """Dimension of the space of degree<=2 polynomials in r invariant under a group, by Reynolds averaging."""
    pts = rng.normal(size=(npts, 3))
    M = np.array([monomials(p) for p in pts])                       # values of the 10 monomials at the points
    avg = np.zeros_like(M)
    for R in group_sample:
        avg += np.array([monomials(R @ p) for p in pts])
    avg /= len(group_sample)
    # invariant polynomials = fixed points of the Reynolds operator on the coefficient space
    C = np.linalg.lstsq(M, avg, rcond=None)[0]                      # 10x10 matrix of the averaged monomials
    return int(np.sum(np.abs(np.linalg.eigvals(C) - 1) < 1e-6))


so3 = [random_rotation() for _ in range(400)]
hax = unit([0.3, -0.5, 0.8])
so2 = [rot(hax, a) for a in np.linspace(0, 2 * np.pi, 48, endpoint=False)]
perp = unit(np.cross(hax, [1, 0, 0]))
o2 = so2 + [rot(perp, np.pi) @ R for R in so2]                      # add the flip h -> -h
d_all, d_axis, d_menu = invariant_dimension(so3), invariant_dimension(so2), invariant_dimension(o2)
check("covariance classifies the rate functions: 2 invariants with no axis, 4 with a physical field axis, 3 with an unordered menu axis",
      d_all == 2 and d_axis == 4 and d_menu == 3,
      f"degree-<=2 invariant dimensions: all rotations {d_all} ({{1, |r|^2}}); rotations about h {d_axis} "
      f"({{1, |r|^2, r.h, (r.h)^2}}); with the flip of an unordered menu {d_menu} ({{1, |r|^2, (r.n)^2}})")

# ------------------------------------------------ 2. isolated site: precession conserves r.h; the field menu is clock-independent
J = 1.0
q_rec = unit([0.6, 0.0, 0.8])                                       # content of two recorded neighbours (supplied)
hvec = J * q_rec                                                    # their field on the site: (J/4) q.sigma per record = (1/2) h.sigma
hhat = unit(hvec)
r0 = unit([0.5, 0.6, 0.4]) * 0.8                                    # initial conditional Bloch vector (length 0.8)
H1 = 0.5 * sum(hvec[a] * SIG[a] for a in range(3))
h_sigma = sum(hhat[a] * SIG[a] for a in range(3))
comm = np.abs(H1 @ h_sigma - h_sigma @ H1).max()
T, dt = 60.0, 2e-3
ts = np.arange(0, T + dt / 2, dt)
w = np.linalg.norm(hvec)
rt = np.array([rot(hhat, w * t) @ r0 for t in ts])                  # precession (checked against expm below)
rho0 = 0.5 * (I2 + sum(r0[a] * SIG[a] for a in range(3)))
Ut = expm(-1j * H1 * 1.37)
rho_t = Ut @ rho0 @ Ut.conj().T
r_expm = np.array([np.trace(rho_t @ SIG[a]).real for a in range(3)])
prec_dev = np.abs(r_expm - rot(hhat, w * 1.37) @ r0).max()
cons = np.abs(rt @ hhat - r0 @ hhat).max()
tilt = unit(hhat + 0.9 * perp)                                      # a menu tilted from the field
RATES = {
    "constant": lambda r, p: np.ones(len(r)),
    "purity |r|^2": lambda r, p: np.sum(r * r, axis=1),
    "aligned odds (1+r.p)/2": lambda r, p: 0.5 * (1 + r @ p),
    "alignment 2(r.p)^2": lambda r, p: 2 * (r @ p) ** 2,
}


def formation_density(f):
    assert np.all(np.isfinite(f)) and np.all(f >= 0), "hazards must be finite and nonnegative"
    F = np.concatenate([[0.0], np.cumsum(0.5 * (f[1:] + f[:-1]) * dt)])
    surv = np.exp(-F)
    return f * surv, surv[-1]


def recorded(rtraj, p, f):
    """Recorded frequency of the aligned outcome, conditional on a record forming before T; the survival at T; the
    conditional mean formation time; the formation-weighted Bloch vector."""
    dens, s_end = formation_density(f)
    mass = np.trapezoid(dens, dx=dt)
    assert mass > 0, "conditional record law requires positive formation probability"
    dens = dens / mass                        # conditional on a record forming before T
    odds = 0.5 * (1 + rtraj @ p)
    P = np.trapezoid(dens * odds, dx=dt)
    mean_tau = np.trapezoid(dens * ts, dx=dt)
    rbar = np.array([np.trapezoid(dens * rtraj[:, a], dx=dt) for a in range(3)])
    return P, s_end, mean_tau, rbar


rows_field, rows_tilt, taus, rbars, survs = [], [], [], [], []
for name, fn in RATES.items():
    Pf, s1, tau, rb = recorded(rt, hhat, fn(rt, hhat))
    Pt, s2, _, rbt = recorded(rt, tilt, fn(rt, tilt))
    rows_field.append(Pf)
    rows_tilt.append(Pt)
    taus.append(tau)
    rbars.append(np.linalg.norm(rb))
    rbars.append(np.linalg.norm(rbt))
    survs += [s1, s2]
born_field = 0.5 * (1 + r0 @ hhat)
expected_rates = [1.0, r0 @ r0, born_field, 2 * (r0 @ hhat)**2]
expected_taus = [1/f - T / np.expm1(f*T) for f in expected_rates]
clock_time_error = max(abs(a-b) for a,b in zip(taus, expected_taus))
dev_field = max(abs(P - born_field) for P in rows_field)
spread_tilt = max(rows_tilt) - min(rows_tilt)
tau_spread = max(taus) - min(taus)
check("isolated site: the field menu's recorded odds equal (1 + r.h)/2 for every clock; a tilted menu's odds depend on the clock",
      comm < 1e-12 and prec_dev < 1e-9 and cons < 1e-9 and dev_field < 1e-9 and spread_tilt > 0.02
      and clock_time_error < 1e-6 and tau_spread > 0.1,
      f"[H, h.sigma] = {comm:.0e}; precession vs expm {prec_dev:.0e}; r.h conserved to {cons:.0e}; field-menu odds deviate from "
      f"(1 + r.h)/2 = {born_field:.4f} by at most {dev_field:.0e} over the four clocks; tilted menu: odds "
      f"{', '.join(f'{P:.4f}' for P in rows_tilt)} (spread {spread_tilt:.4f}); conditional mean formation times "
      f"{', '.join(f'{t:.3f}' for t in taus)}; largest survival at T = 60 is {max(survs):.0e}")

# ------------------------------------------------ 3. the recorded law is the trace rule of one formation-weighted state
check("the recorded law is a trace rule of the formation-weighted state, a valid state for every clock",
      max(rbars) <= 1 + 1e-12 and all(abs(recorded(rt, tilt, fn(rt, tilt))[0]
                                          - 0.5 * (1 + recorded(rt, tilt, fn(rt, tilt))[3] @ tilt)) < 1e-12 for fn in RATES.values()),
      f"|r_f| over clocks and menus at most {max(rbars):.4f}; recorded odds equal (1 + r_f.p)/2 to 1e-12 for each clock")

# ------------------------------------------------ 4. an unrecorded neighbour breaks the clock-independence
sA = [np.kron(s, I2) for s in SIG]
sB = [np.kron(I2, s) for s in SIG]
H2 = 0.5 * sum(hvec[a] * sA[a] for a in range(3)) + 0.25 * J * sum(sA[a] @ sB[a] for a in range(3))
rB0 = unit([-0.4, 0.3, 0.5]) * 0.9
rhoA0 = 0.5 * (I2 + sum(r0[a] * SIG[a] for a in range(3)))
rhoB0 = 0.5 * (I2 + sum(rB0[a] * SIG[a] for a in range(3)))
rho2 = np.kron(rhoA0, rhoB0)
U2 = expm(-1j * H2 * dt)
rA = np.zeros((len(ts), 3))
st = rho2.copy()
for i in range(len(ts)):
    rA[i] = [np.trace(st @ sA[a]).real for a in range(3)]
    st = U2 @ st @ U2.conj().T
consA = np.abs(rA @ hhat - r0 @ hhat).max()
rowsA = [recorded(rA, hhat, fn(rA, hhat))[0] for fn in RATES.values()]
survA = max(recorded(rA, hhat, fn(rA, hhat))[1] for fn in RATES.values())
spreadA = max(rowsA) - min(rowsA)
check("with an unrecorded neighbour r.h is not conserved and the field menu's odds depend on the clock",
      consA > 0.05 and spreadA > 0.01,
      f"r_A.h varies by {consA:.3f} along the trajectory; field-menu odds {', '.join(f'{P:.4f}' for P in rowsA)} "
      f"(spread {spreadA:.4f}) against the isolated value {born_field:.4f}; largest survival at T = 60 is {survA:.0e}")

# ------------------------------------------------ 5. a ring of six sites with clocks everywhere (finite diagnostic)
L = 6
dim = 2 ** L


def op(site, s):
    return np.kron(np.kron(np.eye(2 ** site), s), np.eye(2 ** (L - site - 1)))


S = [[op(i, s) for s in SIG] for i in range(L)]
BONDS = [(i, (i + 1) % L) for i in range(L)]
zaxis = np.array([0.0, 0.0, 1.0])
dt5, ntraj = 0.05, 60


def hamiltonian(recorded_vals):
    """Heisenberg bonds between unrecorded sites; records act as fields J q on their unrecorded neighbours."""
    Hm = np.zeros((dim, dim), dtype=complex)
    for i, j in BONDS:
        ri, rj = recorded_vals.get(i), recorded_vals.get(j)
        if ri is None and rj is None:
            Hm += 0.25 * J * sum(S[i][a] @ S[j][a] for a in range(3))
        elif ri is None:
            Hm += 0.25 * J * sum(rj[a] * S[i][a] for a in range(3))         # the bond with sigma_j replaced by its content
        elif rj is None:
            Hm += 0.25 * J * sum(ri[a] * S[j][a] for a in range(3))
    return Hm


def menu_axis(i, recorded_vals):
    h = sum((recorded_vals[j] for j in ((i - 1) % L, (i + 1) % L) if j in recorded_vals), np.zeros(3))
    return unit(h) if np.linalg.norm(h) > 1e-12 else zaxis


def bloch(psi, i):
    return np.array([np.vdot(psi, S[i][a] @ psi).real for a in range(3)])


def run_ring(fn, psi0):
    psi, recorded_vals, aligned, total = psi0.copy(), {}, 0, 0
    U = expm(-1j * hamiltonian(recorded_vals) * dt5)
    t = 0.0
    while len(recorded_vals) < L and t < 400:
        fired = []
        for i in range(L):
            if i in recorded_vals:
                continue
            r = bloch(psi, i)
            p = menu_axis(i, recorded_vals)
            rate = float(fn(r[None, :], p)[0])
            if rng.random() < rate * dt5:
                fired.append((i, r, p))
        if fired:
            i, r, p = fired[rng.integers(len(fired))]          # one record per step
            odds_plus = 0.5 * (1 + r @ p)
            q = p if rng.random() < odds_plus else -p
            P = 0.5 * (np.eye(dim) + sum(q[a] * S[i][a] for a in range(3)))
            psi = P @ psi
            psi /= np.linalg.norm(psi)
            recorded_vals[i] = q
            aligned += int(np.allclose(q, p))
            total += 1
            U = expm(-1j * hamiltonian(recorded_vals) * dt5)
        psi = U @ psi
        t += dt5
    return aligned, total, t


psi0 = rng.normal(size=dim) + 1j * rng.normal(size=dim)
psi0 /= np.linalg.norm(psi0)
freqs, errs, times = [], [], []
for name, fn in RATES.items():
    al, tot, tt = 0, 0, []
    for _ in range(ntraj):
        a_, t_, tf = run_ring(fn, psi0)
        al += a_
        tot += t_
        tt.append(tf)
    p = al / tot
    freqs.append(p)
    errs.append(np.sqrt(p * (1 - p) / tot))
    times.append(np.mean(tt))
check("ring of six with clocks everywhere: stack frequencies of the aligned outcome per clock, with Monte Carlo errors (diagnostic)",
      all(0 < p < 1 for p in freqs) and all(e < 0.05 for e in errs),
      "; ".join(f"{n}: {p:.3f} +- {e:.3f}, mean time to full recording {t:.2f}" for n, p, e, t in zip(RATES, freqs, errs, times)))

print('per_element: Degree-two rate invariants and weighted trace probabilities are tested.')
print('per_site: Isolated precession and clock-weighted local menus are tested.')
print('per_mode: checked and not executed — no normal-mode or continuum clock limit is claimed.')
print('per_block: One- and two-site trajectories and finite-step six-site samples are tested.')
print('lattice_wide: checked and not executed — no many-site continuous-time limit or formation law is derived.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
