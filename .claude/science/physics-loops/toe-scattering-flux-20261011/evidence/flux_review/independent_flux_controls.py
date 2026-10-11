"""Selective root checks, constructed independently of the author's helper.

Exact finite algebra only. This does not certify stationary phase, a continuum
principal value, an infinite-volume limit, or a finite-beam/plane-wave limit.
"""
import sympy as s

I = s.I
R = s.Rational


def exact(label, left, right):
    delta = left - right
    terms = list(delta) if isinstance(delta, s.MatrixBase) else [delta]
    assert all(s.simplify(t) == 0 for t in terms), label
    print("PASS", label)


pauli = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]
n1, n2 = [R(3, 5), 0, R(4, 5)], [0, R(5, 13), R(12, 13)]
projectors = [(s.eye(2) + sum((n[j] * pauli[j] for j in range(3)), s.zeros(2))) / 2
              for n in (n1, n2)]
projector = s.kronecker_product(*projectors)
u = s.Matrix([15, 3*I, 5, I]) / s.sqrt(260)
c = s.Matrix([0, 1, -1, 0]) / s.sqrt(2)
swap = s.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                 [0, 1, 0, 0], [0, 0, 0, 1]])
w = (c.H * projector * c)[0]
exact("nonparallel Pauli band projector", projector, u * u.H)
exact("singlet band weight", w, R(17, 260))
exact("swap singlet sign", swap*c, -c)
phases = [1, I, -1, -I]
paired = [(z*u-s.conjugate(z)*swap*u)/s.sqrt(2) for z in phases]
exact("paired plane phase-average density", sum((p.H*p)[0] for p in paired)/4, 1)
origin = paired[0]
exact("paired contact intensity", (c.H*origin)[0]*s.conjugate((c.H*origin)[0]), 2*w)
assert s.simplify((origin.H*origin)[0] - 1) != 0
print("PASS general-K density is a mean, not a pointwise normalization")

# A nonuniform three-channel fixture avoids relying on eight equal weights.
prob = [R(1, 2), R(1, 3), R(1, 6)]
v = s.Matrix([s.sqrt(p) for p in prob])
phase = R(3, 5)-R(4, 5)*I
S = s.eye(3)+(phase-1)*(v*v.H)
QA, QB = s.diag(1, 1, 0), s.diag(0, 0, 1)
massA, massB = sum(prob[:2]), prob[2]
chi = QA*v/s.sqrt(massA)
out = S*chi
exact("nonuniform rank-one unitarity", S.H*S, s.eye(3))
phase_change_sq = (phase-1)*s.conjugate(phase-1)
exact("actual disjoint-detector probability", (out.H*QB*out)[0], phase_change_sq*massA*massB)
exact("same-detector interference and normalization", (out.H*QA*out)[0], 1-phase_change_sq*massA*massB)
exact("pure contact receives phase only", S*v, phase*v)
exact("pure-contact probabilities unchanged", (S*v).H*QB*(S*v), v.H*QB*v)
assert s.simplify(((S*v-v).H*(S*v-v))[0]) != 0
print("PASS state difference need not be detector redistribution")

# Limiting ellipsoid formulas and the exact angular antiderivative.
D, e, A, z, kap = s.symbols("D e A z kap", positive=True)
gamma = D+kap**2*z**2
vin = s.symbols("vin", positive=True)
gamma_in = s.symbols("gamma_in", positive=True)
speed = 2*s.sqrt(gamma)/e
weight = gamma/(2*e**2)
curvature = 4*gamma**2/(D**2*e**2)
flux = 2*weight/(s.pi**2*speed*curvature)
exact("scaled outgoing angular flux", flux, D**2*e/(8*s.pi**2*gamma**s.Rational(3, 2)))
win = gamma_in/(2*e**2)
vin = 2*s.sqrt(gamma_in)/e
cross = 4*win*weight/(s.pi**2*vin*speed*curvature*A**2)
exact("scaled paired cross section", cross,
      D**2*s.sqrt(gamma_in)/(16*s.pi**2*A**2*gamma**s.Rational(3, 2)))
exact("angular normalization antiderivative",
      s.diff(z/(D*s.sqrt(gamma)), z), gamma**(-s.Rational(3, 2)))
angular = 2*s.pi*(1/(D*s.sqrt(D+kap**2)) - (-1/(D*s.sqrt(D+kap**2))))
exact("full angular integral after e-squared relation", angular.subs(D+kap**2, e**2), 4*s.pi/(D*e))
exact("integrated scaled flux", (D**2*e/(8*s.pi**2))*(4*s.pi/(D*e)), D/(2*s.pi))
I0 = s.symbols("I0", positive=True)
threshold = (D*s.sqrt(gamma_in)/(4*s.pi*e*A**2)).subs({D:e**2, gamma_in:e**2, A:e*I0})
exact("K-zero finite threshold cross section", threshold, 1/(4*s.pi*I0**2))
print("Scope: exact finite algebra and coefficient reconstruction; analytic limits reviewed separately.")
