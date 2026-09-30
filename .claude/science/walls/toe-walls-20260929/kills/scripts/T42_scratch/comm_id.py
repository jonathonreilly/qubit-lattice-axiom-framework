"""Check: the T-odd licensed plaquette operator {sin(Theta_P), circulation of E} is a commutator with H_E,
i.e. i[H_E, cos Theta_P] = -(1/2){sin Theta_P, sum_l s_l E_l}  (U(1), E_l = -i d/d theta_l)."""
import sympy as sp
th = sp.symbols('t1:5', real=True)
s = [1, 1, -1, -1]
Th = sum(si*ti for si, ti in zip(s, th))
psi = sp.Function('psi')(*th)
E = lambda l, f: -sp.I*sp.diff(f, th[l])
HE = lambda f: sp.Rational(1, 2)*sum(E(l, E(l, f)) for l in range(4))
lhs = sp.I*(HE(sp.cos(Th)*psi) - sp.cos(Th)*HE(psi))
circ = lambda f: sum(s[l]*E(l, f) for l in range(4))
rhs = -sp.Rational(1, 2)*(sp.sin(Th)*circ(psi) + circ(sp.sin(Th)*psi))
print("identity holds:", sp.simplify(sp.expand(lhs - rhs)) == 0)
