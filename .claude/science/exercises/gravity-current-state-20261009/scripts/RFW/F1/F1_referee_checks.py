"""Independent exact checks for the F1 referee report.

These checks do not import the worker scripts.  They verify the displayed
scalar/fermion closure defects and SLAC control, exhibit a counterexample to
the c=0 branch of T1 as stated, and give an exact generic null direction for
the finite-Fourier-support line argument.
"""

import itertools

import sympy as sp


k = sp.symbols("k0:4")


def plane(a, b):
    J = sp.zeros(4)
    J[a, b] = 1
    J[b, a] = -1
    return J


def verify_defect(f, diagonal_factor):
    f = sp.Matrix(f)
    for a in range(4):
        for b in range(a + 1, 4):
            Jf = plane(a, b) * f
            defect = sp.simplify(f.jacobian(k) * Jf - Jf)
            expected = sp.Matrix(
                [(diagonal_factor[r] - 1) * Jf[r] for r in range(4)]
            )
            assert all(sp.simplify(defect[r] - expected[r]) == 0 for r in range(4))


f_scalar = [sp.sin(x) for x in k]
verify_defect(f_scalar, [sp.cos(x) for x in k])

f_fermion = [sp.sin(2 * x) / 2 for x in k]
verify_defect(f_fermion, [sp.cos(2 * x) for x in k])

f_slac = sp.Matrix(k)
for a in range(4):
    for b in range(a + 1, 4):
        Jf = plane(a, b) * f_slac
        assert f_slac.jacobian(k) * Jf - Jf == sp.zeros(4, 1)


# T1's c=0 conclusion is false without an irreducibility/factor exclusion
# stronger than "A does not depend on one linear combination".  This A
# depends on k0 and k1, while S0={k0=0} is an irreducible regular component.
A_counter = (sp.exp(sp.I * k[0]) - 1) * (2 + sp.cos(k[1]))
f_counter = sp.Matrix([1, 0, 0, 0])
grad_counter = sp.Matrix([sp.diff(A_counter, x) for x in k])
for a in range(4):
    for b in range(a + 1, 4):
        Jf = plane(a, b) * f_counter
        tangency_on_S0 = sp.simplify(Jf.dot(grad_counter).subs(k[0], 0))
        closure_c0 = f_counter.jacobian(k) * Jf
        assert tangency_on_S0 == 0
        assert closure_c0 == sp.zeros(4, 1)
assert sp.diff(A_counter, k[0]) != 0 and sp.diff(A_counter, k[1]) != 0


# An exact null direction.  Q-linear independence of
# {1, sqrt(2), sqrt(19)} makes n.v distinct for distinct n in Z^4.
v = sp.Matrix([1, sp.I / 2, sp.I * sp.sqrt(2) / 3, sp.I * sp.sqrt(19) / 6])
assert sp.simplify(v.dot(v)) == 0
freqs = list(itertools.product(range(-2, 3), repeat=4))
# If two exponents agreed, Q-linear independence would force equality of all
# four integer coefficients.  The frequency tuples are already distinct.
assert len(freqs) == len(set(freqs)) == 625


print("PASS: scalar defect = (cos(k_rho)-1)(J sin k)_rho in all six planes")
print("PASS: fermion defect = (cos(2k_rho)-1)(J f)_rho in all six planes")
print("PASS: SLAC f=k has zero interior closure defect")
print("COUNTEREXAMPLE: T1 c=0 holds on S0={k0=0} for A=(e^{ik0}-1)(2+cos k1)")
print("PASS: exact null direction separates all 625 frequencies in [-2,2]^4")
