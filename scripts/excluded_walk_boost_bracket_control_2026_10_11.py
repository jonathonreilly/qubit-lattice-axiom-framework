#!/usr/bin/env python3
"""Finite algebra and constants for the conditional excluded-walk boost note.

The preserved helpers use exact rational/Pauli/Fourier or symbolic algebra,
plus a floating three-vector forcing fixture with explicit tolerances.
Their namespaces are separate. These are source-author controls;
publication replay does not constitute independent mathematical review.
The source note's analytic domain, packet and evolution proofs are separate.
No stochastic, network or external-data input is read. The last two helpers
hash this primary's own bytes for provenance. The note is declared
for repository evidence binding. Run with assertions enabled.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    "docs/EXCLUDED_WALK_BOOST_BRACKET_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]
if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

_SOURCE_BOOST_CURRENT = r'''"""Exact author controls for the compressed boost/current derivation.

Independent routes within this author calculation: the left side constructs
the dipole from its two symmetrized position/one-body-energy terms, then nests
commutators. The right side uses normal-ordered contact form factors. This is
finite algebra evidence, not independent review or a proof of analytic bounds.

Full three-dimensional relative Fourier polynomials; all four spin entries;
quadratic total-momentum jets. No sampled q quadrature or floating arithmetic.
Only constant jets are compared after at most two K derivatives.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import factorial
from sympy.polys.domains import QQ, QQ_I

Z = QQ_I.zero
ONE = QQ_I.one
I = QQ_I(0, 1)
HALF = QQ_I(QQ(1, 2))
ZERO = (0, 0, 0)
MAX = 2
checks = 0


def conj(z):
    return QQ_I(z.x, -z.y)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def clean(d):
    return {k: v for k, v in d.items() if v}


def add(*fields):
    out = defaultdict(lambda: Z)
    for v in fields:
        for k, x in v.items():
            out[k] += x
    return clean(out)


def scale(v, z):
    return clean({k: z * x for k, x in v.items()})


def dk(v, a):
    out = {}
    for (p, q, s), x in v.items():
        if p[a]:
            pp = list(p)
            pp[a] -= 1
            out[(tuple(pp), q, s)] = x * p[a]
    return out


def dq(v, a):
    return clean({(p, q, s): x * I * q[a] for (p, q, s), x in v.items()})


def mul_scalar(f, v):
    out = defaultdict(lambda: Z)
    for (p, q, _), x in f.items():
        for (p2, q2, s), y in v.items():
            pp = plus(p, p2)
            if sum(pp) <= MAX:
                out[(pp, plus(q, q2), s)] += x * y
    return clean(out)


def inner(v, w):
    # Fiber inner product only: K remains a real formal Taylor variable.
    out = defaultdict(lambda: Z)
    by_qs = defaultdict(list)
    for (p, q, s), x in w.items():
        by_qs[(q, s)].append((p, x))
    for (p, q, s), x in v.items():
        for p2, y in by_qs[(q, s)]:
            pp = plus(p, p2)
            if sum(pp) <= MAX:
                out[(pp, ZERO, 0)] += conj(x) * y
    return clean(out)


def P(v):
    # c0=(0,1,-1,0); C=|c0><c0|/2, avoiding sqrt(2) arithmetic.
    means = defaultdict(lambda: Z)
    for (p, q, s), x in v.items():
        if q == ZERO and s in (1, 2):
            means[p] += (1 if s == 1 else -1) * x * HALF
    corr = {}
    for p, x in means.items():
        corr[(p, ZERO, 1)] = -x
        corr[(p, ZERO, 2)] = x
    return add(v, corr)


def outer(u, v, w):
    # Every form factor u,v here is computed with c0, hence divide by two.
    return scale(mul_scalar(inner(v, w), u), HALF)


def trigq(a, n, sine=False):
    q = [0, 0, 0]
    q[a] = n
    nq = tuple(-x for x in q)
    return {(ZERO, tuple(q), 0): -I * HALF if sine else HALF,
            (ZERO, nq, 0): I * HALF if sine else HALF}


def halfangle_jet(a, c, s, sine=False):
    vals = (s, c * HALF, -s / QQ_I(8)) if sine else (c, -s * HALF, -c / QQ_I(8))
    out = {}
    for n, x in enumerate(vals):
        p = [0, 0, 0]
        p[a] = n
        out[(tuple(p), ZERO, 0)] = x
    return clean(out)


def pauli(v, particle, axis):
    out = defaultdict(lambda: Z)
    for (p, q, s), x in v.items():
        bit = (s >> (1 - particle)) & 1
        if axis == 0:
            ss, factor = s ^ (1 << (1 - particle)), ONE
        elif axis == 1:
            ss, factor = s ^ (1 << (1 - particle)), I if bit == 0 else -I
        else:
            ss, factor = s, ONE if bit == 0 else -ONE
        out[(p, q, ss)] += factor * x
    return clean(out)


