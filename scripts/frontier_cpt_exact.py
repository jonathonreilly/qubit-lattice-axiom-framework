#!/usr/bin/env python3
"""Verify the finite-lattice Hermitian-lift antiunitary identities.

The real staggered hopping operator is ``D`` and the Hermitian Hamiltonian is
``H = iD``.  The runner keeps their antiunitary actions separate:

* on ``D``, bare complex conjugation fixes ``D`` and ``CPK`` fixes ``D``;
* on ``H``, bare ``K`` and ``CPK`` flip the sign;
* with ``T_H = CK``, the composite ``CP T_H = PK = Theta_H`` preserves H.

Only the free even-periodic finite-lattice algebra and the resulting
Theta_H-odd H-sector zero are tested.  ``C`` is the sublattice-sign matrix and
``P`` is inversion; the symbols do not assert physical C/P/T/CPT
identifications.  No SME operator-basis identification, interacting extension,
or continuum CPT theorem is claimed.
"""

from __future__ import annotations

import sys

import numpy as np


PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    """Record and print one independently evaluated assertion."""
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def staggered_eta(mu: int, site: tuple[int, int, int]) -> int:
    """Kogut-Susskind phase eta_mu(x)."""
    return (-1) ** sum(site[nu] for nu in range(mu))


def _site_to_idx(site: tuple[int, int, int], L: int) -> int:
    x, y, z = site
    return ((x % L) * L + (y % L)) * L + (z % L)


