"""Disclosed author controls for the full cube energy theorem; no cube limit simulation."""
from pathlib import Path
from collections import defaultdict
from types import SimpleNamespace
import hashlib,json,time,math
import numpy as np
from scipy.linalg import expm,solve_continuous_lyapunov

ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS = ['docs/FULL_ORIGINAL_CUBE_ENSEMBLE_ENERGY_AND_RARE_MATTER_FIELD_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RECENT_BIRTHS_FORCE_FULL_CUBE_ENERGY_VARIANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/SHARP_ACTUAL_ROTOR_CUBE_ENERGY_TAIL_BOUNDED_THEOREM_NOTE_2026-09-24.md']
REUSED_SHA='8f4320e1cb333098bb3a609b0a95366380ffc7f1c693cffb8342d757fbc7a09a'
ROOT_CONTROL_SHA='7354476b7b253e966f66bfe0b3d6cca32f3949b18c4208470de27951e33ad7c7'
RESULT_PATH='outputs/full_original_cube_energy_20260924/FULL_ENSEMBLE_ENERGY_RESULTS.json'

A=(0,3,5,6)

B=(1,2,4,7)

EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))

INDEX={edge:i for i,edge in enumerate(EDGES)}

def charges(E):
    q=[int(v in A) for v in range(8)]
    for m,(a,b) in zip(E,EDGES):q[a]+=m;q[b]-=m
    assert max(abs(x) for x in q)<=1
    return q

def weight(m,k,S):
    if S is None:return 1
    if abs(m+k)>S:return 0.
    w=1-m*(m+k)/(S*(S+1));assert w>=-1e-14
    return math.sqrt(max(0.,w))

def hop(v,S=None,centers=A):
    out=defaultdict(complex)
    for E,c in v.items():
        q=charges(E)
        for e,(a,b) in enumerate(EDGES):
            if a not in centers or not q[a] or q[b]:continue
            k=-q[a];w=weight(E[e],k,S)
            if not w:continue
            ee=list(E);ee[e]+=k;charges(ee);out[tuple(ee)]+=c*w
    return {E:c for E,c in out.items() if abs(c)>1e-14}

def cycle(edges):
    E=[0]*12
    for edge,sign in edges:E[INDEX[edge]]=sign
    assert charges(E)==[int(v in A) for v in range(8)]
    return tuple(E)

def source_algebra():
    m=SimpleNamespace(cycle=cycle,hop=hop,INDEX=INDEX,charges=charges,weight=weight,EDGES=EDGES)
    c1=m.cycle([((0,1),1),((3,1),-1),((3,2),1),((0,2),-1)])
    c2=m.cycle([((0,1),1),((5,1),-1),((5,4),1),((0,4),-1)])
    inputs=[(0,)*12,c1,tuple(-x for x in c1),c2,tuple(x+y for x,y in zip(c1,c2))]

    def mark_edge(v,edge,signs,S):
        out=defaultdict(complex);k=m.INDEX[edge];a,b=edge
        for E,c in v.items():
            q=m.charges(E)
            if q[a] or q[b]:continue
            for sign in signs:
                w=m.weight(E[k],sign,S)
                if not w:continue
                ee=list(E);ee[k]+=sign;m.charges(ee);out[tuple(ee)]+=c*w
        return dict(out)

    def raw_sum(*terms):
        out=defaultdict(complex)
        for a,v in terms:
            for k,c in v.items():out[k]+=a*c
        return dict(out)

    rows=[];mutant_nonzero=0
    for S in (None,2,3,7,21,100):
        vectors=list(inputs)
        if S is not None:vectors.append(tuple(S*x for x in c1))
        residual1=[];residual2=[];wrong=[]
        for E in vectors:
            v={E:1.};f1=m.hop(v,S);f2=m.hop(f1,S);f3=m.hop(f2,S)
            for edge in m.EDGES:
                for name,signs in [('plus',(1,)),('minus',(-1,)),('coherent',(1,-1))]:
                    j1=mark_edge(f1,edge,signs,S);j2=mark_edge(f2,edge,signs,S);j3=mark_edge(f3,edge,signs,S)
                    fj1=m.hop(j1,S);fj2=m.hop(j2,S);ffj1=m.hop(fj1,S)
                    r=raw_sum((1,j2),(-2,fj1),(2,m.hop(mark_edge(m.hop(v,S,(edge[0],)),edge,signs,S),S,(edge[0],))))
                    triple=raw_sum((1,j3),(-3,fj2),(3,ffj1))
                    mutant=raw_sum((1,j3),(-1,fj2),(3,ffj1))
                    norm=lambda x:float(sum(abs(c)**2 for c in x.values()))
                    residual1.append(norm(r));residual2.append(norm(triple));wrong.append(norm(mutant))
                    if norm(mutant)>1e-10:mutant_nonzero+=1
        assert max(residual1)<1e-24 and max(residual2)<1e-23
        if S is None:assert max(residual1)==max(residual2)==0
        rows.append({'S':S,'input_count':len(vectors),'edge_mark_checks':len(residual1),
                     'max_twice_first_high_identity_residual_squared':max(residual1),
                     'max_six_times_second_high_coefficient_residual_squared':max(residual2),
                     'missing_middle_factor_mutant_max_norm_squared':max(wrong),
                     'moving_boundary_word_included':S is not None})
    assert mutant_nonzero>0
    return {'rows':rows,'mutant_nonzero_cases':mutant_nonzero,
            'reused_helper_sha256':REUSED_SHA,
            'scope':'Explicit reuse of root charge, normalized-shift and hop helpers; new all-edge triple coefficient and boundary checks. Rotor integer coefficients are exact in these operations; spin weights are floating checks. This is not an independent reconstruction or a uniform contour-series proof.'}

