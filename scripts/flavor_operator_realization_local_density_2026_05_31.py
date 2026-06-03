#!/usr/bin/env python3
"""Executable local-density bridge for the flavor 2/9 packet.

This runner replaces the former prose-only operator claims with an explicit
finite-lattice check.  It builds the 3D Kawamoto-Smit nearest-neighbor
staggered operator on even periodic L^3 lattices, verifies that a raw C3 axis
permutation fails to commute, solves the site-local Z2 gauge correction, and
then checks that the corrected physical C3 symmetry commutes exactly.

The local Atiyah-Bott density is then computed from the corrected C3 tangent
weights (1,2), while the global eta/equivariant-eta readouts are checked to
vanish by the staggered chirality pairing.  The remaining physical
identification of a single fixed-point density as the charged-lepton asymmetry
observable is intentionally not discharged here.
"""

from __future__ import annotations

import itertools

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
TOL = 1.0e-9


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")
    return cond


def sites(L: int) -> list[tuple[int, int, int]]:
    return list(itertools.product(range(L), repeat=3))


def shift(site: tuple[int, int, int], axis: int, L: int, step: int = 1) -> tuple[int, int, int]:
    out = list(site)
    out[axis] = (out[axis] + step) % L
    return tuple(out)


def eta_phase(site: tuple[int, int, int], axis: int, order: tuple[int, int, int] = (0, 1, 2)) -> int:
    """Kawamoto-Smit phase for a chosen axis ordering."""
    pos = {ax: i for i, ax in enumerate(order)}
    exponent = sum(site[nu] for nu in range(3) if pos[nu] < pos[axis])
    return -1 if exponent % 2 else 1


def build_staggered_D(L: int) -> tuple[np.ndarray, list[tuple[int, int, int]], dict[tuple[int, int, int], int]]:
    """Real antisymmetric nearest-neighbor staggered operator on L^3."""
    lattice_sites = sites(L)
    index = {site: i for i, site in enumerate(lattice_sites)}
    D = np.zeros((len(lattice_sites), len(lattice_sites)), dtype=float)
    for site in lattice_sites:
        row = index[site]
        for axis in range(3):
            plus = shift(site, axis, L, 1)
            minus = shift(site, axis, L, -1)
            D[row, index[plus]] += 0.5 * eta_phase(site, axis)
            D[row, index[minus]] += -0.5 * eta_phase(minus, axis)
    return D, lattice_sites, index


def coordinate_permutation_matrix(
    L: int, perm: tuple[int, int, int]
) -> tuple[np.ndarray, list[tuple[int, int, int]]]:
    """Permutation matrix for n -> (n_perm[0], n_perm[1], n_perm[2])."""
    lattice_sites = sites(L)
    index = {site: i for i, site in enumerate(lattice_sites)}
    P = np.zeros((len(lattice_sites), len(lattice_sites)), dtype=float)
    for site in lattice_sites:
        image = tuple(site[perm[i]] for i in range(3))
        P[index[image], index[site]] = 1.0
    return P, lattice_sites


def solve_sign_gauge(D: np.ndarray, target: np.ndarray) -> tuple[np.ndarray, float]:
    """Solve signs s_i with diag(s) target diag(s) = D on the NN graph."""
    n = D.shape[0]
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for i in range(n):
        for j in np.nonzero(np.abs(D[i]) > TOL)[0]:
            if abs(target[i, j]) <= TOL:
                raise ValueError(f"target support missing on edge {(i, j)}")
            ratio = D[i, j] / target[i, j]
            if abs(abs(ratio) - 1.0) > TOL:
                raise ValueError(f"non-sign edge ratio on {(i, j)}: {ratio}")
            adjacency[i].append((int(j), 1 if ratio > 0 else -1))

    signs: list[int | None] = [None] * n
    signs[0] = 1
    queue = [0]
    while queue:
        i = queue.pop()
        assert signs[i] is not None
        for j, edge_ratio in adjacency[i]:
            wanted = edge_ratio * signs[i]
            if signs[j] is None:
                signs[j] = wanted
                queue.append(j)
            elif signs[j] != wanted:
                raise ValueError(f"inconsistent sign gauge at edge {(i, j)}")
    if any(s is None for s in signs):
        raise ValueError("sign gauge did not reach every lattice site")

    s_array = np.array(signs, dtype=float)
    S = np.diag(s_array)
    residual = float(np.linalg.norm(S @ target @ S - D))
    return s_array, residual


def local_density_exact() -> tuple[sp.Rational, sp.Rational, sp.Expr]:
    omega = sp.exp(2 * sp.pi * sp.I / 3)

    def density(weights: tuple[int, int]) -> sp.Rational:
        value = sp.Rational(1, 3) * sum(
            1 / ((omega ** (k * weights[0]) - 1) * (omega ** (k * weights[1]) - 1))
            for k in (1, 2)
        )
        return sp.nsimplify(sp.simplify(value))

    transverse_det = sp.nsimplify(sp.simplify((1 - omega) * (1 - omega**2)))
    return density((1, 2)), density((1, 1)), transverse_det


