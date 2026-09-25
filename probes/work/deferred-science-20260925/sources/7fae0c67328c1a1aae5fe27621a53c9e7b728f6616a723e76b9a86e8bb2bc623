#!/usr/bin/env python3
"""Finite author controls; actual cube matrix reuse is explicit, not independent."""
from pathlib import Path
import hashlib,importlib.util,json,math,time,sys
import numpy as np
from scipy.sparse import diags

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent/'ordinary-energy-publication/scripts/ordinary_microscopic_cube_energy_after_birth_layer_2026_09_24.py'
PARENT_SHA='4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d'

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
    assert hashlib.sha256(PARENT.read_bytes()).hexdigest()==PARENT_SHA
    spec=importlib.util.spec_from_file_location('frozen_cube_author_builder',PARENT)
    builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
    models=builder.complete_spin_one();m4,m6=models[4],models[6]
    marks=[builder.jump_matrix(m4,m6,1),builder.jump_matrix(m4,m6,-1)]
    marks.append(marks[0]+marks[1]);alpha=.1;rows=[]
    for epsilon in (.08,.05,.03):
        start=time.monotonic();psi,prep=builder.canonical_preparation(m4,epsilon)
        H4=epsilon**-4*(diags(m4['W'])-epsilon*(m4['F']+m4['F'].T)+epsilon**2*m4['C'])
        H6=epsilon**-4*(diags(m6['W'])-epsilon*(m6['F']+m6['F'].T)+epsilon**2*m6['C'])
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
    return {'parent_path':str(PARENT),'parent_sha256':PARENT_SHA,'rows':rows,
            'scope':'Author reuse of complete S=1 physical matrices, actual canonical preparation and original marks. Varying epsilon at fixed S is a finite coefficient control, not the joint spin limit.'}

def main():
    result={'phase_witness':witness_controls(),'conserving_resource':conserving_resource_controls(),
            'actual_cube':actual_cube_controls(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Finite author corroboration; analytic hypotheses, robustness and limiting claims require the written proof and independent check.'}
    (HERE/'COHERENCE_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