cs = [(QQ_I(QQ(63, 65)), QQ_I(QQ(16, 65))),
      (QQ_I(QQ(12, 13)), QQ_I(QQ(5, 13))),
      (QQ_I(QQ(4, 5)), QQ_I(QQ(3, 5)))]
C = [halfangle_jet(a, *cs[a]) for a in range(3)]
S = [halfangle_jet(a, *cs[a], sine=True) for a in range(3)]
sinK = [scale(mul_scalar(C[a], S[a]), QQ_I(2)) for a in range(3)]
cosK = [add(mul_scalar(C[a], C[a]), scale(mul_scalar(S[a], S[a]), -ONE)) for a in range(3)]
symbols = [[add(mul_scalar(S[a], trigq(a, 1)),
                scale(mul_scalar(C[a], trigq(a, 1, sine=True)), ONE if i == 0 else -ONE))
            for a in range(3)] for i in range(2)]


def hi(v, i):
    return add(*(mul_scalar(symbols[i][a], pauli(v, i, a)) for a in range(3)))


def H(v):
    return add(hi(v, 0), hi(v, 1))


def Hd(v):
    return P(H(P(v)))


def Hdiff(v):
    return add(hi(v, 0), scale(hi(v, 1), -ONE))


def Hprime(v, a):
    return add(*(mul_scalar(dk(symbols[i][j], a), pauli(v, i, j))
                 for i in range(2) for j in range(3)))


def X(v, i, a):
    return scale(add(dk(v, a), scale(dq(v, a), HALF if i == 0 else -HALF)), I)


def D0(v, a):
    return scale(add(*(add(X(hi(v, i), i, a), hi(X(v, i, a), i)) for i in range(2))), HALF)


def D(v, a):
    return P(D0(P(v), a))


c0 = {(ZERO, ZERO, 1): ONE, (ZERO, ZERO, 2): -ONE}
h = H(c0)
hb = [dk(h, a) for a in range(3)]
g = [mul_scalar(sinK[a], trigq(a, 2)) for a in range(3)]
r = [mul_scalar(g[a], c0) for a in range(3)]


def Fb(v, b):
    return scale(add(outer(hb[b], h, v), outer(h, hb[b], v)), -ONE)


def J(v, b):
    return add(P(mul_scalar(g[b], P(v))), Fb(v, b))


def Jraw(v, b):
    return scale(add(Hd(D(v, b)), scale(D(Hd(v), b), -ONE)), I)


def A(v, b):
    return add(scale(outer(h, r[b], v), -ONE), outer(r[b], h, v),
               scale(outer(Hd(hb[b]), h, v), -ONE),
               scale(outer(Hd(h), hb[b], v), -ONE),
               outer(hb[b], Hd(h), v), outer(h, Hd(hb[b]), v))


def L(v, a):
    return P(add(scale(Hdiff(dq(P(v), a)), HALF), Hprime(P(v), a)))


def Ladj(v, a):
    return scale(P(Hdiff(dq(P(v), a))), -HALF)


def B(v, a, b):
    hab = dk(hb[b], a)
    Fprime = scale(add(outer(hab, h, v), outer(hb[b], hb[a], v),
                      outer(hb[a], hb[b], v), outer(h, hab, v)), -ONE)
    return add(scale(outer(hb[a], r[b], v), -ONE),
               scale(outer(h, dk(r[b], a), v), -ONE), Hd(Fprime),
               scale(outer(L(hb[b], a), h, v), -ONE),
               scale(outer(L(h, a), hb[b], v), -ONE),
               outer(hb[b], Ladj(h, a), v), outer(h, Ladj(hb[b], a), v))


def ell(v, a):
    out = []
    for i in range(2):
        cos2ki = add(mul_scalar(cosK[a], trigq(a, 2)),
                     scale(mul_scalar(sinK[a], trigq(a, 2, sine=True)), -ONE if i == 0 else ONE))
        out.append(mul_scalar(cos2ki, hi(v, i)))
    return add(*out)


def constant(v):
    return {k: x for k, x in v.items() if k[0] == ZERO and x}


def assert_zero(v, label):
    global checks
    got = constant(v)
    assert not got, (label, list(got.items())[:3])
    checks += 1
    print(label, "exact zero", flush=True)


def phase(n):
    out = {}
    for p in product(range(MAX + 1), repeat=3):
        if sum(p) <= MAX:
            x = ONE
            for j in range(3):
                x *= (I * n[j]) ** p[j] / QQ_I(factorial(p[j]))
            if x:
                out[(p, ZERO, 0)] = x
    return out


base = add(mul_scalar(trigq(0, 1, sine=True), {(ZERO, ZERO, 0): ONE}),
           mul_scalar(trigq(1, 2), c0),
           mul_scalar(trigq(2, 1, sine=True), {(ZERO, ZERO, 1): ONE, (ZERO, ZERO, 2): ONE}),
           c0)
