#!/usr/bin/env python3
"""Additional independent checks for the primary continuation review.

Uses the previously sealed independent quotient data and new locally built
small matrices. It does not import the primary runner.
"""
from pathlib import Path
from itertools import combinations, product
from fractions import Fraction as F
from math import comb
import json
import sympy as s

OUT = Path(__file__).resolve().parent
S = s.Rational
old = json.loads((OUT.parent/'results.json').read_text())
ip = old['identical_pair']
parse = lambda v: S(v['exact'])
Q = s.Matrix([[parse(v) for v in row] for row in ip['quotient_generator']])
pi = s.Matrix([parse(v) for v in ip['quotient_stationary']])
B = s.Matrix([parse(v) for v in ip['quotient_hazards']])
success = s.Matrix([parse(v) for v in ip['quotient_identical_birth_rates']])
P, one, L = s.diag(*pi), s.ones(6,1), -Q
mu = (pi.T*B)[0]
forcing = one-B/mu
phi = (L+one*pi.T).inv()*forcing
centered = phi-one*(pi.T*s.diag(*B)*phi)[0]/mu
derivative = S(37,180)*(pi.T*s.diag(*success)*centered)[0]
epsilon = s.Symbol('epsilon')
probability = s.sympify(ip['finite_epsilon_probability'],locals={'epsilon':epsilon})
from_polynomial = s.diff(probability,epsilon).subs(epsilon,0)
assert derivative == from_polynomial == -S(16823,29030544)
eps = S(1,1000)
g = eps*(L+eps*s.diag(*B)).inv()*one
nu = P*s.diag(*B)*g
nu0 = P*B/mu
first = nu0+eps*P*s.diag(*B)*centered
tv = sum(abs(v) for v in nu-nu0)/2
tv_first = sum(abs(v) for v in nu-first)/2
variance = ((B-mu*one).T*P*(B-mu*one))[0]

# Independent gap certificate: a principal cofactor of the full Poincare
# quadratic form, rather than the primary's weighted mean-zero basis.
edges=((0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5))
nb=[{b if a==x else a for a,b in edges if x in (a,b)} for x in range(6)]
pairs=list(combinations(range(6),2))
index={tuple(p):i for i,p in enumerate(pairs)}
q=s.zeros(15)
weights=[]
for occupied in pairs:
    weights.append(S(3,2) if occupied[1] in nb[occupied[0]] else S(1))
for i,occupied in enumerate(pairs):
    for x in occupied:
        other=next(z for z in occupied if z!=x)
        for y in nb[x]-set(occupied):
            old_weight=S(3,2) if other in nb[x] else S(1)
            new_weight=S(3,2) if other in nb[y] else S(1)
            dest=tuple(sorted((other,y)))
            q[i,index[dest]]+=new_weight/(old_weight+new_weight)
    q[i,i]=-sum(q[i,k] for k in range(15) if k!=i)
p=s.Matrix([w/sum(weights) for w in weights])
pp=s.diag(*p)
assert pp*q==q.T*pp
gap=S(2,5)
form=pp*(-q)-gap*(pp-p*p.T)
assert form*s.ones(15,1)==s.zeros(15,1)
cofactor=form[1:,1:]
pivots=[]
previous=s.Integer(1)
for k in range(1,15):
    determinant=cofactor[:k,:k].det(method='domain-ge')
    assert determinant>0
    pivots.append(determinant/previous)
    previous=determinant

# Poisson remainder and scaled waiting-time bounds on nontrivial small chains.
small_cases=0
for q,pprobs,bb,lam in (
    (s.Matrix([[-2,2],[3,-3]]),[S(3,5),S(2,5)],[S(1),S(4)],S(5)),
    (s.Matrix([[-1,1,0],[1,-2,1],[0,1,-1]]),[S(1,3)]*3,[S(1),S(2),S(5)],S(1))):
    n=q.rows
    p=s.Matrix(pprobs); pp=s.diag(*p); one=s.ones(n,1); b=s.Matrix(bb)
    mean=(p.T*b)[0]; var=((b-mean*one).T*pp*(b-mean*one))[0]
    for f in (one,s.Matrix([1/p[0]]+[0]*(n-1)),b/mean):
        r=f-b/mean
        norm2=(r.T*pp*r)[0]
        corrector=(-q+one*p.T).inv()*r
        assert (-q)*corrector==r and (p.T*corrector)[0]==0
        c=(p.T*s.diag(*b)*corrector)[0]/mean
        for eps in (S(1,1000),S(1,100),S(1,10),S(1),S(10)):
            gg=eps*(-q+eps*s.diag(*b)).inv()*f
            actual=pp*s.diag(*b)*gg
            approx=pp*b/mean+eps*pp*s.diag(*b)*(corrector-one*c)
            err=sum(abs(v) for v in actual-approx)/2
            bound2=eps**4*mean*max(bb)**3*norm2/(4*lam**2*(lam+eps*min(bb))**2)
            assert err**2<=bound2
            wait_error=abs((p.T*gg)[0]-1/mean)
            wait_bound2=eps**2*var*norm2/(mean**2*(lam+eps*min(bb))**2)
            assert wait_error**2<=wait_bound2
            small_cases+=1

