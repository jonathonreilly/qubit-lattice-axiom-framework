#!/usr/bin/env python3
"""Finite diagnostics for the conditional claims in the paired source note.

Random examples do not establish universal theorems; use the explicit proofs
and premises in that note. No native physical law or audit grade is claimed.
"""
import sys

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_LOCALITY_OF_MARGINALS_FORCES_PREPARATION_AFFINITY_AND_THE_TRACE_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

import numpy as np
from scipy.linalg import expm

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260924)
I2 = np.eye(2, dtype=complex)
PX = np.array([[0, 1], [1, 0]], dtype=complex)
PY = np.array([[0, -1j], [1j, 0]])
PZ = np.diag([1.0 + 0j, -1.0])
S = [PX / 2, PY / 2, PZ / 2]


def rho_of(r):
    return 0.5 * (I2 + r[0] * PX + r[1] * PY + r[2] * PZ)


def bloch(rho):
    return np.real(np.array([np.trace(rho @ P) for P in (PX, PY, PZ)]))


def unit(v):
    return v / np.linalg.norm(v)


# ------------------------------------------------ 1. the clause carries purifications
SS = sum(np.kron(s, s) for s in S)
SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
Ubond = expm(-1j * np.pi * SS)                    # J t = pi
phase = Ubond[0, 0]
swap_dev = np.linalg.norm(Ubond - phase * SWAP)
lens = []
for theta in np.linspace(0, np.pi / 4, 7):          # 1 -> 0 as the partial swap entangles
    U = expm(-1j * theta * SWAP)
    psi = U @ np.kron(np.array([1, 0]), np.array([0, 1]))
    rho_a = np.einsum("ij,kj->ik", psi.reshape(2, 2), psi.reshape(2, 2).conj())
    lens.append(np.linalg.norm(bloch(rho_a)))
check("the clause carries purifications: the Heisenberg bond at J t = pi is the swap, and partial swaps give every reduced Bloch length",
      swap_dev < 1e-12 and abs(lens[0] - 1) < 1e-12 and min(lens) < 1e-12 and np.all(np.diff(lens) <= 1e-12),
      f"|U - phase * SWAP| {swap_dev:.1e}; reduced Bloch lengths along the partial swap {np.round(lens, 3).tolist()}")

# ------------------------------------------------ 2. steering realizes every chord
def random_chord():
    """A random mixed rho and a random chord through it with pure endpoints."""
    r = unit(rng.normal(size=3)) * rng.uniform(0.05, 0.95)
    d = unit(rng.normal(size=3))
    # endpoints r + t d on the unit sphere: t^2 + 2 t (r.d) + |r|^2 - 1 = 0
    b_ = r @ d
    disc = np.sqrt(b_ * b_ - (r @ r - 1))
    t1, t2 = -b_ + disc, -b_ - disc
    n1, n2 = r + t1 * d, r + t2 * d
    p = t2 / (t2 - t1)                              # r = p n1 + (1 - p) n2
    return r, n1, n2, p


def steer(n1, n2, p):
    """Purification of p|n1><n1| + (1-p)|n2><n2| and the partner basis that steers to it."""
    def ket(n):
        w, v = np.linalg.eigh(rho_of(n))
        return v[:, 1]
    k1, k2 = ket(n1), ket(n2)
    # |Psi> = sqrt(p)|k1>|0> + sqrt(1-p)|k2>|1>; recording the partner in {|0>,|1>} steers to k1, k2
    Psi = np.sqrt(p) * np.kron(k1, [1, 0]) + np.sqrt(1 - p) * np.kron(k2, [0, 1])
    out = []
    for b in range(2):
        proj = np.kron(I2, np.outer(np.eye(2)[b], np.eye(2)[b]))
        v = proj @ Psi
        pb = np.real(v.conj() @ v)
        rho_site = np.einsum("ij,kj->ik", v.reshape(2, 2), v.reshape(2, 2).conj()) / pb
        out.append((pb, bloch(rho_site)))
    rho_red = np.einsum("ij,kj->ik", Psi.reshape(2, 2), Psi.reshape(2, 2).conj())
    return bloch(rho_red), out


worst = 0.0
for _ in range(200):
    r, n1, n2, p = random_chord()
    red, out = steer(n1, n2, p)
    worst = max(worst, np.linalg.norm(red - r), abs(out[0][0] - p), np.linalg.norm(out[0][1] - n1), np.linalg.norm(out[1][1] - n2))
