#!/usr/bin/env python3
"""Exact-rational residual certificate for a fixed on-shell scattering point.

mpmath proposes square roots and inverses. Exact Fraction residuals, positivity
bounds and Neumann/Sylvester inequalities certify the result; no mpmath output
is trusted as an error estimate. This certifies one energy, not a wavepacket.
"""
from fractions import Fraction as F
from pathlib import Path
import json,math,time,sys,hashlib
import numpy as np
import mpmath as mp

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'evidence'; mp.mp.dps=90
start=time.monotonic(); fit=json.loads((OUT/'ladder_refinement.json').read_text())
DEN=10**15;CERTDEN=10**55
def rat_float(x): return F(round(float(x)*DEN),DEN)
def mpq(q):return mp.mpf(q.numerator)/q.denominator
def rounded(x):return F(int(mp.nint(x*CERTDEN)),CERTDEN)
def zeros(n,m=None):return np.full((n,n if m is None else m),F(0),dtype=object)
def ident(n):
 a=zeros(n)
 for i in range(n):a[i,i]=F(1)
 return a
def norm(a):return max(sum(abs(q) for q in row) for row in a)
def cnorm(ar,ai):return max(sum(abs(q)+abs(t) for q,t in zip(rowr,rowi)) for rowr,rowi in zip(ar,ai))
def product(ar,ai,br,bi):return ar@br-ai@bi, ar@bi+ai@br
def compact(q):return dict(rational=str(q),upper_float=float(q))

x=[rat_float(v) for v in fit['x']]
q=rat_float(math.tan((math.pi-fit['x'][1])/2))
cos=(q*q-1)/(q*q+1);sin=2*q/(q*q+1)
J=x[0];eps=2*J*(1-cos)
gA,gB,t,la,u,extraA,extraB=x[2:9];lb,mu0,mu1=x[9:]
dA=2+eps+F(1,20)+extraA;dB=2+eps+F(1,20)+extraB
reserve=max(F(0),-mu0)+max(F(0),-mu1)
params=dict(J=J,cos_k=cos,sin_k=sin,tan_half_complement=q,epsilon=eps,gA=gA,gB=gB,
 t=t,lambdaA=la,lambdaB=lb,u=u,DeltaA=dA,DeltaB=dB,mu0=mu0,mu1=mu1,scalar_reserve=reserve)
assert cos*cos+sin*sin==1 and sin>0
assert 0<J<F(1,2) and min(dA,dB)>2+4*J
I2=ident(2);I4=ident(4);I8=ident(8);I16=ident(16)
X=zeros(2);X[0,1]=X[1,0]=F(1);Z=np.diag([F(1),F(-1)])
nA=np.diag([F(0),F(0),F(1),F(1)]);nB=np.diag([F(0),F(1),F(0),F(1)])
hop=zeros(4);hop[1,2]=hop[2,1]=F(1)
XA=np.kron(X,I2);XB=np.kron(I2,X)
VA=la*np.kron(I4+XA,I2)+mu0*I8
VB=lb*np.kron(I4+XB,I2)+mu1*I8
rows=[];rapp={};rerr={}
for p in [1,-1]:
 C=(dA+gA)*nA+(dB+gB)*nB+t*(nA+nB-hop)+u*nA@nB
 G=gA*nA+p*gB*nB
 B=np.kron(I4,2*I2+Z)+np.kron(C,I2)+np.kron(G,X)
 for s in [1,-1]:
  iss=0 if s==1 else 1;E=2+s+eps
  D=B[2:,2:]+(2*J-E)*ident(6)
  dl=1+min(dA,dB)+2*J-E
  assert dl>2*J
  A=D@D-4*J*J*ident(6)
  dm=mp.matrix([[mpq(v) for v in row] for row in D]);ev,U=mp.eigsy(dm)
  Sm=U*mp.diag([mp.sqrt(v*v-4*mpq(J)**2) for v in ev])*U.T
  S=np.array([[rounded(Sm[i,j]) for j in range(6)] for i in range(6)],dtype=object)
  assert np.array_equal(S,S.T)
  residual_root=norm(S@S-A)
  S_lower=dl-norm(S-D);trueS_lower=dl-2*J
  assert S_lower>0
  root_error=residual_root/(S_lower+trueS_lower)
  # Symmetric 6x6 matrix: ||R||2<=||R||infty and ||error||infty<=sqrt(6)||error||2<3||error||2.
  source_F_error=F(3,2)*root_error
  Do=(2-s)+2*J-E
  assert abs(Do)>2*J
  Ao=Do*Do-4*J*J;So=rounded(mp.sqrt(mpq(Ao)))
  other_error=abs(So*So-Ao)/(So+abs(Do)-2*J)/2
  Fr=zeros(8);Fi=zeros(8)
  Fr[iss,iss]=-J*cos;Fi[iss,iss]=J*sin
  Fr[1-iss,1-iss]=-(Do+(1 if Do>0 else -1)*So)/2
  Fr[2:,2:]=-(D+S)/2
  Mr=zeros(16);Mi=zeros(16)
  Mr[:8,:8]=(E-2*J)*I8-B-VA
  Mr[:8,8:]=J*I8;Mr[8:,:8]=J*I8;Mr[8:,8:]=Fr-VB
  Mi[8:,8:]=Fi
  mm=mp.matrix([[mpq(Mr[i,j])+1j*mpq(Mi[i,j]) for j in range(16)] for i in range(16)])
  inv=mm**-1
  Nr=np.array([[rounded(mp.re(inv[i,j])) for j in range(16)] for i in range(16)],dtype=object)
  Ni=np.array([[rounded(mp.im(inv[i,j])) for j in range(16)] for i in range(16)],dtype=object)
  rr,ri=product(Mr,Mi,Nr,Ni)
  gamma=cnorm(I16-rr,-ri)
  assert gamma<1
  inv_approx=cnorm(Nr,Ni)/(1-gamma)
  deltaM=max(source_F_error,other_error)
  assert inv_approx*deltaM<1
  inv_true=inv_approx/(1-inv_approx*deltaM)
  br=zeros(16,1);bi=zeros(16,1);bi[8+iss,0]=2*J*sin
  xm=inv*mp.matrix([mpq(br[i,0])+1j*mpq(bi[i,0]) for i in range(16)])
  xr=np.array([[rounded(mp.re(v))] for v in xm],dtype=object)
  xi=np.array([[rounded(mp.im(v))] for v in xm],dtype=object)
  axr,axi=product(Mr,Mi,xr,xi)
  state_residual=cnorm(axr-br,axi-bi)
  state_error=inv_true*(state_residual+deltaM*cnorm(xr,xi))
  ar=xr[8+iss,0]-1;ai=xi[8+iss,0]
  rapp[s,p]=(ar,ai);rerr[s,p]=state_error
  rows.append(dict(s=s,p=p,energy=compact(E),source_threshold_lower=compact(1+min(dA,dB)),
   source_gap_lower=compact(1+min(dA,dB)-E),D_lower=compact(dl),sqrt_candidate_lower=compact(S_lower),
   sqrt_residual_infinity=compact(residual_root),sqrt_operator_error=compact(root_error),
   inverse_residual_infinity=compact(gamma),inverse_infinity_bound=compact(inv_true),
   boundary_matrix_error_infinity=compact(deltaM),state_residual_infinity=compact(state_residual),
   reflection_error=compact(state_error),reflection_real=str(ar),reflection_imag=str(ai)))
