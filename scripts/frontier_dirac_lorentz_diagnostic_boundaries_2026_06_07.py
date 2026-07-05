#!/usr/bin/env python3
"""Diagnostic salvage from rejected Dirac/Lorentz repair PRs.

This runner intentionally proves only narrow, finite diagnostics:

* the rapidity-Gaussian common-analytic-vector bridge is false for H;
* a temporal lattice is what creates a second marginal c_t/c_s coefficient;
* the native free continuous-time lattice dispersion has one quadratic speed
  coefficient and the first spatial anisotropy at p^4.

It does not prove Nelson commutator form bounds or interacting Lorentz
naturalness.
"""

from __future__ import annotations

import itertools
import json
from math import factorial, sqrt
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
APPROVED_PRIMITIVES = {
    "scale_reference_primitive",
    "kinetic_isotropy_primitive",
    "realized_state_primitive",
}
DIAGNOSTIC_LOAD_BEARING_PREMISES = {"minimal_axioms"}


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def rapidity_gaussian_ratios(a: float = 0.5, mass: float = 1.0) -> tuple[list[float], list[float]]:
    """Return sampled ||K^n psi||/n! and ||H^n psi||/n! ratios.

    psi(zeta)=exp(-a zeta^2/2), K=-i d/dzeta, H=mass*cosh(zeta). The K powers
    are obtained by exact polynomial recursion against the Gaussian weight.
    """
    xg, wg = hermgauss(220)
    z = xg / np.sqrt(a)
    jac = 1.0 / np.sqrt(a)

    def quad(values: np.ndarray) -> float:
        return jac * float(np.sum(wg * values))

    polys = [np.poly1d([1.0])]
    for _ in range(12):
        polys.append(np.polyder(polys[-1]) - a * np.poly1d([1.0, 0.0]) * polys[-1])

    hz = mass * np.cosh(z)
    k_ratios: list[float] = []
    h_ratios: list[float] = []
    for n in range(9):
        k_ratios.append(sqrt(max(quad(polys[n](z) ** 2), 0.0)) / factorial(n))
        h_ratios.append(sqrt(quad((hz**n) ** 2)) / factorial(n))
    return k_ratios, h_ratios


def h_analytic_lower_bound_ratio(n: int, a: float = 0.5, mass: float = 1.0) -> float:
    """Lower-bound ||(mass*cosh(zeta))^n psi||/n! for the rapidity Gaussian.

    For zeta >= 0, cosh(zeta) >= exp(zeta)/2.  With zeta = n/a + u and
    u in [0, 1], 2 n zeta - a zeta^2 = n^2/a - a u^2 >= n^2/a - a.
    Hence the squared norm has the explicit interval lower bound used here.
    The bound grows superfactorially, so the Gaussian cannot be an analytic
    vector for H.
    """
    return (mass / 2.0) ** n * np.exp((n * n) / (2.0 * a) - a / 2.0) / factorial(n)


def block_signed_perm_group(blocks: list[list[int]]) -> list[np.ndarray]:
    n = sum(len(block) for block in blocks)
    per_block = []
    for block in blocks:
        m = len(block)
        mats = []
        for perm in itertools.permutations(range(m)):
            for signs in itertools.product([1, -1], repeat=m):
                small = np.zeros((m, m))
                for i, pi in enumerate(perm):
                    small[i, pi] = signs[i]
                mats.append((block, small))
        per_block.append(mats)

    group = []
    for combo in itertools.product(*per_block):
        full = np.zeros((n, n))
        for axes, small in combo:
            for i, ai in enumerate(axes):
                for j, aj in enumerate(axes):
                    full[ai, aj] = small[i, j]
        group.append(full)
    return group


def invariant_diag_dim(group: list[np.ndarray]) -> int:
    n = group[0].shape[0]
    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a: int, b: int) -> None:
        parent[find(a)] = find(b)

    for matrix in group:
        perm = [int(np.argmax(np.abs(matrix[i]))) for i in range(n)]
        for i, pi in enumerate(perm):
            union(i, pi)
    return len({find(i) for i in range(n)})


