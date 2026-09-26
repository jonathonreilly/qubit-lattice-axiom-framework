#!/usr/bin/env python3
"""The walker against the member's cone -- worker w-macbookpro9927a-j6e7c.

Independent check of block 149 (PR #9242, head 5aacd93e4b) and the two-walker
kinematics. Families (see ATTEMPT.md):
  B  T1: the difference identity, the complete equality case, and an exact
     rational sweep of the strict inequality.
  M  T2: the massive energies are 1-Lipschitz in |s|.
  D  T4: the third-order split and |s(q)| < |p(q)|.
  S  T5: the symmetric pair, the two anchor values, the cos-sum criterion.
  X  T3's scope: in the first-quantized two-band walk one walker emits by an
     interband drop exactly at T5's resonance (exact sign change).
  W  two walkers: an exact kinematic witness of intraband emission by a pair.
Everything is exact (fractions, sympy, exact algebraic sign checks).
"""
import random
import sys
from fractions import Fraction as Fr

import sympy as sp

FAILS = []


def ok(tag, cond, msg=""):
    if not cond:
        FAILS.append(tag)
    print(f"{tag} {'ok' if cond else 'FAIL'} {msg}".rstrip())


k, q, mu, a, b = sp.symbols('k q mu a b', real=True)

# ---------------------------------------------------------------- family B
ident = sp.simplify(sp.expand_trig(sp.sin(k) - sp.sin(k - q)
                                   - 2 * sp.cos(k - q / 2) * sp.sin(q / 2))) == 0
n = sp.symbols('n', integer=True)
kk = q / 2 + n * sp.pi
flip = sp.simplify(sp.sin(kk - q) + sp.sin(kk)) == 0
ok("B1", ident and flip,
   "s_j(k) - s_j(k-q) = 2cos(k_j - q_j/2) sin(q_j/2); where cos = +-1, s_j(k-q) = -s_j(k)")
# equality case: components with q_j != 0 flip sign, others unchanged, so |s(k)| = |s(k-q)|


def circ(u):  # rational point on the circle from a rational slope u = tan(theta/2)
    return Fr(1 - u * u, 1 + u * u), Fr(2 * u, 1 + u * u)


random.seed(149)
strict_ok, cnt = True, 0
for _ in range(4000):
    ck, sk, ch, sh = [], [], [], []
    for j in range(3):
        c1, s1 = circ(Fr(random.randint(-40, 40), random.randint(1, 40)))
        c2, s2 = circ(Fr(random.randint(-40, 40), random.randint(1, 40)))
        ck.append(c1); sk.append(s1); ch.append(c2); sh.append(s2)
    # k_j with (cos, sin) = (ck, sk); q_j/2 with (cos, sin) = (ch, sh)
    sq = [2 * sh[j] * ch[j] for j in range(3)]              # sin q_j
    cq = [ch[j]**2 - sh[j]**2 for j in range(3)]            # cos q_j
    s_k = sk
    s_kq = [sk[j] * cq[j] - ck[j] * sq[j] for j in range(3)]  # sin(k_j - q_j)
    p2 = sum(4 * sh[j]**2 for j in range(3))
    if p2 == 0:
        continue
    A2, B2 = sum(x * x for x in s_k), sum(x * x for x in s_kq)
    lhs = A2 + B2 - p2            # (|a| - |b|)^2 < p^2  <=>  A2 + B2 - p2 < 2|a||b|
    strict_ok &= lhs < 0 or lhs * lhs < 4 * A2 * B2
    cnt += 1
ok("B2", strict_ok and cnt > 3900,
   f"| |s(k)| - |s(k-q)| | < |p(q)| at {cnt} exact rational points (k and q/2 on rational "
   "circle points), by squared rational comparison")

# ---------------------------------------------------------------- family M
lip = sp.expand((mu**2 + a**2) * (mu**2 + b**2) - (mu**2 + a * b)**2 - mu**2 * (a - b)**2) == 0
ok("M1", lip, "(mu^2+a^2)(mu^2+b^2) - (mu^2+ab)^2 = mu^2(a-b)^2 >= 0, so "
   "|sqrt(mu^2+a^2) - sqrt(mu^2+b^2)| <= |a-b|; and |s(k-Q)| = |s(k)| for Q = (pi,pi,pi)")

# ---------------------------------------------------------------- family D
ser = sp.series(sp.sin(q) - 2 * sp.sin(q / 2), q, 0, 7).removeO()
inside = sp.simplify(sp.sin(q) - 2 * sp.sin(q / 2) * sp.cos(q / 2)) == 0
ok("D1", sp.expand(ser - (-q**3 / 8 + sp.Rational(1, 128) * q**5)) == 0 and inside,
   "sin q - 2 sin(q/2) = -q^3/8 + q^5/128 + ...; s_j(q) = p_j(q) cos(q_j/2), so "
   "|s(q)| < |p(q)| for q != 0")

# ---------------------------------------------------------------- family S
q1, q2, q3 = sp.symbols('q1 q2 q3', real=True)
qs = (q1, q2, q3)
p2 = sum((2 * sp.sin(x / 2))**2 for x in qs)
half = sp.simplify(p2 - 4 * sum(sp.sin(x / 2)**2 for x in qs)) == 0
anchor = [sp.pi / 2 - x / 2 for x in qs]
pairsq = sum(sp.sin(y)**2 for y in anchor)  # |s(k)|^2 at k_a = pi/2 - q_a/2 (and |s(k+q)| equal)
same = sp.simplify(sum(sp.sin(y + x)**2 for y, x in zip(anchor, qs)) - pairsq) == 0
crit = sp.simplify(sp.expand_trig(4 * pairsq - p2 - 4 * sum(sp.cos(x) for x in qs))) == 0
ok("S1", half and same and crit,
   "|p(q)| = 2|s(q/2)|; at k_a = pi/2 - q_a/2 the pair energy is 2|cos(q/2)|, and "
   "(2|cos(q/2)|)^2 - |p(q)|^2 = 4 sum_a cos q_a; at k = 0 it is |s(q)| < |p(q)|")

