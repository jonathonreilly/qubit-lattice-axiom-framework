#!/usr/bin/env python3
"""Finite integer homotopy, Hodge/source and electric-extension checks."""
from pathlib import Path
import itertools,json,math
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps=50

def interval(kind,m):
 if kind=='both':
  B=np.zeros((m,m+1),dtype=np.int64)
  for j in range(m+1):
   if j<m:B[j,j]=1
   if j>0:B[j-1,j]=-1
  h=np.zeros((m+1,m),dtype=np.int64)
  for j in range(m):h[:j+1,j]=1
  P=[np.zeros((m,m),dtype=np.int64),np.eye(m+1,dtype=np.int64)-h@B]
 elif kind=='left':
  B=np.eye(m,dtype=np.int64)
  for j in range(1,m):B[j-1,j]=-1
  h=np.triu(np.ones((m,m),dtype=np.int64))
  P=[np.zeros((m,m),dtype=np.int64),np.zeros((m,m),dtype=np.int64)]
 else:
  B=np.zeros((m+1,m),dtype=np.int64)
  for j in range(m):B[j,j]=-1;B[j+1,j]=1
  h=np.zeros((m,m+1),dtype=np.int64)
  for j in range(m+1):h[:j,j]=1
  P=[np.eye(m+1,dtype=np.int64)-B@h,np.zeros((m,m),dtype=np.int64)]
 assert np.array_equal(B@h,np.eye(B.shape[0],dtype=np.int64)-P[0])
 assert np.array_equal(h@B,np.eye(B.shape[1],dtype=np.int64)-P[1])
 return B,h,P

