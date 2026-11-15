#!/usr/bin/env python3
# h2_55_c — obstruction examples: wrapped-normal monotonicity. Criteria: h2_55_c_criteria.md (written before this script).
import sympy as sp
res = []
def gate(n, ok, d=''):
    res.append(bool(ok)); print(('PASS' if ok else 'FAIL'), n, d)
def control(n, fired, d=''):
    res.append(bool(fired)); print(('FIRES' if fired else 'DOES-NOT-FIRE'), n, d)
x, y = sp.symbols('x y', real=True); v = sp.symbols('v', positive=True); n = sp.symbols('n', integer=True, positive=True)
gauss = sp.exp(-x**2/(2*v))/sp.sqrt(2*sp.pi*v)
Ecos = sp.simplify(sp.integrate(sp.cos(x)*gauss, (x, -sp.oo, sp.oo)))
gate('C1 E cos X = exp(-v/2); dE[B]/dv = exp(-v/2) > 0', sp.simplify(Ecos - sp.exp(-v/2)) == 0 and sp.simplify(sp.diff(2*(1 - Ecos), v) - sp.exp(-v/2)) == 0, f'{Ecos}')
control('C1-F wrong char. function exp(-v) disagrees', sp.simplify(Ecos - sp.exp(-v)) != 0)
c2a = sp.integrate(y**2, (y, -sp.pi, sp.pi))/(2*sp.pi)
c2b = sp.simplify(sp.integrate(y**2*sp.cos(n*y), (y, -sp.pi, sp.pi)))
gate('C2 int y^2/(2pi) = pi^2/3; int y^2 cos(ny) = 4 pi (-1)^n / n^2', sp.simplify(c2a - sp.pi**2/3) == 0 and sp.simplify(c2b - 4*sp.pi*(-1)**n/n**2) == 0, f'{c2b}')
c2b1 = sp.integrate(y**2*sp.cos(y), (y, -sp.pi, sp.pi))
control('C2-F claim 4 pi/n^2 (no sign) fails at n = 1', sp.simplify(c2b1 - 4*sp.pi) != 0, f'n=1 value {c2b1}')
ratio = sp.simplify(sp.exp(-(n+1)**2*v/2)/sp.exp(-n**2*v/2))
gate('C3 consecutive-term ratio = exp(-(2n+1)v/2) < 1', sp.simplify(ratio - sp.exp(-(2*n+1)*v/2)) == 0 and sp.ask(sp.Q.positive((2*n+1)*v/2)) is True, f'{ratio}')
ok4 = all(sp.sign(sp.exp(-vv/2) - sp.exp(-2*vv)) == 1 for vv in (sp.Rational(1,10), sp.Integer(1), sp.Integer(10)))
gate('C4 exp(-v/2) - exp(-2v) > 0 at v = 1/10, 1, 10 (exact sign)', ok4)
print('VERDICT:', 'PASS' if all(res) else 'FAIL')
