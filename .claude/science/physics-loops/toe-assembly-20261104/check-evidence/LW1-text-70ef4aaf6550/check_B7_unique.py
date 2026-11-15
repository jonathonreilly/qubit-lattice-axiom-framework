# B7 uniqueness instance, robust version: maximise entropy on the min-cost face from several interior starting points.
import numpy as np, itertools
from scipy.optimize import linprog, minimize
from scipy.linalg import expm, null_space
from functools import reduce
rng=np.random.default_rng(5)
def fermions(n):
    a=np.array([[0,1],[0,0]],complex); Z=np.diag([1,-1]).astype(complex); I=np.eye(2)
    return [reduce(np.kron,[Z]*k+[a]+[I]*(n-k-1)) for k in range(n)]
for inst in range(4):
    nm=3 if inst<2 else 4; c=fermions(nm); ns=[x.conj().T@x for x in c]
    h=sum((c[i+1].conj().T@c[i]+c[i].conj().T@c[i+1]) for i in range(nm-1)); W=expm(-(0.5+0.4*inst)*1j*h)
    confs=list(itertools.product((0,1),repeat=nm))
    Ps=[reduce(lambda a,b:a@b,[ns[i] if s[i] else np.eye(2**nm)-ns[i] for i in range(nm)]) for s in confs]
    psi=rng.normal(size=2**nm)+1j*rng.normal(size=2**nm); psi/=np.linalg.norm(psi)
    P=reduce(lambda a,b:a@b,[np.eye(2**nm)-2*n for n in ns]); rho=np.outer(psi,psi.conj()); rho=(rho+P@rho@P)/2
    p=np.array([np.trace(Q@rho).real for Q in Ps]); pp=np.array([np.trace(Q@W@rho@W.conj().T).real for Q in Ps]); m=2**nm
    allowed=[(x,z) for x in range(m) for z in range(m) if abs(Ps[z]@W@Ps[x]).max()>1e-12]
    cost=np.array([sum(a!=b for a,b in zip(confs[x],confs[z])) for x,z in allowed],float)
    A=np.zeros((2*m,len(allowed)))
    for k,(x,z) in enumerate(allowed): A[x,k]=1; A[m+z,k]=1
    b=np.concatenate([p,pp])
    lp=linprog(cost,A_eq=A,b_eq=b,bounds=[(0,None)]*len(allowed),method="highs"); cmin=lp.fun
    A2=np.vstack([A,cost]); b2=np.append(b,cmin)
    # variables that can be positive on the face
    free=[]
    for k in range(len(allowed)):
        r=linprog(-np.eye(len(allowed))[k],A_eq=A2,b_eq=b2,bounds=[(0,None)]*len(allowed),method="highs")
        if -r.fun>1e-9: free.append((k,r.x))
    centre=np.mean([x for _,x in free],axis=0)       # relative interior point of the face
    act=[k for k,_ in free]; N=null_space(A2[:,act]); 
    if N.shape[1]==0:
        print(f'instance {inst} (modes {nm}): min cost {cmin:.6f}; min-cost face is a single point, uniqueness immediate'); continue
    def f(z,base):
        g=base[act]+N@z
        if (g<=0).any(): return 1e6+1e6*np.clip(-g,0,None).sum()
        return float((g*np.log(g)).sum())
    sols=[]
    for st in range(4):
        # random interior start: convex combination of vertices found
        wts=rng.dirichlet(np.ones(len(free))); base=sum(w*x for w,(_,x) in zip(wts,free))
        r=minimize(f,np.zeros(N.shape[1]),args=(base,),method='Powell',options={'xtol':1e-13,'ftol':1e-15,'maxiter':200000,'maxfev':200000})
        g=base.copy(); g[act]=base[act]+N@r.x; sols.append(g)
    print(f"instance {inst}: min cost {cmin:.6f}; face dimension {N.shape[1]}; max spread of entropy maximiser over 4 starts {max(abs(sols[0]-s).max() for s in sols[1:]):.2e}; constraint residual {abs(A2@sols[0]-b2).max():.1e}; entropy {-(sols[0][sols[0]>0]*np.log(sols[0][sols[0]>0])).sum():.8f}")
