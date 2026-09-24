#!/usr/bin/env python3
"""Root local-operator and mixed-state controls, not a full cube simulation."""
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=('docs/MIXED_LOW_FIELD_INPUTS_RETAIN_CUBE_BIRTH_ENERGY_AND_COHERENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/GENERAL_MICROSCOPIC_BIRTH_ENERGY_AND_CUBE_POWER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ACTUAL_CUBE_BIRTH_APPARATUS_COHERENCE_AND_ENERGY_RANGE_BOUNDED_THEOREM_NOTE_2026-09-24.md')
from pathlib import Path
from collections import defaultdict
import hashlib,itertools,json,math,time
import numpy as np

HERE=Path(__file__).resolve().parents[1]/'outputs/mixed_low_field_birth_energy_20260924'
A=(0,3,5,6);B=(1,2,4,7)
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

def mark(v,signs,S=None):
    out=defaultdict(complex)
    for E,c in v.items():
        q=charges(E)
        if q[0] or q[1]:continue
        for sign in signs:
            w=weight(E[0],sign,S)
            if not w:continue
            ee=list(E);ee[0]+=sign;charges(ee);out[tuple(ee)]+=c*w
    return {E:c for E,c in out.items() if abs(c)>1e-14}

def combine(*terms):
    out=defaultdict(complex)
    for scalar,v in terms:
        for E,c in v.items():out[E]+=scalar*c
    return {E:c for E,c in out.items() if abs(c)>1e-13}

def dot(a,b):return sum(c.conjugate()*b.get(E,0) for E,c in a.items())

def cycle(edges):
    E=[0]*12
    for edge,sign in edges:E[INDEX[edge]]=sign
    assert charges(E)==[int(v in A) for v in range(8)]
    return tuple(E)

def coefficient_controls():
    c1=cycle([((0,1),1),((3,1),-1),((3,2),1),((0,2),-1)])
    c2=cycle([((0,1),1),((5,1),-1),((5,4),1),((0,4),-1)])
    c3=cycle([((0,2),1),((6,2),-1),((6,4),1),((0,4),-1)])
    inputs=[(0,)*12,c1,tuple(-x for x in c1),c2,c3,tuple(x+y for x,y in zip(c1,c2))]
    rotor_rows=[];spin_rows=[];mutations=[]
    for label,signs,b,r in [('plus',(1,),2,4),('minus',(-1,),2,2),('coherent',(1,-1),4,6)]:
        vectors=[]
        for E in inputs:
            v={E:1.};born=mark(hop(v),signs)
            canonical=combine((.5,mark(hop(hop(v)),signs)),(-1,hop(born)))
            local=combine((-1,hop(mark(hop(v,centers=(0,)),signs),centers=(0,))))
            assert not combine((1,canonical),(-1,local))
            assert dot(born,born)==b and dot(local,local)==r
            assert all(not any(charges(e)[a]==charges(e)[bb]==0 for a,bb in EDGES) for e in local)
            mutant=combine((1,mark(hop(hop(v)),signs)),(-1,hop(born)))
            mutations.append(float(dot(combine((1,mutant),(-1,local)),combine((1,mutant),(-1,local))).real))
            vectors.append((born,local))
        gramB=np.array([[dot(x[0],y[0]) for y in vectors] for x in vectors])
        gramR=np.array([[dot(x[1],y[1]) for y in vectors] for x in vectors])
        assert np.array_equal(gramB,b*np.eye(len(inputs))) and np.array_equal(gramR,r*np.eye(len(inputs)))
        rotor_rows.append({'mark':label,'b':b,'r':r,'input_dimension':len(inputs),'Gram_B_diagonal':gramB.diagonal().real.tolist(),'Gram_R_diagonal':gramR.diagonal().real.tolist(),'both_offdiagonals_exact_zero':True})
        for S in (3,5,10,30,100):
            C=S*(S+1);deltas=[];rows=[]
            for E in inputs:
                v={E:1.};born=mark(hop(v,S),signs,S)
                canonical=combine((.5,mark(hop(hop(v,S),S),signs,S)),(-1,hop(born,S)))
                local=combine((-1,hop(mark(hop(v,S,(0,)),signs,S),S,(0,))))
                residual=dot(combine((1,canonical),(-1,local)),combine((1,canonical),(-1,local))).real
                assert residual<1e-24
                x,y,z=[E[INDEX[e]] for e in ((0,1),(0,2),(0,4))]
                hp=lambda m:1-m*(m-1)/C
                hm=lambda m:1-m*(m+1)/C
                f=lambda m,s:1-m*(m+s)/C
                predicted_b=sum(f(x,s)*(hp(y)+hp(z)) for s in signs)
                predicted_r=sum(4*f(x,1)*hp(y)*hp(z) if s==1 else f(x,-1)*(hp(y)*hm(z)+hp(z)*hm(y)) for s in signs)
                actual_b=dot(born,born).real;actual_r=dot(local,local).real
                assert abs(actual_b-predicted_b)<1e-12 and abs(actual_r-predicted_r)<1e-12
                deltas.append(max(abs(actual_b-b),abs(actual_r-r)))
                rows.append({'source_fields':E,'b_S':actual_b,'r_S':actual_r,'formula_b':predicted_b,'formula_r':predicted_r})
            spin_rows.append({'mark':label,'S':S,'max_coefficient_error':max(deltas),'C_times_max_error':C*max(deltas),'rows':rows})
    assert min(mutations)>0
    # A moving boundary input is intentionally outside the fixed-support class.
    boundary=[]
    for S in (1,3,10):
        E=tuple(S*x for x in c1);v={E:1.};born=mark(hop(v,S),(1,),S)
        local=hop(mark(hop(v,S,(0,)),(1,),S),S,(0,))
        assert not born and not local
        boundary.append({'S':S,'moving_flux':S,'plus_b':0,'plus_r':0})
    return {'input_field_words':inputs,'rotor':rotor_rows,'finite_spin':spin_rows,
            'wrong_canonical_half_factor_difference_norm_squared':mutations,
            'moving_boundary_counterexample_to_uniform_box_constants':boundary,
            'scope':'Actual local charge/field operators and canonical leading coefficients only; no full canonical eigenproblem or joint-time evolution.'}

