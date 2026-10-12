"""Independent frozen QUMOND quadrupole quadratures; no parent code imports."""
from __future__ import annotations

import json
import math
import os
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
import hashlib

for _name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_name] = '1'
import numpy as np
import scipy
from scipy.special import roots_legendre
from scipy.optimize import brentq

RUNTIME=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=RUNTIME/'galaxy_response/solar_external'
GM=1.32712440018e20
PC=149597870700.0*648000.0/math.pi
A0_PRIMARY=7.658058668049826e-11
A0_FIXED_ML=8.533673475349299e-11

def checkpoint():
    now=datetime.now(timezone.utc)
    deadline=json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
    if now.timestamp()>=deadline or list(RUNTIME.glob('*STOP_REQUESTED*')):
        raise RuntimeError('Campaign deadline or stop marker reached')
    return now.isoformat()

def nu_minus_one(v):
    z=np.sqrt(v)
    return np.exp(-z)/(-np.expm1(-z))

def nu_prime(v):
    z=np.sqrt(v)
    return -np.exp(-z)/(2*z*np.expm1(-z)**2)

@lru_cache(maxsize=16)
def gauss(n):
    return roots_legendre(n)

def nodes(n, lo, hi):
    t,q=gauss(n)
    return (lo+hi)/2+(hi-lo)*t/2, q*(hi-lo)/2

def radial_edges(eta, cutoff):
    saddle=math.sqrt(eta)
    return sorted(set([0.0,cutoff]+[v for v in [saddle/2,saddle,1.5*saddle,2*saddle,4*saddle,8.0,16.0,32.0] if 0<v<cutoff]))

def response(eta, n=128, cutoff=60.0, form='ibp'):
    if eta==0:
        return 0.0
    if eta<0 or form not in ('ibp','density'):
        raise ValueError('eta positive and known form required')
    u,uq=nodes(n,0,math.sqrt(2))
    c=(1-u*u)[None,:]
    dcq=(2*u*uq)[None,:]
    edges=radial_edges(eta,cutoff)
    total=0.0
    for lo,hi in zip(edges[:-1],edges[1:]):
        w,wq=nodes(n,lo,hi)
        w=w[:,None]
        # This positive expression avoids cancellation at the saddle.
        v=np.hypot(w*w-eta, math.sqrt(2*eta)*w*u[None,:])
        if form=='ibp':
            baseline=nu_minus_one(np.hypot(w*w,eta))
            b=w*w*(3*c*c-1)+eta*(3*c-5*c**3)
            integrand=(9/4)*(nu_minus_one(v)-baseline)*b
        else:
            ur=w*w-eta*c
            p2=(3*c*c-1)/2
            integrand=(3/2)*p2*nu_prime(v)*(v*v-3*ur*ur)*w*w/v
        total+=float(np.sum(integrand*wq[:,None]*dcq))
    return total

def tail_bound(eta, cutoff):
    if cutoff<math.sqrt(2*eta):
        raise ValueError('tail inequality precondition')
    return 9*math.exp(eta/cutoff-cutoff)*(cutoff**2+2*cutoff+2+eta)/(-math.expm1(-math.sqrt(cutoff**2-eta)))

def eta_from_physical(a0, g, sigma=0.0):
    sb=2*math.pi*GM*sigma/(PC*PC*a0)
    target=g/a0
    def residual(eta):
        return eta*(1+float(nu_minus_one(math.hypot(eta,sb))))-target
    return brentq(residual,1e-14,max(target,1.0),xtol=5e-15,rtol=1e-14)

def prediction(a0,g,sigma=0.0,n=128):
    eta=eta_from_physical(a0,g,sigma)
    f=response(eta,n=n)
    q=a0**1.5/math.sqrt(GM)*f
    return dict(a0=a0,g_physical=g,sigma_Msun_pc2=sigma,eta_N=eta,F=f,Q2_s_m2=q,
                Hzz_s_m2=-2*q/3,physical_boost=g/(a0*eta))

def initial_diagnostics():
    started=checkpoint()
    rows=[]
    for eta in [0,0.5,1,1.5,2,3,5,10]:
        checkpoint()
        values=[]
        for n,cutoff in [(64,40.0),(128,40.0),(256,40.0),(256,60.0)]:
            values.append(dict(n=n,cutoff=cutoff,ibp=response(eta,n,cutoff,'ibp'),density=response(eta,n,cutoff,'density'),ibp_tail_bound=tail_bound(eta,cutoff)))
        rows.append(dict(eta=eta,values=values))
        print(json.dumps(rows[-1]),flush=True)
    payload=dict(started_at=started,finished_at=checkpoint(),numpy=np.__version__,scipy=scipy.__version__,definition='F=Q2*rM/a0; Hzz*rM/a0=-2F/3',rows=rows,
                 code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),parent_results_read=False)
    dest=OUT/'initial_numerical_results.json'
    if dest.exists():
        raise RuntimeError('Initial results already frozen; refusing overwrite')
    dest.write_text(json.dumps(payload,indent=2)+'\n')
    freeze=dict(frozen_at=checkpoint(),path=str(dest),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),parent_results_read=False)
    (OUT/'initial_numerical_freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
    print(json.dumps(freeze),flush=True)

if __name__=='__main__':
    initial_diagnostics()
