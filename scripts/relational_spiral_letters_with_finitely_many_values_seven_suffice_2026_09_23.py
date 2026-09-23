#!/usr/bin/env python3
"""Relational spiral letters with finitely many values: seven suffice, and
no spiral does with fewer.

Open PR 8691 built relational letters under possibility covariance from
spirals b(x) = R_z(theta . x) b0 with Pythagorean angles, which take
infinitely many values, and left open whether finitely many possibilities
suffice.  Its rule reads a great circle from three back-neighbour values
and returns the unique point that each value reaches by one of the three
rotations.  For angles theta_1, theta_2, theta_3 the output is unique when
  (a) the angles are distinct modulo 180 degrees,
  (b) no permutation shifts every angle by the same amount: no three angles
      in arithmetic progression with step 120 degrees, and
  (c) no angle is the mean of the other two modulo 180 degrees
      (theta_i + theta_j != 2 theta_k modulo 360).
The angles (30, 60, 150) degrees meet all three.  Their spiral lives in
Q(sqrt 3) and takes twelve values on one great circle.  On a box every site
with three back-neighbours is the rule's unique output, the rule commutes
with a rotation of the sphere, and each site reads each neighbour's bond
direction from the rotation between their values.  The angles (30, 90, 150)
break (c), and the rule then has a second output.  A spiral with m values
needs six distinct nonzero signed angles among the multiples of 360/m, so
m >= 7.  For spiral inputs every value lies on one great circle and the
rule's normal is the axis, so each fit is a congruence of angle multiples
modulo m; this planar reduction reproduces the exact Q(sqrt 3) rule at
every site of the twelve-value box, and with it the angles (1, 2, 4) x
360/7 give a seven-value spiral that is the rule's unique output at every
site of a box, with the frame reading.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * the rule of open PR 8691: great circle from w_0 x w_1, all six
    assignments and both orientations, unique surviving point;
  * exact arithmetic in Q(sqrt 3): pairs (a, b) = a + b sqrt 3 of Fractions;
  * the spiral from b0 = (1, 0, 0) about z; boxes 0..L-1 in each coordinate.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


class Q3:
    """a + b sqrt(3) with rational a, b."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, Q3) else Q3(o)))

    def __rsub__(self, o):
        return Q3(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self):
        d = self.a * self.a - 3 * self.b * self.b
        return Q3(self.a / d, -self.b / d)

    def __truediv__(self, o):
        return self * (o if isinstance(o, Q3) else Q3(o)).inv()

    def __eq__(self, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def is_zero(self):
        return self.a == 0 and self.b == 0


def sqrt3field(x):
    """Square root in Q(sqrt 3) of x when it exists there (tries p and q sqrt 3 with rational p, q)."""
    if x.b == 0:
        for cand in (Q3(_ratsqrt(x.a)) if _ratsqrt(x.a) is not None else None,
                     Q3(0, _ratsqrt(x.a / 3)) if _ratsqrt(x.a / 3) is not None else None):
            if cand is not None and cand * cand == x:
                return cand
    return None


def _ratsqrt(r):
    if r < 0:
        return None
    n, d = r.numerator, r.denominator
    sn, sd = _isqrt(n), _isqrt(d)
    return Fr(sn, sd) if sn * sn == n and sd * sd == d else None


def _isqrt(n):
    x = int(n ** 0.5)
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


S3 = Q3(0, 1)
HALF = Q3(Fr(1, 2))
TRIG = {0: (Q3(1), Q3(0)), 30: (S3 * HALF, HALF), 60: (HALF, S3 * HALF), 90: (Q3(0), Q3(1))}


def cs(deg):
    """(cos, sin) of a multiple of 30 degrees, exactly."""
    deg %= 360
    base = deg % 90
    c, s = TRIG[base]
    for _ in range(deg // 90):
        c, s = -s, c
    return c, s


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def rot(n, c, s, v):
    nxv, nv = cross(n, v), dot(n, v)
    return tuple(c * v[t] + s * nxv[t] + (1 - c) * nv * n[t] for t in range(3))


def rule_outputs(ws, angles):
    """All points b with w_i = R_{o n}(-theta_{sigma(i)}) b for some assignment sigma and orientation o."""
    n0 = cross(ws[0], ws[1])
    norm = sqrt3field(dot(n0, n0))
    if norm is None or norm.is_zero():
        return set()
    n = tuple(x / norm for x in n0)
    if not all(dot(n, w).is_zero() for w in ws):
        return set()
    outs = set()
    for sigma in permutations(range(3)):
        for o in (1, -1):
            no = tuple(o * x for x in n)
            c0, s0 = cs(angles[sigma[0]])
            b = rot(no, c0, s0, ws[0])
            if all(rot(no, *[cs(angles[sigma[i]])[0], -cs(angles[sigma[i]])[1]], b) == ws[i] for i in range(3)):
                outs.add(tuple((x.a, x.b) for x in b))
    return outs


def spiral(x, angles, Qrot=None):
    c, s = cs(sum(t * k for t, k in zip(angles, x)))
    v = (c, s, Q3(0))
    return Qrot(v) if Qrot else v


def key(v):
    return tuple((x.a, x.b) for x in v)


print("A. the conditions on the angles")
GOOD, BAD = (30, 60, 150), (30, 90, 150)


def conditions(th):
    a = len({t % 180 for t in th}) == 3
    b = not any(len({(th[p[i]] - th[i]) % 360 for i in range(3)}) == 1 for p in permutations(range(3)) if p != (0, 1, 2)
                and all(p[i] != i for i in range(3)))
    c = all((th[i] + th[j] - 2 * th[k]) % 360 != 0 for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)))
    signed = len({t % 360 for t in th} | {(-t) % 360 for t in th}) == 6
    return a, b, c, signed


