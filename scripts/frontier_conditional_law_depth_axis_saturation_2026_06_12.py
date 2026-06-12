#!/usr/bin/env python3
from __future__ import annotations

import sys

import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if bool(condition):
        PASS_COUNT += 1
        print(f"[PASS] {name}: {detail}")
    else:
        FAIL_COUNT += 1
        print(f"[FAIL] {name}: {detail}")


def finish() -> None:
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


NC = 3
L_RING = 3
EPS, TAU = 0.6, 0.35
K_OCC = 5
ANCHOR_SEED = 4242
ANCHOR_DEPTH_CAP = 11
ANCHOR_ROW = 9
ANCHOR_PREFIX = 3
ANCHOR_PREFIX3 = 0.557
ANCHOR_PREFIX3_TOL = 2.0e-3
ANCHOR_NULL95 = 0.469
ANCHOR_NULL95_TOL = 5.0e-3
DEPTHS = tuple(range(9, 15))
MAX_DEPTH = 14
SEEDS = (4242, 99, 7)
PREFIX_KS = (2, 3, 4)
NULL_DRAWS = 300
NULL_SEED = 7777
RANK_TOL = 1.0e-8
NO_PRUNE_TOL = 1.0e-14
WEIGHT_TOL = 1.0e-10


def build(Lring: int) -> dict[str, object]:
    NM = Lring * NC
    DIM = 2 ** NM
    sz = sp.csr_matrix(np.array([[1, 0], [0, -1]], float))
    sm = sp.csr_matrix(np.array([[0, 1], [0, 0]], float))
    I2 = sp.identity(2, format="csr")

    def ann(j: int) -> sp.csr_matrix:
        out = sp.identity(1, format="csr")
        for k in range(NM):
            out = sp.kron(out, sz if k < j else (sm if k == j else I2), format="csr")
        return out

    A = [ann(j) for j in range(NM)]
    AD = [a.T for a in A]
    h = np.zeros((NM, NM))
    for x in range(Lring):
        for c in range(NC):
            h[x * NC + c, ((x + 1) % Lring) * NC + c] = -1.0
            h[((x + 1) % Lring) * NC + c, x * NC + c] = -1.0
    H = sum(
        (h[i, j] * (AD[i] @ A[j])).astype(complex)
        for i in range(NM)
        for j in range(NM)
        if abs(h[i, j]) > 1e-12
    )
    U_step = expm((-1j * TAU) * H.toarray())
    n0_diag = sum((AD[c] @ A[c]).diagonal().real for c in range(NC))
    Nt = (n0_diag - n0_diag.mean()) / max(abs(n0_diag - n0_diag.mean()))
    kp_diag = np.sqrt((1 + EPS * Nt) / 2).astype(complex)
    km_diag = np.sqrt((1 - EPS * Nt) / 2).astype(complex)
    OPS = [(AD[0 + i] @ A[NC + j]).astype(complex).tocsr() for i in range(3) for j in range(3)]
    ntot_diag = sum((AD[m] @ A[m]).diagonal().real for m in range(NM))
    vac_idx = int(np.argmin(ntot_diag))
    return {
        "NM": NM,
        "DIM": DIM,
        "AD": AD,
        "U": U_step,
        "kp": kp_diag,
        "km": km_diag,
        "OPS": OPS,
        "vac_idx": vac_idx,
    }


def polar_u(M: np.ndarray) -> np.ndarray:
    U, s, Vh = np.linalg.svd(M)
    return U @ Vh


def slater(env: dict[str, object], P: np.ndarray) -> np.ndarray:
    vac = np.zeros(env["DIM"])
    vac[env["vac_idx"]] = 1.0
    psi = vac.astype(complex)
    for k in range(P.shape[1]):
        psi = sum(env["AD"][m].astype(complex) @ (P[m, k] * psi) for m in range(env["NM"]))
    return psi / np.linalg.norm(psi)


def dets_of(env: dict[str, object], states: np.ndarray) -> tuple[np.ndarray, float]:
    B = states.shape[0]
    M = np.empty((B, 9), complex)
    for k in range(9):
        M[:, k] = np.einsum("bi,bi->b", states.conj(), (env["OPS"][k] @ states.T).T)
    M = M.reshape(B, 3, 3)
    sv_min = float(np.min(np.linalg.svd(M, compute_uv=False)[:, -1]))
    return np.array([np.linalg.det(polar_u(m)) for m in M]), sv_min


