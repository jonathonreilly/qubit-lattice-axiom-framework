"""R15-1 (b), step 2: reduce the rank-1 quadratic Lagrangian of r151_quadratic.py to one variable.
q := dchi - (chidot/H) zeta (the kinetic direction; q = -(chidot/H) * R_comoving).
zeta is then auxiliary (after integrating linear zetadot terms by parts) and is eliminated.
Background time derivatives: adot = aH, Hdot = Hd, Hd' = Hdd, chi0'' = -3H chidot - Vp, V' = Vp chidot, Vp' = Vpp chidot.
Output: L = (1/2) A(t) qdot^2 - (1/2) [C(t) k^2/a^2 + M(t)] q^2 + O(total derivative), with g = -2Hd - chidot^2 kept explicit;
compare A, C, M with the GR (g = 0) values.
"""
import sympy as sp, pickle
d = pickle.load(open('r151_quadratic.pkl', 'rb'))
Lred = d['Lred']
fs = {s_.name: s_ for s_ in Lred.free_symbols}
print('free symbols:', sorted(fs))
t = fs['t']; a = sp.Function('a')(t)
H, Hd, cd, V2, k = fs['H'], fs['Hdot'], fs['chidot'], fs.get('Vpp', sp.Symbol('Vpp')), fs['k']
V0 = fs.get('V0', sp.Symbol('V0')); Vp = fs.get('Vp', sp.Symbol('Vp'))
Hdd, Vppp = sp.symbols('Hddot Vppp')
Z, D, Zd, Dd = fs['Z'], fs['D'], fs['Zd'], fs['Dd']
q, qd = sp.symbols('q qd')
aa = sp.Symbol('aa', positive=True)
L = Lred.subs(a, aa)
# time derivative operator on background symbols
def Dt(e):
    return (sp.diff(e, aa)*aa*H + sp.diff(e, H)*Hd + sp.diff(e, Hd)*Hdd + sp.diff(e, cd)*(-3*H*cd - Vp)
            + sp.diff(e, V0)*Vp*cd + sp.diff(e, Vp)*V2*cd + sp.diff(e, V2)*Vppp*cd)
f = cd/H
L = sp.expand(L.subs({D: q + f*Z, Dd: qd + f*Zd + Dt(f)*Z}))
L = sp.expand(sp.simplify(L))
# check: Zd appears at most linearly
assert sp.expand(sp.diff(L, Zd, 2)) == 0, sp.diff(L, Zd, 2)
cZ = sp.expand(sp.diff(L, Zd))          # = c1*Z + c2*q + c3*qd
c1 = cZ.coeff(Z); c2 = cZ.coeff(q); c3 = cZ.coeff(qd)
assert sp.simplify(cZ - c1*Z - c2*q - c3*qd) == 0
L0 = sp.expand(L - cZ*Zd)
# integrate by parts: c1 Z Zd -> -1/2 Dt(c1) Z^2 ; c2 q Zd -> -Dt(c2) q Z - c2 qd Z ; c3 qd Zd -> -Dt(c3) qd Z - c3 qdd Z
qdd = sp.Symbol('qdd')
L1 = sp.expand(L0 - sp.Rational(1, 2)*Dt(c1)*Z**2 - Dt(c2)*q*Z - c2*qd*Z - Dt(c3)*qd*Z - c3*qdd*Z)
print("c3 (qd*Zd coefficient) =", sp.simplify(c3))
# eliminate Z (auxiliary): L1 = A2 Z^2 + B1 Z + rest
A2 = L1.coeff(Z, 2); B1 = L1.coeff(Z, 1); R0 = L1.coeff(Z, 0)
print("Z^2 coefficient:", sp.factor(A2))
Lq = sp.expand(R0 - B1**2/(4*A2))
Lq = sp.simplify(Lq)
# coefficients
Lq = sp.expand(sp.together(Lq))
num, den = sp.fraction(sp.together(Lq))
print("has qdd?", Lq.has(qdd))
A = sp.simplify(2*sp.diff(Lq, qd, 2)/2)
print("A (qdot^2 coefficient x2):", sp.factor(sp.diff(Lq, qd, 2)))
Ld = sp.expand(Lq.subs({qdd: 0}))
mass_like = sp.simplify(-sp.diff(Ld, q, 2))
print("-(d^2 L/dq^2) = C k^2/a^2 + M :", sp.factor(mass_like))
cross = sp.simplify(sp.diff(sp.diff(Ld, q), qd))
print("q*qd cross coefficient (total-derivative piece):", sp.factor(cross))
pickle.dump({'Lq': Lq}, open('r151_reduce.pkl', 'wb'))
# R15-1 addendum: is the auxiliary solution Z = -B1/(2 A2) regular as g -> 0 ?  (g = -2Hdot - chidot^2)
gsym = sp.Symbol('g')
Zsol = sp.simplify((-B1/(2*A2)).subs(Hd, -(gsym + cd**2)/2))
num_, den_ = sp.fraction(sp.factor(Zsol))
print("Z solution denominator (factored):", sp.factor(den_))
print("Z solution at g = 0 (limit):", sp.simplify(sp.limit(Zsol, gsym, 0)))