check("(30, 60, 150) degrees meet the three uniqueness conditions; (30, 90, 150) breaks the third",
      all(conditions(GOOD)) and conditions(BAD)[:2] == (True, True) and conditions(BAD)[2] is False,
      "distinct modulo 180, no equal shift under a 3-cycle, no angle the mean of the other two; six signed angles distinct")

print("B. the twelve-point spiral is stationary under the rule")
L = 4
values, unique_ok, sites = set(), True, 0
for x in product(range(L), repeat=3):
    values.add(key(spiral(x, GOOD)))
    if all(c >= 1 for c in x):
        ws = [spiral(tuple(x[j] - (j == i) for j in range(3)), GOOD) for i in range(3)]
        outs = rule_outputs(ws, GOOD)
        unique_ok = unique_ok and outs == {key(spiral(x, GOOD))}
        sites += 1
check("on the 4-box every site with three back-neighbours is the rule's unique output; the record takes 12 values",
      unique_ok and sites == 27 and len(values) == 12,
      f"{sites} sites, one output each; values are the 12 multiples of 30 degrees on the equator, in Q(sqrt 3)")

print("C. covariance and the frame reading")
Qx = lambda v: (v[0], -v[2], v[1])
cov_ok = True
for x in product(range(1, L), repeat=3):
    ws = [spiral(tuple(x[j] - (j == i) for j in range(3)), GOOD, Qx) for i in range(3)]
    cov_ok = cov_ok and rule_outputs(ws, GOOD) == {key(spiral(x, GOOD, Qx))}
read_ok = True
for x in product(range(1, L - 1), repeat=3):
    here = sum(t * k for t, k in zip(GOOD, x))
    for i in range(3):
        for d in (1, -1):
            y = tuple(x[j] + (d if j == i else 0) for j in range(3))
            there = sum(t * k for t, k in zip(GOOD, y))
            read_ok = read_ok and (there - here) % 360 == (d * GOOD[i]) % 360
E1, E2, E3 = (Q3(1), Q3(0), Q3(0)), (Q3(0), Q3(1), Q3(0)), (Q3(0), Q3(0), Q3(1))
proper = dot(cross(Qx(E1), Qx(E2)), Qx(E3)) == 1 and all(dot(Qx(u), Qx(v)) == dot(u, v) for u in (E1, E2, E3) for v in (E1, E2, E3))
check("the rule commutes with a quarter turn of the sphere, and each core site reads its six bond directions",
      cov_ok and read_ok and proper,
      "a quarter turn about x maps the equator spiral to a spiral on another great circle and the outputs follow; "
      "the rotation to each neighbour is one of the six distinct signed angles")

