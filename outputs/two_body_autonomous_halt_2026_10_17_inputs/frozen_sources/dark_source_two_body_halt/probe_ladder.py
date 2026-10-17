#!/usr/bin/env python3
"""Two clock contacts on the strict square ladder; discovery only."""
import json,time,sys
import numpy as np
from scipy.optimize import least_squares
import probe as base

XB=np.kron(base.I2,base.X)
def reflection(x,details=False):
    prm=base.parameters(x[:9]); J,k=prm[:2]; eps=2*J*(1-np.cos(k))
    lamB,mu0,mu1=x[9:]
    rr=np.zeros((2,2),complex); info=[]
    for ip,p in enumerate([1,-1]):
      B,VA=base.model(p,prm); VA=VA+mu0*base.I8
      VB=lamB*np.kron(base.I4+XB,base.I2)+mu1*base.I8
      ev,U=np.linalg.eigh(B)
      for iss,s in enumerate([1,-1]):
        E=2+s+eps; d=(ev+2*J-E)/J; op=np.abs(d)<2
        f=np.empty(8,complex)
        f[op]=-J/2*(d[op]-1j*np.sqrt(4-d[op]**2))
        f[~op]=-J/2*(d[~op]+np.sign(d[~op])*np.sqrt(d[~op]**2-4))
        D=E*base.I8-2*J*base.I8-B
        M=np.block([[D-VA,J*base.I8],[J*base.I8,(U*f)@U.T-VB]])
        a=np.eye(8)[:,iss]; rhs=np.concatenate([np.zeros(8),2j*J*np.sin(k)*a])
        state=np.linalg.solve(M,rhs); rr[iss,ip]=state[8+iss]-1
        if details:
          info.append(dict(s=s,p=p,E=float(E),source_gap=float(np.linalg.eigvalsh(B[2:,2:])[0]-E),
            open_channels=int(op.sum()),modulus_error=float(abs(abs(rr[iss,ip])-1)),
            maximum_closed_radius=float(max(abs(-J/f[~op]))),
            matrix_condition=float(np.linalg.cond(M)),
            boundary_source_norm=float(np.linalg.norm(np.r_[state[2:8],state[10:16]]))))
    return (rr,info) if details else rr

def residual(x):
    r=reflection(x)
    return np.array([np.angle(r[0,0]/r[0,1]*np.exp(-1j*base.THETA)),
       np.angle(r[1,0]/r[1,1]*np.exp(-1j*base.THETA)),np.angle(r[0,1]/r[1,1])])

def main():
    start=time.monotonic(); seed=2026101602;rng=np.random.default_rng(seed)
    lower=np.array([.03,.08,.001,.001,.001,.001,0,0,0,.001,0,0])
    upper=np.array([.49,np.pi-.08,20,20,20,20,20,20,20,20,10,10])
    rows=[];best=None
    for i in range(120):
      x=lower+(upper-lower)*rng.random(12)
      x[2:6]=np.exp(rng.uniform(np.log(.01),np.log(20),4))
      x[9]=np.exp(rng.uniform(np.log(.01),np.log(20)))
      x[10:12]=rng.uniform(0,.7,2)
      sol=least_squares(residual,x,bounds=(lower,upper),max_nfev=350,ftol=1e-11,xtol=1e-11,gtol=1e-11)
      r,info=reflection(sol.x,True)
      row=dict(index=i,x=sol.x.tolist(),residual=sol.fun.tolist(),norm=float(np.linalg.norm(sol.fun)),
        nfev=sol.nfev,success=bool(sol.success),r_real=r.real.tolist(),r_imag=r.imag.tolist(),channels=info)
      rows.append(row)
      if best is None or row['norm']<best['norm']:
        best=row; print(json.dumps({'new_best':i,'norm':best['norm'],'residual':best['residual'],'x':best['x']}),flush=True)
      if row['norm']<1e-9 or time.monotonic()-start>180:break
    result=dict(kind='bounded numerical search, not proof',seed=seed,max_starts=120,
      max_nfev_per_start=350,wall_cap_seconds=180,elapsed_seconds=time.monotonic()-start,
      lower=lower.tolist(),upper=upper.tolist(),columns=['J','k','gA','gB','t','lambdaA','u','extraA','extraB','lambdaB','mu0','mu1'],
      dimension_per_XX_block=16,full_internal_dimension=32,versions=dict(python=sys.version,numpy=np.__version__),
      best=best,rows=rows)
    (base.OUT/'ladder_optimization.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'completed_starts':len(rows),'best':best,'elapsed_seconds':result['elapsed_seconds']}),flush=True)
if __name__=='__main__':main()
