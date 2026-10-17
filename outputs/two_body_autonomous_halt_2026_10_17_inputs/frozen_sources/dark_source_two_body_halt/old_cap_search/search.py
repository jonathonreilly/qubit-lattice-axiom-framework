#!/usr/bin/env python3
"""Bounded discovery search with gA,gB<=1 and whole-band source closure.

No imports from the immutable witness. Outputs remain in this directory.
The numerical optimizer is discovery only; no interval/rational certificate.
"""
import sys
sys.dont_write_bytecode=True
import json,time,datetime,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import least_squares
ROOT=Path(__file__).resolve().parent
I2=np.eye(2);I4=np.eye(4);I8=np.eye(8)
X=np.array([[0.,1.],[1.,0.]]);Z=np.diag([1.,-1.])
nA=np.diag([0.,0.,1.,1.]);nB=np.diag([0.,1.,0.,1.])
hop=np.zeros((4,4));hop[1,2]=hop[2,1]=1.
XA=np.kron(X,I2);XB=np.kron(I2,X)
w=(-7+24j)/25;theta=np.angle(w);MARGIN=.05
calls=0

def physical(x):
 J,k,gA,gB,h,la,u,ea,eb,lb,m0,m1=x
 return dict(J=J,k=k,gA=gA,gB=gB,h=h,lambdaA=la,lambdaB=lb,u=u,
  DeltaA=2+4*J+MARGIN+ea,DeltaB=2+4*J+MARGIN+eb,mu0=m0,mu1=m1)

def reflect_physical(P,details=False):
 J=P['J'];k=P['k'];eps=2*J*(1-np.cos(k));rr=np.zeros((2,2),complex);info=[]
 gA=P['gA'];gB=P['gB'];h=P['h'];u=P['u']
 VA=P['lambdaA']*np.kron(I4+XA,I2)+P['mu0']*I8
 VB=P['lambdaB']*np.kron(I4+XB,I2)+P['mu1']*I8
 C=(P['DeltaA']+gA)*nA+(P['DeltaB']+gB)*nB+h*(nA+nB-hop)+u*nA@nB
 for ip,p in enumerate([1,-1]):
  B=np.kron(I4,2*I2+Z)+np.kron(C,I2)+np.kron(gA*nA+p*gB*nB,X)
  ev,U=np.linalg.eigh(B)
  for iss,s in enumerate([1,-1]):
   E=2+s+eps;d=(ev+2*J-E)/J;op=abs(d)<2
   f=np.empty(8,complex)
   f[op]=-J/2*(d[op]-1j*np.sqrt(4-d[op]**2))
   f[~op]=-J/2*(d[~op]+np.sign(d[~op])*np.sqrt(d[~op]**2-4))
   D=(E-2*J)*I8-B
   M=np.block([[D-VA,J*I8],[J*I8,(U*f)@U.T-VB]])
   rhs=np.zeros(16,complex);rhs[8+iss]=2j*J*np.sin(k)
   state=np.linalg.solve(M,rhs);rr[iss,ip]=state[8+iss]-1
   if details:
    info.append(dict(s=s,p=p,open_channels=int(op.sum()),energy=float(E),
     bulk_Q_gap=float(np.linalg.eigvalsh(B[2:,2:])[0]-E),
     inverse_norm_infinity=float(np.linalg.norm(np.linalg.inv(M),np.inf)),
     condition_2=float(np.linalg.cond(M)),unitarity_defect=float(abs(abs(rr[iss,ip])-1))))
 return (rr,info) if details else rr

def residual(x):
 global calls
 calls+=1
 r=reflect_physical(physical(x))
 return np.array([np.angle(r[0,0]/r[0,1]/w),np.angle(r[1,0]/r[1,1]/w),np.angle(r[0,1]/r[1,1])])

def loads(P):
 return dict(old1_added=2*P['gA'],old2_added=2*P['gB'],old_edge_separate=3.,
  A=P['DeltaA']+2*P['gA']+2*P['h']+P['u']+2*P['lambdaA'],
  B=P['DeltaB']+2*P['gB']+2*P['h']+P['u']+2*P['lambdaB'],
  clock0=3*P['J']+2*P['lambdaA']+abs(P['mu0']),
  clock1=4*P['J']+2*P['lambdaB']+abs(P['mu1']),tail=4*P['J'])

def describe(x):
 P=physical(x);r,info=reflect_physical(P,True);alpha=r[1,1]
 target=np.array([[w,1],[w,1]])*alpha
 return dict(x=x.tolist(),physical={k:float(v) for k,v in P.items()},
  residual=residual(x).tolist(),phase_residual_norm=float(np.linalg.norm(residual(x))),
  numerical_target_error=float(np.max(abs(r-target))),
  r_real=r.real.tolist(),r_imag=r.imag.tolist(),channels=info,
  source_gap_entire_band=float(min(P['DeltaA'],P['DeltaB'])-2-4*P['J']),
  old_band_separation=float(2-4*P['J']),positive_vacancy_scalar=float(max(0,-P['mu0'])+max(0,-P['mu1'])),
  added_incident_loads={k:float(v) for k,v in loads(P).items()})