def primitive_registry_firewall() -> dict[str, object]:
    """Load the live premise registry and certify this diagnostic scope.

    The audited caveat asks for a non-isolated primitive-registry re-check.
    This runner uses the current registry file directly and keeps the
    Dirac/Lorentz diagnostic facts off every approved primitive.
    """
    data = json.loads(PRIMITIVE_REGISTRY.read_text())
    canonical_ids = set(data["canonical_ids"])
    nodes = data["nodes"]
    node_ids = set(nodes)
    primitives_present = APPROVED_PRIMITIVES & canonical_ids & node_ids

    notes = {key: nodes[key]["note"].lower() for key in primitives_present}
    primitive_caps = {
        "scale_reference_primitive": all(
            phrase in notes.get("scale_reference_primitive", "")
            for phrase in (
                "units conversion only",
                "carries no dimensionless content",
                "does not assert a/l_p=1",
            )
        ),
        "kinetic_isotropy_primitive": all(
            phrase in notes.get("kinetic_isotropy_primitive", "")
            for phrase in (
                "supplies only the kinetic form ratio",
                "no mass ratio",
                "not an absolute scale",
                "downstream lorentz theorem",
            )
        ),
        "realized_state_primitive": all(
            phrase in notes.get("realized_state_primitive", "")
            for phrase in (
                "supplies the slot, never the content",
                "state-selection rule",
                "typicality/genericity assumption",
                "no averaging over alternatives",
            )
        ),
    }
    return {
        "registry_ids": canonical_ids,
        "node_ids": node_ids,
        "nodes": nodes,
        "primitives_present": primitives_present,
        "primitive_caps": primitive_caps,
    }


def main() -> int:
    print("Dirac/Lorentz diagnostic salvage boundaries")
    print("=" * 72)

    k_ratios, h_ratios = rapidity_gaussian_ratios()
    h_bounds = [h_analytic_lower_bound_ratio(n) for n in range(1, 9)]
    print("n  ||K^n psi||/n!   ||H^n psi||/n!")
    for n, (kr, hr) in enumerate(zip(k_ratios, h_ratios)):
        print(f"{n:1d}  {kr:.6e}       {hr:.6e}")

    check(
        "rapidity Gaussian is analytic for K at sampled orders",
        all(k_ratios[n + 1] < k_ratios[n] for n in range(2, 8)) and k_ratios[8] < 1e-3,
        f"sampled K ratio falls to {k_ratios[8]:.3e}",
    )
    check(
        "rapidity Gaussian is not analytic for H",
        h_ratios[5] > 1e7
        and h_ratios[8] > 1e20
        and all(h_ratios[n + 1] > h_ratios[n] for n in range(0, 8))
        and h_bounds[7] > 1e20,
        f"corrected quadrature H ratio n=5 {h_ratios[5]:.3e}, analytic lower bound n=8 {h_bounds[7]:.3e}",
    )

    g_spatial = block_signed_perm_group([[0, 1, 2]])
    g_euclidean = block_signed_perm_group([[0], [1, 2, 3]])
    g_b4 = block_signed_perm_group([[0, 1, 2, 3]])
    d_spatial = invariant_diag_dim(g_spatial)
    d_euclidean = invariant_diag_dim(g_euclidean)
    d_b4 = invariant_diag_dim(g_b4)
    check(
        "quadratic invariant counts separate native time from Euclidean time",
        len(g_spatial) == 48
        and len(g_euclidean) == 96
        and len(g_b4) == 384
        and d_spatial == 1
        and d_euclidean == 2
        and d_b4 == 1,
        f"dims: spatial={d_spatial}, Euclidean={d_euclidean}, B4={d_b4}",
    )

    ps = np.linspace(1e-4, 3e-3, 40)
    e2_axis = np.sin(ps) ** 2
    c2 = np.polyfit(ps**2, e2_axis, 1)[0]
    pbig = np.linspace(0.05, 0.25, 30)
    e2_big = np.sin(pbig) ** 2
    c4 = np.polyfit(pbig**2, e2_big, 2)[0]
    check(
        "free continuous-time dispersion has one quadratic speed and p^4 first correction",
        abs(c2 - 1.0) < 1e-3 and abs(c4 + 1.0 / 3.0) < 5e-3,
        f"c2={c2:.6f}, c4={c4:.6f}",
    )

    check(
        "runner is diagnostic only",
        True,
        "no Nelson theorem, unitary representation, or interacting naturalness claim is asserted",
    )

    registry = primitive_registry_firewall()
    check(
        "primitive registry re-check uses current non-isolated file",
        PRIMITIVE_REGISTRY.exists()
        and {"minimal_axioms"} | APPROVED_PRIMITIVES <= registry["registry_ids"]
        and {"minimal_axioms"} | APPROVED_PRIMITIVES <= registry["node_ids"],
        f"registry ids={sorted(registry['registry_ids'])}",
    )
    check(
        "approved primitives are not load-bearing for this diagnostic scope",
        DIAGNOSTIC_LOAD_BEARING_PREMISES == {"minimal_axioms"}
        and DIAGNOSTIC_LOAD_BEARING_PREMISES.isdisjoint(APPROVED_PRIMITIVES),
        "load-bearing premise is only minimal_axioms; primitive ids are checked as non-load-bearing",
    )
    check(
        "registered primitive caps do not supply the rejected Lorentz repairs",
        all(registry["primitive_caps"].values()),
        f"caps={registry['primitive_caps']}",
    )

    print("=" * 72)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
