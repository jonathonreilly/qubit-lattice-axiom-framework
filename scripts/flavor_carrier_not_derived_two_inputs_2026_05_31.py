#!/usr/bin/env python3
"""Bounded source repair for the flavor carrier derivation route.

This runner verifies the finite content that survives audit pressure:

  A. The bare C_3 singlet/doublet/triplet characters are 1, -1, and 0.
     None equals 2/9.
  B. The value 2/9 is produced by the two-eigenvalue determinant-denominator
     sum L_3(1,2), not by a one-factor shorthand and not by a bare character.
  C. C_3-equivariant Hermitian operators have the circulant form
     H=aI+bC+conj(b)C^2, but the ratio r=|b|^2/a^2 remains free.
  D. Q(r)=1/3+(2/3)r evaluates to 2/3 at r=1/2 and 1 at r=1; this arithmetic
     does not choose the physical section.
  E. The paired note states the bounded-support status and forbids the earlier
     input-count overclaim.

The verdict is route-pruning only: the bare-character shortcut cannot derive
the physical carrier or basepoint. No new axiom is introduced.
"""

from pathlib import Path

import numpy as np


W = np.exp(2j * np.pi / 3)
I3 = np.eye(3, dtype=complex)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]], dtype=complex)
NOTE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md"
)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def note_text():
    return NOTE_PATH.read_text(encoding="utf-8")


def q_of_r(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def main():
    passed = []

    # A. Bare character route fails.
    char_singlet = 1.0
    char_doublet = W + W**2
    char_triplet = 1 + W + W**2
    passed.append(
        check(
            "A1 bare C_3 characters are singlet=1, doublet=-1, triplet=0; none equals 2/9",
            abs(char_singlet - 1.0) < 1e-12
            and abs(char_doublet + 1.0) < 1e-12
            and abs(char_triplet) < 1e-12
            and all(
                abs(x - 2.0 / 9.0) > 1e-2
                for x in (char_singlet, char_doublet.real, char_triplet.real)
            ),
            f"characters=({char_singlet:.1f}, {char_doublet.real:.1f}, {char_triplet.real:.1f})",
        )
    )

    # B. The determinant-denominator route gives the value.
    det_inv_terms = {
        k: 1 / ((W**k - 1) * (W ** (2 * k) - 1))
        for k in (1, 2)
    }
    one_factor_terms = {k: 1 / (W**k - 1) for k in (1, 2)}
    l_3_12 = sum(det_inv_terms.values()) / 3
    passed.append(
        check(
            "B1 determinant inverse uses both doublet eigenvalues; each term is 1/3",
            all(abs(det_inv_terms[k] - 1.0 / 3.0) < 1e-12 for k in (1, 2))
            and all(abs(one_factor_terms[k] - det_inv_terms[k]) > 0.1 for k in (1, 2)),
            "det_inv_terms="
            + str([round(float(det_inv_terms[k].real), 6) for k in (1, 2)])
            + "; one_factor_terms="
            + str(
                [
                    complex(round(one_factor_terms[k].real, 6), round(one_factor_terms[k].imag, 6))
                    for k in (1, 2)
                ]
            ),
        )
    )
    passed.append(
        check(
            "B2 L_3(1,2)=2/9 comes from determinant denominators, not a bare character",
            abs(l_3_12 - 2.0 / 9.0) < 1e-12 and abs(l_3_12 - char_doublet) > 0.1,
            f"L_3(1,2)={l_3_12.real:.6f}; doublet_character={char_doublet.real:.1f}",
        )
    )

    # C. Equivariant form leaves r free.
    r_targets = [0.01, 0.5, 1.0, 4.0, 9.0]
    commutators = []
    recovered = []
    for r in r_targets:
        a = 2.0
        b = a * np.sqrt(r) * (0.6 + 0.8j)
        h = a * I3 + b * C + np.conj(b) * C.conj().T
        commutators.append(np.linalg.norm(h @ C - C @ h))
        recovered.append(abs(b) ** 2 / a**2)
    passed.append(
        check(
            "C1 C_3-equivariant circulant operators commute with C across freely chosen r values",
            max(commutators) < 1e-12
            and all(abs(a - b) < 1e-12 for a, b in zip(r_targets, recovered)),
            f"r_values={r_targets}; max_commutator={max(commutators):.2e}",
        )
    )

    # D. The arithmetic checks candidates but does not choose one.
    passed.append(
        check(
            "D1 Q(r)=1/3+(2/3)r verifies both r=1/2 -> 2/3 and r=1 -> 1",
            abs(q_of_r(0.5) - 2.0 / 3.0) < 1e-12
            and abs(q_of_r(1.0) - 1.0) < 1e-12,
            f"Q(1/2)={q_of_r(0.5):.6f}; Q(1)={q_of_r(1.0):.6f}",
        )
    )

    # E. Source-boundary firewall.
    text = note_text()
    required_phrases = [
        "Actual current surface status:** bounded-support",
        "Trace class:** negative_route_pruning",
        "does **not** derive the physical carrier",
        "does **not** select the basepoint",
        "not proved: a theorem that there are exactly two independent irreducible inputs",
        "No new axiom is introduced.",
    ]
    forbidden_phrases = [
        "TWO independent irreducible flavor inputs remain",
        "Verdict: carrier NOT derived; basepoint irreducible",
        "retained_no_go",
        "open_gate",
        "retained theorems bracket",
    ]
    passed.append(
        check(
            "E1 note keeps bounded-support route-pruning status and required non-closure disclaimers",
            all(phrase in text for phrase in required_phrases),
            "required phrases present",
        )
    )
    passed.append(
        check(
            "E2 note removes old input-count/status overclaim phrases",
            not any(phrase in text for phrase in forbidden_phrases),
            "forbidden phrases absent",
        )
    )
    passed.append(
        check(
            "E3 audit surfaces are not retagged by this source repair",
            "does not retag the audit ledger" in text
            and "does not promote this note or change the audited claim scope" in text,
            "audit retagging left to audit/review lanes",
        )
    )

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("VERDICT: bounded-support negative route pruning.")
    print("The bare-character shortcut fails: C_3 characters are 1, -1, and 0, while")
    print("L_3(1,2)=2/9 comes from the two-eigenvalue determinant denominator.")
    print("Equivariance leaves r free, and Q(r) checks both r=1/2 and r=1 without")
    print("selecting the physical basepoint. The source does not derive the physical")
    print("carrier, does not select the basepoint, and introduces no new axiom.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
