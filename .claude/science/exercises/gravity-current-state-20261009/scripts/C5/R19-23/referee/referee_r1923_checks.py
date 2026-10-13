"""Independent symbolic checks for C5 R19-23.

This file deliberately does not import kernels.py or any r1923_* module.
It uses the standard Fierz-Pauli/linearized-Einstein Hessian directly.
"""

import sympy as sp


def multiplicities(char_rep, class_sizes, irreps):
    order = sum(class_sizes)
    return {
        name: sum(n * a * b for n, a, b in zip(class_sizes, char_rep, chars)) // order
        for name, chars in irreps.items()
    }


# Character order: E, 2C4, C2, 2 sigma_v, 2 sigma_d.
C4V_SIZES = [1, 2, 1, 2, 2]
C4V = {
    "A1": [1, 1, 1, 1, 1],
    "A2": [1, 1, 1, -1, -1],
    "B1": [1, -1, 1, 1, -1],
    "B2": [1, -1, 1, -1, 1],
    "E": [2, 0, -2, 0, 0],
}
axis_h = multiplicities([10, 2, 2, 4, 4], C4V_SIZES, C4V)
axis_gauge = multiplicities([4, 2, 0, 2, 2], C4V_SIZES, C4V)
assert axis_h == {"A1": 4, "A2": 0, "B1": 1, "B2": 1, "E": 2}
assert axis_gauge == {"A1": 2, "A2": 0, "B1": 0, "B2": 0, "E": 1}

# Character order: E, C2, sigma_v, sigma_v'.
C2V_SIZES = [1, 1, 1, 1]
C2V = {
    "A1": [1, 1, 1, 1],
    "A2": [1, 1, -1, -1],
    "B1": [1, -1, 1, -1],
    "B2": [1, -1, -1, 1],
}
face_h = multiplicities([10, 2, 4, 4], C2V_SIZES, C2V)
face_gauge = multiplicities([4, 0, 2, 2], C2V_SIZES, C2V)
assert face_h == {"A1": 5, "A2": 1, "B1": 2, "B2": 2}
assert face_gauge == {"A1": 2, "A2": 0, "B1": 1, "B2": 1}


eta = sp.diag(-1, 1, 1, 1)


def eh_bilinear(h, k, p):
    """Standard linearized-Einstein Hessian, normalized to e K e=w^2-q^2."""
    ans = 0
    for m in range(4):
        for n in range(4):
            if h[m, n] == 0:
                continue
            for r in range(4):
                for s in range(4):
                    if k[r, s] == 0:
                        continue
                    kab = 0
                    for A in range(4):
                        for B in range(4):
                            pa = [eta[A, j] for j in range(4)]
                            pb = [eta[B, j] for j in range(4)]
                            z = sp.Rational(1, 2) * (
                                eta[m, r] * eta[n, s] + eta[m, s] * eta[n, r]
                            ) * eta[A, B]
                            z -= sp.Rational(1, 2) * (
                                pa[m] * pb[r] * eta[n, s]
                                + pa[m] * pb[s] * eta[n, r]
                                + pa[n] * pb[r] * eta[m, s]
                                + pa[n] * pb[s] * eta[m, r]
                            )
                            z += pa[m] * pb[n] * eta[r, s] + pa[r] * pb[s] * eta[m, n]
                            z -= eta[m, n] * eta[r, s] * eta[A, B]
                            kab += z * p[A] * p[B]
                    ans += h[m, n] * kab * k[r, s]
    return sp.factor(-sp.Rational(1, 2) * ans)


def sym_outer(a, b):
    return a * b.T + b * a.T


rt2 = sp.sqrt(2)
t = sp.Matrix([1, 0, 0, 0])
n = sp.Matrix([0, 1 / rt2, 1 / rt2, 0])
a = sp.Matrix([0, 1 / rt2, -1 / rt2, 0])
b = sp.Matrix([0, 0, 0, 1])
face1 = a * a.T - b * b.T
face2 = a * b.T + b * a.T