check("steering realizes every chord: a record on a purifying partner leaves the site in either endpoint with the chord weights",
      worst < 1e-10, f"200 random chords; largest deviation {worst:.1e}")

# ------------------------------------------------ 3-4. consistency and signalling
def law_trace(r, m):
    return 0.5 * (1 + r @ m)


def law_tanh(r, m, k=2.0):
    return 0.5 * (1 + np.tanh(k * (r @ m)) / np.tanh(k))


def law_cubic(r, m, eps=0.3):
    x = r @ m
    return 0.5 * (1 + x + eps * (x ** 3 - x))


def marginal_shift(law):
    """max |sum_b p_b P(rho_b) - P(rho)| over random chords and menu axes."""
    worst_ = 0.0
    for _ in range(300):
        r, n1, n2, p = random_chord()
        m = unit(rng.normal(size=3))
        worst_ = max(worst_, abs(p * law(n1, m) + (1 - p) * law(n2, m) - law(r, m)))
    return worst_


def axis_signal(law):
    """A partially entangled pair: recording the partner along x or z gives different site marginals."""
    worst_ = 0.0
    for _ in range(100):
        r = unit(rng.normal(size=3)) * rng.uniform(0.2, 0.8)
        m = unit(rng.normal(size=3))
        margs = []
        for _ in range(2):
            d = unit(rng.normal(size=3))
            b_ = r @ d
            disc = np.sqrt(b_ * b_ - (r @ r - 1))
            t1, t2 = -b_ + disc, -b_ - disc
            n1, n2 = r + t1 * d, r + t2 * d
            p = t2 / (t2 - t1)
            margs.append(p * law(n1, m) + (1 - p) * law(n2, m))
        worst_ = max(worst_, abs(margs[0] - margs[1]))
    return worst_


s_tr, s_tanh, s_cub = marginal_shift(law_trace), marginal_shift(law_tanh), marginal_shift(law_cubic)
check("the trace rule is consistent: the steered average equals the law at the reduced state",
      s_tr < 1e-12, f"largest |sum_b p_b P(rho_b) - P(rho)| over 300 chords {s_tr:.1e}")
a_tanh, a_cub = axis_signal(law_tanh), axis_signal(law_cubic)
check("nonlinear laws signal: a tanh deformation of the landed exp counterkernel and a cubic deformation change the site's marginal with the distant record and its axis",
      s_tanh > 1e-2 and s_cub > 1e-2 and a_tanh > 1e-2 and a_cub > 1e-2,
      f"record-or-not shift: tanh {s_tanh:.3f}, cubic {s_cub:.3f}; axis-choice shift: tanh {a_tanh:.3f}, cubic {a_cub:.3f}")

# ------------------------------------------------ 5. chord consistency forces affinity
def chord_nonlinearity(eps):
    worst_ = 0.0
    for _ in range(200):
        r, n1, n2, p = random_chord()
        m = unit(rng.normal(size=3))
        worst_ = max(worst_, abs(p * law_cubic(n1, m, eps) + (1 - p) * law_cubic(n2, m, eps) - law_cubic(r, m, eps)))
    return worst_


eps_list = [0.0, 0.01, 0.1, 0.3]
nl = [chord_nonlinearity(e) for e in eps_list]
check("chord consistency forces affinity: the cubic deformation passes only at zero deformation, and fails in proportion to it",
      nl[0] < 1e-12 and all(x > 1e-4 for x in nl[1:]) and nl[1] < nl[2] < nl[3],
      "largest chord violation " + ", ".join(f"eps {e}: {v:.1e}" for e, v in zip(eps_list, nl)))

