# s2_55_1b -- classical sign of the right half of Xi_v (criteria: s2_55_1b_criteria.md, written first). sympy exact.
import sympy as sp
I = sp.I
t = sp.symbols('t', real=True)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def H(M): return M.conjugate().T
def pi_proj(M):
    A = (M - H(M)) / 2
    return A - (A.trace() / M.shape[0]) * sp.eye(M.shape[0])
def ah(a1, a2, a3): return I * (sp.Rational(a1) * sig[0] + sp.Rational(a2) * sig[1] + sp.Rational(a3) * sig[2])
def expser(A, order=5):
    Mt = sp.eye(2); term = sp.eye(2)
    for n in range(1, order + 1):
        term = term * (t * A) / n; Mt = Mt + term
    return Mt.applyfunc(sp.expand)
def trunc(M, order=3):
    return M.applyfunc(lambda z: sum(sp.expand(z).coeff(t, k) * t**k for k in range(order + 1)))
ok, fired = [], []
for (A, Bp, Bm) in [(ah(1, 2, -1), ah(sp.Rational(1, 2), -3, 2), ah(0, 1, 1)),
                    (ah(3, 0, 1), ah(-1, 1, 1), ah(2, -1, 0)),
                    (ah(sp.Rational(2, 3), 1, 0), ah(0, -2, sp.Rational(5, 4)), ah(1, 1, -1))]:
    U, Wp, Wm = expser(A), expser(Bp), expser(Bm)
    Uinv, Wpinv, Wminv = expser(-A), expser(-Bp), expser(-Bm)
    xi = trunc(-(pi_proj(U * Wp) - pi_proj(U * Wm)) / 2)
    Qp, Qm = Uinv * Wpinv, Uinv * Wminv
    for sign, store in ((-1, ok), (+1, fired)):
        xit = trunc(-sign * (pi_proj(Qp) - pi_proj(Qm)) / 2)
        d = trunc(xi - U * xit * Uinv)
        c0 = d.applyfunc(lambda z: sp.simplify(sp.expand(z).coeff(t, 0)))
        c1 = d.applyfunc(lambda z: sp.simplify(sp.expand(z).coeff(t, 1)))
        nonvac = xi.applyfunc(lambda z: sp.simplify(sp.expand(z).coeff(t, 1))) != sp.zeros(2)
        if sign == -1:
            store.append(c0 == sp.zeros(2) and c1 == sp.zeros(2) and nonvac)
        else:
            store.append(c1 != sp.zeros(2))
print('D1', 'PASS' if all(ok) else 'FAIL')
print('D1x', 'FIRED' if all(fired) else 'DID-NOT-FIRE')
print('VERDICT:', 'PASS' if all(ok) and all(fired) else 'FAIL')