# ---------------------------------------------------------------- family X
qv = [sp.pi / 3, 0, 0]
P = sp.sqrt(sum((2 * sp.sin(x / 2))**2 for x in qv))


def g(kv):  # upper band at k -> lower band at k - q, one disturbance q: need g = 0
    return (sp.sqrt(sum(sp.sin(x)**2 for x in kv))
            + sp.sqrt(sum(sp.sin(x - y)**2 for x, y in zip(kv, qv))) - P)


g0 = sp.nsimplify(sp.simplify(g(qv)))
g1 = sp.simplify(g([sp.pi / 2 + sp.pi / 6, sp.pi / 2, sp.pi / 2]))
ok("X1", P == 1 and g0 == sp.sqrt(3) / 2 - 1 and sp.simplify(g1 - (sp.sqrt(11) - 1)) == 0
   and (sp.sqrt(3) / 2 - 1) < 0 < sp.sqrt(11) - 1,
   "q = (pi/3,0,0), |p(q)| = 1: E_+(k) - E_-(k-q) - |p(q)| = |s(k)| + |s(k-q)| - 1 is "
   "sqrt(3)/2 - 1 < 0 at k = q and sqrt(11) - 1 > 0 at k = (2pi/3,pi/2,pi/2): an "
   "interband single-walker emission resonance lies on the segment between")

# ---------------------------------------------------------------- family W
f = sp.sin(a) + sp.sqrt(3) / 2 + 2 * sp.sin((a + sp.pi / 3) / 2) - 2
f0 = sp.simplify(f.subs(a, 0))
f1 = sp.simplify(f.subs(a, sp.pi / 6))
# f1 = sqrt(3)/2 + sqrt(2) - 3/2 > 0 exactly: (sqrt(3)/2 + sqrt(2))^2 = 11/4 + sqrt(6) > 9/4
pos = sp.simplify((sp.sqrt(3) / 2 + sp.sqrt(2))**2 - sp.Rational(11, 4) - sp.sqrt(6)) == 0
ok("W1", sp.simplify(f0 - (sp.sqrt(3) / 2 - 1)) == 0
   and sp.simplify(f1 - (sp.sqrt(3) / 2 + sp.sqrt(2) - sp.Rational(3, 2))) == 0 and pos,
   "two walkers (pi/2,0,0), (-pi/2,0,0) (energies 1, 1) -> (a,0,0), (pi/3,0,0) plus q = "
   "(-a-pi/3,0,0): the energy balance sin a + sqrt(3)/2 + 2 sin((a+pi/3)/2) - 2 is "
   "sqrt(3)/2 - 1 < 0 at a = 0 and sqrt(3)/2 + sqrt(2) - 3/2 > 0 at a = pi/6")
fp = sp.diff(f, a)
mono = sp.simplify(fp - (sp.cos(a) + sp.cos((a + sp.pi / 3) / 2))) == 0
cpos = sp.cos(sp.pi / 6) > 0 and sp.cos(sp.pi / 4) > 0
ok("W2", mono and cpos, "f'(a) = cos a + cos((a+pi/3)/2) >= cos(pi/6) + cos(pi/4) > 0 on [0, pi/6] "
   "(both arguments in [0, pi/4]): one root a* in (0, pi/6), "
   "final momenta distinct, q_x in (-pi/2, -pi/3), every walker in the upper band")

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
    sys.exit(1)
print("SUMMARY: PARTIAL block 149's T1, T2, T4 and T5 confirmed exactly (T1's equality case "
      "completed); T3 holds within a band and above the filled sea, and fails for one walker in "
      "the first-quantized two-band walk (interband drop at T5's resonance); a scattering pair's "
      "intraband emission is kinematically open (exact witness); the rate is not computed")
print("HIT: Block 149 checked independently. T1 holds: s_j(k) - s_j(k-q) = 2cos(k_j - q_j/2) "
      "sin(q_j/2) gives |s(k) - s(k-q)| <= |p(q)|, and where this is an equality the components "
      "with q_j != 0 change sign, so |s(k)| = |s(k-q)|; hence ||s(k)| - |s(k-q)|| < |p(q)| for "
      "q != 0 (this also covers s(k) = 0, which the note's equality clause omits). T2, T4 and T5 "
      "hold as stated. T3 needs a scope: it holds for transitions within one band, which is "
      "every single-excitation transition above the filled sea. In the first-quantized two-band "
      "walk one walker at k emits a disturbance q by dropping to the lower band whenever "
      "|s(k)| + |s(k-q)| = |p(q)|, which is solvable for every q with sum_a cos q_a > 0 "
      "(e.g. q = (pi/3,0,0)). Two walkers can emit within the upper band: (pi/2,0,0) + "
      "(-pi/2,0,0) -> (a*,0,0) + (pi/3,0,0) + q, q = (-a*-pi/3,0,0), a* in (0, pi/6) the "
      "unique root of sin a + sqrt(3)/2 + 2 sin((a+pi/3)/2) = 2. So a scattering pair's "
      "emission is kinematically open, and any vanishing must come from the amplitude.")
