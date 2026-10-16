# (d) rank<=2 locus of Q (h2==0) and NN-only case
import sympy as sp, pickle, itertools, numpy as np
b0,b1,b2=sp.symbols('b0 b1 b2',real=True)
Q=pickle.load(open('Q.pkl','rb'))
minors=[sp.expand(Q.extract(list(r),list(c)).det()) for r in itertools.combinations(range(4),3) for c in itertools.combinations(range(4),3)]
G=sp.groebner(list(set(minors)),b0,b1,b2,order='lex')
print("Groebner basis of 3x3 minors (rank<=2):"); [print("  ",sp.factor(g)) for g in G.exprs]
sols=sp.solve(list(set(minors)),[b0,b1,b2],dict=True)
print("real solutions:")
for s in sols:
    Qs=Q.subs(s); print("  ",s,"  eig(Q)=",[sp.nsimplify(e) for e in Qs.eigenvals()] if not Qs.free_symbols else sp.factor(Qs.det()), Qs.rank() if not Qs.free_symbols else '')
