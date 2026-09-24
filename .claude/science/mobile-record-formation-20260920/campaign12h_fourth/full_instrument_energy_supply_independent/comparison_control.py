#!/usr/bin/env python3
"""POST comparison using only the frozen independent PRE model builder.

New exact test: stationary-input joint energy/flag probabilities through two
marked gates on the same finite reservoir. Independent finite-star matrices
also reproduce the released collision rows, including lambda=1/coherent.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,importlib.util,itertools,json,math,sys
sys.dont_write_bytecode=True
import numpy as np
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent
PRE=HERE/'control.py'
assert hashlib.sha256(PRE.read_bytes()).hexdigest()=='04701d445390b031c8c4399e27d2cba118b41caafc48a12efa1c67f7ec330bbd'
spec=importlib.util.spec_from_file_location('own_frozen_pre',PRE)
own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)


def identity(n):return {(i,i):Q(1) for i in range(n)}


def rotation(n,i,j,c=Q(3,5),s=Q(4,5)):
    U=identity(n);U[i,i]=U[j,j]=c;U[i,j]=-s;U[j,i]=s
    return U


def matvec(A,x):
    out={}
    for (i,j),v in A.items():
        if j in x:out[i]=out.get(i,Q(0))+v*x[j]
    return {i:v for i,v in out.items() if v}


def embed_flag(U,which):
    # System dimension 4, two two-dimensional flags, index 4*s+2*f1+f2.
    out={}
    for col in range(16):
        s,f1,f2=col//4,(col//2)%2,col%2
        fs=[f1,f2];localcol=2*s+fs[which]
        for (localrow,j),v in U.items():
            if j!=localcol:continue
            ss,ff=localrow//2,localrow%2;new=fs.copy();new[which]=ff
            out[4*ss+2*new[0]+new[1],col]=v
    return out


def probs(x,nr,syslabels):
    result={}
    for joint,amp in x.items():
        a=joint//nr;s=a//4;flags=a%4
        key=(syslabels[s],flags)
        result[key]=result.get(key,Q(0))+amp*amp
    return result


def rational_stationary_history():
    # A degenerate ground eigenspace and irrational positive levels 1,sqrt(2).
    syslabels=[0,0,1,2]
    vectors=[(0,0),(0,0),(1,0),(0,1)]
    labels=[vectors[s] for s in range(4) for f in range(4)]
    Ulocal1=own.rational_mul(rotation(8,0,5),rotation(8,2,7,Q(5,13),Q(12,13)),8)
    Ulocal1=own.rational_mul(Ulocal1,rotation(8,0,2),8)
    Ulocal2=own.rational_mul(rotation(8,0,6,Q(5,13),Q(12,13)),rotation(8,1,4),8)
    U1=embed_flag(Ulocal1,0);U2=embed_flag(Ulocal2,1)
    U=own.rational_mul(U2,U1,16)
    V1,charges,dim=own.rational_lift(U1,labels,2,True)
    V2,_,_=own.rational_lift(U2,labels,2,True)
    V,_,_=own.rational_lift(U,labels,2,True)
    assert own.rational_mul(V2,V1,dim)==V
    assert all(charges[i]==charges[j] for (i,j),v in V.items() if v)
    nr=16;coords=list(itertools.product(range(4),repeat=2));loc={n:i for i,n in enumerate(coords)}
    b={1:Q(3,5),2:Q(4,5)}
    eta={loc[n]:b[n[0]]*b[n[1]] for n in itertools.product((1,2),repeat=2)}
    assert sum(a*a for a in eta.values())==1
    inputs=[{0:Q(3,5),4:Q(4,5)},{8:Q(1)},{12:Q(1)}]
    weights=[Q(1,2),Q(1,3),Q(1,6)]
    rows=[];mixed_actual={};mixed_target={};cross_defects=[]
    for index,x in enumerate(inputs):
        joint={a*nr+n:amp*ba for a,amp in x.items() for n,ba in eta.items()}
        actual=matvec(V2,matvec(V1,joint));target=matvec(U,x)
        actual_probs=probs(actual,nr,syslabels)
        target_probs=probs(target,1,syslabels)
        assert actual_probs==target_probs
        # Trace out the physical reservoir; cross-energy coherences may differ.
        for a in range(16):
            for z in range(16):
                if syslabels[a//4]==syslabels[z//4]:continue
                reduced=sum(actual.get(a*nr+n,Q(0))*actual.get(z*nr+n,Q(0)) for n in range(nr))
                ideal=target.get(a,Q(0))*target.get(z,Q(0))
                if reduced!=ideal:cross_defects.append(abs(reduced-ideal))
        for k in set(actual_probs)|set(target_probs):
            mixed_actual[k]=mixed_actual.get(k,Q(0))+weights[index]*actual_probs.get(k,Q(0))
            mixed_target[k]=mixed_target.get(k,Q(0))+weights[index]*target_probs.get(k,Q(0))
        rows.append({'input_energy_label':index,'degenerate_ground_coherence':index==0,'joint_energy_flag_probabilities':{str(k):str(v) for k,v in sorted(target_probs.items())},'exact_probability_equality':True})
    assert mixed_actual==mixed_target and cross_defects
    return {'arithmetic':'Exact fractions.Fraction; no floating tolerances','system_levels':['0 with multiplicity 2','1','sqrt(2)'],'flags':2,'finite_reservoir_dimension':nr,'total_dimension':dim,'profile':'Normalized rational buffered product state, proving the probability identity does not require a sine profile','sequence_composition_exact':True,'charge_conservation_exact':True,'individual_rows':rows,'stationary_mixture_weights':[str(w) for w in weights],'stationary_mixture_joint_probabilities_exact':True,'largest_detected_cross_energy_coherence_defect':str(max(cross_defects)),'claim_limit':'Exact probabilities do not imply exact output coherences.'}


def nonstationary_counterexample():
    # U maps the coherent input (3/5,4/5) to ground with certainty.
    U={(0,0):Q(3,5),(0,1):Q(4,5),(1,0):Q(-4,5),(1,1):Q(3,5)}
    V,_,n=own.rational_lift(U,[(0,),(1,)],2,False)
    nr=n//2;x={0:Q(3,5),1:Q(4,5)};eta={1:Q(3,5),2:Q(4,5)}
    joint={a*nr+r:amp*b for a,amp in x.items() for r,b in eta.items()}
    actual=matvec(V,joint);target=matvec(U,x)
    pg=sum(v*v for i,v in actual.items() if i//nr==0)
    assert target=={0:Q(1)} and pg==Q(11881,15625)
    return {'input':[str(x[i]) for i in range(2)],'buffered_battery':[str(eta[i]) for i in (1,2)],'ideal_ground_probability':'1','implemented_ground_probability':str(pg),'difference':str(1-pg),'stationary_hypothesis_essential':True}


def eigen_projectors(H):
    vals,q=np.linalg.eigh(H)
    return [q[:,abs(vals-e)<2e-11]@q[:,abs(vals-e)<2e-11].conj().T for e in (0,4,10)]


def own_star_histories():
    states,F,W,js=own.build_star();C=2;eps=1/math.sqrt(C);H=C*C*(W-eps*F).T@(W-eps*F)
    ell=np.zeros(16);ell[states.index((1,0,0,0))]=1
    for b in range(1,4):
        q=[0]*4;q[b]=1;ell[states.index(tuple(q))]=eps
    ell/=np.linalg.norm(ell);Ps=eigen_projectors(H)
    assert np.linalg.norm(Ps[0]@ell-ell)<1e-12
    # The buffered product sine state is shifted separately by final energy.
    L=3;b=np.zeros(L+2);b[1:L+1]=own.sine(L);eta=np.kron(b,b)
    coords=list(itertools.product(range(L+2),repeat=2));loc={n:i for i,n in enumerate(coords)}
    shifts=[]
    for v in ((0,0),(1,0),(0,1)):
        shifted=np.zeros(len(eta))
        for n,a in zip(coords,eta):
            if a:shifted[loc[(n[0]-v[0],n[1]-v[1])]]+=a
        assert abs(np.linalg.norm(shifted)-1)<1e-12;shifts.append(shifted)
    rows=[]
    for instrument in ('resolved','coherent'):
        marks=js if instrument=='resolved' else [js[2*i]+js[2*i+1] for i in range(3)]
        Ls=[math.sqrt(.7*C)*j for j in marks]
        Ks,_,_=own.cp_step(H,Ls,.01)
        maximum=0.;normtotal=0.;energytarget=0.;energyactual=0.
        for j,k in itertools.product(range(len(Ks)),repeat=2):
            target=Ks[k]@Ks[j]@ell
            actual=sum(np.outer(P@target,shift) for P,shift in zip(Ps,shifts))
            for energy,P in zip((0,4,10),Ps):
                expected=float(np.linalg.norm(P@target)**2)
                obtained=float(np.linalg.norm(P@actual)**2)
                maximum=max(maximum,abs(expected-obtained));normtotal+=obtained
                energytarget+=energy*expected;energyactual+=energy*obtained
        assert abs(normtotal-1)<3e-12 and maximum<3e-12
        rows.append({'instrument':instrument,'step_count':2,'complete_flag_histories':len(Ks)**2,'max_joint_history_energy_probability_error':maximum,'total_probability':normtotal,'target_energy':energytarget,'finite_supply_energy':energyactual,'source_builder':'own frozen PRE primitive sixteen-state model only'})
    return rows


def collision_rows_from_own_builder():
    path=own.locate('full_instrument_energy_supply_author/MARKED_COLLISION_RESULTS.json')
    assert hashlib.sha256(path.read_bytes()).hexdigest()=='5ad28116cc9e3267a43abc291805a6b839bcdc394e0980e10fb2f82d42ee3b31'
    original=json.loads(path.read_text())['collision_rows']
    states,F,W,js=own.build_star();C=6;eps=1/math.sqrt(C)
    E2=np.diag([sum(q[b]**2 for b in (1,2,3)) for q in states])
    assert np.max(E2)==3
    I=np.eye(16);T=.2;result=[]
    ell=np.zeros(16);ell[states.index((1,0,0,0))]=1
    for b in range(1,4):
        q=[0]*4;q[b]=1;ell[states.index(tuple(q))]=eps
    ell/=np.linalg.norm(ell);rho=np.outer(ell,ell).reshape(-1,order='F')
    for lam,instrument in ((0.,'resolved'),(1.,'coherent')):
        H=C*C*(W-eps*F).T@(W-eps*F)+lam*E2
        marks=js if instrument=='resolved' else [js[2*i]+js[2*i+1] for i in range(3)]
        Ls=[math.sqrt(.7*C)*j for j in marks]
        D=own.dissipator_super(Ls);A=-1j*(np.kron(I,H)-np.kron(H.T,I))
        exact=expm(T*(A+D));erho=(exact@rho).reshape(16,16,order='F')
        exactenergy=float(np.trace(H@erho).real)
        for steps in (16,32,64,128):
            Ks,_,_=own.cp_step(H,Ls,T/steps)
            channel=sum(np.kron(k.conj(),k) for k in Ks)
            repeat=np.linalg.matrix_power(channel,steps);error=repeat-exact
            resultenergy=float(np.trace(H@(repeat@rho).reshape(16,16,order='F')).real)
            frob=float(np.linalg.norm(error));choi=own.trace_norm(own.super_to_choi(error,16))
            source=next(x for x in original if x['lambda']==lam and x['instrument']==instrument and x['steps']==steps)
            residuals={'exact_energy':abs(exactenergy-source['exact_GKLS_energy']),'collision_energy':abs(resultenergy-source['collision_energy']),'Frobenius_error':abs(frob-source['full_superoperator_Frobenius_error']),'Choi_trace_norm':abs(choi-source['unnormalized_Choi_trace_norm_upper_bound'])}
            assert max(residuals.values())<2e-10
            result.append({'lambda':lam,'instrument':instrument,'steps':steps,'own_exact_energy':exactenergy,'own_collision_energy':resultenergy,'own_superoperator_Frobenius_error':frob,'own_unnormalized_Choi_trace_norm':choi,'absolute_author_row_differences':residuals})
    return result


if __name__=='__main__':
    result={'exact_stationary_history':rational_stationary_history(),'nonstationary_counterexample':nonstationary_counterexample(),'complete_star_two_step_histories':own_star_histories(),'author_collision_rows_reconstructed':collision_rows_from_own_builder(),'all_assertions_passed':True,'independence':'Only own frozen PRE code imported; released author code read but never imported. Author result numbers are comparison targets after own calculations.'}
    (HERE/'COMPARISON_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'all_assertions_passed':True,'exact_stationary_mixture':result['exact_stationary_history']['stationary_mixture_joint_probabilities_exact'],'nonstationary_counterexample':result['nonstationary_counterexample'],'two_step_star_histories':result['complete_star_two_step_histories'],'author_collision_rows':len(result['author_collision_rows_reconstructed']),'max_author_row_difference':max(max(x['absolute_author_row_differences'].values()) for x in result['author_collision_rows_reconstructed'])},indent=2))
