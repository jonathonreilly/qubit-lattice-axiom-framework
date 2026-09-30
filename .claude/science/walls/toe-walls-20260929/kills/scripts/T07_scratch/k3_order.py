"""K3: formation order (x1, x3, x2) on the 3-site path 1-2-3.  Is the even-parity law reachable?
(a) general conditional r(b2 | b1, b3), b1,b3 formed first with A = empty (so independent, arbitrary marginals);
(b) Gibbs-note product rule r(s | a1,a3) = K(a1,s) K(a3,s) / K_2(a1,a3) with K a positive 2x2 matrix;
Also the fixed order (1,2,3) [attacker's F2] for reference."""
import numpy as np, itertools
from scipy.optimize import minimize
even = np.zeros((2,2,2))
for a,b,c in itertools.product(range(2),repeat=3):
    if (a+b+c)%2==0: even[a,b,c]=0.25      # index (b1,b2,b3)
sg = lambda z: 1/(1+np.exp(-np.clip(z,-60,60)))
def kl(P,Q):
    return sum(P[i]*np.log(P[i]/max(Q[i],1e-300)) for i in np.ndindex(*P.shape) if P[i]>0)
def q_general(th):
    p1=np.array([sg(th[0]),1-sg(th[0])]); p3=np.array([sg(th[1]),1-sg(th[1])])
    Q=np.zeros((2,2,2))
    k=2
    for b1 in range(2):
        for b3 in range(2):
            p=sg(th[k]); k+=1
            for b2 in range(2): Q[b1,b2,b3]=p1[b1]*p3[b3]*(p if b2==0 else 1-p)
    return Q
def q_product(th):
    p1=np.array([sg(th[0]),1-sg(th[0])]); p3=np.array([sg(th[1]),1-sg(th[1])])
    K=np.exp(th[2:6].reshape(2,2))           # K[a,s] > 0
    Q=np.zeros((2,2,2))
    for b1 in range(2):
        for b3 in range(2):
            w=np.array([K[b1,s]*K[b3,s] for s in range(2)]); w/=w.sum()
            for b2 in range(2): Q[b1,b2,b3]=p1[b1]*p3[b3]*w[b2]
    return Q
def best(q,n):
    b=1e9; rng=np.random.default_rng(1)
    for _ in range(60):
        th=rng.normal(size=n)*2
        r=minimize(lambda t: kl(even,q(t)),th,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-13,maxiter=6000))
        b=min(b,r.fun)
    return b
print('order (1,3,2), general conditional r(b2|b1,b3): min KL(even || model) = %.6f' % best(q_general,6))
print('order (1,3,2), Gibbs product rule K(a1,s)K(a3,s)/norm:  min KL(even || model) = %.6f   (ln2 = %.6f)' % (best(q_product,6),np.log(2)))
