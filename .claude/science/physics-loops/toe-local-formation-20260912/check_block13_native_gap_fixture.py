#!/usr/bin/env python3
"""Literal finite native determinant and separate small Fock energy check."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
from itertools import product
from pathlib import Path
import json,time
import numpy as np
import sympy as s
from check_block12_soft_diagnostic import car
from verify_block12_sign_witness import sha
HERE=Path(__file__).resolve().parent


def run():
    started=time.monotonic();checks=[];finite_shifts=[];L=4;points=list(product(range(L),repeat=3));ix={r:j for j,r in enumerate(points)};M=L**3
    K=np.zeros((M,M))
    for r in points:
        for ax in range(3):
            v=list(r);v[ax]=(v[ax]+1)%L
            sign=(-1)**sum(r[:ax])*(-1 if r[ax]==L-1 else 1)
            K[ix[r],ix[tuple(v)]]=sign;K[ix[tuple(v)],ix[r]]=-sign
    e=np.eye(M)[:,0];old=np.linalg.eigvalsh(1j*K)
    for kind,sites in {'P':((1,0,0),(0,1,0)),'O':((1,0,0),(L-1,0,0))}.items():
        d=np.zeros(M)
        for site in sites:d[ix[site]]=-K[0,ix[site]]
        delta=2*(np.outer(e,d)-np.outer(d,e));changed=K+delta
        new=np.linalg.eigvalsh(1j*changed);shift=(sum(abs(old))-sum(abs(new)))/4
        assert abs(shift-(np.sqrt(6)-2))<1e-12
        finite_shifts.append(shift)
        checks.append({'name':kind+'_finite_full_skew_energy','gap':shift})
        for ss in (0.,.5,1.,2.,4.):
            A=float(e@np.linalg.solve(ss*ss*np.eye(M)-K@K,e));z=ss*ss*A
            expected=1-8*(1-z)**2/9 if kind=='O' else (1+2*z)**2/9+8*ss*ss*A*A
            before=np.linalg.slogdet(ss*np.eye(M)-K);after=np.linalg.slogdet(ss*np.eye(M)-changed)
            ratio=after[0]/before[0]*np.exp(after[1]-before[1]);assert abs(ratio-expected)<1e-12
            checks.append({'name':kind+'_finite_determinant','s':ss,'absolute_error':abs(ratio-expected)})
        mutant=K+delta/2
        ratio=np.exp(np.linalg.slogdet(np.eye(M)-mutant)[1]-np.linalg.slogdet(np.eye(M)-K)[1])
        A=1/7;expected=1-8*(1-A)**2/9
        assert abs(ratio-expected)>1e-3
    # An independent two-mode Fock Hamiltonian realizes the L4 active pair.
    f=car(2);omega=s.sqrt(6);g=f[0]+f[0].T
    b0=s.I*(f[0].T-f[0]);b1=s.I*(f[1].T-f[1]);d=-omega*(b0+s.sqrt(2)*b1)/3
    H=omega*(f[0].T*f[0]+f[1].T*f[1]);D=H+s.I*g*d
    eigen=list(D.eigenvals());minimum=min(eigen,key=lambda x:float(x))
    assert s.simplify(D.det()-8)==0
    assert omega-2 in eigen and all(float(v)>=float(omega-2)-1e-14 for v in eigen)
    for full_trace_shift in finite_shifts:
        assert abs(full_trace_shift-float(minimum))<1e-12
        assert abs(full_trace_shift/2-float(minimum))>1e-3
    checks.append({'name':'independent_small_Fock_minimum','exact':'sqrt6-2','wrong_half_energy_rejected':True})
    return {'status':'passed','count':len(checks),'checks':checks,'half_bond_reversal_mutant_rejected':True,
            'seconds':time.monotonic()-started,'source_sha256':sha(__file__),
            'scope':'finite native determinant/Fock normalization checks; no extrapolated infinite gap'}


if __name__=='__main__':
    result=run();(HERE/'BLOCK13_NATIVE_GAP_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count'],'checks',result['seconds'],'seconds')
