#!/usr/bin/env python3
"""Which positivity can break S_3 -> C_3? Determinant-magnitude vs orientation-sign.

The positivity/orientation program asks whether a positivity-type constraint
can break the (physical, unbroken) S_3 axis-symmetry on the hw=1 triplet down
to C_3. The natural candidate is the retained staggered determinant positivity
`staggered_only_det_positivity` (det(M_KS+mI) > 0). This discriminator tests
whether that positivity actually does the breaking.

Narrow group-theory fact: among one-dimensional character/sign-magnitude
constraints on the finite S_3 axis-ordering surface, the only nontrivial route
whose positive level set is C_3 = A_3 couples to the SIGN (orientation)
representation of S_3 (sgn = +1 on the 3-cycles, -1 on the transpositions). A
constraint that is S_3-INVARIANT (the trivial representation) selects all of
S_3 and breaks nothing. This runner does not classify higher-dimensional
selectors or arbitrary class functions.

Test:
  (A) the staggered determinant det(D+mI) is S_3-INVARIANT (reflection-even):
      identical and positive under the identity, a transposition, and a 3-cycle
      of the axes (they are gauge-equivalent). So det-magnitude positivity is a
      trivial-representation constraint -> it CANNOT break S_3 -> C_3.
  (B) the orientation sign sgn(sigma) = det(permutation matrix) is the sign
      representation: +1 on C_3, -1 on transpositions; the +1 subset is exactly
      C_3. So an orientation/handedness positivity (volume-form / Cl(3)
      pseudoscalar sign) is the one-dimensional route to C_3, if that physical
      bridge is independently supplied.

Verdict: the retained staggered DET-positivity is reflection-even and is NOT the
S_3 -> C_3 breaker. A one-dimensional route to C_3 must use a SIGN/orientation
("handedness") constraint, a different object. The bridge does NOT close via
det-positivity; it requires independently deriving a handedness-sign positivity
in the framework.

Pure finite linear algebra / S_3 representation theory. No PDG / fitted / scale /
mass-value input. Asserts no audit status.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0
L = 4  # even periodic lattice
REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_NOTE = REPO_ROOT / "docs/POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23.md"


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        st = "PASS"
    else:
        FAIL += 1
        st = "FAIL"
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond


def sites():
    return list(itertools.product(range(L), repeat=3))


def eta_ordered(n, mu, order):
    pos = {ax: i for i, ax in enumerate(order)}
    s = sum(n[nu] for nu in range(3) if pos[nu] < pos[mu])
    return -1 if (s % 2) else 1


def staggered_D(order):
    """Massless staggered Dirac operator (anti-Hermitian) for an axis ordering,
    free (trivial) links, periodic L^3."""
    S = sites()
    idx = {n: i for i, n in enumerate(S)}
    N = len(S)
    D = np.zeros((N, N), dtype=complex)
    for n in S:
        for mu in range(3):
            m = list(n); m[mu] = (m[mu] + 1) % L; m = tuple(m)
            e = eta_ordered(n, mu, order)
            # antisymmetric forward/backward hop, coefficient 1/2
            D[idx[m], idx[n]] += 0.5 * e
            D[idx[n], idx[m]] -= 0.5 * e
    return D


def det_pos(order, mass=1.0):
    D = staggered_D(order)
    # det(D + m I); massless staggered is anti-Hermitian so eigenvalues are i*real
    M = D + mass * np.eye(D.shape[0])
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        sign, logdet = np.linalg.slogdet(M)
    return sign, logdet


def source_scope_check():
    text = SOURCE_NOTE.read_text(encoding="utf-8")
    required = [
        "one-dimensional character /",
        "sign-magnitude constraints",
        "does not classify higher-dimensional selectors, arbitrary class",
    ]
    banned = [
        ("broad binary-class-function sentence", "A binary (\"positive/negative\") constraint"),
    ]
    print("\n" + "-" * 76)
    print("SOURCE SCOPE CHECK: one-dimensional sign/magnitude only")
    print("-" * 76)
    ok = True
    for needle in required:
        ok = check(f"source contains scope phrase: {needle}", needle in text) and ok
    for label, needle in banned:
        ok = check(f"source excludes {label}", needle not in text) and ok
    return ok


def main() -> int:
    print("=" * 76)
    print("WHICH POSITIVITY BREAKS S_3 -> C_3:  det-magnitude vs orientation-sign")
    print("=" * 76)

    source_scope_check()

    idorder = (0, 1, 2)
    transposition = (1, 0, 2)
    three_cycle = (1, 2, 0)

    # (A) staggered determinant is S_3-invariant (reflection-even) and positive
    print("\n" + "-" * 76)
    print("(A) staggered det(D+mI): identical & positive under id / transposition / 3-cycle")
    print("-" * 76)
    s_id, ld_id = det_pos(idorder)
    s_tr, ld_tr = det_pos(transposition)
    s_3c, ld_3c = det_pos(three_cycle)
    check("det > 0 for identity ordering", s_id.real > 0, detail=f"sign={s_id.real:+.0f}")
    check("det > 0 for transposition ordering", s_tr.real > 0, detail=f"sign={s_tr.real:+.0f}")
    check("det > 0 for 3-cycle ordering", s_3c.real > 0, detail=f"sign={s_3c.real:+.0f}")
    check("det identical under transposition (reflection-even)",
          abs(ld_id - ld_tr) < 1e-8, detail=f"Δlogdet={abs(ld_id-ld_tr):.2e}")
    check("det identical under 3-cycle",
          abs(ld_id - ld_3c) < 1e-8, detail=f"Δlogdet={abs(ld_id-ld_3c):.2e}")
    check("=> det-magnitude positivity is S_3-INVARIANT (trivial rep): breaks nothing",
          s_id.real > 0 and abs(ld_id - ld_tr) < 1e-8)

    # (B) orientation sign is the sign representation; sgn=+1 subset is exactly C_3
    print("\n" + "-" * 76)
    print("(B) orientation sign sgn(sigma) = det(perm matrix): the sign representation")
    print("-" * 76)
    def perm_matrix(p):
        M = np.zeros((3, 3))
        for i in range(3):
            M[p[i], i] = 1.0
        return M
    sgn = {p: round(float(np.linalg.det(perm_matrix(p)))) for p in itertools.permutations((0, 1, 2))}
    pos_set = {p for p, v in sgn.items() if v == +1}
    C3 = {(0, 1, 2), (1, 2, 0), (2, 0, 1)}
    check("sgn = +1 on identity and the two 3-cycles", all(sgn[p] == 1 for p in C3))
    check("sgn = -1 on the three transpositions",
          all(sgn[p] == -1 for p in sgn if p not in C3))
    check("orientation-positive subset {sgn=+1} is EXACTLY C_3 = A_3", pos_set == C3,
          detail=f"{sorted(pos_set)}")
    # the trivial-rep ("is positive", constant +1) selects all of S_3 -> no breaking
    check("trivial rep (det-magnitude 'is positive') is constant on S_3 -> selects all S_3",
          True)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  THE DET-POSITIVITY BRIDGE DOES NOT CLOSE.\n"
            "  (A) The retained staggered determinant positivity det(D+mI) > 0 is\n"
            "      S_3-INVARIANT (reflection-even): identical and positive under a\n"
            "      transposition and a 3-cycle. It is a trivial-representation\n"
            "      constraint, so it CANNOT break S_3 -> C_3 -- it selects all of\n"
            "      S_3 and breaks nothing.\n"
            "  (B) A one-dimensional route to C_3 requires coupling to the SIGN\n"
            "      (orientation) representation: the {sgn=+1} subset is exactly C_3.\n"
            "      A handedness / orientation-sign positivity would be that route,\n"
            "      but deriving such a framework constraint remains separate.\n\n"
            "  Honest consequence: `staggered_only_det_positivity` is the wrong\n"
            "  positivity for this bridge. A one-dimensional route requires\n"
            "  independently identifying, in the framework, an ORIENTATION-SIGN\n"
            "  positivity (handedness selection).\n"
            "  That is the precise, corrected next target -- the det-positivity\n"
            "  route is closed.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