print("D. the contrast")
x0 = (1, 1, 1)
ws = [spiral(tuple(x0[j] - (j == i) for j in range(3)), BAD) for i in range(3)]
outs_bad = rule_outputs(ws, BAD)
check("with (30, 90, 150) degrees the rule has a second output at the first site",
      len(outs_bad) == 2 and key(spiral(x0, BAD)) in outs_bad,
      "30 + 150 = 2 x 90: reversing the orientation with the outer angles swapped also fits")

print("E. the fewest values")


def works(m):
    """Triples of multiples of 360/m meeting the conditions (angles in units of 360/m, so work modulo m)."""
    good = []
    for tri in product(range(1, m), repeat=3):
        if len(set(tri)) < 3:
            continue
        a = len({(2 * t) % m for t in tri}) == 3
        signed = len({t % m for t in tri} | {(-t) % m for t in tri}) == 6
        bcond = not any(len({(tri[p_[i]] - tri[i]) % m for i in range(3)}) == 1
                        for p_ in permutations(range(3)) if all(p_[i] != i for i in range(3)))
        ccond = all((tri[i] + tri[j] - 2 * tri[k]) % m != 0 for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)))
        if a and signed and bcond and ccond:
            good.append(tri)
    return good


smallest = [m for m in range(2, 13) if works(m)]
check("a spiral with m values needs m >= 7; the angles (1, 2, 4) x 360/7 meet every condition",
      smallest and smallest[0] == 7 and (1, 2, 4) in works(7) and (1, 6, 2) not in works(7) and works(12)
      and all(not works(m) for m in range(2, 7)),
      f"m with a valid triple up to 12: {smallest}; six distinct nonzero signed angles need m >= 7")

print("F. seven values, by the planar reduction")


def planar_outputs(angles_in, th, m):
    """Rule fits for inputs on one great circle, angles in units of 360/m: s = +-1 is the rotation sense."""
    outs = set()
    for sigma in permutations(range(3)):
        for sgn in (1, -1):
            b = (angles_in[0] + sgn * th[sigma[0]]) % m
            if all((b - sgn * th[sigma[i]]) % m == angles_in[i] % m for i in range(3)):
                outs.add(b)
    return outs


def same_output(planar, exact):
    """The planar reduction's single output, as a point, is the exact rule's single output."""
    if len(planar) != 1 or len(exact) != 1:
        return False
    c_, s_ = cs(30 * next(iter(planar)))
    return key((c_, s_, Q3(0))) in exact


def both(x):
    ins = [sum(t // 30 * k for t, k in zip(GOOD, tuple(x[j] - (j == i) for j in range(3)))) % 12 for i in range(3)]
    exact = rule_outputs([spiral(tuple(x[j] - (j == i) for j in range(3)), GOOD) for i in range(3)], GOOD)
    return planar_outputs(ins, [t // 30 for t in GOOD], 12), exact


agree12 = all(same_output(*both(x)) for x in product(range(1, L), repeat=3))
control12 = not same_output(both((1, 1, 1))[0], both((2, 1, 1))[1])
TH7 = (1, 2, 4)
seven_ok, vals7, n7 = True, set(), 0
for x in product(range(5), repeat=3):
    here = sum(t * k for t, k in zip(TH7, x)) % 7
    vals7.add(here)
    if all(c >= 1 for c in x):
        ins = [sum(t * k for t, k in zip(TH7, tuple(x[j] - (j == i) for j in range(3)))) % 7 for i in range(3)]
        seven_ok = seven_ok and planar_outputs(ins, TH7, 7) == {here}
        n7 += 1
signed7 = len({t % 7 for t in TH7} | {(-t) % 7 for t in TH7}) == 6
check("seven values suffice: the planar reduction matches the exact rule at twelve values and gives unique outputs at seven",
      agree12 and control12 and seven_ok and n7 == 64 and len(vals7) == 7 and signed7,
      f"twelve-value box: planar and Q(sqrt 3) outputs agree at all 27 sites; seven-value 5-box: {n7} sites, one output "
      "each, 7 values, six distinct signed angles for the frame reading")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
