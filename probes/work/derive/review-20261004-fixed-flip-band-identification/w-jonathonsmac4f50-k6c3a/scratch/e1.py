import sympy as sp, itertools, time
TERMS=[(0, 1, (-1, 0, 0), 'y'), (0, 1, (0, 0, 0), 'x'), (0, 3, (0, 0, -1), 'z'), (1, 1, (-1, 0, 0), 'odd'), (1, 3, (1, 0, -1), 'odd'), (3, 1, (0, 0, 1), 'odd'), (0, 0, (1, 0, 0), 'odd'), (0, 2, (-1, 0, 0), 'odd'), (2, 0, (0, 0, 0), 'odd'), (2, 3, (0, -1, 0), 'y'), (2, 3, (0, 0, 0), 'x'), (2, 1, (0, 0, 0), 'z'), (3, 3, (0, -1, 0), 'odd'), (3, 1, (0, 1, 0), 'odd'), (1, 3, (0, 0, 0), 'odd'), (2, 2, (0, 1, 0), 'odd'), (2, 0, (0, -1, 1), 'odd'), (0, 2, (0, 0, -1), 'odd')]
Jx,Jy,Jz,k=sp.symbols('Jx Jy Jz kappa',positive=True)
z1,z2,z3,mu=sp.symbols('z1 z2 z3 mu')
amp={'x':2*Jx,'y':2*Jy,'z':2*Jz,'odd':2*k}
M=sp.zeros(4,4)
for a,b,n,kd in TERMS:
    mon=z1**n[0]*z2**n[1]*z3**n[2]
    M[a,b]+=amp[kd]*mon; M[b,a]-=amp[kd]/mon
t=time.time()
cp=sp.Poly(sp.expand((mu*sp.eye(4)-M).det(method='berkowitz')),mu)
for e,c in sorted(cp.terms()): print(e, sp.factor(c) if e[0] in (3,1) else len(sp.expand(c).args))
print(time.time()-t)
# pairing symmetry search: P M(z) P^T = M(1/z) ?
Minv=M.subs({z1:1/z1,z2:1/z2,z3:1/z3},simultaneous=True)
import itertools
for perm in itertools.permutations(range(4)):
    P=sp.zeros(4,4)
    for i,j in enumerate(perm): P[i,j]=1
    for signs in itertools.product([1,-1],repeat=4):
        S=sp.diag(*signs)
        Q=S*P
        d=(Q*M*Q.T-Minv).applyfunc(sp.expand)
        if d==sp.zeros(4,4): print('sym',perm,signs)
        d2=(Q*M*Q.T+Minv).applyfunc(sp.expand)
        if d2==sp.zeros(4,4): print('antisym',perm,signs)