def main():
 global calls
 started=time.monotonic();seed=2026101603;rng=np.random.default_rng(seed)
 initial_time=datetime.datetime.now(datetime.timezone.utc).isoformat()
 lo=np.array([.03,.08,.005,.005,.001,.001,0,0,0,.001,-4,-4])
 hi=np.array([.49,np.pi-.003,1.,1.,4.,4.,4.,4.,4.,4.,4.,4.])
 rows=[];best=None;total_optimizer_calls=0
 for i in range(60):
  # Thirty modest boxes first. The remaining starts allow a stated larger box.
  box='modest' if i<30 else 'expanded'
  lower=lo.copy();upper=hi.copy()
  if i>=30:
   upper[4:10]=[10,10,10,8,8,10];lower[10:]=[-10,-10];upper[10:]=[10,10]
  if i==0:
   x=np.array([.388903,3.06159,1.,.493479,1.,.359303,.749770,.5,.5,2.497330,.520036,-.151066])
  elif i==1:
   x=np.array([.388903,3.06159,1.,1.,4.,.359303,0,.05,.05,2.497330,.520036,-.151066])
  elif i==2:
   x=np.array([.3,np.pi-.02,1.,1.,1.,.2,0,0,0,.7,.3,-.2])
  elif best is not None and i%3==0:
   x=np.array(best['x'])
   x+=rng.normal(0,.12,len(x))*(upper-lower)
  else:
   x=lower+(upper-lower)*rng.random(12)
   x[1]=np.pi-np.exp(rng.uniform(np.log(.0031),np.log(1.4)))
   x[2:4]=rng.uniform(.3,1,2)
   x[4:6]=np.exp(rng.uniform(np.log(.02),np.log(upper[4]),2))
   x[9]=np.exp(rng.uniform(np.log(.02),np.log(upper[9])))
   x[7:9]=rng.uniform(0,min(2,upper[7]),2)
   x[10:12]=rng.uniform(-1,1,2)
  x=np.maximum(lower+1e-10,np.minimum(upper-1e-10,x))
  count0=calls;ts=time.monotonic()
  try:
   sol=least_squares(residual,x,bounds=(lower,upper),max_nfev=500,ftol=2e-11,xtol=2e-11,gtol=2e-11)
   ncall=calls-count0;total_optimizer_calls+=ncall
   row=describe(sol.x)
   row.update(index=i,box=box,lower=lower.tolist(),upper=upper.tolist(),initial=x.tolist(),
    nfev_reported=int(sol.nfev),actual_optimizer_residual_calls=ncall,success=bool(sol.success),
    message=str(sol.message),elapsed_seconds=time.monotonic()-ts)
   if best is None or row['numerical_target_error']<best['numerical_target_error']:
    best=row
    print(json.dumps({'new_best':i,'error':best['numerical_target_error'],'phase_norm':best['phase_residual_norm'],
     'loads':best['added_incident_loads'],'x':best['x']}),flush=True)
  except Exception as e:
   row=dict(index=i,box=box,initial=x.tolist(),failure=repr(e),elapsed_seconds=time.monotonic()-ts,
    actual_optimizer_residual_calls=calls-count0)
  rows.append(row)
  partial=dict(kind='bounded numerical discovery; no certificate',seed=seed,started_utc=initial_time,
   limits=dict(max_starts=60,max_nfev_per_start=500,wall_checkpoint_seconds=180,
     checkpoint='checked between completed starts; one running start may overrun',gA_max=1,gB_max=1,
     source_margin_formula='min Delta >= 2+4J+0.05',maximum_boundary_dimension=16),
   versions=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform()),
   actual_residual_calls_including_detail_evaluations=calls,total_optimizer_residual_calls=total_optimizer_calls,
   elapsed_seconds=time.monotonic()-started,completed_starts=len(rows),best=best,rows=rows)
  (ROOT/'SEARCH.json').write_text(json.dumps(partial,indent=2)+'\n')
  if time.monotonic()-started>=180:break
  if best is not None and best['numerical_target_error']<1e-9:
   # Keep several opportunities to reduce source loads even after a good fit.
   if i>=9:break
 print(json.dumps({'completed_starts':len(rows),'elapsed_seconds':partial['elapsed_seconds'],
  'optimizer_residual_calls':total_optimizer_calls,'best':best}),flush=True)

if __name__=='__main__':main()
