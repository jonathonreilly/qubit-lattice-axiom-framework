"""Independent occupancy/charge-word reconstruction, separate from electric enumeration."""
from pathlib import Path
from itertools import combinations,permutations
import sympy as s
import json

HERE=Path(__file__).resolve().parent
leaves=range(4)
# P: u(i,j) has center +, leaf i +, leaf j -;
# v(i,k) has center -, leaves i,k +.
P=[('u',i,j) for i,j in permutations(leaves,2)]+[('v',i,k) for i,k in combinations(leaves,2)]
Q=[(i,k,j) for i,k in combinations(leaves,2) for j in leaves if j not in (i,k)]
A=s.zeros(len(Q),len(P))
for row,(i,k,j) in enumerate(Q):
    for label in [('u',i,j),('u',k,j),('v',i,k)]:A[row,P.index(label)]=1
assert A.rank()==12
D=s.eye(len(P))-A.T*(A*A.T).inv()*A
assert D*D==D and A*D==s.zeros(12,18) and s.trace(D)==6
vectors={}
for c in leaves:
    plus=s.zeros(18,1);minus=s.zeros(18,1)
    for b in leaves:
        if b==c:continue
        plus[P.index(('u',b,c))]=1
        minus[P.index(('v',*sorted((b,c))))]=1
    vectors[c]=(plus,minus)
resolved=sum((p*p.T+m*m.T for p,m in vectors.values()),s.zeros(18))/24
coherent=sum(((p+m)*(p+m).T for p,m in vectors.values()),s.zeros(18))/24
rows={}
for name,rho in [('resolved',resolved),('coherent',coherent)]:
    assert s.trace(rho)==1
    dark=s.trace(D*rho)
    rows[name]={'trapped_weight':str(dark),'full_probability':str(1-dark),'expected_number_of_births':str(2-dark),'terminal_expected_population':str(5-2*dark),'first_event_purity':str(s.trace(rho*rho))}
assert rows['resolved']['trapped_weight']=='1/3'
assert rows['coherent']['trapped_weight']=='4/15'

# Complete transient two-level block before first birth; exact Lyapunov mean.
delta,kappa,epsilon=s.symbols('delta kappa epsilon',positive=True)
meanrows=[]
for degree in (2,4):
    g=s.sqrt(degree)*delta/epsilon
    loss=2*(degree-1)*kappa/epsilon**2
    detuning=delta/epsilon**2
    H=s.Matrix([[0,-g],[-g,detuning]])
    G=s.diag(0,loss)
    a,b,c,d=s.symbols('a b c d',real=True)
    M=s.Matrix([[a,c+s.I*d],[c-s.I*d,b]])
    # -L_noevent^*(M) = I.
    equations=list(-s.I*(H*M-M*H)+(G*M+M*G)/2-s.eye(2))
    sol=s.solve([x for z in equations for x in (s.re(z),s.im(z))],(a,b,c,d),dict=True)[0]
    mean=s.simplify(sol[a]);rate=s.factor(2*degree*(degree-1)*kappa*delta**2/(delta**2+(degree-1)**2*kappa**2))
    assert s.simplify(mean-1/rate-epsilon**2/((degree-1)*kappa))==0
    meanrows.append({'degree':degree,'full_bare_first_birth_mean':str(mean),'effective_first_rate':str(rate),'finite_epsilon_extra_mean':str(epsilon**2/((degree-1)*kappa))})

data={'method':'charge-word incidence constraints and exact projector, independent of electric-sector builder','P_states':P,'Q_states':Q,'hop_gram_spectrum':{str(x):int(n) for x,n in (A*A.T).eigenvals().items()},'dark_basis_one_example':list(map(str,A.nullspace()[0])),'first_birth_and_absorption':rows,'exact_two_level_means':meanrows,'scope':'All spin S>=1 and all positive finite epsilon,delta,kappa on these stars: only E=0,+-1 occurs; every legal shift has amplitude one. Exact dark projection is reached by first birth. Bright singular blocks decay and the second birth fills the star.'}
(HERE/'STAR_ANALYTIC_RESULTS.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