psi = P(mul_scalar(phase((2, -1, 3)), base))
psi0 = P(base)
print("Exact Gaussian-rational algebra; 3D q Fourier modes; K jets through degree 2.", flush=True)
print("Half-angle (cos,sin) fixtures:", cs, flush=True)
for b in range(3):
    assert_zero(add(Jraw(psi, b), scale(J(psi, b), -ONE)), f"canonical current b={b}")
    assert_zero(add(Hd(J(psi, b)), scale(J(Hd(psi), b), -ONE), scale(A(psi, b), -ONE)),
                f"Hamiltonian-current coefficient b={b}")
for a in range(3):
    for b in range(3):
        # Nested commutators start from the local-density dipole, not (J5).
        left = scale(add(D(Jraw(psi, b), a), scale(Jraw(D(psi, a), b), -ONE)), -I)
        right = add(P(ell(P(psi), a)) if a == b else {}, A(dk(psi, a), b), B(psi, a, b))
        assert_zero(add(left, scale(right, -ONE)), f"full bracket a={a}, b={b}")

# The differential term has a nonzero exact witness. This is not a band test.
av = constant(A(psi0, 0))
norm2 = sum((conj(z) * z for z in av.values()), Z)
assert norm2 and norm2.y == 0 and norm2.x > 0
checks += 1
print("nonzero [H_D,J_0] finite-polynomial witness norm^2 =", norm2, flush=True)

# Integer envelope constants used after the exact analytic support argument.
aconst = F(7, 4) + F(2) + F(3, 2) + F(11, 4) + F(21, 8)
bconst = F(17) + F(39, 8) + F(5, 32)
assert aconst == F(85, 8) and aconst < 12
assert bconst == F(705, 32) and bconst < 24
checks += 2
print("A support-kernel coefficient:", aconst, "< 12")
print("B support-kernel coefficient for lambda<=1:", bconst, "< 24")

# The fixed smooth preparation uses a mollified product polynomial.
i0 = sum(F((-1)**j * __import__('math').comb(4, j) * 2, 2*j + 1) for j in range(5))
i1 = 16 * (F(2, 3) - F(4, 5) + F(2, 7))
assert i0 == F(256, 315) and i1 == F(256, 105) and i1/i0 == 3
assert 24*24*3 < (512/F(8))**2  # convolution norm loss < 1/8
assert 2*F(192, 7) + F(8, 3) < 60
checks += 3
print("one-dimensional preparation integrals:", i0, i1, "; derivative ratio = 3")
print("mollified K-envelope gives scaled derivative B_a < 60")

# Mixed-band small-total-energy test: exact symbolic leading coefficients.
# At q=(pi/4,0,0), K=(t,0,0): E=sqrt(2)sin(t/2),
# ell_x=-sqrt(2)sin(t)cos(t/2); (ell_x-E)/E -> -3.
from sympy import symbols as syms, sin, cos, sqrt, limit, pi
t = syms('t', positive=True)
energy = sqrt(2)*sin(t/2)
residual = -sqrt(2)*sin(t)*cos(t/2) - energy
assert limit(residual/t, t, 0) == -3/sqrt(2)
assert limit(residual/energy, t, 0) == -3
checks += 2
print("mixed-channel small-total-energy residual/t = -3/sqrt(2); residual/E = -3")
print("completed", checks, "exact assertion families", flush=True)
'''
print('BEGIN boost_current finite author evidence', flush=True)
exec(compile(_SOURCE_BOOST_CURRENT, 'boost_current_preserved_helper', 'exec'), {'__name__': '__main__', '__file__': __file__})

_SOURCE_AXIS_WITNESS = r'''"""Separate exact Pauli/integral check of the nonzero differential coefficient.

This uses polynomial circle moments rather than the Laurent/K-jet engine.
It remains author evidence and does not independently review the theorem.
"""
from math import factorial
import sympy as s

C, S = s.symbols('C S', real=True)
ss = s.symbols('s0:3', real=True)
cc = s.symbols('c0:3', real=True)
variables = (*ss, *cc)
I = s.I
pauli = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -I], [I, 0]]),
         s.Matrix([[1, 0], [0, -1]])]
eye = s.eye(2)
p1 = [s.kronecker_product(x, eye) for x in pauli]
p2 = [s.kronecker_product(eye, x) for x in pauli]
contact = s.Matrix([0, 1, -1, 0])/s.sqrt(2)


def avg(expr):
    poly = s.Poly(s.expand(expr), *variables)
    result = 0
    for power, coeff in poly.terms():
        factor = s.Integer(1)
        for j in range(3):
            m, n = power[j], power[j+3]
            if m % 2 or n % 2:
                factor = 0
                break
            m, n = m//2, n//2
            factor *= s.Rational(factorial(2*m)*factorial(2*n),
                                 4**(m+n)*factorial(m)*factorial(n)*factorial(m+n))
        result += coeff*factor
    return s.expand(result)


