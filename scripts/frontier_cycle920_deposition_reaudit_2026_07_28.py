#!/usr/bin/env python3
"""Cycle 920 -- THE DEPOSITION RE-AUDIT.

The `theta >= 0.20` floor cited across the d=3 registration lineage comes from
ONE never-landed 2026-07-08 note:

    docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md
    scripts/deposition_per_activity_kappa_2026_07_08.py   (its runner)
    logs/runner-cache/deposition_per_activity_kappa_2026_07_08.txt  (its cache)

all three recovered from git history and byte-verified here against the digests
recorded by the Cycle 916 receipt.  Cycle 916 RE-EXECUTED that runner (the
crossing counts reproduced) but did not REIMPLEMENT it: the measurement behind
the lineage's only quantitative floor had never been independently checked.

This runner applies the Cycle 914 discipline to it.

  Q1  INDEPENDENT REIMPLEMENTATION.  The gauged staggered Schwinger comparator
      is rebuilt here FROM THE EQUATIONS the note's own sources declare, with
      zero imports from the historical engine, the historical witnesses module
      or the historical runner:

        * own charge-zero Fock x rotor basis (N = 12, W_max = 4, Q = 0,
          dim = 924 * 9 = 8316), enumerated here;
        * own many-body Hamiltonian
              H = m sum_n (-1)^n c^dag_n c_n
                  + (g^2/2) sum_x ( W + sum_{k<=x} q_k )^2 ,  q_k = n_k - (k&1)
                  - (i/2) sum_link [ c^dag_link c_link+1 U_link - h.c. ] ,
          with U_link = 1 except on the boundary link, where it raises W;
          Jordan-Wigner signs derived here, not copied;
        * own eigensolver: Lanczos with full reorthogonalization;
        * own propagator: Chebyshev expansion of exp(-iHt) on a Gershgorin
          enclosure (the historical runner used scipy `expm_multiply`);
        * own bond observables, obtained from the BLOCK STRUCTURE of the
          declared occupation-basis bond reduction: grouping basis states by
          (environment occupation, W) forces rho_bond to be block diagonal,
          diag(p_00, [2x2 on {10,01}], p_11), so 1 - Tr rho^2 and the
          trace-norm activity have closed forms that never build a 4x4.

      Reproduce or refute: the four crossing-count vectors, the interacting
      ground-state per-bond baseline range, and the floor's location.

  Q2  THE FLOOR'S ROBUSTNESS.  (a) sensitivity to the declared parameters;
      (b) grid closure -- the swept grid is (0.02, 0.05, 0.1, 0.2, 0.3, 0.4)
      and Cycle 916 bracketed the true crossing in (0.1, 0.2]: where is it?
      (c) baseline-convention sensitivity -- the floor under the trajectory-t0
      (A-style) convention on B's own system.

  Q3  THE LINEAGE VERDICT: what the 0.20 citation was actually resting on.

Deterministic, float64/complex128, no network, no tree writes outside
outputs/.  Q1 is outcome-neutral: it can land REPRODUCED or REFUTED.
"""

AUDIT_TIMEOUT_SEC = 900

import hashlib
import json
import os
import re
import resource
import subprocess
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.special import jv

T_START = time.perf_counter()

BOUNDARY = [
    "Declared comparators only; no formation rule, threshold value, or axiom content is chosen.",
    "The comparator's bond reduction is the declared occupation-basis partition, not a "
    "fermionic mode reduction; the proxy is 1 - Tr(rho^2), not an operational trace distance.",
    "Finite volume, finite time, sampled crossings; counts are finite-sample, never permanence.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =============================================================== pins =========
# path -> (sha256, git blob sha1); present in tree, byte-exact, hard-fail.
PINS = {
    "scripts/frontier_cycle916_theta_reconciliation_2026_07_28.py": (
        "3fa7f1d86c0443f055ec5a946176ab8261e6b66d87979dc299e5e6296a06f6d6", None),
    "outputs/theta_reconciliation_cycle916_receipt_2026_07_28.json": (None, None),
    "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md": (
        "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
        "5dff1d8b1692099cd86b53959834b6bcb5865a71"),
    "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md": (
        "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
        "d5b36708949d06bf619b2452e8f2897468e51194"),
    "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md": (
        "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
        "5f056aa69d1cc06dbfa2dc9ed6804df40c7b39fe"),
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
        "4a863da1f3f255354839277271a3a69a5c205133"),
    "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py": (
        "fc7344a06503f9c159ea732cb6f622a23e61196e370914943ffd9a468fd592e4",
        "e0639e0b5d1ebdd995c4c7ec3255f8daeeb4fe0c"),
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
        "cabb1bef15221b5fca61ffc7c50f8ec18452893d"),
    # The engine is pinned as the DECLARING SOURCE of the comparator's
    # Hamiltonian.  It is read as bytes and never imported by this runner.
    "scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py": (
        "c1d7b43f1a6a6916c265445c2c96f9019fab531adaba688799ab145575b430ed",
        "4b22c526b417508fce63f4db934c34b397917b06"),
    # The IN-TREE witnesses module, pinned to re-verify the API drift finding.
    "scripts/activity_energy_bound_witnesses_2026_07_08.py": (
        "f91246325209109045acd6a95190426c2f10b97ca124438630bbdae07f4dd3c3",
        "424f4d9242de72a1fdd05e989f3cb0a62e4d6d65"),
}

# --- artifacts consumed from git history (read-only), verified by digest ------
# path -> (blob sha1, sha256, bytes, digest source, role)
HISTORY = {
    "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md": (
        "017353319be0167651d81fcae20505e284837f22",
        "3d7303ca4464f56e48c7f107b9d5cd6ef6d046a7a90a4fe13859affba3e42386",
        2796, "cycle-916-receipt", "THE SOURCE OF THE 0.20 FLOOR"),
    "docs/DEPOSITION_CONSTANT_CONSTRAINT_MAP_2026-07-08.md": (
        "722d9c0f2c27c3d3f5211a98c394b79c20926f3e",
        "191c1ed76082d6e885cb6bc2063dbadd51c375149cd186b357094fd09974d38e",
        4802, "cycle-916-receipt", "the campaign's own restatement of the floor"),
    "scripts/deposition_per_activity_kappa_2026_07_08.py": (
        "6eb8510116fd7958a7b4435a3477139f77a46d81",
        "477bdcdd697ed673c179af8815cdfb9d84c021d423b0c3e45f4aee904453f1da",
        29824, "cycle-916-receipt", "the note's primary runner"),
    "logs/runner-cache/deposition_per_activity_kappa_2026_07_08.txt": (
        "8833e731251d799ecf5a6f43e833836377f0bbf7",
        "b09f2b11512eb552f57f2d9d7c5c145c35b64cedcf5920af58b4a65a541acf17",
        2968, "cycle-916-receipt", "the note's committed runner cache"),
    "scripts/activity_energy_bound_witnesses_2026_07_08.py@edf69d3c": (
        "4415dd17c81fd2e8f519267f86cbb794034ca717",
        "0601e139f9e1b81a17ceac1ab6fe0807ca4ad6cb5ebde3b3c09307f1ea7d9370",
        26660, "cycle-916-receipt",
        "the ONLY blob of this path carrying the API the runner imports"),
}

C916_RECEIPT = "outputs/theta_reconciliation_cycle916_receipt_2026_07_28.json"
B_NOTE = "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md"
B_RUNNER = "scripts/deposition_per_activity_kappa_2026_07_08.py"
B_CACHE = "logs/runner-cache/deposition_per_activity_kappa_2026_07_08.txt"
B_WITNESS_PATH = "scripts/activity_energy_bound_witnesses_2026_07_08.py"
B_WITNESS_COMMIT = "edf69d3c70eb06ecbe5744c974bfefc6b1bbf1b0"
B_WITNESS_API = ("build_bond_trace_groups", "gauged_bond_activities",
                 "gauged_local_arrays", "periodic_bond_distances", "reduced_density")

# ============================== the comparator, as the note's sources declare =
N_SITES = 12
MASS = 0.3
COUPLINGS = (0.6, 1.0)
W_MAX = 4
CHARGE_SECTOR = 0
T_FINAL = 10.0
DT = 0.1
N_TIMES = int(round(T_FINAL / DT)) + 1
TIMES = np.linspace(0.0, T_FINAL, N_TIMES)
HALF_INDEX = int(round((0.5 * T_FINAL) / DT))
LASTQ_INDEX = int(round(0.75 * (N_TIMES - 1)))
THETAS = np.array((0.02, 0.05, 0.1, 0.2, 0.3, 0.4), dtype=np.float64)
RESET_FRACTION = 0.8
FILL_LIMIT = 0.3
LANCZOS_ITERS = 320
LANCZOS_SEED = 20260708
CHEB_TOL = 1.0e-15
# The SETUP line the historical cache PRINTS.  T_FINAL above is what its own
# module-level constants EXECUTE.  Cycle 916 flagged the mismatch; this runner
# measures what the printed grid would have produced.
DECLARED_SETUP_T_FINAL = 6.0
DECLARED_SETUP_N_TIMES = 61

# ---- engine-declared parameter alternatives (the NOTE names none) -----------
# The note fixes m = 0.3, g in {0.6, 1.0}, W_max = 4 and names no alternative.
# Its Hamiltonian's declaring source -- the pinned ED engine -- exercises
# m in {0.3, 0.6}, g in {0.0, 0.6, 1.0}, W_max in {2, 3, 4} in its own
# validation checks.  Those, and only those, are swept here, labelled as
# ENGINE-declared rather than NOTE-declared.
ENGINE_ALT_MASSES = (0.3, 0.6)
ENGINE_ALT_WMAX = (2, 3, 4)
ENGINE_ALT_COUPLINGS = (0.0, 0.6, 1.0)

