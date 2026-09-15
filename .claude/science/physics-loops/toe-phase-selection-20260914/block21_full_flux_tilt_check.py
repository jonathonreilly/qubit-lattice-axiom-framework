#!/usr/bin/env python3
"""Personal finite checks of the full compact-U(1) auxiliary tilt.
No finite calculation proves the fixed-beta auxiliary central limit theorem.
"""
from pathlib import Path
import json, math, itertools
import numpy as np
import sympy as sp
from scipy.integrate import quad
from block17_local_source_check import cube


def exact_hodge():
 rows=[]
 for d in [3,4]:
  cells,ds=cube(d);B=ds[2];H=B*B.T
  if d>3:H+=ds[3].T*ds[3]
  G=H.inv();I=sp.eye(H.rows);c=sp.Rational(1,32);T=(I-c*H).inv()
  H1=ds[0]*ds[0].T+ds[1].T*ds[1]
  P=ds[1]*H1.inv()*ds[1].T;R=B.T*G*B
  assert P+R==sp.eye(B.cols) and P*R==sp.zeros(B.cols)
  assert G*T==G+c*T
  for beta in [sp.Rational(1,5),sp.Rational(3,2)]:
   A=beta*(G-c*I);h=sp.Matrix([sp.Rational((i*7)%11-5,17) for i in range(B.cols)])
   source=-sp.sqrt(beta)*G*B*h;j=A.inv()*source
   assert sp.simplify(j+T*B*h/sp.sqrt(beta))==sp.zeros(B.rows,1)
   assert sp.simplify((h.T*P*h+source.T*A.inv()*source)[0]-(h.T*h+c*h.T*B.T*T*B*h)[0])==0
   # Distinct covariance decompositions for arbitrary positive charge covariance.
   seed=sp.Matrix([[((i+2)*(j+3))%7-3 for j in range(3)] for i in range(B.rows)])
   V=seed*seed.T/sp.Integer(100000)
   Cphi=A-4*sp.pi**2*A*V*A
   Cx=sp.eye(B.cols)+c*B.T*T*B-B.T*T*Cphi*T*B/beta
   expected=P+4*sp.pi**2*beta*B.T*G*V*G*B
   assert sp.simplify(Cx-expected)==sp.zeros(B.cols)
  rows.append(dict(d=d,plaquettes=B.cols,three_cells=B.rows,hodge_spectrum={str(v):m for v,m in H.eigenvals().items()},exact_identities=True))
 return rows


def three_cube():
 # Positive Gaussian quadrature of the auxiliary phi density versus independent
 # magnetic and Poisson-comb formulae for the original full lifted flux.
 _,ds=cube(3);b=np.array(ds[2],dtype=float).ravel();P=np.eye(6)-np.outer(b,b)/6
 c=1/32;rows=[]
 for beta in [.1,.4,1.,3.]:
  A=beta*(1/6-c);T=1/(1-6*c)
  n=np.arange(-80,81,dtype=float);w=np.exp(-2*np.pi**2*beta*n*n/6);w/=w.sum()
  varq=float(w@(n*n))
  def theta(x):
   ls=np.arange(math.floor(x)-12,math.ceil(x)+13,dtype=float)
   return np.exp(-(x-ls)**2/(2*beta*c)).sum()/math.sqrt(2*np.pi*beta*c)
  # Integrate in standard-Gaussian coordinates, bounded interval has omitted
  # standard tail below 4e-33; shifted tilt checks keep the quadratic maximum
  # within this range. Repeat with width14 to challenge the truncation.
  def integral(j=0,power=0,width=12):
   return quad(lambda z: ((math.sqrt(A)*z)**power)*math.exp(-z*z/2+j*math.sqrt(A)*z)*theta(math.sqrt(A)*z)/math.sqrt(2*math.pi),-width,width,epsabs=2e-12,epsrel=2e-12,limit=400)[0]
  norm=integral();varphi=integral(power=2)/norm
  varexpected=A-4*np.pi**2*A*A*varq
  assert abs(varphi-varexpected)<2e-12
  for index,h in enumerate([np.array([.2,-.1,.3,.05,-.4,.15]),b*.11,P@np.array([.3,.4,-.2,.1,.15,.25])]):
   bh=float(b@h);s=-math.sqrt(beta)*bh/6;j=-T*bh/math.sqrt(beta)
   magnetic=math.exp(-float(h@P@h)/2)*float(w@np.cos(2*np.pi*n*s))
   comb=np.exp(-.5*np.sum((h[None,:]+n[:,None]*b[None,:]/math.sqrt(beta))**2,axis=1)).sum()/np.exp(-3*n*n/beta).sum()
   pref=math.exp(-float(h@h)/2-c*T*bh*bh/2)
   aux=pref*integral(j=j)/norm
   aux14=pref*integral(j=j,width=14)/integral(width=14)
   assert max(abs(magnetic-comb),abs(magnetic-aux),abs(aux-aux14))<4e-12
   wrong_sign=pref*quad(lambda z:math.cos(j*math.sqrt(A)*z)*math.exp(-z*z/2)*theta(math.sqrt(A)*z)/math.sqrt(2*math.pi),-12,12,epsabs=1e-12,limit=400)[0]/norm
   if index<2:assert abs(wrong_sign-aux)>1e-4
   rows.append(dict(beta=beta,source=index,magnetic=magnetic,poisson_comb=float(comb),positive_auxiliary_quad=aux,maximum_error=float(max(abs(magnetic-comb),abs(magnetic-aux))),cutoff_error=abs(aux-aux14),wrong_characteristic_instead_of_mgf_error=abs(wrong_sign-aux),aux_covariance_error=abs(varphi-varexpected)))
 return rows


def wedge_symmetry():
 # Every invariant real symmetric quadratic form on Lambda^2(R4) is scalar
 # under the full signed-permutation group. Test via exact linear constraints.
 pairs=list(itertools.combinations(range(4),2));basis=[]
 for i in range(6):
  for j in range(i,6):
   E=sp.zeros(6);E[i,j]=E[j,i]=1;basis.append(E)
 generators=[]
 for r in range(4):
  generators.append(sp.diag(*[(-1 if r in I else 1) for I in pairs]))
 for r in range(3):
  perm=list(range(4));perm[r],perm[r+1]=perm[r+1],perm[r];U=sp.zeros(6)
  for j,I in enumerate(pairs):
   image=tuple(perm[i] for i in I);K=tuple(sorted(image));U[pairs.index(K),j]=1 if image==K else -1
  generators.append(U)
 eq=[]
 for U in generators:
  mats=[U.T*E*U-E for E in basis]
  eq.extend([[m[i,j] for m in mats] for i in range(6) for j in range(6)])
 ker=sp.Matrix(eq).nullspace();assert len(ker)==1
 invariant=sum((ker[0][k]*E for k,E in enumerate(basis)),sp.zeros(6))
 assert invariant==invariant[0,0]*sp.eye(6) and invariant[0,0]!=0
 return dict(generators=len(generators),symmetric_parameters=len(basis),invariant_dimension=len(ker),scope='Quadratic-form algebra only; no homogenized energy existence or identification follows.')

if __name__=='__main__':
 result=dict(exact_hodge=exact_hodge(),three_cube=three_cube(),wedge_symmetry=wedge_symmetry(),qualification='Personal exact identities and distinct finite representations; fixed-beta vector auxiliary CLT and matched state limit not executed or established.')
 Path(__file__).with_name('BLOCK21_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
