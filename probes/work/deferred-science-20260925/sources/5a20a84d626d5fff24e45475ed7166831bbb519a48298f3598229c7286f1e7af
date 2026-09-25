#!/usr/bin/env python3
"""Finite author controls; written proofs supply all uniform quantifiers.

Complete S=1 physical matrix definitions are included from a pinned earlier
author runner. That code reuse is explicit and is not independent evidence.
No execution-time scientific source input is imported.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/ACTUAL_CUBE_BIRTH_APPARATUS_COHERENCE_AND_ENERGY_RANGE_BOUNDED_THEOREM_NOTE_2026-09-24.md', '.claude/science/physics-loops/actual-birth-coherence-20260924/NO_GO_DISCIPLINE_CHECKLIST.md', 'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md')
from pathlib import Path
import hashlib,json,math,time
import numpy as np
from scipy.sparse import diags,csr_matrix
from scipy.sparse.linalg import eigsh
HERE=Path(__file__).resolve().parents[1]/'outputs/actual_birth_coherence_20260924'
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


def canonical_preparation(m4,epsilon):
    h=diags(m4['W'],dtype=float)-epsilon*(m4['F']+m4['F'].T)+epsilon**2*m4['C']
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


def fisher(rho,H):
    w,v=np.linalg.eigh((rho+rho.conj().T)/2);assert w.min()>-2e-12
    w=np.maximum(w,0);HH=v.conj().T@H@v;answer=0.
    for a in range(len(w)):
        for b in range(len(w)):
            if w[a]+w[b]>1e-15:
                answer+=2*(w[a]-w[b])**2/(w[a]+w[b])*abs(HH[a,b])**2
    return float(answer)


def trace_norm(a):return float(np.linalg.svd(a,compute_uv=False).sum())


def witness_controls():
    rows=[];alpha=.1;b=2;r=4
    for epsilon in (.12,.08,.05,.03):
        p=alpha**2*b*epsilon**2;q=r/b*epsilon**2;gap=epsilon**-4
        phi=np.array([math.sqrt(1-q),math.sqrt(q)]);omega=p*np.outer(phi,phi)
        H=np.diag([0.,gap]);A=np.array([[0,-1j],[1j,0]])
        derivative=abs(np.trace(omega@(1j*(H@A-A@H))))
        variance=float(np.trace(omega@(A@A)).real)
        exact=4*p*q*(1-q)*gap*gap
        assert abs(fisher(omega,H)-exact)<1e-10*max(1,exact)
        assert abs(derivative**2/variance-exact)<1e-10*max(1,exact)
        eta=alpha**2*epsilon**4
        coherence_fraction=1-eta/(2*p*math.sqrt(q*(1-q)))
        noisy=omega.copy();noisy[0,1]*=coherence_fraction;noisy[1,0]*=coherence_fraction
        error=trace_norm(noisy-omega);assert abs(error-eta)<1e-15
        lower=max(0.,derivative-2*gap*eta)**2/(variance+eta)
        measured=fisher(noisy,H);assert measured+1e-10>=lower
        pinched=np.diag(np.diag(omega));pinch_error=trace_norm(pinched-omega)
        assert fisher(pinched,H)==0
        stationary=np.eye(2)/2
        assert fisher(stationary,np.diag([0.,epsilon**-2]))==0
        classical_variance=.25*epsilon**-4
        rows.append({'epsilon':epsilon,'success_probability':p,'exact_weighted_fisher':exact,
                     'scaled_coefficient':epsilon**4*exact,'asymptotic_coefficient':4*alpha**2*r,
                     'approximation_error':error,'robust_lower':lower,'realized_noisy_fisher':measured,
                     'pinching_error_over_epsilon_cubed':pinch_error/epsilon**3,
                     'stationary_resource_energy_variance':classical_variance,
                     'stationary_resource_fisher':0.})
    return rows


def conserving_resource_controls():
    # System, resource, zero-energy flag, each two dimensional.
    basis=[(s,r,f) for s in (0,1) for r in (0,1) for f in (0,1)]
    energy=np.array([s+r for s,r,f in basis],float);rng=np.random.default_rng(9241314)
    V=np.zeros((8,8),complex)
    for value in (0,1,2):
        inds=np.flatnonzero(energy==value);z=rng.normal(size=(len(inds),len(inds)))+1j*rng.normal(size=(len(inds),len(inds)))
        q,_=np.linalg.qr(z);V[np.ix_(inds,inds)]=q
    assert np.linalg.norm(V.conj().T@V-np.eye(8))<2e-14
    assert np.linalg.norm((energy[:,None]-energy[None,:])*V)==0
    resource_phi=np.array([math.sqrt(.7),1j*math.sqrt(.3)])
    resources=[np.outer(resource_phi,resource_phi.conj()),np.diag([.7,.3])]
    rows=[];Hout=np.diag([s for s in (0,1) for f in (0,1)]);HR=np.diag([0.,1.])
    for rhoR in resources:
        initial=np.kron(np.kron(np.diag([1.,0.]),rhoR),np.diag([1.,0.]))
        final=V@initial@V.conj().T;out=np.zeros((4,4),complex)
        for i,(s,r,f) in enumerate(basis):
            for j,(ss,rr,ff) in enumerate(basis):
                if r==rr and f==ff:out[2*s+f,2*ss+ff]+=final[i,j]
        supplied=fisher(rhoR,HR);created=fisher(out,Hout)
        assert created<=supplied+2e-12
        if supplied==0:assert created<2e-26
        rows.append({'input_resource_fisher':supplied,'flagged_output_fisher':created,
                     'free_energy_change':float(np.trace(np.diag(energy)@(final-initial)).real),
                     'output_trace':float(np.trace(out).real)})
    return rows


def actual_cube_controls():
    models=complete_spin_one();m4,m6=models[4],models[6]
    marks=[jump_matrix(m4,m6,1),jump_matrix(m4,m6,-1)]
    marks.append(marks[0]+marks[1]);alpha=.1;rows=[]
    for epsilon in (.08,.05,.03):
        start=time.monotonic();psi,prep=canonical_preparation(m4,epsilon)
        H4=epsilon**-4*(diags(m4['W'],dtype=float)-epsilon*(m4['F']+m4['F'].T)+epsilon**2*m4['C'])
        H6=epsilon**-4*(diags(m6['W'],dtype=float)-epsilon*(m6['F']+m6['F'].T)+epsilon**2*m6['C'])
        hp=H4@psi;initial_mean=float(np.vdot(psi,hp).real)
        initial_fisher=4*(float(np.vdot(hp,hp).real)-initial_mean**2)
        assert 0<initial_fisher<500
        outputs=[]
        for mark,(b,r) in zip(marks,((2,4),(2,2),(4,6))):
            raw=mark@psi;prob=alpha**2*float(np.vdot(raw,raw).real);phi=raw/np.linalg.norm(raw)
            hphi=H6@phi;mean=float(np.vdot(phi,hphi).real)
            var=float(np.vdot(hphi,hphi).real)-mean*mean
            F=4*prob*var;target=4*alpha**2*r
            ratio=epsilon**4*F/target
            assert .5<ratio<1.5
            assert .7<prob/(alpha**2*b*epsilon**2)<1.3
            outputs.append({'b':b,'r':r,'probability':prob,'conditional_energy_mean':mean,
                            'conditional_energy_variance':var,'weighted_birth_fisher':F,
                            'scaled_coefficient':epsilon**4*F,'target_coefficient':target,
                            'ratio_to_target':ratio,'resource_lower_from_exact_birth':F-initial_fisher})
        row={'epsilon':epsilon,'initial_fisher':initial_fisher,'initial_energy_mean':initial_mean,
             'preparation':prep,'outputs':outputs,'elapsed_seconds':time.monotonic()-start}
        rows.append(row);print(json.dumps(row),flush=True)
    return {'builder_provenance':'Definitions copied into this runner from author source 4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d; no runtime source import','rows':rows,
            'scope':'Author reuse of complete S=1 physical matrices, actual canonical preparation and original marks. Varying epsilon at fixed S is a finite coefficient control, not the joint spin limit.'}


def range_project(v):return np.outer(v,v.conj())


def range_trnorm(a):return float(np.linalg.svd(a,compute_uv=False).sum())


def range_fisher(rho,H):
    w,v=np.linalg.eigh((rho+rho.conj().T)/2)
    assert w.min()>-1e-13
    w=np.maximum(w,0);h=v.conj().T@H@v
    den=w[:,None]+w[None,:];dif=w[:,None]-w[None,:]
    frac=np.divide(dif*dif,den,out=np.zeros_like(den),where=den>1e-16)
    return float(2*np.sum(frac*abs(h)**2))


def coherence_bandwidth(rho,energies):
    inds=np.argwhere(abs(rho)>1e-12)
    return max((abs(energies[i]-energies[j]) for i,j in inds),default=0.)


def exact_block_frequency_control():
    # Large classical energy range, only unit-frequency resource coherence.
    es=np.array([0,1,100]);er=np.array([0,1,99,100,101,199,200])
    basis=[(s,r,f) for s in range(3) for r in range(7) for f in range(2)]
    index={x:i for i,x in enumerate(basis)}
    energy=np.array([es[s]+er[r] for s,r,f in basis])
    rng=np.random.default_rng(9241347);V=np.zeros((42,42),complex)
    for E in np.unique(energy):
        rows=np.flatnonzero(energy==E)
        z=rng.normal(size=(len(rows),len(rows)))+1j*rng.normal(size=(len(rows),len(rows)))
        q,_=np.linalg.qr(z);V[np.ix_(rows,rows)]=q
    assert np.linalg.norm(V.conj().T@V-np.eye(42))<4e-14
    assert np.max(abs((energy[:,None]-energy[None,:])*V))==0
    psi=np.array([1.,1.,0.])/math.sqrt(2)
    rcat=np.zeros(7);rcat[3:5]=1/math.sqrt(2)
    rhoR=.4*range_project(rcat)+.6*np.eye(7)/7
    assert coherence_bandwidth(rhoR,er)==1
    blank=np.diag([1.,0.]);initial=np.kron(np.kron(range_project(psi),rhoR),blank)
    final=V@initial@V.conj().T
    output=np.zeros((6,6),complex)
    for s,r,f in basis:
        for ss,rr,ff in basis:
            if r==rr and f==ff:
                output[2*s+f,2*ss+ff]+=final[index[s,r,f],index[ss,rr,ff]]
    assert abs(np.trace(output)-1)<1e-13
    forbidden=max(abs(output[2*2+f,2*s+f]) for f in range(2) for s in range(2))
    assert forbidden==0
    high_probability=float(sum(output[4+f,4+f].real for f in range(2)))
    assert high_probability>.01
    row={'system_input_bandwidth':1,'apparatus_spectral_diameter':int(er[-1]-er[0]),
         'apparatus_coherence_bandwidth':int(coherence_bandwidth(rhoR,er)),
         'output_high_low_minimum_gap':99,'forbidden_output_coherence_max':float(forbidden),
         'output_high_energy_probability':high_probability,
         'apparatus_fisher':range_fisher(rhoR,np.diag(er)),
         'apparatus_energy_variance':float(np.trace(rhoR@np.diag(er**2)).real-np.trace(rhoR@np.diag(er)).real**2),
         'free_energy_conservation_residual':float(np.max(abs((energy[:,None]-energy[None,:])*V)))}
    # An explicitly nonconserving output rotation adds a missing frequency.
    U=np.eye(3);t=.2;U[0,0]=U[2,2]=math.cos(t);U[0,2]=-math.sin(t);U[2,0]=math.sin(t)
    wrong=U@range_project(psi)@U.T
    assert abs(wrong[2,0])>.01 and np.linalg.norm(np.diag(es)@U-U@np.diag(es))>1
    row['nonconserving_phase_injection_detected']=True
    return row


def prepared_output_swap_controls():
    # Each accessible subsystem is (two-level energy, zero-energy flag).
    swap=np.zeros((16,16))
    for a in range(4):
        for b in range(4):swap[4*b+a,4*a+b]=1.
    rows=[];alpha=.1;b=2;r=4
    for eps in (.12,.08,.05,.03):
        p=alpha*alpha*b*eps*eps;q=r/b*eps*eps;gap=eps**-4
        phi=np.array([math.sqrt(1-q),math.sqrt(q)])
        H=np.diag([0.,gap]);HF=np.kron(H,np.eye(2))
        stationary=np.diag([1.,0.]);flag0=np.diag([1.,0.]);flag1=np.diag([0.,1.])
        rhoR=p*np.kron(range_project(phi),flag1)+(1-p)*np.kron(stationary,flag0)
        initial=np.kron(np.kron(stationary,flag0),rhoR)
        totalH=np.kron(HF,np.eye(4))+np.kron(np.eye(4),HF)
        assert np.linalg.norm(swap@totalH-totalH@swap)==0
        final=swap@initial@swap.T
        out=np.trace(final.reshape(4,4,4,4),axis1=1,axis2=3)
        assert range_trnorm(out-rhoR)<1e-14
        selected=out[np.ix_([1,3],[1,3])]
        assert range_trnorm(selected-p*range_project(phi))<1e-14
        F=range_fisher(rhoR,HF);mean=float(np.trace(rhoR@HF).real)
        assert abs(mean-alpha*alpha*r)<2e-15
        assert abs(eps**4*F-4*alpha*alpha*r*(1-q))<1e-12
        rows.append({'epsilon':eps,'apparatus_mean_above_ground':mean,
                     'apparatus_spectral_diameter':gap,'apparatus_fisher':F,
                     'scaled_fisher':eps**4*F,'limiting_scaled_fisher':4*alpha*alpha*r,
                     'scaled_coherence_bandwidth':eps**4*coherence_bandwidth(rhoR,np.diag(HF)),
                     'selected_output_error':range_trnorm(selected-p*range_project(phi)),
                     'conservation_residual':0.})
    return rows


def main():
    HERE.mkdir(parents=True,exist_ok=True)
    result={'phase_witness':witness_controls(),'conserving_resource':conserving_resource_controls(),
            'actual_cube':actual_cube_controls(),'frequency':exact_block_frequency_control(),
            'prepared_output_swap':prepared_output_swap_controls(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Finite author corroboration; no uniform-limit numerical proof, full marked-map sufficiency or formal negative-packet PASS.'}
    (HERE/'COHERENCE_RANGE_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    print('per_element: Phase matrix elements, success weights, finite conserving identities and premise-changing controls are explicitly exercised.')
    print('per_site: checked and not executed — this runner does not compute a sitewise formation law or a site-resolved apparatus energy supply.')
    print('per_mode: Finite energy-frequency support is checked, including absent output coherences despite nonzero high-energy populations; no all-mode scan.')
    print('per_block: Complete S=1 physical cube inputs and original marks are checked separately from finite resource toys; the joint-spin proof is analytic.')
    print('lattice_wide: checked and not executed — no thermodynamic-limit or continuum-lattice apparatus is constructed or excluded by these controls.')
    print('TOTAL: PASS=5 FAIL=0',flush=True)
if __name__=='__main__':main()
