#!/usr/bin/env python3
"""Post-seal comparison; imports only the sealed independent implementation."""
from pathlib import Path
import json,hashlib,math,datetime
from itertools import product
import numpy as np
from scipy.sparse.linalg import expm_multiply
import independent_check as own
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent

def ident(p):
    b=p.read_bytes();return dict(path=str(p.resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def rotate(q,N,t,u,continuum=False):
    v=2*np.pi*np.array(q) if continuum else np.sin(2*np.pi*np.array(q)/N)
    r=np.linalg.norm(v)
    if r==0:return u.copy()
    axis=v/r;angle=t*r
    return math.cos(angle)*u+math.sin(angle)*np.cross(axis,u)+(1-math.cos(angle))*axis*np.dot(axis,u)

def wave(pts,N,q,u):
    return (np.exp(2j*np.pi*np.array(pts)@np.array(q)/N)[:,None]*u[None,:]/math.sqrt(N**3)).ravel()

def main():
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for x in pre['sources']+pre['artifacts']:assert ident(Path(x['path']))==x
    a=json.loads((ROOT/'dimer_local_dilute_curl_checks/RESULTS.json').read_text())
    for x in a['sources']:assert ident(Path(x['path']))==x
    q=(1,0,0);r=(0,1,0);u=np.array([1,1j,0])/math.sqrt(2);v=np.array([0,1,1j])/math.sqrt(2)
    arithmetic=[]
    for row in a['two_particle_dynamics']:
        N=row['N'];tau=row['tau'];t=N*tau;ut=rotate(q,N,t,u);vt=rotate(r,N,t,v)
        collision=(1+abs(np.vdot(ut,vt))**2)/N**3;eps=2/math.sqrt(N**3)
        bound=eps*(1+2*math.sqrt(3)*t)+eps**2;combined=bound+2*tau*(2*np.pi)**3/(6*N*N)
        assert row['physical_two_particle_dimension']==9*math.comb(N**3,2)
        assert abs(row['initial_collision']-1.25/N**3)<1e-15
        assert abs(collision-row['free_collision_at_time'])<3e-15
        assert abs(bound-row['proof_bound'])<3e-14 and abs(combined-row['combined_proof_bound'])<3e-14
        arithmetic.append(dict(N=N,tau=tau,collision_discrepancy=abs(collision-row['free_collision_at_time'])))
    symbols=[]
    for row in a['one_particle_symbols']['rows']:
        N=row['N'];Q=2*np.pi*np.array([1,2,-1]);err=np.linalg.norm(N*np.sin(Q/N)-Q)
        assert abs(err-row['low_mode_symbol_error'])<3e-14
        assert abs(np.linalg.norm(Q)**3/(6*N*N)-row['sine_remainder_bound'])<3e-14
        assert row['sine_zero_momenta']==(1 if N%2 else 8)
        symbols.append(N)
    pts,C=own.curl(3);pb,hc=own.physical_two_particle(C);bb,free=own.free_two_particle(C)
    bi={x:i for i,x in enumerate(bb)};idx=np.array([bi[x] for x in pb]);mask=np.ones(len(bb),bool);mask[idx]=False
    psi=own.pair_vector(bb,wave(pts,3,q,u),wave(pts,3,r,v));phi=psi[idx]/np.linalg.norm(psi[idx]);dynamic=[]
    for row in a['two_particle_dynamics']:
        if row['N']!=3:continue
        tau=row['tau'];t=3*tau;actual=expm_multiply(-1j*t*hc,phi)
        embedded=np.zeros(len(bb),complex);embedded[idx]=actual
        target=own.pair_vector(bb,wave(pts,3,q,rotate(q,3,t,u)),wave(pts,3,r,rotate(r,3,t,v)))
        ct=own.pair_vector(bb,wave(pts,3,q,rotate(q,3,tau,u,True)),wave(pts,3,r,rotate(r,3,tau,v,True)))
        e=float(np.linalg.norm(embedded-target));ec=float(np.linalg.norm(embedded-ct))
        assert abs(e-row['free_comparison_error'])<3e-13 and abs(ec-row['continuum_comparison_error'])<3e-13
        dynamic.append(dict(tau=tau,free_error=e,continuum_error=ec,free_discrepancy=abs(e-row['free_comparison_error']),continuum_discrepancy=abs(ec-row['continuum_comparison_error'])))
    # Selectively reconstruct the failed norm identity, without an N=6 trajectory.
    N=6;pts=list(product(range(N),repeat=3));f=wave(pts,N,q,u);g=wave(pts,N,r,v)
    projected=np.array([f[x]*g[y]+g[x]*f[y] for x in range(3*N**3) for y in range(x+1,3*N**3) if x//3!=y//3])
    norm2=math.fsum(float(x) for x in abs(projected)**2);expected=1-1.25/N**3
    assert abs(norm2-expected)<1e-14
    old=ROOT/'dimer_routed_development/local_dilute_norm_accumulation/dimer_local_dilute_curl_check.py'
    current=(ROOT/'dimer_local_dilute_curl_check.py').read_text();before=old.read_text()
    insertion='\ndef accurate_norm(z):\n # The host BLAS norm lost 2.5e-13 on a 208980-entry almost-flat vector.\n # Compensated scalar accumulation keeps the original assertion tolerances.\n return math.sqrt(math.fsum(float(a) for a in np.abs(z).reshape(-1)**2))\n'
    restored=current.replace(insertion,'')
    for arg in ['initial','projected','actual-projected','actual','actual-pc']:
        restored=restored.replace('accurate_norm('+arg+')','float(np.linalg.norm('+arg+'))')
    assert restored==before
    current_receipt=json.loads((ROOT/'DIMER_LOCAL_DILUTE_CURL_RUN_RECEIPT.json').read_text())
    assert current_receipt['returncode']==0 and current_receipt['script_sha256']==ident(ROOT/'dimer_local_dilute_curl_check.py')['sha256']
    assert (ROOT/'DIMER_LOCAL_DILUTE_CURL_RUN.stderr').read_bytes()==b''
    for name in ['local_dilute_norm_accumulation','local_dilute_runtime_missing_scipy']:
        rr=json.loads((ROOT/'dimer_routed_development'/name/'DIMER_LOCAL_DILUTE_CURL_RUN_RECEIPT.json').read_text())
        assert rr['returncode']==1 and rr['script_sha256']==ident(old)['sha256']
    src=[ROOT/x for x in ['DIMER_LOCAL_DILUTE_QUANTUM_CURL_LIMIT.md','dimer_local_dilute_curl_check.py',
         'dimer_local_dilute_curl_checks/RESULTS.json','DIMER_LOCAL_DILUTE_CURL_RUN.log',
         'DIMER_LOCAL_DILUTE_CURL_RUN.stderr','DIMER_LOCAL_DILUTE_CURL_RUN_RECEIPT.json']]
    for name in ['local_dilute_norm_accumulation','local_dilute_runtime_missing_scipy']:
        src.extend(sorted(f for f in (ROOT/'dimer_routed_development'/name).iterdir() if f.is_file()))
    result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_bindings=[ident(f) for f in src],
                preseal_authenticated=True,all_author_sources_read=True,author_code_executed=False,
                all_nine_dynamic_row_formula_comparisons=arithmetic,all_nine_symbol_rows_checked=symbols,
                independently_recomputed_N3_dynamics=dynamic,
                preserved_failure_reconstruction=dict(N=6,dimension=len(projected),compensated_norm_squared=norm2,
                  analytic_value=expected,difference=norm2-expected,current_numpy_norm_squared=float(np.linalg.norm(projected)**2),
                  source_change_is_only_compensated_norm=True),
                scope='No N=4 or N=6 author trajectory replay. The independent preseal used different states and parameters on actual side-3/4 cubic tori. Raw author failures were authenticated; no tolerance or theorem change found.')
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
