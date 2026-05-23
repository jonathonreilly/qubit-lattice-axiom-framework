#!/usr/bin/env python3
"""Native-holonomy plaquette discriminator.

Question (well-posed, decidable on a single Z^3 plaquette):

  The retained `native_gauge_closure` surface gives su(3) as a *static
  symmetry* of the 8-dim taste space V = C^2 (x) C^2 (x) C^2. The holonomy
  form U = exp(i a A^a T_a) needs a *gauged connection* living on edges. Does
  the native staggered structure FORCE a nontrivial (traceless) su(3)
  parallel transport around a plaquette, or is the native flux purely
  center-valued (so the continuous su(3) connection A^a is added structure,
  not native)?

Method. Build the native taste-space "hop in direction mu" operator under the
two natural identifications the framework actually supplies:

  (1) Clifford generators Gamma_mu  (staggered-phase folded hop), and
  (2) cube one-step axis shifts S_mu (graph-first su(3) construction).

For each, form the lattice plaquette holonomy (group commutator)
  W_{mu,nu} = L_mu L_nu L_mu^{-1} L_nu^{-1},
and measure its traceless su(3)-sector content vs its center (scalar) content.

Verdict:
  - if every native W is proportional to the identity -> center-valued flux,
    NO native traceless su(3) connection  -> connection is ADDED structure
    (the gauge field enters by the standard minimal-coupling principle);
  - else -> a native continuous su(3) holonomy is forced.

This script asserts no audit status. It is a branch discriminator for the
holonomy-derivation theorem scope.
"""

from __future__ import annotations

import numpy as np

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

    all_center = True
    for mu in range(3):
        for nu in range(mu + 1, 3):
            w = group_commutator(hops[mu], hops[nu])
            tl, scalar = traceless_su_content(w)
            is_center = tl < TOL
            all_center = all_center and is_center
            check(
                f"plaquette ({mu + 1},{nu + 1}) holonomy is center-valued (scalar*I)",
                is_center,
                detail=f"scalar={scalar:+.3f}, ||traceless||={tl:.2e}",
            )
            # report which center element
            label = "+I (trivial flux)" if abs(scalar - 1) < 1e-9 else (
                "-I (Z2 center flux)" if abs(scalar + 1) < 1e-9 else f"scalar={scalar}")
            print(f"        -> W_({mu + 1},{nu + 1}) = {label}")
    return all_center


def main() -> int:
    print("=" * 76)
    print("NATIVE HOLONOMY PLAQUETTE DISCRIMINATOR")
    print("=" * 76)

    clifford_center = run_identification("Clifford-folded hops Gamma_mu", clifford_hops())
    shift_center = run_identification("Graph-first cube shifts S_mu", cube_shift_hops())

    # Center membership: -I commutes with the native su(2) (and any embedded su(3)).
    print("\n" + "-" * 76)
    print("Center membership of the native flux")
    print("-" * 76)
    minus_I = -I8
    su2 = native_su2_generators()
    for i, s in enumerate(su2, start=1):
        check(f"-I commutes with native S_{i}", np.linalg.norm(minus_I @ s - s @ minus_I) < TOL)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    both_center = clifford_center and shift_center
    check(
        "native plaquette holonomy is center-valued under BOTH identifications",
        both_center,
    )
    if both_center:
        print(
            "\n  BRANCH = NO-GO (connection not native).\n"
            "  The native staggered/taste structure produces only a CENTER-valued\n"
            "  plaquette flux (Clifford hops -> -I Z2 flux; cube shifts -> +I).\n"
            "  Its traceless su(3) component is exactly zero, so the continuous\n"
            "  color connection A^a_mu is NOT generated by the native hops.\n\n"
            "  Consequence for the holonomy-derivation theorem:\n"
            "   * the gauge GROUP su(3) is native (retained, as a symmetry);\n"
            "   * the gauge FIELD / connection enters by the standard minimal-\n"
            "     coupling principle, i.e. it is ADDED structure, not derived;\n"
            "   * this does NOT threaten g_bare = 1: that is the canonical\n"
            "     normalization of the generators T_a (g_bare_rigidity), which\n"
            "     is independent of whether the field A is native. Once the\n"
            "     connection is added in the canonical basis, no extra\n"
            "     multiplicative coupling appears -> g_bare = 1 still holds.\n"
        )
    else:
        print(
            "\n  BRANCH = native su(3) holonomy present (connection may be forced).\n"
            "  At least one native plaquette holonomy carries a nonzero traceless\n"
            "  su(3) component; pursue the forced-connection derivation.\n"
        )

    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
