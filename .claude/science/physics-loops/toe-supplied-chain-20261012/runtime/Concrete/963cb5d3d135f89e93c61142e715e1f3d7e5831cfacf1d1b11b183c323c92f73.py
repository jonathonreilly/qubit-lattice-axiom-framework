#!/usr/bin/env python3
"""Disjoint author control: Laurent BdG kernels and Gaussian-integer matrices.

No imports of local_symbolic or previous campaign helpers. Symbolic controls
derive the current/stress from differential-operator commutators. Spin matrices
are assembled by Kronecker products. All matrix arithmetic is int64 with an
operation-bound guard before each multiplication/addition.
"""
import argparse,json,platform
from pathlib import Path
import sympy as s
import numpy as np

LIMIT=2**60
guard_max=0
def bound(a): return max(int(np.max(np.abs(a[0]))),int(np.max(np.abs(a[1]))))
def guard(v):
 global guard_max
 guard_max=max(guard_max,v)
 if v>=LIMIT: raise OverflowError('operation bound exceeded')
def plus(a,b):
 guard(bound(a)+bound(b));return(a[0]+b[0],a[1]+b[1])
def minus(a,b): return plus(a,(-b[0],-b[1]))
def times(a,b):
 guard(2*a[0].shape[1]*bound(a)*bound(b))
 return(a[0]@b[0]-a[1]@b[1],a[0]@b[1]+a[1]@b[0])
def comm(a,b): return minus(times(a,b),times(b,a))
def ix(a): return(-a[1],a[0])
def scale(a,v):
 guard(abs(v)*bound(a));return(v*a[0],v*a[1])
def zero(n): return (np.zeros((n,n),dtype=np.int64),np.zeros((n,n),dtype=np.int64))
def eq(a,b): return np.array_equal(a[0],b[0]) and np.array_equal(a[1],b[1])
def tensor(a,b):
 guard(2*bound(a)*bound(b))
 return(np.kron(a[0],b[0])-np.kron(a[1],b[1]),np.kron(a[0],b[1])+np.kron(a[1],b[0]))
P={p:zero(2) for p in 'IXYZ'}
P['I']=(np.eye(2,dtype=np.int64),np.zeros((2,2),dtype=np.int64))
P['X']=(np.array([[0,1],[1,0]],dtype=np.int64),np.zeros((2,2),dtype=np.int64))
P['Y']=(np.zeros((2,2),dtype=np.int64),np.array([[0,-1],[1,0]],dtype=np.int64))
P['Z']=(np.diag(np.array([1,-1],dtype=np.int64)),np.zeros((2,2),dtype=np.int64))
def spin(n,terms):
 a=(np.ones((1,1),dtype=np.int64),np.zeros((1,1),dtype=np.int64))
 for x in range(n):a=tensor(a,P[terms.get(x,'I')])
 return a
