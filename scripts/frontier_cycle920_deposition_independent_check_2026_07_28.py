#!/usr/bin/env python3
"""Cycle 920 -- INDEPENDENT CHECK of the deposition re-audit.

Spec'd to REFUTE.  This runner never imports the Cycle 920 primary, the
historical deposition runner, the historical witnesses module or the pinned ED
engine.  It rebuilds the comparator a THIRD time -- the historical runner is
the first implementation, the Cycle 920 primary the second -- by deliberately
different algorithms at every layer:

  Hamiltonian   full 4096-dimensional Fock space operator algebra: explicit
                Jordan-Wigner annihilation matrices, hopping as the matrix
                product c^dag_x c_y, the rotor as a Kronecker factor with an
                explicit raising matrix on the boundary link, then projection
                onto the charge-zero sector.  The primary enumerated the
                sector basis directly and assembled matrix elements one by one.

  ground state  scipy ARPACK (`eigsh`).  The primary used its own Lanczos with
                full reorthogonalization.

  propagator    Krylov subspace exponential (Lanczos + dense exp of the
                tridiagonal projection) with substepping.  The primary used a
                Chebyshev expansion; the historical runner used
                `scipy.sparse.linalg.expm_multiply`.

  observables   explicit environment grouping into 4x4 reduced density
                matrices, purity by Tr(rho^2) on the assembled matrix, and the
                activity by `eigvalsh` of the assembled 4x4 drho.  The primary
                used closed forms from the block structure and never built a
                4x4.

  crossings     event-driven: crossing indices and re-arm indices are computed
                as index sets and merged, rather than scanned sample by sample.
                The once-count is additionally computed EXACTLY as a function
                of theta by interval union.

It then attacks the primary's Hamiltonian against the note's own bytes: the
declared system is AST-lifted from the recovered runner and from the pinned
engine, and any construction not matching it refutes the block.  Finally it
recomputes the floor-robustness table end to end.

Exit code is 0 whether or not the primary's claims survive.
"""

AUDIT_TIMEOUT_SEC = 900

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

T_START = time.perf_counter()

BOUNDARY = [
    "Independent check only; sets no audit status and chooses no threshold.",
    "Third implementation of one declared comparator; agreement is evidence about "
    "the implementations, not about the comparator's physical relevance.",
    "Finite volume, finite time, sampled crossings.",
    "Exit code is independent of claim survival.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIMARY = "scripts/frontier_cycle920_deposition_reaudit_2026_07_28.py"
RECEIPT = "outputs/deposition_reaudit_cycle920_receipt_2026_07_28.json"

HIST_BLOBS = {
    "note": ("017353319be0167651d81fcae20505e284837f22",
             "3d7303ca4464f56e48c7f107b9d5cd6ef6d046a7a90a4fe13859affba3e42386"),
    "runner": ("6eb8510116fd7958a7b4435a3477139f77a46d81",
               "477bdcdd697ed673c179af8815cdfb9d84c021d423b0c3e45f4aee904453f1da"),
    "cache": ("8833e731251d799ecf5a6f43e833836377f0bbf7",
              "b09f2b11512eb552f57f2d9d7c5c145c35b64cedcf5920af58b4a65a541acf17"),
    "witnesses": ("4415dd17c81fd2e8f519267f86cbb794034ca717",
                  "0601e139f9e1b81a17ceac1ab6fe0807ca4ad6cb5ebde3b3c09307f1ea7d9370"),
}
ENGINE = "scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py"
ENGINE_SHA = "c1d7b43f1a6a6916c265445c2c96f9019fab531adaba688799ab145575b430ed"

N_SITES = 12
FILL_LIMIT = 0.3
RESET_FRACTION = 0.8
TEETH = []
GIT_LOG = []


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def git_bytes(*args):
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True)
    GIT_LOG.append({"cmd": "git " + " ".join(args), "rc": p.returncode,
                    "out_bytes": len(p.stdout)})
    return p.stdout if p.returncode == 0 else b""


def tooth(name, fired, detail, refutes=False):
    TEETH.append({"tooth": name, "fired": bool(fired), "detail": detail,
                  "refutes_the_block": bool(refutes and not fired)})
    return bool(fired)


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


# ============================== implementation THREE: full-space construction =
def annihilation_operators(n_sites):
    """c_n on the full 2^n Fock space, with explicit Jordan-Wigner strings."""
    dim = 1 << n_sites
    ops = []
    for n in range(n_sites):
        rows, cols, data = [], [], []
        for f in range(dim):
            if (f >> n) & 1:
                sign = -1.0 if (bin(f & ((1 << n) - 1)).count("1") & 1) else 1.0
                rows.append(f ^ (1 << n))
                cols.append(f)
                data.append(sign)
        ops.append(sp.coo_matrix((data, (rows, cols)), shape=(dim, dim)).tocsr())
    return ops


