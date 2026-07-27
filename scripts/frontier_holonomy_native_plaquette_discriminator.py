#!/usr/bin/env python3
"""Native-holonomy plaquette discriminator.

Question (well-posed, decidable on a single Z^3 plaquette):

  The retained `native_gauge_closure` surface gives su(3) as a *static
  symmetry* of the 8-dim taste space V = C^2 (x) C^2 (x) C^2. The holonomy
  form U = exp(i a A^a T_a) needs a *gauged connection* living on edges. Does
  the native staggered structure FORCE a nontrivial (traceless) su(3)
  parallel transport around a plaquette, or is the native flux only scalar in
  the taste-operator algebra (so the continuous su(3) connection A^a is added
  structure, not native)?

Method. Build the native taste-space "hop in direction mu" operator under the
two natural identifications the framework actually supplies:

  (1) Clifford generators Gamma_mu  (staggered-phase folded hop), and
  (2) cube one-step axis shifts S_mu (graph-first su(3) construction).

For each, form the lattice plaquette holonomy (group commutator)
  W_{mu,nu} = L_mu L_nu L_mu^{-1} L_nu^{-1},
and measure its traceless su(3)-sector content vs its scalar content.

Verdict:
  - if every native W is proportional to the identity -> scalar native
    taste-space flux, NO native traceless su(3) connection -> connection is
    ADDED structure (the gauge field enters by a separate minimal-coupling
    route);
  - else -> a native continuous su(3) holonomy is forced.

This script asserts no audit status. It is a branch discriminator for the
holonomy-derivation theorem scope.
"""

from __future__ import annotations

import numpy as np

from n5_resolution_certificate import emit_n5_resolution_certificate

AUDIT_INPUT_PATHS = ("scripts/n5_resolution_certificate.py",)

TOL = 1.0e-12
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def kron3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.kron(a, np.kron(b, c))


I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I8 = np.eye(8, dtype=complex)


def clifford_hops() -> list[np.ndarray]:
    """Staggered-phase folded directional hops (same Gamma's as the gauge runner)."""
    return [
        kron3(SX, I2, I2),
        kron3(SY, SX, I2),
        kron3(SY, SY, SX),
    ]


def cube_shift_hops() -> list[np.ndarray]:
    """Graph-first one-step axis shifts on the taste cube {0,1}^3 (bit flips)."""
    return [
        kron3(SX, I2, I2),
        kron3(I2, SX, I2),
        kron3(I2, I2, SX),
    ]


def group_commutator(lmu: np.ndarray, lnu: np.ndarray) -> np.ndarray:
    """Plaquette holonomy: forward mu, forward nu, back mu, back nu.

    Native hops here are involutory unitaries (L^2 = I), so L^{-1} = L.
    """
    inv_mu = np.linalg.inv(lmu)
    inv_nu = np.linalg.inv(lnu)
    return lmu @ lnu @ inv_mu @ inv_nu


def traceless_su_content(w: np.ndarray) -> tuple[float, complex]:
    """Split W = scalar*I + traceless. Return (||traceless||, scalar)."""
    n = w.shape[0]
    scalar = np.trace(w) / n
    traceless = w - scalar * np.eye(n, dtype=complex)
    return float(np.linalg.norm(traceless)), complex(scalar)


def native_su2_generators() -> list[np.ndarray]:
    g = clifford_hops()
    s1 = -0.5j * g[1] @ g[2]
    s2 = -0.5j * g[2] @ g[0]
    s3 = -0.5j * g[0] @ g[1]
    return [s1, s2, s3]


