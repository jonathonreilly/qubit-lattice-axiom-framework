import sympy as sp, pickle, numpy as np
free, Fs, coeqs = pickle.load(open('q1.pkl','rb'))
c = sp.symbols('c1:4'); s = sp.symbols('s1:4')
names=[str(v) for v in free]
# K-family
K_sin = sp.expand(s[0]*c[1]*c[2]+c[0]*s[1]*c[2]+c[0]*c[1]*s[2]-s[0]*s[1]*s[2])
K_cos = sp.expand(c[0]*c[1]*c[2]-c[0]*s[1]*s[2]-s[0]*c[1]*s[2]-s[0]*s[1]*c[2])
target = [K_cos] + [K_sin/sp.sqrt(3)]*3
eqs=[]
for F,T in zip(Fs,target):
    eqs += sp.Poly(sp.expand(F-T), *c, *s).coeffs()
sol = sp.solve(eqs, free, dict=True); print('K-family in ansatz:', sol)
# probe direction
f = sp.lambdify([free], coeqs, 'numpy')
d = np.zeros(len(free)); 
for n,v in {'x3_10':-np.sqrt(3),'x3_20':np.sqrt(3),'x3_11':1,'x3_19':1,'x3_21':-2}.items(): d[names.index(n)]=v
for tt in (1e-3,1e-2,1e-1):
    x = tt*d; x[names.index('x0_0')] = np.sqrt(1-0)  # crude
    # optimize only x0 block: use least squares with others fixed? just print residual
    print(tt, np.linalg.norm(np.array(f(x),float)))
