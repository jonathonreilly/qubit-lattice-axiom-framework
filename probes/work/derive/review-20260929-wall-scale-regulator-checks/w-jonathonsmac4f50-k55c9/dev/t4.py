import sympy as sp, itertools, time
u,m=sp.symbols('u m')
# 2^4 all-antiperiodic block of staggered operator: site x in {0,1}^4. forward hop mu: x -> x+mu (mod 2) with sign -1 if wraps (x_mu=1)
# backward hop from x to x-mu (mod 2): sign -1 if wraps (x_mu=0). On a 2-site ring both neighbours are the same site.
sites=list(itertools.product((0,1),repeat=4)); idx={s:i for i,s in enumerate(sites)}
def eta(mu,x): return (-1)**sum(x[:mu])
K=sp.zeros(16,16)
for x in sites:
    for mu in range(4):
        y=list(x); y[mu]=(y[mu]+1)%2; y=tuple(y)
        sf=-1 if x[mu]==1 else 1      # forward wrap
        K[idx[x],idx[y]]+=sp.Rational(1,2)*eta(mu,x)*sf
        sb=-1 if x[mu]==0 else 1      # backward wrap
        K[idx[x],idx[y]]-=sp.Rational(1,2)*eta(mu,x)*sb
print('K antihermitian:',K==-K.T)
K2=K*K
print('K^2 =',sp.simplify(K2)==-sp.eye(16), K2[0,0])
print('K^2 == -4 I:',K2==-4*sp.eye(16))
t=time.time()
M=m*sp.eye(16)+u*K
d=sp.factor(M.det(method='berkowitz'))
print(d, time.time()-t)
print(sp.degree(sp.expand(d.subs(m,0)),u))
# naive Dirac on same block: gamma matrices
I2=sp.eye(2); sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-sp.I],[sp.I,0]]); sz=sp.Matrix([[1,0],[0,-1]])
from sympy.physics.quantum import TensorProduct as TP
g=[TP(sx,I2),TP(sy,I2),TP(sz,sx),TP(sz,sy)]
print([ (g[a]*g[b]+g[b]*g[a]==2*sp.eye(4)*(1 if a==b else 0)) for a in range(4) for b in range(4)].count(True))