# ------------------------------------------------ 6. orientation from compression
# D-perm: a record q leaves the normalized compression P_q rho P_q / Tr(P_q rho), which must exist
# whenever the record can form. For the affine menu law (1 + lam r.q)/2 at the antipodal pure state
# r = -q, Tr(P_q rho) = 0, so P(q | -q) = (1 - lam)/2 must vanish.
q = np.array([0.0, 0.0, 1.0])
lams = np.linspace(-1, 1, 21)
viol = [(1 - lam) / 2 for lam in lams]
only_one = [lam for lam, v in zip(lams, viol) if v < 1e-15]
# general two-outcome effects E_q = a I + b.sigma/2 (0 <= E <= I), E_{-q} = I - E_q:
# consistency needs Tr(E_q P_{-q}) = 0 and Tr(E_{-q} P_q) = 0
Pq, Pmq = rho_of(q), rho_of(-q)
best = []
for _ in range(20000):
    bvec = rng.normal(size=3) * rng.uniform(0, 1)
    a = rng.uniform(np.linalg.norm(bvec) / 2, 1 - np.linalg.norm(bvec) / 2) if np.linalg.norm(bvec) < 1 else 0.5
    E = a * I2 + sum(bvec[k] * S[k] for k in range(3))
    w = np.linalg.eigvalsh(E)
    if w.min() < -1e-12 or w.max() > 1 + 1e-12:
        continue
    v = abs(np.real(np.trace(E @ Pmq))) + abs(np.real(np.trace((I2 - E) @ Pq)))
    best.append((v, np.linalg.norm(E - Pq)))
best.sort()
# A finite sample ratio is descriptive only; no uniform bound follows.
ratio = max(d / v for v, d in best if v > 1e-6)
check("orientation from compression: a record must leave a normalizable compressed state, so P(q | -q) = 0; this forces lambda = 1 and, for any two-outcome effect, E_q = P_q",
      only_one == [1.0] and abs(law_trace(-q, q)) < 1e-15 and law_trace(q, q) == 1.0,
      f"lambda passing on a 21-point grid: {[float(x) for x in only_one]}; {len(best)} sampled effects (sample ratio |E_q - P_q| / violation up to {ratio:.2f})")

# ------------------------------------------------ 7. self-consistent weights
# The partner's record weights come from the same law as the site's. A random pure site-partner state;
# the partner records along n with weights f(+-b.n) from its own reduced Bloch vector b; the site's
# conditional states follow by projecting the partner; D-loc compares the site's marginal with and
# without the partner's record.
def selfconsistent_shift(f, trials=400):
    worst_ = 0.0
    for _ in range(trials):
        v = rng.normal(size=4) + 1j * rng.normal(size=4)
        v /= np.linalg.norm(v)
        M = v.reshape(2, 2)                                   # site x partner amplitudes
        rho_site = M @ M.conj().T
        rho_part = M.T @ M.conj()
        r, bvec = bloch(rho_site), bloch(rho_part)
        n, m = unit(rng.normal(size=3)), unit(rng.normal(size=3))
        avg = 0.0
        for sgn in (1, -1):
            Pn = rho_of(sgn * n)
            cond = M @ Pn.T @ M.conj().T                   # site state given partner outcome (unnormalized)
            pr = np.real(np.trace(cond))
            if pr < 1e-12:
                continue
            w = f(sgn * (bvec @ n))                          # the partner's weight from the same law
            avg += w * f(bloch(cond / pr) @ m)
        worst_ = max(worst_, abs(avg - f(r @ m)))
    return worst_


laws = {
    "Born (lambda 1)": lambda x: 0.5 * (1 + x),
    "trivial (lambda 0)": lambda x: 0.5,
    "lambda 0.5": lambda x: 0.5 * (1 + 0.5 * x),
    "anti-Born (lambda -1)": lambda x: 0.5 * (1 - x),
    "cubic": lambda x: 0.5 * (1 + x + 0.3 * (x ** 3 - x)),
}
sc = {k: selfconsistent_shift(f) for k, f in laws.items()}
ok7 = sc["Born (lambda 1)"] < 1e-12 and sc["trivial (lambda 0)"] < 1e-12 and all(sc[k] > 1e-2 for k in ("lambda 0.5", "anti-Born (lambda -1)", "cubic"))
check("self-consistent weights: with the partner's weights from the same law, the sampled laws agree with the exact affine-family classification; support excludes lambda = 0",
      ok7, "largest marginal shift: " + ", ".join(f"{k} {v:.1e}" for k, v in sc.items()))