# Direct finite sums challenge the graph identity and its triangle-free scope.
def graph_check(n,edges,j):
    near=[{v if u==x else u for u,v in edges if x in (u,v)} for x in range(n)]
    def w(a,b): return 1+j if a==b else 1-j if a==(b^1) else F(1)
    def config_weight(state):
        value=F(1)
        for u,v in edges:
            if state[u]>=0 and state[v]>=0: value*=w(state[u],state[v])
        return value
    za=den=num=F(0)
    for occupied in combinations(range(n),2):
        state=tuple(0 if x in occupied else -1 for x in range(n))
        weight=config_weight(state); za+=weight
        for x in range(n):
            if state[x]>=0: continue
            for a in range(6):
                value=F(1)
                for y in near[x]:
                    if state[y]>=0: value*=w(a,state[y])
                den+=weight*value
                if a==0: num+=weight*value
    all_weight=same_weight=F(0)
    for occupied in combinations(range(n),3):
        for content in product(range(6),repeat=3):
            state=[-1]*n
            for x,a in zip(occupied,content): state[x]=a
            ww=config_weight(state)
            all_weight+=ww
            if len(set(content))==1: same_weight+=ww
    dynamic=za/(6*comb(n,2))*num/den
    static=same_weight/all_weight
    wedge=sum(comb(len(v),2) for v in near)
    main=6*(n-2)*za
    predicted=main/(main+2*j*j*wedge)
    return {'dynamic_static_ratio':str(dynamic/static),'claimed_ratio':str(predicted),
            'matches':dynamic/static==predicted,'static_partition':str(all_weight)}
graphs=[('path_3',3,((0,1),(1,2))),('cycle_4',4,((0,1),(1,2),(2,3),(0,3))),
        ('star_5',5,((0,1),(0,2),(0,3),(0,4))),('ladder_6',6,edges)]
graph_results=[]
for name,n,ee in graphs:
    for j in (F(-1,2),F(1,2),F(3,4)):
        result=graph_check(n,ee,j)
        assert result['matches']
        graph_results.append({'graph':name,'j':str(j),**result})
triangle=graph_check(3,((0,1),(1,2),(0,2)),F(1,2))
assert not triangle['matches']

# Independently check the general menu modes symbolically for all positive p,q,r.
equal,opposite,orthogonal=s.symbols('p q r',positive=True)
scale=6/(equal+opposite+4*orthogonal)
W=s.Matrix([[scale*(equal if a==b else opposite if a==(b^1) else orthogonal)
             for b in range(6)] for a in range(6)])
modes=[s.Matrix([1,-1,0,0,0,0]),s.Matrix([0,0,1,-1,0,0]),s.Matrix([0,0,0,0,1,-1]),
       s.Matrix([1,1,-1,-1,0,0]),s.Matrix([1,1,1,1,-2,-2])]
for i,mode in enumerate(modes):
    theta=scale*(equal-opposite) if i<3 else scale*(equal+opposite-2*orthogonal)
    assert sum(mode)==0 and all(s.simplify(v)==0 for v in W*mode-theta*mode)

# Green function in characteristic-root form, with kappa>0.
kappa=s.symbols('kappa',positive=True)
root=1+kappa-s.sqrt(kappa*(kappa+2))
amplitude=1/s.sqrt(kappa*(kappa+2))
assert s.simplify((1+kappa)*root-(1+root**2)/2)==0
assert s.simplify((1+kappa)*amplitude-amplitude*root)==1
assert s.simplify(amplitude*(1+root)/(1-root)-1/kappa)==0

result={'sealed_quotient_derivative':str(derivative),'sealed_polynomial_derivative':str(from_polynomial),
        'epsilon_1_over_1000_prebirth_TV':str(tv),'epsilon_1_over_1000_corrected_TV':str(tv_first),
        'hazard_variance':str(variance),'independent_gap_certificate':{
            'form':'diag(pi)*L-(2/5)*(diag(pi)-pi*pi.T), first coordinate deleted',
            'positive_sylvester_pivots':[str(x) for x in pivots]},
        'small_chain_poisson_waiting_cases':small_cases,'graph_results':graph_results,
        'triangle_exclusion_counterexample':triangle,'general_pqr_modes_symbolically_checked':5,
        'green_characteristic_root_identities':True}
(OUT/'REVIEW_EXTRA_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
