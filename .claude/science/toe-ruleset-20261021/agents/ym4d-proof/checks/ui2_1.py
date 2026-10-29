# ui2_1 — super-marginal EOM bubble integral (criteria: ui2_1_criteria.md, written before this script). Exact sympy only.
import sympy as sp
x, t, c, s = sp.symbols('x t c s', positive=True)
z = sp.symbols('z')
res = {}
def theta_int(num, r):
    """int_0^pi num(cos,sin)/(1+2 r cos+r^2)^2 dtheta, num even in theta, exact via residues (half of the 0..2pi contour)."""
    C = (z + 1/z)/2; S = (z - 1/z)/(2*sp.I)
    f = sp.together(num(C, S)/(1 + 2*r*C + r**2)**2/(sp.I*z))
    poles = [sp.Integer(0), -r if r < 1 else -1/r]
    tot = sum(sp.residue(f, z, p) for p in poles)
    return sp.nsimplify(sp.simplify(sp.pi*sp.I*tot))  # = (1/2)*2*pi*i*sum
# L1: Feynman parameters
D = x*(1 - x)
inner = sp.Rational(1, 4)*sp.pi**2*sp.integrate(t*t/(t + D)**4, (t, 0, sp.oo))
I1_R1 = sp.simplify(sp.integrate(sp.simplify(6*x*(1 - x)*inner), (x, 0, 1)))
res['L1'] = sp.simplify(I1_R1 - sp.pi**2/2) == 0
# L2(a): Gegenbauer orthogonality with weight sin^4 theta (c = cos theta)
th = sp.symbols('th')
okA = True
for n in range(0, 9):
    val = sp.integrate(sp.expand(sp.gegenbauer(n, 2, sp.cos(th))*sp.sin(th)**4), (th, 0, sp.pi))
    target = 3*sp.pi/8 if n == 0 else 0
    okA = okA and sp.simplify(val - target) == 0
res['L2a'] = okA
# L2(b): exact J(r) at sample radii
okB = True
for r in [sp.Rational(1, 2), sp.Rational(1, 3), sp.Integer(2), sp.Integer(3)]:
    J = theta_int(lambda C, S: S**4, r)
    target = 3*sp.pi/8 if r < 1 else 3*sp.pi/(8*r**4)
    okB = okB and sp.simplify(J - target) == 0
res['L2b'] = okB
rr = sp.symbols('rr', positive=True)
I1_R2 = sp.Rational(4, 3)*sp.pi*(sp.integrate(rr*3*sp.pi/8, (rr, 0, 1)) + sp.integrate(rr*3*sp.pi/(8*rr**4), (rr, 1, sp.oo)))
res['L2c'] = sp.simplify(I1_R2 - sp.pi**2/2) == 0 and sp.simplify(I1_R2 - I1_R1) == 0
# L3: scaling degree of the bubble integrand under K = s z, P = s e (E = e_1 perpendicular to P = e_2 direction)
K = sp.symbols('k1:5'); Z = sp.symbols('w1:5')
P = (0, s, 0, 0)
f = K[0]**2/((sum(k*k for k in K))**2*(sum((K[i] + P[i])**2 for i in range(4)))**2)
g = f.subs({K[i]: s*Z[i] for i in range(4)}, simultaneous=True)*s**4
g0 = (Z[0]**2/((sum(w*w for w in Z))**2*(sum((Z[i] + (1 if i == 1 else 0))**2 for i in range(4)))**2))
res['L3'] = sp.simplify(g/g0 - s**(-2)) == 0
# Cc1: wrong target pi^2/4 must FAIL
res['Cc1_fires'] = not (sp.simplify(I1_R2 - sp.pi**2/4) == 0)
# Cc2: longitudinal numerator z_2^2 -> J_2(r) ~ const/(1-r): divergence must be seen
vals = []
for N in [10, 100, 1000]:
    r = 1 - sp.Rational(1, N)
    vals.append(theta_int(lambda C, S: C**2*S**2, r))
ratios = [sp.nsimplify(vals[1]/vals[0]), sp.nsimplify(vals[2]/vals[1])]
res['Cc2_fires'] = all((q > 9) and (q < 11) for q in ratios)
# Cc3: marginal analogue (one 1-form line): r^2 * Kint(r) -> 3pi/8 at large r, so the radial integrand ~ (3pi/8)/r (log divergent)
def theta_int1(num, r):
    C = (z + 1/z)/2; S = (z - 1/z)/(2*sp.I)
    fz = sp.together(num(C, S)/(1 + 2*r*C + r**2)/(sp.I*z))
    poles = [sp.Integer(0), -r if r < 1 else -1/r]
    return sp.nsimplify(sp.simplify(sp.pi*sp.I*sum(sp.residue(fz, z, p) for p in poles)))
okC3 = True
for r in [sp.Integer(2), sp.Integer(5), sp.Integer(10)]:
    Kint = theta_int1(lambda C, S: S**4, r)
    okC3 = okC3 and sp.simplify(Kint - sp.pi*(3 - r**-2)/(8*r**2)) == 0
res['Cc3_fires'] = okC3   # integrand r*Kint ~ 3pi/(8r): divergent radial integral detected
for k, v in res.items():
    print(k, 'PASS' if v else 'FAIL')
print('I1 (R1) =', I1_R1, '; I1 (R2) =', I1_R2, '; Cc2 ratios =', [str(q) for q in ratios][:2] and [sp.Rational(int(q*1000), 1000) for q in ratios])
