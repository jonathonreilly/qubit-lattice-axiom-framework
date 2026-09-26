#!/usr/bin/env python3
"""Author controls for the bounded-cycle stationary-mode argument.

Finite matrix identities and numerical controls are distinct from the
uniform proof in the companion note. No physical field is identified here.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import scipy.linalg as la
import sympy as sp

HERE = Path(__file__).resolve().parent
ROWS: list[dict] = []


def check(name: str, condition: bool, **data: object) -> None:
    row = {"name": name, "pass": bool(condition), **data}
    ROWS.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
    assert condition, name


def normalized_form(L: np.ndarray, pi: np.ndarray):
    """Return full and skew norms in the dissipative metric."""
    w = np.sqrt(pi)
    G = w[:, None] * L / w[None, :]
    D = -(G + G.conj().T) / 2
    vals, vecs = la.eigh(D)
    pos = vals > 1e-11
    V = vecs[:, pos] / np.sqrt(vals[pos])[None, :]
    full = V.conj().T @ G @ V
    skew = V.conj().T @ ((G - G.conj().T) / 2) @ V
    return float(la.svdvals(full)[0]), float(la.svdvals(skew)[0]), vals


def cycle_constants() -> None:
    rows = []
    for m in range(2, 17):
        P = np.zeros((m, m))
        for j in range(m):
            P[j, (j + 1) % m] = 1
        L = P - np.eye(m)
        full, skew, _ = normalized_form(L, np.ones(m) / m)
        c = 1 / np.sin(np.pi / m)
        a = 1 / np.tan(np.pi / m)
        rows.append({"m": m, "full_norm": full, "csc_pi_m": float(c),
                     "skew_norm": skew, "cot_pi_m": float(a)})
    err = max(max(abs(r["full_norm"] - r["csc_pi_m"]),
                  abs(r["skew_norm"] - r["cot_pi_m"])) for r in rows)
    check("cycle_form_constants_by_matrix_whitening", err < 2e-12,
          max_error=err, cycles=rows)


def overlapping_cycles() -> None:
    n = 9
    p = sp.Matrix([sp.Rational(j + 1, 45) for j in range(n)])
    cycles = [(0, 1, 2, 3), (2, 4, 5), (5, 6),
              (6, 7, 8, 0), (1, 5, 8, 4)]
    weights = [sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(3, 7),
               sp.Rational(1, 2), sp.Rational(5, 11)]
    Q = sp.zeros(n)
    for C, w in zip(cycles, weights):
        for x, y in zip(C, C[1:] + C[:1]):
            Q[x, y] += w
    L = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                L[i, j] = Q[i, j] / p[i]
        L[i, i] = -sum(L[i, j] for j in range(n) if j != i)
    check("exact_nonuniform_stationarity_for_overlapping_positive_cycles",
          L * sp.ones(n, 1) == sp.zeros(n, 1)
          and p.T * L == sp.zeros(1, n)
          and Q != Q.T,
          pi=[str(x) for x in p], cycle_lengths=list(map(len, cycles)))
    f = sp.Matrix(sp.symbols("f0:9", real=True))
    g = sp.Matrix(sp.symbols("g0:9", real=True))
    D = -(f.T * sp.diag(*p) * L * f)[0]
    edgeD = sum(Q[i, j] * (f[j] - f[i]) ** 2 / 2
                for i in range(n) for j in range(n))
    bilinear = (f.T * sp.diag(*p) * L * g)[0]
    cycleB = sum(w * sum(f[x] * (g[y] - g[x])
                        for x, y in zip(C, C[1:] + C[:1]))
                 for C, w in zip(cycles, weights))
    check("exact_dirichlet_and_cycle_bilinear_decompositions",
          sp.expand(D - edgeD) == 0 and sp.expand(bilinear - cycleB) == 0)
    Ln = np.array(L, dtype=float)
    pn = np.array(p, dtype=float).ravel()
    full, skew, ds = normalized_form(Ln, pn)
    check("overlap_sector_bound_without_uniform_stationary_weights",
          full <= np.sqrt(2) + 1e-12 and skew <= 1 + 1e-12
          and ds[0] > -1e-12,
          full_norm=full, full_bound=float(np.sqrt(2)), skew_norm=skew,
          skew_bound=1.0, smallest_dissipative_eigenvalue=float(ds[0]))
    eig = la.eigvals(Ln)
    ratios = [abs(z.imag) / (-z.real) for z in eig if z.real < -1e-10]
    check("overlap_eigenvalue_sector", max(ratios) <= 1 + 1e-12,
          max_imaginary_to_damping=max(ratios), bound=1.0,
          eigenvalues=[[float(z.real), float(z.imag)] for z in eig])
    rng = np.random.default_rng(21092026)
    cases = []
    for trial in range(5):
        fn = rng.normal(size=n) + 1j * rng.normal(size=n)
        fn -= pn @ fn
        S = float(np.vdot(fn, pn * fn).real)
        Dn = float(-np.vdot(fn, pn * (Ln @ fn)).real)
        for t in (0.0001, 0.003, 0.1, 1.0, 10.0):
            Pt = la.expm(t * Ln)
            increment = 2 * float(S - np.vdot(fn, pn * (Pt @ fn)).real)
            bound = np.sqrt(2) * np.sqrt(2 * t * Dn * S)
            cases.append({"trial": trial, "t": t, "variance": S,
                          "dirichlet": Dn, "increment": increment,
                          "bound": float(bound), "ratio": float(increment / bound)})
    check("stationary_semigroup_increment_bound_complex_observables",
          all(-1e-10 <= r["increment"] <= r["bound"] + 1e-10 for r in cases),
          cases=cases, max_ratio=max(r["ratio"] for r in cases))


def loop(center: tuple[int, int, int], species: str) -> dict:
    c = np.array(center)
    positions = [(0, -1, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0)]
    labels = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]
    return {tuple(c + np.array(x)): (species + str(j), species, a)
            for j, (x, a) in enumerate(zip(positions, labels))}


def reverse(records: dict, center: tuple[int, int, int], species: str) -> dict:
    c = np.array(center)
    return {tuple(2 * c - np.array(x)) if a[1] == species else x: a
            for x, a in records.items()}


def field(records: dict, species: str) -> dict:
    return {x: np.array(a[2], dtype=int) for x, a in records.items() if a[1] == species}


def charge(F: dict) -> dict:
    out: dict[tuple, int] = {}
    for x, a in F.items():
        for j in range(3):
            if not a[j]:
                continue
            e = np.eye(3, dtype=int)[j]
            lo, hi = tuple(np.array(x) - e), tuple(np.array(x) + e)
            out[lo] = out.get(lo, 0) + int(a[j])
            out[hi] = out.get(hi, 0) - int(a[j])
    return {x: q for x, q in out.items() if q}


def immutable_gauss_cycle() -> None:
    cE, cB = (0, 0, 0), (0, 0, 3)
    initial = loop(cE, "E") | loop(cB, "B")
    states = [initial]
    for center, species in [(cE, "E"), (cB, "B"), (cE, "E"), (cB, "B")]:
        states.append(reverse(states[-1], center, species))
    identities = sorted(initial.values())
    check("four_state_cycle_preserves_gauss_capacity_and_record_contents",
          states[-1] == states[0]
          and all(len(s) == 8 and sorted(s.values()) == identities for s in states)
          and all(not charge(field(s, a)) for s in states for a in ("E", "B")),
          distinct_states=len({tuple(sorted(s.items())) for s in states[:-1]}),
          record_count=8, cycle_length=4)
    weights = sp.Matrix([1, 2, 3, 5])
    pi = weights / sum(weights)
    L = sp.zeros(4)
    for i in range(4):
        L[i, (i + 1) % 4] = 1 / weights[i]
        L[i, i] = -1 / weights[i]
    check("nonuniform_weights_preserved_by_common_gauss_cycle_flow",
          pi.T * L == sp.zeros(1, 4),
          pi=[str(x) for x in pi], rates=[str(1 / x) for x in weights])
    rows = []
    for N in (9, 17, 33, 65, 129):
        k = 2 * np.pi * np.array([1, 2, 1]) / N
        for state, successor in zip(states[:-1], states[1:]):
            for a in ("E", "B"):
                F, G = field(state, a), field(successor, a)
                positions = set(F) | set(G)
                delta = {x: G.get(x, np.zeros(3)) - F.get(x, np.zeros(3))
                         for x in positions}
                total = sum(delta.values(), np.zeros(3))
                actual = sum((np.exp(-1j * k @ np.array(x)) * v for x, v in delta.items()),
                             np.zeros(3, dtype=complex)) / N ** 1.5
                bound = sum(np.linalg.norm(v) * np.linalg.norm(x)
                            for x, v in delta.items()) * np.linalg.norm(k) / N ** 1.5
                rows.append({"N": N, "species": a, "increment_norm": float(la.norm(actual)),
                             "bound": float(bound), "zero_content_sum": bool(np.all(total == 0))})
    check("conservative_local_fourier_increment_bound",
          all(r["zero_content_sum"] and r["increment_norm"] <= r["bound"] + 1e-14
              for r in rows), cases=rows)


def long_cycle_countercontrol() -> None:
    rows = []
    tau = 0.25
    for N in (9, 17, 33, 65, 129, 257, 1025):
        theta = 2 * np.pi / N
        lam = np.expm1(1j * theta)
        t = tau * N
        increment = 2 * (1 - np.exp(t * lam).real)
        D = -lam.real
        false_M4_bound = np.sqrt(2) * np.sqrt(2 * t * D)
        true_MN_bound = np.sqrt(2 * t * D) / np.sin(np.pi / N)
        rows.append({"N": N, "euler_time": tau, "microscopic_time": t,
                     "increment": float(increment), "false_M4_bound": float(false_M4_bound),
                     "true_MN_bound": float(true_MN_bound),
                     "imaginary_to_damping": float(abs(lam.imag) / D),
                     "cot_pi_N": float(1 / np.tan(np.pi / N))})
    check("spatial_locality_does_not_imply_bounded_configuration_cycles",
          rows[-1]["increment"] > rows[-1]["false_M4_bound"]
          and abs(rows[-1]["increment"] - 2) < 1e-4
          and all(r["increment"] <= r["true_MN_bound"] + 1e-12 for r in rows),
          euler_limit_increment=2.0, cases=rows)


def main() -> None:
    cycle_constants()
    overlapping_cycles()
    immutable_gauss_cycle()
    long_cycle_countercontrol()
    note = HERE / "BOUNDED_CYCLE_FLOW_AND_EULER_DYNAMICS.md"
    out = {"scope": "Author finite/exact/numerical controls; uniform proof and independent review remain distinct.",
           "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
           "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "checks": ROWS, "pass": all(r["pass"] for r in ROWS)}
    (HERE / "BOUNDED_CYCLE_FLOW_RESULTS.json").write_text(json.dumps(out, indent=2) + "\n")
    print(f"TOTAL: PASS={len(ROWS)} FAIL=0")


if __name__ == "__main__":
    main()
