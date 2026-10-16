import sympy as sp, pickle, numpy as np, sys
from scipy.optimize import least_squares
free, Fs, coeqs = pickle.load(open('q1.pkl','rb'))
c = sp.symbols('c1:4'); s = sp.symbols('s1:4')
# L2 mass of zero-frequency part: a0's constant Fourier coeff = x0_0 + (avg of other terms) ; compute mean of a0 over torus exactly
def torus_mean(e):
    # mean of monomial c^i s^j: E[c]=E[s]=0, E[c^2]=E[s^2]=1/2, E[cs]=0 etc. apply per variable
    P = sp.Poly(sp.expand(e), *c, *s); tot=0
    m1 = lambda i,j: {(0,0):1,(2,0):sp.Rational(1,2),(0,2):sp.Rational(1,2),(1,0):0,(0,1):0,(1,1):0}.get((i,j), None)
    for mon,co in P.terms():
        val=co
        for a in range(3):
            i,j = mon[a], mon[3+a]
            if (i,j) in [(0,0)]: v=1
            elif i+j==2 and i%2==0: v=sp.Rational(1,2)
            elif i%2==1 or j%2==1: v=0
            else: raise
            val*=v
        tot+=val
    return sp.expand(tot)
means = [torus_mean(F) for F in Fs]
print('constant Fourier coeffs:', means)
mu = sp.Symbol('mu')
extra = sp.expand(1 - sum(m**2 for m in means))  # = moving L2 mass
f = sp.lambdify([free], coeqs, 'numpy'); fe = sp.lambdify([free], extra, 'numpy')
J = sp.lambdify([free], sp.Matrix(coeqs+[extra]).jacobian(free), 'numpy')
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
names=[str(v) for v in free]
out=[]
for muv in (0.05,0.2,0.4,0.6,0.8,0.95,1.0):
    best=1e9; nsol=0
    for trial in range(150):
        x0 = rng.normal(size=len(free))*rng.uniform(0.1,0.7)
        fun = lambda x: np.concatenate([np.array(f(x),float), [10*(fe(x)-muv)]])
        jac = lambda x: np.array(J(x),float)*np.concatenate([np.ones(len(coeqs)),[10]])[:,None]
        r = least_squares(fun, x0, jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
        res = np.linalg.norm(r.fun); best=min(best,res)
        if res<1e-9: nsol+=1; out.append((muv,r.x))
    print('mu',muv,'best residual',best,'nsol',nsol, flush=True)
pickle.dump(out, open('q1_mu_sols.pkl','wb'))
