#!/usr/bin/env python3
"""Finite exact incidence witnesses and direct/dual Villain comparisons."""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
import itertools,json,math
import numpy as np
import sympy as sp

def complex_matrices(d):
 cells=[]
 for k in range(d+1):
  ck=[]
  for I in itertools.combinations(range(d),k):
   for bits in itertools.product([0,1],repeat=d-k):
    x=[0]*d
    for mu,b in zip([i for i in range(d) if i not in I],bits):x[mu]=b
    ck.append((tuple(x),I))
  cells.append(ck)
 deriv=[]
 for k in range(d):
  ids={c:i for i,c in enumerate(cells[k])};D=sp.zeros(len(cells[k+1]),len(cells[k]))
  for row,(x,J) in enumerate(cells[k+1]):
   for pos,mu in enumerate(J):
    I=J[:pos]+J[pos+1:];upper=list(x);upper[mu]+=1
    D[row,ids[(tuple(upper),I)]]+=(-1)**pos;D[row,ids[(x,I)]]-=(-1)**pos
  deriv.append(D)
 for k in range(d-1):assert deriv[k+1]*deriv[k]==sp.zeros(len(cells[k+2]),len(cells[k]))
 # A canonical rooted spanning tree from incidence endpoints.
 incidence=deriv[0];seen={0};tree=[]
 while len(seen)<len(cells[0]):
  for e in range(len(cells[1])):
   vertices=[i for i in range(len(cells[0])) if incidence[e,i]]
   if len(set(vertices)&seen)==1:
    tree.append(e);seen.update(vertices);break
  else:raise AssertionError('no spanning tree')
 non_tree=[i for i in range(len(cells[1])) if i not in tree];D=deriv[1][:,non_tree];Q=D.T*D;Qi=Q.inv();Pe=D*Qi*D.T;Pp=sp.eye(D.rows)-Pe
 assert D.rank()==D.cols and Pe*Pe==Pe and Pp*D==sp.zeros(D.rows,D.cols)
 rows=list(D.T.rref()[1]);minor=D[rows,:].det();assert abs(minor)==1
 complement=[i for i in range(D.rows) if i not in rows];R=sp.eye(D.rows)[:,complement];assert abs(D.row_join(R).det())==1
 B=R.T*Pp*R;M=Qi*D.T*R
 assert B.det()>0
 return dict(d=d,cells=cells,deriv=deriv,D=D,Q=Q,Qi=Qi,Pe=Pe,Pp=Pp,R=R,B=B,M=M,non_tree=non_tree,tree=tree)

def phi(u,beta):
 u=(np.asarray(u)+np.pi)%(2*np.pi)-np.pi
 k=np.arange(-12,13);return np.exp(-beta*(u[...,None]-2*np.pi*k)**2/2).sum(-1)

def direct_clock(C,N,beta,j):
 D=np.array(C['D']).astype(float);r=D.shape[1];a=np.array(list(itertools.product(range(N),repeat=r)),dtype=float);theta=2*np.pi*a/N
 w=phi(theta@D.T,beta).prod(1);z=w.mean();value=np.mean(w*np.exp(1j*(theta@j)))
 return z,value

def dual_three_cube(C,N,beta,j,A=10,Bcut=12):
 Qi=np.array(C['Qi']).astype(float);M=np.array(C['M']).astype(float).ravel();B=float(C['B'][0]);r=len(j)
 denom=sp.ilcm(*[x.q for x in C['M']]);denom=int(denom);m_int=np.array([int(x*denom) for x in C['M']]);assert np.max(abs(M-m_int/denom))<1e-15
 b=np.arange(-Bcut,Bcut+1);mag_w=np.exp(-2*np.pi**2*beta*B*b*b)
 phase=np.cos(2*np.pi*np.arange(denom)[:,None]*b[None,:]/denom);mag=phase@mag_w
 assert min(mag)>0
 grid=np.array(list(itertools.product(range(-A,A+1),repeat=r-1)),dtype=float)
 total=0.;no_phase=0.
 for first in range(-A,A+1):
  a=np.column_stack([np.full(len(grid),first),grid]);l=j[None,:]+N*a
  e=np.exp(-np.einsum('bi,ij,bj->b',l,Qi,l)/(2*beta))
  classes=np.rint(l@m_int).astype(np.int64)%denom;total+=float(e@mag[classes]);no_phase+=float(e.sum()*mag_w.sum())
 c=(2*np.pi*beta)**(-r/2)/math.sqrt(float(C['Q'].det()))
 return dict(value=c*total,without_phase=c*no_phase,min_magnetic_character=float(min(mag)),phase_denominator=denom)

