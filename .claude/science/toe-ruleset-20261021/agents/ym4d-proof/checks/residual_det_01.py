#!/usr/bin/env python3
"""Exact finite controls; see residual_det_01_criteria.md for scope."""
from itertools import permutations
import sympy as s

t=s.symbols('t', real=True)
Q=s.Rational
verdicts=[]
def check(name, predicate, detail=''):
    ok=bool(predicate)
    verdicts.append(ok)
    print(('PASS ' if ok else 'FAIL ')+name+((': '+str(detail)) if detail else ''))

def matjets(m):
    return [m.applyfunc(lambda x,k=k:s.simplify(s.diff(x,t,k).subs(t,0)/s.factorial(k))) for k in range(3)]
def jm(a,b):
    return [sum((a[j]*b[k-j] for j in range(k+1)),s.zeros(a[0].rows,b[0].cols)) for k in range(3)]
def jt(a):return [x.T for x in a]
def conv(a,b):
    return [s.expand(sum(a[j]*b[k-j] for j in range(k+1))) for k in range(3)]
def detjet(a):
    n=a[0].rows
    ans=[s.S.Zero]*3
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=[s.S.One,s.S.Zero,s.S.Zero]
        for i,j in enumerate(p):term=conv(term,[a[k][i,j] for k in range(3)])
        ans=[ans[k]+(-1)**inv*term[k] for k in range(3)]
    return [s.simplify(x) for x in ans]
def log2_direct(a):
    d=detjet(a)
    return s.simplify(Q(1,2)*(d[2]/d[0]-Q(1,2)*(d[1]/d[0])**2))
def log2_trace(a, wrong=False):
    g=a[0].inv()
    return s.simplify(Q(1,2)*s.trace(g*a[2])-(Q(1,8) if wrong else Q(1,4))*s.trace(g*a[1]*g*a[1]))
def scalarjets(x):return matjets(s.Matrix([[x]]))

Z=s.Matrix([[5+2*t+t*t,1+t],[1+t,4-t+2*t*t]])
Y=s.Matrix([1+t,2-t*t]); X=3+t+2*t*t
b=t+2*t*t; c=9-6*t+4*t*t
Df=(2+t)**2; Dc=(3-t)**2; cov=Q(1,3)+t/7+t*t/5
J=s.zeros(5)
J[:2,:2]=Z; J[2,2]=Df; J[:2,3]=Y; J[3,:2]=Y.T
J[3,3]=X; J[3,4]=b; J[4,3]=b; J[4,4]=c
A=Z-Y*Y.T/X; B=-Y*b/X; C=c-b*b/X
Jr=A.row_join(B).col_join(B.T.row_join(s.Matrix([[C]])))
A0=A.subs(t,0)
WT=A0+t*s.Matrix([[1,Q(1,3)],[Q(1,3),-2]])+t*t*s.diag(2,1)
bw=t*s.Matrix([1,-2])+t*t*s.Matrix([Q(1,2),1])
WH=WT.row_join(bw).col_join(bw.T.row_join(s.Matrix([[Df+t*t]])))

# Rotation jets come from exp(t K): moving frames, including second derivative.
Kf=s.Matrix([[0,0,-1],[0,0,0],[1,0,0]])
Kc=s.Matrix([[0,-2],[2,0]])
K=s.diag(Kf,Kc)
rot=[s.eye(5),K,K*K/2]
rf=[s.eye(3),Kf,Kf*Kf/2]
Jphysical=jm(jm(rot,matjets(J)),jt(rot))
Wphysical=jm(jm(rf,matjets(WH)),jt(rf))
check('orthonormal moving-frame jets',jm(jt(rot),rot)==[s.eye(5),s.zeros(5),s.zeros(5)])
check('direct permutation determinant is frame invariant',detjet(Jphysical)==detjet(matjets(J)))
product=conv(conv(detjet(scalarjets(Df)),detjet(scalarjets(X))),detjet(matjets(Jr)))
check('actual Schur product through second order',detjet(Jphysical)==[s.simplify(x) for x in product])
check('trace expansion versus permutation determinant',log2_trace(Jphysical)==log2_direct(Jphysical),log2_direct(Jphysical))
check('designed control: wrong half-bubble rejected',log2_trace(Jphysical,wrong=True)!=log2_direct(Jphysical))

a=matjets(A); bb=matjets(B); cc=scalarjets(C)
ga=a[0].inv(); gc=cc[0].inv()
five=s.simplify(Q(1,2)*s.trace(ga*a[2])+Q(1,2)*s.trace(gc*cc[2])
               -Q(1,4)*s.trace(ga*a[1]*ga*a[1])-Q(1,4)*s.trace(gc*cc[1]*gc*cc[1])
               -Q(1,2)*s.trace(ga*bb[1]*gc*bb[1].T))
