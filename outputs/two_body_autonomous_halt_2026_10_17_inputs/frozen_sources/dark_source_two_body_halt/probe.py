#!/usr/bin/env python3
"""Finite-channel dark-source search; numerical discovery, no certificate."""
import json, time, sys, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import least_squares

OUT=Path(__file__).resolve().parent/'evidence'
I2=np.eye(2); X=np.array([[0.,1.],[1.,0.]]); Z=np.diag([1.,-1.])
I4=np.eye(4); I8=np.eye(8)
nA=np.diag([0.,0.,1.,1.]); nB=np.diag([0.,1.,0.,1.])
hop=np.zeros((4,4)); hop[1,2]=hop[2,1]=1.
XA=np.kron(X,I2)
THETA=np.angle((-7+24j)/25)

def parameters(x):
    # Positive blocks, fixed finite search box. Penalties place every excited
    # source threshold strictly above both chosen incoming total energies.
    J,k,gA,gB,t,lam,u,extraA,extraB=x
    eps=2*J*(1-np.cos(k))
    dA=2+eps+.05+extraA; dB=2+eps+.05+extraB
    return J,k,gA,gB,t,lam,u,dA,dB

def model(p,prm):
    J,k,gA,gB,t,lam,u,dA,dB=prm
    C=(dA+gA)*nA+(dB+gB)*nB+t*(nA+nB-hop)+u*nA@nB
    F=gA*nA+p*gB*nB
    B=np.kron(I4,2*I2+Z)+np.kron(C,I2)+np.kron(F,X)
    V=lam*np.kron(I4+XA,I2)
    return B,V

def reflection(prm,details=False):
    J,k,*_=prm; eps=2*J*(1-np.cos(k)); rr=np.zeros((2,2),complex)
    info=[]
    for ip,p in enumerate([1,-1]):
      B,V=model(p,prm); ev,U=np.linalg.eigh(B)
      for iss,s in enumerate([1,-1]):
        E=2+s+eps; d=(ev+2*J-E)/J
        op=np.abs(d)<2
        f=np.empty(8,complex)
        f[op]=-J/2*(d[op]-1j*np.sqrt(4-d[op]**2))
        f[~op]=-J/2*(d[~op]+np.sign(d[~op])*np.sqrt(d[~op]**2-4))
        M=(U*f)@U.T-V
        a=np.eye(8)[:,iss]
        state=np.linalg.solve(M,2j*J*np.sin(k)*a)
        rr[iss,ip]=state[iss]-1
        if details:
          coeff=U.T@(state-a)
          radii=np.abs(-J/f[~op])
          excited_ev=np.linalg.eigvalsh(B[2:,2:])
          info.append(dict(s=s,p=p,E=float(E),source_gap=float(excited_ev[0]-E),
            open_channels=int(op.sum()),modulus_error=float(abs(abs(rr[iss,ip])-1)),
            maximum_closed_radius=float(max(radii)),boundary_source_norm=float(np.linalg.norm(state[2:])),
            boundary_opposite_old_norm=float(abs(state[1-iss])),
            matrix_condition=float(np.linalg.cond(M))))
    return (rr,info) if details else rr

def residual(x):
    r=reflection(parameters(x))
    return np.array([np.angle(r[0,0]/r[0,1]*np.exp(-1j*THETA)),
      np.angle(r[1,0]/r[1,1]*np.exp(-1j*THETA)),np.angle(r[0,1]/r[1,1])])

def main():
    start=time.monotonic(); seed=20261016; rng=np.random.default_rng(seed)
    lower=np.array([.03,.08,.001,.001,.001,.001,0,0,0])
    upper=np.array([.49,np.pi-.08,20,20,20,20,20,20,20])
    rows=[]; best=None
    for i in range(80):
      x=lower+(upper-lower)*rng.random(9)
      # log-wide sample couplings while retaining bounds.
      x[2:6]=np.exp(rng.uniform(np.log(.01),np.log(20),4))
      sol=least_squares(residual,x,bounds=(lower,upper),max_nfev=350,
        ftol=2e-10,xtol=2e-10,gtol=2e-10)
      r,info=reflection(parameters(sol.x),True)
      row=dict(index=i,x=sol.x.tolist(),physical_parameters=list(parameters(sol.x)),
        residual=sol.fun.tolist(),norm=float(np.linalg.norm(sol.fun)),nfev=sol.nfev,
        success=bool(sol.success),r_real=r.real.tolist(),r_imag=r.imag.tolist(),channels=info)
      rows.append(row)
      if best is None or row['norm']<best['norm']:
        best=row; print(json.dumps({'new_best':i,'norm':best['norm'],'residual':best['residual'],'physical_parameters':best['physical_parameters']}),flush=True)
      if time.monotonic()-start>180: break
    result=dict(kind='bounded numerical optimization, not impossibility or existence proof',
      seed=seed,max_starts=80,max_nfev_per_start=350,wall_cap_seconds=180,
      lower=lower.tolist(),upper=upper.tolist(),columns=['J','k','gA','gB','t','lambda','u','extraA','extraB'],
      dimension_per_XX_block=8,full_internal_dimension=16,clock='infinite half-line, analytic surface root',
      versions=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform()),
      elapsed_seconds=time.monotonic()-start,best=best,rows=rows)
    (OUT/'optimization.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'completed_starts':len(rows),'elapsed_seconds':result['elapsed_seconds'],'best':best}),flush=True)

if __name__=='__main__': main()