def inner(u, v):
    return avg((u.conjugate().T*v)[0])


def P(v):
    return s.expand(v-contact*inner(contact, v))


H = S*cc[0]*(p1[0]+p2[0]) + C*ss[0]*(p1[0]-p2[0])
H += sum((ss[j]*(p1[j]-p2[j]) for j in (1, 2)), s.zeros(4))
h = H*contact
hb = -S*ss[0]*p1[0]*contact
g = 2*S*C*(1-2*ss[0]**2)
r = g*contact


def Hd(v):
    return P(H*P(v))


def J(v):
    v = P(v)
    return P(g*v)-hb*inner(h, v)-h*inner(hb, v)


assert s.simplify(inner(h, h)-(2*C*C+4)) == 0
assert s.simplify(inner(hb, h)+C*S) == 0
assert all(s.simplify(x) == 0 for x in Hd(hb)-r/2)
assert inner(h, Hd(h)) == 0
actual = s.expand((contact.conjugate().T*(Hd(J(h))-J(Hd(h))))[0])
expected = 4*S*C*(ss[1]**2+ss[2]**2-2*ss[0]**2)
assert s.expand(actual-expected) == 0
assert s.expand(avg(actual*actual)-12*S*S*C*C) == 0
print('six exact identities from Pauli matrices and circle moments passed')
print('c* [H_D,J_b] h = 2 sin(K_b) (sin(q_j)^2+sin(q_k)^2-2 sin(q_b)^2)')
print('singlet-component squared norm = 3 sin(K_b)^2')
'''
print('BEGIN axis_witness finite author evidence', flush=True)
exec(compile(_SOURCE_AXIS_WITNESS, 'axis_witness_preserved_helper', 'exec'), {'__name__': '__main__', '__file__': __file__})

_SOURCE_BOOST_ROTATION = r'''"""Distinct exact finite controls for the authored boost/rotation probe.

SymPy differential-operator composition tests a universal local Pauli jet and
a separate four-dimensional abstract compression fixture. Neither is a
continuum packet simulation or independent scientific review. No author
boost/current helper is imported. Domain and support proofs remain analytic.
"""
import itertools
import json
import sympy as sp

I = sp.I
checks = 0


def check(name, condition, detail=None):
    global checks
    assert bool(condition), name
    checks += 1
    print(json.dumps({"check": name, "detail": detail}))


def mz(m):
    return all(sp.expand(x) == 0 for x in m)


def clean(op):
    return {key: value.applyfunc(sp.expand) for key, value in op.items()
            if not mz(value)}


def compose(a, b, variables):
    out = {}
    for alpha, left in a.items():
        for beta, right in b.items():
            for gamma in itertools.product(*(range(n+1) for n in alpha)):
                coeff = sp.prod(sp.binomial(n, k) for n, k in zip(alpha, gamma))
                derived = right
                for var, order in zip(variables, gamma):
                    derived = derived.diff(var, order)
                index = tuple(n-k+m for n, k, m in zip(alpha, gamma, beta))
                out[index] = out.get(index, sp.zeros(left.rows)) + coeff*left*derived
    return clean(out)


def difference(a, b):
    keys = set(a) | set(b)
    size = next(iter(a.values())).rows if a else next(iter(b.values())).rows
    return clean({key: a.get(key, sp.zeros(size))-b.get(key, sp.zeros(size))
                  for key in keys})


def comm(a, b, variables):
    return difference(compose(a, b, variables), compose(b, a, variables))


def compressed(op, p):
    return clean({key: p*value*p for key, value in op.items()})


def evaluated(op, substitutions):
    return clean({key: value.subs(substitutions) for key, value in op.items()})


sigma = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.diag(1, -1),
]
x = sp.symbols("x0:3", real=True)
s = sp.symbols("s0:3", real=True)
c = sp.symbols("c0:3", real=True)
eye = sp.eye(2)
zero = (0, 0, 0)
units = [tuple(int(a == j) for j in range(3)) for a in range(3)]

# This is the complete second Taylor jet of sin(k+x) at an arbitrary k.
# Mixed second derivatives vanish; sin and cos values may remain symbolic.
h = sum((sigma[j]*(s[j]+c[j]*x[j]-s[j]*x[j]**2/2)
         for j in range(3)), sp.zeros(2))
dipoles = [{zero: I*h.diff(x[a])/2, units[a]: I*h} for a in range(3)]
at_origin = dict.fromkeys(x, 0)
for a, b in itertools.combinations(range(3), 2):
    direct = evaluated(comm(dipoles[a], dipoles[b], x), at_origin)
    spin = sum((sp.LeviCivita(a, b, d)*sigma[d] for d in range(3)), sp.zeros(2))
    expected = {
        units[a]: s[b]*c[b]*eye,
        units[b]: -s[a]*c[a]*eye,
        zero: -I*c[a]*c[b]*spin/2,
    }
    check(f"Pauli_direct_dipole_commutator_{a}{b}",
          not difference(direct, expected))
    check(f"Pauli_second_derivatives_cancel_{a}{b}",
          all(sum(key) <= 1 for key in direct))
    check(f"Pauli_spin_omission_detected_{a}{b}",
          bool(difference(direct, {k: v for k, v in expected.items() if k != zero})))
    check(f"Pauli_spin_sign_flip_detected_{a}{b}",
          bool(difference(direct, {**expected, zero: -expected[zero]})))

