#!/usr/bin/env python3
"""Small exact algebra controls; general implication is the accompanying proof."""
import os,time,json,hashlib,subprocess
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
assert not (runtime/'STOP_REQUESTED.json').exists()
import sympy as s
start=time.monotonic();I=s.I
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
h=s.symbols('h0:3',real=True);hp=s.symbols('hp0:3',real=True)
H=sum((v*M for v,M in zip(h,sig)),s.zeros(2))
Hp=sum((v*M for v,M in zip(hp,sig)),s.zeros(2))
a,b,c,d,P=s.symbols('a b c d P',real=True)
Z=s.Matrix([[a,c+I*d],[c-I*d,b]])
assert s.simplify(s.trace(H*(I*P*(Z*H-H*Z))))==0
omega=sum(v*v for v in h)
assert s.simplify(H*H-omega*s.eye(2))==s.zeros(2)
u,v,up,vp=s.symbols('u v up vp',real=True)
Fp=up*s.eye(2)+vp*H+v*Hp
expr=s.expand((Fp*H+H*Fp)/2-up*H-(vp*omega+v*sum(x*y for x,y in zip(h,hp)))*s.eye(2))
assert expr==s.zeros(2)
q0,q1,p0,p1=s.symbols('q0 q1 p0 p1',real=True)
x=s.Matrix([q0,q1,p0,p1]);psi=s.Matrix([q0+I*p0,q1+I*p1])/s.sqrt(2)
J=s.BlockMatrix([[s.im(Z),s.re(Z)],[-s.re(Z),s.im(Z)]]).as_explicit()
assert J+J.T==s.zeros(4)
A=sig[0]+2*sig[2];B=sig[1]+s.eye(2)
f=(psi.conjugate().T*A*psi)[0];g=(psi.conjugate().T*B*psi)[0]
actual=(s.Matrix([s.diff(f,t) for t in x]).T*J*s.Matrix([s.diff(g,t) for t in x]))[0]
expected=(-I*psi.conjugate().T*(A*Z*B-B*Z*A)*psi)[0]
assert s.simplify(actual-expected)==0
assert s.simplify(actual+expected)!=0 # sign control has a nonzero witness
# Circle control retains transverse gap to avoid accidental H=0 parametrization.
k=s.symbols('k',real=True)
ftrace=s.sin(k)*s.cos(k)*(2+s.cos(k))
assert s.integrate(s.diff(ftrace,k),(k,-s.pi,s.pi))==0
assert s.integrate(s.diff(ftrace,k)-1,(k,-s.pi,s.pi))==-2*s.pi
# Fixed flow ZH=H and H^2=omega I imply Z=I on omega!=0 by exact multiplication.
assert s.simplify((Z*H-H)*H-omega*(Z-s.eye(2)))==s.zeros(2)
result={'uniform_trace_identity':True,'Pauli_matrix_affine_decomposition':True,'real_coordinate_Poisson_control':True,'opposite_sign_control_nonzero':True,'circle_residual_integral':'-2*pi','fixed_flow_identity':True,'seconds':time.monotonic()-start,'status':'author algebra controls only; independent check pending'}
p=Path(__file__).resolve().parent
(p/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
