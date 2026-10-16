# enumerate real points of the rank<=2 variety of Q (from 3x3-minor Groebner basis) and test PSD
import sympy as sp, pickle, itertools, numpy as np
b0,b1,b2=sp.symbols('b0 b1 b2')
Q=pickle.load(open('Q.pkl','rb')).subs({sp.Symbol('b0',real=True):b0,sp.Symbol('b1',real=True):b1,sp.Symbol('b2',real=True):b2})
minors=list(set(sp.expand(Q.extract(list(r),list(c)).det()) for r in itertools.combinations(range(4),3) for c in itertools.combinations(range(4),3)))
x=sp.Symbol('x')
for p2 in [27*x**2-153432*x+32, 27*x**2-72*x-16]:
    for xr in sp.solve(p2,x):
        if xr<=0: continue
        for B2 in (sp.sqrt(xr),-sp.sqrt(xr)):
            eqs=[sp.simplify(m.subs(b2,B2)) for m in minors]
            G=sp.groebner([e for e in eqs if e!=0],b0,b1,order='lex')
            sols=sp.solve(G.exprs,[b0,b1],dict=True)
            for s in sols:
                v=[complex(sp.N(s[b0])),complex(sp.N(s[b1]))]
                if max(abs(t.imag) for t in v)>1e-12: continue
                M=np.array(Q.subs({b0:s[b0],b1:s[b1],b2:B2}).evalf(30),dtype=complex).real
                print("b=(%.6g,%.6g,%.6g)"%(v[0].real,v[1].real,float(B2)),"eig",np.round(np.linalg.eigvalsh(M),8))
print("b2=0 case: PSD forces b1=b0=0 (see Q[3,3]=3b2^2, Q[2,2]=2b1^2-b2^2) ")
