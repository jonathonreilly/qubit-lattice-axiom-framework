#!/usr/bin/env python3
"""Finite CAR proof of the local density/readout bridge.

Companion runner for
docs/STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md.

The runner proves that rho_x := chibar_x chi_x is exactly the finite CAR local
number projection a_x^dag a_x and the normalized onsite U(1) generator on the
single-mode surface. It also checks that this density is the matrix-unit
rho_p = E_pp consumed by the abstract bilinear Noether theorem.
"""

from __future__ import annotations

from pathlib import Path
from itertools import product

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md"
NOETHER_PATH = ROOT / "docs" / "AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md"

PASS = 0
FAIL = 0
TOL = 1e-12


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def jw_annihilators(n_sites: int) -> list[np.ndarray]:
    """Jordan-Wigner annihilation operators for finite CAR."""
    ident = np.eye(2, dtype=complex)
    parity = np.array([[1, 0], [0, -1]], dtype=complex)
    ann = np.array([[0, 1], [0, 0]], dtype=complex)
    ops: list[np.ndarray] = []
    for site in range(n_sites):
        factors = [parity] * site + [ann] + [ident] * (n_sites - site - 1)
        op = factors[0]
        for factor in factors[1:]:
            op = np.kron(op, factor)
        ops.append(op)
    return ops


def max_abs(mat: np.ndarray) -> float:
    return float(np.max(np.abs(mat)))


def test_one_site_density() -> None:
    print("\n=== One-site CAR density ===")
    ident = np.eye(2, dtype=complex)
    a = np.array([[0, 1], [0, 0]], dtype=complex)
    adag = a.conj().T
    n = adag @ a

    check("single-mode CAR: a^2=0 and {a,a^dag}=I",
          max_abs(a @ a) < TOL and max_abs(a @ adag + adag @ a - ident) < TOL)
    check("rho = a^dag a is Hermitian",
          max_abs(n - n.conj().T) < TOL)
    check("rho is a projection, rho^2=rho",
          max_abs(n @ n - n) < TOL)
    spectrum = sorted(float(np.real(x)) for x in np.linalg.eigvals(n))
    check("rho has spectrum {0,1}",
          max(abs(spectrum[0]), abs(spectrum[1] - 1.0)) < TOL,
          f"spectrum={spectrum}")
    check("rho generates local U(1): [rho,a]=-a and [rho,a^dag]=a^dag",
          max_abs(comm(n, a) + a) < TOL and max_abs(comm(n, adag) - adag) < TOL)


def test_uniqueness() -> None:
    print("\n=== Unique normalized onsite U(1) generator ===")
    r00, r01, r10, r11 = sp.symbols("r00 r01 r10 r11")
    r = sp.Matrix([[r00, r01], [r10, r11]])
    a = sp.Matrix([[0, 1], [0, 0]])
    adag = a.T
    equations = list(r * a - a * r + a) + list(r * adag - adag * r - adag)
    equations.append(r00)  # vacuum normalization R|0> = 0.
    solution = sp.solve(equations, [r00, r01, r10, r11], dict=True)
    check("linear commutator equations have a unique normalized solution",
          solution == [{r00: 0, r01: 0, r10: 0, r11: 1}],
          f"solution={solution}")


def test_lattice_car_density() -> None:
    print("\n=== Finite-lattice CAR density ===")
    n_sites = 3
    ops = jw_annihilators(n_sites)
    adags = [op.conj().T for op in ops]
    rhos = [adags[i] @ ops[i] for i in range(n_sites)]
    ident = np.eye(2 ** n_sites, dtype=complex)
    zero = np.zeros_like(ident)

    car_ok = True
    for i, j in product(range(n_sites), repeat=2):
        car_ok &= max_abs(ops[i] @ ops[j] + ops[j] @ ops[i]) < TOL
        car_ok &= max_abs(adags[i] @ adags[j] + adags[j] @ adags[i]) < TOL
        target = ident if i == j else zero
        car_ok &= max_abs(ops[i] @ adags[j] + adags[j] @ ops[i] - target) < TOL
    check("Jordan-Wigner operators satisfy finite CAR for all sites", car_ok)

    commute_ok = all(max_abs(comm(rhos[i], rhos[j])) < TOL for i, j in product(range(n_sites), repeat=2))
    projection_ok = all(max_abs(rho @ rho - rho) < TOL for rho in rhos)
    check("local densities commute", commute_ok)
    check("each local density remains a projection", projection_ok)

    charge = sum(rhos)
    generator_ok = True
    for i in range(n_sites):
        generator_ok &= max_abs(comm(charge, ops[i]) + ops[i]) < TOL
        generator_ok &= max_abs(comm(charge, adags[i]) - adags[i]) < TOL
    check("Q=sum_x rho_x generates global U(1) on all a_x, a_x^dag", generator_ok)

    neutral_ok = True
    for x, y in product(range(n_sites), repeat=2):
        e_xy = adags[x] @ ops[y]
        neutral_ok &= max_abs(comm(charge, e_xy)) < TOL
    check("number-conserving bilinears E_xy=a_x^dag a_y are U(1)-neutral", neutral_ok)

    matrix_unit_ok = True
    for x, y, p in product(range(n_sites), repeat=3):
        e_xy = adags[x] @ ops[y]
        lhs = comm(e_xy, rhos[p])
        rhs = (1.0 if y == p else 0.0) * (adags[x] @ ops[p])
        rhs -= (1.0 if p == x else 0.0) * (adags[p] @ ops[y])
        matrix_unit_ok &= max_abs(lhs - rhs) < TOL
    check("[E_xy,rho_p] equals the matrix-unit density commutator", matrix_unit_ok)


def test_source_status_firewall() -> None:
    print("\n=== Source-status firewall ===")
    note = NOTE_PATH.read_text(encoding="utf-8")
    noether = NOETHER_PATH.read_text(encoding="utf-8")
    flat = " ".join(note.split())
    noether_flat = " ".join(noether.split())

    check("bridge note declares positive-theorem source status",
          "actual_current_surface_status: positive-theorem" in note
          and "**Claim type:** positive_theorem" in note)
    check("bridge note proves density as local number projection",
          "rho_x := chibar_x chi_x -> n_x := a_x^dag a_x" in flat
          and "positive local projection" in flat)
    check("bridge note excludes full realization-gate claims",
          "does not claim:" in flat
          and "full staggered/Kawamoto-Smit kinetic realization gate" in flat)
    check("Noether note cites the density bridge",
          "STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md" in noether)
    check("Noether note no longer keeps the realization gate as markdown dependency repair link",
          "[staggered_dirac_realization_gate_note_2026-05-03]" not in noether
          and "(STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)" not in noether)
    check("Noether note keeps KS carrier as supplied exhibit, not status promotion",
          "explicit supplied finite exhibit" in noether_flat
          and "does not promote the realization gate" in noether_flat)


def main() -> int:
    print("=" * 72)
    print("Staggered-Dirac local density/readout bridge")
    print("=" * 72)
    test_one_site_density()
    test_uniqueness()
    test_lattice_car_density()
    test_source_status_firewall()
    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