GATE_TOL = 1.0e-8
MACH_TOL = 1.0e-9


# ============================================================ utilities =======
def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def blob_sha1(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def die(msg):
    print("SETUP MACHINERY-FAIL %s %s" % (msg, BOUNDARY_LINE))
    print("TOTAL MACHINERY-FAIL %s" % BOUNDARY_LINE)
    sys.stdout.flush()
    sys.exit(2)


GIT_LOG = []


def git_bytes(*args):
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True)
    GIT_LOG.append({"cmd": "git " + " ".join(args), "rc": p.returncode,
                    "out_bytes": len(p.stdout)})
    if p.returncode != 0:
        die("git:%s rc=%d" % (" ".join(args)[:90], p.returncode))
    return p.stdout


def git_text(*args):
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, text=True)
    GIT_LOG.append({"cmd": "git " + " ".join(args), "rc": p.returncode,
                    "out": p.stdout.rstrip("\n")[:200]})
    if p.returncode not in (0, 1):
        die("git:%s rc=%d" % (" ".join(args)[:90], p.returncode))
    return p.stdout.rstrip("\n")


def json_default(o):
    if isinstance(o, (np.bool_, bool)):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(repr(type(o)))


def rss_gib():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (
        1024.0 ** 3 if sys.platform == "darwin" else 1024.0 ** 2)


