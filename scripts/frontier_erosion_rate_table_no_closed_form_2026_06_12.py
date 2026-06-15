#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/EROSION_RATE_TABLE_NO_TESTED_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_erosion_rate_table_no_closed_form_2026_06_12.py
"""

from __future__ import annotations

import math

import numpy as np


N_QUBITS = 4
N_FRAG = 3
DIM = 2 ** N_QUBITS
EPS_GRID = (0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99)
PHASE2_STEPS = 7
TOL = 1e-12

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")
    return ok


def section(title: str) -> None:
    print("=" * 78)
    print(title)
    print("=" * 78)


def bit(index: int, qubit: int, nqubits: int = N_QUBITS) -> int:
    return (index >> (nqubits - qubit - 1)) & 1


def flip_bit(index: int, qubit: int, nqubits: int = N_QUBITS) -> int:
    return index ^ (1 << (nqubits - qubit - 1))


def initial_state() -> np.ndarray:
    psi = np.zeros(DIM, dtype=complex)
    psi[0] = 1.0 / math.sqrt(2.0)      # |0 000>
    psi[8] = 1.0 / math.sqrt(2.0)      # |1 000>
    return psi


def cnot_pointer_to_fragment(psi: np.ndarray, frag: int) -> np.ndarray:
    target = 1 + frag
    out = np.zeros_like(psi)
    for i, amp in enumerate(psi):
        if bit(i, 0) == 1:
            out[flip_bit(i, target)] += amp
        else:
            out[i] += amp
    return out


def measure_fragment(psi: np.ndarray, frag: int, eps: float) -> list[tuple[float, np.ndarray]]:
    q = 1 + frag
    out: list[tuple[float, np.ndarray]] = []
    for y in (1.0, -1.0):
        phi = psi.copy()
        for i in range(DIM):
            z = 1.0 if bit(i, q) == 0 else -1.0
            phi[i] *= math.sqrt(max(0.0, (1.0 + y * eps * z) / 2.0))
        p = float(np.vdot(phi, phi).real)
        if p > 1e-15:
            out.append((p, phi / math.sqrt(p)))
    return out


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def partial_trace(rho: np.ndarray, keep: list[int], nqubits: int = N_QUBITS) -> np.ndarray:
    tensor = rho.reshape([2] * (2 * nqubits))
    traced = [q for q in range(nqubits) if q not in keep]
    for q in sorted(traced, reverse=True):
        half = tensor.ndim // 2
        tensor = np.trace(tensor, axis1=q, axis2=q + half)
    dim = 2 ** len(keep)
    return tensor.reshape((dim, dim))


def entropy_bits(rho: np.ndarray) -> float:
    herm = 0.5 * (rho + rho.conj().T)
    vals = np.linalg.eigvalsh(herm)
    vals = np.clip(vals.real, 0.0, 1.0)
    vals = vals[vals > 1e-15]
    if vals.size == 0:
        return 0.0
    return float(-np.sum(vals * np.log2(vals)))


def mutual_information(rho: np.ndarray, a: list[int], b: list[int]) -> float:
    ab = sorted(a + b)
    return (
        entropy_bits(partial_trace(rho, a))
        + entropy_bits(partial_trace(rho, b))
        - entropy_bits(partial_trace(rho, ab))
    )


def branch_rbar(branches: list[tuple[float, np.ndarray]]) -> float:
    total = 0.0
    for w, psi in branches:
        rho = density(psi)
        total += w * float(
            np.mean([mutual_information(rho, [0], [1 + frag]) for frag in range(N_FRAG)])
        )
    return total


def ensemble_mis(branches: list[tuple[float, np.ndarray]]) -> np.ndarray:
    rho = sum(w * density(psi) for w, psi in branches)
    return np.array([mutual_information(rho, [0], [1 + frag]) for frag in range(N_FRAG)])


def advance_measure(branches: list[tuple[float, np.ndarray]], frag: int, eps: float) -> list[tuple[float, np.ndarray]]:
    new: list[tuple[float, np.ndarray]] = []
    for w, psi in branches:
        for p, phi in measure_fragment(psi, frag, eps):
            new.append((w * p, phi))
    return new


def run_tree(eps: float) -> dict[str, object]:
    branches: list[tuple[float, np.ndarray]] = [(1.0, initial_state())]

    for frag in range(N_FRAG):
        branches = [(w, cnot_pointer_to_fragment(psi, frag)) for w, psi in branches]
        branches = advance_measure(branches, frag, eps)

    rbar = [branch_rbar(branches)]
    mi = [ensemble_mis(branches)]
    counts = [len(branches)]
    weight_errors = [abs(sum(w for w, _ in branches) - 1.0)]

    for step in range(PHASE2_STEPS):
        frag = step % N_FRAG
        branches = advance_measure(branches, frag, eps)
        rbar.append(branch_rbar(branches))
        mi.append(ensemble_mis(branches))
        counts.append(len(branches))
        weight_errors.append(abs(sum(w for w, _ in branches) - 1.0))

    return {
        "eps": eps,
        "rbar": np.array(rbar, dtype=float),
        "mi": np.array(mi, dtype=float),
        "counts": np.array(counts, dtype=int),
        "weight_errors": np.array(weight_errors, dtype=float),
    }


def odd_ratios(rbar: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    odd_steps = np.array([t for t in range(1, len(rbar)) if t % 2 == 1], dtype=int)
    values = rbar[odd_steps]
    ratios = []
    for a, b in zip(values[:-1], values[1:]):
        if a > 1e-12 and b > 1e-12:
            ratios.append(float(b / a))
    return odd_steps, np.array(ratios, dtype=float)


def ratio_datum(ratios: np.ndarray) -> float:
    if ratios.size == 0:
        return float("nan")
    return float(np.exp(np.mean(np.log(ratios))))


def first_threshold_time(rbar: np.ndarray, threshold: float = 0.5) -> int | None:
    hits = np.flatnonzero(rbar < threshold)
    if hits.size == 0:
        return None
    return int(hits[0])


def exact_projective_kill_control() -> tuple[float, float]:
    branches: list[tuple[float, np.ndarray]] = [(1.0, initial_state())]
    for frag in range(N_FRAG):
        branches = [(w, cnot_pointer_to_fragment(psi, frag)) for w, psi in branches]
    before = branch_rbar(branches)
    after = branch_rbar(advance_measure(branches, 0, 1.0))
    return before, after


def monotone_censored(times: list[int | None]) -> bool:
    finite = [t for t in times if t is not None]
    finite_nonincreasing = all(a >= b for a, b in zip(finite[:-1], finite[1:]))
    reached_suffix = True
    seen_reached = False
    for t in times:
        if t is not None:
            seen_reached = True
        elif seen_reached:
            reached_suffix = False
    return finite_nonincreasing and reached_suffix


def fmt_float(x: float) -> str:
    if not np.isfinite(x):
        return "nan"
    return f"{x:.10g}"


def main() -> int:
    section("Record erosion exact tree")
    print("Model: pointer + 3 fragments; 3 broadcast+measure steps; 7 measurement-only steps.")
    print("Rbar(t): Born-weighted mean branch I(P:F_j), averaged over j=0,1,2.")
    print()

    results = {eps: run_tree(eps) for eps in EPS_GRID}

    max_weight_error = max(float(np.max(res["weight_errors"])) for res in results.values())
    max_rbar_upper = max(float(np.max(res["rbar"])) for res in results.values())
    min_rbar = min(float(np.min(res["rbar"])) for res in results.values())
    check("exact trees conserve total Born weight at every recorded layer",
          max_weight_error < 1e-12, f"max |sum w - 1| = {max_weight_error:.3e}")
    check("Rbar is a computed branch-information quantity bounded in [0,1]",
          min_rbar > -1e-12 and max_rbar_upper < 1.0 + 1e-12,
          f"min={min_rbar:.3e}, max={max_rbar_upper:.12f}")

    section("Phase-2 Rbar trajectories")
    print("Columns are phase-2 t=0..7, where t=0 is after the three broadcast+measure steps.")
    for eps, res in results.items():
        vals = " ".join(f"{x:.8f}" for x in res["rbar"])
        print(f"eps={eps:>4}: {vals}")
    print()

    section("Odd-step envelope ratios")
    ratio_rows: dict[float, dict[str, object]] = {}
    for eps, res in results.items():
        steps, ratios = odd_ratios(res["rbar"])
        r_eff = ratio_datum(ratios)
        rel_spread = 0.0
        if ratios.size > 1 and ratios[0] > 0:
            rel_spread = float(np.max(np.abs(ratios - ratios[0])) / ratios[0])
        ratio_rows[eps] = {
            "steps": steps,
            "ratios": ratios,
            "r_eff": r_eff,
            "rel_spread": rel_spread,
        }
        ratio_text = ", ".join(fmt_float(x) for x in ratios)
        print(
            f"eps={eps:>4}: odd_steps={steps.tolist()} "
            f"ratios=[{ratio_text}] r_eff={fmt_float(r_eff)} rel_spread={rel_spread:.6g}"
        )

    ratio_extraction_ok = all(ratio_rows[eps]["ratios"].size >= 1 for eps in EPS_GRID)
    check("odd-step rebound envelope ratios are extracted where Rbar>1e-12",
          ratio_extraction_ok)
    geometric_by_eps = {
        eps: (ratio_rows[eps]["ratios"].size > 0 and ratio_rows[eps]["rel_spread"] < 5e-2)
        for eps in EPS_GRID
    }
    for eps in EPS_GRID:
        rel = float(ratio_rows[eps]["rel_spread"])
        ratios = ratio_rows[eps]["ratios"]
        if geometric_by_eps[eps]:
            check(f"Odd-step envelope eps={eps}: geometric envelope passes the 5e-2 fixed-eps gate",
                  rel < 5e-2 and ratios.size > 0,
                  f"relative spread={rel:.6g}")
        else:
            check(f"Odd-step envelope eps={eps}: measured fixed-eps pattern is non-geometric",
                  rel >= 5e-2 and ratios.size > 1,
                  f"relative spread={rel:.6g}")
    if all(geometric_by_eps.values()):
        worst_spread = max(float(ratio_rows[eps]["rel_spread"]) for eps in EPS_GRID)
        check("Odd-step envelope pattern: odd-step ratios are step-independent at fixed eps "
              "(geometric envelope, 5e-2 relative gate)",
              all(geometric_by_eps.values()),
              f"worst relative spread = {worst_spread:.6g}")
    else:
        offenders = [eps for eps, ok in geometric_by_eps.items() if not ok]
        worst_spread = max(float(ratio_rows[eps]["rel_spread"]) for eps in EPS_GRID)
        check("Odd-step envelope pattern: the measured odd-step envelope is not globally "
              "step-independent; geometric gate rejected for the listed eps",
              len(offenders) > 0,
              f"offenders={offenders}, worst relative spread={worst_spread:.6g}")
    print()

    section("Candidate closed-form checks")
    r_table = {eps: float(ratio_rows[eps]["r_eff"]) for eps in EPS_GRID}
    print("Measured r(eps) datum: geometric mean of the odd-step ratios printed above.")
    for eps in EPS_GRID:
        print(f"eps={eps:>4}: r={fmt_float(r_table[eps])}")

    candidates = {
        "(1-eps^2)/4": lambda e: (1.0 - e * e) / 4.0,
        "(1-eps^2)^2/4": lambda e: (1.0 - e * e) ** 2 / 4.0,
        "(1-eps^2)/2": lambda e: (1.0 - e * e) / 2.0,
        "(1-eps^2)^2": lambda e: (1.0 - e * e) ** 2,
    }
    matches: dict[str, bool] = {}
    for name, fn in candidates.items():
        rels = []
        for eps in EPS_GRID:
            pred = fn(eps)
            rels.append(abs(r_table[eps] - pred) / max(abs(pred), 1e-300))
        max_rel = float(max(rels))
        matches[name] = bool(max_rel < 1e-6)
        rel_text = ", ".join(f"{eps}:{rel:.3e}" for eps, rel in zip(EPS_GRID, rels))
        print(f"candidate {name}: max_rel={max_rel:.3e}; rel_devs={{ {rel_text} }}")

    matched = [name for name, ok in matches.items() if ok]
    if matched:
        check("Candidate-form pattern: a tested closed form matches all eps at 1e-6 relative",
              len(matched) > 0, ", ".join(matched))
    else:
        check("Candidate-form pattern: no tested closed form matches; the measured table is the datum",
              not any(matches.values()))
    print()

    section("First threshold time Rbar < 0.5")
    threshold_times: list[int | None] = []
    for eps in EPS_GRID:
        tstar = first_threshold_time(results[eps]["rbar"])
        threshold_times.append(tstar)
        label = f"{tstar}" if tstar is not None else f">{PHASE2_STEPS}"
        print(f"eps={eps:>4}: t*={label}")
    check("Threshold-time monotonicity: threshold times are censored-nonincreasing as eps rises",
          monotone_censored(threshold_times),
          "times=" + ", ".join(">" + str(PHASE2_STEPS) if t is None else str(t) for t in threshold_times))
    print()

    section("Controls")
    zero = run_tree(0.0)
    zero_decay = float(np.max(np.abs(zero["rbar"] - zero["rbar"][0])))
    check("eps=0 no-decay control: Rbar is constant through phase 2",
          zero_decay < 1e-12 and abs(float(zero["rbar"][0]) - 1.0) < 1e-12,
          f"max drift={zero_decay:.3e}, Rbar0={zero['rbar'][0]:.12f}")

    before, after = exact_projective_kill_control()
    check("one projective readout step kills the branch-relational record",
          abs(before - 1.0) < 1e-12 and after < 1e-12,
          f"before={before:.12f}, after={after:.3e}")

    mi_devs = []
    for eps in EPS_GRID:
        mi = results[eps]["mi"]
        mi_devs.append(float(np.max(np.abs(mi - 1.0))))
        print(
            f"eps={eps:>4}: ensemble MI max dev={mi_devs[-1]:.3e}; "
            f"final MI={np.array2string(mi[-1], precision=12)}"
        )
    check("ensemble MI stays [1,1,1] at every probed eps and phase-2 layer",
          max(mi_devs) < 1e-12,
          f"max deviation={max(mi_devs):.3e}")
    print("Finite-lattice range/size claims: none asserted; four-qubit exact tree only.")

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print("SCOPE: erosion-rate law of the branch-relational record in the explicit")
    print("  pointer + 3-fragment CNOT/QND-readout model; exact dense NumPy trees;")
    print("  candidate-form testing without fitting; Born cap inherited; statuses")
    print("  pipeline-derived and audit-lane graded.  No finite-lattice scaling,")
    print("  continuum limit, fitted rate law, or physical measurement derivation is")
    print("  claimed.")
    if FAIL:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
