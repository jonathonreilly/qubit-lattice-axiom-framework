#!/usr/bin/env python3
"""Runner for the K/CPT orbit-constancy supplied-context bridge.

This verifies the finite algebra in
KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.
It does not derive the supplied readout context, K/CPT structure, or the
determinant-character/log-character homomorphism boundary from Record.
"""

from __future__ import annotations

import math
import re
from pathlib import Path

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md"


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def wrap_phase(theta: float) -> float:
    return (theta + math.pi) % (2.0 * math.pi) - math.pi


def circulant_h(delta: float, a: float = 1.30, b: float = 0.37) -> np.ndarray:
    ident = np.eye(3, dtype=complex)
    shift = np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=complex,
    )
    return a * ident + b * np.exp(1j * delta) * shift + b * np.exp(-1j * delta) * shift.T


def check_t1_positive() -> None:
    orbit = {0: 0, 1: 2, 2: 1}
    idempotents = [np.diag([1.0 if i == j else 0.0 for i in range(3)]) for j in range(3)]
    idempotent_ok = all(np.allclose(e @ e, e) for e in idempotents)
    orthogonal_ok = all(
        np.allclose(idempotents[j] @ idempotents[k], np.zeros((3, 3)))
        for j in range(3)
        for k in range(3)
        if j != k
    )
    report("A1 3-idempotent context has orthogonal central idempotents", idempotent_ok and orthogonal_ok)

    contents = np.array([0, 1, 1])
    orbit_indexed = all(contents[j] == contents[orbit[j]] for j in range(3))
    report("A2 ORBIT-INDEXING gives equal record content on K/CPT orbits", orbit_indexed)

    rng = np.random.default_rng(20260704)
    all_constant = True
    for _ in range(200):
        readout_by_content = {0: float(rng.normal()), 1: float(rng.normal())}
        values = np.array([readout_by_content[int(content)] for content in contents])
        all_constant = all_constant and all(values[j] == values[orbit[j]] for j in range(3))
    report("A3 200 random content-determined readouts are orbit-constant", all_constant)


def check_t1_negative() -> None:
    orbit = {0: 0, 1: 2, 2: 1}
    contents = np.array([0, 1, 2])
    readout_by_content = {0: 7.0, 1: 0.0, 2: 1.0}
    values = np.array([readout_by_content[int(content)] for content in contents])
    registrable = all(
        values[j] == values[k]
        for j in range(3)
        for k in range(3)
        if contents[j] == contents[k]
    )
    nonconstant = any(values[j] != values[orbit[j]] for j in range(3))
    report(
        "B1 conjugate-distinguishing contents admit a registrable non-orbit-constant readout",
        registrable and nonconstant,
        f"values={values.tolist()}",
    )


def check_t2_symbolic() -> None:
    g0 = sp.Symbol("g0", real=True)
    zero_solution = sp.solve(sp.Eq(g0, g0 + g0), g0)
    report("C1 additivity at zero forces g(0)=0", zero_solution == [0])

    gx, gminusx = sp.symbols("gx gminusx", real=True)
    odd_solution = sp.solve(sp.Eq(gx + gminusx, 0), gminusx)
    report("C2 g(x)+g(-x)=g(0)=0 forces g(-x)=-g(x)", odd_solution == [-gx])

    even_odd_solution = sp.solve(
        [sp.Eq(gminusx, -gx), sp.Eq(gminusx, gx)],
        [gminusx, gx],
        dict=True,
    )
    report("C3 even plus odd forces the homomorphic phase functional to zero", even_odd_solution == [{gminusx: 0, gx: 0}])