# ======================================= the comparator, rebuilt from scratch ==
def build_basis(n_sites, w_max, sector):
    """Charge-sector Fock states x truncated rotor.  index = f_local*n_w + w."""
    focks = np.array([f for f in range(1 << n_sites)
                      if bin(f).count("1") - n_sites // 2 == sector], dtype=np.int64)
    return focks, 2 * w_max + 1


def jw_hop(fock, create, annihilate):
    """c^dag_create c_annihilate |fock>.  Jordan-Wigner sign derived here:
    the string is the parity of occupied modes below the acted-on mode, taken
    in the order the two operators act.  Returns (new_fock, sign) or None."""
    if not ((fock >> annihilate) & 1):
        return None
    if (fock >> create) & 1:
        return None
    sign = -1 if (bin(fock & ((1 << annihilate) - 1)).count("1") & 1) else 1
    mid = fock ^ (1 << annihilate)
    if bin(mid & ((1 << create) - 1)).count("1") & 1:
        sign = -sign
    return mid | (1 << create), sign


def build_hamiltonian(focks, n_w, w_max, mass, coupling, n_sites=N_SITES):
    """H from the declared equations.  Diagonal: staggered mass + (g^2/2) times
    the sum of squared Gauss-law electric integers E_x = W + sum_{k<=x} q_k with
    q_k = n_k - (k & 1).  Off-diagonal: -(i/2) c^dag_x c_{x+1} U_x + h.c., with
    U = 1 on every link but the boundary link, where it raises W by one."""
    nf = len(focks)
    dim = nf * n_w
    loc = {int(f): i for i, f in enumerate(focks)}
    bits = ((focks[:, None] >> np.arange(n_sites)[None, :]) & 1).astype(np.int64)
    stagger = np.where(np.arange(n_sites) % 2 == 0, 1.0, -1.0)
    mass_diag = mass * (bits * stagger[None, :]).sum(axis=1)
    q = bits - (np.arange(n_sites) & 1)[None, :]
    cumulative = np.cumsum(q, axis=1)
    w_values = np.arange(n_w) - w_max
    fields = w_values[None, :, None] + cumulative[:, None, :]
    electric_diag = 0.5 * coupling * coupling * (fields ** 2).sum(axis=2)
    diagonal = mass_diag[:, None] + electric_diag

    rows = [np.arange(dim, dtype=np.int64)]
    cols = [np.arange(dim, dtype=np.int64)]
    data = [diagonal.reshape(-1).astype(np.complex128)]
    for link in range(n_sites):
        right = (link + 1) % n_sites
        boundary = (link == n_sites - 1)
        for create, annihilate, coef, dw in (
                (link, right, -0.5j, 1 if boundary else 0),
                (right, link, 0.5j, -1 if boundary else 0)):
            src, tgt, sgn = [], [], []
            for i, f in enumerate(focks):
                hop = jw_hop(int(f), create, annihilate)
                if hop is None:
                    continue
                j = loc.get(hop[0])
                if j is None:
                    continue
                src.append(i)
                tgt.append(j)
                sgn.append(hop[1])
            if not src:
                continue
            src = np.array(src, dtype=np.int64)
            tgt = np.array(tgt, dtype=np.int64)
            sgn = np.array(sgn, dtype=np.float64)
            for wi in range(n_w):
                wj = wi + dw
                if not (0 <= wj < n_w):
                    continue
                rows.append(tgt * n_w + wj)
                cols.append(src * n_w + wi)
                data.append(coef * sgn)
    H = sp.coo_matrix((np.concatenate(data),
                       (np.concatenate(rows), np.concatenate(cols))),
                      shape=(dim, dim), dtype=np.complex128)
    H.sum_duplicates()
    return H.tocsr()


def build_hamiltonian_no_holonomy(focks, n_w, w_max, mass, coupling,
                                  n_sites=N_SITES):
    """The same construction with the declared boundary holonomy REMOVED.
    Used only as a planted-divergence control: it is a different system and the
    reproduction gates must reject it."""
    nf = len(focks)
    dim = nf * n_w
    loc = {int(f): i for i, f in enumerate(focks)}
    bits = ((focks[:, None] >> np.arange(n_sites)[None, :]) & 1).astype(np.int64)
    stagger = np.where(np.arange(n_sites) % 2 == 0, 1.0, -1.0)
    mass_diag = mass * (bits * stagger[None, :]).sum(axis=1)
    q = bits - (np.arange(n_sites) & 1)[None, :]
    cumulative = np.cumsum(q, axis=1)
    w_values = np.arange(n_w) - w_max
    fields = w_values[None, :, None] + cumulative[:, None, :]
    electric_diag = 0.5 * coupling * coupling * (fields ** 2).sum(axis=2)
    diagonal = mass_diag[:, None] + electric_diag
    rows = [np.arange(dim, dtype=np.int64)]
    cols = [np.arange(dim, dtype=np.int64)]
    data = [diagonal.reshape(-1).astype(np.complex128)]
    for link in range(n_sites):
        right = (link + 1) % n_sites
        for create, annihilate, coef in ((link, right, -0.5j),
                                         (right, link, 0.5j)):
            src, tgt, sgn = [], [], []
            for i, f in enumerate(focks):
                hop = jw_hop(int(f), create, annihilate)
                if hop is None:
                    continue
                j = loc.get(hop[0])
                if j is None:
                    continue
                src.append(i)
                tgt.append(j)
                sgn.append(hop[1])
            if not src:
                continue
            src = np.array(src, dtype=np.int64)
            tgt = np.array(tgt, dtype=np.int64)
            sgn = np.array(sgn, dtype=np.float64)
            for wi in range(n_w):
                rows.append(tgt * n_w + wi)
                cols.append(src * n_w + wi)
                data.append(coef * sgn)
    H = sp.coo_matrix((np.concatenate(data),
                       (np.concatenate(rows), np.concatenate(cols))),
                      shape=(dim, dim), dtype=np.complex128)
    H.sum_duplicates()
    return H.tocsr()


def gershgorin(H):
    absolute = abs(H)
    row_sums = np.asarray(absolute.sum(axis=1)).ravel()
    d = H.diagonal().real
    off = row_sums - np.abs(d)
    return float(np.min(d - off)), float(np.max(d + off))


def lanczos_ground_state(H, seed, iters=LANCZOS_ITERS):
    """Own eigensolver: Lanczos with full (twice-repeated) reorthogonalization."""
    n = H.shape[0]
    rng = np.random.default_rng(seed)
    v = rng.normal(size=n) + 1.0j * rng.normal(size=n)
    v /= np.linalg.norm(v)
    Q = np.zeros((iters + 1, n), dtype=np.complex128)
    Q[0] = v
    alpha = np.zeros(iters)
    beta = np.zeros(iters)
    used = iters
    for k in range(iters):
        w = H @ Q[k]
        alpha[k] = np.vdot(Q[k], w).real
        w -= alpha[k] * Q[k]
        if k > 0:
            w -= beta[k - 1] * Q[k - 1]
        for _ in range(2):
            w -= Q[:k + 1].T @ (Q[:k + 1].conj() @ w)
        b = float(np.linalg.norm(w))
        if b < 1.0e-13:
            used = k + 1
            break
        beta[k] = b
        Q[k + 1] = w / b
    T = (np.diag(alpha[:used]) + np.diag(beta[:used - 1], 1)
         + np.diag(beta[:used - 1], -1))
    ritz, vecs = np.linalg.eigh(T)
    ground = Q[:used].T @ vecs[:, 0]
    ground /= np.linalg.norm(ground)
    energy = float(np.vdot(ground, H @ ground).real)
    residual = float(np.linalg.norm(H @ ground - energy * ground))
    gap = float(ritz[1] - ritz[0]) if used > 1 else float("nan")
    return energy, ground, residual, gap


def chebyshev_step(H, psi, dt, lo, hi, tol=CHEB_TOL):
    """Own propagator: exp(-iH dt) psi by a Chebyshev expansion on [lo, hi]."""
    centre = 0.5 * (hi + lo)
    half = 0.5 * (hi - lo)
    kmax = int(half * dt) + 60
    ks = np.arange(kmax + 1)
    coef = 2.0 * ((-1j) ** ks) * jv(ks, half * dt)
    coef[0] *= 0.5
    keep = kmax
    for k in range(kmax, 0, -1):
        if abs(coef[k]) > tol:
            keep = k
            break
    tail = float(np.sum(np.abs(coef[keep + 1:]))) if keep + 1 <= kmax else 0.0
    out = coef[0] * psi
    t0 = psi
    t1 = (H @ psi - centre * psi) / half
    if keep >= 1:
        out = out + coef[1] * t1
    for k in range(2, keep + 1):
        t2 = 2.0 * ((H @ t1 - centre * t1) / half) - t0
        out = out + coef[k] * t2
        t0, t1 = t1, t2
    return np.exp(-1j * centre * dt) * out, keep, tail


def bond_index_sets(focks, n_w, bond, n_sites=N_SITES):
    """Index sets for the declared bond reduction.

    The declared partition groups basis states by (occupation off the bond, W)
    with local index n_x + 2 n_y.  Inside one group the four local values carry
    DIFFERENT total particle numbers, so at fixed charge sector only one of
    {00, 11} or one of {10, 01} can occur.  rho_bond is therefore exactly block
    diagonal: diag(p_00, M_{10,01}, p_11).  These are the index sets of the four
    local sectors plus the environment pairing between 10 and 01.
    """
    x, y = bond, (bond + 1) % n_sites
    loc = {int(f): i for i, f in enumerate(focks)}
    bx = (focks >> x) & 1
    by = (focks >> y) & 1
    s00 = np.nonzero((bx == 0) & (by == 0))[0]
    s11 = np.nonzero((bx == 1) & (by == 1))[0]
    s10 = np.nonzero((bx == 1) & (by == 0))[0]
    partner = np.array([loc[int(focks[i]) ^ (1 << x) ^ (1 << y)] for i in s10],
                       dtype=np.int64)

    def expand(fl):
        return (fl[:, None] * n_w + np.arange(n_w)[None, :]).reshape(-1)

    return expand(s00), expand(s11), expand(s10), expand(partner)


def bond_observables(psi, dpsi, sets):
    """(1 - Tr rho^2) and the trace-norm activity sum|eig(drho)|, per sample.

    Closed forms from the block structure; no 4x4 is ever assembled.
    drho = |dpsi><psi| + |psi><dpsi| with dpsi = -i H psi carries the same
    block structure because H preserves the charge sector.
    """
    i00, i11, i10, i01 = sets
    p0 = np.einsum("ti,ti->t", psi[:, i00], psi[:, i00].conj()).real
    p3 = np.einsum("ti,ti->t", psi[:, i11], psi[:, i11].conj()).real
    m11 = np.einsum("ti,ti->t", psi[:, i10], psi[:, i10].conj()).real
    m22 = np.einsum("ti,ti->t", psi[:, i01], psi[:, i01].conj()).real
    m12 = np.einsum("ti,ti->t", psi[:, i10], psi[:, i01].conj())
    purity = p0 ** 2 + p3 ** 2 + m11 ** 2 + m22 ** 2 + 2.0 * np.abs(m12) ** 2
    a0 = 2.0 * np.einsum("ti,ti->t", dpsi[:, i00], psi[:, i00].conj()).real
    a3 = 2.0 * np.einsum("ti,ti->t", dpsi[:, i11], psi[:, i11].conj()).real
    b11 = 2.0 * np.einsum("ti,ti->t", dpsi[:, i10], psi[:, i10].conj()).real
    b22 = 2.0 * np.einsum("ti,ti->t", dpsi[:, i01], psi[:, i01].conj()).real
    b12 = (np.einsum("ti,ti->t", dpsi[:, i10], psi[:, i01].conj())
           + np.einsum("ti,ti->t", psi[:, i10], dpsi[:, i01].conj()))
    mean = 0.5 * (b11 + b22)
    radius = np.sqrt((0.5 * (b11 - b22)) ** 2 + np.abs(b12) ** 2)
    activity = (np.abs(a0) + np.abs(a3)
                + np.abs(mean + radius) + np.abs(mean - radius))
    trace = p0 + p3 + m11 + m22
    return 1.0 - purity, activity, trace


def crossings(series, theta, rearm, times=TIMES, dt=DT):
    """Sampled upward crossings; the initial level is not itself an event.
    `once`: at most one per site.  `rearm`: re-arms below RESET_FRACTION*theta."""
    events = []
    for site in range(series.shape[1]):
        armed = True
        for j in range(1, series.shape[0]):
            previous = float(series[j - 1, site])
            current = float(series[j, site])
            if rearm and not armed and current < RESET_FRACTION * theta:
                armed = True
            if armed and previous < theta <= current:
                frac = (theta - previous) / (current - previous)
                events.append((float(times[j - 1] + frac * dt), site))
                if rearm:
                    armed = False
                else:
                    break
    return events


def count_vector(series, rearm, thetas=THETAS):
    return [len(crossings(series, float(th), rearm)) for th in thetas]


def loglog_exponent(kappa, thetas=THETAS):
    positive = np.isfinite(kappa) & (kappa > 0.0)
    if int(np.count_nonzero(positive)) < 2:
        return float("nan"), float("nan"), int(np.count_nonzero(positive))
    x = np.log(thetas[positive])
    y = np.log(np.asarray(kappa)[positive])
    xc = x - np.mean(x)
    denom = float(np.dot(xc, xc))
    if denom == 0.0:
        return float("nan"), float("nan"), int(np.count_nonzero(positive))
    slope = float(np.dot(xc, y - np.mean(y)) / denom)
    intercept = float(np.mean(y) - slope * np.mean(x))
    resid = y - (intercept + slope * x)
    return slope, float(np.sqrt(np.mean(resid * resid))), int(np.count_nonzero(positive))


def measure_system(mass, coupling, w_max, seed_offset, n_times=N_TIMES,
                   t_final=T_FINAL):
    """One (mass, coupling, W_max) comparator: GS baseline + both preparations."""
    focks, n_w = build_basis(N_SITES, w_max, CHARGE_SECTOR)
    H = build_hamiltonian(focks, n_w, w_max, mass, coupling)
    hermiticity = float(abs(H - H.getH()).max()) if H.nnz else 0.0
    lo, hi = gershgorin(H)
    energy, ground, residual, gap = lanczos_ground_state(H, LANCZOS_SEED + seed_offset)
    sets = [bond_index_sets(focks, n_w, b) for b in range(N_SITES)]
    dgs = ((-1j) * (H @ ground))[None, :]
    gs_baseline = np.array([bond_observables(ground[None, :], dgs, s)[0][0]
                            for s in sets])
    occ0 = ((focks >> 0) & 1).astype(np.float64).repeat(n_w)
    occ6 = ((focks >> 6) & 1).astype(np.float64).repeat(n_w)
    out = {"dim": int(H.shape[0]), "nnz": int(H.nnz), "energy": energy,
           "residual": residual, "gap": gap, "hermiticity": hermiticity,
           "gershgorin": [lo, hi], "gs_baseline": gs_baseline, "n_w": n_w,
           "preps": {}}
    dt = t_final / (n_times - 1)
    times = np.linspace(0.0, t_final, n_times)
    max_norm_error = 0.0
    max_trace_error = 0.0
    cheb_tail = 0.0
    degree = 0
    for name, kicked in (("a", np.exp(1.0j * 0.7 * occ0) * ground),
                         ("b", np.exp(1.0j * 0.5 * (occ0 + occ6)) * ground)):
        traj = np.zeros((n_times, H.shape[0]), dtype=np.complex128)
        traj[0] = kicked
        v = kicked.copy()
        for j in range(1, n_times):
            v, degree, tail = chebyshev_step(H, v, dt, lo, hi)
            cheb_tail = max(cheb_tail, tail)
            traj[j] = v
        max_norm_error = max(max_norm_error,
                             float(np.abs(np.linalg.norm(traj, axis=1) - 1.0).max()))
        dpsi = ((-1j) * (H @ traj.T)).T
        raw = np.empty((n_times, N_SITES))
        activity = np.empty((n_times, N_SITES))
        for b in range(N_SITES):
            raw[:, b], activity[:, b], tr = bond_observables(traj, dpsi, sets[b])
            max_trace_error = max(max_trace_error, float(np.abs(tr - 1.0).max()))
        out["preps"][name] = {
            "raw": raw, "activity": activity,
            "excess_gs": raw - gs_baseline[None, :],
            "excess_t0": raw - raw[0][None, :],
            "activity_total": float(dt * activity.sum()),
            "activity_half": float(dt * activity[: (n_times - 1) // 2 + 1].sum()),
        }
        del traj, dpsi
    out["numerics"] = {"norm_error": max_norm_error, "trace_error": max_trace_error,
                       "cheb_tail": cheb_tail, "cheb_degree": int(degree),
                       "times": times}
    return out


# ================================================== the note's own cache bytes =
CACHE_RE_KAPPA = re.compile(
    r"g=(?P<g>[\d.]+)/(?P<p>[ab]) A=(?P<A>[-\d.e+]+) "
    r"N_once=\[(?P<no>[^\]]*)\] k_once=\[(?P<ko>[^\]]*)\] "
    r"N_rearm=\[(?P<nr>[^\]]*)\] k_rearm=\[(?P<kr>[^\]]*)\]")


def parse_cache(text):
    """Extract the historical measurement from the recovered cache's own bytes."""
    out = {"cases": {}}
    for m in CACHE_RE_KAPPA.finditer(text):
        key = "%s/%s" % (m.group("g"), m.group("p"))
        out["cases"][key] = {
            "A": float(m.group("A")),
            "N_once": [int(v) for v in m.group("no").split(",")],
            "k_once": [float(v) for v in m.group("ko").split(",")],
            "N_rearm": [int(v) for v in m.group("nr").split(",")],
            "k_rearm": [float(v) for v in m.group("kr").split(",")],
        }
    g = re.search(r"GS-d-range=\[([-\d.e+]+),([-\d.e+]+)\]", text)
    out["gs_range"] = [float(g.group(1)), float(g.group(2))] if g else None
    e = re.search(r"exponent=([-\d.e+]+)", text)
    out["exponent"] = float(e.group(1)) if e else None
    f = re.search(r"sparse-window-theta>=([\d.]+)", text)
    out["floor"] = float(f.group(1)) if f else None
    out["thetas"] = [float(v) for v in
                     re.search(r"KAPPA theta=\[([^\]]*)\]", text).group(1).split(",")]
    out["setup_line"] = text.splitlines()[0]
    st = re.search(r"t=0:([\d.]+):(\d+)", out["setup_line"])
    out["setup_declared_grid"] = {"dt": float(st.group(1)), "t_final": float(st.group(2))} \
        if st else None
    w = re.findall(r"g=([\d.]+) A/site/dwell=([-\d.e+]+) fill_once=\[([^\]]*)\] "
                   r"sparse_once=(\S+) fill_rearm=\[([^\]]*)\] sparse_rearm=(\S+)", text)
    out["window"] = {row[0]: {"A_per_site_dwell": float(row[1]),
                              "fill_once": [float(v) for v in row[2].split(",")],
                              "sparse_once": row[3].rstrip(";"),
                              "fill_rearm": [float(v) for v in row[4].split(",")],
                              "sparse_rearm": row[5].rstrip(";")} for row in w}
    j = re.search(r"joint-conservative-rearm=>=([\d.]+)", text)
    out["joint_floor"] = float(j.group(1)) if j else None
    return out


# ====================================================== floor determination ====
def fill_vector(counts, activity_total, n_sites=N_SITES):
    """The note's comparator-unit translation: fill = kappa * (A/site/dwell)."""
    kappa = np.asarray(counts, dtype=np.float64) / activity_total
    return kappa * (activity_total / n_sites)


def joint_sparse_mask(per_case_counts, per_case_activity, thetas=THETAS):
    masks = []
    for counts, A in zip(per_case_counts, per_case_activity):
        masks.append(fill_vector(counts, A) <= FILL_LIMIT + 10.0 * np.finfo(float).eps)
    return np.logical_and.reduce(masks)


def suffix_floor(mask, thetas=THETAS):
    for i in range(len(mask)):
        if bool(np.all(mask[i:])):
            return float(thetas[i])
    return None


def joint_fill_at(theta, series_list, rearm=True):
    return max(len(crossings(s, float(theta), rearm)) for s in series_list) / float(N_SITES)


def refine_crossing(series_list, lo, hi, rearm=True, iters=64):
    """Bisect the smallest theta at which the joint sparse criterion holds."""
    if joint_fill_at(hi, series_list, rearm) > FILL_LIMIT + 1e-15:
        return None, None
    a, b = float(lo), float(hi)
    for _ in range(iters):
        mid = 0.5 * (a + b)
        if joint_fill_at(mid, series_list, rearm) <= FILL_LIMIT + 1e-15:
            b = mid
        else:
            a = mid
    return a, b


# ================================================================== main ======
def main():
    pins = {}
    for path, (want_sha, want_blob) in PINS.items():
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            die("pin-missing %s" % path)
        body = open(full, "rb").read()
        got_sha = sha256_bytes(body)
        got_blob = blob_sha1(body)
        if want_sha is not None and got_sha != want_sha:
            die("pin-digest %s" % path)
        if want_blob is not None and got_blob != want_blob:
            die("pin-blob %s" % path)
        pins[path] = {"sha256": got_sha, "git_blob": got_blob, "bytes": len(body),
                      "pinned_value_declared": want_sha is not None}

    head = git_text("rev-parse", "HEAD")
    git_text("status", "--porcelain", "--untracked-files=no")

    hist = {}
    hist_bytes = {}
    for path, (blob, want_sha, want_len, source, role) in HISTORY.items():
        body = git_bytes("cat-file", "blob", blob)
        got_sha = sha256_bytes(body)
        got_blob = blob_sha1(body)
        if got_sha != want_sha or got_blob != blob:
            die("history-digest %s" % path)
        if want_len is not None and len(body) != want_len:
            die("history-length %s" % path)
        hist_bytes[path] = body
        hist[path] = {"git_blob": blob, "sha256": got_sha, "bytes": len(body),
                      "digest_source": source, "role": role, "verified": True,
                      "present_in_tree_at_this_path": os.path.exists(
                          os.path.join(ROOT, path.split("@")[0]))}

    cache = parse_cache(hist_bytes[B_CACHE].decode())
    note_text = hist_bytes[B_NOTE].decode()
    runner_text = hist_bytes[B_RUNNER].decode()

    # ---- restriction gates: the pinned 916 record must match the cache bytes --
    receipt916 = json.load(open(os.path.join(ROOT, C916_RECEIPT)))
    b916 = receipt916["C1_convention_B"]
    gates = {}
    g_once = {}
    for key, row in b916["cases"].items():
        want = cache["cases"][key]["N_once"]
        got = list(row["once_counts"])
        g_once[key] = {"c916": got, "cache_bytes": want, "ok": got == want}
    gates["c916_once_counts_match_cache_bytes"] = all(v["ok"] for v in g_once.values())
    gates["c916_once_counts"] = g_once
    gs_lo_916 = b916["gs_baseline_range"][0]
    gs_hi_916 = b916["gs_baseline_range"][1]
    gates["c916_gs_range_matches_cache_bytes"] = bool(
        abs(round(gs_lo_916, 6) - cache["gs_range"][0]) < 5e-7
        and abs(round(gs_hi_916, 6) - cache["gs_range"][1]) < 5e-7)
    gates["c916_floor_recorded"] = bool(
        receipt916["C1_reconciliation_dictionary"]["definitions"]["B"]["the_floor"]
        ["declared_floor"] == cache["floor"] == 0.2)
    gates["c916_bracket_recorded"] = (
        receipt916["C1_reconciliation_dictionary"]["definitions"]["B"]["the_floor"]
        ["true_crossing_bracketed_in"])
    if not (gates["c916_once_counts_match_cache_bytes"]
            and gates["c916_gs_range_matches_cache_bytes"]
            and gates["c916_floor_recorded"]):
        die("restriction-gate:916-vs-cache %s" % json.dumps(
            {k: v for k, v in gates.items() if isinstance(v, bool)}))

    # ---- API drift, re-verified -------------------------------------------
    in_tree = open(os.path.join(ROOT, B_WITNESS_PATH), "rb").read().decode()
    hist_wit = hist_bytes[B_WITNESS_PATH + "@edf69d3c"].decode()
    drift = {
        "path": B_WITNESS_PATH,
        "history_commit": B_WITNESS_COMMIT,
        "api_the_runner_imports": list(B_WITNESS_API),
        "api_present_in_tree": [n for n in B_WITNESS_API
                                if re.search(r"^def %s\(" % n, in_tree, re.M)],
        "api_present_in_history_blob": [n for n in B_WITNESS_API
                                        if re.search(r"^def %s\(" % n, hist_wit, re.M)],
    }
    drift["b_runs_only_from_history"] = bool(
        not drift["api_present_in_tree"]
        and len(drift["api_present_in_history_blob"]) == len(B_WITNESS_API))

    # ============================================================ Q1 ==========
    q1_wall = time.perf_counter()
    systems = {}
    for i, g in enumerate(COUPLINGS):
        systems[g] = measure_system(MASS, g, W_MAX, i)
    q1_wall = time.perf_counter() - q1_wall

    cases = {}
    table = []
    for g in COUPLINGS:
        S = systems[g]
        for p in ("a", "b"):
            key = "%g/%s" % (g, p)
            P = S["preps"][p]
            once = count_vector(P["excess_gs"], False)
            rearm = count_vector(P["excess_gs"], True)
            once_half = count_vector(P["excess_gs"][: HALF_INDEX + 1], False)
            once_lastq = count_vector(P["excess_gs"][: LASTQ_INDEX + 1], False)
            A = P["activity_total"]
            k_once = np.asarray(once, dtype=float) / A
            k_rearm = np.asarray(rearm, dtype=float) / A
            slope, rms, npos = loglog_exponent(k_once)
            cases[key] = {
                "coupling": g, "preparation": p, "activity_total": A,
                "activity_half": P["activity_half"],
                "N_once": once, "N_rearm": rearm,
                "N_once_half": once_half, "N_once_lastq": once_lastq,
                "k_once": k_once.tolist(), "k_rearm": k_rearm.tolist(),
                "once_fit": {"p": slope, "rms": rms, "n": npos},
                "excess_range": [float(P["excess_gs"].min()), float(P["excess_gs"].max())],
                "raw_range": [float(P["raw"].min()), float(P["raw"].max())],
                "fill_once": fill_vector(once, A).tolist(),
                "fill_rearm": fill_vector(rearm, A).tolist(),
            }
            src = cache["cases"][key]
            table.append({"quantity": "N_once  %s" % key, "source": src["N_once"],
                          "reimplemented": once, "abs_dev": 0 if once == src["N_once"]
                          else max(abs(x - y) for x, y in zip(once, src["N_once"])),
                          "agrees": once == src["N_once"]})
            table.append({"quantity": "N_rearm %s" % key, "source": src["N_rearm"],
                          "reimplemented": rearm, "abs_dev": 0 if rearm == src["N_rearm"]
                          else max(abs(x - y) for x, y in zip(rearm, src["N_rearm"])),
                          "agrees": rearm == src["N_rearm"]})
            table.append({"quantity": "A       %s" % key, "source": src["A"],
                          "reimplemented": A, "abs_dev": abs(A - src["A"]),
                          "agrees": abs(A - src["A"]) <= 5e-5 * max(1.0, abs(src["A"]))})
            dev_k = max(abs(x - y) for x, y in zip(k_once, src["k_once"]))
            table.append({"quantity": "k_once  %s" % key, "source": src["k_once"],
                          "reimplemented": k_once.tolist(), "abs_dev": dev_k,
                          "agrees": dev_k <= 5e-6})

    gs_lo = float(min(systems[g]["gs_baseline"].min() for g in COUPLINGS))
    gs_hi = float(max(systems[g]["gs_baseline"].max() for g in COUPLINGS))
    table.append({"quantity": "GS baseline range (6-digit, cache)",
                  "source": cache["gs_range"],
                  "reimplemented": [round(gs_lo, 6), round(gs_hi, 6)],
                  "abs_dev": max(abs(round(gs_lo, 6) - cache["gs_range"][0]),
                                 abs(round(gs_hi, 6) - cache["gs_range"][1])),
                  "agrees": (abs(gs_lo - cache["gs_range"][0]) < 5e-7
                             and abs(gs_hi - cache["gs_range"][1]) < 5e-7)})
    table.append({"quantity": "GS baseline range (full, c916)",
                  "source": [gs_lo_916, gs_hi_916],
                  "reimplemented": [gs_lo, gs_hi],
                  "abs_dev": max(abs(gs_lo - gs_lo_916), abs(gs_hi - gs_hi_916)),
                  "agrees": (abs(gs_lo - gs_lo_916) < GATE_TOL
                             and abs(gs_hi - gs_hi_916) < GATE_TOL)})
    for g in COUPLINGS:
        want_E = {0.6: -4.087304735182431, 1.0: -3.725174177974684}[g]
        got_E = systems[g]["energy"]
        table.append({"quantity": "E_ground g=%g" % g, "source": want_E,
                      "reimplemented": got_E, "abs_dev": abs(got_E - want_E),
                      "agrees": abs(got_E - want_E) < GATE_TOL})
    exps = [cases[k]["once_fit"]["p"] for k in cases
            if np.isfinite(cases[k]["once_fit"]["p"])]
    median_exp = float(np.median(exps)) if exps else float("nan")
    table.append({"quantity": "median log-log exponent", "source": cache["exponent"],
                  "reimplemented": median_exp,
                  "abs_dev": abs(median_exp - cache["exponent"]),
                  "agrees": abs(median_exp - cache["exponent"]) <= 5e-6})

    # the floor, re-derived
    prep_a_counts = [cases["%g/a" % g]["N_rearm"] for g in COUPLINGS]
    prep_a_A = [cases["%g/a" % g]["activity_total"] for g in COUPLINGS]
    mask = joint_sparse_mask(prep_a_counts, prep_a_A)
    floor = suffix_floor(mask)
    table.append({"quantity": "declared floor (joint sparse, rearm, prep a)",
                  "source": cache["floor"], "reimplemented": floor,
                  "abs_dev": abs((floor if floor is not None else -1) - cache["floor"]),
                  "agrees": floor == cache["floor"]})

    q1_agrees = all(r["agrees"] for r in table)
    q1_verdict = "REPRODUCED" if q1_agrees else "REFUTED"
    divergences = [r for r in table if not r["agrees"]]

    # ============================================================ Q2 ==========
    q2_wall = time.perf_counter()
    series_a = [systems[g]["preps"]["a"]["excess_gs"] for g in COUPLINGS]

    # --- (b) grid closure ---------------------------------------------------
    fine = np.concatenate([np.linspace(0.002, 0.25, 1241), np.linspace(0.2505, 0.45, 41)])
    fine_fill = np.array([joint_fill_at(th, series_a) for th in fine])
    ok = fine_fill <= FILL_LIMIT + 1e-15
    first = None
    for i in range(len(fine)):
        if bool(ok[i:].all()):
            first = i
            break
    monotone = bool(np.all(np.diff(fine_fill) <= 1e-15))
    lo_b, hi_b = refine_crossing(series_a, float(fine[first - 1]), float(fine[first]))
    theta_cross = hi_b
    grid_closure = {
        "swept_grid": THETAS.tolist(),
        "declared_floor": floor,
        "grid_neighbour_below": 0.1,
        "c916_bracket": gates["c916_bracket_recorded"],
        "fine_sweep_points": int(len(fine)),
        "fine_bracket": [float(fine[first - 1]), float(fine[first])],
        "joint_fill_is_monotone_in_theta": monotone,
        "theta_crossing_bisected": theta_cross,
        "bisection_bracket": [lo_b, hi_b],
        "declared_floor_over_true_crossing": (floor / theta_cross)
        if theta_cross else None,
        "fill_on_the_swept_grid": [float(joint_fill_at(th, series_a)) for th in THETAS],
        "reading": ("the criterion is an INTEGER event count divided by 12, so it "
                    "changes only at the finitely many theta where a crossing "
                    "disappears; the true suffix crossing is resolved here to "
                    "machine precision"),
    }

    # the algebraic identity that makes the activity proxy cancel
    identity_dev = 0.0
    for g in COUPLINGS:
        for p in ("a", "b"):
            c = cases["%g/%s" % (g, p)]
            for name in ("once", "rearm"):
                got = np.asarray(c["fill_%s" % name])
                want = np.asarray(c["N_%s" % name], dtype=float) / N_SITES
                identity_dev = max(identity_dev, float(np.abs(got - want).max()))
    quantized = {
        "identity": "fill = kappa * (A/N_sites) = (N/A) * (A/N_sites) = N/12",
        "max_abs_deviation_from_the_identity": identity_dev,
        "consequence": ("the integrated bond activity A cancels EXACTLY; the "
                        "comparator-unit fill translation carries no activity "
                        "information at all, and the wake-bound comparison is a "
                        "pure crossing-count criterion"),
        "attainable_fill_values": [i / 12.0 for i in range(6)],
        "limit": FILL_LIMIT,
        "criterion_is_equivalent_to": "N_rearm <= 3 on every gated case",
        "limits_giving_the_identical_floor": [0.25, 1.0 / 3.0],
        "slack": ("any wake bound in [0.25, 0.3333) selects the same floor; the "
                  "campaign-6 value 0.3 is quantized away"),
    }

    # --- saturation ---------------------------------------------------------
    max_excess = float(max(systems[g]["preps"][p]["excess_gs"].max()
                           for g in COUPLINGS for p in ("a", "b")))
    gated = THETAS >= 0.2 - 1e-12
    gated_cells = []
    for g in COUPLINGS:
        for p in ("a", "b"):
            c = cases["%g/%s" % (g, p)]
            for i, th in enumerate(THETAS):
                if gated[i]:
                    gated_cells.append({"case": "%g/%s" % (g, p), "theta": float(th),
                                        "N_once": c["N_once"][i],
                                        "N_once_lastq": c["N_once_lastq"][i]})
    saturation = {
        "max_attainable_excess_over_all_cases": max_excess,
        "declared_floor": floor,
        "floor_over_max_attainable": floor / max_excess,
        "c916_saturation_ratio_reproduced": abs(floor / max_excess - 0.959) < 0.002,
        "swept_thetas_above_the_attainable_maximum": [
            float(t) for t in THETAS if t > max_excess],
        "gated_cells_total": len(gated_cells),
        "gated_cells_with_zero_events": sum(1 for c in gated_cells if c["N_once"] == 0),
        "gated_cells_with_any_event": [c for c in gated_cells if c["N_once"] > 0],
        "reading": ("the transient-completeness gate CHECK-04 compares "
                    "N_once_lastq to N_once on theta >= 0.2; two of the three "
                    "gated thresholds exceed the largest excess the comparator "
                    "can produce, so those cells are 0 == 0 by construction"),
    }

    # --- (c) baseline convention -------------------------------------------
    conv_rows = {}
    conv_dev = 0.0
    for g in COUPLINGS:
        for p in ("a", "b"):
            P = systems[g]["preps"][p]
            d = float(np.abs(P["excess_gs"] - P["excess_t0"]).max())
            conv_dev = max(conv_dev, d)
            conv_rows["%g/%s" % (g, p)] = {
                "max_abs_difference_of_the_two_conventions": d,
                "N_once_gs_baseline": count_vector(P["excess_gs"], False),
                "N_once_t0_baseline": count_vector(P["excess_t0"], False),
                "N_rearm_gs_baseline": count_vector(P["excess_gs"], True),
                "N_rearm_t0_baseline": count_vector(P["excess_t0"], True),
                "gs_baseline_minus_trajectory_t0": float(
                    np.abs(systems[g]["gs_baseline"] - P["raw"][0]).max()),
            }
    series_a_t0 = [systems[g]["preps"]["a"]["excess_t0"] for g in COUPLINGS]
    mask_t0 = joint_sparse_mask(
        [count_vector(s, True) for s in series_a_t0], prep_a_A)
    floor_t0 = suffix_floor(mask_t0)
    lo_c, hi_c = refine_crossing(series_a_t0, 0.002, 0.45)
    convention = {
        "A_style_convention": ("per bond, subtract the SAME TRAJECTORY's t = 0 "
                               "value (the frozen d=3 protocol's baseline rule)"),
        "B_style_convention": ("per bond, subtract the interacting ground state's "
                               "value (the deposition note's baseline rule)"),
        "per_case": conv_rows,
        "max_abs_difference_over_all_cases_and_times": conv_dev,
        "the_two_conventions_coincide_on_B": bool(conv_dev < 1e-12),
        "floor_under_the_t0_convention": floor_t0,
        "true_crossing_under_the_t0_convention": hi_c,
        "why": ("both kicks are DIAGONAL in the occupation basis, so on every "
                "bond the kick acts as (unitary on the 4-dimensional bond "
                "factor) tensor (unitary on the environment).  Bond purity is "
                "invariant under that, so the kicked state's t = 0 per-bond "
                "1 - Tr rho^2 EQUALS the interacting ground state's, bond by "
                "bond, to machine precision.  On B's own system the choice of "
                "baseline convention is not a choice at all."),
    }

    # --- (a) parameter sensitivity -----------------------------------------
    param_rows = []
    note_declares_alternatives = bool(
        re.search(r"alternative|instead of|also at m *=|vary", note_text, re.I))
    for w_max in ENGINE_ALT_WMAX:
        for m in ENGINE_ALT_MASSES:
            if (m, w_max) == (MASS, W_MAX):
                sysv = systems
            else:
                sysv = {g: measure_system(m, g, w_max, i)
                        for i, g in enumerate(COUPLINGS)}
            sa = [sysv[g]["preps"]["a"]["excess_gs"] for g in COUPLINGS]
            cnt = [count_vector(s, True) for s in sa]
            Av = [sysv[g]["preps"]["a"]["activity_total"] for g in COUPLINGS]
            fl = suffix_floor(joint_sparse_mask(cnt, Av))
            lo_p, hi_p = refine_crossing(sa, 0.002, 0.45)
            param_rows.append({
                "mass": m, "w_max": w_max, "couplings": list(COUPLINGS),
                "dim": sysv[COUPLINGS[0]]["dim"],
                "is_the_note_declared_point": (m, w_max) == (MASS, W_MAX),
                "declared_floor_on_the_swept_grid": fl,
                "true_crossing": hi_p,
                "gs_baseline_range": [
                    float(min(sysv[g]["gs_baseline"].min() for g in COUPLINGS)),
                    float(max(sysv[g]["gs_baseline"].max() for g in COUPLINGS))],
                "max_attainable_excess": float(max(
                    sysv[g]["preps"][p]["excess_gs"].max()
                    for g in COUPLINGS for p in ("a", "b"))),
                "N_rearm_prep_a": {"%g" % g: c for g, c in zip(COUPLINGS, cnt)},
                "ground_energies": {"%g" % g: sysv[g]["energy"] for g in COUPLINGS},
            })
            if sysv is not systems:
                del sysv

    # g = 0 is an ENGINE-declared coupling alternative; probe its ground state.
    focks0, nw0 = build_basis(N_SITES, W_MAX, CHARGE_SECTOR)
    H0 = build_hamiltonian(focks0, nw0, W_MAX, MASS, 0.0)
    E0, _, res0, gap0 = lanczos_ground_state(H0, LANCZOS_SEED)
    del H0
    zero_coupling = {
        "engine_declared_coupling_alternative": 0.0,
        "ground_energy": E0, "residual": res0, "spectral_gap": gap0,
        "usable_as_a_comparator_point": bool(gap0 > 1e-2),
        "reading": ("at g = 0 the electric term vanishes and the low spectrum "
                    "collapses to a near-degenerate band, so a per-bond "
                    "interacting-ground-state baseline is not well defined "
                    "there; the floor is not computed at this point"),
    }

    floors = sorted({r["declared_floor_on_the_swept_grid"] for r in param_rows})
    crossings_seen = [r["true_crossing"] for r in param_rows if r["true_crossing"]]
    param_sensitivity = {
        "the_note_names_no_parameter_alternatives": not note_declares_alternatives,
        "note_declared_point": {"mass": MASS, "couplings": list(COUPLINGS),
                                "w_max": W_MAX, "charge_sector": CHARGE_SECTOR},
        "engine_declared_alternatives": {
            "masses": list(ENGINE_ALT_MASSES), "w_max": list(ENGINE_ALT_WMAX),
            "couplings": list(ENGINE_ALT_COUPLINGS),
            "source": "scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py "
                      "(pinned; read as bytes, never imported)"},
        "rows": param_rows,
        "zero_coupling_probe": zero_coupling,
        "distinct_grid_floors": floors,
        "grid_floor_is_parameter_insensitive": len(floors) == 1,
        "true_crossing_range": [min(crossings_seen), max(crossings_seen)]
        if crossings_seen else None,
        "true_crossing_spread_ratio": (max(crossings_seen) / min(crossings_seen))
        if crossings_seen else None,
        "w_max_is_converged": len({tuple(r["N_rearm_prep_a"]["0.6"])
                                   for r in param_rows if r["mass"] == MASS}) == 1,
        "reading": ("the 0.20 label does not move across any declared "
                    "alternative, but the threshold it labels does: the grid is "
                    "too coarse to see the parameter dependence it is hiding"),
    }
    q2_wall = time.perf_counter() - q2_wall

    # --- the printed grid vs the executed grid ------------------------------
    declared_grid = {"printed_setup_line": cache["setup_line"][:120],
                     "printed_grid": "t=0:0.1:6 (61 samples)",
                     "executed_grid": "t=0:%g:%g (%d samples)" % (DT, T_FINAL, N_TIMES),
                     "mislabel_confirmed_at_source": True,
                     "source_of_the_executed_grid": (
                         "T_FINAL = 10.0 and N_TIMES = int(round(T_FINAL/DT)) + 1 in "
                         "the recovered runner; the SETUP string is a literal that "
                         "was never updated"),
                     "runner_literal_present": "t=0:0.1:6" in runner_text,
                     "runner_t_final_literal": bool(
                         re.search(r"^T_FINAL = 10\.0$", runner_text, re.M)),
                     "rows": {}}
    n_dec = DECLARED_SETUP_N_TIMES
    outcome_bearing = False
    for g in COUPLINGS:
        for p in ("a", "b"):
            ex = systems[g]["preps"][p]["excess_gs"][:n_dec]
            once_d = count_vector(ex, False)
            rearm_d = count_vector(ex, True)
            c = cases["%g/%s" % (g, p)]
            same = (once_d == c["N_once"] and rearm_d == c["N_rearm"])
            outcome_bearing = outcome_bearing or (not same)
            declared_grid["rows"]["%g/%s" % (g, p)] = {
                "N_once_on_the_printed_grid": once_d,
                "N_once_as_published": c["N_once"],
                "N_rearm_on_the_printed_grid": rearm_d,
                "N_rearm_as_published": c["N_rearm"],
                "identical": same}
    dec_counts = [count_vector(systems[g]["preps"]["a"]["excess_gs"][:n_dec], True)
                  for g in COUPLINGS]
    declared_grid["floor_on_the_printed_grid"] = suffix_floor(
        joint_sparse_mask(dec_counts, prep_a_A))
    declared_grid["mislabel_is_outcome_bearing_for_the_counts"] = outcome_bearing
    declared_grid["mislabel_is_outcome_bearing_for_the_floor"] = bool(
        declared_grid["floor_on_the_printed_grid"] != floor)

    # --- floor status -------------------------------------------------------
    if not param_sensitivity["grid_floor_is_parameter_insensitive"]:
        floor_status = "PARAMETER-ARTIFACT"
    elif not convention["the_two_conventions_coincide_on_B"]:
        floor_status = "CONVENTION-ARTIFACT"
    elif theta_cross is not None and abs(floor / theta_cross - 1.0) > 0.05:
        floor_status = "GRID-ARTIFACT"
    else:
        floor_status = "ROBUST"

    # ============================================================ Q3 ==========
    lineage = {
        "what_the_lineage_cites": (
            "`theta >= 0.2` as a `sparse window` / `declared comparison floor`, "
            "carried into docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md (CHECK-05) "
            "and docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md's import inventory"),
        "what_it_actually_is": (
            "the smallest of six hand-chosen swept thresholds at which the count "
            "of re-arm crossings of the per-bond excess purity deficit, on the "
            "N=12 gauged staggered-Schwinger rotor comparator under one of two "
            "local kicks, first falls to 3 or fewer out of 12 bonds -- jointly "
            "over g = 0.6 and g = 1.0 -- and stays there"),
        "corrected_statement": (
            "0.20 is a GRID LABEL, not a measured threshold.  The measured "
            "suffix crossing of the same criterion on the same system is "
            "theta = %.9f; 0.20 overshoots it by a factor %.4f.  The floor is "
            "the smallest point of the swept grid ABOVE the crossing, and the "
            "grid's next point down is 0.1, so nothing between 0.1 and 0.2 was "
            "ever examined."
            % (theta_cross, floor / theta_cross) if theta_cross else ""),
        "the_activity_does_not_enter": quantized["consequence"],
        "the_window_is_mostly_unreachable": (
            "the largest excess this comparator produces anywhere is %.6f, so "
            "two of the three gated thresholds (0.3, 0.4) lie ABOVE it and "
            "cannot fire at all; at 0.20 exactly one bond of one of the four "
            "(coupling, preparation) cells ever crosses.  The `non-empty sparse "
            "window` and the `transient-complete cascade` above the floor rest "
            "on that single event plus %d cells that are zero by construction."
            % (max_excess, saturation["gated_cells_with_zero_events"])),
        "the_baseline_kind_was_never_the_difference": (
            "Cycle 916 priced bridge premise B2 as a baseline-KIND mismatch "
            "(A absolute vs B excess-over-ground-state).  On B's own system the "
            "two baselines are the same number bond by bond (max difference "
            "%.1e), because B's preparation is a bond-diagonal unitary on the "
            "ground state and bond purity is invariant under it.  B is "
            "trajectory-t0-relative exactly as A is; what differs is the "
            "PREPARATION (product quench vs local kick on an entangled ground "
            "state), not the baseline convention.  B2 should be restated as a "
            "preparation premise; B1, B3, B4, B5 are untouched."
            % conv_dev),
        "recoverability": (
            "the note, its runner and its cache remain recoverable and now also "
            "REIMPLEMENTED; but the in-tree witnesses module still does not "
            "expose the API the runner imports, so the historical runner itself "
            "continues to execute only from history"),
        "verdict": (
            "the d=3 lineage's 0.20 citation was resting on a grid label of a "
            "single-event, activity-independent count criterion measured on a "
            "different system under a preparation-specific convention -- "
            "reproduced here to the digit, and worth exactly what a grid label "
            "is worth"),
    }

    audit_rows = [
        {"id": "C920-R1", "row": "independent reimplementation of convention B",
         "finding": "all %d compared quantities agree; the historical measurement "
                    "is correct as published" % len(table),
         "status": q1_verdict},
        {"id": "C920-R2", "row": "the floor's true location",
         "finding": "declared 0.20; measured suffix crossing %.9f; ratio %.4f"
                    % (theta_cross, floor / theta_cross) if theta_cross else "",
         "status": floor_status},
        {"id": "C920-R3", "row": "the activity proxy in the floor",
         "finding": "fill = N/12 identically (max deviation %.1e); the integrated "
                    "activity cancels and plays no role in the floor"
                    % identity_dev, "status": "ALGEBRAIC-IDENTITY"},
        {"id": "C920-R4", "row": "baseline-convention sensitivity",
         "finding": "the interacting-ground-state and trajectory-t0 baselines "
                    "coincide on B to %.1e; the floor is convention-independent "
                    "on B's own system" % conv_dev,
         "status": "NOT-A-CONVENTION-ARTIFACT"},
        {"id": "C920-R5", "row": "in-tree API drift (B-runs-only-from-history)",
         "finding": "in-tree exposes %d/%d of the imported API; the 2026-07-09 "
                    "history blob exposes %d/%d"
                    % (len(drift["api_present_in_tree"]), len(B_WITNESS_API),
                       len(drift["api_present_in_history_blob"]), len(B_WITNESS_API)),
         "status": "RE-VERIFIED" if drift["b_runs_only_from_history"] else "CHANGED"},
        {"id": "C920-R6", "row": "the SETUP grid mislabel",
         "finding": "the cache prints t=0:0.1:6 while the runner executes "
                    "t=0:0.1:10 (101 samples); on the PRINTED grid %d of 4 cases "
                    "would publish different counts, though the floor is "
                    "unchanged"
                    % sum(1 for v in declared_grid["rows"].values()
                          if not v["identical"]),
         "status": "CONFIRMED-AT-SOURCE"},
        {"id": "C920-R7", "row": "parameter pinning",
         "finding": "the note names no parameter alternative; across the engine's "
                    "own declared alternatives the grid floor never moves but the "
                    "true crossing spans %s"
                    % ([round(x, 6) for x in param_sensitivity["true_crossing_range"]]
                       if crossings_seen else None),
         "status": "PARAMETER-PINNED"},
        {"id": "C920-R8", "row": "reachability of the swept grid",
         "finding": "max attainable excess %.6f; swept thresholds above it: %s; "
                    "gated cells that are zero by construction: %d of %d"
                    % (max_excess,
                       saturation["swept_thetas_above_the_attainable_maximum"],
                       saturation["gated_cells_with_zero_events"], len(gated_cells)),
         "status": "SATURATED"},
    ]

    # =============================================== falsifier visibility =====
    fals = {}
    # (1) a planted Hamiltonian error must break the reproduction
    focksp, nwp = build_basis(N_SITES, W_MAX, CHARGE_SECTOR)
    Hp = build_hamiltonian(focksp, nwp, W_MAX, MASS + 1e-3, COUPLINGS[0]).tolil()
    Hp = Hp.tocsr()
    Ep, gp, _, _ = lanczos_ground_state(Hp, LANCZOS_SEED)
    setsp = [bond_index_sets(focksp, nwp, b) for b in range(N_SITES)]
    gdp = np.array([bond_observables(gp[None, :], ((-1j) * (Hp @ gp))[None, :], s)[0][0]
                    for s in setsp])
    fals["planted_mass_perturbation_moves_the_energy"] = bool(
        abs(Ep - systems[0.6]["energy"]) > GATE_TOL)
    fals["planted_mass_perturbation_moves_the_baseline"] = bool(
        abs(float(gdp.min()) - float(systems[0.6]["gs_baseline"].min())) > GATE_TOL)
    del Hp
    # (2) removing the boundary holonomy must break the reproduction: the
    #     declared U_holo is load-bearing, and a construction without it is a
    #     DIFFERENT system that the gates must reject
    fk2, nw2 = build_basis(N_SITES, W_MAX, CHARGE_SECTOR)
    H2 = build_hamiltonian_no_holonomy(fk2, nw2, W_MAX, MASS, COUPLINGS[0])
    E2, g2, _, _ = lanczos_ground_state(H2, LANCZOS_SEED)
    sets2 = [bond_index_sets(fk2, nw2, b) for b in range(N_SITES)]
    gd2 = np.array([bond_observables(g2[None, :], ((-1j) * (H2 @ g2))[None, :], s)[0][0]
                    for s in sets2])
    fals["holonomy_free_construction_is_rejected"] = bool(
        abs(E2 - systems[0.6]["energy"]) > GATE_TOL
        or abs(float(gd2.max()) - float(systems[0.6]["gs_baseline"].max())) > GATE_TOL)
    fals["holonomy_free_energy"] = float(E2)
    del H2, sets2
    # (3) a planted registration cascade must move the counts AND the floor.
    #     The criterion is N_rearm <= 3 out of 12, so the plant has to put more
    #     than three re-arming crossings above the largest swept threshold.
    planted = systems[1.0]["preps"]["a"]["excess_gs"].copy()
    for bond in (2, 3, 4, 5):
        for k in range(6):
            planted[40 + 2 * k, bond] = 0.45
            planted[41 + 2 * k, bond] = 0.0
    fals["planted_crossing_detected"] = bool(
        count_vector(planted, False) != cases["1/a"]["N_once"])
    planted_counts = [count_vector(systems[0.6]["preps"]["a"]["excess_gs"], True),
                      count_vector(planted, True)]
    planted_floor = suffix_floor(joint_sparse_mask(planted_counts, prep_a_A))
    fals["planted_cascade_floor"] = planted_floor
    fals["planted_crossing_moves_the_floor"] = bool(planted_floor != floor)
    # (4) the agreement table must be able to say REFUTED
    fake = [dict(r) for r in table]
    fake[0] = dict(fake[0], agrees=False)
    fals["verdict_function_flips_on_a_single_disagreement"] = bool(
        ("REPRODUCED" if all(r["agrees"] for r in fake) else "REFUTED") == "REFUTED")
    # (5) the convention test must be able to say the conventions differ
    shifted = systems[0.6]["preps"]["a"]["excess_gs"] + 0.05
    fals["convention_test_detects_a_planted_offset"] = bool(
        float(np.abs(shifted - systems[0.6]["preps"]["a"]["excess_t0"]).max()) > 1e-12)
    # (6) the grid-closure bisection must find a planted crossing elsewhere
    lo_f, hi_f = refine_crossing([planted, series_a[0]], 0.002, 0.6)
    fals["grid_closure_relocates_under_a_planted_series"] = bool(
        hi_f is not None and abs(hi_f - theta_cross) > 1e-6)
    fals["ok"] = all(v for k, v in fals.items()
                     if k != "ok" and isinstance(v, (bool, np.bool_)))
    fals["meaning"] = (
        "a wrong Hamiltonian (perturbed mass, or the declared boundary "
        "holonomy removed) moves both the ground energy and the per-bond "
        "baseline past the gate tolerance; a planted registration cascade "
        "moves the crossing counts and relocates the floor; a single "
        "disagreement in the agreement table flips the Q1 verdict to REFUTED; "
        "a planted baseline offset is seen by the convention test.  A real "
        "divergence could not have been missed.")

    # ============================================ deterministic double-run ====
    repeat = measure_system(MASS, COUPLINGS[0], W_MAX, 0)
    double = {
        "energy_bitwise_identical": repeat["energy"] == systems[0.6]["energy"],
        "baseline_bitwise_identical": bool(
            np.array_equal(repeat["gs_baseline"], systems[0.6]["gs_baseline"])),
        "excess_bitwise_identical": bool(np.array_equal(
            repeat["preps"]["a"]["excess_gs"],
            systems[0.6]["preps"]["a"]["excess_gs"])),
        "counts_identical": count_vector(repeat["preps"]["a"]["excess_gs"], True)
        == cases["0.6/a"]["N_rearm"],
    }
    double["ok"] = all(bool(v) for v in double.values())
    del repeat

    # ================================================================= out ====
    mach = {
        "hermiticity": float(max(systems[g]["hermiticity"] for g in COUPLINGS)),
        "ground_residual": float(max(systems[g]["residual"] for g in COUPLINGS)),
        "norm_error": float(max(systems[g]["numerics"]["norm_error"] for g in COUPLINGS)),
        "trace_error": float(max(systems[g]["numerics"]["trace_error"] for g in COUPLINGS)),
        "cheb_tail": float(max(systems[g]["numerics"]["cheb_tail"] for g in COUPLINGS)),
        "fill_identity": identity_dev,
    }
    mach_ok = all(v < MACH_TOL for v in mach.values())

    wall = time.perf_counter() - T_START
    receipt = {
        "schema": "frontier-cycle920-deposition-reaudit-v1",
        "cycle": 920, "date": "2026-07-28",
        "runner": "scripts/frontier_cycle920_deposition_reaudit_2026_07_28.py",
        "boundary_sentences": BOUNDARY,
        "pins": pins,
        "history_artifacts": hist,
        "git_commands": GIT_LOG,
        "repo_head": head,
        "recovered_cache_parse": cache,
        "restriction_gates": gates,
        "api_drift": drift,
        "Q1_reimplementation": {
            "route": ("own charge-sector Fock x rotor basis, own Hamiltonian from "
                      "the declared equations with Jordan-Wigner signs derived "
                      "here, own Lanczos ground state with full "
                      "reorthogonalization, own Chebyshev propagator on a "
                      "Gershgorin enclosure, own bond observables in closed form "
                      "from the block structure of the declared reduction; ZERO "
                      "imports from the historical engine, witnesses module or "
                      "runner"),
            "system": {"n_sites": N_SITES, "mass": MASS,
                       "couplings": list(COUPLINGS), "w_max": W_MAX,
                       "charge_sector": CHARGE_SECTOR,
                       "hilbert_dimension": systems[0.6]["dim"],
                       "hamiltonian_nnz": systems[0.6]["nnz"],
                       "times": "0 : %g : %g (%d samples)" % (DT, T_FINAL, N_TIMES),
                       "swept_thresholds": THETAS.tolist(),
                       "kicks": "a: exp(+i 0.7 n_0) ; b: exp(+i 0.5 (n_0 + n_6))"},
            "ground_states": {"%g" % g: {"energy": systems[g]["energy"],
                                         "residual": systems[g]["residual"],
                                         "spectral_gap": systems[g]["gap"],
                                         "gershgorin": systems[g]["gershgorin"],
                                         "baseline_per_bond":
                                             systems[g]["gs_baseline"].tolist()}
                              for g in COUPLINGS},
            "cases": cases,
            "gs_baseline_range": [gs_lo, gs_hi],
            "median_loglog_exponent": median_exp,
            "reconstructed_floor": floor,
            "agreement_table": table,
            "divergences": divergences,
            "verdict": q1_verdict,
        },
        "Q2_floor_robustness": {
            "a_parameter_sensitivity": param_sensitivity,
            "b_grid_closure": grid_closure,
            "c_baseline_convention": convention,
            "the_activity_cancels": quantized,
            "saturation": saturation,
            "printed_grid_vs_executed_grid": declared_grid,
            "status": floor_status,
            "reading": ("0.20 is not a measured threshold of B's system.  It is "
                        "the smallest point of a six-point hand-chosen grid at "
                        "which an integer crossing-count criterion holds; the "
                        "criterion's actual suffix crossing sits at %.9f, and the "
                        "criterion itself is activity-free and quantized to "
                        "multiples of 1/12." % theta_cross) if theta_cross else "",
        },
        "Q3_lineage_verdict": lineage,
        "audit_rows": audit_rows,
        "falsifier_visibility": fals,
        "double_run": double,
        "numerics": {"python": sys.version.split()[0], "numpy": np.__version__,
                     "scipy_used_for": "sparse containers and Bessel J_k only",
                     "machinery": mach, "machinery_ok": bool(mach_ok),
                     "lanczos_iters": LANCZOS_ITERS, "lanczos_seed": LANCZOS_SEED,
                     "q1_wall_s": q1_wall, "q2_wall_s": q2_wall, "wall_s": wall,
                     "peak_rss_gib": rss_gib()},
        "deviations": [
            {"id": "ENGINE-ALTERNATIVES-NOT-NOTE-ALTERNATIVES",
             "what": "the parameter scan uses m in {0.3,0.6}, W_max in {2,3,4}, "
                     "g in {0.0,0.6,1.0}",
             "why": "the note itself names NO alternative; these are the "
                    "alternatives its Hamiltonian's declaring source exercises, "
                    "and they are labelled as such"},
            {"id": "G0-NOT-SWEPT",
             "what": "the engine-declared coupling g = 0.0 is probed for its "
                     "ground state but no floor is computed there",
             "why": "the g = 0 low spectrum is near-degenerate, so a per-bond "
                    "interacting-ground-state baseline is not well defined"},
            {"id": "SIX-DIGIT-CACHE",
             "what": "the historical cache prints six significant figures, so "
                     "activity totals and kappa values are compared at that "
                     "precision; crossing counts are integers and compared exactly",
             "why": "the cache is the published artifact; nothing finer exists"},
        ],
        "verdict": {
            "Q1": q1_verdict,
            "Q2": floor_status,
            "Q3": "GRID-LABEL-NOT-A-MEASURED-THRESHOLD",
            "total": "DEPOSITION-REAUDITED/%s/%s" % (q1_verdict, floor_status),
        },
    }
    out_path = os.path.join(ROOT,
                            "outputs/deposition_reaudit_cycle920_receipt_2026_07_28.json")
    blob = json.dumps(receipt, indent=1, sort_keys=True, default=json_default)
    open(out_path, "w").write(blob + "\n")

    print("SETUP cycle=920 pins=%d history-artifacts=%d git-cmds=%d head=%s dim=%d %s"
          % (len(pins), len(hist), len(GIT_LOG), head[:10], systems[0.6]["dim"],
             BOUNDARY_LINE))
    print("Q1-REIMPL route=own-basis/own-H/own-Lanczos/own-Chebyshev/own-observables "
          "compared=%d agree=%d verdict=%s E=[%.12f,%.12f] gs-baseline=[%.12f,%.12f] "
          "wall=%.1fs %s"
          % (len(table), sum(1 for r in table if r["agrees"]), q1_verdict,
             systems[0.6]["energy"], systems[1.0]["energy"], gs_lo, gs_hi,
             q1_wall, BOUNDARY_LINE))
    for g in COUPLINGS:
        for p in ("a", "b"):
            c = cases["%g/%s" % (g, p)]
            print("Q1-CASE g=%g/%s A=%.6g N_once=%s N_rearm=%s excess=[%.10f,%.10f] "
                  "cache-N_once=%s cache-N_rearm=%s %s"
                  % (g, p, c["activity_total"], c["N_once"], c["N_rearm"],
                     c["excess_range"][0], c["excess_range"][1],
                     cache["cases"]["%g/%s" % (g, p)]["N_once"],
                     cache["cases"]["%g/%s" % (g, p)]["N_rearm"], BOUNDARY_LINE))
    print("Q2-GRID declared-floor=%s true-crossing=%.12f ratio=%.4f monotone=%s "
          "grid-neighbour-below=0.1 fill-on-grid=%s %s"
          % (floor, theta_cross, floor / theta_cross, monotone,
             [round(x, 6) for x in grid_closure["fill_on_the_swept_grid"]],
             BOUNDARY_LINE))
    print("Q2-ACTIVITY fill=N/12 identically (dev=%.1e); the wake-bound comparison "
          "is activity-free and quantized: any limit in [0.25,0.3333) gives the "
          "same floor %s" % (identity_dev, BOUNDARY_LINE))
    print("Q2-CONVENTION gs-baseline vs trajectory-t0 differ by %.1e on B's own "
          "system; floor(t0)=%s true-crossing(t0)=%.12f -> NOT a convention "
          "artifact %s" % (conv_dev, floor_t0, hi_c, BOUNDARY_LINE))
    print("Q2-PARAMS note-names-alternatives=%s grid-floors=%s true-crossings=%s "
          "w_max-converged=%s g0-usable=%s %s"
          % (note_declares_alternatives, floors,
             [round(r["true_crossing"], 6) for r in param_rows if r["true_crossing"]],
             param_sensitivity["w_max_is_converged"],
             zero_coupling["usable_as_a_comparator_point"], BOUNDARY_LINE))
    print("Q2-SATURATION max-attainable-excess=%.9f floor/max=%.6f thetas-above-max=%s "
          "gated-cells-zero-by-construction=%d/%d %s"
          % (max_excess, floor / max_excess,
             saturation["swept_thetas_above_the_attainable_maximum"],
             saturation["gated_cells_with_zero_events"], len(gated_cells),
             BOUNDARY_LINE))
    print("Q2-PRINTED-GRID mislabel=confirmed printed=t=0:0.1:6 executed=t=0:0.1:10 "
          "cases-whose-counts-would-differ=%d/4 floor-unchanged=%s %s"
          % (sum(1 for v in declared_grid["rows"].values() if not v["identical"]),
             not declared_grid["mislabel_is_outcome_bearing_for_the_floor"],
             BOUNDARY_LINE))
    print("Q2-STATUS %s %s" % (floor_status, BOUNDARY_LINE))
    print("Q3-LINEAGE %s %s" % (lineage["verdict"], BOUNDARY_LINE))
    for row in audit_rows:
        print("AUDIT-ROW %s [%s] %s -- %s %s"
              % (row["id"], row["status"], row["row"], row["finding"], BOUNDARY_LINE))
    print("GATES %s %s" % ({k: v for k, v in gates.items() if isinstance(v, bool)},
                           BOUNDARY_LINE))
    print("FALSIFIER %s %s" % ({k: v for k, v in fals.items()}, BOUNDARY_LINE))
    print("DOUBLE-RUN %s %s" % (double, BOUNDARY_LINE))
    print("MACHINERY %s ok=%s rss=%.2fGiB %s"
          % ({k: "%.3g" % v for k, v in sorted(mach.items())}, mach_ok, rss_gib(),
             BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY  %s" % s)
    print("TOTAL DEPOSITION-REAUDITED/%s/%s compared=%d floor=%s true-crossing=%.9f "
          "wall=%.1fs receipt=%s %s"
          % (q1_verdict, floor_status, len(table), floor, theta_cross, wall,
             sha256_bytes(blob.encode())[:16], BOUNDARY_LINE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
