import sympy as sp, pickle, numpy as np
Gb = pickle.load(open('G.pkl','rb')); alpha,beta,gam,w = pickle.load(open('series.pkl','rb'))
b0,b1,b2 = sp.symbols('b0 b1 b2'); u,v = sp.symbols('u v')
sub = {b0: b1+2*b2}
Gp = Gb.subs(sub).applyfunc(sp.expand)
sp.pprint(Gp)
D = sp.factor(Gp.det()); print('det G on plane =', D)
C2 = sp.factor(gam['|k|^2 sum k^4'].subs(sub)); print('C2 on plane =', C2)
print('alpha on plane =', sp.factor(alpha.subs(sub)))
print('C1 on plane=', sp.factor(gam['|k|^6'].subs(sub))); print('C3 on plane =', sp.factor(gam['k1^2k2^2k3^2'].subs(sub)))
# char poly coefficients
lam = sp.Symbol('lam'); cp = sp.Poly(Gp.charpoly(lam).as_expr(), lam)
print('charpoly coeffs:', [sp.factor(cf) for cf in cp.all_coeffs()])
pickle.dump((Gp,D,C2), open('plane.pkl','wb'))
# numeric scan of PSD region
f = sp.lambdify((b1,b2), Gp, 'numpy')
best = (0,None)
B1 = np.linspace(-0.6,0.6,1201)
for x in B1:
    for y in B1:
        ev = np.linalg.eigvalsh(np.array(f(x,y),dtype=float))
        if ev[0] >= -1e-12:
            sv = 3*(x+y)
            if abs(sv)>best[0]: best=(abs(sv),(x,y,ev))
print('grid best |s|', best)