def tensor_homotopy(kinds,m):
 d=len(kinds);data=[interval(k,m if isinstance(m,int) else m[j]) for j,k in enumerate(kinds)];atoms=[]
 for B,h,P in data:atoms.append([(grade,i) for grade in [0,1] for i in range(B.shape[grade])])
 bases={k:[] for k in range(d+1)}
 for a in itertools.product(*atoms):bases[sum(g for g,i in a)].append(a)
 ids={k:{a:i for i,a in enumerate(v)} for k,v in bases.items()}
 boundary={};hom={};project={}
 for k in range(d+1):
  n=len(bases[k]);project[k]=np.zeros((n,n),dtype=np.int64)
  if k>0:boundary[k]=np.zeros((len(bases[k-1]),n),dtype=np.int64)
  if k<d:hom[k]=np.zeros((len(bases[k+1]),n),dtype=np.int64)
  for col,a in enumerate(bases[k]):
   for j,(grade,index) in enumerate(a):
    if grade==1:
     B=data[j][0]
     for i in np.flatnonzero(B[:,index]):
      out=list(a);out[j]=(0,int(i));sgn=(-1)**sum(g for g,z in a[:j])
      boundary[k][ids[k-1][tuple(out)],col]+=sgn*B[i,index]
    if grade==0 and k<d:
     choices=[]
     for c,(g,z) in enumerate(a):
      if c<j:
       mat=data[c][2][g];choices.append([(g,int(i),int(mat[i,z])) for i in np.flatnonzero(mat[:,z])])
      elif c==j:
       mat=data[c][1];choices.append([(1,int(i),int(mat[i,z])) for i in np.flatnonzero(mat[:,z])])
      else:choices.append([(g,z,1)])
     for b in itertools.product(*choices):
      out=tuple((g,i) for g,i,v in b);v=math.prod(v for g,i,v in b)*(-1)**sum(g for g,z in a[:j])
      hom[k][ids[k+1][out],col]+=v
   choices=[]
   for c,(g,z) in enumerate(a):
    mat=data[c][2][g];choices.append([(g,int(i),int(mat[i,z])) for i in np.flatnonzero(mat[:,z])])
   for b in itertools.product(*choices):
    out=tuple((g,i) for g,i,v in b);project[k][ids[k][out],col]+=math.prod(v for g,i,v in b)
 rows=[]
 for k in range(d+1):
  actual=np.zeros_like(project[k])
  if k<d:actual+=boundary[k+1]@hom[k]
  if k>0:actual+=hom[k-1]@boundary[k]
  assert np.array_equal(actual,np.eye(len(bases[k]),dtype=np.int64)-project[k])
  if 0<k<d:
   seed=np.arange(len(bases[k+1]))%5-2;q=boundary[k+1]@seed;filling=hom[k]@q
   assert not np.any(boundary[k]@q)
   assert np.array_equal(boundary[k+1]@filling,q)
   assert np.max(abs(filling),initial=0)<=d*np.sum(abs(q))
  if k<d:assert np.max(abs(hom[k]),initial=0)<=d
  rows.append(dict(degree=k,dimension=len(bases[k]),projection_rank=int(np.linalg.matrix_rank(project[k].astype(float))),max_homotopy_entry=int(np.max(abs(hom[k]),initial=0)) if k<d else None))
 if all(k=='both' for k in kinds):assert rows[-1]['projection_rank']==1 and all(r['projection_rank']==0 for r in rows[:-1])
 if 'left' in kinds:assert all(r['projection_rank']==0 for r in rows)
 extra={}
 if d==2 and isinstance(m,list):
  q=np.zeros(len(bases[1]),dtype=np.int64);mid=m[1]//2
  for i in range(m[0]+1):q[ids[1][((1,i),(0,mid))]]=1
  assert not np.any(boundary[1]@q)
  f=hom[1]@q;assert np.array_equal(boundary[2]@f,q)
  cycle=np.ones(len(bases[2]),dtype=np.int64);assert not np.any(boundary[2]@cycle)
  assert np.linalg.matrix_rank(boundary[2].astype(float))==len(cycle)-1
  least=min(np.count_nonzero(f+t*cycle) for t in [-1,0,1])
  assert least==(m[0]+1)*min(mid+1,m[1]-mid)
  extra=dict(carrier_mass=int(np.sum(abs(q))),least_filling_cells=int(least),required_long_direction_extent=int(least//(m[0]+1)))
 return dict(kinds=kinds,m=m,degrees=rows,anisotropic_control=extra)

def cube(d):
 cells=[]
 for k in range(d+1):
  level=[]
  for I in itertools.combinations(range(d),k):
   for bits in itertools.product([0,1],repeat=d-k):
    x=[0]*d
    for mu,b in zip([i for i in range(d) if i not in I],bits):x[mu]=b
    level.append((tuple(x),I))
  cells.append(level)
 deriv=[]
 for k in range(d):
  ids={c:i for i,c in enumerate(cells[k])};D=sp.zeros(len(cells[k+1]),len(cells[k]))
  for row,(x,J) in enumerate(cells[k+1]):
   for j,mu in enumerate(J):
    I=J[:j]+J[j+1:];y=list(x);y[mu]+=1
    D[row,ids[(tuple(y),I)]]+=(-1)**j;D[row,ids[(x,I)]]-=(-1)**j
  deriv.append(D)
 return cells,deriv

def hodge_and_source():
 rows=[]
 for d in [3,4]:
  cells,D=cube(d)
  for k in range(d-1):assert D[k+1]*D[k]==sp.zeros(len(cells[k+2]),len(cells[k]))
  spectra=[]
  for p in range(1,d+1):
   H=D[p-1]*D[p-1].T
   if p<d:H+=D[p].T*D[p]
   expected={2*(p+s):math.comb(d,p)*math.comb(d-p,s) for s in range(d-p+1)}
   assert H.eigenvals()==expected and max(expected)<=4*d
   spectra.append(dict(p=p,spectrum={str(k):v for k,v in expected.items()}))
  H1=D[0]*D[0].T+D[1].T*D[1];G1=H1.inv();ep=sp.eye(len(cells[2]))[:,0];J=D[1].T*ep;f=D[1]*G1*J
  assert D[0].T*J==sp.zeros(len(cells[0]),1) and D[1].T*f==J
  energy=(J.T*G1*J)[0];assert (f.T*f)[0]==energy
  H3=D[2]*D[2].T
  if d>3:H3+=D[3].T*D[3]
  G3=H3.inv();q=D[2]*ep;Pp=sp.eye(len(cells[2]))-D[1]*G1*D[1].T
  assert (q.T*G3*q)[0]==(ep.T*Pp*ep)[0]
  edge=next(i for i,x in enumerate(J) if abs(x)==1);ell=sp.eye(len(cells[1]))[:,edge]
  shift=((D[1]*ell).T*f)[0];assert shift==(ell.T*J)[0] and abs(shift)==1
  assert sp.simplify(sp.exp(2*sp.pi*sp.I*shift))==1 and sp.simplify(sp.exp(sp.pi*sp.I*shift))==-1
  rows.append(dict(d=d,spectra=spectra,current_energy=str(energy),magnetic_energy=str((q.T*G3*q)[0]),integer_phase_shift=int(shift),half_current_phase_ratio='-1'))
 return rows

def electric_extension():
 # Exact one-mode magnetic quotient of the actual single three-cube.
 # This finite check does not establish the p<d uniform filling theorem.
 rows=[];n=np.arange(-30,31);E=sp.Rational(5,6);M=float(E);N=3
 for beta in [2.,3.,4.]:
  w=np.exp(-2*math.pi**2*beta*n*n/6);a0=float(w.sum()-1);a1=float(np.sum(abs(2*math.pi*n)*w));a2=float(np.sum((2*math.pi*n)**2*w));delta=a2/(1-a0)+a1*a1/(1-a0)**2
  assert a0<1 and beta*delta<1
  for x in [-.7,-.19,0.,.23,.61]:
   sigma=N*M*x;phase=np.exp(2j*math.pi*sigma*n);z=(phase@w).real;zp=(phase@(2j*math.pi*n*w)).real;zpp=(phase@(-(2*math.pi*n)**2*w)).real
   curvature=N*N*float(E)/beta-(N*M)**2*(zpp/z-(zp/z)**2)
   lower=N*N*(1/beta-delta)*float(E);upper=N*N*(1/beta+delta)*float(E)
   assert lower-1e-10<=curvature<=upper+1e-10
   mb=mp.mpf(str(beta));mx=mp.mpf(str(x));h=mp.mpf('0.000001')
   def action(y):
    theta=sum(mp.exp(-2*mp.pi**2*mb*k*k/6)*mp.cos(2*mp.pi*N*mp.mpf(5)/6*y*k) for k in range(-20,21))
    return N*N*mp.mpf(5)/6*y*y/(2*mb)-mp.log(theta)
   fd=float((action(mx+h)-2*action(mx)+action(mx-h))/h**2)
   assert abs(fd-curvature)<1e-8
   rows.append(dict(beta=beta,x=x,hessian=curvature,lower=lower,upper=upper,finite_difference_error=abs(fd-curvature),beta_delta=beta*delta))
 return rows

def boundary_controls():
 rows=[]
 for m in [3,7,11]:
  B,h,P=interval('both',m);q=np.eye(m,dtype=np.int64)[:,m//2];f=h@q;cycle=np.ones(m+1,dtype=np.int64)
  assert np.array_equal(B@f,q) and not np.any(B@cycle)
  assert np.linalg.matrix_rank(B.astype(float))==m
  least=min(np.count_nonzero(f+t*cycle) for t in [-1,0,1])
  assert least==min(m//2+1,m-m//2)
  rows.append(dict(interior_vertices=m,top_degree_charge_mass=1,least_filling_cells=int(least)))
 return dict(top_degree=rows,anisotropic=[tensor_homotopy(['both','both'],[1,m]) for m in [3,7,11]])

def run():
 return dict(relative_homotopies=[tensor_homotopy(['both']*3,2),tensor_homotopy(['both']*4,1),tensor_homotopy(['left','absolute','absolute'],2),tensor_homotopy(['absolute']*3,2)],boundary_controls=boundary_controls(),hodge_and_source=hodge_and_source(),electric_extension=electric_extension())
if __name__=='__main__':
 rows=run();Path(__file__).with_name('BLOCK17_CHECKS.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
