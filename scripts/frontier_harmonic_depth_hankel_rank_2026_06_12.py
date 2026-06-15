#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/HARMONIC_DEPTH_HANKEL_RANK_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_harmonic_depth_hankel_rank_2026_06_12.py
"""
from __future__ import annotations

import sys
from dataclasses import dataclass

import numpy as np


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


@dataclass(frozen=True)
class StateSpec:
    label: str
    k_occ: int
    seed: int


L = 3
NC = 3
DIM = L * NC
TAU = 0.35
T_STEPS = 256
WINDOW = 64
WINDOWS = (64, 128)
RANK_REL_FLOOR = 1.0e-6
RANK_REL_FLOORS = (1.0e-5, RANK_REL_FLOOR, 1.0e-7)
COUPLING_FLOOR = 1.0e-8
ANCHOR_TOL = 1.0e-3
ANCHOR_K3_O8 = 0.9836
ANCHOR_K6_O4 = 0.9950

# Frozen realized states.  K=5/seed=99 is required by the spec; the other seeds
# are the landed deterministic states for the K=3/4/6 rows mirrored here.
STATES = (
    StateSpec("K=3", 3, 391),
    StateSpec("K=4", 4, 99),
    StateSpec("K=5(seed=99)", 5, 99),
    StateSpec("K=6", 6, 466),
)


@dataclass(frozen=True)
class RankResult:
    window: int
    threshold: float
    svals: np.ndarray
    rank: int
    floor: float
    cap: int

    @property
    def censored(self) -> bool:
        return self.rank >= self.window


def lattice_hamiltonian(n_sites: int) -> np.ndarray:
    """Color-diagonal nearest-neighbor hopping on a periodic n-site ring."""
    h = np.zeros((n_sites * NC, n_sites * NC), dtype=complex)
    for x in range(n_sites):
        y = (x + 1) % n_sites
        for c in range(NC):
            h[NC * x + c, NC * y + c] = -1.0
            h[NC * y + c, NC * x + c] = -1.0
    return h


def polar_u(m: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(m.conj().T @ m)
    if float(np.min(w)) <= 1.0e-14:
        raise FloatingPointError(f"polar block singular: min eig={float(np.min(w)):.3e}")
    return m @ v @ np.diag(w**-0.5) @ v.conj().T


def state_modes(dim: int, k_occ: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(dim, k_occ)) + 1j * rng.normal(size=(dim, k_occ))
    q, r = np.linalg.qr(z)
    # QR sign/phase convention fixed so the same seed is platform-stable.
    phases = np.exp(-1j * np.angle(np.diag(r)))
    q = q @ np.diag(phases)
    return q[:, :k_occ]


def phase_increment_sequence(spec: StateSpec, evals: np.ndarray, evecs: np.ndarray) -> dict:
    q = state_modes(DIM, spec.k_occ, spec.seed)
    rho0 = q @ q.conj().T
    phases = []
    min_sigma = np.inf
    for t in range(T_STEPS + 1):
        u = evecs @ np.diag(np.exp(-1j * TAU * evals * t)) @ evecs.conj().T
        rho_t = u @ rho0 @ u.conj().T
        block_01 = rho_t[0:NC, NC : 2 * NC]
        svals = np.linalg.svd(block_01, compute_uv=False)
        min_sigma = min(min_sigma, float(svals[-1]))
        phases.append(float(np.angle(np.linalg.det(polar_u(block_01)))))
    raw = np.diff(np.unwrap(np.array(phases)))
    centered = raw - float(np.mean(raw))
    return {
        "modes": q,
        "rho0": rho0,
        "raw_increments": raw,
        "increments": centered,
        "raw_mean": float(np.mean(raw)),
        "min_block_sigma": min_sigma,
    }


def trajectory_hankel(x: np.ndarray, window: int = WINDOW) -> np.ndarray:
    if len(x) < window:
        raise ValueError("sequence shorter than Hankel window")
    return np.column_stack([x[i : i + window] for i in range(len(x) - window + 1)])


def hankel_rank_result(
    x: np.ndarray,
    window: int = WINDOW,
    threshold: float = RANK_REL_FLOOR,
) -> RankResult:
    hankel = trajectory_hankel(x, window)
    svals = np.linalg.svd(hankel, compute_uv=False)
    floor = threshold * float(svals[0])
    rank = int(np.sum(svals >= floor))
    return RankResult(
        window=window,
        threshold=threshold,
        svals=svals,
        rank=rank,
        floor=floor,
        cap=int(min(hankel.shape)),
    )


def rank_cell(result: RankResult) -> str:
    if result.censored:
        return f">={result.rank}"
    return str(result.rank)


def rank_detail(result: RankResult) -> str:
    status = "censored lower bound" if result.censored else "uncensored"
    text = (
        f"rank={rank_cell(result)} ({status}), cap={result.cap}, "
        f"floor={result.floor:.3e}, s_rank={result.svals[result.rank - 1]:.3e}"
    )
    if result.rank < len(result.svals):
        text += f", s_next={result.svals[result.rank]:.3e}"
    return text


def sv_capture(svals: np.ndarray, order: int) -> float:
    total = float(np.sum(svals * svals))
    kept = float(np.sum(svals[:order] * svals[:order]))
    return kept / total


def site01_projector(n_sites: int) -> np.ndarray:
    p = np.zeros((n_sites * NC, n_sites * NC), dtype=complex)
    p[0:NC, 0:NC] = np.eye(NC)
    p[NC : 2 * NC, NC : 2 * NC] = np.eye(NC)
    return p


def coupled_gap_count(rho0: np.ndarray, evals: np.ndarray, evecs: np.ndarray) -> tuple[int, dict]:
    """Count distinct spectral gaps coupled by the site-0/1 block.

    For a realized occupied projector rho0, the spectral weight of gap a-b is
    |(V^dag rho0 V)_{ab}| * |(V^dag P_01 V)_{ba}|.  This is the linear spectral
    support seen by the site-0/1 block; the determinant phase can still have a
    different Hankel rank because polar+det is nonlinear.
    """
    occ = evecs.conj().T @ rho0 @ evecs
    p01 = evecs.conj().T @ site01_projector(L) @ evecs
    weights: dict[float, float] = {}
    for a in range(len(evals)):
        for b in range(len(evals)):
            weight = abs(occ[a, b]) * abs(p01[b, a])
            if weight > COUPLING_FLOOR:
                gap = round(float(evals[a] - evals[b]), 12)
                weights[gap] = weights.get(gap, 0.0) + float(weight)
    return len(weights), weights


def wraparound_probe() -> bool:
    """Mandatory small-L wraparound sanity probe for the finite periodic carrier."""
    ok = True
    for n_sites in (3, 4, 12):
        h = lattice_hamiltonian(n_sites)
        for x in range(n_sites):
            for c in range(NC):
                row = np.flatnonzero(abs(h[NC * x + c]) > 0)
                expected = {
                    NC * ((x - 1) % n_sites) + c,
                    NC * ((x + 1) % n_sites) + c,
                }
                ok = ok and set(map(int, row)) == expected
        ok = ok and h[0, NC] == -1.0
        ok = ok and h[0, NC * (n_sites - 1)] == -1.0
    return ok


def main() -> int:
    print("=" * 78)
    print("S2 det-phase increments: numerical trajectory rank vs capture depth")
    print("=" * 78)
    print(f"constants: L={L}, NC={NC}, tau={TAU}, T={T_STEPS}, windows={WINDOWS}")
    print(
        "rank floors: relative "
        + ", ".join(f"{threshold:.1e}" for threshold in RANK_REL_FLOORS)
        + f"; default {RANK_REL_FLOOR:.1e}; coupling floor {COUPLING_FLOOR:.1e}"
    )
    print()

    h = lattice_hamiltonian(L)
    evals, evecs = np.linalg.eigh(h)

    check(
        "periodic carrier wraparound probe: degree and site-0/1 adjacency stable at L=3,4,12",
        wraparound_probe(),
        "guards against treating small-L wraparound shell data as a range law",
    )
    check(
        "Hamiltonian is Hermitian and color-diagonal nearest-neighbor",
        np.max(np.abs(h - h.conj().T)) < 1.0e-14,
        f"max Hermitian defect {np.max(np.abs(h - h.conj().T)):.1e}",
    )
    check(
        "state domain is exactly K in {3,4,5,6} with K=5 seed 99",
        [s.k_occ for s in STATES] == [3, 4, 5, 6] and STATES[2].seed == 99,
        "seeds " + ", ".join(f"{s.label}:{s.seed}" for s in STATES),
    )

    rows = {}
    print()
    print("Per-state spectra, capture, and rank table")
    print("-" * 78)
    for spec in STATES:
        data = phase_increment_sequence(spec, evals, evecs)
        rank_results = {
            window: hankel_rank_result(data["increments"], window)
            for window in WINDOWS
        }
        primary = rank_results[WINDOW]
        svals = primary.svals
        cap4 = sv_capture(svals, 4)
        cap8 = sv_capture(svals, 8)
        gap_count, gap_weights = coupled_gap_count(data["rho0"], evals, evecs)
        rows[spec.k_occ] = {
            "spec": spec,
            "data": data,
            "rank_results": rank_results,
            "cap4": cap4,
            "cap8": cap8,
            "gap_count": gap_count,
            "gap_weights": gap_weights,
        }
        gaps = ", ".join(f"{g:+.1f}" for g in sorted(gap_weights))
        rank_text = ", ".join(
            f"w{window}:{rank_cell(rank_results[window])}" for window in WINDOWS
        )
        print(
            f"  {spec.label:12s} seed={spec.seed:3d} raw_mean={data['raw_mean']:+.6f} "
            f"ranks[{rank_text}] cap4={cap4:.6f} cap8={cap8:.6f} "
            f"gaps={gap_count} [{gaps}] min_sigma={data['min_block_sigma']:.3e}"
        )
        for window in WINDOWS:
            head = " ".join(f"{v:.6g}" for v in rank_results[window].svals[:10])
            print(f"      sv head w{window}: {head}")

    print()
    print("Anchor gates")
    print("-" * 78)
    check(
        "ANCHOR: K=3 capture at o=8 reproduces landed ceiling 0.9836 within 1e-3",
        abs(rows[3]["cap8"] - ANCHOR_K3_O8) <= ANCHOR_TOL,
        f"cap8={rows[3]['cap8']:.6f}, expected={ANCHOR_K3_O8:.4f}",
    )
    check(
        "ANCHOR: K=6 saturation capture at o=4 reproduces landed 0.995 within 1e-3",
        abs(rows[6]["cap4"] - ANCHOR_K6_O4) <= ANCHOR_TOL,
        f"cap4={rows[6]['cap4']:.6f}, expected={ANCHOR_K6_O4:.4f}",
    )
    check(
        "anti-fabrication: determinant blocks stay full-rank on every sampled trajectory",
        min(row["data"]["min_block_sigma"] for row in rows.values()) > 1.0e-8,
        "mins " + ", ".join(f"K{k}:{row['data']['min_block_sigma']:.2e}" for k, row in rows.items()),
    )

    print()
    print("Rank floor gates")
    print("-" * 78)
    for k, row in rows.items():
        for window in WINDOWS:
            result = row["rank_results"][window]
            rank = result.rank
            svals = result.svals
            above_ok = rank > 0 and float(svals[rank - 1]) >= result.floor
            below_ok = rank == len(svals) or float(svals[rank]) < result.floor
            if result.censored:
                name = (
                    f"K={k} window={window} numerical trajectory rank LOWER BOUND "
                    "is censored (rank >= window) at threshold 1e-6"
                )
            else:
                name = (
                    f"K={k} window={window} numerical trajectory rank is UNCENSORED "
                    "at threshold 1e-6"
                )
            check(name, above_ok and below_ok, rank_detail(result))

    print()
    print("Relation gates")
    print("-" * 78)
    numeric_rank_tables = {
        window: {
            k: rows[k]["rank_results"][window].rank
            for k in sorted(rows)
        }
        for window in WINDOWS
    }
    default_rank_tables = {
        window: {
            k: rank_cell(rows[k]["rank_results"][window])
            for k in sorted(rows)
        }
        for window in WINDOWS
    }
    cap4_table = {k: rows[k]["cap4"] for k in sorted(rows)}
    print("  default-threshold rank tables (censored cells are lower bounds):")
    for window in WINDOWS:
        print(f"    window={window}: {default_rank_tables[window]}")
    print("  cap4 table:", {k: round(v, 6) for k, v in cap4_table.items()})

    k6_uncensored_smallest = all(
        not rows[6]["rank_results"][window].censored
        and all(
            rows[6]["rank_results"][window].rank
            < rows[k]["rank_results"][window].rank
            for k in rows
            if k != 6
        )
        for window in WINDOWS
    )
    check(
        "S2b: K=6 numerical trajectory rank is UNCENSORED at windows 64/128 and smallest (fixed)",
        k6_uncensored_smallest,
        f"ranks={default_rank_tables}",
    )

    k34_censored_or_double = all(
        all(
            rows[k]["rank_results"][window].censored
            or rows[k]["rank_results"][window].rank
            >= 2 * rows[6]["rank_results"][window].rank
            for k in (3, 4)
        )
        for window in WINDOWS
    )
    check(
        "S2b: K=3/K=4 ranks are censored-or-larger at both windows (>= 2*K6 when uncensored)",
        k34_censored_or_double,
        f"ranks={default_rank_tables}",
    )
    check(
        "S2b: K=6-smallest numerical trajectory rank matches the landed early-saturation behavior",
        rows[6]["cap4"] > rows[3]["cap4"]
        and rows[6]["cap4"] > rows[4]["cap4"]
        and k6_uncensored_smallest,
        f"K6 cap4={rows[6]['cap4']:.6f}, K3/K4 cap4={rows[3]['cap4']:.6f}/{rows[4]['cap4']:.6f}",
    )

    print()
    print("Threshold sensitivity rank tables")
    print("-" * 78)
    threshold_results = {
        threshold: {
            k: {
                window: hankel_rank_result(row["data"]["increments"], window, threshold)
                for window in WINDOWS
            }
            for k, row in rows.items()
        }
        for threshold in RANK_REL_FLOORS
    }
    threshold_tables = {}
    for threshold in RANK_REL_FLOORS:
        threshold_tables[threshold] = {}
        print(f"  threshold={threshold:.0e}")
        for window in WINDOWS:
            table = {
                k: rank_cell(threshold_results[threshold][k][window])
                for k in sorted(rows)
            }
            threshold_tables[threshold][window] = table
            print(f"    window={window}: {table}")
    threshold_k6_smallest = all(
        all(
            threshold_results[threshold][6][window].rank
            < threshold_results[threshold][k][window].rank
            for k in rows
            if k != 6
        )
        for threshold in RANK_REL_FLOORS
        for window in WINDOWS
    )
    check(
        "S2b: threshold sensitivity ranks at 1e-5/1e-6/1e-7 keep K=6-smallest ordering stable",
        threshold_k6_smallest,
        f"ranks={threshold_tables}",
    )

    gap_table = {k: rows[k]["gap_count"] for k in sorted(rows)}
    print("  coupled distinct-gap table:", gap_table)
    check(
        "S2c: identical coupled-gap counts cannot explain the ordering (3 each, gated)",
        len(set(gap_table.values())) == 1
        and gap_table[3] == gap_table[4] == gap_table[5] == gap_table[6] == 3
        and all(len(set(table.values())) > 1 for table in numeric_rank_tables.values()),
        f"gap_counts={gap_table}, ranks={default_rank_tables}",
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print("SCOPE: exact finite one-body composite-link datum at L=3, tau=0.35, T=256.")
    print("  The per-state tables are data.  The gated claims are: the two landed")
    print("  capture anchors reproduce; K=6 has the smallest uncensored numerical")
    print("  trajectory rank (window/threshold-relative); K=3/K=4 are censored-or-")
    print("  larger relative to K=6 at windows 64/128; threshold sensitivity preserves")
    print("  the K=6-smallest ordering; and identical coupled-gap counts cannot explain")
    print("  the ordering (3 each, gated).")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