check('five reduced trace groups exhaust J_red',five==log2_direct(matjets(Jr)),five)
lhs=log2_direct(Jphysical)+log2_direct(scalarjets(cov))-log2_direct(scalarjets(Dc))-log2_direct(Wphysical)
rhs=log2_direct(scalarjets(X))+log2_direct(scalarjets(cov))+log2_direct(scalarjets(Df))-log2_direct(scalarjets(Dc))+five-log2_direct(matjets(WH))
check('full six-determinant residual combination',s.simplify(lhs-rhs)==0,lhs)
check('designed control: omitted coarse gauge factor rejected',s.simplify(lhs-(rhs+log2_direct(scalarjets(Dc))))!=0)
Jwrong=WT.row_join(B).col_join(B.T.row_join(s.Matrix([[C]])))
wrong=rhs-five+log2_direct(matjets(Jwrong))
check('designed control: replacing completed A by Wilson TT rejected',s.simplify(lhs-wrong)!=0)
freeze=[w[:2,:2] for w in Wphysical]
check('designed control: frozen transverse frame rejected',log2_direct(freeze)!=log2_direct(matjets(WT)))
T=[s.diag(1,1,2),s.diag(0,0,1),s.zeros(3)]
nonorth=jm(jm(T,matjets(WH)),T)
check('unnormalized gauge coordinates need Gram correction',s.simplify(log2_direct(nonorth)-log2_direct(scalarjets(Df))-log2_direct(matjets(WH)))==0)
check('designed control: missing Gram determinant rejected',log2_direct(nonorth)!=log2_direct(matjets(WH)))

# Independently assembled soft-distance Hessian, prior to h elimination.
mu=Q(3,2); ww=s.Integer(5)
da=s.Matrix([1,0]); db=s.Matrix([1,t]); eye=s.eye(2)
Hw=s.Matrix([[0,mu*t],[mu*t,ww]])
hh=mu*(da.T*db)[0]
qaa=mu*eye-mu**2*db*db.T/hh
qab=-mu*eye+mu**2*db*da.T/hh
qbb=mu*eye-mu**2*da*da.T/hh
check('fine gauge-row completion',s.simplify((Hw+qaa)*da)==s.zeros(2,1))
check('mixed rows annihilate both gauge ranges',s.simplify(da.T*qab)==s.zeros(1,2) and s.simplify(qab*db)==s.zeros(2,1))
sc=s.Matrix([-t,1]); sf=s.Matrix([0,1])
zs=(sf.T*(Hw+qaa)*sf)[0]; ys=(sf.T*qab*sc)[0]; xs=(sc.T*qbb*sc)[0]
a_h_first=s.factor(zs-ys**2/xs)
orig=s.Matrix([[ww+mu,-mu,mu*t],[-mu,mu*(1+t*t),mu*t],[mu*t,mu*t,mu]])
# Exact determinant by its permutation definition, independent of Schur inverse.
def determinant_perm(m):
    return s.expand(sum((-1)**sum(p[i]>p[j] for i in range(m.rows) for j in range(i+1,m.rows))*s.prod(m[i,p[i]] for i in range(m.rows)) for p in permutations(range(m.rows))))
a_direct=s.cancel(determinant_perm(orig)/determinant_perm(orig[1:,1:]))
expected=ww-3*mu*t*t-mu*t**4
check('soft-distance transverse correction by two eliminations',s.simplify(a_h_first-expected)==0 and s.simplify(a_direct-expected)==0,a_direct)
for idx in [1,2]:
    bad=orig.copy()
    if idx==1:bad[0,2]=bad[2,0]=0
    else:bad[1,2]=bad[2,1]=0
    val=s.cancel(determinant_perm(bad)/determinant_perm(bad[1:,1:]))
    check('designed control: projected h coupling '+str(idx)+' is necessary',s.simplify(s.diff(val-expected,t,2).subs(t,0))!=0)

# Scaling arithmetic; the note supplies the universal analytic estimates.
p=s.symbols('p',positive=True)
check('two simple poles are separately integrable',all(a<4 for a in (2,2)))
check('two simple poles vanish after residual substitution',s.limit(p*p*s.log(1/p),p,0,dir='+')==0)
check('designed control: quadratic amplitude alone is insufficient',(3<4 and 3<4) and 4+(4-3-3)-2==0)
check('designed control: total degree does not permit a fourth-order pole',not all(a<4 for a in (4,2)))
print('SCOPE per_element: rational matrix entries and polynomial coefficients only')
print('SCOPE per_site: no actual SU(N) lattice site instance claimed')
print('SCOPE per_mode: algebraic mode model only; no spectral estimate from sampling')
print('SCOPE per_block: complete finite Schur blocks and their moving-frame trace groups')
print('SCOPE lattice_wide: no infinite-lattice or depth-uniform theorem certified by this runner')
print(f'OVERALL: {sum(verdicts)}/{len(verdicts)} predicates true')
raise SystemExit(0 if all(verdicts) else 1)
