#!/usr/bin/env python3
"""Finite-valued norm/saturation arithmetic and reversible-oracle tournament.

Descriptive filename target (NO cycle number in filenames; owner directive):
    scripts/physical_finite_reversible_norm_saturation_evaluator_tournament_2026_07_23.py

Frozen question (SPEC A). How much of the continuous arithmetic of the campaign
Cycle-626 Route-A normalizer and Route-B saturation can be replaced by executed
finite-valued arithmetic on a declared value lattice, with an exact reversible
oracle embedding on the value-basis code space, all-24-frame covariance,
support-two lowering of the output-register rotations, and a certified
quantization bound against the continuous reference evaluated on the actual
landed Cycle-576 deficits, without changing the exact-pinned, audit-unset
actuation interface and without selecting any sign, scale, regulator, or
receiver association?

This is a repo-side CONSTRUCTIVE evaluator tournament. It imports the landed
Cycle-576 module read-only (pinned sha256), builds the 24-frame deficit orbit
from c576 `source_profiles` under the c576 real-space frame idiom, and runs a
finite integer normalizer + an exact-rational saturation, with an explicitly
materialized reversible oracle permutation, covariance, a derived quantization
bound, and the c626 actuation endpoint comparison. It does not compile the
reciprocal-square-root control logic or Route-B arithmetic into a gate-level
reversible circuit. Every check row is a COMPUTED condition.

Firewalls (interpretation guards; also written to the receipt):
- Constructive finite-arithmetic and reversible-oracle support ON THE DECLARED
  LATTICES ONLY; the full gate-level finite-evaluator compiler, arbitrary-
  precision evaluator, and continuum evaluator remain open.
- No sign, scale, regulator, saturation-scale, lambda, or c is selected; the
  full grid survives; branch selection remains open.
- No shared-code 3/4 DELAY association is derived; the PR5557 acceptance harness
  is untouched; the 5/4 ADVANCE count-edit interface is not driven.
- No energy, stress, source, gravity, causal-rate, event, Record, or Born claim.
  A contact-sensitive response is not energy, stress, source, or gravity.
- The value lattice, FLOOR, register widths, and grid are DECLARED SUPPLIED
  STRUCTURE. No new axiom, primitive, or premise class is introduced.

Acceptance duties (for the supervisor, who owns all verdicts):
- review every row line-by-line; the worker synthesizes no final verdict and
  sets no cycle claim (CYCLE_CLAIM is a None placeholder set at freeze);
- supervisor rulings applied (2026-07-23): lambda is INPUT-SIDE per the c626
  member loop; the improvement axis c is DECLARED-ABSENT (c620 unlanded); the
  E2 r0/rho values are declared fixture constants; population curation and the
  micro permutation-matrix scale are accepted and declared;
- the note at the declared path is REQUIRED at run time with all firewall
  clauses present (row 02).

Preregistered falsifiers (each maps to a named FAIL row):
- F1 garbage-retention: an uncompute-skipping variant MUST fail ancilla
  cleanliness with a nonzero garbage witness on a superposition (row PASSES
  when the probe FAILS). This probe does not claim entanglement when both
  selected inputs carry the same retained accumulator value.
- F2 irreversibility: a truncating variant without disambiguating ancilla MUST
  produce an explicit collision-pair witness in the bijection check.
- F3 zero-branch: the all-zero orbit through the FULL circuit yields exactly
  zero output for eps=0.
- F4 below-floor refusal: a nonzero orbit below FLOOR is refused with a witness.
- F5 no-refit: a single frozen TOL table; no tolerance value carries two
  meanings; FLOOR/grids/bound constants are frozen at the top.

python3 + numpy/scipy exactly as c576 uses them; fractions.Fraction for exact
rational rows. No git/subprocess/network. The runner writes its own receipt JSON
and exits decisively (return 0 iff FAIL == 0).
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import sys
from time import perf_counter

import numpy as np
from scipy.linalg import expm
from scipy.sparse import csr_matrix, eye as sparse_eye


# ---------------------------------------------------------------------------
# Repo location and the single landed import (pinned).
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as c576  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen header constants (supervisor sets the final cycle claim at freeze).
# ---------------------------------------------------------------------------
CYCLE_CLAIM = 680  # frozen 2026-07-23: joint visible max at re-fetch was 679
#                    (our PR #5563 claim; campaign tip fb0ab5636e filenames
#                    reach 678). Descriptive filenames per owner directive;
#                    the claim lives here and in the receipt/note only.
AUTHORITY = "none"
AUDIT = "unset"
DATE = "2026-07-23"

RECEIPT_PATH = ROOT / "outputs" / (
    "physical_finite_reversible_norm_saturation_evaluator_tournament_"
    "receipt_2026_07_23.json"
)
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / (
    "PHYSICAL_FINITE_REVERSIBLE_NORM_SATURATION_EVALUATOR_TOURNAMENT_"
    "NOTE_2026-07-23.md"
)

# Pin block (verified at preflight against disk).
PINS = {
    "c576_files": {
        "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
            "7980bff1293202656afeefb46c7c7dcf8145e748004b541d3619f19896c79ea7",
        "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md":
            "5822c14b74de606d302beb637e03dd0a30968e6a7bf120723eb3da16e09e6768",
        "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":
            "bc719ca8d88662e082fd63db8f524d9af94749012208b5a76f2ea6200f305c3a",
    },
    # Read-only campaign evidence anchors: transcribed, NEVER read from disk,
    # never imported. Context anchors for the note and coarse consistency only;
    # the runner's own claims rest on its own computations on landed bytes.
    "campaign_anchors": {
        "campaign_head": "fb0ab5636e557d8de1da8e643f419867ae69197a",
        "c626_note": "1346e9c5aec6206642e64059eeff0b49d59df33f8fe0584c7c8537d3e2760893",
        "c626_runner": "a775cb759ebd4a54ca4707dd99540256658d5f70315afbb6685058fd568911cf",
        "c626_receipt": "ab8489e9875e362d2b496b1f92464e6c5c642eb3cdb72b1755e77c4d70b752f6",
        "route_a_min_endpoint_deletion": 0.0106,
        "route_a_all24_covariance_residual": 1.22e-15,
        "route_a_inverse_residual": 6.69e-16,
        "route_a_unitarity_residual": 3.09e-15,
        "route_a_both_quadrature_signs_occur": True,
        "route_b_max_fixed_point_residual": 3.55e-15,
        "route_b_pointwise_inverse_residual": 3.14e-16,
        "route_b_min_feedback_deletion": 0.0378,
    },
}

# ----- Value lattice (declared supplied structure) -----
Q_SIZES = (64, 256)                 # L_Q = { k/Q : |k| <= K_MAX }
K_MAX_FACTOR = 2                    # K_MAX(Q) = K_MAX_FACTOR * Q  (|d| <= 2)
FLOOR = 0.1                        # lattice-norm floor; below curated min data norm, above 1/Q
N_FRAMES = 24

# regulator grid eps in {0, 1/2, 1, 2} as exact rationals (eQ = eps*Q integer, Q even)
EPS_GRID = (Fraction(0), Fraction(1, 2), Fraction(1, 1), Fraction(2, 1))

# ----- input population (curated; see design_memo_A.md deviation D1) -----
POP_LENGTHS = (3, 6, 7)                                 # L3 / L6 / L7
POP_PROFILE_NAMES = ("TRAIN_XY", "TRAIN_DIAGONAL", "BLINDED_HELD_OBLIQUE")
POP_SITES = ((2, 1, 0), (3, 1, 0), (2, 1, 3))          # asymmetric declared sites (mod L)

# ----- E2 saturation grid (declared supplied rational structure) -----
E2_SIGMA = (-1, 1)
E2_KAPPA = (Fraction(1, 2), Fraction(1, 1), Fraction(2, 1))
E2_ALPHA = (Fraction(1, 2), Fraction(1, 1), Fraction(2, 1))
E2_R0 = Fraction(3, 10)            # declared fixture value (see uncertainty U3)
E2_RHO = Fraction(-1, 5)           # declared fixture value (see uncertainty U3)
E2_D0 = 10                         # common denominator of r-grid, r0, rho
E2_RGRID = tuple(Fraction(t, 10) for t in range(-20, 21))
# Write r=t/10, rho=-2/10, n=t+2, alpha=A/2, kappa=K/2 with
# A,K in {1,2,4}.  The nonlinear term has raw denominator
# 2(20+A|n|), so after adding r0=3/10 the reduced denominator divides
# lcm(10, 2(20+A|n|)).  This is an analytic upper bound independent of
# the saturation implementation under test; its maximum on the frozen grid is
# 1080.  (The exact output census below observes the sharper reduced maximum.)
E2_U_NUMS = tuple(t + 2 for t in range(-20, 21))
E2_ALPHA_TWICE = (1, 2, 4)
E2_DEN_BOUND = max(
    math.lcm(E2_D0, 2 * (2 * E2_D0 + A * abs(n)))
    for A in E2_ALPHA_TWICE
    for n in E2_U_NUMS
)

# ----- actuation grid (unchanged c626 Route-A interface) -----
ACT_B = 0.17                       # reuse c576 SOURCE_COUPLING magnitude
ACT_T = 0.7                        # evolution parameter (declared)
ACT_KAPPA = (Fraction(1, 2), Fraction(1, 1), Fraction(2, 1))
ACT_SIGMA = (-1, 1)
# lambda enters INPUT-SIDE, faithful to the c626 member loop
# (coupling = lambda_sign*lambda_magnitude*SOURCE_COUPLING multiplies the base
# feeding the orbit BEFORE normalization; magnitude cancels only for eps=0).
ACT_LAM_SIGN = (-1, 1)
ACT_LAM_MAG = (Fraction(1, 2), Fraction(1, 1))
# improvement axis c: DECLARED-ABSENT off main. c626's improvement vector is
# c620.spatial_trace_vector() @ q from the UNLANDED Cycle-620 module; there is
# no landed byte source for it, so the c grid is not executable here. The axis
# is recorded as {0} with this rationale in the contract; no substitute
# semantics (e.g. endpoint detuning) are invented.
ACT_C = (0,)
ACT_N_ORBITS = 3                   # thinning: one representative orbit per length (declared)
SWAP_BUDGET_CAP = 10_000_000       # declared full-instance support-two word cap

# ----- micro fully-materialised permutation-matrix instance (memo section 4) -----
MICRO_Q = 4
MICRO_ALPHABET = (-1, 0, 1)
MICRO_MSET = (0, 1, 2, 3)          # M = sum k^2, k in {-1,0,1}, 3 registers

# ----- reduced fixture (spec: 3 frame registers, Q=16) -----
REDUCED_Q = 16
REDUCED_ALPHABET = (-1, 0, 1)

SEED = 20260723

# ----- single frozen TOL registry (F5: no tolerance carries two meanings) -----
TOL = {
    "float_match": 1.0e-9,       # generic float equality (expm endpoints, linearity)
    "signal": 1.0e-6,            # deletion-sensitivity signal floor
    "bound_slack": 1.0e-12,      # float slack when checking a <= B inequalities
    "tightness_ratio": 1.0 / 8,  # informativeness: max observed >= B * tightness_ratio
    "scaling_factor": 16.0,      # observed-max Q-ratio must lie within this factor
}


# ---------------------------------------------------------------------------
# Harness.
# ---------------------------------------------------------------------------
PASS = 0
FAIL = 0
ROWS: list[dict] = []


def check(label: str, condition: object, detail: object = "") -> bool:
    global PASS, FAIL
    cond = bool(condition)
    if cond:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)
    ROWS.append({"label": label, "pass": cond, "detail": str(detail)[:400]})
    return cond


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Certified integer reciprocal-sqrt-multiply (no float in the certificate).
# a = round(B / sqrt(M)) for non-negative ints B, M>0, certified by integer
# inequalities (memo section 0): 4B^2 < (2a+1)^2 M and (a==0 or (2a-1)^2 M <= 4B^2).
# ---------------------------------------------------------------------------
def cert_ok(a: int, B: int, M: int) -> bool:
    if a < 0:
        return False
    right = 4 * B * B < (2 * a + 1) ** 2 * M
    left = (a == 0) or ((2 * a - 1) ** 2 * M <= 4 * B * B)
    return bool(right and left)


def certified_round(B: int, M: int) -> tuple[int, bool]:
    if M <= 0:
        raise ValueError("certified_round requires M > 0")
    if B == 0:
        return 0, cert_ok(0, 0, M)
    cand = math.isqrt((B * B) // M)
    for a in (cand - 1, cand, cand + 1, cand + 2):
        if a >= 0 and cert_ok(a, B, M):
            return a, True
    return cand, False


# ---------------------------------------------------------------------------
# Executed finite normalizer with an exact reversible-oracle embedding.
# Input numerators k are retained; the explicitly represented (sq, M) work
# registers are restored to 0; output is written by modular add into result
# registers (m = 2Q+1). The reciprocal-square-root selection is evaluated by
# certified_round but is not itself compiled into reversible primitive gates.
# Returns the output numerators, the represented post-uncompute ancilla
# residual (0 == clean), an explicit-operation trace, and info.
# ---------------------------------------------------------------------------
def reversible_normalize(k: list[int], Q: int, eQ: int, keep_garbage: bool = False):
    n = len(k)
    m = 2 * Q + 1
    trace: list[str] = []
    sq = [0] * n
    Msum = 0
    # compute k^2 into sq (starts 0)
    for i in range(n):
        sq[i] += k[i] * k[i]
        trace.append("squarer")
    # accumulate M = sum sq + eQ^2
    for i in range(n):
        Msum += sq[i]
        trace.append("acc_add")
    Msum += eQ * eQ
    trace.append("acc_add_const")
    # result registers, written by modular add
    r = [0] * n
    zero_branch = (Msum == 0)
    cert_all = True
    if not zero_branch:
        for i in range(n):
            a, ok = certified_round(Q * abs(k[i]), Msum)
            cert_all = cert_all and ok
            j = a if k[i] >= 0 else -a
            r[i] = (r[i] + (j % m)) % m
            trace.append("add_mod")
    # uncompute ancilla back to 0 (Bennett) unless the garbage probe is active
    if not keep_garbage:
        Msum -= eQ * eQ
        trace.append("acc_add_const_inv")
        for i in range(n):
            Msum -= sq[i]
            trace.append("acc_add_inv")
        for i in range(n):
            sq[i] -= k[i] * k[i]
            trace.append("squarer_inv")
    anc_residual = max([abs(Msum)] + [abs(x) for x in sq])
    j_out = [(r[i] if r[i] <= Q else r[i] - m) for i in range(n)]
    info = {"M_after": Msum, "sq_after": list(sq), "zero_branch": zero_branch,
            "cert_all": cert_all}
    return j_out, anc_residual, trace, info


def finite_normalize(k: list[int], Q: int, eQ: int) -> list[int]:
    return reversible_normalize(k, Q, eQ)[0]


def continuous_reference(d_true: np.ndarray, eps: float) -> np.ndarray:
    S = math.sqrt(float(d_true @ d_true) + eps * eps)
    if S == 0.0:
        return np.zeros_like(d_true)
    return d_true / S


def q_round(x: float) -> int:
    return int(math.floor(x + 0.5))


def quantize(d_true: np.ndarray, Q: int, K_max: int) -> list[int]:
    out = []
    for x in d_true:
        k = q_round(float(x) * Q)
        k = max(-K_max, min(K_max, k))
        out.append(int(k))
    return out


# ---------------------------------------------------------------------------
# 24-frame label permutations, EXTRACTED from c576.frame_sector_permutation.
# ---------------------------------------------------------------------------
FRAMES = c576.FRAMES


def extract_label_perm(frame: np.ndarray) -> list[int]:
    mat = c576.frame_sector_permutation(frame)  # (1 + 24*15) square permutation
    perm = [0] * 24
    for old in range(24):
        col = 1 + 15 * old  # first component of old sector
        rows = np.where(mat[:, col] == 1)[0]
        perm[old] = (int(rows[0]) - 1) // 15
    return perm


LABEL_PERMS = [extract_label_perm(f) for f in FRAMES]


def apply_perm(vec: list, perm: list[int]) -> list:
    # active rotation: (P vec)[perm[old]] = vec[old]
    out = [None] * len(vec)
    for old, val in enumerate(vec):
        out[perm[old]] = val
    return out


def compose_perm(p: list[int], q: list[int]) -> list[int]:
    return [p[q[i]] for i in range(len(q))]


# ---------------------------------------------------------------------------
# Input population: c576 real-space source field over the 24-frame orbit of a
# fixed declared site (rotate_profile idiom; memo deviation D3).
# ---------------------------------------------------------------------------
def orbit_at_site(profile: np.ndarray, site: tuple[int, int, int]) -> np.ndarray:
    L = profile.shape[0]
    s = np.asarray([c % L for c in site])
    vals = []
    for f in FRAMES:
        src = tuple(int(round(v)) % L for v in f.T @ s)  # F^{-1} s = F^T s (orthogonal)
        vals.append(float(profile[src]))
    return np.asarray(vals, dtype=float)


def build_population() -> list[dict]:
    pop = []
    seen = set()
    for L in POP_LENGTHS:
        profiles = dict(c576.source_profiles(L, False)) | dict(c576.source_profiles(L, True))
        for name in POP_PROFILE_NAMES:
            if name not in profiles:
                continue
            prof = profiles[name]
            for site in POP_SITES:
                d = orbit_at_site(prof, site)
                nrm = float(np.linalg.norm(d))
                key = tuple(np.round(d, 12))
                if nrm < FLOOR or key in seen:
                    continue
                seen.add(key)
                pop.append({"label": f"L{L}:{name}:{site}", "d": d, "norm": nrm})
    return pop


# ---------------------------------------------------------------------------
# Micro fully-materialised integer permutation matrices (clean + F1 retention).
# Basis index over (input k in {-1,0,1}^3) x (result in Z_m^3) x (M in MSET).
# ---------------------------------------------------------------------------
def micro_build():
    n = 3
    m = 2 * MICRO_Q + 1
    n_res = m ** n
    n_M = len(MICRO_MSET)
    inputs = list(product(MICRO_ALPHABET, repeat=n))
    n_in = len(inputs)
    in_index = {a: i for i, a in enumerate(inputs)}
    D = n_in * n_res * n_M

    def encode(a_idx, res_tuple, M_idx):
        res_lin = 0
        for v in res_tuple:
            res_lin = res_lin * m + v
        return (a_idx * n_res + res_lin) * n_M + M_idx

    def decode_res(res_lin):
        digits = []
        for _ in range(n):
            digits.append(res_lin % m)
            res_lin //= m
        return tuple(reversed(digits))

    # precompute per-input output numerators j(a) and M(a)
    jmap = {}
    Mmap = {}
    for a in inputs:
        j = finite_normalize(list(a), MICRO_Q, 0)
        jmap[a] = tuple(v % m for v in j)  # enc(j)
        Mmap[a] = sum(v * v for v in a)

    clean = np.empty(D, dtype=np.int64)
    reten = np.empty(D, dtype=np.int64)
    for a_idx, a in enumerate(inputs):
        enc_j = jmap[a]
        Ma = Mmap[a]
        M_add_idx = MICRO_MSET.index(Ma % n_M)
        for res_lin in range(n_res):
            res = decode_res(res_lin)
            new_res = tuple((res[i] + enc_j[i]) % m for i in range(n))
            new_res_lin = 0
            for v in new_res:
                new_res_lin = new_res_lin * m + v
            for M_idx in range(n_M):
                src = encode(a_idx, res, M_idx)
                # clean: M spectator (compute then uncompute) -> unchanged
                clean[src] = encode(a_idx, new_res, M_idx)
                # retention: M <- (M + M(a)) mod n_M (uncompute skipped)
                reten[src] = encode(a_idx, new_res, (M_idx + M_add_idx) % n_M)
    return {
        "D": D, "n_in": n_in, "n_res": n_res, "n_M": n_M, "m": m,
        "inputs": inputs, "in_index": in_index, "encode": encode,
        "clean": clean, "reten": reten, "jmap": jmap, "Mmap": Mmap,
    }


def perm_to_sparse(perm: np.ndarray) -> csr_matrix:
    D = perm.shape[0]
    data = np.ones(D, dtype=np.float64)
    return csr_matrix((data, (perm, np.arange(D))), shape=(D, D))


# ---------------------------------------------------------------------------
# Support-two lowering: decompose a permutation into adjacent transpositions.
# ---------------------------------------------------------------------------
def adjacent_transposition_word(perm: list[int]) -> list[int]:
    """Return adjacent swaps (each named by its low index k => swap(k,k+1)) whose
    left-to-right product equals `perm` (as a function i -> perm[i])."""
    a = list(perm)
    word = []
    n = len(a)
    # selection by adjacent swaps (bubble): sort a to identity, record swaps
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                word.append(j)
    return word


def apply_word(word: list[int], n: int) -> list[int]:
    perm = list(range(n))
    for k in reversed(word):
        perm[k], perm[k + 1] = perm[k + 1], perm[k]
    return perm


# ---------------------------------------------------------------------------
# E2 Route-B saturation, exact rational.
# ---------------------------------------------------------------------------
def saturate(r: Fraction, sigma: int, kappa: Fraction, alpha: Fraction,
             r0: Fraction = E2_R0, rho: Fraction = E2_RHO) -> Fraction:
    u = r - rho
    absu = u if u >= 0 else -u
    return r0 + sigma * kappa * alpha * u / (1 + alpha * absu)


# ---------------------------------------------------------------------------
# Actuation endpoint on the one-excitation (1 + n_frames) block (c626 Route A).
# ---------------------------------------------------------------------------
def endpoint_probability(nvec: np.ndarray, coupling: float, t: float) -> float:
    dim = 1 + len(nvec)
    H = np.zeros((dim, dim), dtype=complex)
    H[0, 1:] = coupling * nvec
    H[1:, 0] = coupling * nvec
    U = expm(-1j * t * H)
    psi0 = np.zeros(dim, dtype=complex)
    psi0[0] = 1.0
    psi = U @ psi0
    return float(np.sum(np.abs(psi[1:]) ** 2))


def bound_B(eps: float, Q: int) -> float:
    L = (1.0 / FLOOR) if eps == 0.0 else (1.0 / eps)
    return (math.sqrt(N_FRAMES) / (2.0 * Q)) * (L + 1.0)


# ===========================================================================
# main
# ===========================================================================
def main() -> int:
    started = perf_counter()
    rng = np.random.default_rng(SEED)
    print("FINITE REVERSIBLE NORM/SATURATION EVALUATOR TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT, "cycle_claim", CYCLE_CLAIM)

    # ---- 1. preflight: pins ------------------------------------------------
    pin_obs = {}
    pin_ok = True
    for name, want in PINS["c576_files"].items():
        p = ROOT / name
        if p.exists():
            got = file_sha(p)
        else:
            got = "MISSING"
        pin_obs[name] = got
        pin_ok = pin_ok and (got == want)
    module_sha = file_sha(Path(c576.__file__))
    module_pinned = PINS["c576_files"][
        "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py"]
    check("01 pins/c576_script_and_note_and_receipt_sha256",
          pin_ok and module_sha == module_pinned,
          {"module_sha": module_sha, "observed": pin_obs})

    # ---- 2. note contract (enforced only when the note is present) ---------
    required_note = (
        "authority: none", "audit: unset", "finite", "reversible", "lattice",
        "quantization bound", "all 24", "576", "support-two", "garbage-free",
        "oracle embedding", "output-register rotations", "not gravity",
        "not physical stress", "no axiom", "supplied", "open",
    )
    note_present = NOTE.exists()
    note_body = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if note_present else ""
    note_missing = tuple(item for item in required_note if item not in note_body)
    note_report = {"present": note_present, "missing": note_missing}
    check("02 note_present_with_all_firewall_clauses",
          note_present and not note_missing, note_report)

    # ---- 3. 24 label perms extracted from c576 + 576 products (integer) ----
    perms_valid = all(sorted(p) == list(range(24)) for p in LABEL_PERMS)

    def rule_perm(frame):
        inv = frame.T
        return [c576.FRAME_LOOKUP[tuple((sector @ inv).reshape(-1))] for sector in FRAMES]

    extract_matches_rule = all(LABEL_PERMS[i] == rule_perm(FRAMES[i]) for i in range(24))
    prod_ok = True
    n_products = 0
    for li, lf in enumerate(FRAMES):
        for ri, rf in enumerate(FRAMES):
            tgt = c576.FRAME_LOOKUP[tuple((lf @ rf).reshape(-1))]
            if compose_perm(LABEL_PERMS[li], LABEL_PERMS[ri]) != LABEL_PERMS[tgt]:
                prod_ok = False
            n_products += 1
    check("03 frame_label_perms_valid_and_match_c576_rule",
          perms_valid and extract_matches_rule, {"n_perms": len(LABEL_PERMS)})
    check("04 all576_label_perm_products_close_integer_exact",
          prod_ok and n_products == 576, {"n_products": n_products})

    # ---- 5. population + FLOOR --------------------------------------------
    population = build_population()
    min_norm = min(o["norm"] for o in population)
    max_norm = max(o["norm"] for o in population)
    check("05 exact_24_orbit_population_built_and_floor_below_min_norm",
          len(population) == 24 and FLOOR < min_norm and FLOOR > 1.0 / max(Q_SIZES),
          {"n_orbits": len(population), "min_norm": round(min_norm, 6),
           "max_norm": round(max_norm, 6), "FLOOR": FLOOR})

    # ---- 6. certified rounding: exhaustive-domain census + certificate -----
    # exhaustive check that certified_round matches nearest and the certificate
    # holds over a bounded (B,M) domain (<= 2^20 states)
    cr_bad = 0
    cr_states = 0
    for B in range(0, 200):
        for M in range(1, 200):
            a, ok = certified_round(B, M)
            cr_states += 1
            ref = math.floor(B / math.sqrt(M) + 0.5)
            tie = abs(B / math.sqrt(M) - (a - 0.5)) < 1e-9 or abs(B / math.sqrt(M) - (a + 0.5)) < 1e-9
            if not ok or (a != ref and not tie):
                cr_bad += 1
    check("06 certified_rounding_exact_over_bounded_domain",
          cr_bad == 0 and cr_states <= (1 << 20),
          {"bad": cr_bad, "states": cr_states})

    # certificate holds on every ACTUAL evaluated (B,M) in the population
    cert_pop_ok = True
    cert_pop_seen = 0
    for orbit in population:
        for Q in Q_SIZES:
            K_max = K_MAX_FACTOR * Q
            k = quantize(orbit["d"], Q, K_max)
            for eps in EPS_GRID:
                eQ = int(eps * Q)
                M = sum(x * x for x in k) + eQ * eQ
                if M == 0:
                    continue
                for x in k:
                    a, ok = certified_round(Q * abs(x), M)
                    cert_pop_seen += 1
                    if not (ok and cert_ok(a, Q * abs(x), M)):
                        cert_pop_ok = False
    check("07 certificate_holds_on_every_evaluated_population_input",
          cert_pop_ok and cert_pop_seen > 0, {"checked": cert_pop_seen})

    # ---- 8. primitive-level exhaustive reversibility ----------------------
    # (a) modular adder bijection over Z_m^2 for m=2Q+1 (both Q); (b) squarer;
    # (c) acc adder; each domain <= 2^20.
    add_ok = True
    add_states = 0
    for Q in Q_SIZES:
        m = 2 * Q + 1
        for c in range(m):
            images = [(b + c) % m for b in range(m)]
            add_states += m
            if sorted(images) != list(range(m)):
                add_ok = False
    check("08a primitive_modular_adder_bijective_exhaustive",
          add_ok and add_states <= (1 << 20) * 2, {"states": add_states})

    # squarer as the PAIR map (k, c) -> (k, c + k^2): exhaustively bijective on
    # its bounded domain and exactly inverted by (k, c') -> (k, c' - k^2).
    sq_ok = True
    sq_states = 0
    SQ_WINDOW = 32
    for Q in (min(Q_SIZES),):
        K_max = K_MAX_FACTOR * Q
        images = set()
        for k in range(-K_max, K_max + 1):
            for cch in range(SQ_WINDOW):
                img = (k, cch + k * k)
                if img in images:
                    sq_ok = False
                images.add(img)
                back = (img[0], img[1] - img[0] * img[0])
                if back != (k, cch):
                    sq_ok = False
                sq_states += 1
    check("08b primitive_squarer_pair_map_bijective_and_exactly_inverted",
          sq_ok and 0 < sq_states <= (1 << 20), {"states": sq_states})

    acc_ok = True
    acc_states = 0
    for delta in range(0, 128):
        images = [A + delta for A in range(0, 128)]  # A -> A + delta bijective
        acc_states += len(images)
        if len(set(images)) != len(images):
            acc_ok = False
    check("08c primitive_accumulator_add_bijective",
          acc_ok and acc_states <= (1 << 20), {"states": acc_states})

    # ---- 9. explicit-operation composition row ----------------------------
    known_kinds = {"squarer", "acc_add", "acc_add_const", "add_mod",
                   "acc_add_const_inv", "acc_add_inv", "squarer_inv"}
    _, _, trace_sample, _ = reversible_normalize([1, 0, 2] + [0] * 21, 64, 32)
    struct_ok = all(kind in known_kinds for kind in trace_sample)
    check("09 every_explicit_trace_operation_is_a_verified_primitive_kind",
          struct_ok and len(trace_sample) > 0,
          {"kinds": sorted(set(trace_sample)), "operations": len(trace_sample),
           "scope": "represented square/accumulator/output operations only; "
                    "certified-round control logic is not gate-compiled"})

    # ---- 10. reduced fixture (3 regs, Q=16): enumerate + ancilla restored --
    reduced_inputs = list(product(REDUCED_ALPHABET, repeat=3))
    reduced_anc_clean = True
    reduced_out_matches_ref = True
    for a in reduced_inputs:
        j, anc_res, _, info = reversible_normalize(list(a), REDUCED_Q, 0)
        if anc_res != 0:
            reduced_anc_clean = False
        # FLOAT reference (independent of the integer certificate): cross-check
        M = sum(x * x for x in a)
        ref = [0, 0, 0]
        if M != 0:
            for i, x in enumerate(a):
                mag = math.floor(REDUCED_Q * abs(x) / math.sqrt(M) + 0.5)
                ref[i] = mag if x >= 0 else -mag
        if j != ref:
            # tolerate an exact half-integer tie (float ref may round the other way)
            tie = M != 0 and all(
                (x == 0) or
                abs(REDUCED_Q * abs(x) / math.sqrt(M) - (abs(j[i]) - 0.5)) < 1e-9 or
                abs(REDUCED_Q * abs(x) / math.sqrt(M) - (abs(j[i]) + 0.5)) < 1e-9
                for i, x in enumerate(a))
            if not tie:
                reduced_out_matches_ref = False
    check("10 reduced_fixture_all_inputs_ancilla_restored_and_matches_float_ref",
          reduced_anc_clean and reduced_out_matches_ref,
          {"n_inputs": len(reduced_inputs), "Q": REDUCED_Q})

    # ---- 11-14. micro materialised permutation matrices --------------------
    micro = micro_build()
    D = micro["D"]
    clean_perm = micro["clean"]
    reten_perm = micro["reten"]
    # bijection == exact unitarity of the integer permutation matrix
    clean_bijection = int(np.bincount(clean_perm, minlength=D).max()) == 1 and \
        int(np.bincount(clean_perm, minlength=D).min()) == 1
    P = perm_to_sparse(clean_perm)
    unit_resid = (P.T @ P - sparse_eye(D, format="csr")).count_nonzero()
    check("11 micro_permutation_matrix_bijection_and_unitary",
          clean_bijection and unit_resid == 0, {"D": D, "PtP_minus_I_nnz": int(unit_resid)})

    # linearity + norm preservation on seeded complex vectors
    x = rng.normal(size=D) + 1j * rng.normal(size=D)
    y = rng.normal(size=D) + 1j * rng.normal(size=D)
    alpha = complex(rng.normal(), rng.normal())
    beta = complex(rng.normal(), rng.normal())
    lhs = P @ (alpha * x + beta * y)
    rhs = alpha * (P @ x) + beta * (P @ y)
    lin_resid = float(np.max(np.abs(lhs - rhs)))
    norm_resid = abs(float(np.linalg.norm(P @ x)) - float(np.linalg.norm(x)))
    check("12 micro_permutation_matrix_linear_and_norm_preserving",
          lin_resid < TOL["float_match"] and norm_resid < TOL["float_match"],
          {"linearity_residual": lin_resid, "norm_residual": norm_resid})

    # unentanglement on a superposition of two DISTINCT actual quantized orbits
    # (reduced to {-1,0,1}^3 sign patterns; declared reduction, memo section 4)
    def sign_reduce(orbit_d):
        k = quantize(orbit_d, 64, K_MAX_FACTOR * 64)
        return tuple(int(np.sign(v)) for v in k[:3])
    a1 = sign_reduce(population[0]["d"])
    a2 = None
    for o in population[1:]:
        cand = sign_reduce(o["d"])
        if cand != a1 and micro["Mmap"][cand] != 0 and micro["Mmap"][a1] != 0:
            a2 = cand
            break
    if a2 is None:  # fall back to structured distinct nonzero-M inputs
        a1, a2 = (1, 1, 0), (1, 0, 1)
    m = micro["m"]
    n_M = micro["n_M"]
    idx1 = micro["encode"](micro["in_index"][a1], (0, 0, 0), 0)
    idx2 = micro["encode"](micro["in_index"][a2], (0, 0, 0), 0)
    psi = np.zeros(D, dtype=complex)
    psi[idx1] = 1 / math.sqrt(2)
    psi[idx2] = 1 / math.sqrt(2)

    def weight_on_M_nonzero(vec):
        # exact: amplitude weight on ancilla basis states with M != 0
        w = 0.0
        for i in np.nonzero(np.abs(vec) > 0)[0]:
            if int(i) % n_M != 0:
                w += float(abs(vec[int(i)]) ** 2)
        return w
    clean_out = P @ psi
    Preten = perm_to_sparse(reten_perm)
    reten_out = Preten @ psi
    clean_wnz = weight_on_M_nonzero(clean_out)   # exactly 0.0 when unentangled
    reten_wnz = weight_on_M_nonzero(reten_out)   # > 0 when garbage retained
    check("13 micro_clean_ancilla_exactly_unentangled_superposition",
          clean_wnz == 0.0,
          {"clean_weight_M_nonzero": clean_wnz, "inputs": [a1, a2],
           "M": [micro["Mmap"][a1], micro["Mmap"][a2]]})

    # F1 falsifier: retention probe MUST fail cleanliness (nonzero M weight)
    check("14 F1_garbage_retention_probe_fails_cleanliness",
          reten_wnz > TOL["float_match"] and clean_wnz == 0.0,
          {"retention_weight_M_nonzero": reten_wnz, "clean_weight_M_nonzero": clean_wnz})

    # ---- 15. support-two lowering of output-register rotations ------------
    # 15a: EVERY modular rotation add-by-j on the micro register decomposes into
    # a word of adjacent rail transpositions with exact recomposition and word
    # length <= m-1 (exhaustive over all j in [0, m)).
    m_micro = 2 * MICRO_Q + 1
    rot_ok = True
    rot_max_word = 0
    for jrot in range(m_micro):
        rot = [(i + jrot) % m_micro for i in range(m_micro)]
        word = adjacent_transposition_word(rot)
        rot_max_word = max(rot_max_word, len(word))
        if apply_word(word, m_micro) != rot:
            rot_ok = False
    per_gate_bound_holds = rot_max_word <= m_micro * (m_micro - 1) // 2
    check("15a support_two_all_micro_output_rotations_recompose_exactly",
          rot_ok and per_gate_bound_holds,
          {"rotations": m_micro, "max_word_len": rot_max_word,
           "word_len_bound": m_micro * (m_micro - 1) // 2})

    # 15b: output-rotation budget derived from the explicit-operation trace:
    # count add_mod operations in a full-instance trace and multiply by the
    # adjacent-transposition bound m(m-1)/2 for a rail permutation on m rails
    # (the bubble decomposition bound verified exhaustively at micro scale in
    # 15a); compare against the declared cap.
    budget = {}
    budget_ok = True
    for Q in Q_SIZES:
        m_full = 2 * Q + 1
        k_probe = quantize(population[0]["d"], Q, K_MAX_FACTOR * Q)
        _, _, tr, _ = reversible_normalize(k_probe, Q, 0)
        n_addmod = sum(1 for g in tr if g == "add_mod")
        per_add = m_full * (m_full - 1) // 2
        budget[Q] = n_addmod * per_add
        if not (n_addmod == 24 and budget[Q] <= SWAP_BUDGET_CAP):
            budget_ok = False
    check("15b support_two_output_rotation_budget_from_trace_within_cap",
          budget_ok, {"output_rotation_budget": budget, "cap": SWAP_BUDGET_CAP,
                      "excluded": "reciprocal-sqrt control logic, work-register "
                                  "arithmetic, and Route-B compilation"})

    # ---- 16-18. E2 saturation, exact rational -----------------------------
    e2_inject_ok = True
    e2_max_den = 0
    for sigma in E2_SIGMA:
        for kappa in E2_KAPPA:
            for alpha in E2_ALPHA:
                outs = [saturate(r, sigma, kappa, alpha) for r in E2_RGRID]
                if len(set(outs)) != len(outs):
                    e2_inject_ok = False
                for v in outs:
                    e2_max_den = max(e2_max_den, v.denominator)
    check("16 E2_saturation_injective_over_grid_bijection_witness",
          e2_inject_ok, {"grid": len(E2_SIGMA) * len(E2_KAPPA) * len(E2_ALPHA),
                         "rvals": len(E2_RGRID)})
    check("17 E2_denominator_census_within_analytic_raw_bound",
          E2_DEN_BOUND == 1080 and e2_max_den <= E2_DEN_BOUND,
          {"observed_max_den": e2_max_den,
           "analytic_raw_den_bound": E2_DEN_BOUND})
    zero_in_ok = all(saturate(E2_RHO, s, k, a) == E2_R0
                     for s in E2_SIGMA for k in E2_KAPPA for a in E2_ALPHA)
    recv_zero_ok = all(saturate(r, s, Fraction(0), a) == E2_R0
                       for s in E2_SIGMA for a in E2_ALPHA for r in E2_RGRID)
    check("18 E2_zero_input_and_receiver_zero_controls_exact",
          zero_in_ok and recv_zero_ok, {"zero_input": zero_in_ok, "receiver_zero": recv_zero_ok})

    # ---- 19. finite vs continuous: quantization bound (validity/tight/scale)
    observed_max = {}   # (eps, Q) -> max ||n_finite - n_exact||_2
    validity_ok = True
    zero_branch_seen = False
    for orbit in population:
        for Q in Q_SIZES:
            K_max = K_MAX_FACTOR * Q
            k = quantize(orbit["d"], Q, K_max)
            for eps in EPS_GRID:
                eQ = int(eps * Q)
                j = finite_normalize(k, Q, eQ)
                n_fin = np.asarray(j, dtype=float) / Q
                n_ex = continuous_reference(orbit["d"], float(eps))
                err = float(np.linalg.norm(n_fin - n_ex))
                key = (float(eps), Q)
                observed_max[key] = max(observed_max.get(key, 0.0), err)
                if err > bound_B(float(eps), Q) + TOL["bound_slack"]:
                    validity_ok = False
    check("19 quantization_bound_validity_all_inputs_within_B",
          validity_ok, {"n_pairs": len(observed_max)})

    # tightness: at least one regime within factor 8 (informative)
    ratios = {f"{e}:{Q}": observed_max[(e, Q)] / bound_B(e, Q) for (e, Q) in observed_max}
    tight_ok = max(ratios.values()) >= TOL["tightness_ratio"]
    check("20 quantization_bound_tightness_informative",
          tight_ok, {"max_ratio": round(max(ratios.values()), 4),
                     "threshold": TOL["tightness_ratio"]})

    # scaling: B(256)/B(64) == 1/4 exactly; observed-max ratio within factor
    scale_exact = all(abs(bound_B(float(e), 256) / bound_B(float(e), 64) - 0.25) < 1e-12
                      for e in EPS_GRID)
    obs_scale_ok = True
    for e in EPS_GRID:
        o64 = observed_max.get((float(e), 64), 0.0)
        o256 = observed_max.get((float(e), 256), 0.0)
        if o256 > 0:
            r = o64 / o256
            if not (1.0 / TOL["scaling_factor"] <= r <= TOL["scaling_factor"]):
                obs_scale_ok = False
    check("21 quantization_bound_scaling_one_over_Q",
          scale_exact and obs_scale_ok,
          {"B256_over_B64": round(bound_B(1.0, 256) / bound_B(1.0, 64), 6)})

    # ---- 22. covariance: finite evaluator commutes with all 24 frame perms -
    cov_ok = True
    cov_checked = 0
    for orbit in population:
        for Q in Q_SIZES:
            K_max = K_MAX_FACTOR * Q
            k = quantize(orbit["d"], Q, K_max)
            for eps in EPS_GRID:
                eQ = int(eps * Q)
                base = finite_normalize(k, Q, eQ)
                for p in LABEL_PERMS:
                    kp = apply_perm(k, p)
                    jp = finite_normalize(kp, Q, eQ)
                    expected = apply_perm(base, p)
                    cov_checked += 1
                    if jp != expected:
                        cov_ok = False
    check("22 covariance_all24_population_orbits_all24_frames_integer_exact",
          cov_ok and cov_checked > 0, {"comparisons": cov_checked})

    # ---- 23. F3 zero-branch, F4 below-floor refusal -----------------------
    zj, zanc, _, zinfo = reversible_normalize([0] * 24, 64, 0)
    f3_ok = all(v == 0 for v in zj) and zinfo["zero_branch"] and zanc == 0
    check("23 F3_zero_branch_exact_zero_output_no_division",
          f3_ok, {"zero_branch": zinfo["zero_branch"], "all_zero": all(v == 0 for v in zj)})

    def evaluate_with_floor(k, Q, eQ):
        lat_norm = math.sqrt(sum(x * x for x in k)) / Q
        if lat_norm == 0.0:
            return {"status": "zero_branch", "j": finite_normalize(k, Q, eQ)}
        if lat_norm < FLOOR:
            return {"status": "refused", "witness": {"k": list(k), "lattice_norm": lat_norm}}
        return {"status": "evaluated", "j": finite_normalize(k, Q, eQ)}

    Qf = 64
    sub = [1] + [0] * 23  # one +1/Q component; lattice norm 1/64 < FLOOR
    res_sub = evaluate_with_floor(sub, Qf, 0)
    # REAL below-floor c576 data: the excluded delta-like BLINDED_HELD_POINT_NEUTRAL
    # profile's generic-site L7 orbit (norm ~0.0143 < FLOOR, site-independent)
    # must be refused (it quantizes to the exact-zero branch at Q=64, with the
    # true norm strictly between 0 and FLOOR).
    pn_profiles = dict(c576.source_profiles(7, False)) | dict(c576.source_profiles(7, True))
    pn_name = next((nm for nm in pn_profiles if "POINT_NEUTRAL" in nm), None)
    if pn_name is not None:
        pn_orbit = orbit_at_site(pn_profiles[pn_name], POP_SITES[0])
        pn_k = quantize(pn_orbit, Qf, K_MAX_FACTOR * Qf)
        res_pn = evaluate_with_floor(pn_k, Qf, 0)
        pn_refused = (res_pn["status"] in ("refused", "zero_branch")
                      and 0.0 < float(np.linalg.norm(pn_orbit)) < FLOOR)
    else:
        res_pn = {"status": "profile_not_found"}
        pn_refused = False
    # a healthy population orbit must NOT be refused
    healthy = quantize(population[0]["d"], Qf, K_MAX_FACTOR * Qf)
    res_healthy = evaluate_with_floor(healthy, Qf, 0)
    f4_ok = (res_sub["status"] == "refused" and "witness" in res_sub
             and pn_refused and res_healthy["status"] == "evaluated")
    check("24 F4_below_floor_refused_with_witness_healthy_evaluated",
          f4_ok, {"sub_floor": res_sub.get("status"),
                  "sub_norm": round(res_sub.get("witness", {}).get("lattice_norm", 0), 5),
                  "point_neutral_real_data": res_pn.get("status"),
                  "healthy": res_healthy["status"]})

    # ---- 25. F2 irreversibility: truncating variant collision witness ------
    # a variant that DISCARDS the input (overwrites it with the output) collides
    scan = list(product(range(-2, 3), repeat=3))
    out_map = {}
    collision = None
    for a in scan:
        M = sum(x * x for x in a)
        if M == 0:
            j = (0, 0, 0)
        else:
            j = tuple((certified_round(Qf * abs(x), M)[0]) * (1 if x >= 0 else -1) for x in a)
        if j in out_map and collision is None:
            collision = [out_map[j], list(a), list(j)]
        else:
            out_map.setdefault(j, list(a))
    check("25 F2_truncating_variant_has_explicit_collision_pair",
          collision is not None, {"collision": collision})

    # ---- 26. F5 no-refit: single frozen TOL registry ----------------------
    tol_values_positive = all(v > 0 for v in TOL.values())
    must_differ = ("float_match", "signal", "bound_slack")
    md_distinct = len({TOL[k] for k in must_differ}) == len(must_differ)
    frozen_present = all(x is not None for x in (FLOOR, Q_SIZES, EPS_GRID, E2_DEN_BOUND))
    check("26 F5_no_refit_single_frozen_tol_table",
          tol_values_positive and md_distinct and frozen_present,
          {"keys": sorted(TOL)})

    # ---- 27-29. actuation endpoint (finite vs continuous reference) --------
    # lambda is INPUT-SIDE (c626 member-loop semantics): the orbit fed to both
    # the finite evaluator and the continuous reference is lam_sign*lam_mag*d;
    # the actuation coupling carries only b*sigma*kappa. For eps=0 the lambda
    # magnitude cancels in the normalizer; for eps>0 it does not (physical axis).
    # Frozen thinning rule: the first valid orbit in the declared enumeration
    # order for each lattice length.  Do not use population[:3], which would
    # select three L=3 orbits rather than one representative per length.
    act_orbits = []
    for L in POP_LENGTHS:
        selected = next(
            (orbit for orbit in population if orbit["label"].startswith(f"L{L}:")),
            None,
        )
        if selected is not None:
            act_orbits.append(selected)
    act_selection_ok = (
        len(act_orbits) == ACT_N_ORBITS == len(POP_LENGTHS)
        and {orbit["label"].split(":", 1)[0] for orbit in act_orbits}
        == {f"L{L}" for L in POP_LENGTHS}
    )
    max_dP = {}         # (eps,Q) -> max |P_finite - P_exact|
    coupling_signs = set()
    driven_endpoint_max = 0.0
    deleted_endpoint_max = 0.0
    act_within_bound = True
    lam_floor_ok = True
    C_prop = {}
    for Q in Q_SIZES:
        for eps in EPS_GRID:
            epsf = float(eps)
            eQ = int(eps * Q)
            K_max = K_MAX_FACTOR * Q
            # propagation constant: |P_f-P_e| <= 2 t max|coupling| ||n_f-n_e||
            max_coupling = ACT_B * max(abs(s) for s in ACT_SIGMA) * float(max(ACT_KAPPA))
            C_prop[(epsf, Q)] = 2.0 * ACT_T * max_coupling
            for orbit in act_orbits:
                for lam_sign in ACT_LAM_SIGN:
                    for lam_mag in ACT_LAM_MAG:
                        d_in = lam_sign * float(lam_mag) * orbit["d"]
                        if float(np.linalg.norm(d_in)) < FLOOR:
                            lam_floor_ok = False  # scaled input left the declared domain
                            continue
                        k = quantize(d_in, Q, K_max)
                        n_fin = np.asarray(finite_normalize(k, Q, eQ), dtype=float) / Q
                        n_ex = continuous_reference(d_in, epsf)
                        for sigma in ACT_SIGMA:
                            for kappa in ACT_KAPPA:
                                for c in ACT_C:
                                    coupling = ACT_B * sigma * float(kappa)
                                    coupling_signs.add(int(np.sign(coupling)))
                                    Pf = endpoint_probability(n_fin, coupling, ACT_T)
                                    Pe = endpoint_probability(n_ex, coupling, ACT_T)
                                    dP = abs(Pf - Pe)
                                    key = (epsf, Q)
                                    max_dP[key] = max(max_dP.get(key, 0.0), dP)
                                    driven_endpoint_max = max(driven_endpoint_max, Pe)
                                    if dP > C_prop[key] * bound_B(epsf, Q) + TOL["bound_slack"]:
                                        act_within_bound = False
                # deletion: zero coupling -> endpoint ~ 0
                deleted = endpoint_probability(
                    continuous_reference(orbit["d"], epsf), 0.0, ACT_T)
                deleted_endpoint_max = max(deleted_endpoint_max, deleted)
    check("27 actuation_endpoint_finite_matches_reference_within_propagated_bound",
          act_selection_ok and act_within_bound and lam_floor_ok and len(max_dP) > 0,
          {"max_dP": {f"{e}:{Q}": round(v, 8) for (e, Q), v in max_dP.items()},
           "lambda_scaled_inputs_stayed_above_floor": lam_floor_ok,
           "selected_orbits": [orbit["label"] for orbit in act_orbits]})
    check("28 actuation_both_quadrature_signs_occur",
          coupling_signs == {-1, 1}, {"coupling_signs": sorted(coupling_signs)})
    check("29 actuation_deletion_sensitivity_signal",
          driven_endpoint_max > TOL["signal"] and deleted_endpoint_max < TOL["signal"],
          {"driven_max": round(driven_endpoint_max, 6),
           "deleted_max": deleted_endpoint_max})

    # ---- 30. firewalls / inventory completeness ---------------------------
    firewalls = [
        "Constructive finite-arithmetic and reversible-oracle support ON THE "
        "DECLARED LATTICES ONLY; the full gate-level finite-evaluator compiler, "
        "arbitrary-precision evaluator, and continuum evaluator remain open.",
        "Support-two lowering and its SWAP budget cover output-register rotations "
        "only; reciprocal-sqrt control logic, work-register arithmetic, and Route-B "
        "gate compilation are not supplied.",
        "No sign, scale, regulator, saturation-scale, lambda, or c is selected; "
        "the full grid survives; branch selection remains open.",
        "No shared-code 3/4 DELAY association is derived; the PR5557 acceptance "
        "harness is untouched; the 5/4 ADVANCE count-edit interface is not driven.",
        "No energy, stress, source, gravity, causal-rate, event, Record, or Born "
        "claim. A contact-sensitive response is not energy, stress, source, or gravity.",
        "The value lattice, FLOOR, register widths, and grid are DECLARED SUPPLIED "
        "STRUCTURE. No new axiom, primitive, or premise class is introduced.",
    ]
    inventory = {
        "supplied": [
            "c576 actual-Regge source profiles, proper-cubic 24 frames, frame-sector permutation",
            "value lattice L_Q with Q in {64,256}, K_max, FLOOR, register widths",
            "regulator grid eps in {0,1/2,1,2}; saturation grid sigma/kappa/alpha; r0, rho",
            "actuation grid b, t, sigma, kappa, lambda, c; one-excitation block layout",
        ],
        "derived": [
            "certified integer reciprocal-sqrt-multiply and exact reversible-oracle "
            "embedding with represented work registers restored",
            "exact all-24 covariance and 576 label-perm products of the finite evaluator",
            "derived quantization bound B(eps,Q) with validity/tightness/scaling",
            "exact-rational saturation with denominator census, analytic raw-denominator "
            "bound, and controls",
            "materialised integer permutation matrix: bijection/unitarity/linearity/unentanglement",
            "support-two output-rail SWAP recomposition and output-rotation budget",
            "actuation endpoint match within a derived propagated bound",
        ],
        "open": [
            "gate-level reversible compilation of reciprocal-sqrt control logic, "
            "work-register arithmetic, and the Route-B rational map",
            "support-two lowering and resource budget for the full controlled evaluator",
            "arbitrary-precision / continuum evaluator and non-lattice inputs",
            "selection of sign/scale/regulator/saturation-scale/lambda/c (full grid survives)",
            "endogenous source profiles and locally-enforced value-basis domain",
            "physical stress/energy/gravity identification (not claimed)",
        ],
    }
    # firewalls/inventory are written to the receipt VERBATIM (below), NOT as a
    # check row: a constant-vs-constant assertion on the runner's own hardcoded
    # literals cannot fail and would be PASS-count padding (the defect class
    # disclosed for the vendored substrate). The externally-anchored guard is
    # the on-disk note-contract row 02.

    # ---- receipt ----------------------------------------------------------
    elapsed = perf_counter() - started
    contract = {
        "lattice": {"Q_sizes": list(Q_SIZES), "K_max_factor": K_MAX_FACTOR,
                    "FLOOR": FLOOR, "n_frames": N_FRAMES,
                    "eps_grid": [str(e) for e in EPS_GRID]},
        "population": {"lengths": list(POP_LENGTHS), "profiles": list(POP_PROFILE_NAMES),
                       "sites": [list(s) for s in POP_SITES], "n_orbits": len(population),
                       "min_orbit_norm": min_norm, "max_orbit_norm": max_norm},
        "E2": {"sigma": list(E2_SIGMA), "kappa": [str(k) for k in E2_KAPPA],
               "alpha": [str(a) for a in E2_ALPHA], "r0": str(E2_R0), "rho": str(E2_RHO),
               "observed_max_denominator": e2_max_den,
               "analytic_raw_denominator_bound": E2_DEN_BOUND},
        "actuation": {"b": ACT_B, "t": ACT_T, "kappa": [str(k) for k in ACT_KAPPA],
                      "sigma": list(ACT_SIGMA), "lam_sign": list(ACT_LAM_SIGN),
                      "lam_mag": [str(x) for x in ACT_LAM_MAG], "c": list(ACT_C),
                      "lambda_placement": "input-side, faithful to the c626 member loop "
                                          "(lambda scales the orbit before normalization; "
                                          "magnitude cancels only at eps=0)",
                      "improvement_axis_c": "DECLARED-ABSENT: c626's improvement vector is "
                                            "c620.spatial_trace_vector()@q from the unlanded "
                                            "Cycle-620 module; the c grid is not executable "
                                            "off main and no substitute semantics are invented",
                      "n_orbits_thinned": len(act_orbits),
                      "selected_orbits": [orbit["label"] for orbit in act_orbits],
                      "thinning_declared": "first valid orbit in frozen enumeration order "
                                           "for each declared length; full "
                                           "sigma/kappa/eps/lambda axes preserved"},
        "bounds": {"B": {f"{float(e)}:{Q}": bound_B(float(e), Q)
                         for e in EPS_GRID for Q in Q_SIZES}},
        "micro_instance": {"Q": MICRO_Q, "D": micro["D"]},
        "reduced_instance": {
            "Q": REDUCED_Q,
            "n_inputs": len(reduced_inputs),
            "reversible_scope": (
                "exact oracle embedding; represented square/accumulator work registers "
                "restore exactly; certified-round control logic is not gate-compiled"
            ),
            "enumeration_scope": (
                "reduced input fixture enumerated in full; micro oracle permutation "
                "materialized in full; full 24-register instance NOT exhaustive"
            ),
        },
        "support_two_scope": {
            "covered": "output-register modular rotations",
            "output_rotation_budget": budget,
            "not_covered": (
                "reciprocal-sqrt control logic, work-register arithmetic, Route-B "
                "gate compilation, or a full controlled-evaluator resource bound"
            ),
        },
        "tol": TOL,
    }
    receipt = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
        "date": DATE,
        "pins": PINS,
        "contract": contract,
        "firewalls": firewalls,
        "inventory": inventory,
        "rows": ROWS,
        "observed_bound_ratios": ratios,
        "actuation_max_dP": {f"{e}:{Q}": v for (e, Q), v in max_dP.items()},
        "campaign_consistency_anchors": PINS["campaign_anchors"],
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "tests_total": PASS + FAIL,
        "elapsed_seconds": elapsed,
        "pass": FAIL == 0,
    }
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=1, sort_keys=True, default=str))

    summary = {"authority": AUTHORITY, "audit": AUDIT, "cycle_claim": CYCLE_CLAIM,
               "passes": PASS, "failures": FAIL, "elapsed_seconds": round(elapsed, 3)}
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL == 0:
        print("RESULT FINITE_NORM_SATURATION_ARITHMETIC_REVERSIBLE_ORACLE_BOUNDED_SUPPORT")
        return 0
    print("RESULT FINITE_REVERSIBLE_NORM_SATURATION_EVALUATOR_TOURNAMENT_FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
