import sympy as sp, itertools, pickle
c = sp.symbols('c1:4'); b0,b1,b2 = sp.symbols('b0 b1 b2')
e1 = c[0]+c[1]+c[2]; e2 = c[0]*c[1]+c[0]*c[2]+c[1]*c[2]; e3 = c[0]*c[1]*c[2]
phi = sp.Matrix([1,e1,e2,e3])
def ga(a):
    o = [x for x in range(3) if x!=a]
    return b0 + b1*(c[o[0]]+c[o[1]]) + b2*c[o[0]]*c[o[1]]
g2 = sp.expand(sum((1-c[a]**2)*ga(a)**2 for a in range(3)))   # |g|^2 with s_a^2 = 1-c_a^2
Gs = sp.symbols('G0:10'); idx = [(i,j) for i in range(4) for j in range(i,4)]
G = sp.zeros(4)
for t,(i,j) in zip(Gs, idx): G[i,j]=t; G[j,i]=t
expr = sp.expand((phi.T*G*phi)[0] + g2 - 1)
P = sp.Poly(expr, *c)
eqs = [co for _,co in P.terms()]
# uniqueness: rank of linear system in G
A, rhs = sp.linear_eq_to_matrix(eqs, Gs)
print('num eqs', len(eqs), 'rank', A.rank(), 'unknowns', len(Gs))
sol = sp.solve(eqs, Gs, dict=True); assert len(sol)==1
Gb = G.subs(sol[0]).applyfunc(sp.factor)
sp.pprint(Gb)
assert sp.expand((phi.T*Gb*phi)[0] + g2 - 1) == 0
pickle.dump(Gb, open('G.pkl','wb'))
