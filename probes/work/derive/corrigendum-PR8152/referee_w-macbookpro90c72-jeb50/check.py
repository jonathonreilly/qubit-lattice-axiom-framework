"""Independent confirmation of the PR 8152 frame corrigendum.

Own cross products and own Cayley rotations. The author's script is not called.
"""
import subprocess
import sys

import sympy as sp

FAILS = []


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def dot(a, b):
    return (a.T * b)[0]


def cross(a, b):
    return sp.Matrix([
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ])


def note_frame(q1, q2):
    u = q2 - dot(q1, q2) * q1
    u = u / sp.sqrt(dot(u, u))
    return sp.Matrix.hstack(q1, u, cross(q1, q2))


def fixed_frame(q1, q2):
    u = q2 - dot(q1, q2) * q1
    u = u / sp.sqrt(dot(u, u))
    return sp.Matrix.hstack(q1, u, cross(q1, u))


def gram_det(F):
    return sp.simplify(F.T * F), sp.simplify(F.det())


# Lagrange identity: |q1 x q2|^2 = |q1|^2 |q2|^2 - (q1·q2)^2
x = sp.Matrix(sp.symbols("x1 x2 x3"))
y = sp.Matrix(sp.symbols("y1 y2 y3"))
n = cross(x, y)
lag = sp.expand(dot(n, n) - (dot(x, x) * dot(y, y) - dot(x, y) ** 2))
# unit axis and a unit partner at sine s
s = sp.symbols("s", positive=True)
q1 = sp.Matrix([1, 0, 0])
q2 = sp.Matrix([sp.sqrt(1 - s ** 2), s, 0])
Fn = note_frame(q1, q2)
G, d = gram_det(Fn)
ok = lag == 0 and sp.simplify(G - sp.diag(1, 1, s ** 2)) == sp.zeros(3) and sp.simplify(d - s) == 0
Ff = fixed_frame(q1, q2)
Gf, df = gram_det(Ff)
ok = ok and sp.simplify(Gf - sp.eye(3)) == sp.zeros(3) and sp.simplify(df - 1) == 0
ok = ok and sp.simplify(Fn - Ff * sp.diag(1, 1, s)) == sp.zeros(3)
want("S1 the written third column has length sin t and the corrected frame is a rotation", ok)

pairs = [
    (sp.Matrix([1, 0, 0]), sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5), 0]), sp.Rational(16, 25)),
    (sp.Matrix([sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3)]),
     sp.Matrix([sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)]),
     sp.Rational(185, 441)),
]
ok = True
for a, b, cross2 in pairs:
    n = cross(a, b)
    ok = ok and sp.simplify(dot(n, n) - cross2) == 0
    Fn = note_frame(a, b)
    Ff = fixed_frame(a, b)
    Gn, dn = gram_det(Fn)
    Gf, df = gram_det(Ff)
    sint = sp.sqrt(cross2)
    ok = ok and sp.simplify(Gn - sp.diag(1, 1, cross2)) == sp.zeros(3)
    ok = ok and sp.simplify(dn - sint) == 0
    ok = ok and sp.simplify(Gf - sp.eye(3)) == sp.zeros(3) and sp.simplify(df - 1) == 0
    ok = ok and sp.simplify(Fn - Ff * sp.diag(1, 1, sint)) == sp.zeros(3)
want("S2 at (1,0,0),(3/5,4/5,0) the note determinant is 4/5; the second pair has cross-square 185/441", ok)

def cayley(a, b, c):
    A = sp.Matrix([[0, -c, b], [c, 0, -a], [-b, a, 0]])
    return sp.simplify((sp.eye(3) - A) * (sp.eye(3) + A).inv())


ok = True
for a, b, c in ((sp.Rational(1, 3), sp.Rational(-1, 5), sp.Rational(1, 7)),
                (sp.Rational(2, 9), sp.Rational(1, 4), sp.Rational(-1, 6))):
    Q = cayley(a, b, c)
    ok = ok and sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3) and sp.simplify(Q.det() - 1) == 0
    for q1, q2, _ in pairs:
        for frame in (note_frame, fixed_frame):
            left = sp.simplify(frame(Q * q1, Q * q2))
            right = sp.simplify(Q * frame(q1, q2))
            ok = ok and left == right
want("S3 both frames are equivariant under two rational rotations, and the corrected one has determinant 1", ok)

note = "docs/ADMISSIBILITY_RULE_MENUS_NEIGHBOUR_GENERATED_SUPPORTS_UNSOLDERED_AND_CUBE_ORBIT_MENUS_SOLDERED_BOUNDED_THEOREM_NOTE_2026-09-15.md"
body = subprocess.run(["git", "show", f"70f28178:{note}"], capture_output=True, text=True).stdout.splitlines()
line = body[90] if len(body) >= 91 else ""
ok = "q_1 × q_2" in line and "rotation matrix" in line
runner = "scripts/admissibility_rule_menus_neighbour_generated_supports_and_cube_orbit_menus_2026_09_15.py"
src = subprocess.run(["git", "show", f"70f28178:{runner}"], capture_output=True, text=True).stdout.splitlines()
chunk = "\n".join(src[130:135])
ok = ok and "e1.cross(e2)" in chunk and "e2 /" in chunk
want("S4 the note's line 91 writes the un-normalised cross product, and the runner already crosses the normalised axis", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - the note's frame has Gram diag(1, 1, sin^2 t) and determinant sin t, "
    "so it is a rotation only for orthogonal pairs. At the executed pair the determinant is 4/5. "
    "Replacing the third column by q1 cross u2 makes a rotation for every non-collinear pair, and that is what the runner builds."
)
print(
    "SUMMARY: confirmed the corrigendum. One symbol in the note's definition is the fix. "
    "Both frames stay equivariant. The second witness has |q1 cross q2|^2 = 185/441."
)