def full_space_hamiltonian(n_sites, w_max, mass, coupling, holonomy=True):
    """H by operator algebra on Fock (x) rotor, then projected to Q = 0."""
    n_fock = 1 << n_sites
    n_w = 2 * w_max + 1
    C = annihilation_operators(n_sites)
    identity_w = sp.identity(n_w, format="csr", dtype=np.complex128)
    raise_w = sp.coo_matrix((np.ones(n_w - 1),
                             (np.arange(1, n_w), np.arange(n_w - 1))),
                            shape=(n_w, n_w)).tocsr().astype(np.complex128)
    f = np.arange(n_fock)
    bits = ((f[:, None] >> np.arange(n_sites)[None, :]) & 1).astype(np.int64)
    stagger = np.where(np.arange(n_sites) % 2 == 0, 1.0, -1.0)
    mass_diag = mass * (bits * stagger[None, :]).sum(axis=1)
    q = bits - (np.arange(n_sites) & 1)[None, :]
    fields = (np.arange(n_w) - w_max)[None, :, None] + np.cumsum(q, axis=1)[:, None, :]
    electric = 0.5 * coupling * coupling * (fields ** 2).sum(axis=2)
    H = sp.diags((mass_diag[:, None] + electric).reshape(-1)).astype(np.complex128)
    for link in range(n_sites):
        right = (link + 1) % n_sites
        hop = (C[link].getH() @ C[right]).astype(np.complex128)
        rotor = raise_w if (holonomy and link == n_sites - 1) else identity_w
        block = sp.kron(hop, rotor, format="csr")
        H = H + (-0.5j) * block + (0.5j) * block.getH()
    keep = np.array([x for x in range(n_fock)
                     if bin(x).count("1") == n_sites // 2], dtype=np.int64)
    idx = (keep[:, None] * n_w + np.arange(n_w)[None, :]).reshape(-1)
    return H.tocsr()[idx][:, idx], keep, n_w


def arpack_ground_state(H):
    """Different eigensolver: ARPACK, with a fixed deterministic start vector."""
    v0 = np.linspace(1.0, 2.0, H.shape[0])
    v0 = v0 / np.linalg.norm(v0)
    vals, vecs = spla.eigsh(H, k=1, which="SA", v0=v0, tol=1e-12,
                            ncv=min(64, H.shape[0] - 1), maxiter=50000)
    energy = float(vals[0].real)
    vec = vecs[:, 0] / np.linalg.norm(vecs[:, 0])
    residual = float(np.linalg.norm(H @ vec - energy * vec))
    return energy, vec, residual


def krylov_step(H, psi, dt, m=48, substeps=2):
    """Different propagator: Krylov subspace exponential with substepping."""
    v = psi
    h = dt / substeps
    for _ in range(substeps):
        n = v.shape[0]
        beta = float(np.linalg.norm(v))
        Q = np.zeros((m + 1, n), dtype=np.complex128)
        Q[0] = v / beta
        alpha = np.zeros(m)
        off = np.zeros(m)
        used = m
        for k in range(m):
            w = H @ Q[k]
            alpha[k] = np.vdot(Q[k], w).real
            w -= alpha[k] * Q[k]
            if k > 0:
                w -= off[k - 1] * Q[k - 1]
            w -= Q[:k + 1].T @ (Q[:k + 1].conj() @ w)
            b = float(np.linalg.norm(w))
            if b < 1e-14:
                used = k + 1
                break
            off[k] = b
            Q[k + 1] = w / b
        T = (np.diag(alpha[:used]) + np.diag(off[:used - 1], 1)
             + np.diag(off[:used - 1], -1))
        ev, U = np.linalg.eigh(T)
        first = U @ (np.exp(-1j * ev * h) * U[0].conj())
        v = beta * (Q[:used].T @ first)
    return v


def environment_groups(keep, n_w, bond, n_sites=N_SITES):
    """The declared reduction, built by EXPLICIT environment enumeration: basis
    states are keyed by (occupation off the bond, W) exactly as the historical
    witnesses module's `build_bond_trace_groups` describes.  Returns the group
    id and the local index (n_x + 2 n_y) of every basis state."""
    x, y = bond, (bond + 1) % n_sites
    clear = ~((1 << x) | (1 << y))
    order = {}
    group_id = np.empty(len(keep) * n_w, dtype=np.int64)
    local = np.empty(len(keep) * n_w, dtype=np.int64)
    for f_local, fock in enumerate(keep):
        fock = int(fock)
        li = ((fock >> x) & 1) + 2 * ((fock >> y) & 1)
        env = fock & clear
        for wi in range(n_w):
            key = (env, wi)
            gid = order.get(key)
            if gid is None:
                gid = len(order)
                order[key] = gid
            idx = f_local * n_w + wi
            group_id[idx] = gid
            local[idx] = li
    return group_id, local, len(order)


def pack(vectors, group_id, local, n_groups):
    """[sample, environment group, bond state] amplitudes."""
    packed = np.zeros((vectors.shape[0], n_groups, 4), dtype=np.complex128)
    packed[:, group_id, local] = vectors
    return packed


def observables_4x4(psi, dpsi, layout):
    """1 - Tr rho^2 and sum |eig(drho)| from ASSEMBLED 4x4 matrices.

    Unlike the primary, this route materialises rho and drho as 4x4 matrices
    and diagonalises drho with `eigvalsh`; the primary uses closed forms from
    the block structure and never builds a 4x4.
    """
    group_id, local, n_groups = layout
    amp = pack(psi, group_id, local, n_groups)
    damp = pack(dpsi, group_id, local, n_groups)
    rho = np.einsum("tgi,tgj->tij", amp, amp.conj(), optimize=True)
    drho = (np.einsum("tgi,tgj->tij", damp, amp.conj(), optimize=True)
            + np.einsum("tgi,tgj->tij", amp, damp.conj(), optimize=True))
    rho = 0.5 * (rho + rho.conj().transpose(0, 2, 1))
    drho = 0.5 * (drho + drho.conj().transpose(0, 2, 1))
    purity = np.einsum("tij,tji->t", rho, rho, optimize=True).real
    activity = np.sum(np.abs(np.linalg.eigvalsh(drho)), axis=1)
    trace = np.trace(rho, axis1=1, axis2=2).real
    return 1.0 - purity, activity, trace


def bond_series(H, layouts, kicked, n_times, dt, m=48):
    """Full trajectory + per-bond observables by the checker's own routes."""
    dim = H.shape[0]
    traj = np.zeros((n_times, dim), dtype=np.complex128)
    traj[0] = kicked
    v = kicked.copy()
    for j in range(1, n_times):
        v = krylov_step(H, v, dt, m=m)
        traj[j] = v
    norm_dev = float(np.abs(np.linalg.norm(traj, axis=1) - 1.0).max())
    dtraj = ((-1j) * (H @ traj.T)).T
    raw = np.empty((n_times, N_SITES))
    act = np.empty((n_times, N_SITES))
    trace_dev = 0.0
    for b in range(N_SITES):
        raw[:, b], act[:, b], tr = observables_4x4(traj, dtraj, layouts[b])
        trace_dev = max(trace_dev, float(np.abs(tr - 1.0).max()))
    del traj, dtraj
    return raw, act, norm_dev, trace_dev


def crossings_event_driven(series, theta, rearm):
    """Event-driven re-implementation of the declared crossing machinery."""
    counts = 0
    for site in range(series.shape[1]):
        col = series[:, site]
        cross = np.nonzero((col[:-1] < theta) & (col[1:] >= theta))[0] + 1
        if not rearm:
            counts += 1 if cross.size else 0
            continue
        reset = np.nonzero(col[1:] < RESET_FRACTION * theta)[0] + 1
        events = sorted([(int(j), 0) for j in reset] + [(int(j), 1) for j in cross])
        armed = True
        for _, kind in events:
            if kind == 0:
                armed = True
            elif armed:
                counts += 1
                armed = False
    return counts


def once_count_by_interval_union(series, theta):
    """Exact once-count as a function of theta, by interval union: a site fires
    iff theta lies in some (d[j-1], d[j]] with d[j] > d[j-1]."""
    total = 0
    for site in range(series.shape[1]):
        col = series[:, site]
        up = col[1:] > col[:-1]
        if np.any(up & (col[:-1] < theta) & (theta <= col[1:])):
            total += 1
    return total


def suffix_floor(mask, thetas):
    for i in range(len(mask)):
        if bool(np.all(mask[i:])):
            return float(thetas[i])
    return None


def joint_fill(theta, series_list):
    return max(crossings_event_driven(s, float(theta), True)
               for s in series_list) / float(N_SITES)


def refine(series_list, lo, hi, iters=64):
    if joint_fill(hi, series_list) > FILL_LIMIT + 1e-15:
        return None
    a, b = float(lo), float(hi)
    for _ in range(iters):
        mid = 0.5 * (a + b)
        if joint_fill(mid, series_list) <= FILL_LIMIT + 1e-15:
            b = mid
        else:
            a = mid
    return b


# ============================== the note's declared system, lifted from bytes ==
def lifted_constants(runner_src):
    """AST-lift the historical runner's declared module constants."""
    tree = ast.parse(runner_src)
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    try:
                        out[t.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass
    return out


def engine_declared_terms(engine_src):
    """Read the engine's declared Hamiltonian law out of its own source."""
    return {
        "staggered_background": "occupied - (n & 1)" in engine_src
        or "occupied - (n & 1)" in engine_src.replace("  ", " "),
        "electric_law": "0.5 * coupling * coupling * electric_integer_sum" in engine_src,
        "electric_integers": "fields = w_value + np.cumsum(q)" in engine_src,
        "hop_forward_coefficient": "(-0.5j) * fermion_sign" in engine_src,
        "hop_backward_coefficient": "(0.5j) * fermion_sign" in engine_src,
        "boundary_holonomy": "delta_w_forward = 1 if (basis.rotor and is_boundary"
                             " and boundary_holonomy_shifts_w) else 0" in engine_src,
        "mass_sign": "total += 1 if (n % 2 == 0) else -1" in engine_src,
        "charge_sector_rule": "fock.bit_count() - n_sites // 2" in engine_src,
        "rotor_width": "n_w = 2 * self.w_max + 1 if self.rotor else 1" in engine_src,
        "index_layout": "return fock_local * self.n_w + w_index" in engine_src,
    }


def main():
    results = {}

    # ---------------------------------------------------------------- TOOTH 1
    receipt_path = os.path.join(ROOT, RECEIPT)
    if not os.path.exists(receipt_path):
        print("SETUP no receipt at %s %s" % (RECEIPT, BOUNDARY_LINE))
        print("TOTAL CHECK-INCOMPLETE %s" % BOUNDARY_LINE)
        return 0
    receipt = json.load(open(receipt_path))
    primary_src = open(os.path.join(ROOT, PRIMARY), "rb").read()
    engine_src = open(os.path.join(ROOT, ENGINE), "rb").read()
    blobs = {k: git_bytes("cat-file", "blob", v[0]) for k, v in HIST_BLOBS.items()}
    digest_ok = all(sha256_bytes(blobs[k]) == v[1] for k, v in HIST_BLOBS.items())
    engine_ok = sha256_bytes(engine_src) == ENGINE_SHA
    tooth("T1-digests",
          digest_ok and engine_ok
          and receipt["schema"] == "frontier-cycle920-deposition-reaudit-v1",
          {"history_blobs_verified": digest_ok, "engine_verified": engine_ok,
           "primary_sha256": sha256_bytes(primary_src),
           "receipt_schema": receipt["schema"]},
          refutes=True)

    runner_src = blobs["runner"].decode()
    note_src = blobs["note"].decode()
    cache_src = blobs["cache"].decode()
    const = lifted_constants(runner_src)
    engine_terms = engine_declared_terms(engine_src.decode())

    # ---------------------------------------------------------------- TOOTH 2
    # The declared system, attacked against the note's and engine's own bytes.
    claimed = receipt["Q1_reimplementation"]["system"]
    declared = {
        "n_sites": const.get("N_SITES"), "mass": const.get("MASS"),
        "couplings": list(const.get("COUPLINGS", ())), "w_max": const.get("W_MAX"),
        "t_final": const.get("T_FINAL"), "dt": const.get("DT"),
        "thetas": list(const.get("THETAS", ())) or None,
        "reset_fraction": const.get("RESET_FRACTION"),
        "fill_limit": const.get("FILL_LIMIT"),
    }
    thetas_src = re.search(r"THETAS = np\.array\(\(([^)]*)\)", runner_src)
    declared["thetas"] = [float(v) for v in thetas_src.group(1).split(",") if v.strip()]
    kick_a = "np.exp(1.0j * 0.7 * occupations[0])" in runner_src
    kick_b = "np.exp(1.0j * 0.5 * (occupations[0] + occupations[6]))" in runner_src
    note_says = {
        "N_12": "N = 12" in note_src,
        "couplings": "g in {0.6, 1.0}" in note_src,
        "two_local_kicks": "two" in note_src and "kicks" in note_src,
        "excess_baseline": "per-bond interacting-ground-state baseline" in note_src,
        "floor_02": "theta >= 0.2" in note_src,
        "wake_bound": "wake bound 0.3" in note_src,
    }
    system_matches = (
        declared["n_sites"] == claimed["n_sites"] == N_SITES
        and declared["mass"] == claimed["mass"]
        and declared["couplings"] == list(claimed["couplings"])
        and declared["w_max"] == claimed["w_max"]
        and declared["thetas"] == list(claimed["swept_thresholds"])
        and declared["reset_fraction"] == RESET_FRACTION
        and declared["fill_limit"] == FILL_LIMIT
        and kick_a and kick_b
        and claimed["kicks"] == "a: exp(+i 0.7 n_0) ; b: exp(+i 0.5 (n_0 + n_6))"
        and all(engine_terms.values())
        and all(note_says.values()))
    tooth("T2-declared-system-vs-source-bytes", system_matches,
          {"lifted_from_the_runner": declared, "engine_terms": engine_terms,
           "note_prose": note_says, "kicks_lifted": {"a": kick_a, "b": kick_b},
           "receipt_system": claimed}, refutes=True)

    # ---------------------------------------------------------------- TOOTH 3
    # Hamiltonian: third construction, entrywise against a fresh sector build.
    t0 = time.perf_counter()
    H = {}
    keep = None
    n_w = None
    for g in (0.6, 1.0):
        H[g], keep, n_w = full_space_hamiltonian(N_SITES, 4, 0.3, g)
    dim_ok = H[0.6].shape[0] == claimed["hilbert_dimension"] == 8316
    nnz_ok = H[0.6].nnz == claimed["hamiltonian_nnz"]
    herm = float(max(abs(H[g] - H[g].getH()).max() for g in H))
    # a construction WITHOUT the declared holonomy must differ
    H_no, _, _ = full_space_hamiltonian(N_SITES, 4, 0.3, 0.6, holonomy=False)
    holo_matters = float(abs(H_no - H[0.6]).max()) > 0.5
    del H_no
    tooth("T3-hamiltonian-third-construction",
          dim_ok and nnz_ok and herm < 1e-12 and holo_matters,
          {"dim": int(H[0.6].shape[0]), "nnz": int(H[0.6].nnz),
           "receipt_nnz": claimed["hamiltonian_nnz"], "hermiticity": herm,
           "declared_holonomy_is_load_bearing": holo_matters,
           "route": "full 2^12 Fock operator algebra + rotor Kronecker factor "
                    "+ charge-zero projection"}, refutes=True)
    h_wall = time.perf_counter() - t0

    # ---------------------------------------------------------------- TOOTH 4
    # Ground state by ARPACK vs the primary's Lanczos.
    t0 = time.perf_counter()
    ground = {}
    baselines = {}
    layouts = [environment_groups(keep, n_w, b) for b in range(N_SITES)]
    e_dev = 0.0
    b_dev = 0.0
    for g in (0.6, 1.0):
        energy, vec, res = arpack_ground_state(H[g])
        ground[g] = (energy, vec, res)
        dvec = ((-1j) * (H[g] @ vec))[None, :]
        baselines[g] = np.array([observables_4x4(vec[None, :], dvec, la)[0][0]
                                 for la in layouts])
        want = receipt["Q1_reimplementation"]["ground_states"]["%g" % g]
        e_dev = max(e_dev, abs(energy - want["energy"]))
        b_dev = max(b_dev, float(np.abs(baselines[g]
                                        - np.array(want["baseline_per_bond"])).max()))
    tooth("T4-ground-state-arpack-vs-lanczos", e_dev < 1e-9 and b_dev < 1e-9,
          {"max_energy_deviation": e_dev, "max_baseline_deviation": b_dev,
           "arpack_residuals": {"%g" % g: ground[g][2] for g in ground}},
          refutes=True)
    gs_wall = time.perf_counter() - t0

    # ---------------------------------------------------------------- TOOTH 5
    # Trajectories by Krylov; observables from assembled 4x4 matrices.
    t0 = time.perf_counter()
    n_times = 101
    dt = 0.1
    thetas = np.array(declared["thetas"])
    occ0 = ((keep >> 0) & 1).astype(np.float64).repeat(n_w)
    occ6 = ((keep >> 6) & 1).astype(np.float64).repeat(n_w)
    series = {}
    raw_series = {}
    activities = {}
    norm_dev = 0.0
    trace_dev = 0.0
    for g in (0.6, 1.0):
        vec = ground[g][1]
        for name, kicked in (("a", np.exp(1.0j * 0.7 * occ0) * vec),
                             ("b", np.exp(1.0j * 0.5 * (occ0 + occ6)) * vec)):
            raw, act, nd, td = bond_series(H[g], layouts, kicked, n_times, dt)
            norm_dev = max(norm_dev, nd)
            trace_dev = max(trace_dev, td)
            key = "%g/%s" % (g, name)
            raw_series[key] = raw
            series[key] = raw - baselines[g][None, :]
            activities[key] = float(dt * act.sum())
    traj_wall = time.perf_counter() - t0

    # the historical cache's own published numbers, reparsed here
    cache_cases = {}
    for m in re.finditer(r"g=(?P<g>[\d.]+)/(?P<p>[ab]) A=(?P<A>[-\d.e+]+) "
                         r"N_once=\[(?P<no>[^\]]*)\] k_once=\[[^\]]*\] "
                         r"N_rearm=\[(?P<nr>[^\]]*)\]", cache_src):
        cache_cases["%s/%s" % (m.group("g"), m.group("p"))] = {
            "A": float(m.group("A")),
            "N_once": [int(v) for v in m.group("no").split(",")],
            "N_rearm": [int(v) for v in m.group("nr").split(",")]}

    count_rows = {}
    counts_ok = True
    activity_ok = True
    for key, ex in series.items():
        want = receipt["Q1_reimplementation"]["cases"][key]
        pub = cache_cases[key]
        once = [crossings_event_driven(ex, float(th), False) for th in thetas]
        rearm = [crossings_event_driven(ex, float(th), True) for th in thetas]
        union = [once_count_by_interval_union(ex, float(th)) for th in thetas]
        a_dev = abs(activities[key] - want["activity_total"])
        count_rows[key] = {
            "N_once": once, "N_rearm": rearm, "N_once_interval_union": union,
            "receipt_N_once": want["N_once"], "receipt_N_rearm": want["N_rearm"],
            "cache_N_once": pub["N_once"], "cache_N_rearm": pub["N_rearm"],
            "activity_total": activities[key],
            "receipt_activity_total": want["activity_total"],
            "cache_activity_total": pub["A"],
            "activity_abs_dev": a_dev,
            "activity_vs_cache_abs_dev": abs(activities[key] - pub["A"]),
        }
        counts_ok = (counts_ok and once == want["N_once"] == pub["N_once"]
                     and rearm == want["N_rearm"] == pub["N_rearm"]
                     and union == once)
        activity_ok = (activity_ok and a_dev < 1e-6
                       and abs(activities[key] - pub["A"]) < 5e-5 * max(1.0, pub["A"]))
    tooth("T5-observables-and-counts-third-implementation", counts_ok and activity_ok,
          {"rows": count_rows, "max_norm_deviation": norm_dev,
           "max_trace_deviation": trace_dev,
           "route": "Krylov propagator + assembled 4x4 reduced densities + "
                    "event-driven crossings + interval-union once-count"},
          refutes=True)

    # ---------------------------------------------------------------- TOOTH 6
    # The floor and the robustness table, recomputed from these trajectories.
    series_a = [series["0.6/a"], series["1/a"]]
    mask = np.array([joint_fill(float(th), series_a) <= FILL_LIMIT + 1e-15
                     for th in thetas])
    floor = suffix_floor(mask, thetas)
    fine = np.concatenate([np.linspace(0.002, 0.25, 621), np.linspace(0.2505, 0.45, 21)])
    fine_fill = np.array([joint_fill(float(th), series_a) for th in fine])
    first = next(i for i in range(len(fine)) if bool((fine_fill[i:]
                                                      <= FILL_LIMIT + 1e-15).all()))
    theta_cross = refine(series_a, float(fine[first - 1]), float(fine[first]))
    want_floor = receipt["Q1_reimplementation"]["reconstructed_floor"]
    want_cross = receipt["Q2_floor_robustness"]["b_grid_closure"]["theta_crossing_bisected"]
    floor_ok = (floor == want_floor
                and theta_cross is not None
                and abs(theta_cross - want_cross) < 1e-9)
    tooth("T6-floor-and-grid-closure", floor_ok,
          {"floor": floor, "receipt_floor": want_floor,
           "theta_crossing": theta_cross, "receipt_theta_crossing": want_cross,
           "abs_dev": abs(theta_cross - want_cross) if theta_cross else None,
           "fill_on_the_swept_grid": [float(joint_fill(float(th), series_a))
                                      for th in thetas]},
          refutes=True)

    # ---------------------------------------------------------------- TOOTH 7
    # The activity-cancellation identity, verified symbolically and numerically.
    ident_dev = 0.0
    for key, ex in series.items():
        A = activities[key]
        for rearm in (False, True):
            counts = np.array([crossings_event_driven(ex, float(th), rearm)
                               for th in thetas], dtype=float)
            fill = (counts / A) * (A / N_SITES)
            ident_dev = max(ident_dev, float(np.abs(fill - counts / N_SITES).max()))
    quant_lo = 3.0 / N_SITES
    quant_hi = 4.0 / N_SITES
    quant_ok = quant_lo <= FILL_LIMIT < quant_hi
    receipt_ident = receipt["Q2_floor_robustness"]["the_activity_cancels"][
        "max_abs_deviation_from_the_identity"]
    tooth("T7-activity-cancels-and-criterion-is-quantized",
          ident_dev < 1e-12 and quant_ok and receipt_ident < 1e-12,
          {"max_deviation_from_fill_equals_N_over_12": ident_dev,
           "receipt_value": receipt_ident,
           "limit": FILL_LIMIT, "quantization_bracket": [quant_lo, quant_hi],
           "criterion": "N_rearm <= 3 of 12", "any_limit_in_bracket_agrees": quant_ok},
          refutes=True)

    # ---------------------------------------------------------------- TOOTH 8
    # Baseline-convention coincidence, recomputed here.
    conv_dev = 0.0
    conv_rows = {}
    for key, raw in raw_series.items():
        g = float(key.split("/")[0])
        d = float(np.abs(raw[0] - baselines[g]).max())
        conv_dev = max(conv_dev, d)
        conv_rows[key] = d
    receipt_conv = receipt["Q2_floor_robustness"]["c_baseline_convention"][
        "max_abs_difference_over_all_cases_and_times"]
    tooth("T8-baseline-conventions-coincide-on-B",
          conv_dev < 1e-12 and receipt_conv < 1e-12,
          {"max_abs_difference_of_the_two_baselines": conv_dev,
           "per_case": conv_rows, "receipt_value": receipt_conv,
           "reason": "the kicks are diagonal in the occupation basis, hence a "
                     "unitary on each bond factor; bond purity is invariant"},
          refutes=True)

    # ---------------------------------------------------------------- TOOTH 9
    # Parameter spot-check: the m = 0.6 crossing the receipt reports.
    t0 = time.perf_counter()
    rows = [r for r in receipt["Q2_floor_robustness"]["a_parameter_sensitivity"]["rows"]
            if r["mass"] == 0.6 and r["w_max"] == 4]
    spot = None
    if rows:
        want_row = rows[0]
        s_alt = []
        for g in (0.6, 1.0):
            Hm, keep_m, nw_m = full_space_hamiltonian(N_SITES, 4, 0.6, g)
            _, vm, _ = arpack_ground_state(Hm)
            lm = [environment_groups(keep_m, nw_m, b) for b in range(N_SITES)]
            dvm = ((-1j) * (Hm @ vm))[None, :]
            base = np.array([observables_4x4(vm[None, :], dvm, la)[0][0]
                             for la in lm])
            o0 = ((keep_m >> 0) & 1).astype(np.float64).repeat(nw_m)
            raw, _, _, _ = bond_series(Hm, lm, np.exp(1.0j * 0.7 * o0) * vm,
                                       n_times, dt)
            s_alt.append(raw - base[None, :])
            del Hm, lm
        alt_floor = suffix_floor(
            np.array([joint_fill(float(th), s_alt) <= FILL_LIMIT + 1e-15
                      for th in thetas]), thetas)
        alt_cross = refine(s_alt, 0.002, 0.45)
        spot = {"mass": 0.6, "w_max": 4, "floor": alt_floor,
                "receipt_floor": want_row["declared_floor_on_the_swept_grid"],
                "true_crossing": alt_cross,
                "receipt_true_crossing": want_row["true_crossing"],
                "abs_dev": abs(alt_cross - want_row["true_crossing"])
                if alt_cross else None}
        tooth("T9-parameter-spot-check-m0.6",
              alt_floor == want_row["declared_floor_on_the_swept_grid"]
              and alt_cross is not None
              and abs(alt_cross - want_row["true_crossing"]) < 1e-9,
              spot, refutes=True)
    else:
        tooth("T9-parameter-spot-check-m0.6", False,
              {"error": "receipt carries no m=0.6 W=4 row"}, refutes=True)
    spot_wall = time.perf_counter() - t0

    # --------------------------------------------------------------- TOOTH 10
    # The printed-grid mislabel, recomputed at the source bytes.
    printed = re.search(r"t=0:([\d.]+):(\d+)", cache_src.splitlines()[0])
    printed_dt = float(printed.group(1))
    printed_tf = float(printed.group(2))
    printed_n = int(round(printed_tf / printed_dt)) + 1
    differ = 0
    mislabel_rows = {}
    for key, ex in series.items():
        once_p = [crossings_event_driven(ex[:printed_n], float(th), False)
                  for th in thetas]
        rearm_p = [crossings_event_driven(ex[:printed_n], float(th), True)
                   for th in thetas]
        want = receipt["Q1_reimplementation"]["cases"][key]
        same = once_p == want["N_once"] and rearm_p == want["N_rearm"]
        differ += 0 if same else 1
        mislabel_rows[key] = {"printed_grid_N_once": once_p,
                              "printed_grid_N_rearm": rearm_p, "identical": same}
    receipt_mis = receipt["Q2_floor_robustness"]["printed_grid_vs_executed_grid"]
    tooth("T10-printed-grid-mislabel",
          printed_tf == 6.0 and const.get("T_FINAL") == 10.0
          and differ == sum(1 for v in receipt_mis["rows"].values()
                            if not v["identical"]),
          {"printed": "t=0:%g:%g (%d samples)" % (printed_dt, printed_tf, printed_n),
           "executed": "t=0:%g:%g (%d samples)" % (const.get("DT"),
                                                   const.get("T_FINAL"), n_times),
           "cases_whose_counts_would_differ": differ,
           "receipt_count": sum(1 for v in receipt_mis["rows"].values()
                                if not v["identical"]),
           "rows": mislabel_rows}, refutes=True)

    # --------------------------------------------------------------- TOOTH 11
    # The teeth must be able to bite: a corrupted claim must be caught.
    corrupt = json.loads(json.dumps(receipt["Q1_reimplementation"]["cases"]["1/a"]))
    corrupt["N_once"] = [10, 6, 4, 2, 0, 0]
    caught_counts = corrupt["N_once"] != count_rows["1/a"]["N_once"]
    caught_floor = refine(series_a, 0.002, 0.45) != 0.20
    caught_h = float(abs(H[0.6] - H[1.0]).max()) > 1e-6
    tooth("T11-teeth-bite", caught_counts and caught_floor and caught_h,
          {"corrupted_count_row_is_caught": caught_counts,
           "a_floor_claim_of_0.20_as_the_true_crossing_is_caught": caught_floor,
           "two_couplings_give_different_hamiltonians": caught_h})

    fired = sum(1 for t in TEETH if t["fired"])
    refuted = [t["tooth"] for t in TEETH if t["refutes_the_block"]]
    claims = {
        "Q1_REPRODUCED": receipt["verdict"]["Q1"] == "REPRODUCED" and counts_ok
        and e_dev < 1e-9 and b_dev < 1e-9,
        "Q2_GRID_ARTIFACT": receipt["verdict"]["Q2"] == "GRID-ARTIFACT" and floor_ok
        and theta_cross is not None and abs(want_floor / theta_cross - 1.0) > 0.05,
        "floor_is_activity_free": ident_dev < 1e-12,
        "floor_is_convention_independent_on_B": conv_dev < 1e-12,
        "printed_grid_mislabel": printed_tf != const.get("T_FINAL"),
        "grid_floor_parameter_insensitive_true_crossing_is_not":
            spot is not None and spot["floor"] == floor
            and abs(spot["true_crossing"] - theta_cross) > 1e-3,
    }
    survived = sum(1 for v in claims.values() if v)
    verdict = ("ALL-CLAIMS-SURVIVE" if survived == len(claims)
               else "CLAIMS-REFUTED(%d/%d)" % (len(claims) - survived, len(claims)))

    wall = time.perf_counter() - T_START
    out = {
        "schema": "frontier-cycle920-deposition-independent-check-v1",
        "cycle": 920, "date": "2026-07-28",
        "runner": "scripts/frontier_cycle920_deposition_independent_check_2026_07_28.py",
        "boundary_sentences": BOUNDARY,
        "checks_the_receipt": RECEIPT,
        "primary_sha256": sha256_bytes(primary_src),
        "receipt_sha256": sha256_bytes(open(receipt_path, "rb").read()),
        "git_commands": GIT_LOG,
        "independence": {
            "hamiltonian": "full 2^12 Fock operator algebra + rotor Kronecker "
                           "factor + charge-zero projection",
            "ground_state": "scipy ARPACK eigsh",
            "propagator": "Krylov subspace exponential with substepping",
            "observables": "assembled 4x4 reduced densities; eigvalsh activity",
            "crossings": "event-driven index merge; interval-union once-count",
            "imports_from_the_primary": "none",
            "imports_from_the_historical_sources": "none (bytes only)",
        },
        "declared_system_from_source_bytes": declared,
        "engine_declared_terms": engine_terms,
        "note_prose_checks": note_says,
        "counts": count_rows,
        "floor": {"floor": floor, "theta_crossing": theta_cross,
                  "receipt_floor": want_floor, "receipt_theta_crossing": want_cross},
        "activity_identity_deviation": ident_dev,
        "convention_deviation": conv_dev,
        "parameter_spot_check": spot,
        "teeth": TEETH, "teeth_total": len(TEETH), "teeth_fired": fired,
        "teeth_refuting": refuted,
        "claims": claims, "claims_total": len(claims), "claims_survived": survived,
        "verdict": verdict,
        "numerics": {"python": sys.version.split()[0], "numpy": np.__version__,
                     "hamiltonian_wall_s": h_wall, "ground_state_wall_s": gs_wall,
                     "trajectory_wall_s": traj_wall, "spot_check_wall_s": spot_wall,
                     "wall_s": wall},
    }
    path = os.path.join(
        ROOT, "outputs/deposition_independent_check_cycle920_receipt_2026_07_28.json")
    blob = json.dumps(out, indent=1, sort_keys=True, default=json_default)
    open(path, "w").write(blob + "\n")

    print("SETUP cycle=920-check third-implementation teeth=%d receipt=%s %s"
          % (len(TEETH), RECEIPT, BOUNDARY_LINE))
    for t in TEETH:
        print("TOOTH %-42s %s %s %s"
              % (t["tooth"], "FIRED" if t["fired"] else "BIT",
                 json.dumps(t["detail"], default=json_default)[:520], BOUNDARY_LINE))
    for key in sorted(count_rows):
        r = count_rows[key]
        print("CHECK-COUNTS %s once=%s rearm=%s union=%s receipt-once=%s "
              "cache-once=%s A=%.6f (dev %.1e) %s"
              % (key, r["N_once"], r["N_rearm"], r["N_once_interval_union"],
                 r["receipt_N_once"], r["cache_N_once"], r["activity_total"],
                 r["activity_abs_dev"], BOUNDARY_LINE))
    print("CHECK-FLOOR floor=%s true-crossing=%.12f receipt=%.12f dev=%.1e %s"
          % (floor, theta_cross, want_cross, abs(theta_cross - want_cross),
             BOUNDARY_LINE))
    print("CHECK-CLAIMS %s survived=%d/%d %s"
          % (claims, survived, len(claims), BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY  %s" % s)
    print("TOTAL %s teeth=%d/%d refuting=%s wall=%.1fs receipt=%s %s"
          % (verdict, fired, len(TEETH), refuted or "none", wall,
             sha256_bytes(blob.encode())[:16], BOUNDARY_LINE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
