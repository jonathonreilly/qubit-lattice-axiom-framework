#!/usr/bin/env python3
"""Same-coupling executed positive field-update response tournament (SPEC B draft).

An EXECUTED, exactly time-reversible, finite-step (leapfrog / Stormer-Verlet)
field update is driven on two DECLARED positive-sector carriers by ONE physical
coupling constant q that enters BOTH the source insertion q*g(t)<rho_src, phi>
AND the receiver readout q*<rho_rec, phi>.  The tournament asks whether the
executed update reproduces the Cycle-626 stationary q^2-elimination response in
the adiabatic (slow-ramp) limit at a preregistered convergence rate, without
refit, with orientation-sign cancellation holding under the same coupling,
flipping under a preregistered source/receiver DECOUPLING, and nulling under
receiver decoupling (no contact leakage).

Carriers (DECLARED SUPPLIED STRUCTURE, constructed in-run):
  D1 periodic : combinatorial graph Laplacian of the c576 L3/L6/L7 periodic
                cubic site graph (3-torus), restricted to the zero-mode-removed
                P0 sector (constant mode projected out).
  D2 open     : real open Dirichlet finite-difference scalar Laplacian on the
                same L3/L6/L7 site sets, boundary sites clamped (no zero mode).
The transcribed Cycle-626 anchor eigenvalues are reproduced on matching
fixtures by construction (D1 P0 min-nonzero 2(1-cos 2pi/L) -> 0.753 at L7;
D2 min 3*2(1-cos pi/(L+1)) -> 1.757/0.594/0.457 at L3/L6/L7).

FIREWALLS (interpretation guards; also written verbatim to the receipt):
  - The certified object is a SAME-COUPLING executed-update response law on the
    two DECLARED carriers.  It is NOT energy, NOT stress, NOT a unique physical
    coupling normalization (q is declared; c613's "representation charge is not
    a unique physical coupling" stands), NOT a source-law selection, NOT
    gravity, NOT attraction language, NOT a rate, NOT physical time.
  - A contact-sensitive response is not energy/stress/source/gravity: the
    q_rec=0 bare-field readout <rho_rec, phi> is REPORTED AS DIAGNOSTIC ONLY and
    certified as nothing; the certified response is the q-coupled readout.
  - The finite-Weyl NQ carrier join (c607/c609) is NOT executed here and stays
    open; no open-real-space coframe K claim; the F17 domain is untouched.
  - No 3/4 DELAY association, no PR5557 harness compilation, no 5/4 ADVANCE
    count-edit driving.
  - Carriers / ramp / hold window / grids / source-receiver supports are
    DECLARED SUPPLIED STRUCTURE; no new axiom, primitive, or premise class.

ACCEPTANCE DUTIES (owner + supervisor):
  - The supervisor owns all verdicts, line-by-line review, execution, cycle
    number, promotions; this runner only computes rows and writes its receipt.
  - Re-hash the imported c576 runner against the pinned sha before trusting any
    anchor; the c626/c604 notes and receipts are transcribed read-only anchors,
    never read from disk.
  - Declared divergences (see D1 near/far below) are REPORTED, not forced to a
    match, and not silently promoted to a pass.

PREREGISTERED FALSIFIERS (each maps to a named check row):
  F1 decoupled arm fails to flip sign  -> FAIL (same-coupling requirement empty).
  F2 adiabatic convergence violates the frozen rate p=2 -> FAIL (bridge broken).
  F3 reversibility recovery exceeds the machine-tight bound -> FAIL.
  F4 an anchor eigenvalue row mismatches with no declared divergence -> FAIL.
  F5 near/far ordering inverts on a size where the test is WELL-POSED (open
     carrier) -> FAIL.  (On the compact torus the P0 Green's function is
     antipode-peaked; D1 near/far is a DECLARED DIVERGENCE, not a hard gate.)
  F6 kick/drift orderings disagree beyond the O(dt^2) declared bound -> FAIL.

No git/subprocess/network.  Runner writes its own receipt JSON.  Decisive exit.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product as iproduct
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np
import scipy.sparse as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

# c576 supplies the fixture/frame idioms and the source-profile machinery.
# c579 is NOT imported: its kernel/Lie-product/frame-selection machinery is not
# used by this executed-leapfrog response tournament (spec prefers not importing
# it; its sha is pinned below as a recorded anchor only).
import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as c576


# ------------------------------------------------------------------ identity
CYCLE_CLAIM = 681  # frozen 2026-07-23: joint visible max at freeze was 680
#                    (this lane's evaluator tournament; 679 = PR #5563;
#                    campaign tip fb0ab5636e filenames reach 678). Descriptive
#                    filenames per owner directive; claim lives in content only.
DATE = "2026-07-23"
AUTHORITY = "none"
AUDIT = "unset"

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SAME_COUPLING_EXECUTED_FIELD_UPDATE_RESPONSE_TOURNAMENT_"
    "NOTE_2026-07-23.md"
)
RECEIPT_PATH = ROOT / "outputs" / (
    "physical_same_coupling_executed_field_update_response_tournament_"
    "receipt_2026_07_23.json"
)


# ------------------------------------------------------------------ tolerances (frozen)
REVERSIBILITY_TOL = 1.0e-11     # scaled machine-tight forward-then-reversed bound
SYMPLECTIC_TOL = 1.0e-11        # ||M^T J M - J||_F for the one-step linear map
INVERSE_RESID_TOL = 1.0e-12     # ||H phi* + q P rho_src|| on the sector
ENERGY_DRIFT_TOL = 5.0e-2       # bounded shadow-energy relative oscillation band
SECULAR_FRACTION_TOL = 0.20     # secular drift as fraction of the bounded band
ANCHOR_TOL = 1.0e-3             # transcribed c626 anchor eigenvalue tolerance
POSITIVITY_MARGIN = 1.0e-6      # min sector eigenvalue must exceed this
EXACT_ZERO_TOL = 1.0e-12        # source-off / receiver-zero / q_rec=0 certified
SIGNAL = 1.0e-6                 # a control must move by at least this
SIGN_INVARIANCE_TOL = 1.0e-10   # |E_exec(+q) - E_exec(-q)| executed even-ness
DECOUPLE_REL_TOL = 1.2e-2       # |E_dec - (-E_stat)| / |E_stat| flip magnitude (adiabatic residual at TAU_PROBE)
SCALE_EXP_TOL = 5.0e-2          # measured q-exponent vs 2
MEAN_CONV_TOL = 1.0e-3          # |hold-mean(tau_max) - E_stat| convergence bound
ORDER_DT2_COEFF = 1.0           # |E_KDK - E_DKD| <= ORDER_DT2_COEFF * dt^2

# ------------------------------------------------------------------ dynamics (frozen)
DT = 0.01                       # leapfrog step (stable: dt*omega_max ~ 0.035)
T_HOLD = 24.0                   # FIXED hold window (independent of tau -> preserves p)
TAU_LADDER = (20.0, 40.0, 80.0, 160.0)   # geometric x2 ramp-time ladder
Q_MAIN = 1.0
Q_SCALE = (0.5, 1.0, 2.0)
TAU_PROBE = 80.0                # single ramp time for sign/scale/near-far rows
PREREGISTERED_P = 2.0           # frozen adiabatic rate (see design memo derivation)
P_TOL = 0.35                    # |fitted slope - (-2)| tolerance
ENVELOPE_C = 1.0                # frozen envelope: deviation(tau) * tau^2 <= ENVELOPE_C (measured max ~0.56)
SIZES = (3, 6, 7)

# Frozen source/receiver geometry per (carrier, L): (src, near, far, ball_radius).
# Bounded, disjoint supports; radius 0 on the L3 torus (too small for disjoint
# balls), radius 1 elsewhere.  near/far declared displacements (frozen control).
GEOMETRY = {
    ("D1", 3): ((0, 0, 0), (1, 0, 0), (1, 1, 1), 0),
    ("D1", 6): ((0, 0, 0), (3, 0, 0), (3, 3, 3), 1),
    ("D1", 7): ((0, 0, 0), (3, 0, 0), (3, 3, 3), 1),
    ("D2", 3): ((0, 0, 0), (1, 1, 1), (2, 2, 2), 1),
    ("D2", 6): ((0, 0, 0), (2, 2, 2), (5, 5, 5), 1),
    ("D2", 7): ((0, 0, 0), (2, 2, 2), (6, 6, 6), 1),
}
# near/far locality is a HARD gate only on the open carrier D2 (decaying
# propagator).  On the periodic carrier D1 the P0 Green's function is
# antipode-peaked (compact-carrier / commute-time structure), so near/far is a
# DECLARED DIVERGENCE diagnostic, not a hard fail.
NEARFAR_HARD_GATE = ("D2",)


# ------------------------------------------------------------------ PINS (read-only anchors)
PINS = {
    "campaign_head": "fb0ab5636e557d8de1da8e643f419867ae69197a",
    "c626_note": "1346e9c5aec6206642e64059eeff0b49d59df33f8fe0584c7c8537d3e2760893",
    "c626_receipt": "ab8489e9875e362d2b496b1f92464e6c5c642eb3cdb72b1755e77c4d70b752f6",
    "c604_receipt": "2fe20ba1ddbe304a11eb1809f76d552fdab89ff77d1c281d775d730c36021e90",
    "c576_script": "53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
    "c576_note": "2d5650c57d5518e274803f5c511886981c8572b553dda926739cc98199939c20",
    "c576_receipt": "06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
    "c579_script": "e607e8a0d46fbb70e7be35d1897acebebdb8ad900a4ab69159e572f3fbc5c7ab",
    # transcribed Cycle-626 comparator anchors to reproduce in-run:
    "c626_periodic_min_nonzero": 0.753,          # D1, belongs to L7 by construction
    "c626_dirichlet_min": {"3": 1.757, "6": 0.594, "7": 0.457},
    "c626_sign_cancellation_residual": 0.0,      # stationary, exact
    "c626_source_off_action": 0.0,               # exact
    "c626_receiver_zero_action": 0.0,            # exact
}

CLAIM_BOUNDARIES = {
    "certified_object": "same-coupling executed-update response law on two declared carriers",
    "is_energy": False, "is_stress": False, "is_gravity": False,
    "is_unique_physical_coupling_normalization": False, "is_source_law_selection": False,
    "is_attraction_language": False, "is_rate": False, "is_physical_time": False,
    "c613_representation_charge_not_unique_coupling_stands": True,
    "contact_sensitive_response_is_certified_as_nothing": True,
    "finite_Weyl_NQ_carrier_join_c607_c609_executed": False,
    "open_real_space_coframe_K_claimed": False, "F17_domain_touched": False,
    "three_over_four_DELAY_association_used": False, "PR5557_harness_compiled": False,
    "five_over_four_ADVANCE_count_edit_driven": False,
    "new_axiom_primitive_or_premise_class_added": False,
}

FIREWALLS = [
    "The certified object is a same-coupling executed-update response law on the two "
    "declared carriers; it is NOT energy, NOT stress, NOT a unique physical coupling "
    "normalization (q is declared; c613's representation-charge-is-not-a-unique-coupling "
    "stands), NOT a source-law selection, NOT gravity, NOT attraction language, NOT a "
    "rate, NOT physical time.",
    "A contact-sensitive response is not energy/stress/source/gravity: the q_rec=0 "
    "bare-field readout <rho_rec, phi> is reported as diagnostic only and certified as "
    "nothing; the certified response is the q-coupled readout.",
    "The finite-Weyl NQ carrier join (c607/c609) is not executed here and stays open; no "
    "open-real-space coframe K claim; the F17 domain is untouched.",
    "No 3/4 DELAY association, no PR5557 harness compilation, no 5/4 ADVANCE count-edit "
    "driving.",
    "Carriers, ramp, hold window, grids and source/receiver supports are declared "
    "supplied structure; no new axiom, primitive, or premise class.",
]

ACCEPTANCE_DUTIES = [
    "The supervisor owns all verdicts, line-by-line review, execution, the claimed cycle "
    "number and any promotion; this runner only computes rows and writes its receipt.",
    "Re-hash the imported c576 runner against the pinned sha before trusting any anchor; "
    "the c626/c604 notes and receipts are transcribed read-only anchors, never read from disk.",
    "Declared divergences (D1 periodic near/far antipode-peaking) are reported, not forced "
    "to a match, and not silently promoted to a pass.",
]


# ------------------------------------------------------------------ harness
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)
    return ok


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


# ------------------------------------------------------------------ carriers
def periodic_laplacian_1d(L: int) -> np.ndarray:
    """1D circulant (ring) combinatorial Laplacian: eigenvalues 2(1-cos 2pi k/L)."""
    M = 2.0 * np.eye(L) - np.eye(L, k=1) - np.eye(L, k=-1)
    M[0, -1] -= 1.0
    M[-1, 0] -= 1.0
    return M


def dirichlet_laplacian_1d(L: int) -> np.ndarray:
    """1D Dirichlet finite-difference Laplacian on L interior points:
    eigenvalues 2(1-cos k*pi/(L+1))."""
    return 2.0 * np.eye(L) - np.eye(L, k=1) - np.eye(L, k=-1)


def kron_sum_3d(A: np.ndarray, L: int) -> np.ndarray:
    """3D Kronecker sum A(x) (+) A(y) (+) A(z) on the L^3 site grid."""
    I = np.eye(L)
    return (np.kron(np.kron(A, I), I)
            + np.kron(np.kron(I, A), I)
            + np.kron(np.kron(I, I), A))


def build_carrier(kind: str, L: int) -> dict:
    """Return the dense operator, its eigenpairs, the sector projector and the
    minimum sector eigenvalue for one (carrier, size) fixture."""
    if kind == "D1":
        dense = kron_sum_3d(periodic_laplacian_1d(L), L)
    else:
        dense = kron_sum_3d(dirichlet_laplacian_1d(L), L)
    dense = 0.5 * (dense + dense.T)
    w, V = np.linalg.eigh(dense)
    if kind == "D1":
        # P0 sector: remove the single constant zero mode.
        nonzero = w > 1.0e-9
        min_sector = float(w[nonzero].min())
        proj = _mean_removal_projector
    else:
        min_sector = float(w.min())
        proj = _identity
    return {
        "kind": kind, "L": L, "dim": L ** 3,
        "H": sp.csr_matrix(dense), "w": w, "V": V,
        "proj": proj, "min_sector_eig": min_sector,
    }


def _identity(v: np.ndarray) -> np.ndarray:
    return v


def _mean_removal_projector(v: np.ndarray) -> np.ndarray:
    return v - v.mean()


# ------------------------------------------------------------------ source / receiver
def _torus_delta(a: int, b: int, L: int) -> int:
    d = abs(a - b)
    return min(d, L - d)


def bounded_bump(center: tuple, radius: int, L: int, periodic: bool) -> np.ndarray:
    """Bounded, non-negative source/receiver profile.

    Uses c576's own source machinery: the c576.source_profiles TRAIN_XY texture
    on the L^3 grid, restricted (windowed) to a ball of the given radius about
    `center` and made non-negative (|texture|), then normalized.  Bounded
    support = the ball; the sign of the c576 texture is dropped so the profile
    is a definite-sign localized insertion (declared).  A radius-0 window yields
    a single-site bump (used only where disjoint balls do not fit on the torus).
    """
    profiles = dict(c576.source_profiles(L, False))
    texture = profiles["TRAIN_XY"]  # explicit name lookup (no tuple-order reliance)
    grid = np.zeros((L, L, L))
    for x, y, z in iproduct(range(L), repeat=3):
        if periodic:
            dx, dy, dz = (_torus_delta(x, center[0], L),
                          _torus_delta(y, center[1], L),
                          _torus_delta(z, center[2], L))
        else:
            dx, dy, dz = x - center[0], y - center[1], z - center[2]
        if dx * dx + dy * dy + dz * dz <= radius * radius + 1.0e-9:
            grid[x, y, z] = abs(float(texture[x, y, z]))
    vec = grid.reshape(-1)
    norm = float(np.linalg.norm(vec))
    return vec / norm if norm > 0 else vec


def support(vec: np.ndarray) -> set:
    return set(int(i) for i in np.nonzero(np.abs(vec) > 1.0e-12)[0])


# ------------------------------------------------------------------ ramp / stationary
def ramp(t: float, tau: float) -> float:
    """Quartic ramp g(t)=4u^3-3u^4 (u=t/tau) on [0,tau], then hold g=1.

    C^1 at both ends (g'(0)=g'(tau)=0); g''(0)=0 removes the ramp-start endpoint
    oscillation; g''(tau)=-12/tau^2 != 0 leaves the clean tau^-2 non-adiabatic
    excitation envelope -> preregistered p=2.
    """
    if t >= tau:
        return 1.0
    u = t / tau
    return 4.0 * u ** 3 - 3.0 * u ** 4


def stationary(carrier: dict, rho_src: np.ndarray, rho_rec: np.ndarray, q: float):
    """phi* = -q H^{-1} P rho_src on the sector (mode sum, zero mode skipped);
    E_stat = q <rho_rec, phi*> = -q^2 <rho_rec, H^{-1} rho_src>.  Returns
    (E_stat, phi*, inverse_residual)."""
    w, V, proj = carrier["w"], carrier["V"], carrier["proj"]
    s = V.T @ proj(rho_src)
    inv = np.where(w > 1.0e-9, 1.0 / np.where(w > 1.0e-9, w, 1.0), 0.0)
    phistar = -q * (V @ (inv * s))
    e_stat = q * float(rho_rec @ phistar)
    resid = float(np.linalg.norm(carrier["H"] @ phistar + q * proj(rho_src)))
    return e_stat, phistar, resid


# ------------------------------------------------------------------ leapfrog
def _force(H, se: np.ndarray, q_src: float, phi: np.ndarray, gval: float) -> np.ndarray:
    return -(H @ phi + q_src * gval * se)


def executed_run(carrier: dict, rho_src: np.ndarray, rho_rec: np.ndarray,
                 q_src: float, q_rec: float, tau: float, order: str = "KDK",
                 e_stat_for_rms: float | None = None) -> dict:
    """Run the executed leapfrog update from (phi,pi)=(0,0): quartic ramp over
    [0,tau] then hold g=1 over [tau, tau+T_HOLD].  Certified response is the
    hold-mean of q_rec*<rho_rec, phi>; also returns the hold-mean bare field
    <rho_rec, phi> (contact diagnostic) and, if e_stat_for_rms is given, the RMS
    of the readout about that stationary value (the adiabatic-deviation metric).
    """
    H = carrier["H"]
    se = carrier["proj"](rho_src)
    n = carrier["dim"]
    phi = np.zeros(n)
    pi = np.zeros(n)
    N = int(round((tau + T_HOLD) / DT))
    t = 0.0
    sum_read = 0.0
    sum_bare = 0.0
    sum_sq = 0.0
    cnt = 0
    for _ in range(N):
        if order == "KDK":
            pi = pi + 0.5 * DT * _force(H, se, q_src, phi, ramp(t, tau))
            phi = phi + DT * pi
            t += DT
            pi = pi + 0.5 * DT * _force(H, se, q_src, phi, ramp(t, tau))
        else:  # DKD
            phi = phi + 0.5 * DT * pi
            pi = pi + DT * _force(H, se, q_src, phi, ramp(t + 0.5 * DT, tau))
            phi = phi + 0.5 * DT * pi
            t += DT
        if t >= tau:
            bare = float(rho_rec @ phi)
            sum_bare += bare
            sum_read += q_rec * bare
            if e_stat_for_rms is not None:
                sum_sq += (q_rec * bare - e_stat_for_rms) ** 2
            cnt += 1
    out = {
        "E_resp": sum_read / cnt,
        "bare_field": sum_bare / cnt,
        "hold_samples": cnt,
    }
    if e_stat_for_rms is not None:
        out["rms_deviation"] = math.sqrt(sum_sq / cnt)
    return out


def reversibility_frozen(carrier: dict, rho_src: np.ndarray, q: float,
                         n_steps: int) -> float:
    """Executed-update reversibility at frozen coupling g=1: integrate N steps,
    negate pi, integrate N more, negate pi, compare to the initial (0,0).  No
    dissipative or projective operation anywhere."""
    H = carrier["H"]
    se = carrier["proj"](rho_src)
    n = carrier["dim"]
    phi = np.zeros(n)
    pi = np.zeros(n)
    for _ in range(n_steps):
        pi = pi + 0.5 * DT * _force(H, se, q, phi, 1.0)
        phi = phi + DT * pi
        pi = pi + 0.5 * DT * _force(H, se, q, phi, 1.0)
    pi = -pi
    for _ in range(n_steps):
        pi = pi + 0.5 * DT * _force(H, se, q, phi, 1.0)
        phi = phi + DT * pi
        pi = pi + 0.5 * DT * _force(H, se, q, phi, 1.0)
    pi = -pi
    return float(np.linalg.norm(phi) + np.linalg.norm(pi))


def reversibility_ramp(carrier: dict, rho_src: np.ndarray, q: float,
                       tau: float) -> float:
    """Full ramped update reversibility: ramp forward over [0,tau], negate pi,
    replay the ramp schedule in reverse, negate pi, compare to (0,0)."""
    H = carrier["H"]
    se = carrier["proj"](rho_src)
    n = carrier["dim"]
    N = int(round(tau / DT))
    gvals = [ramp(i * DT, tau) for i in range(N + 1)]
    phi = np.zeros(n)
    pi = np.zeros(n)
    for i in range(N):
        pi = pi + 0.5 * DT * _force(H, se, q, phi, gvals[i])
        phi = phi + DT * pi
        pi = pi + 0.5 * DT * _force(H, se, q, phi, gvals[i + 1])
    pi = -pi
    for i in range(N):
        j = N - i
        pi = pi + 0.5 * DT * _force(H, se, q, phi, gvals[j])
        phi = phi + DT * pi
        pi = pi + 0.5 * DT * _force(H, se, q, phi, gvals[j - 1])
    pi = -pi
    return float(np.linalg.norm(phi) + np.linalg.norm(pi))


def symplectic_defect(carrier: dict) -> float:
    """Build the 2n x 2n linear part of one KDK step (source-free) and return
    ||M^T J M - J||_F -- exact symplecticity of the executed one-step map."""
    H = carrier["H"]
    n = carrier["dim"]

    def step_linear(phi, pi):
        pi = pi - 0.5 * DT * (H @ phi)
        phi = phi + DT * pi
        pi = pi - 0.5 * DT * (H @ phi)
        return phi, pi

    M = np.zeros((2 * n, 2 * n))
    for col in range(2 * n):
        phi = np.zeros(n)
        pi = np.zeros(n)
        if col < n:
            phi[col] = 1.0
        else:
            pi[col - n] = 1.0
        phi2, pi2 = step_linear(phi, pi)
        M[:n, col] = phi2
        M[n:, col] = pi2
    J = np.zeros((2 * n, 2 * n))
    J[:n, n:] = np.eye(n)
    J[n:, :n] = -np.eye(n)
    return float(np.linalg.norm(M.T @ J @ M - J))


def energy_series(carrier: dict, n_steps: int) -> dict:
    """Source-free harmonic leapfrog from a deterministic sector state; return
    the bounded relative energy band and the secular-drift fraction."""
    H = carrier["H"]
    proj = carrier["proj"]
    n = carrier["dim"]
    rng = np.random.default_rng(20260723 + carrier["L"] + (0 if carrier["kind"] == "D1" else 100))
    phi = proj(rng.standard_normal(n))
    pi = proj(rng.standard_normal(n))

    def energy(ph, p):
        return 0.5 * float(p @ p) + 0.5 * float(ph @ (H @ ph))

    e0 = energy(phi, pi)
    es = [e0]
    for _ in range(n_steps):
        pi = pi - 0.5 * DT * (H @ phi)
        phi = phi + DT * pi
        pi = pi - 0.5 * DT * (H @ phi)
        es.append(energy(phi, pi))
    es = np.asarray(es)
    band = float(es.max() - es.min())
    rel_band = band / abs(e0)
    steps = np.arange(len(es), dtype=float)
    slope = float(np.polyfit(steps, es, 1)[0])
    secular = abs(slope) * len(es)
    secular_fraction = secular / band if band > 0 else 0.0
    return {"e0": e0, "relative_band": rel_band, "secular_fraction": secular_fraction,
            "n_steps": n_steps}


# ------------------------------------------------------------------ per-fixture analysis
def analyze_fixture(kind: str, L: int) -> dict:
    carrier = build_carrier(kind, L)
    src, near, far, radius = GEOMETRY[(kind, L)]
    periodic = (kind == "D1")
    rho_src = bounded_bump(src, radius, L, periodic)
    rho_near = bounded_bump(near, radius, L, periodic)
    rho_far = bounded_bump(far, radius, L, periodic)
    overlap = support(rho_src) & support(rho_near)
    overlap_far = support(rho_src) & support(rho_far)

    q = Q_MAIN
    e_stat_near, _, inv_resid = stationary(carrier, rho_src, rho_near, q)
    e_stat_far, _, _ = stationary(carrier, rho_src, rho_far, q)

    # --- stationary identities (independent solves) ---
    e_stat_minus, _, _ = stationary(carrier, rho_src, rho_near, -q)
    sign_cancel = abs(e_stat_near - e_stat_minus)          # exactly even in q
    zero_vec = np.zeros(carrier["dim"])
    e_source_off, _, _ = stationary(carrier, zero_vec, rho_near, q)
    e_recv_zero, _, _ = stationary(carrier, rho_src, zero_vec, q)

    # --- adiabatic bridge: RMS deviation about E_stat over the hold, both orderings ---
    bridge = {"KDK": [], "DKD": []}
    means = {"KDK": [], "DKD": []}
    for tau in TAU_LADDER:
        for order in ("KDK", "DKD"):
            r = executed_run(carrier, rho_src, rho_near, q, q, tau, order,
                             e_stat_for_rms=e_stat_near)
            bridge[order].append(r["rms_deviation"])
            means[order].append(r["E_resp"])
    logt = np.log(np.asarray(TAU_LADDER))
    slope_kdk = float(np.polyfit(logt, np.log(bridge["KDK"]), 1)[0])
    slope_dkd = float(np.polyfit(logt, np.log(bridge["DKD"]), 1)[0])
    monotone = all(bridge["KDK"][i + 1] < bridge["KDK"][i]
                   for i in range(len(TAU_LADDER) - 1))
    envelope_ok = all(d * (tau ** 2) <= ENVELOPE_C
                      for d, tau in zip(bridge["KDK"], TAU_LADDER))
    # genuine convergence: the executed hold-mean approaches the independently
    # solved E_stat as tau grows (closer at tau_max than tau_min AND small there)
    mean_dev = [abs(m - e_stat_near) for m in means["KDK"]]
    mean_converges = (mean_dev[-1] < mean_dev[0]) and (mean_dev[-1] < MEAN_CONV_TOL)

    # --- ordering agreement at the probe ramp time ---
    r_kdk = executed_run(carrier, rho_src, rho_near, q, q, TAU_PROBE, "KDK")
    r_dkd = executed_run(carrier, rho_src, rho_near, q, q, TAU_PROBE, "DKD")
    order_gap = abs(r_kdk["E_resp"] - r_dkd["E_resp"])
    order_bound = ORDER_DT2_COEFF * DT ** 2

    # --- same-coupling sign law (executed) ---
    exec_plus = executed_run(carrier, rho_src, rho_near, q, q, TAU_PROBE, "KDK")
    exec_minus = executed_run(carrier, rho_src, rho_near, -q, -q, TAU_PROBE, "KDK")
    sign_invariance = abs(exec_plus["E_resp"] - exec_minus["E_resp"])   # two separate runs
    # decoupled arm (q_src=+q, q_rec=-q) executed vs -E_stat (independent solve)
    exec_dec = executed_run(carrier, rho_src, rho_near, q, -q, TAU_PROBE, "KDK")
    decouple_gap = abs(exec_dec["E_resp"] - (-e_stat_near))
    decouple_rel = decouple_gap / max(abs(e_stat_near), 1.0e-30)
    decouple_flips = (exec_dec["E_resp"] * exec_plus["E_resp"]) < 0.0
    # q_rec = 0: certified exactly zero, bare field non-zero (contact diagnostic)
    exec_rec0 = executed_run(carrier, rho_src, rho_near, q, 0.0, TAU_PROBE, "KDK")
    certified_rec0 = abs(exec_rec0["E_resp"])
    bare_contact = abs(exec_rec0["bare_field"])

    # --- q^2 scaling (three separate executed runs) ---
    scale_abs = []
    for qq in Q_SCALE:
        r = executed_run(carrier, rho_src, rho_near, qq, qq, TAU_PROBE, "KDK")
        scale_abs.append(abs(r["E_resp"]))
    scale_exponent = float(np.polyfit(np.log(np.asarray(Q_SCALE)),
                                      np.log(np.asarray(scale_abs)), 1)[0])

    # --- near / far (executed response magnitude) ---
    e_near_exec = abs(executed_run(carrier, rho_src, rho_near, q, q, TAU_PROBE, "KDK")["E_resp"])
    e_far_exec = abs(executed_run(carrier, rho_src, rho_far, q, q, TAU_PROBE, "KDK")["E_resp"])
    near_gt_far = e_near_exec > e_far_exec

    # --- reversibility / symplectic / energy ---
    rev_frozen = reversibility_frozen(carrier, rho_src, q, n_steps=int(round(TAU_PROBE / DT)))
    rev_ramp = reversibility_ramp(carrier, rho_src, q, tau=TAU_PROBE)
    symp = symplectic_defect(carrier) if L == 3 else None
    energy = energy_series(carrier, n_steps=6000)

    return {
        "fixture": f"{kind}_L{L}", "kind": kind, "L": L,
        "min_sector_eigenvalue": carrier["min_sector_eig"],
        "geometry": {"src": src, "near": near, "far": far, "ball_radius": radius},
        "support_sizes": {"src": len(support(rho_src)), "near": len(support(rho_near)),
                          "far": len(support(rho_far))},
        "supp_src_near_overlap": sorted(overlap),
        "supp_src_far_overlap": sorted(overlap_far),
        "disjoint_src_near": len(overlap) == 0,
        "disjoint_src_far": len(overlap_far) == 0,
        "E_stat_near": e_stat_near, "E_stat_far": e_stat_far,
        "stationary_inverse_residual": inv_resid,
        "sign_cancellation_residual": sign_cancel,
        "source_off_action": abs(e_source_off),
        "receiver_zero_action": abs(e_recv_zero),
        "bridge_rms_KDK": bridge["KDK"], "bridge_rms_DKD": bridge["DKD"],
        "bridge_means_KDK": means["KDK"],
        "bridge_slope_KDK": slope_kdk, "bridge_slope_DKD": slope_dkd,
        "bridge_monotone": monotone, "bridge_envelope_ok": envelope_ok,
        "bridge_mean_converges": mean_converges, "bridge_mean_dev": mean_dev,
        "order_gap": order_gap, "order_bound": order_bound,
        "sign_invariance_residual": sign_invariance,
        "decouple_gap": decouple_gap, "decouple_rel": decouple_rel,
        "decouple_flips": decouple_flips,
        "E_dec_executed": exec_dec["E_resp"], "E_same_executed": exec_plus["E_resp"],
        "qrec0_certified": certified_rec0, "qrec0_bare_contact": bare_contact,
        "scale_abs": scale_abs, "scale_exponent": scale_exponent,
        "E_near_exec": e_near_exec, "E_far_exec": e_far_exec, "near_gt_far": near_gt_far,
        "reversibility_frozen": rev_frozen, "reversibility_ramp": rev_ramp,
        "symplectic_defect": symp,
        "energy_relative_band": energy["relative_band"],
        "energy_secular_fraction": energy["secular_fraction"],
    }


# ------------------------------------------------------------------ anchors
def anchor_report(fixtures: dict) -> dict:
    """Reproduce the transcribed Cycle-626 anchor eigenvalues on matching
    fixtures; flag any that cannot be reproduced as a DECLARED DIVERGENCE."""
    d1 = {L: fixtures[("D1", L)]["min_sector_eigenvalue"] for L in SIZES}
    d2 = {L: fixtures[("D2", L)]["min_sector_eigenvalue"] for L in SIZES}
    # D1 anchor 0.753 belongs to L7 by construction: 2(1-cos 2pi/7).
    d1_anchor_L = 7
    d1_anchor_ok = abs(d1[d1_anchor_L] - PINS["c626_periodic_min_nonzero"]) < ANCHOR_TOL
    d2_anchor_ok = {L: abs(d2[L] - PINS["c626_dirichlet_min"][str(L)]) < ANCHOR_TOL
                    for L in SIZES}
    divergences = []
    if not d1_anchor_ok:
        divergences.append({"fixture": "D1_L7", "constructed": d1[7],
                            "anchor": PINS["c626_periodic_min_nonzero"]})
    for L in SIZES:
        if not d2_anchor_ok[L]:
            divergences.append({"fixture": f"D2_L{L}", "constructed": d2[L],
                                "anchor": PINS["c626_dirichlet_min"][str(L)]})
    return {
        "D1_periodic_min_nonzero": d1, "D2_dirichlet_min": d2,
        "D1_anchor_size": d1_anchor_L, "D1_anchor_ok": d1_anchor_ok,
        "D2_anchor_ok": d2_anchor_ok,
        "all_anchors_reproduced": d1_anchor_ok and all(d2_anchor_ok.values()),
        "declared_divergences": divergences,
    }


def declared_divergences(fixtures: dict) -> dict:
    """D1 (periodic) near/far antipode-peaking is a declared divergence, not a
    hard gate: report each and confirm they are all on the periodic carrier."""
    rows = []
    for L in SIZES:
        f = fixtures[("D1", L)]
        rows.append({"fixture": f["fixture"], "E_near_exec": f["E_near_exec"],
                     "E_far_exec": f["E_far_exec"], "near_gt_far": f["near_gt_far"]})
    return {
        "reason": (
            "On the compact 3-torus the zero-mode-removed (P0) Green's function is "
            "antipode-peaked (commute-time / heat-kernel-on-torus structure): |response| "
            "does not decay monotonically with displacement, so the near/far LOCALITY "
            "gate is ill-posed on the periodic carrier and is reported as a diagnostic, "
            "not certified.  The open Dirichlet carrier D2 carries the near/far hard gate."
        ),
        "rows": rows,
    }


def inventory() -> dict:
    return {
        "supplied": (
            "c576 periodic L3/L6/L7 cubic site graph and its source_profiles texture machinery",
            "two declared carriers (periodic P0 graph Laplacian; open Dirichlet FD Laplacian)",
            "bounded non-negative disjoint source/receiver supports and their frozen displacements",
            "one physical coupling q wired to both source insertion and receiver readout",
            "quartic ramp 4u^3-3u^4, fixed hold window, leapfrog step, KDK/DKD orderings",
            "geometric ramp-time ladder, preregistered adiabatic rate p=2 and tolerances",
            "transcribed Cycle-626 comparator eigenvalues and stationary identities",
        ),
        "derived": (
            "exact reproduction of the transcribed c626 periodic and Dirichlet anchor eigenvalues",
            "exactly reversible symplectic executed update (frozen and schedule-reversed)",
            "adiabatic bridge: executed response's residual oscillation about E_stat decays as tau^-2",
            "same-coupling even-ness in q; decoupled arm sign flip; receiver-zero null response",
            "measured q^2 response scaling without refit",
            "open-carrier near/far locality; declared periodic-carrier antipode divergence",
            "kick/drift ordering agreement within the O(dt^2) bound sharing one adiabatic limit",
        ),
        "open": (
            "selection/derivation of the carriers, ramp, coupling q, supports and grids",
            "physical energy/stress/source/gravity identification (explicitly NOT claimed)",
            "the finite-Weyl NQ carrier join (c607/c609) and any open-real-space coframe K",
            "continuum, nonlinear and strong-field extensions; endogenous source law",
        ),
    }


# ------------------------------------------------------------------ main
def main() -> int:
    started = perf_counter()
    print("SAME-COUPLING EXECUTED FIELD-UPDATE RESPONSE TOURNAMENT (SPEC B draft)")
    print("authority", AUTHORITY, "audit", AUDIT, "cycle_claim", CYCLE_CLAIM)

    # --- provenance: re-hash the landed c576 runner, note and receipt pins ---
    c576_path = ROOT / "scripts" / "physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py"
    c576_note_path = ROOT / (
        "docs/work_history/repo/review_feedback/"
        "PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md")
    c576_receipt_path = ROOT / (
        "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json")
    c576_sha = file_sha(c576_path)
    c576_note_sha = file_sha(c576_note_path) if c576_note_path.exists() else "MISSING"
    c576_receipt_sha = file_sha(c576_receipt_path) if c576_receipt_path.exists() else "MISSING"
    check("c576 imported runner, note and receipt all match their pinned sha256",
          c576_sha == PINS["c576_script"] and c576_note_sha == PINS["c576_note"]
          and c576_receipt_sha == PINS["c576_receipt"],
          {"script": c576_sha == PINS["c576_script"],
           "note": c576_note_sha == PINS["c576_note"],
           "receipt": c576_receipt_sha == PINS["c576_receipt"]})

    # --- the paired note must exist with its firewall clauses (checked on disk) ---
    required_note_clauses = (
        "authority: none", "audit: unset", "same-coupling", "executed",
        "reversible", "adiabatic", "not energy", "not gravity", "not stress",
        "declared divergence", "supplied", "open", "no new axiom",
    )
    note_present = NOTE.exists()
    note_body = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if note_present else ""
    note_missing = tuple(cl for cl in required_note_clauses if cl not in note_body)
    check("paired note present on disk with all firewall clauses",
          note_present and not note_missing,
          {"present": note_present, "missing": note_missing})

    fixtures = {(kind, L): analyze_fixture(kind, L)
                for kind in ("D1", "D2") for L in SIZES}
    anchors = anchor_report(fixtures)
    divergence = declared_divergences(fixtures)
    supplied = inventory()

    # --- gate 2 / F4: transcribed anchor eigenvalues + positivity ---
    check("D1 periodic P0 min-nonzero anchor 0.753 reproduced at L7 (by construction)",
          anchors["D1_anchor_ok"] and not anchors["declared_divergences"],
          {"D1_min_nonzero": anchors["D1_periodic_min_nonzero"], "anchor_size": 7})
    check("D2 open Dirichlet min-eigenvalue anchors 1.757/0.594/0.457 reproduced on L3/L6/L7",
          all(anchors["D2_anchor_ok"].values()),
          {"D2_min": anchors["D2_dirichlet_min"], "anchors": PINS["c626_dirichlet_min"]})
    check("both carriers strictly positive on the tested sector, all three sizes",
          all(fixtures[(k, L)]["min_sector_eigenvalue"] > POSITIVITY_MARGIN
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": fixtures[(k, L)]["min_sector_eigenvalue"]
           for k in ("D1", "D2") for L in SIZES})

    # --- disjoint (no-contact) supports ---
    check("source and receiver supports are disjoint (supp(rho_src) cap supp(rho_rec) = empty)",
          all(fixtures[(k, L)]["disjoint_src_near"] and fixtures[(k, L)]["disjoint_src_far"]
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": fixtures[(k, L)]["support_sizes"] for k in ("D1", "D2") for L in SIZES})

    # --- gate 1 / F3: reversibility + symplectic + bounded energy ---
    check("executed update exactly reversible at frozen coupling (forward/negate/back/negate)",
          all(fixtures[(k, L)]["reversibility_frozen"] < REVERSIBILITY_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": fixtures[(k, L)]["reversibility_frozen"]
           for k in ("D1", "D2") for L in SIZES})
    check("full ramped update reversible under schedule reversal to the machine-tight bound",
          all(fixtures[(k, L)]["reversibility_ramp"] < REVERSIBILITY_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": fixtures[(k, L)]["reversibility_ramp"]
           for k in ("D1", "D2") for L in SIZES})
    check("one-step executed map is exactly symplectic (||M^T J M - J|| ~ machine) on L3",
          all(fixtures[(k, 3)]["symplectic_defect"] < SYMPLECTIC_TOL for k in ("D1", "D2")),
          {f"{k}_L3": fixtures[(k, 3)]["symplectic_defect"] for k in ("D1", "D2")})
    check("shadow energy stays in a bounded band with no secular trend (frozen g, source-free)",
          all(fixtures[(k, L)]["energy_relative_band"] < ENERGY_DRIFT_TOL
              and fixtures[(k, L)]["energy_secular_fraction"] < SECULAR_FRACTION_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": (round(fixtures[(k, L)]["energy_relative_band"], 6),
                         round(fixtures[(k, L)]["energy_secular_fraction"], 4))
           for k in ("D1", "D2") for L in SIZES})

    # --- stationary identities (independent solves) ---
    check("stationary inverse residual ||H phi* + q P rho_src|| <= machine-tight on every fixture",
          all(fixtures[(k, L)]["stationary_inverse_residual"] < INVERSE_RESID_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": fixtures[(k, L)]["stationary_inverse_residual"]
           for k in ("D1", "D2") for L in SIZES})
    check("stationary sign cancellation exact: E_stat(q) = E_stat(-q) (both vertices, two solves)",
          all(fixtures[(k, L)]["sign_cancellation_residual"] < EXACT_ZERO_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": fixtures[(k, L)]["sign_cancellation_residual"]
           for k in ("D1", "D2") for L in SIZES})
    check("source-off and receiver-zero stationary actions are exactly zero",
          all(fixtures[(k, L)]["source_off_action"] < EXACT_ZERO_TOL
              and fixtures[(k, L)]["receiver_zero_action"] < EXACT_ZERO_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": (fixtures[(k, L)]["source_off_action"],
                         fixtures[(k, L)]["receiver_zero_action"])
           for k in ("D1", "D2") for L in SIZES})

    # --- gate 3 / F2: adiabatic bridge, per fixture ---
    for k in ("D1", "D2"):
        for L in SIZES:
            f = fixtures[(k, L)]
            check(
                f"adiabatic bridge {f['fixture']}: RMS(response about E_stat) ~ tau^-2 "
                f"(p={PREREGISTERED_P}), monotone, envelope-bounded, mean converges, no refit",
                abs(f["bridge_slope_KDK"] - (-PREREGISTERED_P)) < P_TOL
                and f["bridge_monotone"] and f["bridge_envelope_ok"]
                and f["bridge_mean_converges"],
                {"slope_KDK": round(f["bridge_slope_KDK"], 4),
                 "rms": [f"{d:.2e}" for d in f["bridge_rms_KDK"]],
                 "envelope_ok": f["bridge_envelope_ok"],
                 "mean_converges": f["bridge_mean_converges"]},
            )

    # --- gate 4 / F1: same-coupling sign law ---
    check("q -> -q leaves the EXECUTED response invariant (exactly even; two separate runs)",
          all(fixtures[(k, L)]["sign_invariance_residual"] < SIGN_INVARIANCE_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": fixtures[(k, L)]["sign_invariance_residual"]
           for k in ("D1", "D2") for L in SIZES})
    check("F1 decoupled arm (q_src=+q, q_rec=-q) flips the sign; magnitude = -E_stat (independent)",
          all(fixtures[(k, L)]["decouple_flips"]
              and fixtures[(k, L)]["decouple_rel"] < DECOUPLE_REL_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": {"E_dec": fixtures[(k, L)]["E_dec_executed"],
                         "E_same": fixtures[(k, L)]["E_same_executed"],
                         "rel_to_minus_Estat": round(fixtures[(k, L)]["decouple_rel"], 6)}
           for k in ("D1", "D2") for L in SIZES})
    check("q_rec=0 certified response is exactly zero WHILE the bare contact field is nonzero "
          "(diagnostic only, firewalled)",
          all(fixtures[(k, L)]["qrec0_certified"] < EXACT_ZERO_TOL
              and fixtures[(k, L)]["qrec0_bare_contact"] > SIGNAL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": {"certified": fixtures[(k, L)]["qrec0_certified"],
                         "bare_contact": fixtures[(k, L)]["qrec0_bare_contact"]}
           for k in ("D1", "D2") for L in SIZES})

    # --- gate 5: q^2 scaling ---
    check("executed response scales as q^2 (measured exponent within tolerance, no refit)",
          all(abs(fixtures[(k, L)]["scale_exponent"] - 2.0) < SCALE_EXP_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": round(fixtures[(k, L)]["scale_exponent"], 4)
           for k in ("D1", "D2") for L in SIZES})

    # --- gate 6 / F5: near/far on the well-posed (open) carrier ---
    check("near-source executed response exceeds the frozen far control on the open carrier, all sizes",
          all(fixtures[(k, L)]["near_gt_far"] for k in NEARFAR_HARD_GATE for L in SIZES),
          {f"D2_L{L}": {"near": fixtures[("D2", L)]["E_near_exec"],
                        "far": fixtures[("D2", L)]["E_far_exec"]} for L in SIZES})

    # --- gate 7 / F6: kick/drift ordering ---
    check("F6 kick/drift orderings agree within the O(dt^2) bound at the probe ramp time",
          all(fixtures[(k, L)]["order_gap"] <= fixtures[(k, L)]["order_bound"]
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": {"gap": fixtures[(k, L)]["order_gap"],
                         "bound": fixtures[(k, L)]["order_bound"]}
           for k in ("D1", "D2") for L in SIZES})
    check("kick/drift orderings share one adiabatic limit (both bridge slopes ~ -p)",
          all(abs(fixtures[(k, L)]["bridge_slope_DKD"] - (-PREREGISTERED_P)) < P_TOL
              for k in ("D1", "D2") for L in SIZES),
          {f"{k}_L{L}": round(fixtures[(k, L)]["bridge_slope_DKD"], 4)
           for k in ("D1", "D2") for L in SIZES})

    # --- claim boundaries / inventory: written to the receipt VERBATIM below.
    # Deliberately NOT check() rows: a constant-vs-constant assertion on the
    # runner's own hardcoded firewall/inventory literals cannot fail and would
    # be PASS-count padding (the defect class disclosed for the vendored
    # substrate). The externally-anchored guard is the on-disk note-contract
    # row above; the receipt carries the firewalls, claim boundaries and
    # inventory for the reviewer.

    # --- resources / receipt ---
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = peak / (1024 ** 2) if sys.platform == "darwin" else peak / 1024

    def jsonable(obj):
        if isinstance(obj, dict):
            return {str(k): jsonable(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [jsonable(v) for v in obj]
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, (np.integer,)):
            return int(obj)
        return obj

    receipt = {
        "cycle_claim": CYCLE_CLAIM,
        "date": DATE, "authority": AUTHORITY, "audit": AUDIT,
        "runner_role": "bounded drafting worker output; supervisor owns all verdicts",
        "c576_runner_sha256_observed": c576_sha,
        "pins": PINS,
        "c579_imported": False,
        "tolerances": {
            "REVERSIBILITY_TOL": REVERSIBILITY_TOL, "SYMPLECTIC_TOL": SYMPLECTIC_TOL,
            "INVERSE_RESID_TOL": INVERSE_RESID_TOL, "ANCHOR_TOL": ANCHOR_TOL,
            "EXACT_ZERO_TOL": EXACT_ZERO_TOL, "SIGNAL": SIGNAL,
            "SIGN_INVARIANCE_TOL": SIGN_INVARIANCE_TOL, "DECOUPLE_REL_TOL": DECOUPLE_REL_TOL,
            "SCALE_EXP_TOL": SCALE_EXP_TOL, "P_TOL": P_TOL, "ENVELOPE_C": ENVELOPE_C,
            "ORDER_DT2_COEFF": ORDER_DT2_COEFF, "ENERGY_DRIFT_TOL": ENERGY_DRIFT_TOL,
            "SECULAR_FRACTION_TOL": SECULAR_FRACTION_TOL, "POSITIVITY_MARGIN": POSITIVITY_MARGIN,
        },
        "dynamics": {
            "integrator": "leapfrog / Stormer-Verlet (KDK and DKD)", "dt": DT,
            "ramp": "quartic 4u^3-3u^4 on [0,tau] (g''(0)=0, g''(tau)!=0), then hold g=1",
            "hold_window": T_HOLD, "tau_ladder": list(TAU_LADDER),
            "preregistered_rate_p": PREREGISTERED_P,
            "bridge_observable": "RMS over hold of (q<rho_rec,phi> - E_stat); executed hold-mean is E_resp",
            "coupling_wiring": "single scalar q enters BOTH source insertion and receiver readout",
        },
        "anchors": jsonable(anchors),
        "declared_divergences_near_far_periodic": jsonable(divergence),
        "fixtures": {f"{k}_L{L}": jsonable(fixtures[(k, L)])
                     for k in ("D1", "D2") for L in SIZES},
        "inventory": jsonable(supplied),
        "claim_boundaries": CLAIM_BOUNDARIES,
        "interpretation_firewall": FIREWALLS,
        "acceptance_duties": ACCEPTANCE_DUTIES,
        "preregistered_falsifiers": {
            "F1": "decoupled arm fails to flip -> FAIL",
            "F2": "adiabatic convergence violates frozen p=2 -> FAIL",
            "F3": "reversibility recovery exceeds machine-tight bound -> FAIL",
            "F4": "anchor eigenvalue mismatches with no declared divergence -> FAIL",
            "F5": "near/far inverts where well-posed (open carrier) -> FAIL",
            "F6": "kick/drift disagree beyond O(dt^2) -> FAIL",
        },
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
        "tests_passed": PASS, "tests_total": PASS + FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=1, sort_keys=True))

    print("SUMMARY_JSON", json.dumps({
        "authority": AUTHORITY, "audit": AUDIT, "cycle_claim": CYCLE_CLAIM,
        "anchors_reproduced": anchors["all_anchors_reproduced"],
        "bridge_slopes": {f"{k}_L{L}": round(fixtures[(k, L)]["bridge_slope_KDK"], 4)
                          for k in ("D1", "D2") for L in SIZES},
        "scale_exponents": {f"{k}_L{L}": round(fixtures[(k, L)]["scale_exponent"], 4)
                            for k in ("D1", "D2") for L in SIZES},
        "passes": PASS, "failures": FAIL,
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
    }, sort_keys=True))

    if FAIL == 0:
        print("RESULT SAME_COUPLING_EXECUTED_FIELD_UPDATE_RESPONSE_BRIDGE_POSITIVE", str(RECEIPT_PATH))
        return 0
    print("RESULT SAME_COUPLING_EXECUTED_FIELD_UPDATE_RESPONSE_TOURNAMENT_FAILED", str(RECEIPT_PATH))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