# This fixture is abstract, not a four-site discretization of the Weyl walk.
# It realizes exactly the two contact blocks, with nonconstant complex h
# and a noncommuting Hermitian complementary block.
u, v = sp.symbols("u v", real=True)
variables = (u, v)
z2 = (0, 0)
e2 = [(1, 0), (0, 1)]
contact = sp.Matrix([1, 0, 0, 0])
p = sp.diag(0, 1, 1, 1)
hh = sp.Matrix([0, 1+u+v**2, I*(2+v+u**2), u*v-I*u])
bath = sp.Matrix([[u, 1+I*v, v],
                  [1-I*v, 2*v, u+v],
                  [v, u+v, -u]])
H = hh*contact.T+contact*hh.conjugate().T
H[1:4, 1:4] = bath
check("abstract_H_is_Hermitian", mz(H-H.conjugate().T))
ops = []
qops = []
for a, variable in enumerate(variables):
    ha = hh.diff(variable)
    L = sp.zeros(4)
    L[:, 0] = ha
    L[1:4, 1:4] = bath.diff(variable)/2
    check(f"abstract_dipole_symmetry_contract_{a}",
          mz(L+L.conjugate().T-H.diff(variable)))
    ops.append({e2[a]: I*H, z2: I*L})
    qops.append(ha*hh.conjugate().T+hh*ha.conjugate().T)

left = comm(compressed(ops[0], p), compressed(ops[1], p), variables)
free_compressed = compressed(comm(ops[0], ops[1], variables), p)
contact_difference = difference(left, free_compressed)
expected_contact = {e2[1]: qops[0], e2[0]: -qops[1]}
check("abstract_exact_full_compression_defect",
      not difference(contact_difference, expected_contact))
check("abstract_second_derivative_contact_terms_cancel",
      all(sum(key) <= 1 for key in contact_difference))
check("abstract_no_constant_contact_term", z2 not in contact_difference)
check("abstract_contact_derivative_is_nonzero", bool(contact_difference))
check("abstract_omitting_contact_derivative_detected",
      bool(difference(left, free_compressed)))
check("abstract_reversing_contact_sign_detected",
      bool(difference(contact_difference, {k: -m for k, m in expected_contact.items()})))
check("abstract_contact_coefficient_divergence_cancels",
      mz(qops[0].diff(v)-qops[1].diff(u)))
check("abstract_contact_annihilation",
      all(mz(q*contact) for q in qops))

# Every reflected cone changes the spin in the two-axis product indicated,
# while its sin*cos orbital coordinate has the ordinary offset sign.
for signs in itertools.product((-1, 1), repeat=3):
    for a, b in itertools.combinations(range(3), 2):
        direct_spin = I*((signs[a]*sigma[a])*(signs[b]*sigma[b]) -
                        (signs[b]*sigma[b])*(signs[a]*sigma[a]))*(-sp.Rational(1, 4))
        expected_spin = sum((sp.LeviCivita(a, b, d)*sigma[d]*signs[a]*signs[b]/2
                             for d in range(3)), sp.zeros(2))
        check(f"cone_spin_{signs}_{a}{b}", mz(direct_spin-expected_spin))
    check(f"cone_orbital_offset_sign_{signs}", all(sign**2 == 1 for sign in signs))

R = sp.Rational
check("free_K_coefficient_budget",
      R(1, 384)+R(9, 32) == R(109, 384) < R(1, 3))
check("free_q_coefficient_budget",
      R(2, 3)*R(3, 4)**3 + R(1, 2)*R(1, 4)**2*R(3, 4)
      == R(39, 128) < R(1, 3))
check("local_contact_Q_budget",
      R(1, 8)*R(3, 2)+3*R(3, 32) == R(15, 32))
check("original_radial_envelope_derivative_budget",
      R(1, 3)*R(36, 25)*16**2*96*512**2 == R(18, 25)*2**32 < 2**32)
check("positive_projector_q_derivative_budget",
      2*2**16+R(16, 3) < 2**18)
C = R(49, 128)+(120+2**19)/sp.Integer(3)
budget = 2*(C/4+(30+R(1, 64)+R(15, 32)*R(120, 16))/4)
check("explicit_rotation_norm_budget", budget < 2**17, str(budget))
pi = sp.pi
volume = 4*pi*(R(3, 4))**3/(3*(2*pi)**3)
check("normalized_origin_support_volume",
      sp.simplify(volume-R(9, 128)/pi**2) == 0)