# ------------------------------------------------ 8. the distant update carries the argument
# Replacement countermodel: a record q at the partner sets the partner to P_q and leaves the site's
# state at its reduced state (no distant update). The lock holds, and D-loc holds for every law.
def replacement_test(f, trials=300):
    worst_loc, worst_gap = 0.0, 0.0
    for _ in range(trials):
        v = rng.normal(size=4) + 1j * rng.normal(size=4)
        v /= np.linalg.norm(v)
        M = v.reshape(2, 2)
        rho_site, rho_part = M @ M.conj().T, M.T @ M.conj()
        r, bvec = bloch(rho_site), bloch(rho_part)
        n, m = unit(rng.normal(size=3)), unit(rng.normal(size=3))
        avg = 0.0
        for sgn in (1, -1):
            w = f(sgn * (bvec @ n))                               # the partner ends in P_q (the lock)
            avg += w * f(r @ m)                                   # the site keeps its reduced state
        worst_loc = max(worst_loc, abs(avg - f(r @ m)))
        worst_gap = max(worst_gap, abs(f(r @ m) - 0.5 * (1 + r @ m)))
    return worst_loc, worst_gap


rep = {"anti-Born": replacement_test(lambda x: 0.5 * (1 - x)), "tanh": replacement_test(lambda x: 0.5 * (1 + np.tanh(2 * x) / np.tanh(2)))}
check("the distant update carries the argument: with a replacement update (the lock alone) anti-Born and tanh laws pass D-loc",
      all(v[0] < 1e-12 and v[1] > 0.1 for v in rep.values()),
      "; ".join(f"{k}: D-loc shift {v[0]:.0e}, largest gap to the trace rule {v[1]:.2f}" for k, v in rep.items())
      + " (the lock holds by construction)")

# ------------------------------------------------ 9. D-loc is an equal-time reading
def chain_ops(n):
    def op(site, P):
        mats = [I2] * n
        mats[site] = P
        out = mats[0]
        for mm in mats[1:]:
            out = np.kron(out, mm)
        return out
    H = sum(op(i, P) @ op(i + 1, P) for i in range(n - 1) for P in (PX, PY, PZ)) / 4
    return op, H


nch = 4
op4, H4 = chain_ops(nch)
psi = rng.normal(size=2 ** nch) + 1j * rng.normal(size=2 ** nch)
psi /= np.linalg.norm(psi)
rho0 = np.outer(psi, psi.conj())
Pz = [op4(nch - 1, 0.5 * (I2 + sg * PZ)) for sg in (1, -1)]
rec = sum(P @ rho0 @ P for P in Pz)                                # a record at site 3, outcome not selected
shifts = []
for t in (0.0, 0.01, 0.05, 0.1):
    U = expm(-1j * H4 * t)
    b_no = np.real([np.trace(U @ rho0 @ U.conj().T @ op4(0, P)) for P in (PX, PY, PZ)])
    b_rec = np.real([np.trace(U @ rec @ U.conj().T @ op4(0, P)) for P in (PX, PY, PZ)])
    shifts.append(np.linalg.norm(b_no - b_rec))
growth = np.log(shifts[3] / shifts[2]) / np.log(2)
check("D-loc is an equal-time reading: a record at distance 3 leaves site 0 unchanged at equal time and shifts it afterwards",
      shifts[0] < 1e-12 and all(x > 1e-9 for x in shifts[1:]) and 2.5 < growth < 3.5,
      f"shift of site 0's Bloch vector at t = 0, 0.01, 0.05, 0.1: {shifts[0]:.0e}, {shifts[1]:.1e}, {shifts[2]:.1e}, {shifts[3]:.1e}; growth exponent {growth:.2f}")


# Exact formula evaluated away from zero: lambda(lambda-1)r/2.
for lam in (-1.0,0.0,0.5,1.0):
    r=0.5
    direct=(1+lam*r)/2
    avg=(1+lam*r)/2*(1+lam)/2+(1-lam*r)/2*(1-lam)/2
    check(f"affine self-weighted identity lambda={lam}",abs((avg-direct)-lam*(lam-1)*r/2)<1e-14)
th=1e-5
Et=np.array([[np.cos(th)**2,np.cos(th)*np.sin(th)],[np.cos(th)*np.sin(th),np.sin(th)**2]])
v=2*np.sin(th)**2
check("support ratio has no constant linear bound",np.linalg.norm(Et-np.diag([1,0]))/v>1e4)

# Scope resolutions are provenance, not additional numerical checks.
print('N5 resolution: Supply ensemble weights in the general affinity argument; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Restrict self-weighted classification to the affine covariant family; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Separate controlled preparation from an autonomous randomizer; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Use exact positive-effect support instead of a sampled ratio bound; see the explicit conditional proof and limitation in the paired note.')
print('N5 resolution: Keep frequency and finite-time propagation obligations separate; see the explicit conditional proof and limitation in the paired note.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