def comparisons():
 C=complex_matrices(3);D=np.array(C['D']).astype(int);r=D.shape[1];rows=[]
 sources=[np.zeros(r,dtype=int),D[0,:].copy()]
 for N,beta in [(2,.2),(3,.5),(3,1.),(2,2.),(5,1.)]:
  for j in sources:
   z,actual=direct_clock(C,N,beta,j);dual=dual_three_cube(C,N,beta,j,A=10,Bcut=12)
   error=abs(dual['value']-actual);assert error<3e-11*max(1.,z)
   rows.append(dict(N=N,beta=beta,j=j.tolist(),clock_states=N**r,direct=float(actual.real),direct_imag=float(actual.imag),dual=dual['value'],absolute_error=float(error),omitting_phase_error=float(abs(dual['without_phase']-actual)),min_magnetic_character=dual['min_magnetic_character']))
 # Exact alias source at N times an independent tree-gauge character.
 N=3;beta=1.;j=np.zeros(r,dtype=int);j[0]=N;z,v=direct_clock(C,N,beta,j);dual=dual_three_cube(C,N,beta,j)
 assert abs(v-z)<1e-13 and abs(dual['value']-z)<3e-11
 # Representative change k -> k+D n shifts the phase by integer l dot n.
 R=C['R'];k=R[:,0];n=sp.Matrix([1,-2,0,1,3]);l=sp.Matrix([2,-1,1,0,3]);shift=(l.T*C['Qi']*C['D'].T*(k+C['D']*n)-l.T*C['Qi']*C['D'].T*k)[0]
 assert shift==(l.T*n)[0] and (C['Pp']*(k+C['D']*n))==C['Pp']*k
 # One stricter cutoff comparison; tails are not used as a proof of the identity.
 j=sources[1];base=dual_three_cube(C,2,2.,j,A=10,Bcut=12);ref=dual_three_cube(C,2,2.,j,A=12,Bcut=14)
 assert abs(base['value']-ref['value'])<3e-12
 return dict(cases=rows,alias_error=float(abs(v-z)),representative_integer_shift=int(shift),cutoff_comparison=float(abs(base['value']-ref['value'])),cube_r=r,cube_P=D.shape[0],Q_det=int(C['Q'].det()),magnetic_Q=str(C['B'][0]))

def four_cube_witness():
 C=complex_matrices(4);D=C['D'];r=D.cols;P=D.rows;assert (r,P)==(17,24)
 expected=sp.Rational(17,24);assert all(C['Pe'][i,i]==expected for i in range(P))
 ep=sp.eye(P)[:,0];a=D.T*ep;k=3*ep;N=3;phase=(N*a.T*C['Qi']*D.T*k)[0]
 ee=(a.T*C['Qi']*a)[0];em=(k.T*C['Pp']*k)[0];charge=C['deriv'][2]*k
 assert phase==sp.Rational(51,8) and ee==sp.Rational(17,24) and em==sp.Rational(21,8)
 assert charge!=sp.zeros(charge.rows,1) and C['deriv'][3]*charge==sp.zeros(1,1)
 real=sp.simplify(sp.cos(2*sp.pi*phase));assert real==-sp.sqrt(2)/2
 # Current reconstructed before gauge fixing is divergence-free.
 full_current=C['deriv'][1].T*ep;assert C['deriv'][0].T*full_current==sp.zeros(len(C['cells'][0]),1)
 return dict(r=r,P=P,Q_det=int(C['Q'].det()),magnetic_rank=C['B'].rows,phase_turns=str(phase),phase_real=str(real),electric_energy=str(ee),magnetic_energy=str(em),magnetic_charge=[int(x) for x in charge],integer_completion_determinant=int(D.row_join(C['R']).det()))

def run():return dict(three_cube=comparisons(),four_cube=four_cube_witness())
if __name__=='__main__':
 rows=run()
 print(json.dumps(rows,indent=2))
 print('per_element: executed integer boundary-of-boundary identities and exact rational curl projections on single three- and four-cubes.')
 print('per_site: executed exact tree gauge counts and direct finite-clock sums up to3125states with the supplied Villain weight.')
 print('per_mode: executed electric aliases, integer representative shifts and an exact negative mixed phase at N=3 on the four-cube.')
 print('per_block: executed ten direct/dual three-cube comparisons, a shifted-cutoff comparison and positive complete magnetic phase-class sums.')
 print('lattice_wide: checked and not executed: the general coupled-defect identity and positive marginal follow from the written proof; fixed-law phase control remains open.')
