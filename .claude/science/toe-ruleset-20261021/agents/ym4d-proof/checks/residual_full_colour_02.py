#!/usr/bin/env python3
"""Real-space exact regulator controls, with separately derived Fourier expectations."""
import itertools, json
import sympy as s
checks=[]
def check(name,predicate,detail=None):
    good=bool(predicate)
    checks.append({'name':name,'passed':good,'detail':str(detail) if detail is not None else None})
    if not good:
        print(json.dumps({'checks':checks,'failed':name},indent=2))
        raise AssertionError(name)
def zero(M): return all(s.simplify(x)==0 for x in M)
pts=list(itertools.product(range(3),repeat=4)); loc={p:i for i,p in enumerate(pts)}; V=len(pts)
D=s.zeros(V)
for p in pts:
    row=loc[p]; D[row,row]=8
    for mu in range(4):
        for sign in (-1,1):
            q=list(p); q[mu]=(q[mu]+sign)%3
            D[row,loc[tuple(q)]]-=1
P=s.ones(V)/V
# Construct the candidate Green kernel by exact radial orbit equations.
g=s.symbols('g0:5'); eq=[]
for h in range(5):
    lhs=(8-h)*g[h]
    if h: lhs-=h*g[h-1]
    if h<4: lhs-=2*(4-h)*g[h+1]
    eq.append(lhs-((1 if h==0 else 0)-s.Rational(1,V)))
eq.append(sum(s.binomial(4,h)*2**h*g[h] for h in range(5)))
sol=s.solve(eq,g)
G=s.Matrix(V,V,lambda i,j:sol[g[sum(a!=b for a,b in zip(pts[i],pts[j]))]])
check('periodic Green exact rank-one inverse',zero((D+P)*(G+P)-s.eye(V)))
check('periodic inverse defect retained',zero(D*G-(s.eye(V)-P)))
check('mean-zero domain',zero(G*s.ones(V,1)))
check('ordinary inverse assertion rejected',not zero(D*G-s.eye(V)))
w=s.Matrix([1 if p[0]==0 else -s.Rational(1,2) for p in pts])
check('external cosine norm and mean',sum(w)==0 and (w.T*w)[0]==s.Rational(V,2))
check('independent Fourier eigenvalue',zero(D*w-3*w))
Gw=w
for r in (1,2,3):
    Gw=G*Gw
    exact=s.factor((w.T*Gw)[0]/V)
    expected=s.Rational(1,2*3**r)
    check('exceptional trace word r='+str(r),exact==expected,{'trace':str(exact),'per_site':str(exact/V)})
    check('zero-defect replacement rejected r='+str(r),exact!=0)
T=s.symbols('T',positive=True)
for r in (1,2,3):
    fixed=s.Rational(1,2)/(T**4*2**r)
    check('fixed momentum volume limit r='+str(r),s.limit(fixed,T,s.oo)==0)
moving=s.Rational(1,2)/(T**4*(4*s.sin(s.pi/T)**2)**2)
limit=s.limit(moving,T,s.oo)
check('merging limit differs',s.simplify(limit-1/(32*s.pi**4))==0 and limit!=0,limit)

# Verify the pinned inverse by its own deleted-domain inverse equation.
origin=loc[(0,0,0,0)]; keep=[j for j in range(V) if j!=origin]
GP=s.Matrix(V,V,lambda i,j:G[i,j]-G[i,origin]-G[origin,j]+G[origin,origin])
check('pinned rows exactly zero',zero(GP[origin,:]) and zero(GP[:,origin]))
check('pinned deleted-domain inverse',zero(D.extract(keep,keep)*GP.extract(keep,keep)-s.eye(V-1)))
meantrace=s.trace(G)/V; pintrace=s.trace(GP)/V
check('pinned constant term matters',pintrace==2*meantrace and meantrace>0,{'mean_zero':str(meantrace),'pinned':str(pintrace)})
GPwrong=s.Matrix(V,V,lambda i,j:G[i,j]-G[i,origin]-G[origin,j])
check('missing pinned constant rejected',not zero(D.extract(keep,keep)*GPwrong.extract(keep,keep)-s.eye(V-1)))
check('finite rank difference not negligible',s.simplify(pintrace-meantrace)==meantrace and meantrace!=0)

# Direct determinant expansion versus projected trace calculus.
t=s.symbols('t'); O=s.Matrix([[2+t*t,t],[t,3+2*t+t*t]])
O0=O.subs(t,0); O1=O.diff(t).subs(t,0); O2=O.diff(t,2).subs(t,0)/2
G0=O0.inv(); trace=s.trace(G0*O2)-s.trace(G0*O1*G0*O1)/2
poly=s.series(s.log(O.det()/O0.det()),t,0,3).removeO().expand().coeff(t,2)
check('fixed-domain complete coefficient',s.simplify(trace-poly)==0 and trace==s.Rational(4,9),trace)
check('outer half weight',trace/2==s.Rational(2,9))
wrong=s.trace(G0*O2)-s.trace(G0*O1*G0*O1)/4
check('wrong bubble factor rejected',wrong!=poly)
vm=s.Matrix([1,t]); movingO=vm*vm.T
pdet=s.trace(movingO); reduced=movingO[0,0]
truecoef=s.series(s.log(pdet),t,0,3).removeO().coeff(t,2)
fixedcoef=s.series(s.log(reduced),t,0,3).removeO().coeff(t,2)
check('moving-kernel Gram correction',truecoef==1 and fixedcoef==0 and truecoef!=fixedcoef)
print(json.dumps({'scope':'exact finite periodic Green, projector-defect and Gram controls; no uniform-depth or nonlinear finite-volume verdict','passed':sum(x['passed'] for x in checks),'total':len(checks),'radial_green':{str(k):str(v) for k,v in sol.items()},'checks':checks},indent=2))