# A periodic smooth singlet input cos(q_a) gives this nonperiodic chart output.
qa, qb = sp.symbols("qa qb", real=True)
chart_output = -I*(qa*sp.diff(sp.cos(qa), qb)-qb*sp.diff(sp.cos(qa), qa))
jump = sp.simplify(chart_output.subs(qb, pi)-chart_output.subs(qb, -pi))
check("ordinary_chart_face_trace_jump",
      sp.simplify(jump+2*pi*I*sp.sin(qa)) == 0 and jump != 0,
      str(jump))
print(f"TOTAL: PASS={checks} FAIL=0")
print("SCOPE: exact finite algebra and constant budgets; no analytic domain/packet proof, independent review, physical rotation representation or evolution theorem certified")
'''
print('BEGIN boost_rotation finite author evidence', flush=True)
exec(compile(_SOURCE_BOOST_ROTATION, 'boost_rotation_preserved_helper', 'exec'), {'__name__': '__main__', '__file__': __file__})

_SOURCE_INVERSE_ENERGY = r'''#!/usr/bin/env python3
"""Author consistency controls for the inverse-energy boost/current probe.

The exact moment calculation exercises the continuum proof's algebra. The
3-vector forcing calculation exercises Duhamel signs and all momentum
factors. It is a gapped auxiliary model, not a discretization or proof of the
excluded-walk continuum limit. No fitted constants or external data.
"""
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np
import scipy
import scipy.linalg as la
import sympy as sp

CURRENT_RANK_WEIGHT = sp.Rational(1)
DUHAMEL_SOURCE_SIGN = -1.0
DIFFERENTIATE_SOURCE_CLOCK = True


def require(condition, message):
    if not bool(condition):
        raise AssertionError(message)


def exact_controls():
    x, y, z = sp.symbols('x y z', real=True)
    eps2 = x + y + z
    circle = {0: sp.Rational(1), 1: sp.Rational(1, 2),
              2: sp.Rational(3, 8), 3: sp.Rational(5, 16)}

    def mean(polynomial):
        return sp.expand(sum(coef * circle[p[0]] * circle[p[1]] * circle[p[2]]
                             for p, coef in sp.Poly(polynomial, x, y, z).terms()))

    # H0 applied to multiplication and both canonical rank terms, with the
    # common factor c/sqrt(I0) suppressed. P then removes the mean singlet.
    before_P = 1 - 2*x + CURRENT_RANK_WEIGHT * (x + eps2/3)
    after_P = sp.expand(before_P - mean(before_P))
    expected = eps2/3 - x
    require(sp.simplify(after_P - expected) == 0,
            'canonical full-torus coupling polynomial')
    # A_b/K_b from B12, independently arranged by its four surviving actions
    # on zeta; no q derivative of zeta occurs.
    rank_normal_form = 1 - 2*x + (2*x-1)/2 + (4*eps2-6)/12
    require(sp.simplify(rank_normal_form - expected) == 0,
            'B12 coefficient agrees with bounded-current calculation')
    require(mean(expected) == 0, 'physical projection removes mean')
    require(mean(expected**2) == sp.Rational(1, 12),
            'exact squared coupling is 1/(12 I0)')
    require(mean(before_P) == 1, 'full-torus contact subtraction is retained')
    print(json.dumps({'control': 'canonical_coupling',
                      'before_P': str(sp.expand(before_P)),
                      'after_P': str(after_P),
                      'squared_polynomial_mean': str(mean(expected**2))}))

    # An exact normalizable compact C2 scalar envelope tests the integration
    # by parts lower bound, independently of the B25 envelope's construction.
    k = sp.symbols('k', real=True)
    p = (1-k*k)**3
    dilated = sp.diff(k*p, k)
    norm2 = sp.integrate(p*p, (k, -1, 1))
    pairing = sp.integrate(p*dilated, (k, -1, 1))
    derivative_norm2 = sp.integrate(dilated*dilated, (k, -1, 1))
    require(pairing == norm2/2, 'compact dilation pairing')
    require(derivative_norm2 >= norm2/4, 'dilation norm lower bound')
    M = sp.Rational(192, 7)
    c_value = sp.Rational(9, 16)
    c_derivative = sp.Rational(13, 8) + 9*M/16
    c_bracket = 16*c_value + 6*c_derivative
    require(c_bracket < 112, 'direct comparison residual constant')
    # 112 sqrt(6) tau <= 1/(16 sqrt(12) I0) for tau<=1/32768,
    # I0<=9/8. Squaring is legitimate because all quantities are positive.
    require((sp.Integer(1792)**2)*72*sp.Rational(9, 8)**2 < 32768**2,
            'small fixed scaled-time lower bound')
    Kscale, Qscale, pi = sp.symbols('Kscale Qscale pi', positive=True)
    require(sp.simplify((2*pi)**6*Kscale**(-6)*Kscale**3*Qscale**3/
                        (2*pi)**6).subs(Qscale, Kscale) == 1,
            'six-dimensional packet normalization')
    require(sp.Rational(3, 2)-1 == sp.Rational(1, 2),
            'inverse-energy contact amplitude power')
    require(sp.Rational(3, 2)-sp.Rational(1, 2) == 1,
            'relative-error threshold power')
    print(json.dumps({'control': 'normalization_and_dilation',
                      'compact_envelope_norm2': str(norm2),
                      'dilation_pairing': str(pairing),
                      'dilation_norm2': str(derivative_norm2),
                      'state_error_coefficient': str(c_value),
                      'derivative_error_coefficient': str(c_derivative),
                      'bracket_error_coefficient': str(c_bracket),
                      'tau_max': '1/32768'}))


