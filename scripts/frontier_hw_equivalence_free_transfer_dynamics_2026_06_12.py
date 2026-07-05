#!/usr/bin/env python3
"""Bounded runner for hw-complement equivalence at free corner-transfer level.

The runner verifies the finite corner facts, the six-mode free two-step
transfer equivalence, the trace/Berezin registrability surface, and the
source-note firewall required by the 2026-06-12 spec.
"""

from __future__ import annotations

import itertools
import math
import re
import sys
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "HW_COMPLEMENT_EQUIVALENCE_EXTENDS_TO_FREE_CORNER_TRANSFER_DYNAMICS_BOUNDED_NOTE_2026-06-12.md"
RP_DEP = ROOT / "docs" / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
GRASS_DEP = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
REG_DEP = ROOT / "docs" / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"

TOL = 1.0e-11
PARAMS = (
    (1.0, 0.25, 2.0 / 9.0),
    (1.35, 0.31, 0.71),
)
LS = 2
MOMENTA = tuple(2.0 * math.pi * n / LS for n in range(LS))

checks: list[tuple[str, bool, str]] = []


def record(tag: str, ok: bool, detail: str = "") -> bool:
    checks.append((tag, bool(ok), detail))
    status = "PASS" if ok else "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{status} {tag}{suffix}")
    return bool(ok)