def prefix(Theta: np.ndarray, w: np.ndarray, kpref: int, lbl: np.ndarray | None = None) -> float:
    B = len(w)
    if lbl is None:
        lbl = np.arange(B) % (2 ** kpref)
    within, wts = [], []
    for v in range(2 ** kpref):
        m = lbl == v
        if w[m].sum() < 1e-12:
            continue
        within.append(abs(complex(np.sum(w[m] * np.exp(1j * Theta[m])) / w[m].sum())))
        wts.append(w[m].sum())
    return float(np.average(within, weights=wts))


def null_p95(Theta: np.ndarray, w: np.ndarray, kpref: int, n_draws: int = NULL_DRAWS, seed: int = NULL_SEED) -> float:
    r = np.random.default_rng(seed)
    B = len(w)
    base = np.arange(B) % (2 ** kpref)
    vals = [prefix(Theta, w, kpref, lbl=base[r.permutation(B)]) for _ in range(n_draws)]
    return float(np.quantile(np.array(vals), 0.95))


def scan(env: dict[str, object], seed: int, depth: int, K_occ: int) -> tuple[tuple[int, float, np.ndarray, np.ndarray], dict[int, tuple[float, np.ndarray, np.ndarray]], float, float, float]:
    rng = np.random.default_rng(seed)
    psi0 = slater(
        env,
        np.linalg.qr(rng.normal(size=(env["NM"], K_occ)) + 1j * rng.normal(size=(env["NM"], K_occ)))[0],
    )
    sf = psi0[None, :].copy()
    base = []
    dprev = None
    for n in range(depth):
        sf = sf @ env["U"].T
        d, _ = dets_of(env, sf)
        if dprev is not None:
            base.append(float(np.angle(d[0] / dprev[0])))
        dprev = d

    states = psi0[None, :].copy()
    weights = np.array([1.0])
    detprev = None
    Theta = np.zeros(1)
    worst_sv = np.inf
    min_norm = np.inf
    max_weight_error = 0.0
    most = None
    rows = {}
    for n in range(depth):
        states = states @ env["U"].T
        new = np.vstack([states * env["kp"][None, :], states * env["km"][None, :]])
        norms = np.einsum("bi,bi->b", new.conj(), new).real
        min_norm = min(min_norm, float(np.min(norms)))
        assert (norms > NO_PRUNE_TOL).all(), "no-prune guard"
        weights = np.concatenate([weights, weights]) * norms
        states = (new.T / np.sqrt(norms)).T
        max_weight_error = max(max_weight_error, abs(float(weights.sum()) - 1.0))
        d, svm = dets_of(env, states)
        worst_sv = min(worst_sv, svm)
        if detprev is not None:
            par = detprev[np.arange(len(d)) % len(detprev)]
            Theta = Theta[np.arange(len(d)) % len(Theta)] + np.angle(
                np.exp(1j * (np.angle(d / par) - base[n - 1]))
            )
            Z = weights.sum()
            g1 = abs(complex(np.sum(weights * np.exp(1j * Theta)) / Z))
            rows[n + 1] = (g1, Theta.copy(), weights.copy())
            if n >= 5 and (most is None or g1 < most[1]):
                most = (n + 1, g1, Theta.copy(), weights.copy())
        detprev = d
    if most is None:
        raise RuntimeError("most-spread selector has no eligible row")
    return most, rows, worst_sv, min_norm, max_weight_error


def row_profiles(Theta: np.ndarray, w: np.ndarray) -> dict[int, dict[str, float]]:
    out = {}
    for kpref in PREFIX_KS:
        p = prefix(Theta, w, kpref)
        n95 = null_p95(Theta, w, kpref)
        out[kpref] = {"p": p, "null95": n95, "gap": p - n95}
    return out


def most_spread_for_cap(rows: dict[int, tuple[float, np.ndarray, np.ndarray]], depth_cap: int) -> tuple[int, float, np.ndarray, np.ndarray]:
    candidates = [(row_n, data) for row_n, data in rows.items() if row_n <= depth_cap and row_n >= 6]
    if not candidates:
        raise RuntimeError(f"no most-spread row for depth cap {depth_cap}")
    row_n, (g1, Theta, w) = min(candidates, key=lambda item: item[1][0])
    return row_n, g1, Theta, w


def classify_min_gain(min_gain: float) -> str:
    if min_gain < -1.0e-10:
        return "drop"
    if min_gain <= 1.0e-3:
        return "stall"
    return "monotone"


def print_scope() -> None:
    print(
        "SCOPE: fixed period L=3, depth axis 9..14, 3 adversarial seeds; "
        "trends are DATA (no asymptotic claim); Born derived-chain cap inherited; "
        f"named instruments eps={EPS}, tau={TAU} supplied; trajectories realized-state data; "
        "the depth-ledger is the deliverable. Statuses pipeline-derived; audit lane grades."
    )


