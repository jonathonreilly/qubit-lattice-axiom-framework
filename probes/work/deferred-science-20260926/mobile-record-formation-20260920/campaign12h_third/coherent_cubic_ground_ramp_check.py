#!/usr/bin/env python3
"""Finite cubic coherent preparation with an exact integer gap certificate.

Floating eigensolvers propose bases only. Integer residual/Gram certificates
bound every eigenvalue at dyadic grid points, and a Lipschitz bound covers
the intervals. Time evolution is a separate converged numerical control.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np
import scipy.linalg as la
import scipy.sparse as ss
from scipy.integrate import solve_ivp

import local_gauge_record_cooling_check as base

OUT=Path(__file__).resolve().parent


def exact_integer_eigen_certificate(a_integer,denominator,values,vectors,bits=22):
    n=len(values);scale=1<<bits
    q=np.rint(vectors*scale).astype(np.int64)
    lam=np.rint(values*scale).astype(np.int64)
    assert np.all(lam[:-1]<=lam[1:])
    qmax=int(np.max(abs(q)));lmax=int(np.max(abs(lam)))
    rowsum=max(sum(abs(int(v)) for v in row) for row in a_integer)
    limit=np.iinfo(np.int64).max
    # These exact Python integer bounds cover all partial dot sums and both
    # summands in each subsequent arithmetic expression before subtraction.
    assert n*qmax*qmax+scale*scale<limit
    assert rowsum*qmax<limit
    assert scale*rowsum*qmax+denominator*qmax*lmax<limit
    gram=q.T@q-scale*scale*np.eye(n,dtype=np.int64)
    residual=scale*(a_integer@q)-denominator*(q*lam[None,:])
    gram_max=int(np.max(abs(gram)));residual_max=int(np.max(abs(residual)))
    orth=Fraction(n*gram_max,scale*scale)
    res=Fraction(n*residual_max,denominator*scale*scale)
    assert 0<=orth<Fraction(1,2)
    # For Q=US (polar decomposition), ||S-I||<=orth and sigma_min(S)>=1-orth.
    # Thus ||A-U diag(lam/scale) U*|| <= (res+2 Lambda_max orth)/(1-orth).
    eta=(res+2*Fraction(lmax,scale)*orth)/(1-orth)
    gap=Fraction(int(lam[1]-lam[0]),scale)-2*eta
    assert gap>0
    return {'dimension':n,'fixed_point_bits':bits,'matrix_denominator':denominator,
            'integer_Gram_max':gram_max,'integer_residual_max':residual_max,
            'Gram_operator_bound_exact':str(orth),'eigenvalue_error_bound_exact':str(eta),
            'eigenvalue_error_bound':float(eta),'ground_gap_lower_exact':str(gap),
            'ground_gap_lower':float(gap),'integer_overflow_excluded':True,
            'integer_basis_sha256':hashlib.sha256(q.astype('<i8').tobytes()).hexdigest(),
            'quantized_eigenvalues_sha256':hashlib.sha256(lam.astype('<i8').tobytes()).hexdigest()},gap


def make_component():
    vertices,edges,faces=base.geometry((2,2,2),True)
    seed=sum(1<<j for j,(v,a,w) in enumerate(edges) if sum(v[b] for b in range(3) if b!=a)%2==0)
    states,tree=base.component(seed,faces);pairs=base.pairs_from_component(states,faces)
    n=len(states);rows=[];cols=[];degree=np.zeros(n,dtype=np.int64)
    for ps in pairs:
        for a,b in ps:rows.extend([a,b]);cols.extend([b,a]);degree[a]+=1;degree[b]+=1
    adj=ss.csr_matrix((np.ones(len(rows),dtype=np.int64),(rows,cols)),shape=(n,n))
    assert (adj-adj.T).nnz==0 and np.array_equal(adj@np.ones(n,dtype=np.int64),degree)
    assert n==864
    return adj,degree,{'vertices':len(vertices),'links':len(edges),'plaquettes':len(faces),
                       'component_dimension':n,'degree_min':int(degree.min()),'degree_max':int(degree.max()),
                       'states_sha256':hashlib.sha256(json.dumps(states).encode()).hexdigest()}


def ramp(adj,degree,target,ground_energy,tau,profile,tolerance):
    n=len(degree);psi0=np.ones(n,dtype=complex)/np.sqrt(n)
    def rhs(s,psi):
        f=s if profile=='linear' else 3*s*s-2*s*s*s
        return -1j*tau*((1-f)*degree*psi-adj@psi)
    sol=solve_ivp(rhs,(0.,1.),psi0,method='DOP853',rtol=tolerance,atol=tolerance/30)
    assert sol.success
    psi=sol.y[:,-1];norm=float(np.vdot(psi,psi).real)
    fidelity=float(abs(np.vdot(target,psi))**2)
    energy=float(np.vdot(psi,-adj@psi).real)/norm
    return {'duration':tau,'profile':profile,'rtol':tolerance,'rhs_evaluations':sol.nfev,
            'norm_error':abs(norm-1),'ground_infidelity':max(0.,1-fidelity/norm),
            'energy_excess':energy-ground_energy},psi


def main():
    start=time.monotonic();adj,degree,info=make_component();n=len(degree)
    dep=hashlib.sha256((OUT/'local_gauge_record_cooling_check.py').read_bytes()).hexdigest()
    assert dep=='9faf0f87d0574368feb0f656308308c269d3df922bfff7576a8d6d10182b5552'
    certificates=[];gaps=[];target=None;target_energy=None;grid_den=16
    aa=adj.toarray()
    for j in range(grid_den+1):
        integer=(grid_den-j)*np.diag(degree)-grid_den*aa
        ham=integer.astype(float)/grid_den
        values,vectors=la.eigh(ham)
        cert,gap=exact_integer_eigen_certificate(integer,grid_den,values,vectors)
        cert.update({'delta':j/grid_den,'floating_ground_energy':float(values[0]),
                     'floating_ground_gap':float(values[1]-values[0])})
        certificates.append(cert);gaps.append(gap)
        if j==grid_den:target=vectors[:,0];target_energy=float(values[0])
        print(json.dumps({'gap_grid_index':j,'gap_lower':float(gap),'eta':cert['eigenvalue_error_bound'],
                          'elapsed_seconds':time.monotonic()-start}),flush=True)
    # Subtracting the delta-dependent scalar at the degree midpoint leaves
    # derivative norm (degree_max-degree_min)/2. Each point is at most half
    # a grid spacing away, and an eigenvalue gap is twice as Lipschitz.
    derivative_norm=Fraction(int(degree.max()-degree.min()),2)
    global_gap=min(gaps)-derivative_norm/grid_den
    assert global_gap>0
    bound_linear=2*derivative_norm/global_gap**2+7*derivative_norm**2/global_gap**3
    bound_smooth=3*derivative_norm/global_gap**2+Fraction(42,5)*derivative_norm**2/global_gap**3
    print(json.dumps({'whole_interval_gap_lower':float(global_gap),'linear_adiabatic_amplitude_coefficient':float(bound_linear),
                      'smooth_adiabatic_amplitude_coefficient':float(bound_smooth)}),flush=True)
    rows=[]
    for profile in ('linear','smoothstep'):
        for tau in (.25,.5,1.,2.,4.,8.,16.):
            row,psi=ramp(adj,degree,target,target_energy,tau,profile,2e-10)
            tight,psit=ramp(adj,degree,target,target_energy,tau,profile,2e-12)
            overlap=np.vdot(psi,psit);phase=overlap/abs(overlap)
            distance=float(la.norm(psi*phase-psit))
            assert distance<2e-7 and tight['norm_error']<1e-8
            assert abs(row['ground_infidelity']-tight['ground_infidelity'])<1e-7
            tight['looser_rtol_state_distance_after_phase']=distance
            coeff=float(bound_linear if profile=='linear' else bound_smooth)
            tight['rigorous_adiabatic_infidelity_upper']=min(1.,(coeff/tau)**2)
            rows.append(tight);print(json.dumps(tight),flush=True)
    info.update({'J':1.,'delta_start':0.,'delta_end':1.,'cooling_during_ramp':False})
    result={'status':'PASS','geometry_dependency_sha256':dep,'geometry':info,
            'gap_grid_certificates':certificates,'whole_interval_gap_lower_exact':str(global_gap),
            'whole_interval_gap_lower':float(global_gap),
            'linear_adiabatic_amplitude_coefficient_exact':str(bound_linear),
            'smoothstep_adiabatic_amplitude_coefficient_exact':str(bound_smooth),
            'numerical_ramps':rows,'runtime_seconds':time.monotonic()-start,
            'scope':'Ground state within one complete finite cubic ice component. Exact-integer gap certificate and stated adiabatic theorem give finite-time preparation; no system-size-uniform gap or photon phase is inferred.'}
    (OUT/'COHERENT_CUBIC_GROUND_RAMP_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'finished':True,'runtime_seconds':result['runtime_seconds']}),flush=True)


if __name__=='__main__':main()
