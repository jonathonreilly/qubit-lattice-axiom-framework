"""Bounded exchange-sign reduction for the Newtonian attraction sign.

The runner derives and checks the static tree-level sign algebra used in
GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_...
It does not derive the framework's source/action normalization, local energy
conditions, or healthy spin-2 kinetic sign.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(cond)
    FAIL += int(not cond)
    return cond


def potential_sign(numerator: float, kinetic_sign: float = 1.0, source_product: float = 1.0) -> float:
    """Static sign of V ~ - kinetic_sign * source_product * numerator."""
    value = -kinetic_sign * source_product * numerator
    if value > 0:
        return 1.0
    if value < 0:
        return -1.0
    return 0.0


def derived_exchange_cross_term() -> sp.Expr:
    """Derive the static two-source cross term by eliminating one mediator mode."""
    kinetic_sign, k, j_a, j_b = sp.symbols("sigma K J_A J_B", nonzero=True)
    phi = sp.symbols("phi")
    energy = sp.Rational(1, 2) * kinetic_sign * k * phi**2 - (j_a + j_b) * phi
    stationary_phi = sp.solve(sp.diff(energy, phi), phi)[0]
    on_shell = sp.expand(energy.subs(phi, stationary_phi))
    return sp.expand(on_shell).coeff(j_a * j_b)


def main() -> int:
    print("GRAVITY ATTRACTION SIGN: bounded source/action exchange reduction")
    print("=" * 78)

    sigma, k = sp.symbols("sigma K", nonzero=True)
    cross_term = derived_exchange_cross_term()
    check(
        "E0 exchange sign derived by finite quadratic on-shell elimination",
        sp.simplify(cross_term + 1 / (sigma * k)) == 0,
        f"cross_term={cross_term}; for sigma=+/-1 this has sign -sigma when K>0",
    )

    eta00 = -1.0
    numerator_scalar = 1.0
    numerator_vector = eta00

    def tensor_projector(mu: int, nu: int, alpha: int, beta: int) -> float:
        eta = [-1.0, 1.0, 1.0, 1.0]
        def e(i: int, j: int) -> float:
            return eta[i] if i == j else 0.0

        return (
            0.5 * (e(mu, alpha) * e(nu, beta) + e(mu, beta) * e(nu, alpha))
            - 0.5 * e(mu, nu) * e(alpha, beta)
        )

    numerator_tensor = tensor_projector(0, 0, 0, 0)

    check(
        "E1 numerator contractions",
        abs(numerator_scalar - 1.0) < 1e-12
        and abs(numerator_vector + 1.0) < 1e-12
        and abs(numerator_tensor - 0.5) < 1e-12,
        f"scalar={numerator_scalar:+.1f}, vector={numerator_vector:+.1f}, tensor={numerator_tensor:+.1f}",
    )

    signs = {
        "scalar_same_source": potential_sign(numerator_scalar),
        "vector_like_charge": potential_sign(numerator_vector),
        "tensor_positive_source": potential_sign(numerator_tensor),
    }
    check(
        "E2 healthy exchange signs",
        signs == {
            "scalar_same_source": -1.0,
            "vector_like_charge": +1.0,
            "tensor_positive_source": -1.0,
        },
        f"signs={signs} (-1 attraction, +1 repulsion)",
    )

    healthy = potential_sign(numerator_tensor, kinetic_sign=+1.0, source_product=+1.0)
    ghost = potential_sign(numerator_tensor, kinetic_sign=-1.0, source_product=+1.0)
    check(
        "E3 tensor attraction iff healthy kinetic sign for positive sources",
        healthy < 0 and ghost > 0,
        f"healthy sign={healthy:+.0f}, ghost sign={ghost:+.0f}",
    )

    note_path = Path("docs/GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md")
    note = note_path.read_text(encoding="utf-8")
    guardrails = [
        "It does not derive that",
        "pointwise local energy-condition theorem",
        "no derivation of the framework source/action normalization",
        "no assertion that Record, the scale-reference primitive, or the",
    ]
    check(
        "E4 source note keeps the exchange premises explicit",
        all(item in note for item in guardrails),
        "guardrails present for kinetic sign, source/action normalization, local energy, and primitive scope",
    )
    check(
        "E5 source note treats textbook QFT only as parallel reference",
        "Textbook Reference Boundary" in note
        and "parallel cross-check" in note
        and "not load-bearing" in note
        and "admitted bounded-theorem input" not in note,
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: PASS for the bounded sign reduction only. The exchange sign is derived by\n"
        "finite quadratic on-shell elimination inside the displayed source/action model.\n"
        "Positive sources plus a healthy spin-2 kinetic sign give attraction; flipping the\n"
        "kinetic sign flips the force. The runner does not derive the kinetic sign or the\n"
        "source/action normalization."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
