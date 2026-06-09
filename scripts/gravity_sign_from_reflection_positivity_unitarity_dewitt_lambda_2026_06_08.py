"""Bounded RP/unitarity gate for the gravity-sign route map.

The runner checks finite linear algebra only:
  * a reflection-positive reconstructed Gram matrix has no negative-norm
    physical state, while an indefinite Gram has a ghost direction;
  * the DeWitt lambda-one control has the TT/trace sign split, while lambda=0
    and lambda=1/d do not;
  * the source note keeps the result conditional and does not claim RP alone
    derives G>0.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

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


def trace_weight(lambda_value: float, d: int = 3) -> float:
    """Unnormalized trace-channel weight for G_lambda."""
    return 1.0 - lambda_value * d


def main() -> int:
    print("GRAVITY SIGN: bounded reflection-positive unitarity gate")
    print("=" * 78)

    rng = np.random.default_rng(0)
    matrix = rng.standard_normal((8, 8)) + 1j * rng.standard_normal((8, 8))
    rp_gram = matrix.conj().T @ matrix
    rp_eigs = np.linalg.eigvalsh(rp_gram)
    indefinite_gram = np.diag([1.0, 1.0, -1.0])
    indefinite_eigs = np.linalg.eigvalsh(indefinite_gram)

    check(
        "H1 RP Gram is positive semidefinite; indefinite Gram has a ghost direction",
        np.min(rp_eigs) >= -1e-9 and np.min(indefinite_eigs) < 0,
        f"min RP eigenvalue={np.min(rp_eigs):.3e}; indefinite eigenvalues={indefinite_eigs.tolist()}",
    )

    d = 3
    tt_weight = 1.0
    trace_lambda_one = trace_weight(1.0, d)
    trace_lambda_zero = trace_weight(0.0, d)
    trace_lambda_degenerate = trace_weight(1.0 / d, d)

    check(
        "H2 DeWitt lambda-one has TT/trace split; lambda=0 and lambda=1/d do not",
        tt_weight > 0
        and trace_lambda_one < 0
        and trace_lambda_zero > 0
        and abs(trace_lambda_degenerate) < 1e-12,
        f"TT={tt_weight:+.0f}; trace(lambda=1)={trace_lambda_one:+.0f}; "
        f"trace(lambda=0)={trace_lambda_zero:+.0f}; trace(lambda=1/d)={trace_lambda_degenerate:+.0e}",
    )

    note = Path(
        "docs/GRAVITY_SIGN_FROM_REFLECTION_POSITIVITY_UNITARITY_REDUCES_TO_EMERGENT_DIFFEOMORPHISM_NARROW_THEOREM_NOTE_2026-06-08.md"
    ).read_text(encoding="utf-8")
    guardrails = [
        "conditional gate, not a derivation of `G>0` from reflection positivity alone",
        "The existing universal-GR blocker remains load-bearing",
        "No global no-go is shipped.",
        "Physical RP embedding of TT modes",
        "no new primitive, axiom, Tier-A admission",
    ]
    check(
        "H3 source note keeps RP/unitarity route conditional",
        all(item in note for item in guardrails),
        "guardrails present for RP-alone boundary, supermetric blocker, no-go scope, and primitive scope",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: PASS for the bounded RP/unitarity gate only. RP forbids physical\n"
        "negative-norm ghosts after reconstruction, and the lambda-one DeWitt control\n"
        "has the TT/trace sign split. G>0 is not derived from RP alone; the open work is\n"
        "to derive physical RP TT modes, conformal gauge removal, and source/action\n"
        "orientation in the framework."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
