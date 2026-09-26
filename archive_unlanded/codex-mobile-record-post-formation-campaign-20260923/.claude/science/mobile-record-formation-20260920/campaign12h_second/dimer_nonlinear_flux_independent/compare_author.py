#!/usr/bin/env python3
"""Post-seal authentication and selective comparison; no author-code execution."""
from pathlib import Path
import hashlib,json,difflib,datetime
import numpy as np
import sympy as s
import independent_check as own

HERE=Path(__file__).resolve().parent
RAW=HERE.parent
def identity(p):
    data=p.read_bytes()
    return {'path':str(p.resolve()),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def main():
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['sources']+pre['artifacts']:
        assert identity(Path(row['path']))==row,row['path']
    expected={'dimer_nonlinear_flux_check.py':'45f732b01260e3bd9e8651aefe42acb346a7a2f8bd30190f9f1b33313de57cc4',
              'dimer_nonlinear_flux_checks/RESULTS.json':'756b19b0ebcdacdda23510173e63f2b16627d6ba6cc1d6a2998d0a145fe6f138'}
    for name,sha in expected.items(): assert identity(RAW/name)['sha256']==sha
    author=json.loads((RAW/'dimer_nonlinear_flux_checks/RESULTS.json').read_text())
    for row in author['sources']: assert identity(Path(row['path']))==row
    failure=RAW/'dimer_routed_development/nonlinear_initial_drift_threshold'
    old=(failure/'dimer_nonlinear_flux_check.py').read_text()
    new=(RAW/'dimer_nonlinear_flux_check.py').read_text()
    diag=json.loads((failure/'DIAGNOSIS.json').read_text())
    assert hashlib.sha256(old.encode()).hexdigest()==diag['original_checker_sha256']
    delta=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='preserved_old',tofile='reviewed_final'))
    (HERE/'AUTHOR_THRESHOLD_SOURCE_DELTA.txt').write_text(delta)
    removed=[line[1:] for line in delta.splitlines() if line.startswith('-') and not line.startswith('---')]
    added=[line[1:] for line in delta.splitlines() if line.startswith('+') and not line.startswith('+++')]
    assert len(removed)==len(added)==2
    assert removed[0].startswith('T=') and added[0]=='T=s.Matrix.vstack(s.eye(13),-s.ones(1,13))'
    assert removed[1]==' for N in [8,16,32,64,128,256,512,1024]:'
    assert added[1]==' for N in [8,16,32,64,128,256,512,1024,2048,4096,8192]:'
    assert diag['rows']==author['actual_initial_drift']['rows'][:8]
    assert '.003' in new and 'AssertionError' in (failure/'DIMER_NONLINEAR_FLUX_RUN.stderr').read_text()
    assert (RAW/'DIMER_NONLINEAR_FLUX_RUN.stderr').read_bytes()==b''
    receipt=json.loads((RAW/'DIMER_NONLINEAR_FLUX_RUN_RECEIPT.json').read_text())
    assert receipt['script_sha256']==expected['dimer_nonlinear_flux_check.py'] and receipt['returncode']==0
    assert (RAW/'DIMER_NONLINEAR_FLUX_RUN.log').read_text().splitlines()==[
        'moment_fluxes complete','entropy_symmetrizer complete','optical_diagnostic complete',
        'actual_initial_drift complete','all_four_control_groups_complete']

    # Independent differentiated species formula, rather than the author's Jacobian implementation.
    ee=np.asarray(own.e,float); bb=np.asarray(own.b,float)
    dirs=[np.asarray(v,float).ravel() for i in range(3) for v in (own.axes[i],-own.axes[i]) if v!=own.axes[0]]
    kernels=[sum(delta[i]*np.asarray(own.kernel(own.axes[i]),float) for i in range(3))/2 for delta in dirs]
    p0=np.ones(14)/14
    perturb=np.zeros(14)
    perturb[:6]=ee[:6]@np.array([0.,.08,.04])/2
    perturb[6:]=bb[6:]@np.array([0.,-.08,.16])/8
    checks=[]
    for N in (8,128,1024,8192):
        x=np.arange(N)/N
        p=p0+np.cos(2*np.pi*x)[:,None]*perturb
        dp=-2*np.pi*np.sin(2*np.pi*x)[:,None]*perturb
        X,Y,dX,dY=p@ee,p@bb,dp@ee,dp@bb
        factor=np.cross(ee[None,:,:],Y[:,None,:])+np.cross(X[:,None,:],bb[None,:,:])-2*np.cross(X,Y)[:,None,:]
        dfactor=np.cross(ee[None,:,:],dY[:,None,:])+np.cross(dX[:,None,:],bb[None,:,:])-2*(np.cross(dX,Y)+np.cross(X,dY))[:,None,:]
        target=-(dp[:,:,None]*factor+p[:,:,None]*dfactor)[:,:,0]
        def outgoing(row,step,S):
            pl=p[(row-step)%N];pu=p[row];pw=p[(row+step)%N];pr=p[(row+2*step)%N]
            sv=(pl+pr)@S
            return 1.1*(pu-pw)/2+((pu+pw)*sv-pu*np.sum(pw*sv,axis=1)[:,None]-pw*np.sum(pu*sv,axis=1)[:,None])/4
        indices=np.arange(N); drift=np.zeros_like(p)
        for delta,S in zip(dirs,kernels):
            step=int(delta[0]-1)
            drift+=N*(outgoing((indices-step)%N,step,S)-outgoing(indices,step,S))
        error=float(np.max(np.abs(drift-target)))
        saved=next(row for row in author['actual_initial_drift']['rows'] if row['N']==N)
        assert abs(error-saved['max_color_initial_Euler_drift_error'])<1e-11
        checks.append({'N':N,'independent_error':error,'stored_error':saved['max_color_initial_Euler_drift_error'],
                       'absolute_difference':abs(error-saved['max_color_initial_Euler_drift_error'])})
    for row in author['actual_initial_drift']['rows']:
        assert row['N']*row['max_color_initial_Euler_drift_error']==row['N_times_error']
    phase=s.symbols('x',real=True); amp=s.Rational(2,25)
    X=s.Matrix([0,amp*s.cos(phase),amp*s.cos(phase)/2]);Y=s.Matrix([0,-amp*s.cos(phase),2*amp*s.cos(phase)])
    rho_flux=X.cross(Y)[0]/7
    z_flux=X.cross(Y[2]*own.axes[1]+Y[1]*own.axes[2])[0]
    locals={'x':phase}
    assert s.simplify(rho_flux-s.sympify(author['actual_initial_drift']['finite_amplitude_rhoA_flux'],locals=locals))==0
    assert s.simplify(z_flux-s.sympify(author['actual_initial_drift']['finite_amplitude_Z23_flux'],locals=locals))==0
    # Recheck all nine saved exact optical speed pairs against the independently assembled full moment matrix.
    for row in author['optical_diagnostic']:
        p=own.rest([s.Rational(1,7)]*3,[0,0,s.Rational(1,14)] if row['profile']=='Z23' else [0,0,0],
                   s.Rational(1,14) if row['profile']=='hidden_w' else 0)
        A=own.moment_jac(p,own.axes[row['axis']],1)
        ev=(A[3:9,3:9]**2).eigenvals()
        values=sorted([v for v,multiplicity in ev.items() if v!=0 for _ in range(multiplicity//2)])
        assert values==[s.Rational(z) for z in row['exact_squared_speeds']]
        assert A.rank()==row['full_color_rank']==4
    src=list(pre['sources'])
    files=[RAW/'dimer_nonlinear_flux_check.py',RAW/'dimer_nonlinear_flux_checks/RESULTS.json',
           RAW/'DIMER_NONLINEAR_FLUX_RUN.log',RAW/'DIMER_NONLINEAR_FLUX_RUN.stderr',RAW/'DIMER_NONLINEAR_FLUX_RUN_RECEIPT.json']
    files+=sorted(q for q in failure.iterdir() if q.is_file())
    src += [identity(q) for q in files]
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'no actionable discrepancy',
            'pre_seal_verified':{'sources':len(pre['sources']),'artifacts':len(pre['artifacts'])},
            'author_sources':src,'author_code_executed':False,
            'coverage':'Complete final checker/result and preserved source delta read. All four result source bindings authenticated. Four initial profiles independently recomputed; all eleven N-times-error arithmetic rows, nine exact optical pairs and two symbolic harmonic fluxes checked. Author moment/entropy checks are authenticated support; general identities are supported by the sealed independent derivation.',
            'selected_initial_drift_rows':checks,'source_delta_only':'dead false conditional in tangent basis plus three larger grids',
            'preserved_failure':'Original threshold failure retained; all eight original row values exactly retained, profile and .003 threshold unchanged.'}
    with (HERE/'AUTHOR_COMPARISON.json').open('x') as f: json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'source_count':len(src),'selected_initial_drift_rows':checks}))

if __name__=='__main__':main()
