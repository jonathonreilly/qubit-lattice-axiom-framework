import sympy as sp, pickle
Gb = pickle.load(open('G.pkl','rb'))
b0,b1,b2 = sp.symbols('b0 b1 b2'); t = sp.Symbol('t'); k = sp.symbols('k1:4'); x=sp.Symbol('x')
cs = [sp.cos(t*ki) for ki in k]
e1 = sum(cs); e2 = cs[0]*cs[1]+cs[0]*cs[2]+cs[1]*cs[2]; e3 = cs[0]*cs[1]*cs[2]
phi = sp.Matrix([1,e1,e2,e3]); phi0 = sp.Matrix([1,3,3,1])
w = (Gb*phi0).applyfunc(sp.expand)
print('w = G phi0 =', list(w)); print('phi0.G.phi0 =', sp.factor((phi0.T*Gb*phi0)[0]))
F = (w.T*phi)[0]
X = sp.expand(sp.series(1-F, t, 0, 8).removeO())
# arccos(1-x)^2 series
h = sp.series(sp.acos(1-x)**2, x, 0, 4).removeO()
print('h(x)=', h)
om2p = sp.Poly(sp.expand(h.subs(x, X)), t)
om2 = sum(co*t**m[0] for m,co in om2p.terms() if m[0]<=7)
p1 = sum(ki**2 for ki in k); p2 = sum(ki**4 for ki in k); E3 = k[0]**2*k[1]**2*k[2]**2
o2 = om2.coeff(t,2); o4 = om2.coeff(t,4); o6 = om2.coeff(t,6)
S = sp.Symbol('S'); al, be = sp.symbols('alpha beta')
s = b0+2*b1+b2
print('order2 - s^2|k|^2 =', sp.factor(o2 - s**2*p1))
# fit order 4
A_, B_ = sp.symbols('A_ B_')
eq = sp.Poly(sp.expand(o4 - A_*p1**2 - B_*p2), *k).coeffs()
s4 = sp.solve(eq, [A_,B_], dict=True); assert len(s4)==1
alpha = sp.factor(s4[0][A_]); beta = sp.factor(s4[0][B_])
print('alpha =', alpha); print('beta =', beta)
C1,C2,C3 = sp.symbols('C1 C2 C3')
eq = sp.Poly(sp.expand(o6 - C1*p1**3 - C2*p1*p2 - C3*E3), *k).coeffs()
s6 = sp.solve(eq, [C1,C2,C3], dict=True); assert len(s6)==1
gam = {n: sp.factor(s6[0][v]) for n,v in zip(['|k|^6','|k|^2 sum k^4','k1^2k2^2k3^2'],[C1,C2,C3])}
for n,v in gam.items(): print('order6', n, '=', v)
pickle.dump((alpha,beta,gam,w), open('series.pkl','wb'))