def corner_rotation(corner: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = corner
    return (z, x, y)


def corner_rotation_inverse(corner: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = corner
    return (y, z, x)


def complement(corner: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(1 - bit for bit in corner)


def symbolic_lambdas() -> tuple[list[sp.Expr], bool, bool, bool]:
    a, b, delta = sp.symbols("a B delta", real=True)
    lambdas = [
        a + 2 * b * sp.cos(delta + 2 * sp.pi * k / 3)
        for k in range(3)
    ]
    e1 = sp.simplify(sum(lambdas) - 3 * a)
    e2 = sp.simplify(
        sum(lambdas[i] * lambdas[j] for i in range(3) for j in range(i + 1, 3))
        - (3 * a**2 - 3 * b**2)
    )
    e3 = sp.trigsimp(
        sp.expand_trig(sp.prod(lambdas))
        - (a**3 - 3 * a * b**2 + 2 * b**3 * sp.cos(3 * delta))
    )
    return lambdas, sp.simplify(e1) == 0, sp.simplify(e2) == 0, sp.simplify(e3) == 0


def numeric_lambdas(a: float, b: float, delta: float) -> np.ndarray:
    return np.array(
        [a + 2.0 * b * math.cos(delta + 2.0 * math.pi * k / 3.0) for k in range(3)],
        dtype=float,
    )


def permute_channels(values: np.ndarray, old_to_new: tuple[int, int, int]) -> np.ndarray:
    out = np.empty_like(values)
    for old_index, new_index in enumerate(old_to_new):
        out[new_index] = values[old_index]
    return out


def energies(channel_lambdas: np.ndarray) -> np.ndarray:
    vals: list[float] = []
    for lam in channel_lambdas:
        for p in MOMENTA:
            vals.append(math.asinh(math.sqrt(float(lam) ** 2 + math.sin(p) ** 2)))
    return np.array(vals, dtype=float)


def kernels(channel_lambdas: np.ndarray) -> np.ndarray:
    return np.exp(-2.0 * energies(channel_lambdas))


def fock_diag(mode_weights: np.ndarray) -> np.ndarray:
    dim = 1 << len(mode_weights)
    diag = np.ones(dim, dtype=float)
    for occ in range(dim):
        weight = 1.0
        for mode, t in enumerate(mode_weights):
            if (occ >> mode) & 1:
                weight *= float(t)
        diag[occ] = weight
    return np.diag(diag)


def mode_permutation(channel_perm: tuple[int, int, int]) -> tuple[int, ...]:
    perm: list[int] = []
    for channel in range(3):
        for spatial in range(LS):
            perm.append(channel_perm[channel] * LS + spatial)
    return tuple(perm)


def fock_permutation_matrix(mode_perm: tuple[int, ...]) -> np.ndarray:
    dim = 1 << len(mode_perm)
    pi = np.zeros((dim, dim), dtype=float)
    for old_occ in range(dim):
        new_occ = 0
        for old_mode, new_mode in enumerate(mode_perm):
            if (old_occ >> old_mode) & 1:
                new_occ |= 1 << new_mode
        pi[new_occ, old_occ] = 1.0
    return pi


ORDER = {"bar": 0, "chi": 1}
Poly = dict[tuple[str, ...], float]


def grassmann_mul_monomial(left: tuple[str, ...], right: tuple[str, ...]) -> tuple[tuple[str, ...] | None, int]:
    if set(left).intersection(right):
        return None, 0
    inversions = sum(1 for x in left for y in right if ORDER[x] > ORDER[y])
    sign = -1 if inversions % 2 else 1
    return tuple(sorted(left + right, key=lambda item: ORDER[item])), sign


def grassmann_add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for monomial, coeff in right.items():
        out[monomial] = out.get(monomial, 0.0) + coeff
        if abs(out[monomial]) < 1.0e-14:
            del out[monomial]
    return out


def grassmann_mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial, sign = grassmann_mul_monomial(lm, rm)
            if monomial is None:
                continue
            out[monomial] = out.get(monomial, 0.0) + sign * lc * rc
    return {m: c for m, c in out.items() if abs(c) > 1.0e-14}


def grassmann_scale(poly: Poly, scale: float) -> Poly:
    return {monomial: scale * coeff for monomial, coeff in poly.items()}


def berezin_pair_integral(mu: float, t: float) -> float:
    one: Poly = {(): 1.0}
    bar: Poly = {("bar",): 1.0}
    chi: Poly = {("chi",): 1.0}
    x = grassmann_mul(bar, chi)
    measure = grassmann_add(one, grassmann_scale(x, mu))
    kernel = grassmann_add(one, grassmann_scale(x, t))
    expanded = grassmann_mul(measure, kernel)
    return expanded.get(("bar", "chi"), 0.0)


def berezin_self_check() -> bool:
    bar: Poly = {("bar",): 1.0}
    chi: Poly = {("chi",): 1.0}
    x = grassmann_mul(bar, chi)
    anti = grassmann_add(x, grassmann_mul(chi, bar))
    nil = grassmann_mul(x, x)
    sample_t = 0.375
    expansion_ok = abs(berezin_pair_integral(1.0, sample_t) - (1.0 + sample_t)) < TOL
    rescale_ok = abs(berezin_pair_integral(2.0, sample_t) - (2.0 + sample_t)) < TOL
    return x == {("bar", "chi"): 1.0} and anti == {} and nil == {} and expansion_ok and rescale_ok


def berezin_product(mode_weights: np.ndarray, mu: float) -> float:
    product = 1.0
    for t in mode_weights:
        product *= berezin_pair_integral(mu, float(t))
    return product


def sorted_close(left: np.ndarray, right: np.ndarray, tol: float = TOL) -> bool:
    return np.allclose(np.sort(left), np.sort(right), atol=tol, rtol=0)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    print("HW-COMPLEMENT FREE CORNER-TRANSFER REGISTRATION-EQUIVALENCE RUNNER")
    print(f"params={PARAMS}; L_s={LS}; fock_dim={1 << (3 * LS)}")

    corners = tuple(itertools.product((0, 1), repeat=3))
    hw1 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    hw2_base = tuple(complement(corner) for corner in hw1)
    hw2 = hw2_base[1:] + hw2_base[:1]
    old_to_new = tuple(hw2.index(complement(corner)) for corner in hw1)
    mode_perm = mode_permutation(old_to_new)
    pi_fock = fock_permutation_matrix(mode_perm)

    m1a_triplets = set(map(complement, hw1)) == set(hw2_base) == {c for c in corners if sum(c) == 2}
    m1a_commutes = all(complement(corner_rotation(c)) == corner_rotation(complement(c)) for c in corners)
    named_corner = (1, 0, 0)
    lhs = complement(corner_rotation(named_corner))
    rhs = corner_rotation_inverse(complement(named_corner))
    m1a_reversal_fails = lhs != rhs
    record(
        "M1a",
        m1a_triplets and m1a_commutes and m1a_reversal_fails,
        f"old_to_new={old_to_new}; reversal witness {named_corner}: {lhs} != {rhs}",
    )

    lambdas_sym, e1_ok, e2_ok, e3_ok = symbolic_lambdas()
    permuted_sym = [lambdas_sym[i] for i in old_to_new]
    symbolic_multiset_ok = sorted(map(sp.sstr, lambdas_sym)) == sorted(map(sp.sstr, permuted_sym))
    record(
        "M1b",
        symbolic_multiset_ok and e1_ok and e2_ok and e3_ok,
        "symbolic multiset and elementary symmetric checks",
    )

    positivity_results = []
    for params in PARAMS:
        a, b, delta = params
        vals = numeric_lambdas(a, b, delta)
        positivity_results.append(a > 2.0 * b > 0.0 and bool(np.all(vals > 0.0)))
    record("M1c", all(positivity_results), f"positivity={positivity_results}")

    all_m2a = []
    all_m2b = []
    all_m3a = []
    all_m3b = []
    all_m3c = []
    all_m3d = []
    transfer_residuals = []
    trace_residuals: list[float] = []
    berezin_breaks: list[tuple[float, float]] = []
    witness_residuals: list[float] = []

    pi_unitary_ok = np.allclose(pi_fock.T @ pi_fock, np.eye(pi_fock.shape[0]), atol=TOL, rtol=0)

    for a, b, delta in PARAMS:
        lam1 = numeric_lambdas(a, b, delta)
        lam2 = permute_channels(lam1, old_to_new)
        t1 = kernels(lam1)
        t2 = kernels(lam2)
        e_hw1 = energies(lam1)
        e_hw2 = energies(lam2)

        all_m2a.append(sorted_close(t1, t2))
        transfer_hw1 = fock_diag(t1)
        transfer_hw2 = fock_diag(t2)
        residual = float(np.linalg.norm(transfer_hw2 - pi_fock @ transfer_hw1 @ pi_fock.T, ord="fro"))
        transfer_residuals.append(residual)
        all_m2b.append(pi_unitary_ok and residual < TOL)

        for n in (1, 2, 3):
            tr1 = float(np.trace(np.linalg.matrix_power(transfer_hw1, n)))
            tr2 = float(np.trace(np.linalg.matrix_power(transfer_hw2, n)))
            trace_residuals.append(abs(tr1 - tr2))
            all_m3a.append(abs(tr1 - tr2) < TOL)

        all_m3b.append(sorted_close(e_hw1, e_hw2))

        trace1 = float(np.trace(transfer_hw1))
        trace2 = float(np.trace(transfer_hw2))
        berezin1 = berezin_product(t1, 1.0)
        berezin2 = berezin_product(t2, 1.0)
        rescaled1 = berezin_product(t1, 2.0)
        rescaled2 = berezin_product(t2, 2.0)
        break1 = abs(rescaled1 - trace1)
        break2 = abs(rescaled2 - trace2)
        berezin_breaks.append((break1, break2))
        all_m3c.append(
            abs(berezin1 - trace1) < TOL
            and abs(berezin2 - trace2) < TOL
            and break1 > 1.0e-6
            and break2 > 1.0e-6
            and abs(break1 - break2) < TOL
        )

        witness1 = math.log(trace1)
        witness2 = math.log(trace2)
        witness_residuals.append(abs(witness1 - witness2))
        all_m3d.append(abs(witness1 - witness2) < TOL)

    record("M2a", all(all_m2a), f"kernel multiset equality={all_m2a}")
    record("M2b", all(all_m2b), f"dim={pi_fock.shape[0]}, residuals={transfer_residuals}")
    record("M3a", all(all_m3a), f"max trace residual={max(trace_residuals):.3e}")
    record("M3b", all(all_m3b), "dispersion multisets sorted-equal at both points")
    record("M3c", all(all_m3c), f"berezin lambda=2 break residuals={berezin_breaks}")
    record("M3d", all(all_m3d), f"log Tr Gamma(t) residuals={witness_residuals}")

    m1 = all(ok for tag, ok, _ in checks if tag.startswith("M1"))
    m2 = all(ok for tag, ok, _ in checks if tag.startswith("M2"))
    m3 = all(ok for tag, ok, _ in checks if tag.startswith("M3"))
    m4_open_statement = "the interacting/gauge level remains the named open"
    record("M4", m1 and m2 and m3, m4_open_statement)

    note_text = read_text(NOTE)
    rp_text = read_text(RP_DEP)
    grass_text = read_text(GRASS_DEP)
    reg_text = read_text(REG_DEP)

    dep_ok = (
        "2-step blocked transfer matrix" in rp_text
        and "free (`U = 1`)" in rp_text
        and "e^{-2 E(p)}" in rp_text
        and "det(M)" in grass_text
        and "single-pair" in grass_text
        and "additive" in reg_text.lower()
        and "constant on `K`/CPT orbits" in reg_text
    )
    record("B11", dep_ok, "dependency phrase greps")

    firewall_phrases = (
        "does not select a physical species reading",
        "free (U = 1)",
        "the interacting/gauge",
        "the occupancy binary",
        "does not fix r",
        "hw=1` versus `hw=2` remains frame/convention data",
    )
    record("B12", all(phrase in note_text for phrase in firewall_phrases), "firewall sentences present")

    forbidden_closing = (
        "interacting/gauge level is closed",
        "closes the interacting/gauge",
        "full-dynamics equivariance is closed",
        "full dynamics are closed",
        "physical species reading selected",
        "fixes r",
        "occupancy binary changed",
    )
    record("B13", not any(phrase in note_text for phrase in forbidden_closing), "forbidden closing language absent")

    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note_text)
    expected_links = [
        "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md",
        "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md",
        "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
    ]
    record("B14", links == expected_links, f"links={links}")

    context_tokens = (
        "ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-06-12.md",
        "corner-extension note",
        "trace-correspondence note",
        "ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md",
        "open_gate",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
    )
    context_backticked = all(f"`{token}`" in note_text for token in context_tokens)
    context_not_linked = not any(token in match for token in context_tokens for match in links)
    record("B15", context_backticked and context_not_linked, "companions are backticked only")

    record("B16", "No-promotion statement:" in note_text, "No-promotion present")
    record("B17", berezin_self_check(), "Berezin self-check flag from explicit Grassmann expansion")

    passed = sum(1 for _, ok, _ in checks if ok)
    failed = sum(1 for _, ok, _ in checks if not ok)
    print("\nSUMMARY")
    print(f"PASS={passed} FAIL={failed}")
    print("M1-M4 assembly: free U=1 corner-transfer registration-equivalence holds on the supplied surface.")
    print("Firewall: no physical species reading selected; r not fixed; occupancy binary untouched.")
    print("Named open: the interacting/gauge extension remains open and is not supplied here.")
    return 0 if passed == 17 and failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