def print_depth_table(records: list[dict[str, object]]) -> None:
    print("W3 DEPTH AXIS: most-spread row per depth cap, selector=min global |ch1| for n>=5")
    for rec in records:
        print(
            f"seed={rec['seed']} depth_cap={rec['depth_cap']} selected_row={rec['selected_row']} "
            f"branches={rec['branches']} global={rec['global']:.6f}"
        )
        for kpref in PREFIX_KS:
            pdata = rec["profiles"][kpref]
            print(
                f"  p{kpref}={pdata['p']:.6f} "
                f"null95={pdata['null95']:.6f} "
                f"gap={pdata['gap']:.6f}"
            )


def print_min_gain_ledger(records: list[dict[str, object]]) -> None:
    print("W3 MIN-GAIN LEDGER")
    for seed in SEEDS:
        seed_recs = [rec for rec in records if rec["seed"] == seed]
        parts = [
            f"d{rec['depth_cap']}:row{rec['selected_row']}="
            f"{rec['min_gain']:.6f}:{rec['classification']}"
            for rec in seed_recs
        ]
        print(f"seed={seed} " + " ".join(parts))


def anchor_gate(env: dict[str, object]) -> None:
    most, rows, worst_sv, min_norm, max_weight_error = scan(env, ANCHOR_SEED, ANCHOR_DEPTH_CAP, K_OCC)
    g1, Theta, w = rows[ANCHOR_ROW]
    profiles = row_profiles(Theta, w)
    p3 = profiles[ANCHOR_PREFIX]["p"]
    n95 = profiles[ANCHOR_PREFIX]["null95"]
    print(
        "ANCHOR: seed=4242 depth_cap=11 row=9 "
        f"most_row={most[0]} global={g1:.6f} "
        f"prefix-3={p3:.6f} null95={n95:.6f} gap={p3 - n95:.6f}"
    )
    check(
        "W3b landed anchor prefix-3",
        abs(p3 - ANCHOR_PREFIX3) <= ANCHOR_PREFIX3_TOL,
        f"prefix-3={p3:.6f} target={ANCHOR_PREFIX3:.3f} tol={ANCHOR_PREFIX3_TOL:.1e}",
    )
    check(
        "W3b landed anchor null p95",
        abs(n95 - ANCHOR_NULL95) <= ANCHOR_NULL95_TOL,
        f"null95={n95:.6f} target~={ANCHOR_NULL95:.3f} tol={ANCHOR_NULL95_TOL:.1e}",
    )
    check(
        "W3a anchor rank/no-prune/weights",
        worst_sv > RANK_TOL and min_norm > NO_PRUNE_TOL and max_weight_error <= WEIGHT_TOL,
        (
            f"worst_sv={worst_sv:.12e}, min_norm={min_norm:.12e}, "
            f"max_abs(sum_w-1)={max_weight_error:.12e}"
        ),
    )


ROW_LEDGERS: dict[int, dict[int, tuple]] = {}
FROZEN_ROWS: dict[int, int] = {}


def build_depth_records(env: dict[str, object]) -> list[dict[str, object]]:
    records = []
    for seed in SEEDS:
        most, rows, worst_sv, min_norm, max_weight_error = scan(env, seed, MAX_DEPTH, K_OCC)
        ROW_LEDGERS[seed] = {n: (rows[n][0],) for n in rows}
        FROZEN_ROWS[seed] = most_spread_for_cap(rows, MAX_DEPTH)[0]
        for depth_cap in DEPTHS:
            selected_row, g1, Theta, w = most_spread_for_cap(rows, depth_cap)
            profiles = row_profiles(Theta, w)
            min_gain = min(profiles[3]["p"] - profiles[2]["p"], profiles[4]["p"] - profiles[3]["p"])
            clears_null = any(profiles[kpref]["gap"] > 0.0 for kpref in PREFIX_KS)
            records.append(
                {
                    "seed": seed,
                    "depth_cap": depth_cap,
                    "selected_row": selected_row,
                    "branches": len(w),
                    "global": g1,
                    "profiles": profiles,
                    "min_gain": float(min_gain),
                    "classification": classify_min_gain(float(min_gain)),
                    "clears_null": clears_null,
                    "worst_sv": worst_sv,
                    "min_norm": min_norm,
                    "max_weight_error": max_weight_error,
                    "scan_most_row": most[0],
                    "scan_most_global": most[1],
                }
            )
    return records