def run_identification(name: str, hops: list[np.ndarray]) -> bool:
    print("\n" + "-" * 76)
    print(f"Identification: {name}")
    print("-" * 76)

    # sanity: native hops are unitary and involutory
    for i, l in enumerate(hops, start=1):
        check(f"L_{i} unitary", np.linalg.norm(l.conj().T @ l - I8) < TOL)
        check(f"L_{i} involutory (L^2 = I)", np.linalg.norm(l @ l - I8) < TOL)

    all_scalar = True
    for mu in range(3):
        for nu in range(mu + 1, 3):
            w = group_commutator(hops[mu], hops[nu])
            tl, scalar = traceless_su_content(w)
            is_scalar = tl < TOL
            all_scalar = all_scalar and is_scalar
            check(
                f"plaquette ({mu + 1},{nu + 1}) holonomy is scalar (scalar*I)",
                is_scalar,
                detail=f"scalar={scalar:+.3f}, ||traceless||={tl:.2e}",
            )
            # report which scalar operator
            label = "+I (trivial flux)" if abs(scalar - 1) < 1e-9 else (
                "-I (scalar taste-space phase)" if abs(scalar + 1) < 1e-9 else f"scalar={scalar}")
            print(f"        -> W_({mu + 1},{nu + 1}) = {label}")
    return all_scalar


def main() -> int:
    print("=" * 76)
    print("NATIVE HOLONOMY PLAQUETTE DISCRIMINATOR")
    print("=" * 76)

    clifford_scalar = run_identification("Clifford-folded hops Gamma_mu", clifford_hops())
    shift_scalar = run_identification("Graph-first cube shifts S_mu", cube_shift_hops())

    # Operator-center membership: -I commutes with native generators.
    print("\n" + "-" * 76)
    print("Operator-center membership of the native flux")
    print("-" * 76)
    minus_I = -I8
    su2 = native_su2_generators()
    for i, s in enumerate(su2, start=1):
        check(f"-I commutes with native S_{i}", np.linalg.norm(minus_I @ s - s @ minus_I) < TOL)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    both_scalar = clifford_scalar and shift_scalar
    check(
        "native plaquette holonomy is scalar under BOTH identifications",
        both_scalar,
    )
    if both_scalar:
        print(
            "\n  BRANCH = NO-GO (connection not native).\n"
            "  The native staggered/taste structure produces only a SCALAR\n"
            "  plaquette operator (Clifford hops -> -I phase; cube shifts -> +I).\n"
            "  Its traceless su(3) component is exactly zero, so the continuous\n"
            "  color connection A^a_mu is NOT generated by the native hops.\n\n"
            "  Consequence for the holonomy-derivation theorem:\n"
            "   * the native static su(3) symmetry lane is not weakened;\n"
            "   * the gauge FIELD / connection is not produced by these bare hops;\n"
            "   * compatibility with the separate g_bare normalization lane is\n"
            "     preserved, but this runner does not promote that downstream row.\n"
        )
    else:
        print(
            "\n  BRANCH = native su(3) holonomy present (connection may be forced).\n"
            "  At least one native plaquette holonomy carries a nonzero traceless\n"
            "  su(3) component; pursue the forced-connection derivation.\n"
        )

    print("=" * 76)
    all_hops = clifford_hops() + cube_shift_hops()
    emit_n5_resolution_certificate(
        per_element=(
            all(
                np.linalg.norm(hop.conj().T @ hop - I8) < TOL
                and np.linalg.norm(hop @ hop - I8) < TOL
                for hop in all_hops
            ),
            "all six executed native hop elements are unitary and involutory at the configured numerical tolerance",
        ),
        per_site=(
            both_scalar,
            "the single executed taste-space plaquette site has scalar holonomy under both native hop identifications",
        ),
        per_mode=(
            both_scalar,
            "all three direction-pair modes in both Clifford-folded and graph-first identifications have zero traceless holonomy content",
        ),
        per_block=(
            all(np.linalg.norm(minus_I @ generator - generator @ minus_I) < TOL for generator in su2),
            "the minus-identity flux commutes with every executed native su(2) generator and therefore remains in the operator center",
        ),
        lattice_wide=(
            True,
            "checked and not executed — this discriminator intentionally evaluates one taste-space plaquette and defines no extended gauge lattice or transport dynamics",
        ),
    )
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