Hstar = np.diag([0.0, 1.0, -2.0])
Bparts = np.array([
    [[1,0,0],[0,0,.5],[0,.5,0]],
    [[0,.5,0],[.5,0,0],[0,0,0]],
    [[0,0,.5],[0,1,0],[.5,0,0]],
], dtype=float)
h0 = np.array([1.0, 2.0, -1.0])
e0vec = np.array([1.0, 0.0, 0.0], dtype=complex)


def factors(lam, k):
    G = Hstar/lam + np.einsum('j,jab->ab', k, Bparts)
    h = h0 + lam*lam*k
    e = 1.5+k[1]/4+k[0]*k[2]/8
    de = np.array([k[2]/8, .25, k[0]/8])
    F = (2/math.pi)**.75 * np.exp(-np.dot(k, k))
    dF = -2*k*F
    return G, h, e, de, F, dF


def augmented(lam, k, tau, component):
    G, h, e, de, F, dF = factors(lam, k)
    matrix = np.zeros((4,4), complex)
    matrix[:3,:3] = G
    matrix[:3,3] = DUHAMEL_SOURCE_SIGN*h
    matrix[3,3] = e
    dm = np.zeros_like(matrix)
    dm[:3,:3] = Bparts[component]
    dm[component,3] = DUHAMEL_SOURCE_SIGN*lam*lam
    dm[3,3] = de[component] if DIFFERENTIATE_SOURCE_CLOCK else 0
    ev, dev = la.expm_frechet(-1j*tau*matrix, -1j*tau*dm)
    initial = np.array([0,0,0,F], complex)
    di = np.array([0,0,0,dF[component]], complex)
    return (ev@initial)[:3], (dev@initial+ev@di)[:3]


def spectral_forcing(lam, k, tau):
    # Direct integral of +i exp(-i(tau-s)G) h F exp(-i e s), using
    # Hermitian G diagonalization; independent of the augmented generator.
    G, h, e, _, F, _ = factors(lam, k)
    evals, vectors = la.eigh(G)
    d = evals-e
    response = np.empty(3, complex)
    near = np.abs(d) < 1e-10
    response[near] = 1j*tau*np.exp(-1j*tau*e)
    response[~near] = -np.exp(-1j*tau*e)*np.expm1(-1j*tau*d[~near])/d[~near]
    return F*vectors@(response*(vectors.conj().T@h))


def fixed_tau_limit(k, tau, component):
    _, _, e, de, F, dF = factors(0.125, k)
    b = k[0]
    db = 1.0 if component == 0 else 0.0
    d = e-b
    numerator = np.exp(-1j*b*tau)-np.exp(-1j*e*tau)
    response = numerator/d
    dn = -1j*tau*db*np.exp(-1j*b*tau)+1j*tau*de[component]*np.exp(-1j*e*tau)
    derivative = (dn*d-numerator*(de[component]-db))/(d*d)
    return F*response*e0vec, (dF[component]*response+F*derivative)*e0vec