def tangent_weight_check() -> tuple[bool, str]:
    perm = (1, 2, 0)
    P3 = sp.zeros(3, 3)
    for j in range(3):
        P3[perm[j], j] = 1
    lam = sp.symbols("lam")
    charpoly = sp.factor(P3.charpoly(lam).as_expr())
    omega = sp.exp(2 * sp.pi * sp.I / 3)
    one = sp.Matrix([1, 1, 1])
    transverse_1 = sp.Matrix([1, omega, omega**2])
    transverse_2 = sp.Matrix([1, omega**2, omega])
    ok = (
        sp.expand(charpoly - (lam**3 - 1)) == 0
        and P3 * one == one
        and sp.simplify(P3 * transverse_1 - omega**2 * transverse_1) == sp.zeros(3, 1)
        and sp.simplify(P3 * transverse_2 - omega * transverse_2) == sp.zeros(3, 1)
    )
    return ok, f"charpoly={charpoly}; transverse eigenweights are omega and omega^2"


def operator_packet(L: int) -> dict[str, float | complex | int]:
    D, lattice_sites, _ = build_staggered_D(L)
    P, _ = coordinate_permutation_matrix(L, (1, 2, 0))
    raw_conjugate = P @ D @ P.T
    raw_error = float(np.linalg.norm(raw_conjugate - D))
    signs, gauge_residual = solve_sign_gauge(D, raw_conjugate)
    S = np.diag(signs)
    U_phys = S @ P
    commutation_error = float(np.linalg.norm(U_phys @ D @ U_phys.T - D))
    order_error = float(np.linalg.norm(U_phys @ U_phys @ U_phys - np.eye(D.shape[0])))

    gamma5 = np.diag([(-1) ** sum(site) for site in lattice_sites])
    gamma_anticomm_error = float(np.linalg.norm(D @ gamma5 + gamma5 @ D))
    H = 1j * D
    evals, evecs = np.linalg.eigh(H)
    signs_e = np.sign(np.where(np.abs(evals) < TOL, 0.0, evals))
    eta_sum = float(np.sum(signs_e))
    signH = (evecs * signs_e) @ evecs.conj().T
    equivariant_eta = complex(np.trace(U_phys @ signH))
    graded_lefschetz = complex(np.trace(gamma5 @ U_phys))
    zero_modes = int(np.sum(np.abs(evals) < TOL))

    return {
        "antisym_error": float(np.linalg.norm(D + D.T)),
        "raw_error": raw_error,
        "gauge_residual": gauge_residual,
        "commutation_error": commutation_error,
        "order_error": order_error,
        "gamma_anticomm_error": gamma_anticomm_error,
        "eta_sum": eta_sum,
        "equivariant_eta_abs": abs(equivariant_eta),
        "graded_lefschetz_abs": abs(graded_lefschetz),
        "zero_modes": zero_modes,
    }


def main() -> int:
    print("FLAVOR OPERATOR-REALIZATION LOCAL DENSITY REPAIR")

    L12, L11, transverse_det = local_density_exact()
    check(
        "local Atiyah-Bott density: L_3(1,2)=2/9 and degenerate L_3(1,1)=1/9",
        L12 == sp.Rational(2, 9) and L11 == sp.Rational(1, 9),
        f"L_3(1,2)={L12}; L_3(1,1)={L11}",
    )
    check(
        "transverse determinant is det(1-dg)=(1-omega)(1-omega^2)=3",
        transverse_det == 3,
        f"det={transverse_det}",
    )
    tangent_ok, tangent_detail = tangent_weight_check()
    check("C3 tangent splits as singlet plus faithful transverse weights (1,2)", tangent_ok, tangent_detail)

    packets = {L: operator_packet(L) for L in (4, 6)}
    for L, pkt in packets.items():
        check(
            f"L={L}: staggered operator is antisymmetric and gamma5-anticommuting",
            pkt["antisym_error"] < TOL and pkt["gamma_anticomm_error"] < TOL,
            f"||D+D^T||={pkt['antisym_error']:.1e}; ||D gamma5 + gamma5 D||={pkt['gamma_anticomm_error']:.1e}",
        )
        check(
            f"L={L}: raw C3 axis permutation fails but a site-local Z2 gauge repairs it",
            pkt["raw_error"] > 1.0
            and pkt["gauge_residual"] < TOL
            and pkt["commutation_error"] < TOL
            and pkt["order_error"] < TOL,
            "raw ||PDP^T-D||="
            f"{pkt['raw_error']:.6g}; gauge residual={pkt['gauge_residual']:.1e}; "
            f"corrected comm={pkt['commutation_error']:.1e}; ||U^3-I||={pkt['order_error']:.1e}",
        )
        check(
            f"L={L}: global eta, equivariant eta, and graded Lefschetz traces vanish",
            abs(pkt["eta_sum"]) < TOL
            and pkt["equivariant_eta_abs"] < 1.0e-8
            and pkt["graded_lefschetz_abs"] < TOL,
            f"zero_modes={pkt['zero_modes']}; eta={pkt['eta_sum']:.1e}; "
            f"|eta_U|={pkt['equivariant_eta_abs']:.1e}; |Tr(gamma5 U)|={pkt['graded_lefschetz_abs']:.1e}",
        )

    check(
        "local/global split is explicit: the 2/9 local density survives only as a fixed-point summand",
        L12 == sp.Rational(2, 9)
        and all(abs(pkt["eta_sum"]) < TOL and pkt["equivariant_eta_abs"] < 1.0e-8 for pkt in packets.values()),
        "the runner does not promote the single summand to the physical observable",
    )

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: operator side repaired. The native finite staggered operator has a nontrivial "
        "gauge-corrected C3 symmetry, its tangent weights give the local density 2/9, and the "
        "global eta/equivariant readouts vanish. Remaining open bridge: physical identification "
        "of the single fixed-point local density as the charged-lepton asymmetry observable."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
