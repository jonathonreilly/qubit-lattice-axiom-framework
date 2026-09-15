"""Control, block 18 (supervisor): menus. (1) the 24 proper rotations of the cube as integer matrices; orbits of directions
(6 axes, 8 diagonals, 12 edge directions, 24 generic); stabilizers; (2) a rational rotation about an axis (cos 3/5, sin 4/5)
moves a non-polar point to a new point: finite SO(2)_q-invariant sets are subsets of the poles; (3) the frame map of a pair is
equivariant under a rational rotation; (4) the Born overlap on the antipodal menu is deterministic; (5) seed-generated alphabet on a
path under the antipodal support (symbolic seed)."""
from fractions import Fraction as F
from itertools import permutations, product
import sympy as sp
def rotations():
    mats = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            Mx = [[0] * 3 for _ in range(3)]
            for i in range(3):
                Mx[perm[i]][i] = signs[i]
            det = sp.Matrix(Mx).det()
            if det == 1:
                mats.append(tuple(tuple(r) for r in Mx))
    return mats
R = rotations()
print("proper rotations:", len(R))
def apply(Mx, v):
    return tuple(sum(Mx[i][j] * v[j] for j in range(3)) for i in range(3))
def orbit(v):
    return {apply(Mx, v) for Mx in R}
for name, v in (("axis", (1, 0, 0)), ("diagonal", (1, 1, 1)), ("edge", (1, 1, 0)), ("generic", (1, 2, 3)), ("mirror-plane generic", (1, 1, 2))):
    o = orbit(v); stab = sum(1 for Mx in R if apply(Mx, v) == v)
    print(f"{name} {v}: orbit size {len(o)}, stabilizer order {stab}")
# (2) rational rotation about z by angle with cos 3/5 sin 4/5
Rz = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
s = sp.Matrix([sp.Rational(3, 5), 0, sp.Rational(4, 5)])  # a unit vector not on the z-axis
pts = set(); cur = s
for k in range(12):
    pts.add(tuple(cur)); cur = Rz * cur
print("orbit of a non-polar unit vector under a rational rotation about z: distinct points after 12 steps:", len(pts), "(the pole is fixed:", tuple(Rz * sp.Matrix([0, 0, 1])), ")")
# (3) frame equivariance
q1 = sp.Matrix([1, 0, 0]); q2 = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5), 0])
def frame(a, b):
    e1 = a
    e2 = b - (a.dot(b)) * a; e2 = e2 / sp.sqrt(e2.dot(e2))
    e3 = e1.cross(e2)
    return sp.Matrix.hstack(e1, e2, e3)
g = sp.Matrix([[sp.Rational(3, 5), 0, sp.Rational(4, 5)], [0, 1, 0], [-sp.Rational(4, 5), 0, sp.Rational(3, 5)]])  # rotation about y
print("frame equivariance F(g q1, g q2) == g F(q1, q2):", sp.simplify(frame(g * q1, g * q2) - g * frame(q1, q2)) == sp.zeros(3, 3))
# (4) Born on antipodal
t = sp.symbols("t")
f = (1 + t) / 2
print("Born overlap at t = 1 and t = -1:", f.subs(t, 1), f.subs(t, -1))
# (5) seed-generated alphabet: path of 5 with the antipodal support {q, -q} and copy probability a
a = sp.symbols("a", positive=True)
seed = sp.Matrix(sp.symbols("s1 s2 s3"))
# values are ±seed; the law on the path with rule r(q|q) = a, r(-q|q) = 1-a: all patterns in {±seed}^5; check the support
vals = [seed, -seed]
patterns = list(product(range(2), repeat=5))
print("path of 5 under the antipodal support: every record is ±seed; patterns:", len(patterns), "; all in the seed's axis:", all(all(vals[i] in (seed, -seed) for i in pat) for pat in patterns))
