#!/usr/bin/env python3
"""J:attack-f:PR8152 — pattern (f) NORMALIZATION.

The note has no Fourier/L/N/2π-sum conventions. It does claim the Gram frame
    F(q1, q2) = (q1, (q2 − (q1·q2) q1)/|·|, q1 × q2)
is a rotation matrix. The second column is unit-normalized; the third is the
raw cross product. At a non-orthogonal pair, |q1 × q2| = sqrt(1 − (q1·q2)^2)
is not 1, so F is not in SO(3).

Recompute at the runner's own rational pair q1=(1,0,0), q2=(3/5,4/5,0)
(dot 3/5) and at an orthogonal control. HIT if the written third column
fails to be unit while F is claimed to be a rotation matrix.
"""
from __future__ import annotations

from fractions import Fraction as Fr

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def note_F(q1, q2):
    """Literal formula of the Premises: third column = q1 × q2, unnormalized."""
    e1 = q1
    u = q2 - (q1.dot(q2)) * q1
    e2 = u / sp.sqrt(u.dot(u))
    e3 = q1.cross(q2)
    return sp.Matrix.hstack(e1, e2, e3)


def runner_F(q1, q2):
    """What B2 actually builds: third column = e1 × e2 with e2 already unit."""
    e1 = q1
    u = q2 - (q1.dot(q2)) * q1
    e2 = u / sp.sqrt(u.dot(u))
    return sp.Matrix.hstack(e1, e2, e1.cross(e2))


def so3_report(name, F):
    gram = sp.simplify(F.T * F)
    det = sp.simplify(F.det())
    cols = [sp.simplify(F[:, j].dot(F[:, j])) for j in range(3)]
    print(f"{name}: col-norms^2={cols} det={det} F^T F=\n{gram}")
    return gram, det, cols


def main() -> int:
    q1 = sp.Matrix([1, 0, 0])
    q2 = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5), 0])
    print(f"executed pair: q1={tuple(q1)} q2={tuple(q2)} q1·q2={sp.simplify(q1.dot(q2))}")
    print(f"|q1×q2|^2 = {sp.simplify(q1.cross(q2).dot(q1.cross(q2)))} stated unit iff 1")

    Fn = note_F(q1, q2)
    Frun = runner_F(q1, q2)
    gram_n, det_n, cols_n = so3_report("note F (q1×q2)", Fn)
    gram_r, det_r, cols_r = so3_report("runner F (e1×e2)", Frun)

    if cols_n[2] != 1:
        hit(
            f"note's third column q1×q2 has |·|^2={cols_n[2]} != 1 at the "
            f"executed pair q1·q2=3/5; det F={det_n} != 1, so F is not a rotation matrix"
        )
    if gram_n != sp.eye(3):
        if not any("not a rotation" in h for h in HITS):
            hit(f"note F^T F != I at the executed pair: {gram_n}")
    if gram_r != sp.eye(3) or det_r != 1:
        hit(f"runner F is not SO(3) either: det={det_r}")

    # orthogonal control: note formula and runner formula agree and are SO(3)
    q2o = sp.Matrix([0, 1, 0])
    Fo_n = note_F(q1, q2o)
    Fo_r = runner_F(q1, q2o)
    print(f"orthogonal control q2=(0,1,0): note==runner {sp.simplify(Fo_n-Fo_r)==sp.zeros(3,3)}")
    gram_o, det_o, cols_o = so3_report("note F at orthogonal pair", Fo_n)
    if gram_o != sp.eye(3) or det_o != 1:
        hit(f"note F fails SO(3) even at an orthogonal pair: det={det_o}")

    # extra non-orthogonal pair (3/5,0,4/5)
    q2b = sp.Matrix([sp.Rational(3, 5), 0, sp.Rational(4, 5)])
    Fb = note_F(q1, q2b)
    _, det_b, cols_b = so3_report("note F at (1,0,0)×(3/5,0,4/5)", Fb)
    if cols_b[2] != 1:
        print(f"INFO: extra pair also has |q1×q2|^2={cols_b[2]} det={det_b}")

    # Born 1/2 (the other explicit 1/2 in the note) does recompute
    def born(s, q):
        return (1 + s.dot(q)) / 2

    q = sp.Matrix([0, 0, 1])
    b_plus, b_minus = born(q, q), born(-q, q)
    print(f"M5 Born (1+s·q)/2: at q -> {b_plus}, at -q -> {b_minus}")
    if b_plus != 1 or b_minus != 0:
        hit(f"Born 1/2 failed: {(b_plus, b_minus)}")
    if (1 + q.dot(q)) != 2:
        hit("control: 1+s·q without /2 is 2, not a probability")

    if HITS:
        print(
            "SUMMARY: attack pattern (f) NORMALIZATION - the written frame "
            "F=(q1, Gram-Schmidt(q2), q1×q2) is claimed to be a rotation matrix "
            "but at the executed pair q1=(1,0,0), q2=(3/5,4/5,0) the unnormalized "
            "third column has length 4/5 and det F=4/5; the runner's B2 passes "
            "only because it crosses the already-normalized second column "
            f"({'; '.join(HITS)})"
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - no Fourier/L/N/2π "
        "sum conventions; the written frame is SO(3) at the executed pair and "
        "Born (1+s·q)/2 is {0,1} on the antipodal menu"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
