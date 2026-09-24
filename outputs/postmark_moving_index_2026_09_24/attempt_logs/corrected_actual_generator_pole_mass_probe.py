#!/usr/bin/env python3
"""Root-only diagnostic: compare actual H_S eigenvalues with deleted-anchor poles.

This measures prepared spectral mass by each full eigenvalue's distance to the
spectrum of H_II, normalized by its local full-spectrum spacing. It is a finite
floating-point discriminator, not a uniform estimate.
"""
import importlib.util, json, math
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal, expm

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('exact_runner',ROOT/'scripts/postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py')
runner=importlib.util.module_from_spec(spec); spec.loader.exec_module(runner)

ELL=(0,1,0,1,1); PI=(-1,0,0,0,1); RHO=(0,0,0,1,0)
def cas(c,m): return c-m*(m+1)

def one(S):
    c=S*(S+1); lo=-5*S; hi=5*S-4
    sites=np.arange(lo,hi+1,dtype=np.int64)
    d=np.zeros(len(sites)); e=np.zeros(len(sites)-1)
    for i,nv in enumerate(sites):
        k,s=divmod(int(nv),5)
        d[i]=cas(c,k+ELL[s])+cas(c,k+PI[s])
        if i<len(e):
            a=cas(c,k+ELL[s]); b=cas(c,k+RHO[s])
            if a<0 or b<0: raise ArithmeticError((S,int(nv),a,b))
            e[i]=-math.sqrt(a*b)
    # Independent coefficient-table cross-check against the current primary runner.
    rlo,rhi,rd,re,_=runner.finite_spin_matrix(S)
    coefficient_error=max(float(np.max(np.abs(d-c*rd))),float(np.max(np.abs(e-c*re))))
    ev,U=eigh_tridiagonal(d,e,eigvals_only=False,check_finite=True)
    a_ids=np.flatnonzero(sites%5==0)
    is_anchor=np.zeros(len(sites),dtype=bool); is_anchor[a_ids]=True
    pole_parts=[]
    start=None
    for i in range(len(sites)+1):
        inside=(i<len(sites) and not is_anchor[i])
        if inside and start is None: start=i
        if not inside and start is not None:
            stop=i
            block_d=d[start:stop]
            block_e=e[start:stop-1]
            pole_parts.append(eigh_tridiagonal(block_d,block_e,eigvals_only=True))
            start=None
    poles=np.sort(np.concatenate(pole_parts))
    gaps=np.min(np.abs(ev[:,None]-poles[None,:]),axis=1)
    local=np.empty_like(ev)
    local[0]=ev[1]-ev[0]; local[-1]=ev[-1]-ev[-2]
    local[1:-1]=np.minimum(ev[1:-1]-ev[:-2],ev[2:]-ev[1:-1])
    ratio=gaps/local
    z0=int(np.flatnonzero(sites==0)[0])
    p=np.abs(U[z0,:])**2
    mass_by_ratio={}
    for q in (1e-4,1e-3,1e-2,5e-2,1e-1,0.25,0.5):
        m=ratio<=q
        mass_by_ratio[str(q)]={"modes":int(m.sum()),"prepared_mass":float(p[m].sum())}
    relgap=gaps/c
    mass_by_c={}
    for q in (1e-6,1e-5,1e-4,1e-3):
        m=relgap<=q
        mass_by_c[str(q)]={"modes":int(m.sum()),"prepared_mass":float(p[m].sum())}
    v=np.exp(2j*np.pi*sites/3); o=(1+v+v.conj())/3
    # H=C*N has eigenvalue E, while the sourced generator is G=N^2-C*N.
    # Its exact phase is therefore exp[-it(E^2/C^2-E)].
    target_phase=np.exp(-0.25j*(ev**2/c**2-ev))
    coeff=target_phase*U[z0,:].conj()
    psi=U@coeff
    qchar=np.vdot(psi,v*psi)
    readout=float(np.vdot(psi,o*psi).real)
    dense_check=None
    if S<=5:
        N=np.diag(d/c)+np.diag(e/c,1)+np.diag(e/c,-1)
        G=N@N-c*N
        basis=np.zeros(len(sites),dtype=np.complex128); basis[z0]=1.0
        dense_psi=expm(-0.25j*G)@basis
        dense_check=float(abs(readout-np.vdot(dense_psi,o*dense_psi).real))
    return {"S":S,"dimension":len(sites),"anchor_count":len(a_ids),"pole_count":len(poles),
        "independent_coefficient_max_error":coefficient_error,
        "min_gap_abs":float(gaps.min()),"min_gap_over_C":float(relgap.min()),
        "min_gap_over_local_spacing":float(ratio.min()),
        "pole_neighborhood_prepared_mass_by_local_spacing":mass_by_ratio,
        "pole_neighborhood_prepared_mass_by_C_scale":mass_by_c,
        "target_generator":"G_S=N_S^2-C*N_S, evaluated via H_S=C*N_S eigenvalues",
        "target_phase":"exp(-it*(E^2/C^2-E)) for H_S eigenvalue E, t=1/4",
        "direct_actual_character_expectation":str(complex(qchar)),
        "direct_actual_period_three_readout":readout,
        "dense_expm_readout_error_when_S_le_5":dense_check,
        "scope":"Finite target-generator readout, eigenspectrum and prepared weights only; no uniform pole-mass or phase-cancellation result."}

if __name__=='__main__':
 print(json.dumps({"base":"0e6ad8285096ed668816f18caaa6fbbfbd9c50e8","method":"independent five-residue Jacobi build; tridiagonal eigensolver; each H_II block diagonalized separately; coefficients cross-checked against primary runner; target phases checked against dense expm for S<=5","rows":[one(S) for S in (1,2,3,5,8,16,32,64,128,256,512)]},indent=2,sort_keys=True))
