#!/usr/bin/env python3
"""Finite exact determinants, independent permutation implementation."""
from itertools import permutations
import sympy as s

t=s.symbols('t', real=True); Q=s.Rational
checks=[]
def det(m):
    n=m.rows
    return s.factor(sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))*s.prod(m[i,p[i]] for i in range(n)) for p in permutations(range(n))))
def equal(a,b):
    if isinstance(a,s.MatrixBase):return a.applyfunc(s.simplify)==b.applyfunc(s.simplify)
    return s.simplify(a-b)==0
def check(label,ok,value=''):
    checks.append(bool(ok)); print(('PASS ' if ok else 'FAIL ')+label+(': '+str(value) if value else ''))

mu=Q(3,2); da=s.Matrix([2+t,0]); db=s.Matrix([2+t,t]); I=s.eye(2)
DA=(da.T*da)[0]; DB=(db.T*db)[0]; K=(da.T*db)[0]
H=s.Matrix([[0,mu*t/(2+t)],[mu*t/(2+t),5]])
W=H+da*da.T
check('exact off-shell fine gauge-row identity',equal(H*da,mu*(db-da)))
aug=(H+mu*I+da*da.T).row_join(-mu*I).row_join(mu*db)
aug=aug.col_join((-mu*I).row_join(mu*I+db*db.T).row_join(-mu*da))
aug=aug.col_join((mu*db.T).row_join(-mu*da.T).row_join(s.Matrix([[mu*K]])))
base=aug.copy(); base[:2,:2]-=da*da.T; base[2:4,2:4]-=db*db.T
null=da.col_join(s.zeros(2,1)).col_join(s.Matrix([-1]))
check('ungaugefixed augmented fine null vector',equal(base*null,s.zeros(5,1)))
S=s.eye(5); S[:2,4]=da; S[4,4]=-1
trans=s.simplify(S.T*aug*S)
check('triangular shear has unit determinant modulus',det(S)**2==1)
check('shear exposes Delta_A squared',equal(trans[4,4],DA**2))
check('shear coarse-gauge mixed block vanishes',equal(trans[2:4,4],s.zeros(2,1)))
L=(H+mu*I).row_join(-mu*I).col_join((-mu*I).row_join(mu*I+db*db.T))
check('permutation determinant after shear',equal(det(aug),DA**2*det(L)))
J=aug[:4,:4]-aug[:4,4:]*aug[4:,4:].inv()*aug[4:,:4]
check('h-first determinant agrees',equal(det(J),DA**2*det(L)/(mu*K)))
check('designed control: one Delta_A power missing',not equal(det(J),DA*det(L)/(mu*K)))
check('designed control: h determinant omitted',not equal(det(J),DA**2*det(L)))
M=mu*I+db*db.T
O=H+mu*db*db.T/(mu+DB)
check('massive coarse elimination gives actual gauge profile',equal(det(L),det(M)*det(O)))
wrong=H+mu*da*da.T/(mu+DA)
check('designed control: D_A substituted for D_B rejected',not equal(det(L),det(M)*det(wrong)))
lhs=det(J)/(mu*DB*det(W)) # dim one-forms minus gauge parameters = 1
rhs=det(O)/det(W)*DA**2/(DB*K)*(1+DB/mu)
check('complete residual determinant ratio',equal(lhs,rhs))

# Separate profile/congruence control with rational square root exactly equal to 2.
d=s.Matrix([3,0]); delta=s.Integer(9); m=s.Integer(3); f=Q(1,9)
C=s.eye(2)+d*f*d.T; gauge=m*d*d.T/(m+delta)
h=s.Matrix([[t,2*t],[2*t,5]])
TE=h*d; W0=h+d*d.T
r1=d*f*TE.T+TE*f*d.T
r2=d*f*(d.T*TE)*f*d.T
check('local congruence restores Feynman gauge block',equal(C*gauge*C,d*d.T))
check('profile Jacobian',equal(det(C)**2,1+delta/m))
check('complete derivative-bearing EOM completion',equal(C*h*C-h,r1+r2))
check('designed control: quadratic congruence term necessary',not equal(C*h*C-h,r1))
check('profile-compensated determinant equality',equal(det(h+gauge)*(1+delta/m),det(W0+r1+r2)))
print('SCOPE: exact finite algebra, including off-shell rows and every determinant factor')
print('SCOPE: neither actual lattice/alias matching nor a full Yang-Mills proof is tested')
print(f'OVERALL: {sum(checks)}/{len(checks)} predicates true')
raise SystemExit(0 if all(checks) else 1)
