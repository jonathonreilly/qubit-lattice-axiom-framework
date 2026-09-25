#!/usr/bin/env python3
"""Finite consistency checks for the conditional fixed-time microscopic cube theorem.

The analytic note proves the joint limit; these numerical finite-spin controls do not.
Selected prior matrix-builder definitions are included explicitly, without claiming
independent reconstruction. Scientific source reads: none at execution. The cache
binds the declared mathematical source notes separately. Outputs contain own results.
"""
AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FIXED_TIME_MICROSCOPIC_CUBE_BIRTH_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY_BOUNDED_THEOREM_NOTE_2026-09-24.md']
from pathlib import Path
import hashlib,json,time,tempfile
import numpy as np
from scipy.linalg import eig,expm
from scipy.sparse import diags,eye,csr_matrix
from scipy.sparse.linalg import eigsh,expm_multiply,splu

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUTPUT_DIR=ROOT/'outputs/fixed_time_cube_birth_energy_20260924'
A=(0,3,5,6);B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))

def complete_spin_one():
    inc=np.zeros((12,8),np.int8)
    for i,(a,b) in enumerate(EDGES):inc[i,a]=1;inc[i,b]=-1
    allE=np.indices((3,)*12,dtype=np.int8).reshape(12,-1).T-1
    allq=allE@inc+np.array([int(i in A) for i in range(8)],np.int8)
    valid=(np.abs(allq)<=1).all(axis=1);number=(allq*allq).sum(axis=1)
    models={}
    for N in (4,6,8):
        select=valid&(number==N);fields=allE[select].copy();charges=allq[select].copy()
        index={tuple(int(x) for x in E):i for i,E in enumerate(fields)};n=len(fields)
        W=(charges[:,A]==0).sum(axis=1)
        rows=[];cols=[];delta=np.zeros(n);loss=np.zeros(n)
        for i,(q,E) in enumerate(zip(charges,fields)):
            for e,(a,b) in enumerate(EDGES):
                if q[a]!=0 and q[b]==0:
                    weight=1-int(E[e])*(int(E[e])-int(q[a]))/2
                    assert weight in (0,1)
                    if weight:
                        ee=E.copy();ee[e]-=q[a];dest=index[tuple(int(x) for x in ee)]
                        rows.append(dest);cols.append(i)
                    if W[i]==0:delta[i]+=1-weight
                if q[a]==q[b]==0:loss[i]+=2-int(E[e])**2
        F=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(n,n))
        P=diags((W==0).astype(float));C=P@(F.T@F)@P+diags(delta)
        if N==8:assert F.nnz==C.nnz==0 and np.max(W)==0 and np.max(loss)==0
        if N==6:assert np.all(loss[W!=1]==0)
        models[N]={'E':fields,'q':charges,'index':index,'W':W,'F':F,'C':C,'loss':loss}
    return models

def jump_matrix(m4,m6,sigma):
    rows=[];cols=[]
    for i,(q,E) in enumerate(zip(m4['q'],m4['E'])):
        if q[0] or q[1]:continue
        weight=1-int(E[0])*(int(E[0])+sigma)/2
        assert weight in (0,1)
        if not weight:continue
        ee=E.copy();ee[0]+=sigma;rows.append(m6['index'][tuple(int(x) for x in ee)]);cols.append(i)
    return csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(m6['E']),len(m4['E'])))

def normcols(x):
    return np.sum(abs(x)**2,axis=0)

def riesz_action(h,x,grade,n):
    """Trapezoidal contour integral; an approximate projector, never exact evidence."""
    result=np.zeros_like(x,dtype=complex)
    ident=eye(h.shape[0],format='csc',dtype=complex)
    for k in range(n):
        dz=.35*np.exp(2j*np.pi*(k+.5)/n)
        result+=dz*splu((grade+dz)*ident-h).solve(np.asarray(x,dtype=complex))/n
    return result

