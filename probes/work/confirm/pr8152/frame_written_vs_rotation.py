#!/usr/bin/env python3
"""J:confirm:J-attack-f-PR8152 -- independent test of block 18's frame definition (PR #8152).

Statement tested (note, Definitions 'Frames'): "For non-collinear unit vectors q_1, q_2, the frame
F(q_1, q_2) = (q_1, (q_2 - (q_1.q_2) q_1)/|.|, q_1 x q_2) is a rotation matrix with F(g q_1, g q_2) = g F(q_1, q_2)";
M2 then writes the covariant supports as S(q_1, q_2) = F(q_1, q_2) . S_0(q_1.q_2) with S_0 a subset of S^2.

Machinery (the finder evaluated the pair (1,0,0), (3/5,4/5,0)):
  1. symbolic: q_1 = e_1, q_2 = (cos t, sin t, 0): F^T F and det F of the WRITTEN frame as functions of t;
  2. an exact generic pair from Pythagorean quadruples, q_1 = (2/3, 2/3, 1/3), q_2 = (2/7, 3/7, 6/7) (q_1.q_2 = 16/21);
  3. the consequence for M2: the written F maps the unit vector e_3 of S_0 to a vector of length |q_1 x q_2|, off S^2;
  4. equivariance under an exact rational rotation for the written and the corrected frame (q_1, e_2, q_1 x e_2), and
     F^T F = I, det = 1 for the corrected one (the frame the runner's B2 builds).
"""
from __future__ import annotations

import sympy as sp


def frame_written(a, b):
    e2 = b - a.dot(b) * a
    e2 = e2 / sp.sqrt(e2.dot(e2))
    return sp.Matrix.hstack(a, e2, a.cross(b))


def frame_corrected(a, b):
    e2 = b - a.dot(b) * a
    e2 = e2 / sp.sqrt(e2.dot(e2))
    return sp.Matrix.hstack(a, e2, a.cross(e2))


def main():
    t = sp.Symbol("t", real=True)
    q1 = sp.Matrix([1, 0, 0])
    q2 = sp.Matrix([sp.cos(t), sp.sin(t), 0])
    Fw = frame_written(q1, q2).subs(sp.sqrt(sp.sin(t) ** 2), sp.sin(t))  # 0 < t < pi
    gram = sp.simplify(Fw.T * Fw)
    det = sp.simplify(Fw.det())
    print(f"1. q1 = e1, q2 = (cos t, sin t, 0), 0 < t < pi: written F^T F = {gram.tolist()}; det F = {det}")

    a = sp.Matrix([sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3)])
    b = sp.Matrix([sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)])
    Fw2 = frame_written(a, b)
    g2 = sp.simplify(Fw2.T * Fw2)
    d2 = sp.nsimplify(sp.simplify(Fw2.det()))
    cross2 = sp.simplify(a.cross(b).dot(a.cross(b)))
    print(f"2. q1 = (2/3,2/3,1/3), q2 = (2/7,3/7,6/7), q1.q2 = {a.dot(b)}: |q1 x q2|^2 = {cross2}; written F^T F = {g2.tolist()}; "
          f"det F = {d2} = {float(d2):.6f}")

    img = Fw2 * sp.Matrix([0, 0, 1])
    print(f"3. M2 with the written frame: e3 in S_0 maps to a vector of squared length {sp.simplify(img.dot(img))} (not on S^2)")

    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    g = sp.Matrix([[c, 0, s], [0, 1, 0], [-s, 0, c]]) * sp.Matrix([[1, 0, 0], [0, sp.Rational(5, 13), -sp.Rational(12, 13)],
                                                                  [0, sp.Rational(12, 13), sp.Rational(5, 13)]])
    eq_w = sp.simplify(frame_written(g * a, g * b) - g * frame_written(a, b)) == sp.zeros(3, 3)
    Fc = frame_corrected(a, b)
    eq_c = sp.simplify(frame_corrected(g * a, g * b) - g * Fc) == sp.zeros(3, 3)
    rot_c = sp.simplify(Fc.T * Fc - sp.eye(3)) == sp.zeros(3, 3) and sp.simplify(Fc.det()) == 1
    print(f"4. rational rotation g (det {g.det()}): written frame equivariant {eq_w}; corrected frame (q1, e2, q1 x e2) equivariant "
          f"{eq_c}, in SO(3) {rot_c}")

    rot_written = sp.simplify(g2 - sp.eye(3)) == sp.zeros(3, 3)
    if (not rot_written) and gram[2, 2] == sp.sin(t) ** 2 and eq_w and eq_c and rot_c:
        print(f"HIT: confirmed - block 18's written frame F = (q1, GS(q2), q1 x q2) is not a rotation matrix for non-orthogonal pairs: "
              f"F^T F = diag(1, 1, sin^2 t) and det F = sin t for q2 at angle t from q1 (exact: (2/3,2/3,1/3), (2/7,3/7,6/7) give "
              f"|q1 x q2|^2 = {cross2}, det F = {d2}), so M2's F . S_0 leaves S^2 (e3 -> squared length {cross2}); the equivariance "
              f"part holds; the corrected third column q1 x e2 = (q1 x q2)/|q1 x q2| gives an SO(3) frame, which is the one the runner's B2 checks")
        print("SUMMARY: confirmed - the note's frame lacks the 1/|q1 x q2| normalization of its third column (a definition typo; the runner "
              "builds the normalized frame, M2 holds with it)")
    else:
        print(f"SUMMARY: not reproduced - written frame rotation {rot_written}, gram {gram}")


if __name__ == "__main__":
    main()