def simp(M):return M.applyfunc(s.simplify)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True)
 ap.add_argument('--mutation',choices=['none','kernel_current_sign','stress_drop_range2','boost_connection'],default='none');a=ap.parse_args()
 rows=[];data={}
 def check(name,test):rows.append({'name':name,'ok':bool(test)})
 J,g,z=s.symbols('J g z',nonzero=True);I=s.I
 dk=lambda M: M.diff(z)*I*z
 K=s.Matrix([[0,2*I*(g-J/z)],[-2*I*(g-J*z),0]])
 E2=4*(g**2+J**2-J*g*(z+1/z));p=-2*I*J*g*(z-1/z)
 A=I*K; C=I*dk(K)/2-K/2
 Kp=simp(I*(K*C-C*K-A*dk(K)))
 if a.mutation=='kernel_current_sign':Kp=-Kp
 Kt=simp(I*(Kp*C-C*Kp-A*dk(Kp)))
 tab=I*(-4*J**2*g+4*J*g**2*(z+1/z)-0*J**2*g/z**2)
 tba=-I*(-4*J**2*g+4*J*g**2*(z+1/z)-4*J**2*g*z**2)
 if a.mutation=='stress_drop_range2':
  tab+=4*I*J**2*g/z**2;tba-=4*I*J**2*g*z**2
 Tspin=s.Matrix([[0,tab],[tba,0]])
 check('K squared gives generic E squared',simp(K*K-E2*s.eye(2))==s.zeros(2))
 check('differential current equals direct CAR current',simp(Kp-p*s.eye(2))==s.zeros(2))
 check('current commutes with generic Hamiltonian',simp(K*Kp-Kp*K)==s.zeros(2))
 check('stress commutator equals spin-derived range-two kernel',simp(Kt-Tspin)==s.zeros(2))
 check('stress is beta cos(k) times K',simp(Kt-2*J*g*(z+1/z)*K)==s.zeros(2))
 k=s.symbols('k',real=True);theta=s.Function('theta',real=True)(k);E=s.Function('E',real=True)(k)
 D=s.diag(s.exp(I*theta/2),s.exp(-I*theta/2));C0=s.Matrix([[0,I],[-I,0]])
 Krot=E*D*C0*D.conjugate().T;Aprime=I*Krot
 Cprime=I*s.diff(Krot,k)/(1 if a.mutation=='boost_connection' else 2)-Krot/2
 transformed=simp(D.conjugate().T*(Aprime*s.diff(D,k)+Cprime*D))
 target=(I*s.diff(E,k)/2-E/2)*C0
 check('Bogoliubov derivative connection cancels exactly',simp(transformed-target)==s.zeros(2))
 data['kernels']={'H':str(K),'H2':str(E2),'P':str(Kp),'T':str(Kt),'rotated_boost_zeroth':str(transformed)}
 fixtures=[]
 for j,gg in [(1,2),(2,3),(3,7),(0,2),(2,0)]:
  n=7;dim=2**n;H=zero(dim);B=zero(dim);Pdirect=zero(dim);T=zero(dim)
  # H and B below are doubled, so i[H,B] is four times physical current.
  for x in range(n-1):
   h=plus(scale(spin(n,{x:'X',x+1:'X'}),-2*j),scale(plus(spin(n,{x:'Z'}),spin(n,{x+1:'Z'})),-gg))
   H=plus(H,h);B=plus(B,scale(h,x-3))
   c=minus(spin(n,{x:'X',x+1:'Y'}),spin(n,{x:'Y',x+1:'X'}))
   Pdirect=plus(Pdirect,scale(c,j*gg))
   T=plus(T,scale(plus(spin(n,{x:'X',x+1:'X'}),spin(n,{x:'Y',x+1:'Y'})),2*j*gg**2))
  for x in range(n):T=plus(T,scale(spin(n,{x:'Z'}),2*j*j*gg))
  for x in range(n-2):T=plus(T,scale(spin(n,{x:'X',x+1:'Z',x+2:'X'}),-2*j*j*gg))
  P4=ix(comm(H,B));T8=ix(comm(P4,B));HP=comm(H,P4)
  for p0 in 'XYZ':
   O=spin(n,{3:p0})
   check(f'{j},{gg} center {p0}: current boundary localization',eq(comm(P4,O),scale(comm(Pdirect,O),4)))
   check(f'{j},{gg} center {p0}: energy-current conservation',eq(comm(HP,O),zero(dim)))
   check(f'{j},{gg} center {p0}: weighted stress',eq(comm(T8,O),scale(comm(T,O),8)))
  fixtures.append({'J':j,'g':gg,'open_boundary_HP_max':bound(HP),'open_boundary_current_diff_max':bound(minus(P4,scale(Pdirect,4)))})
 # Finite JW normalization on an independent 3-site tensor calculation.
 n=3;maj=[]
 for x in range(n):
  maj.append(spin(n,{**{y:'Z' for y in range(x)},x:'X'}));maj.append(spin(n,{**{y:'Z' for y in range(x)},x:'Y'}))
 check('JW Z=-i ab',eq(spin(n,{1:'Z'}),scale(ix(times(maj[2],maj[3])),-1)))
 check('JW XX=-i b a_next',eq(spin(n,{0:'X',1:'X'}),scale(ix(times(maj[1],maj[2])),-1)))
 check('JW YY=i a b_next',eq(spin(n,{0:'Y',1:'Y'}),ix(times(maj[0],maj[3]))))
 check('JW XZX=-i b a_next2',eq(spin(n,{0:'X',1:'Z',2:'X'}),scale(ix(times(maj[1],maj[4])),-1)))
 check('JW Bogoliubov generator sign and quarter factor',eq(ix(minus(times(maj[0],maj[2]),times(maj[1],maj[3]))),plus(spin(n,{0:'Y',1:'X'}),spin(n,{0:'X',1:'Y'}))))
 out={'python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'mutation':a.mutation,'matrix_integer_operation_bound':guard_max,'bound_limit':LIMIT,'fixtures':fixtures,'checks':rows,**data}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'checks':len(rows),'failed':[r['name'] for r in rows if not r['ok']],'largest_integer_operation_bound':guard_max,'fixtures':fixtures},indent=2))
 raise SystemExit(0 if all(r['ok'] for r in rows) else 1)
if __name__=='__main__':main()
