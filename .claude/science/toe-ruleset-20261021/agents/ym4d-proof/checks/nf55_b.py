# nf55_b -- normalisation chain e ~ F^aF^a/(2u) and the witness's expected amplitude (criteria: nf55_b_criteria.md).
# Exact symbolic arithmetic (sympy); pi symbolic. No floats.
import sympy as sp
res = {}
th = sp.symbols('theta', positive=True)
# B0: SU(2), X = theta n.sigma/2 ; Re tr(1 - exp(iX)) = 2(1 - cos(theta/2)) ; tr X^2 = theta^2/2
lhs = sp.series(2*(1 - sp.cos(th/2)), th, 0, 4).removeO()
rhs = (th**2/2)/2
res['B0'] = sp.simplify(lhs.coeff(th, 2) - rhs.coeff(th, 2)) == 0
print("B0: theta^2 coefficients", lhs.coeff(th, 2), rhs.coeff(th, 2), res['B0'])
# B1: u * sum_{mu<nu} s(U_p)/a^4 = (1/4) sum_{mu,nu} F^2 ; s = a^4 g^2 sum_a (F^a_{mu nu})^2/(4N)
N, g, a = sp.symbols('N g a', positive=True)
F = {}
for c in range(2):
    for m in range(4):
        for n in range(4):
            if m < n:
                F[(c, m, n)] = sp.Symbol('F%d_%d%d' % (c, m, n))
def Fv(c, m, n):
    if m == n: return 0
    return F[(c, m, n)] if m < n else -F[(c, n, m)]
s_p = lambda m, n: a**4*g**2*sum(Fv(c, m, n)**2 for c in range(2))/(4*N)
quarterF2 = sp.Rational(1, 4)*sum(Fv(c, m, n)**2 for c in range(2) for m in range(4) for n in range(4))
u = 2*N/g**2
d1 = sp.simplify(u*sum(s_p(m, n) for m in range(4) for n in range(4) if m < n)/a**4 - quarterF2)
res['B1'] = (d1 == 0)
d1f = sp.simplify((1/g**2)*sum(s_p(m, n) for m in range(4) for n in range(4) if m < n)/a**4 - quarterF2)
res['B1-F'] = (d1f != 0)
print("B1: difference", d1, res['B1'], "| B1-F (u=1/g^2) difference nonzero:", res['B1-F'])
# B2: e = (4a^4)^-1 sum_{mu != nu} 4 s(U_p) == (1/(2u)) sum_{mu,nu} F^aF^a
e = sum(4*s_p(m, n) for m in range(4) for n in range(4) if m != n)/(4*a**4)
FF = sum(Fv(c, m, n)**2 for c in range(2) for m in range(4) for n in range(4))
d2 = sp.simplify(e - FF/(2*u))
res['B2'] = (d2 == 0)
print("B2: difference", d2, res['B2'])
# B3: Theta/e with Theta = (beta/(2g)) FF, beta = -b0 g^3, b0 = 11N/(48 pi^2)
b0 = 11*N/(48*sp.pi**2)
Theta = (-b0*g**3/(2*g))*FF
ratio = sp.simplify(Theta/e)
res['B3'] = sp.simplify(ratio + 11*N**2/(24*sp.pi**2)) == 0
print("B3: Theta/e =", ratio, res['B3'])
# B4: (1/(2u))^2 * 48 (N^2-1)/pi^4 == 12 (N^2-1)/(pi^4 u^2)
U = sp.Symbol('U', positive=True)
res['B4'] = sp.simplify((1/(2*U))**2*48*(N**2 - 1)/sp.pi**4 - 12*(N**2 - 1)/(sp.pi**4*U**2)) == 0
print("B4:", res['B4'])
ok = all(res[k] for k in ['B0', 'B1', 'B2', 'B3', 'B4']) and res['B1-F']
print("RESULTS:", res)
print("VERDICT:", "PASS" if ok else "FAIL")
