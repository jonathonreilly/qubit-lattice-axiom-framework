import sympy as sp, pickle, numpy as np
Gp,D,C2 = pickle.load(open('plane.pkl','rb'))
b1,b2 = sp.symbols('b1 b2'); sg,t = sp.symbols('sigma t')
P = sp.factor_list(D)[1]; P = [p for p,e in P if sp.Poly(p,b1,b2).total_degree()==6][0]
print('P =', P)
Q = sp.expand(P.subs({b1: sg-t, b2: t}))
print('P(sigma,t) =', sp.collect(Q, t))
# critical points of sigma on P=0 : P=0, dP/dt = 0 (incl singular points)
Rres = sp.factor(sp.resultant(Q, sp.diff(Q,t), t))
print('resultant in sigma:', Rres)
gb = sp.groebner([Q, sp.diff(Q,t)], t, sg, order='lex')
print('lex GB last:', sp.factor(gb.exprs[-1]))
for g in gb.exprs: print('  GB elt:', sp.factor(g))
pickle.dump((P,Q,gb), open('max.pkl','wb'))