def check_machinery(records: list[dict[str, object]]) -> None:
    for seed in SEEDS:
        seed_records = [rec for rec in records if rec["seed"] == seed]
        worst_sv = min(rec["worst_sv"] for rec in seed_records)
        min_norm = min(rec["min_norm"] for rec in seed_records)
        max_weight_error = max(rec["max_weight_error"] for rec in seed_records)
        check(
            f"W3a rank guard seed {seed}",
            worst_sv > RANK_TOL,
            f"worst_sv={worst_sv:.12e} tol>{RANK_TOL:.1e}",
        )
        check(
            f"W3a no-prune seed {seed}",
            min_norm > NO_PRUNE_TOL,
            f"min_norm={min_norm:.12e} tol>{NO_PRUNE_TOL:.1e}",
        )
        check(
            f"W3a weights seed {seed}",
            max_weight_error <= WEIGHT_TOL,
            f"max_abs(sum_w-1)={max_weight_error:.12e} tol<={WEIGHT_TOL:.1e}",
        )


def check_depth_profiles(records: list[dict[str, object]]) -> None:
    for rec in records:
        ok = True
        parts = []
        for kpref in PREFIX_KS:
            pdata = rec["profiles"][kpref]
            p = pdata["p"]
            n95 = pdata["null95"]
            finite = np.isfinite(p) and np.isfinite(n95) and np.isfinite(pdata["gap"])
            bounded = -1.0e-12 <= p <= 1.0 + 1.0e-12
            ok = ok and finite and bounded
            parts.append(f"k={kpref}:p={p:.6f},null95={n95:.6f},finite={finite},bounded={bounded}")
        check(
            f"W3c profiles/nulls seed {rec['seed']} depth_cap {rec['depth_cap']}",
            ok,
            "; ".join(parts),
        )


def check_null_clearing(records: list[dict[str, object]]) -> None:
    clearing = [rec for rec in records if rec["clears_null"]]
    detail_parts = []
    for rec in clearing:
        winners = [
            f"k{kpref}:gap={rec['profiles'][kpref]['gap']:.6f}"
            for kpref in PREFIX_KS
            if rec["profiles"][kpref]["gap"] > 0.0
        ]
        detail_parts.append(
            f"seed={rec['seed']} depth_cap={rec['depth_cap']} row={rec['selected_row']} "
            + ",".join(winners)
        )
    detail = f"clears={len(clearing)}/{len(records)}"
    if detail_parts:
        detail += " " + " | ".join(detail_parts)
    # Panel edit: the full per-row g1 ledger (discloses WHY the argmin freezes --
    # deeper rows' global coherence is genuinely larger than the early minimum).
    print("\nPer-row g1 ledger (row: g1), per seed at the deepest cap:")
    for seed, rows_full in ROW_LEDGERS.items():
        ledger = ", ".join(f"{n}:{rows_full[n][0]:.4f}" for n in sorted(rows_full))
        print(f"  seed {seed}: {ledger}")
        beyond = [n for n in sorted(rows_full) if n > FROZEN_ROWS[seed]]
        check(f"W3f seed {seed}: every row deeper than the frozen most-spread row "
              f"{FROZEN_ROWS[seed]} has strictly larger g1 (the freeze is the "
              f"argmin's content, disclosed, not an eligibility artifact)",
              all(rows_full[n][0] > rows_full[FROZEN_ROWS[seed]][0] for n in beyond),
              f"frozen g1={rows_full[FROZEN_ROWS[seed]][0]:.4f}; "
              f"{len(beyond)} deeper rows")
    check("W3e ALL 18/18 gated (seed x depth-cap) events clear their "
          "label-permutation nulls (explicit gate; finite seeded null sampling: "
          "300 draws, rng 7777)",
          len(clearing) == 18, f"clears={len(clearing)}/18")
    check("W3d null-clearing existence", len(clearing) >= 1, detail)


def main() -> None:
    if max(DEPTHS) > MAX_DEPTH or MAX_DEPTH > 14:
        raise RuntimeError("depth cap would exceed the requested depth-14 memory limit")
    print_scope()
    print("MACHINERY: landed L=3 Slater/K_occ=5/U_step/Kraus/OPS/baseline/rows/null conventions")
    env = build(L_RING)
    anchor_gate(env)
    records = build_depth_records(env)
    print_depth_table(records)
    print_min_gain_ledger(records)
    check_machinery(records)
    check_depth_profiles(records)
    check_null_clearing(records)
    finish()


if __name__ == "__main__":
    main()