alpha=rapp[-1,-1];aerr=rerr[-1,-1];errors=[]
for s in [1,-1]:
 for p in [1,-1]:
  wr,wi=(F(-7,25),F(24,25)) if p==1 else (F(1),F(0))
  tr=wr*alpha[0]-wi*alpha[1];ti=wr*alpha[1]+wi*alpha[0]
  er,ei=rapp[s,p][0]-tr,rapp[s,p][1]-ti
  # l1 complex bound, plus rigorous reflection errors; |w|=1 exactly.
  bound=abs(er)+abs(ei)+rerr[s,p]+aerr
  errors.append(dict(s=s,p=p,bound=compact(bound)))
maxerror=max(F(v['bound']['rational']) for v in errors)
assert maxerror<F(52,10**14)
loads=dict(old1_added=2*gA,old2_added=2*gB,old_edge_separate=F(3),
 A=dA+2*gA+2*t+u+2*la,B=dB+2*gB+2*t+u+2*lb,
 clock0=3*J+2*la+abs(mu0),clock1=4*J+2*lb+abs(mu1),clock_tail=4*J)
result=dict(claim='Exact rational on-shell residual certificate only; finite wavepacket theorem pending',
 exact_parameters={k:str(v) for k,v in params.items()},parameter_floats={k:float(v) for k,v in params.items()},
 coefficient_rounding_denominator=DEN,certificate_rounding_denominator=CERTDEN,
 dimension_per_p=8,boundary_dimension_per_p=16,physical_source_old_dimension=16,
 source_threshold_gap_entire_clock_band=compact(min(dA,dB)-2-4*J),
 old_energy_band_separation=compact(2-4*J),channels=rows,comparison_errors=errors,
 certified_point_isometry_error=compact(maxerror),outgoing_clock_phase='alpha = exact r_(s=-1,p=-1)(k0)',
 actual_positive_onsite_scalar=compact(reserve),added_incident_block_norms={k:compact(v) for k,v in loads.items()},
 versions=dict(python=sys.version,numpy=np.__version__,mpmath=mp.__version__,mpmath_dps=mp.mp.dps),
 elapsed_seconds=time.monotonic()-start)
(OUT/'rational_point_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(certified_point_error_upper=float(maxerror),coefficient_denominator=DEN,
 source_gap_entire_band=float(min(dA,dB)-2-4*J),old_band_separation=float(2-4*J),
 maximum_inverse_infinity=max(v['inverse_infinity_bound']['upper_float'] for v in rows),
 maximum_reflection_certificate_error=max(v['reflection_error']['upper_float'] for v in rows),
 parameters={k:float(v) for k,v in params.items()},loads={k:float(v) for k,v in loads.items()},
 elapsed_seconds=result['elapsed_seconds']),indent=2))