def small_controls():
    eps=.12;kappa=.7
    W=np.diag([0.,1.,2.]);T=np.array([[0.,-1.,0.],[-1.,0.,-.8],[0.,-.8,0.]])
    C=np.diag([1.4,0.,0.]);Gamma=np.diag([0.,2.,0.])
    h=W+eps*T+eps**2*C;heff=h-.5j*kappa*eps**2*Gamma
    values,U=np.linalg.eigh(h);P=np.outer(U[:,1],U[:,1]);initial=U[:,0].astype(complex)
    lam,V=eig(heff);index=int(np.argmin(abs(lam-1)));E=V[:,[index]]@np.linalg.inv(V)[[index],:]
    G=-1j*heff/eps**4
    times=np.linspace(0,.03,61);states=np.stack([expm(t*G)@initial for t in times])
    orth=np.array([np.linalg.norm(P@v)**2 for v in states])
    oblique=np.array([np.linalg.norm(E@v)**2 for v in states])
    assert np.linalg.norm(E@E-E)<1e-12
    assert np.linalg.norm(E-E.conj().T)>1e-5
    assert orth[0]<1e-25 and orth.max()>1e-9
    assert np.max(np.diff(oblique))<2e-13
    assert np.linalg.norm(E@expm(.01*G)-expm(.01*G)@E)<2e-12
    density_rows=[]
    for n in (10,100,1000):
        # rho_n -> |0><0| in trace norm while Tr(diag(0,n^2)rho_n)=n.
        rho=np.diag([1-1/n,1/n]);energy=np.diag([0.,float(n*n)])
        distance=float(np.linalg.norm(rho-np.diag([1.,0.]),ord='nuc'))
        mean=float(np.trace(energy@rho));assert abs(distance-2/n)<1e-12 and abs(mean-n)<1e-10
        density_rows.append({'n':n,'trace_norm_distance':distance,'energy':mean})
    return {'orthogonal_high_weight_starts_at':float(orth[0]),'orthogonal_high_weight_maximum':float(orth.max()),'oblique_max_increment':float(np.max(np.diff(oblique))),'oblique_projector_nonselfadjoint_norm':float(np.linalg.norm(E-E.conj().T)),'density_counterexample':density_rows}

def canonical_preparation(m4,epsilon):
    h=diags(m4['W'])-epsilon*(m4['F']+m4['F'].T)+epsilon**2*m4['C']
    p=np.flatnonzero(m4['W']==0)
    seed=np.random.default_rng(92405).normal(size=h.shape[0])
    values,V=eigsh(h,k=len(p),sigma=-.01,which='LM',tol=2e-12,v0=seed)
    residual=float(np.linalg.norm(h@V-V*values));orth=float(np.linalg.norm(V.T@V-np.eye(len(p))))
    assert max(abs(values))<.2 and residual<2e-10 and orth<2e-10
    VP=V[p,:];gram=VP@VP.T;w,q=np.linalg.eigh(gram);assert w.min()>.6
    j=int(np.flatnonzero(p==m4['index'][(0,)*12])[0]);unit=np.eye(len(p))[:,j]
    v=V@(VP.T@((q/np.sqrt(w))@q.T@unit))
    assert abs(np.vdot(v,v).real-1)<2e-10
    return v,{'eigen_residual':residual,'orthogonality_error':orth,'minimum_overlap_eigenvalue':float(w.min())}