def vec(a):return a.reshape(-1,order='F')

def mat(a,n):return a.reshape((n,n),order='F')

def liouville(K):return np.kron(np.eye(len(K)),K)+np.kron(K.conj(),np.eye(len(K)))

def trace_norm(a):return float(np.linalg.svd(a,compute_uv=False).sum())

def realtrace(a):
    z=np.trace(a);assert abs(z.imag)<1e-8*max(1.,abs(z.real));return float(z.real)

def driven_blocks(generator_in,generator_out,source,rho0,t):
    ni=len(generator_in);no=len(generator_out)
    full=np.zeros((ni+no,ni+no),complex)
    full[:ni,:ni]=generator_in;full[ni:,:ni]=source;full[ni:,ni:]=generator_out
    state=expm(t*full)@np.concatenate([vec(rho0),np.zeros(no,complex)])
    n=int(round(ni**.5));m=int(round(no**.5))
    return mat(state[:ni],n),mat(state[ni:],m)

def evolving_input_cascade():
    delta=1.1;kappa=.17;b=2.;r=4.;age_cap=2.6
    hI=np.array([[.3,.7],[.7,-.2]],complex)
    hB=np.array([[-.4,.2+.1j],[.2-.1j,.1]],complex)
    Q=np.array([[1.,.2j],[-.3,.65]],complex)
    B=np.array([[.2,.1],[.1,-.4]],complex)
    G=np.block([[np.zeros((2,2)),Q.conj().T],[Q,B]])
    bright=np.diag([0.,0.,1.,1.]);Z=-1j*delta*G-kappa*bright
    R=np.sqrt(r)*np.vstack([np.eye(2),np.zeros((2,2))])
    psi=np.array([1.,1j])/np.sqrt(2);rho0=np.outer(psi,psi.conj())
    superR=np.kron(R.conj(),R);Lf=liouville(Z);LB=liouville(-1j*hB)
    assert np.max(np.linalg.eigvals(Z).real)<0
    rows=[];targets=[]
    for t in (.4,1.1,2.3):
        LI0=liouville(-1j*hI)-kappa*b*np.eye(4)
        rhoI0,rhoB0=driven_blocks(LI0,LB,kappa*b*np.eye(4),rho0,t)
        source=R@rhoI0@R.conj().T
        Sigma=solve_continuous_lyapunov(Z,-kappa*source)
        lyap_error=np.linalg.norm(Z@Sigma+Sigma@Z.conj().T+kappa*source)
        bright_target=r*np.exp(-kappa*b*t)/2
        assert lyap_error<1e-12 and abs(realtrace(bright@Sigma)-bright_target)<1e-12
        Ecommon=realtrace(hI@rhoI0)+realtrace(hB@rhoB0)
        high_mass=realtrace(Sigma)
        frozen_initial=solve_continuous_lyapunov(Z,-kappa*np.exp(-kappa*b*t)*(R@rho0@R.conj().T))
        wrong_source_distance=trace_norm(Sigma-frozen_initial)
        assert wrong_source_distance>1e-3
        ea=expm(age_cap*Z);Sigma_cap=Sigma-ea@Sigma@ea.conj().T
        targets.append({'t':t,'Sigma_trace':high_mass,'Sigma_bright_trace':realtrace(bright@Sigma),
                        'bright_trace_target':bright_target,'Lyapunov_residual':float(lyap_error),
                        'common_low_mean':Ecommon,'mean_target':Ecommon+delta*high_mass,
                        'scaled_variance_target':delta*delta*high_mass,
                        'incorrect_zero_field_source_trace_distance':wrong_source_distance,
                        'Sigma_real':Sigma.real.tolist(),'Sigma_imag':Sigma.imag.tolist()})
        for eps in (.16,.08,.04,.02,.01):
            lam=kappa*(b+eps*eps*r);LI=liouville(-1j*hI)-lam*np.eye(4)
            rhoI,rhoH=driven_blocks(LI,Lf/eps**2,kappa*eps**2*superR,rho0,t)
            rhoIagain,rhoB=driven_blocks(LI,LB,kappa*b*np.eye(4),rho0,t)
            assert np.linalg.norm(rhoI-rhoIagain)<1e-11
            Hh=delta*eps**-4*np.eye(4)+delta*eps**-2*G
            mean=realtrace(hI@rhoI)+realtrace(hB@rhoB)+realtrace(Hh@rhoH)
            second=realtrace(hI@hI@rhoI)+realtrace(hB@hB@rhoB)+realtrace(Hh@Hh@rhoH)
            var=second-mean*mean
            terminal=1-realtrace(rhoI)-realtrace(rhoB)-realtrace(rhoH)
            assert terminal>=-1e-12 and var>0
            minimum=min(float(np.linalg.eigvalsh((x+x.conj().T)/2).min()) for x in (rhoI,rhoB,rhoH))
            assert minimum>-1e-11
            error=trace_norm(rhoH/eps**4-Sigma)
            start=t-eps**2*age_cap;assert start>0
            source_start=mat(expm(start*LI)@vec(rho0),2)
            _,recent=driven_blocks(LI,Lf/eps**2,kappa*eps**2*superR,source_start,eps**2*age_cap)
            _,old_before=driven_blocks(LI,Lf/eps**2,kappa*eps**2*superR,rho0,t-eps)
            old=mat(expm(Lf/eps)@vec(old_before),4)
            rows.append({'t':t,'epsilon':eps,'full_mean':mean,'mean_target':Ecommon+delta*high_mass,
                         'scaled_full_variance':eps**4*var,'scaled_variance_target':delta*delta*high_mass,
                         'scaled_high_density_trace_distance':error,
                         'scaled_high_trace':realtrace(rhoH)/eps**4,'target_high_trace':high_mass,
                         'scaled_recent_density_trace_distance':trace_norm(recent/eps**4-Sigma_cap),
                         'scaled_older_than_epsilon_high_trace':realtrace(old)/eps**4,
                         'terminal_probability':terminal,'minimum_diagonal_block_eigenvalue':minimum})
        finest=rows[-1]
        assert finest['scaled_high_density_trace_distance']/high_mass<.002
        assert abs(finest['full_mean']-finest['mean_target'])<.003
        assert abs(finest['scaled_full_variance']/finest['scaled_variance_target']-1)<.002
    return {'parameters':dict(delta=delta,kappa=kappa,b=b,r=r,age_cap=age_cap),
            'maximum_real_fast_eigenvalue':float(np.max(np.linalg.eigvals(Z).real)),
            'targets':targets,'rows':rows,
            'scope':'Exact diagonal density blocks of a supplied ten-state GKLS cascade with a rotating two-state initial input, born low doublet, four fast matter states and terminal doublet. A coherent first jump has low amplitude sqrt(kappa b)I and high amplitude sqrt(kappa) epsilon R; the second jump absorbs bright states at rate 2 kappa/epsilon^2. Off-diagonal density blocks are unnecessary for these block-diagonal Hermitian energy moments and are not approximated here. This toy has an exponential fast gap, unlike the cube rotor. No cube limit, QFI or conserving-apparatus claim.'}

def main():
    start=time.monotonic()
    result={'source_algebra':source_algebra(),'evolving_input_cascade':evolving_input_cascade(),
            'elapsed_seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'provenance':{'embedded_author_word_helpers':REUSED_SHA,'reused_author_control':ROOT_CONTROL_SHA}}
    target=ROOT/RESULT_PATH;target.parent.mkdir(parents=True,exist_ok=True)
    data=json.dumps(result,indent=2)+'\n';target.write_text(data)
    print(data,end='');print('TOTAL: PASS=2 FAIL=0')

if __name__=='__main__':main()
