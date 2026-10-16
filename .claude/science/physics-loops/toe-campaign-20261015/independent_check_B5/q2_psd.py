import sympy as sp, pickle, numpy as np
Gp,D,C2 = pickle.load(open('plane.pkl','rb'))
b1,b2 = sp.symbols('b1 b2'); lam=sp.Symbol('lam')
r6,r15 = sp.sqrt(6), sp.sqrt(15)
pts = {'A': ((5*r6-2*r15)/27, (2*r15-2*r6)/27), 'B': ((5*r6+2*r15)/27, (-2*r15-2*r6)/27)}
cp = sp.Poly(Gp.charpoly(lam).as_expr(), lam).all_coeffs()
for name,(x,y) in pts.items():
    print(name, 'b=', [sp.radsimp(x+2*y), x, y], 'numeric', [float(x+2*y), float(x), float(y)])
    M = np.array(Gp.subs({b1:x,b2:y}).evalf(30).tolist(), dtype=float)
    print('  eigs', np.linalg.eigvalsh(M))
    co = [sp.radsimp(sp.expand(c.subs({b1:x,b2:y}))) for c in cp]
    print('  charpoly coeffs exact:', co, [float(c) for c in co])
