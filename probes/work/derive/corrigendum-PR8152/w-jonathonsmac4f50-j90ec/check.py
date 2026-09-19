#!/usr/bin/env python3
"""Corrigendum packet for PR #8152 (block 18's frame): the checks behind ATTEMPT.md.

Block 18 (note at 70f28178, L90-92): 'For non-collinear unit vectors q_1, q_2, the frame F(q_1, q_2) = (q_1, (q_2 - (q_1.q_2) q_1)/|.|, q_1 x q_2)
is a rotation matrix with F(g q_1, g q_2) = g F(q_1, q_2) for g in SO(3).'
 F1  for unit q_1, q_2: F_note^T F_note = diag(1, 1, |q_1 x q_2|^2), |q_1 x q_2|^2 = 1 - (q_1.q_2)^2 (Lagrange), det F_note = |q_1 x q_2| = sin t;
     so F_note is a rotation iff q_1 . q_2 = 0 (the largest domain of the original)
 F2  the executed pair of the runner, q_1 = (1,0,0), q_2 = (3/5, 4/5, 0): det F_note = 4/5, and F_note e_3 has squared length 16/25 (off S^2);
     the pair (2/3,2/3,1/3), (2/7,3/7,6/7): |q_1 x q_2|^2 = 185/441
 F3  the corrected frame F = (q_1, u_2, q_1 x u_2), u_2 = (q_2 - (q_1.q_2) q_1)/|.|: F^T F = I, det F = 1, F_note = F diag(1, 1, sin t);
     equivariance F(g q_1, g q_2) = g F(q_1, q_2) for g in SO(3) (Cayley rotations with rational parameters, and the identity
     g(a x b) = (g a) x (g b) for det g = 1, symbolically)
 F4  the runner's frame function (e2 normalized, third column e1.cross(e2)) is the corrected F at the executed pair (not F_note)
"""
import sys

import sympy as sp

FAILS = []


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


def F_note(q1, q2):
    u2 = q2 - q1.dot(q2) * q1
    u2 = u2 / sp.sqrt(u2.dot(u2))
    return sp.Matrix.hstack(q1, u2, q1.cross(q2))


def F_fix(q1, q2):
    u2 = q2 - q1.dot(q2) * q1
    u2 = u2 / sp.sqrt(u2.dot(u2))
    return sp.Matrix.hstack(q1, u2, q1.cross(u2))