def complete_cube_controls():
    models=complete_spin_one();m4,m6=models[4],models[6]
    print('Complete spin-one spaces built: '+str({n:len(m['E']) for n,m in models.items()}),flush=True)
    F=m6['F'];Gamma=diags(m6['loss']);kappa=.7
    jp=jump_matrix(m4,m6,1);jm=jump_matrix(m4,m6,-1)
    rows=[]
    for epsilon in (.1,.075,.05):
        start=time.monotonic();dressed,prep=canonical_preparation(m4,epsilon)
        raw=np.stack([j@dressed for j in (jp,jm,jp+jm)],axis=1)
        X=raw/np.sqrt(normcols(raw))[None,:]
        h=(diags(m6['W'])-epsilon*(F+F.T)+epsilon**2*m6['C']).tocsc()
        heff=h-.5j*kappa*epsilon**2*Gamma
        e16=riesz_action(heff,X,1,16);e32=riesz_action(heff,X,1,32)
        quad=float(np.linalg.norm(e32-e16));assert quad<2e-5
        # Identify the selected band on these actual outputs; commutation alone is insufficient.
        ell=np.array([2.,1.,1.5])
        assert np.max(abs(normcols(e32)/epsilon**2-ell))<40*epsilon**2
        p32=riesz_action(h,X,1,32)
        difference=float(np.linalg.norm(e32-p32));assert difference<50*epsilon**3
        # Propagate the exact full generator and the numerically projected component.
        gen=-1j*heff/epsilon**4;times=np.linspace(0,.02,5)
        paths=expm_multiply(gen,np.column_stack([X,e32]),start=0,stop=times[-1],num=len(times),traceA=gen.diagonal().sum())
        ordinary=paths[:,:,:3];component=paths[:,:,3:]
        weights=np.array([normcols(x) for x in component]);assert np.max(np.diff(weights,axis=0))<2e-9
        commutation=np.linalg.norm(riesz_action(heff,ordinary[-1],1,32)-component[-1])
        assert commutation<2e-8
        survival=np.array([normcols(x) for x in ordinary]);assert np.max(survival)<=1+2e-9
        assert np.max(np.diff(survival,axis=0))<2e-9
        scaled_mean=np.array([np.sum(x.conj()*(h@x),axis=0).real/epsilon**2 for x in ordinary])
        scaled_second=np.array([normcols(h@x)/epsilon**2 for x in ordinary])
        scaled_variance=scaled_second-epsilon**2*scaled_mean**2
        assert scaled_second.min()>=0 and scaled_variance.min()>-2e-9
        # Finite regression controls against independently derived leading coefficients.
        # These tolerances are not analytic uniform remainder certificates.
        ell=np.array([2.,1.,1.5])
        assert np.max(abs(scaled_mean[0]-ell))<30*epsilon**2
        assert np.max(abs(scaled_second[0]-ell))<5*epsilon**2
        row={'epsilon':epsilon,'spin':1,'not_a_joint_scaling_sequence':True,'preparation':prep,'contour_16_to_32_difference':quad,'projector_difference_on_actual_outputs':difference,'projector_difference_divided_by_epsilon_cubed':difference/epsilon**3,'commutation_action_residual':float(commutation),'physical_times':times.tolist(),'mark_order':['resolved_plus','resolved_minus','coherent'],'oblique_component_squared_norm':weights.tolist(),'survival':survival.tolist(),'epsilon_squared_mean_over_delta':scaled_mean.tolist(),'epsilon_sixth_second_moment_over_delta_squared':scaled_second.tolist(),'epsilon_sixth_variance_over_delta_squared':scaled_variance.tolist(),'elapsed_seconds':time.monotonic()-start}
        rows.append(row)
        (OUTPUT_DIR/f'CUBE_CONTROL_epsilon_{epsilon}.json').write_text(json.dumps(row,indent=2)+'\n')
        print(json.dumps({k:row[k] for k in ('epsilon','contour_16_to_32_difference','projector_difference_divided_by_epsilon_cubed','commutation_action_residual','elapsed_seconds')}),flush=True)
    return {'complete_dimensions':{str(n):len(m['E']) for n,m in models.items()},'rows':rows}

def main():
    OUTPUT_DIR.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();result={'small_controls':small_controls(),'complete_cube':complete_cube_controls(),'builder_provenance':'Selected complete_spin_one and jump_matrix definitions from the prior guarded control cf51bc234d72cb26667b740dddf9f29b27b3c43826dac74df941401a113df125, included here without algorithm changes.','builder_reuse':'Previous checker builder, personally reused here; these new controls are not independent reconstruction.','scope':'Numerical finite spin-one checks only; no interval certification, no joint-limit fit. The analytic proof supplies the asymptotic claim.','all_assertions_passed':True,'elapsed_seconds':time.monotonic()-start}
    (OUTPUT_DIR/'FIXED_TIME_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    print('TOTAL: PASS=2 FAIL=0',flush=True)

if __name__=='__main__':
    with tempfile.TemporaryDirectory(prefix='fixed-time-cube-') as td:
        OUTPUT_DIR=Path(td)
        main()