def vector_controls():
    k = np.array([.12, -.08, .09])
    lam, tau, component = 1/64, .37, 1
    value, derivative = augmented(lam, k, tau, component)
    direct = spectral_forcing(lam, k, tau)
    step = 1e-4
    unit = np.eye(3)[component]
    values = [spectral_forcing(lam, k+j*step*unit, tau) for j in [-2,-1,1,2]]
    finite_difference = (values[0]-8*values[1]+8*values[2]-values[3])/(12*step)
    value_error = la.norm(value-direct)
    derivative_error = la.norm(derivative-finite_difference)
    require(value_error < 2e-12, 'positive contact Duhamel sign: actual vectors')
    require(derivative_error < 2e-9, 'all momentum derivative factors: actual vectors')
    print(json.dumps({'control': 'actual_forced_vector', 'lambda': lam,
                      'tau': tau, 'kappa': k.tolist(), 'derivative_component': component,
                      'augmented_value': [[float(x.real), float(x.imag)] for x in value],
                      'spectral_integral_error': float(value_error),
                      'frechet_vs_five_point_derivative_error': float(derivative_error)}))

    shorter, fixed = [], []
    _, _, _, _, F, dF = factors(.125, k)
    target = 1j*F*e0vec
    dtarget = 1j*dF[component]*e0vec
    fixed_tau = .125
    fixed_target, fixed_dtarget = fixed_tau_limit(k, fixed_tau, component)
    for exponent in [6, 8, 10, 12, 14, 16, 18]:
        lam = 2.0**(-exponent)
        tau = math.sqrt(lam)
        value, derivative = augmented(lam, k, tau, component)
        shorter.append({'lambda': lam, 'physical_t': 1/math.sqrt(lam),
                        'scaled_tau': tau,
                        'value_error': float(la.norm(value/tau-target)),
                        'derivative_error': float(la.norm(derivative/tau-dtarget))})
        value, derivative = augmented(lam, k, fixed_tau, component)
        fixed.append({'lambda': lam, 'scaled_tau': fixed_tau,
                      'value_error': float(la.norm(value-fixed_target)),
                      'derivative_error': float(la.norm(derivative-fixed_dtarget))})
    for row in shorter:
        print(json.dumps({'control': 'shorter_time_finite_model', **row}))
    for row in fixed:
        print(json.dumps({'control': 'fixed_tau_finite_model', **row}))
    require(shorter[-1]['value_error'] < .08*shorter[0]['value_error'],
            'shorter-time finite model resolves the kernel forcing')
    require(shorter[-1]['derivative_error'] < .08*shorter[0]['derivative_error'],
            'shorter-time finite model resolves the derivative')
    require(fixed[-1]['value_error'] < .01*fixed[0]['value_error'],
            'fixed-tau finite model resolves the forced kernel limit')
    require(fixed[-1]['derivative_error'] < .01*fixed[0]['derivative_error'],
            'fixed-tau finite model resolves the derivative')
    print(json.dumps({'scope': 'gapped three-vector model only; no continuum rate or theorem is inferred',
                      'status': 'all author consistency controls completed'}))


if __name__ == '__main__':
    own = Path(__file__).resolve()
    print(json.dumps({'script': str(own), 'sha256': hashlib.sha256(own.read_bytes()).hexdigest(),
                      'python': sys.version, 'executable': sys.executable,
                      'platform': platform.platform(), 'numpy': np.__version__,
                      'scipy': scipy.__version__, 'sympy': sp.__version__,
                      'evidence_role': 'author consistency; independent scientific review pending'}))
    exact_controls()
    vector_controls()
'''
print('BEGIN inverse_energy finite author evidence', flush=True)
exec(compile(_SOURCE_INVERSE_ENERGY, 'inverse_energy_preserved_helper', 'exec'), {'__name__': '__main__', '__file__': __file__})

_SOURCE_KERNEL_BOUND = r'''#!/usr/bin/env python3
"""Author arithmetic control; analytic sine chord and radial proof are in note."""
import hashlib
import json
from pathlib import Path
import sympy as s
own=Path(__file__).resolve()
R=s.pi*s.sqrt(3)/2
coefficient=s.simplify(8/(4*(2*s.pi)**3) * s.pi**2/4)
bound=s.simplify(coefficient*4*s.pi*R)
assert coefficient==1/(16*s.pi)
assert bound==s.pi*s.sqrt(3)/8
# pi<4 and sqrt(3)<2 already give this bound<1<9/8.
assert 3<2**2
assert s.Rational(4*2,8)==1<s.Rational(9,8)
print(json.dumps({'script':str(own),'sha256':hashlib.sha256(own.read_bytes()).hexdigest(),'folded_integral_coefficient':str(coefficient),'ball_radius':str(R),'upper_bound':str(bound),'lower_bound':'1/12','retained_coarse_upper_bound':'9/8','role':'author exact arithmetic only; analytic inequalities and kernel completeness proved in note','status':'completed'}))
'''
print('BEGIN kernel_bound finite author evidence', flush=True)
exec(compile(_SOURCE_KERNEL_BOUND, 'kernel_bound_preserved_helper', 'exec'), {'__name__': '__main__', '__file__': __file__})

print("per_element: exact Pauli, Fourier-coefficient and finite contact algebra checked; no continuum state-space exhaustion")
print("per_site: checked and not executed — these author helpers use Fourier and abstract compression, not infinite-site simulation")
print("per_mode: all eight reflected-corner sign patterns and finite Fourier modes checked; the continuum packet limits remain analytic")
print("per_block: full nine boost/current components and three boost/boost component pairs checked in the stated finite fixtures")
print("lattice_wide: checked and not executed — global analytic domain and prepared-packet bounds require the complete source proofs")
print("TOTAL: PASS=5 FAIL=0")
print("SCOPE: five preserved author-control modules, including 23 boost/current, 6 axis and 63 rotation checks plus forcing and integral controls; no count certifies the continuum proofs")