def check_t2_concrete() -> None:
    grid = np.array([-0.73, -0.41, -2.0 / 9.0, -0.07, 0.0, 0.07, 2.0 / 9.0, 0.41, 0.73])
    tol = 1e-10

    conj_errors = []
    det_conj_errors = []
    phase_flip_errors = []
    logmod_errors = []
    logmods = []
    det_abs = []
    for delta in grid:
        h_plus = circulant_h(float(delta))
        h_minus = circulant_h(float(-delta))
        conj_errors.append(float(np.max(np.abs(np.conjugate(h_plus) - h_minus))))

        det_plus = np.linalg.det(h_plus)
        det_minus = np.linalg.det(h_minus)
        det_abs.append(float(abs(det_plus)))
        det_conj_errors.append(float(abs(det_minus - np.conjugate(det_plus))))
        phase_flip_errors.append(abs(wrap_phase(float(np.angle(det_plus) + np.angle(det_minus)))))
        logmods.append(math.log(abs(det_plus)))
        logmod_errors.append(abs(math.log(abs(det_plus)) - math.log(abs(det_minus))))

    report("D1 circulant family satisfies conj(H(delta)) = H(-delta)", max(conj_errors) < tol)
    report("D2 det(H(-delta)) is conjugate to det(H(delta))", max(det_conj_errors) < tol)
    report("D3 determinant phase flips sign modulo 2pi under K/CPT", max(phase_flip_errors) < tol)
    report("D4 log|det H(delta)| is K/CPT invariant", max(logmod_errors) < tol)

    # D5 constructs the object instead of asserting it: the continuous
    # R-valued homomorphisms of the phase group are g_c(theta) = c*theta.
    # Oddness (step 4) gives g_c(-theta) = -g_c(theta); T1 evenness (step 5)
    # gives g_c(-theta) = g_c(theta); at a nonzero phase the two force c = 0.
    # The Hermitian circulant family cannot supply the nonzero witness -- its
    # determinant is REAL (phase index already in {0, pi}), which is itself a
    # consistency check that only modulus data survives on that family. The
    # witness lives on generic supplied sector data z_j = r_j e^{i theta_j}.
    det_imag = max(abs(np.linalg.det(circulant_h(float(d))).imag) for d in grid)
    report("D5a Hermitian circulant determinant is real (phase index already in {0, pi})", det_imag < tol)
    sector_thetas = np.array([0.41, -0.15, 0.55])
    theta_witness = wrap_phase(float(np.sum(sector_thetas)))
    report("D5b generic sector data gives a nonzero total-phase witness", abs(theta_witness) > 1e-6)
    c = sp.Symbol("c", real=True)
    theta_s = sp.Symbol("theta_s", real=True, nonzero=True)
    forced_c = sp.solve(sp.Eq(c * theta_s, -c * theta_s), c)
    report("D5c even+odd at a nonzero phase forces the homomorphic coefficient c=0", forced_c == [0])
    forced_values = np.array([0.0 * theta_witness, 0.0 * wrap_phase(-theta_witness)])
    report("D5d the forced (c=0) functional evaluates to 0 on generic sector data", np.allclose(forced_values, 0.0))
    logmod_survives = min(det_abs) > 1e-8 and (max(logmods) - min(logmods)) > 1e-4
    report("D6 log-modulus datum survives as finite nonconstant data", logmod_survives)

    two_ninths_count = int(np.sum(np.isclose(grid, 2.0 / 9.0)))
    two_ninths_finite = math.isfinite(logmods[int(np.where(np.isclose(grid, 2.0 / 9.0))[0][0])])
    report("D7 delta=2/9 is included as an ordinary finite grid point", two_ninths_count == 1 and two_ninths_finite)


def check_hostile_guards() -> None:
    theta, phi, theta1, theta2, phi1, phi2 = sp.symbols(
        "theta phi theta1 theta2 phi1 phi2",
        real=True,
    )

    cos_even = sp.simplify(sp.cos(-theta) - sp.cos(theta)) == 0
    cos_nonzero = sp.cos(0) == 1
    cos_phase_dependent = sp.diff(sp.cos(theta), theta) != 0
    cos_hom_gap = sp.simplify(sp.cos(theta + phi) - sp.cos(theta) - sp.cos(phi))
    report(
        "E1 cos(theta) is K-even, phase-dependent, nonzero, and non-homomorphic",
        cos_even and cos_nonzero and cos_phase_dependent and cos_hom_gap != 0,
    )

    sum_cos = sp.cos(theta1) + sp.cos(theta2)
    sum_cos_neg = sp.cos(-theta1) + sp.cos(-theta2)
    vector_gap = sp.simplify(
        (sp.cos(theta1 + phi1) + sp.cos(theta2 + phi2))
        - (sp.cos(theta1) + sp.cos(theta2))
        - (sp.cos(phi1) + sp.cos(phi2))
    )
    sum_even = sp.simplify(sum_cos_neg - sum_cos) == 0
    sum_nonzero = sum_cos.subs({theta1: 0, theta2: 0}) == 2
    sum_phase_dependent = sp.diff(sum_cos, theta1) != 0
    report(
        "E2 sum_j cos(theta_j) is K-even, phase-dependent, nonzero, and non-homomorphic",
        sum_even and sum_nonzero and sum_phase_dependent and vector_gap != 0,
    )


def check_text_guards() -> None:
    note_text = NOTE.read_text(encoding="utf-8")
    lowered = note_text.lower()

    required_phrases = [
        "supplied",
        "not derived",
        "context handle, not a citation-graph dependency",
    ]
    for phrase in required_phrases:
        report(f"F1 note contains required phrase: {phrase}", phrase in lowered)

    forbidden_phrases = [
        "discharges",
        "retires",
        "closes the admission",
    ]
    for phrase in forbidden_phrases:
        report(f"F2 note excludes forbidden completion phrase: {phrase}", phrase not in lowered)

    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note_text)
    doc_targets = []
    for target in targets:
        bare = target.split("#", 1)[0]
        if bare.endswith(".md") or bare.startswith("docs/") or "/docs/" in bare:
            doc_targets.append(Path(bare).name)
    report(
        "F3 only markdown doc-note citation target is MINIMAL_AXIOMS_2026-06-29.md",
        doc_targets == ["MINIMAL_AXIOMS_2026-06-29.md"],
        f"doc_targets={doc_targets}",
    )


def main() -> int:
    check_t1_positive()
    check_t1_negative()
    check_t2_symbolic()
    check_t2_concrete()
    check_hostile_guards()
    check_text_guards()

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    print("DONE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