def _idx_to_site(idx: int, L: int) -> tuple[int, int, int]:
    z = idx % L
    y = (idx // L) % L
    x = idx // (L * L)
    return x, y, z


def build_direction_D(L: int, mu: int) -> np.ndarray:
    """Build the direction-mu real anti-Hermitian hopping operator D_mu."""
    if L % 2:
        raise ValueError("even L required for bipartite periodic Z^3")
    if mu not in (0, 1, 2):
        raise ValueError("mu must be 0, 1, or 2")
    n = L**3
    D_mu = np.zeros((n, n), dtype=np.complex128)
    for row in range(n):
        site = _idx_to_site(row, L)
        eta = staggered_eta(mu, site)
        forward = list(site)
        backward = list(site)
        forward[mu] = (forward[mu] + 1) % L
        backward[mu] = (backward[mu] - 1) % L
        D_mu[row, _site_to_idx(tuple(forward), L)] += 0.5 * eta
        D_mu[row, _site_to_idx(tuple(backward), L)] -= 0.5 * eta
    return D_mu


def build_D(L: int) -> np.ndarray:
    """Build D=sum_mu D_mu; D is the real anti-Hermitian hopping matrix."""
    return sum((build_direction_D(L, mu) for mu in range(3)))


def build_full_hamiltonian(L: int) -> np.ndarray:
    """Compatibility name: return the Hermitian lift H=iD."""
    return 1j * build_D(L)


def build_sublattice_sign(L: int) -> np.ndarray:
    """Real unitary C=diag((-1)^(x_1+x_2+x_3))."""
    n = L**3
    C = np.zeros((n, n), dtype=np.complex128)
    for idx in range(n):
        C[idx, idx] = (-1) ** sum(_idx_to_site(idx, L))
    return C


def build_inversion(L: int) -> np.ndarray:
    """Real unitary P implementing x -> -x mod L."""
    n = L**3
    P = np.zeros((n, n), dtype=np.complex128)
    for col in range(n):
        x, y, z = _idx_to_site(col, L)
        row = _site_to_idx((-x, -y, -z), L)
        P[row, col] = 1.0
    return P


def antiunitary_action(unitary_part: np.ndarray, op: np.ndarray) -> np.ndarray:
    """Return (U K) op (U K)^-1 = U op^* U^dagger."""
    return unitary_part @ np.conj(op) @ unitary_part.conj().T


def antiunitary_square(unitary_part: np.ndarray) -> np.ndarray:
    """Return the linear unitary part of (U K)^2, namely U U^*."""
    return unitary_part @ np.conj(unitary_part)


def exact_equal(left: np.ndarray, right: np.ndarray) -> bool:
    """Exact equality is valid here: all entries are dyadic times 1 or i."""
    return bool(np.array_equal(left, right))


def frobenius(op: np.ndarray) -> float:
    return float(np.linalg.norm(op, ord="fro"))


def verify_odd_L_rejected() -> None:
    L = 3
    try:
        build_D(L)
    except ValueError:
        rejected = True
    else:
        rejected = False
    origin = (0, 0, 0)
    wrapped_neighbor = (L - 1, 0, 0)
    same_sublattice_across_boundary = (
        (-1) ** sum(origin) == (-1) ** sum(wrapped_neighbor)
    )
    site = (1, 0, 0)
    inverted_site = tuple((-coordinate) % L for coordinate in site)
    inversion_changes_eta = staggered_eta(1, site) != staggered_eta(1, inverted_site)
    check(
        "odd periodic L rejected",
        rejected and same_sublattice_across_boundary and inversion_changes_eta,
        "odd wrapping breaks bipartite grading and inversion-phase parity",
    )


def verify_lattice(L: int) -> None:
    print()
    print(f"L={L} ({L**3} sites)")
    print("-" * 72)

    D_mu = [build_direction_D(L, mu) for mu in range(3)]
    D = build_D(L)
    H = 1j * D
    H_mu = [1j * part for part in D_mu]
    C = build_sublattice_sign(L)
    P = build_inversion(L)
    CP = C @ P
    identity = np.eye(L**3, dtype=np.complex128)
    zero = np.zeros_like(D)

    check(f"L={L} D=sum_mu D_mu", exact_equal(D, sum(D_mu)), "direct reconstruction")
    check(f"L={L} D real", exact_equal(np.conj(D), D))
    check(f"L={L} D anti-Hermitian", exact_equal(D.conj().T, -D))
    check(f"L={L} H=iD Hermitian", exact_equal(H.conj().T, H))
    check(f"L={L} H purely imaginary", exact_equal(np.conj(H), -H), "H^*=-H")

    check(
        f"L={L} C real unitary involution",
        exact_equal(np.conj(C), C)
        and exact_equal(C.conj().T @ C, identity)
        and exact_equal(C @ C, identity),
    )
    check(
        f"L={L} P real unitary involution",
        exact_equal(np.conj(P), P)
        and exact_equal(P.conj().T @ P, identity)
        and exact_equal(P @ P, identity),
    )
    check(f"L={L} [C,P]=0", exact_equal(C @ P, P @ C))
    check(f"L={L} CP unitary involution", exact_equal(CP @ CP, identity))

    check(f"L={L} C D C=-D", exact_equal(C @ D @ C, -D))
    check(f"L={L} P D P=-D", exact_equal(P @ D @ P, -D))
    check(f"L={L} K D K^-1=D", exact_equal(np.conj(D), D), "D-level identity only")
    check(f"L={L} CP D (CP)^-1=D", exact_equal(CP @ D @ CP.conj().T, D))
    check(f"L={L} CPK preserves D", exact_equal(antiunitary_action(CP, D), D), "D-level identity only")

    check(f"L={L} C H C=-H", exact_equal(C @ H @ C, -H))
    check(f"L={L} P H P=-H", exact_equal(P @ H @ P, -H))
    check(f"L={L} K H K^-1=-H", exact_equal(np.conj(H), -H), "bare K is not T_H")
    check(f"L={L} CP H (CP)^-1=H", exact_equal(CP @ H @ CP.conj().T, H))
    check(f"L={L} CPK flips H", exact_equal(antiunitary_action(CP, H), -H), "not a symmetry of H=iD")

    # T_H = C K; the composite C P T_H has unitary part CP C = P.
    T_H_unitary = C
    CP_T_H_unitary = CP @ C
    Theta_H_unitary = P
    check(f"L={L} T_H=C K preserves H", exact_equal(antiunitary_action(T_H_unitary, H), H))
    check(f"L={L} C P T_H=P K", exact_equal(CP_T_H_unitary, Theta_H_unitary), "uses [C,P]=0 and C^2=I")
    theta_H = antiunitary_action(Theta_H_unitary, H)
    check(f"L={L} Theta_H=P K preserves H", exact_equal(theta_H, H))
    check(f"L={L} C P T_H preserves H directly", exact_equal(antiunitary_action(CP_T_H_unitary, H), H))

    # Counterchecks for the complete table: C T_H = K and P T_H = PC K.
    check(f"L={L} C T_H=K flips H", exact_equal(antiunitary_action(C @ C, H), -H))
    check(f"L={L} P T_H=PC K flips H", exact_equal(antiunitary_action(P @ C, H), -H))

    antiunitaries = (
        ("K", identity),
        ("T_H=C K", C),
        ("C P K", CP),
        ("Theta_H=P K", P),
        ("C T_H=K", C @ C),
        ("P T_H=P C K", P @ C),
        ("C P T_H=P K", CP_T_H_unitary),
    )
    for label, unitary_part in antiunitaries:
        check(
            f"L={L} ({label})^2=I on states",
            exact_equal(antiunitary_square(unitary_part), identity),
        )

    H_odd = 0.5 * (H - theta_H)
    check(f"L={L} H_odd=0 under Theta_H", exact_equal(H_odd, zero), f"||H_odd||_F={frobenius(H_odd):.2e}")

    direction_odd = []
    for mu, component in enumerate(H_mu, start=1):
        transformed = antiunitary_action(Theta_H_unitary, component)
        odd = 0.5 * (component - transformed)
        direction_odd.append(odd)
        check(
            f"L={L} H_{mu},odd=0 under Theta_H",
            exact_equal(odd, zero),
            f"||H_{mu},odd||_F={frobenius(odd):.2e}; trace/N={np.trace(odd)/(L**3):.2e}",
        )
    check(f"L={L} sum_mu H_mu=H", exact_equal(sum(H_mu), H))
    check(f"L={L} sum_mu H_mu,odd=H_odd", exact_equal(sum(direction_odd), H_odd))


def main() -> int:
    print("=" * 72)
    print("FREE STAGGERED HERMITIAN-LIFT ANTIUNITARY IDENTITIES")
    print("=" * 72)
    print("D is real anti-Hermitian; H=iD is its Hermitian lift.")
    print("T_H=C K and C P T_H=Theta_H=P K are tested on H directly.")

    verify_odd_L_rejected()
    for L in (4, 6, 8):
        verify_lattice(L)

    print()
    print("=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 72)
    if FAIL_COUNT:
        print("One or more convention-consistency checks failed.")
        return 1
    print("All finite-lattice Hermitian-lift identities passed exactly.")
    print("No SME basis-completeness, interaction, or continuum claim was tested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