# At the face light cone, the EH null block is face1 plus two A1 gauge vectors.
w = sp.symbols("w", positive=True)
p_face = sp.Matrix([w, 1 / rt2, 1 / rt2, 0])
g0 = sym_outer(p_face.subs(w, 1), t)
gn = sym_outer(p_face.subs(w, 1), n)
null_basis = [face1, g0, gn]
K0 = sp.Matrix(
    [[eh_bilinear(x, y, p_face).subs(w, 1) for y in null_basis] for x in null_basis]
)
D = sp.Matrix(
    [
        [sp.diff(eh_bilinear(x, y, p_face), w).subs(w, 1) / 2 for y in null_basis]
        for x in null_basis
    ]
)
assert K0 == sp.zeros(3)
assert D == sp.diag(1, 0, 0)

# Generic leading-order degenerate perturbation: det(delta*D-P)=0 gives a Schur complement.
P = sp.Matrix([[2, 1, -1], [1, 3, 1], [-1, 1, 2]])
PGG = P[1:, 1:]
schur = sp.factor(P[0, 0] - (P[0, 1:] * PGG.inv() * P[1:, 0])[0])
delta = sp.symbols("delta")
assert sp.factor((delta * D - P).det()) == sp.factor(PGG.det() * (delta - schur))

# One isolated pole, including the exact wave-function denominator.
eps, q, mu, bw, bq = sp.symbols("eps q mu bw bq")
omega2_exact = sp.factor((eps * mu + (1 + eps * bq) * q**2) / (1 - eps * bw))
mass2_exact = sp.factor(omega2_exact.subs(q, 0))
speed2_exact = sp.factor(sp.diff(omega2_exact, q, 2) / 2)
assert sp.series(mass2_exact, eps, 0, 3).removeO() == eps * mu + eps**2 * bw * mu
assert sp.series(speed2_exact, eps, 0, 2).removeO() == 1 + eps * (bw + bq)


# Solid kernel: bulk plus cubic E and T2 shear projectors, with no h_0mu terms.
lb, mE, mT = sp.symbols("lb mE mT")


def solid_bilinear(h, k):
    trh = sum(h[i, i] for i in (1, 2, 3))
    trk = sum(k[i, i] for i in (1, 2, 3))
    dh = [h[i, i] - trh / 3 for i in (1, 2, 3)]
    dk = [k[i, i] - trk / 3 for i in (1, 2, 3)]
    off = sum(h[i, j] * k[i, j] for i in (1, 2, 3) for j in (1, 2, 3) if i != j)
    return sp.factor(lb * trh * trk + mE * sum(x * y for x, y in zip(dh, dk)) / 2 + mT * off / 2)


def mat(entries):
    h = sp.zeros(4)
    for i, j, value in entries:
        h[i, j] = value
        h[j, i] = value
    return h


w, q, eps = sp.symbols("w q eps", nonzero=True)
p_axis = sp.Matrix([w, 0, 0, q])
h0x = mat([(0, 1, 1)])
hxz = mat([(1, 3, 1)])
h0z = mat([(0, 3, 1)])
hzz = sp.diag(0, 0, 0, 1)
htt = sp.diag(0, 1, 1, 0)
h00 = sp.diag(1, 0, 0, 0)
Eg = sp.diag(0, 1, -1, 0)
T2 = mat([(1, 2, 1)])


def Qsolid(h, k):
    return sp.factor(eh_bilinear(h, k, p_axis) - eps * solid_bilinear(h, k))


vector = sp.Matrix([[Qsolid(x, y) for y in (h0x, hxz)] for x in (h0x, hxz)])
# h00=0 fixes the residual xi0 symmetry for nonzero frequency.
scalar_fixed = sp.Matrix([[Qsolid(x, y) for y in (h0z, hzz, htt)] for x in (h0z, hzz, htt)])
assert sp.factor(vector.det()) == -eps * mT * q**2
assert sp.factor(scalar_fixed.det()) == 4 * eps * q**2 * w**2 * (3 * lb + mE) / 3
assert Qsolid(Eg, Eg) == w**2 - q**2 - eps * mE
assert Qsolid(T2, T2) == w**2 - q**2 - eps * mT

