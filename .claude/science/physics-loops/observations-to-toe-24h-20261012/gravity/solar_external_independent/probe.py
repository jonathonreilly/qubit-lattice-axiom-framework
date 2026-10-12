#!/usr/bin/env python3
"""Independent direct-Poisson and integration-by-parts Hessian quadratures."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre


def response(eta,order,cutoff=40.):
    z,w=roots_legendre(order)
    t=(z+1)/2;tw=w/2
    c=1-2*t*t;cw=4*t*tw
    total_parts=0.;total_direct=0.
    for lo,hi in ((0.,np.sqrt(eta)),(np.sqrt(eta),cutoff)):
        v=(lo+hi)/2+(hi-lo)/2*z;vw=(hi-lo)/2*w
        vv=v[:,None];cc=c[None,:]
        q=np.sqrt((vv*vv-eta)**2+2*eta*vv*vv*(1-cc))
        sq=np.sqrt(q)
        nm1=1/np.expm1(sq)
        derivative=-np.exp(-sq)/(2*sq*(-np.expm1(-sq))**2)
        angular_parts=nm1*(-vv*vv*(3*cc*cc-1)+eta*cc*(5*cc*cc-3))
        bracket=-2*vv**4+4*eta*cc*vv*vv+eta*eta*(1-3*cc*cc)
        angular_direct=derivative*vv*vv/q*bracket*(3*cc*cc-1)
        total_parts+=1.5*float(vw@(angular_parts@cw))
        total_direct-=.5*float(vw@(angular_direct@cw))
    bound=6*np.exp(np.sqrt(eta)-cutoff)*(cutoff**2+2*cutoff+2+eta)/(1-np.exp(-(cutoff-np.sqrt(eta))))
    return dict(eta=eta,order=order,h_parts=total_parts,h_direct=total_direct,
                disagreement=total_direct-total_parts,parts_tail_bound=float(bound))


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    rows=[response(eta,n) for eta in (.5,1.,2.,3.,4.) for n in (64,128,256,512)]
    result=dict(convention='h=Hzz*rM/a0 with acceleration=-grad(Phi); QPhi=3Hzz/2',
                candidate='QUMOND with nu=1/(1-exp(-sqrt(q)))',
                code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                derivation_sha256=hashlib.sha256(Path(__file__).with_name('DERIVATION.md').read_bytes()).hexdigest(),
                observational_target_used=False,results=rows)
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([r for r in rows if r['order']==512],indent=2))


if __name__=='__main__':main()