def fisher(sigma,H):
    values,Q=np.linalg.eigh(sigma);values=np.maximum(values,0)
    rotated=Q.conj().T@H@Q
    den=values[:,None]+values[None,:];num=(values[:,None]-values[None,:])**2
    ratio=np.divide(num,den,out=np.zeros_like(num),where=den>1e-18)
    return float(2*np.sum(ratio*abs(rotated)**2))

def mixed_witness_controls():
    rng=np.random.default_rng(924083);n=4
    z=rng.normal(size=n)+1j*rng.normal(size=n);z/=np.linalg.norm(z)
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));rho=X@X.conj().T;rho/=np.trace(rho)
    densities={'pure':np.outer(z,z.conj()),'maximally_mixed':np.eye(n)/n,'mixed_noncommuting':rho}
    K=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));K=(K+K.conj().T)/4
    M=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));M=(M+M.conj().T)/5
    VB=np.vstack([np.eye(n),np.zeros((n,n))]);VR=np.vstack([np.zeros((n,n)),np.eye(n)])
    test=1j*(VR@VB.T-VB@VR.T);test2=test@test
    alpha=.1;rows=[]
    for mark,b,r in [('plus',2,4),('minus',2,2),('coherent',4,6)]:
        for label,rho in densities.items():
            series=[]
            for eps in (.12,.06,.03,.015):
                H=np.zeros((2*n,2*n),complex);H[:n,:n]=K;H[n:,n:]=eps**-4*np.eye(n)+eps**-2*M
                actual=alpha*(eps*math.sqrt(b)*VB+eps**2*math.sqrt(r)*VR)
                omega=actual@rho@actual.conj().T;p=float(np.trace(omega).real)
                derivative=float(abs(np.trace(omega@(1j*(H@test-test@H)))))
                denominator=float(np.trace(omega@test2).real)
                F=fisher(omega,H);lower=derivative*derivative/denominator
                assert F+1e-8*max(1,F)>=lower
                pinched=omega.copy();pinched[:n,n:]=0;pinched[n:,:n]=0
                norm=float(np.sum(abs(np.linalg.eigvalsh(omega-pinched))))
                predicted=2*alpha*alpha*math.sqrt(b*r)*eps**3
                assert abs(norm/predicted-1)<1e-12
                series.append({'epsilon':eps,'selected_probability':p,'scaled_Fisher':eps**4*F,'scaled_witness_lower':eps**4*lower,
                               'predicted_Fisher_coefficient':4*alpha*alpha*r,'pinched_Fisher':fisher(pinched,H),
                               'pinch_trace_error_over_epsilon_cubed':norm/eps**3,'predicted_error_coefficient':2*alpha*alpha*math.sqrt(b*r)})
            assert abs(series[-1]['scaled_Fisher']/(4*alpha*alpha*r)-1)<.005
            assert abs(series[-1]['scaled_witness_lower']/(4*alpha*alpha*r)-1)<.005
            rows.append({'mark':mark,'density':label,'input_eigenvalues':np.linalg.eigvalsh(rho).tolist(),'series':series})
    return {'rows':rows,'scope':'Paired-isometry finite mixed-state witness with nonconstant internal band energies; this is a resource/leading-map toy, not a full cube apparatus.'}

def main():
    HERE.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();result={'coefficients':coefficient_controls(),'mixed_witness':mixed_witness_controls(),
        'elapsed_seconds':time.monotonic()-started,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'MIXED_PREPARATION_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    print('TOTAL: PASS=2 FAIL=0',flush=True)
if __name__=='__main__':main()
