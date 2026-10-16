import pickle, sympy as sp, numpy as np, sys
from scipy.optimize import least_squares
d=pickle.load(open('spinj_3_2.pkl','rb'))
eqs, unk, feas = d['eqs'], d['unk'], d['feas']
bi=int(sys.argv[1])
mvec,pvec,sol=feas[bi]
sub=dict(zip(unk,sol))
free=sorted(set().union(*[sp.sympify(v).free_symbols for v in sol]),key=str)
red=[e for e in (sp.expand(e.subs(sub)) for e in eqs) if e!=0]
red=sorted(set(red),key=str)
print(mvec,pvec,len(free),'free',len(red),'eqs',flush=True)
pickle.dump({'free':free,'red':red,'sub':sub},open(f'spin32_branch{bi}.pkl','wb'))
F=sp.lambdify(free,red,'numpy'); Jm=sp.Matrix(red).jacobian(free); Jf=sp.lambdify(free,Jm,'numpy')
rng=np.random.default_rng(1); best=[]
for t in range(200):
    x0=rng.normal(size=len(free))*rng.choice([0.1,0.3,1.0])
    r=least_squares(lambda x: np.array(F(*x),float), x0, jac=lambda x: np.array(Jf(*x),float), xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=2000)
    res=np.linalg.norm(r.fun); best.append((res,np.linalg.norm(r.x)))
    if res<1e-10: print(f'trial {t}: SOLUTION residual {res:.1e}, |x| = {np.linalg.norm(r.x):.4f}',flush=True); np.save(f'spin32_sol{bi}_{t}.npy',r.x)
best.sort(); print('best residuals',[f'{a:.1e}/{b:.2f}' for a,b in best[:8]])
