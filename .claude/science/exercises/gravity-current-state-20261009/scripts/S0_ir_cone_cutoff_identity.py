"""Step 3 'shrink': the smallest object in which the stiffness wall bites.

One massless field, vacuum energy E = s * (1/2) * sum_k omega(k) over a cutoff
window (s = +1 per bosonic mode, s = -2 for a two-component Weyl sea), in a
constant metric g = exp(-t*eps) with eps symmetric traceless (volume
preserving, det g = 1), so omega(k) = sqrt(k^T exp(t*eps) k).

  A: window fixed in label space  (|k| < K0)          -- a fixed-adjacency lattice
  B: window fixed in proper space (|g^{-1/2} k| < K0)  -- a cutoff that moves
     with the geometry; unit Jacobian since det g = 1.

Claim checked here (exact, sympy): d^2E/dt^2 at t=0 per unit tr(eps^2) is
  A: s * K0^4 / (240 pi^2) * 2  = s*K0^4/(120 pi^2)  [boson s=+1]
  B: 0
For a Weyl sea (s = -2) case A gives -K0^4/(60 pi^2), the value the W1
referee obtained independently. Exact, no lattice: it isolates the cutoff
geometry as the source of the transverse-traceless (TT) modulus.
"""
import sympy as sp

t, K0, k, th, ph = sp.symbols('t K0 k theta phi', positive=True)
# a traceless symmetric eps with tr(eps^2) = 1, generic orientation is not needed:
# the angular average of (n.eps.n)^2 over the sphere is 2 tr(eps^2)/15 for any
# traceless symmetric eps, and n.eps^2.n averages to tr(eps^2)/3.
n = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])


def angavg(expr):
    return sp.simplify(sp.integrate(sp.integrate(expr * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi))


def second_derivative_fixed_window(eps):
    # d^2/dt^2 sqrt(k^T e^{t eps} k) at t=0 = |k| [ n.eps^2.n / 2 - (n.eps.n)^2 / 4 ]
    a = (n.T * eps * eps * n)[0]
    b = (n.T * eps * n)[0]
    ang = angavg(a / 2 - b ** 2 / 4)
    radial = sp.integrate(k * k ** 2, (k, 0, K0)) * 4 * sp.pi / (2 * sp.pi) ** 3
    return sp.simplify(sp.Rational(1, 2) * ang * radial)


def check(eps, name):
    tr2 = sp.simplify((eps * eps).trace())
    epsn = eps / sp.sqrt(tr2)
    A = second_derivative_fixed_window(epsn)
    print(f"{name}: tr(eps^2) normalised to 1;  fixed label-space window: d2E/dt2 = {A}"
          f"  (= {sp.nsimplify(A / K0**4)} K0^4);  Weyl sea (x -2): {sp.simplify(-2 * A)}")
    return A


axis = sp.diag(1, -1, 0)
face = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
gen = sp.Matrix([[2, 1, 0], [1, -1, 3], [0, 3, -1]])
vals = [check(axis, 'axis (E_g)'), check(face, 'face (T_2g)'), check(gen, 'generic traceless')]
assert all(sp.simplify(v - vals[0]) == 0 for v in vals), 'isotropy of the IR-cone value failed'
assert sp.simplify(vals[0] - K0 ** 4 / (120 * sp.pi ** 2)) == 0
assert sp.simplify(-2 * vals[0] + K0 ** 4 / (60 * sp.pi ** 2)) == 0

# B: proper-space window. Change variables k = g^{1/2} p (unit Jacobian, det g = 1):
# omega = sqrt(k^T g^{-1} k) = |p|, window |p| < K0 -> E independent of t exactly.
p = sp.symbols('p', positive=True)
EB = sp.Rational(1, 2) * sp.integrate(p * p ** 2, (p, 0, K0)) * 4 * sp.pi / (2 * sp.pi) ** 3
print('proper-space window: E(t) =', sp.simplify(EB), '(no t dependence) -> d2E/dt2 = 0 exactly')
print('PASS: fixed label-space cutoff gives a nonzero, isotropic TT modulus K0^4/(120 pi^2) per bosonic mode;'
      ' a cutoff that follows the geometry gives 0.')