# Static mass and transverse-light amplitudes.  The exact axis ratios are analytic.
static_basis = (h00, hzz, htt)
static_Q = sp.Matrix(
    [[Qsolid(x, y).subs(w, 0) for y in static_basis] for x in static_basis]
)
source_mass = sp.Matrix([1, 0, 0])
source_light_x = sp.Matrix([1, 0, 1])
static_inverse = static_Q.inv()
U_mm = sp.factor((source_mass.T * static_inverse * source_mass)[0])
U_ml = sp.factor((source_mass.T * static_inverse * source_light_x)[0])
R_mm = sp.factor(U_mm / (-1 / q**2))
R_ml = sp.factor(U_ml / (-2 / q**2))
assert sp.simplify(R_mm - (1 - 9 * eps * lb * mE / (q**2 * (3 * lb + mE)))) == 0
assert sp.simplify(sp.limit(R_mm, eps, 0) - 1) == 0
assert sp.simplify(sp.limit(R_ml, eps, 0) - 1) == 0
assert sp.factor(R_mm.subs(lb, 0)) == 1


# Counterexample to "speed-row violation always propagates pi0".
# K_ii = omega*h_ii - 2*q_i*h_0i is spatial-diffeomorphism invariant.
c = sp.symbols("c", nonzero=True)


def kdiag_bilinear(h, k):
    kh = [w * h[1, 1], w * h[2, 2], w * h[3, 3] - 2 * q * h[0, 3]]
    kk = [w * k[1, 1], w * k[2, 2], w * k[3, 3] - 2 * q * k[0, 3]]
    return c * sum(x * y for x, y in zip(kh, kk))


row_pattern = [
    sp.factor(kdiag_bilinear(Eg, Eg) / (2 * c * w**2)),
    sp.factor(kdiag_bilinear(T2, T2) / (2 * c * w**2)),
    sp.factor(kdiag_bilinear(face1, face1) / (2 * c * w**2)),
    sp.factor(kdiag_bilinear(face2, face2) / (2 * c * w**2)),
]
assert row_pattern == [1, 0, sp.Rational(3, 4), 0]

pure_xi0 = sym_outer(sp.Matrix([w, 0, 0, q]), t)
assert sp.factor(kdiag_bilinear(pure_xi0, pure_xi0)) == 4 * c * q**4


def Qcounter(h, k):
    return sp.factor(
        eh_bilinear(h, k, p_axis) - eps * (solid_bilinear(h, k) + kdiag_bilinear(h, k))
    )


scalar_full = sp.Matrix(
    [[Qcounter(x, y) for y in (h00, h0z, hzz, htt)] for x in (h00, h0z, hzz, htt)]
)
assert sp.factor(scalar_full.det()) == -4 * c * eps**2 * q**6 * (3 * lb + mE) / 3

# A generic leading Goldstone pencil can instead yield omega^2 proportional to q.
A, B, C, E = sp.symbols("A B C E", nonzero=True)
goldstone = sp.Matrix([[B * w**2 * q**2, C * w**3 * q], [C * w**3 * q, A * q**2 + E * w**4]])
goldstone_det = sp.factor(goldstone.det())
assert sp.simplify(goldstone_det - q**2 * w**2 * (A * B * q**2 + (B * E - C**2) * w**4)) == 0


print("axis h irreps:", axis_h)
print("axis gauge irreps:", axis_gauge)
print("face h irreps:", face_h)
print("face gauge irreps:", face_gauge)
print("face null-block dK/d(omega^2):", D.tolist())
print("face Schur example:", schur)
print("isolated exact mass^2:", mass2_exact)
print("isolated exact c^2:", speed2_exact)
print("solid vector determinant:", sp.factor(vector.det()))
print("solid scalar determinant after xi0 gauge fixing:", sp.factor(scalar_fixed.det()))
print("solid TT factors:", Qsolid(Eg, Eg), ";", Qsolid(T2, T2))
print("static U_mm/U_GR:", R_mm)
print("static U_ml/U_GR:", R_ml)
print("auxiliary speed-row counterexample:", row_pattern)
print("pure-pi0 form of counterexample:", sp.factor(kdiag_bilinear(pure_xi0, pure_xi0)))
print("counterexample scalar determinant:", sp.factor(scalar_full.det()))
print("generic Goldstone determinant:", goldstone_det)
print("all independent symbolic checks: PASS")
