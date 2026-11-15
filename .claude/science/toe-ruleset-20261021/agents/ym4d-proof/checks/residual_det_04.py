#!/usr/bin/env python3
"""Exact gauge-path controls. Scope is declared in residual_det_04.criteria.md."""
from itertools import product
import sympy as sp
import json
checks=[]
def ck(name, value, detail=None):
    checks.append({'name':name,'ok':bool(value),**({'detail':detail} if detail is not None else {})})
def zz(mat): return all(sp.cancel(v)==0 for v in mat)
coords=list(product(range(3),repeat=4)); idx={x:i for i,x in enumerate(coords)}
Delta=sp.zeros(81)
for x in coords:
    j=idx[x]; Delta[j,j]=8
    for mu in range(4):
        for step in (-1,1):
            y=list(x); y[mu]=(y[mu]+step)%3
            Delta[idx[tuple(y)],j]-=1
Di=Delta[1:,1:]; b=Delta[:1,1:]
h=Di.inv(method='DM')*b.T
ck('periodic_3_power_4_dirichlet_harmonic_constant',zz(h+sp.ones(80,1)))
r=(h.T*h)[0]
ck('actual_interior_norm_r_80',r==80)
z=sp.symbols('z',real=True)
alpha=sp.Integer(9)
den=(alpha+1)-(alpha-1)*z*z
u=2*z/den
v=(1-z)*((alpha+1)-(alpha-1)*z)/den
a=sp.cancel(alpha*u+v)
d=sp.cancel(1+r*u*u)
ck('path_endpoints',u.subs(z,1)==1 and v.subs(z,1)==0 and u.subs(z,0)==0 and v.subs(z,0)==1)
ck('path_exact_normalization',sp.cancel(a*a-d)==0)
# This is the full high-gradient block, not the scalar Schur formula being tested.
Qhi=sp.eye(80)+u*u*h*h.T
ym=Qhi.inv(method='DM')*(-u*a*h)
energy=sp.cancel((ym.T*ym)[0]+(u*(h.T*ym)[0]+a)**2)
ck('direct_80d_schur_energy_one',energy==1)
partial=sp.cancel(sp.diff(u,z)*(h.T*ym)[0]+sp.diff(a,z))
ck('partial_dotted_fixing_not_total_derivative_vanishes',partial==0)
ck('minimizing_high_vector_changes_with_parameter',any(sp.diff(x,z).subs(z,sp.Rational(1,2))!=0 for x in ym))
# The vector derivative is deliberately not included in the partial expression.
naive_u=z; naive_v=1-z; naive_a=alpha*naive_u+naive_v
naive_d=1+r*naive_u**2
naive_coeff=sp.cancel(naive_a**2/naive_d)
ck('control_naive_midpoint_is_25_over_21',naive_coeff.subs(z,sp.Rational(1,2))==sp.Rational(25,21))
naive_partial=sp.cancel(sp.diff(naive_a,z)-sp.diff(naive_u,z)*naive_u*r*naive_a/naive_d)
ck('control_naive_partial_does_not_vanish',naive_partial.subs(z,sp.Rational(1,3))!=0)
# Completely independent finite matrix identity, with no lattice normal-form assumption.
t=sp.symbols('t',real=True)
D=sp.Matrix([[1,0],[0,1],[1,1]])
F=D.T+t*sp.Matrix([[1,2,0],[0,-1,1]])
H=sp.Matrix([[5,1,0],[1,4,1],[0,1,3]])
Q=H+F.T*F; B=F*D
# Rational determinant derivatives avoid logs and any branch ambiguity.
direct=sp.cancel(sp.diff(Q.det(),t)/(2*Q.det())-sp.diff(B.det(),t)/B.det())
rhs=sp.cancel(-sp.trace(Q.inv()*H*D*B.inv()*sp.diff(F,t)))
ck('off_shell_logdet_derivative_equals_Nielsen_trace',sp.cancel(direct-rhs)==0)
ck('off_shell_gauge_row_is_nonzero',not zz(H*D))
ck('control_dropping_off_shell_row_gives_wrong_derivative',direct.subs(t,0)!=0,{'derivative_at_zero':str(direct.subs(t,0))})
null=D[:,0].cross(D[:,1]); H0=2*null*null.T
Q0=H0+F.T*F
on_shell=sp.cancel(sp.diff(Q0.det(),t)/(2*Q0.det())-sp.diff(B.det(),t)/B.det())
ck('zero_gauge_row_normalized_determinant_is_gauge_independent',on_shell==0)
result={'scope':'finite algebra and partial gauge-path derivative only','checks':checks,
        'passed':sum(x['ok'] for x in checks),'total':len(checks),'all_ok':all(x['ok'] for x in checks)}
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['all_ok'] else 1)
