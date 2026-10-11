"""Independent finite reconstruction: a weighted three-channel S and a
14-point sphere design, not the author's polynomial integrator or quadrature.
No continuum threshold, coarea, or physical collision-clock certification.
"""
from itertools import product
import sympy as s
R, I = s.Rational, s.I


def exact(label, left, right):
    d = left-right
    terms = list(d) if isinstance(d, s.MatrixBase) else [d]
    assert all(s.simplify(x) == 0 for x in terms), label
    print("EXACT", label)


mu, w = [R(2), R(1), R(3)], [R(1, 3), R(2, 5), R(1, 4)]
rho = sum(x*y for x, y in zip(mu, w))
nu = [x*y/rho for x, y in zip(mu, w)]
v = s.Matrix([s.sqrt(x) for x in nu])
phase = R(3, 5)-R(4, 5)*I
S = s.eye(3)+(phase-1)*v*v.H
f, h = [R(1), R(-2), R(3)], [R(2), R(4), R(-1)]
Df = S.H*s.diag(*f)*S-s.diag(*f)
Dh = S.H*s.diag(*h)*S-s.diag(*h)


def cov(a, b):
    return sum(p*x*y for p, x, y in zip(nu, a, b))-sum(p*x for p, x in zip(nu, a))*sum(p*x for p, x in zip(nu, b))


# G=pi*rho*(2+i) enforces Im G=pi rho; hence pi*c_G=4/(5rho^2).
qpi = R(2, 5)/rho**2*sum(mu[a]*mu[b]*w[a]*w[b]*(f[b]-f[a])**2
                           for a in range(3) for b in range(3))
exact("independent three-channel flux/variance coefficient", qpi, R(4, 5)*cov(f, f))
exact("squared-norm spectral polynomial", Df**3, qpi*Df)
exact("opposite eigenvalues from zero trace", s.trace(Df), 0)
assert Df.rank() == 2 and qpi > 0
exact("Hilbert-Schmidt polarization", s.trace(Df*Dh), R(8, 5)*cov(f, h))
meanmu = sum(x*y for x, y in zip(mu, f))/sum(mu)
dist = sum(x*(y-meanmu)**2 for x, y in zip(mu, f))
assert R(4, 5)*min(w)/rho*dist <= qpi <= R(4, 5)*max(w)/rho*dist
print("EXACT nonuniform-measure coercivity bounds")

# Six axis points, each weight 1/15, and eight cube vertices, each 3/40.
# These weights reproduce every even second and fourth sphere moment.
design = []
for axis in range(3):
    for sign in (-1, 1):
        n = s.zeros(3, 1); n[axis] = sign
        design.append((n, R(1, 15)))
for signs in product((-1, 1), repeat=3):
    design.append((s.Matrix(signs)/s.sqrt(3), R(3, 40)))
exact("sphere-design normalization", sum(p for n, p in design), 1)
for i in range(3):
    exact(f"sphere-design second moment {i}", sum(p*n[i]**2 for n, p in design), R(1, 3))
    exact(f"sphere-design fourth moment {i}", sum(p*n[i]**4 for n, p in design), R(1, 5))
for i, j in ((0, 1), (0, 2), (1, 2)):
    exact(f"sphere-design crossed fourth moment {i},{j}", sum(p*n[i]**2*n[j]**2 for n, p in design), R(1, 15))

for vals in ([0, 0, 0], [R(1, 3), 0, 0], [R(1, 8), -R(1, 4), 0],
             [R(1, 8), -R(1, 4), R(1, 4)]):
    kap = s.Matrix(vals); k2 = kap.dot(kap)
    e = 2+k2/8; d = 2-k2/8; D = d*d
    L = (1-k2/16)*s.eye(3)+kap*kap.T/8
    B = (D*s.eye(3)+kap*kap.T)/4
    exact(f"rational ellipsoid square root {vals}", L*L, B)
    assert k2 <= e**2/16
    gammas = [(s.Matrix([-2*kap[i]*(L*n)[i]**2 for i in range(3)]), p)
              for n, p in design]
    mean = sum((p*g for g, p in gammas), s.zeros(3, 1))
    covariance = sum((p*g*g.T for g, p in gammas), s.zeros(3))-mean*mean.T
    target = s.Matrix(3, 3, lambda i, j: R(8, 45)*kap[i]*kap[j]*(3*B[i,j]**2-B[i,i]*B[j,j]))
    exact(f"full tensor from 14-point design {vals}", covariance, target)
    active = [i for i in range(3) if kap[i] != 0]
    assert covariance.rank() == len(active)
    if active:
        Binv = B.inv()
        eta = 1-sum(Binv[i,i]**2 for i in active)/sum(x*x for x in Binv)
        assert eta > 0
        diag = s.diag(*[x*x for x in kap])
        assert (covariance-D**2*eta*diag/30).is_positive_semidefinite
        assert (e**4*diag/30-covariance).is_positive_semidefinite
    print("EXACT active rank and quadratic bounds", len(active))

b, D = s.symbols("b D", positive=True)
B = (D*s.eye(3)+b*b*s.ones(3))/4
C = s.Matrix(3, 3, lambda i, j: R(8, 45)*b*b*(3*B[i,j]**2-B[i,i]*B[j,j]))
exact("diagonal-momentum longitudinal eigenvalue", C*s.ones(3, 1), b**6*s.ones(3, 1)/15)
z = s.Matrix([1, -1, 0])
exact("diagonal-momentum transverse eigenvalue", C*z, b*b*D*(D+2*b*b)*z/30)
print("Scope: exact finite coefficients and rank discriminators; analytic uniformity reviewed separately.")
