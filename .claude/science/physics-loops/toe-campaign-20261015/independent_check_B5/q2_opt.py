import sympy as sp, pickle
Gp,D,C2 = pickle.load(open('plane.pkl','rb')); P,Q,gb = pickle.load(open('max.pkl','rb'))
b1,b2 = sp.symbols('b1 b2'); sg,t = sp.symbols('sigma t')
S0 = sp.sqrt(sp.Rational(2,27))
for sv in (S0, -S0):
    qt = sp.factor(Q.subs(sg, sv)); print('P(sigma*,t) =', qt)
    roots = sp.solve(sp.Poly(sp.expand(Q.subs(sg,sv)), t), t)
    print(' roots t:', roots)
    for r in set(roots):
        if not r.is_real: continue
        r = sp.nsimplify(sp.radsimp(r))
        Pt = sp.simplify(sp.diff(Q,t).subs({sg:sv,t:r})); Ps = sp.simplify(sp.diff(Q,sg).subs({sg:sv,t:r}))
        bb1 = sp.radsimp(sv - r); bb2 = r; bb0 = sp.radsimp(bb1+2*bb2)
        M = Gp.subs({b1:bb1, b2:bb2}).applyfunc(sp.radsimp)
        print('  t=',r,' b=(',bb0,',',bb1,',',bb2,')  s=',sp.radsimp(bb0+2*bb1+bb2), ' P_t=',Pt,' P_sigma=',Ps)
        print('  G =', M.tolist())
        print('  rank G =', M.rank(simplify=True))
        ev = M.eigenvals(); print('  eigenvalues:', {sp.nsimplify(sp.simplify(k)):m for k,m in ev.items()})
