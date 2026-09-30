"""Exact check of the cross-term lemma for the spin-1/2 (x taste) carrier.
U(k) = a + 2 p C(k) + 2 i sum_j sigma_j (x) Q sin k_j, with a,p,Q taste matrices (here a 2x2 taste block, generic complex).
U^dag U - I must vanish identically in x_j = cos k_j.  We extract the x1*x2 and x1^2 coefficients symbolically."""
import sympy as sp
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
m = 2                                   # taste dimension (any m works the same way; checked m=1,2)
def cmat(name):
    return sp.Matrix(m, m, lambda i, j: sp.Symbol(f'{name}{i}{j}r', real=True) + sp.I * sp.Symbol(f'{name}{i}{j}i', real=True))
a, p, Q = cmat('a'), cmat('p'), cmat('Q')
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
xs = [x1, x2, x3]
ys = [sp.Symbol(f'y{j}', real=True) for j in range(3)]
C = sum(xs)
kron = sp.kronecker_product
U = kron(sp.eye(2), a) + 2 * C * kron(sp.eye(2), p) + 2 * sp.I * sum((kron(sig[j], Q) * ys[j] for j in range(3)), sp.zeros(2 * m, 2 * m))
F = (U.H * U - sp.eye(2 * m))
tr = sp.expand(F.trace())
tr = sp.expand(tr.subs({ys[j]**2: 1 - xs[j]**2 for j in range(3)}))
tr = sp.expand(tr.subs({ys[j]**2: 1 - xs[j]**2 for j in range(3)}))
c12 = sp.Poly(tr, x1, x2, x3, *ys).coeff_monomial(x1 * x2)
c11 = sp.Poly(tr, x1, x2, x3, *ys).coeff_monomial(x1**2)
p_norm2 = sum(sp.Abs(p[i, j])**2 for i in range(m) for j in range(m))
Q_norm2 = sum(sp.Abs(Q[i, j])**2 for i in range(m) for j in range(m))
pn = sp.expand(sum(sp.re(p[i, j])**2 + sp.im(p[i, j])**2 for i in range(m) for j in range(m)))
Qn = sp.expand(sum(sp.re(Q[i, j])**2 + sp.im(Q[i, j])**2 for i in range(m) for j in range(m)))
print('coefficient of x1*x2 in tr(U^dag U - 1):  ', sp.simplify(c12 - 16 * pn) == 0, '  (= 16 ||p||_F^2 for 2x2 spin x taste m=2 -> 2*m*4... )')
print('   c12 - 8*2*||p||^2 =', sp.simplify(c12 - 16 * pn))
print('coefficient of x1^2 in tr(U^dag U - 1): c11 =', sp.simplify(c11), ';  expected 2*(4||p||^2 - ||Q||^2)*... -> check c11 - (16*pn/2... )')
print('   c11 - (8*pn - 8*Qn) =', sp.simplify(c11 - (8 * pn - 8 * Qn)), ' [tr over spin(2)x taste; 4||p||^2*2 - 4||Q||^2*2]')
