"""Direct float check of saved numerical solutions: covariance with explicit D(R), unitarity of W(k), flatness."""
import sys, json, itertools, numpy as np
src=open('setup.py').read().split("# Check genuine rep")[0]
tag=sys.argv[3]; sys.argv=['x','/dev/null']+sys.argv[1:3]
exec(src)
import sympy as sp

m=json.load(open(tag+'.json')); P=m['P']; c=sp.symbols('c1:%d'%(P+1))
X=np.load(tag+'_numsols.npy')
Af={n:sp.lambdify(c,sp.Matrix([[sp.sympify(e) for e in r] for r in m['A'][str(n)]]),'numpy') for n in offs}
rng=np.random.default_rng(5); worst=[0,0,0]
for x in X:
    A={n:np.array(Af[n](*x),dtype=complex) for n in offs}
    for R,D in G:
        for n in offs:
            Rn=tuple((R@np.array(n)).tolist()); worst[0]=max(worst[0],np.abs(A[Rn]-D@A[n]@D.T).max())
    cps=[]
    for _ in range(5):
        k=rng.uniform(-np.pi,np.pi,3); W=sum(A[n]*np.exp(1j*np.dot(k,n)) for n in offs)
        worst[1]=max(worst[1],np.abs(W.conj().T@W-np.eye(8)).max()); cps.append(np.poly(np.linalg.eigvals(W)))
    worst[2]=max(worst[2],max(np.abs(cp-cps[0]).max() for cp in cps))
print(tag,len(X),"sols; max covariance err %.1e, max unitarity err %.1e, max charpoly k-variation %.1e"%tuple(worst))