def main():
    t = sp.Symbol("t", real=True)
    q1 = sp.Matrix([1, 0, 0])
    q2 = sp.Matrix([sp.cos(t), sp.sin(t), 0])
    tt = sp.Symbol("tt", positive=True)            # restrict to 0 < t < pi via sin t = s > 0
    s = sp.Symbol("s", positive=True)
    q2s = sp.Matrix([sp.sqrt(1 - s ** 2), s, 0])
    Fn = F_note(q1, q2s)
    G = sp.simplify(Fn.T * Fn)
    ok = sp.simplify(G - sp.diag(1, 1, s ** 2)) == sp.zeros(3, 3) and sp.simplify(Fn.det() - s) == 0
    # general unit vectors: Lagrange identity and orthogonality of the columns
    a = sp.Matrix(sp.symbols("a1:4", real=True))
    b = sp.Matrix(sp.symbols("b1:4", real=True))
    lag = sp.expand(a.cross(b).dot(a.cross(b)) - (a.dot(a) * b.dot(b) - a.dot(b) ** 2)) == 0
    orth = sp.expand(a.dot(a.cross(b))) == 0 and sp.expand(b.dot(a.cross(b))) == 0
    ok &= lag and orth
    check("F1", ok, "for unit q_1, q_2 at angle t: F_note^T F_note = diag(1, 1, sin^2 t) and det F_note = sin t (with q_2 = (sqrt(1 - s^2), s, 0) by rotation "
          "invariance; in general the third column q_1 x q_2 is orthogonal to q_1 and to span(q_1, q_2) and has squared length 1 - (q_1.q_2)^2 by the "
          "Lagrange identity, checked symbolically): F_note is a rotation iff q_1 . q_2 = 0")
    # F2
    p1 = sp.Matrix([1, 0, 0])
    p2 = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5), 0])
    Fe = F_note(p1, p2)
    col3 = Fe[:, 2]
    c1 = sp.Matrix([sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3)])
    c2 = sp.Matrix([sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)])
    ok = Fe.det() == sp.Rational(4, 5) and col3.dot(col3) == sp.Rational(16, 25) and c1.cross(c2).dot(c1.cross(c2)) == sp.Rational(185, 441)
    check("F2", ok, f"at the runner's executed pair q_1 = (1,0,0), q_2 = (3/5, 4/5, 0): det F_note = {Fe.det()}, and F_note e_3 = {list(col3)} has squared length "
          f"16/25, so F_note . S_0 leaves the sphere; at the pair (2/3,2/3,1/3), (2/7,3/7,6/7): |q_1 x q_2|^2 = 185/441")
    # F3
    Ff = F_fix(q1, q2s)
    ok = sp.simplify(Ff.T * Ff - sp.eye(3)) == sp.zeros(3, 3) and sp.simplify(Ff.det() - 1) == 0 and sp.simplify(Fn - Ff * sp.diag(1, 1, s)) == sp.zeros(3, 3)
    # equivariance: Cayley rotation with rational parameters, and the general cross-product identity for rotations
    def cayley(x, y, z):
        Sk = sp.Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])
        I = sp.eye(3)
        return (I - Sk).inv() * (I + Sk)
    ok_eq = True
    for (x, y, z) in ((sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(-1, 5)), (sp.Rational(2), sp.Rational(-1, 7), sp.Rational(3, 4))):
        g = cayley(x, y, z)
        ok_eq &= sp.simplify(g.T * g - sp.eye(3)) == sp.zeros(3, 3) and g.det() == 1
        for (u, v) in ((p1, p2), (c1, c2)):
            ok_eq &= sp.simplify(F_fix(g * u, g * v) - g * F_fix(u, v)) == sp.zeros(3, 3)
            ok_eq &= sp.simplify(F_note(g * u, g * v) - g * F_note(u, v)) == sp.zeros(3, 3)
    ok &= ok_eq
    check("F3", ok, "the corrected frame F = (q_1, u_2, q_1 x u_2) has F^T F = I and det F = 1 for every non-collinear unit pair, F_note = F diag(1, 1, sin t); "
          "both F and F_note are SO(3)-equivariant (checked with two rational Cayley rotations at both pairs); only F is a rotation, which M2's "
          "S = F . S_0 and M4's 'orbit under compositions of the frame maps' need to stay on S^2")
    # F4: the runner's frame
    def runner_frame(a_, b_):
        e1 = a_
        e2 = b_ - (a_.dot(b_)) * a_
        e2 = e2 / sp.sqrt(e2.dot(e2))
        return sp.Matrix.hstack(e1, e2, e1.cross(e2))
    ok = runner_frame(p1, p2) == F_fix(p1, p2) and runner_frame(p1, p2) != F_note(p1, p2)
    check("F4", ok, "the runner's frame (block 18 runner L131-135: e2 normalized, third column e1.cross(e2)) equals the corrected F at the executed pair and "
          "differs from the note's formula: the runner's B2 ('a rotation matrix') tested the corrected frame, not the note's")
    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("corrigendum for PR #8152: block 18's written frame F = (q_1, GS(q_2), q_1 x q_2) has F^T F = diag(1, 1, sin^2 t) and det F = sin t, so it is a "
            "rotation only for orthogonal pairs (det 4/5 at the executed pair); the corrected frame (q_1, u_2, q_1 x u_2) is a rotation for every non-collinear "
            "pair and equivariant, equals what the runner already builds, and M2 (S = F S_0) and M4 (frame-map orbits) hold with it; the fix is one symbol "
            "in the note's definition (L91); no other note of #8146-#8180 uses the formula")
    print("SUMMARY: PROVED (ATTEMPT.md S1-S4; finite facts CHECKED here) " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
