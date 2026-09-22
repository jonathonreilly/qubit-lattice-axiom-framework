#!/usr/bin/env python3
"""Personal exact checks of the total kernel and all-frontier activation.
All fixtures are constructed here; only this source is read for integrity.
Finite checks do not independently review the arbitrary-horizon proof.
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 300
from functools import lru_cache
from pathlib import Path
import hashlib,itertools,json
import numpy as np
import sympy as sp

I=sp.eye(2);ZERO=sp.zeros(2)
PZ=sp.diag(1,0);PX=sp.ones(2)/2
PY=sp.Matrix([[1,-sp.I],[sp.I,1]])/2
PV=sp.Matrix([[9,12],[12,16]])/25
DIRS=tuple(tuple(s if i==a else 0 for i in range(3)) for a in range(3) for s in (-1,1))
assert len(set(DIRS))==6

def clean(A):return A.applyfunc(sp.simplify)
def adjacent(z):return [tuple(z[i]+d[i] for i in range(3)) for d in DIRS]
def psi(u):
    u=sp.simplify(u)
    if u<=sp.Rational(1,4):return sp.Integer(1)
    if u>=1:return sp.Integer(0)
    a=sp.exp(-1/(1-u));b=sp.exp(-1/(u-sp.Rational(1,4)))
    return a/(a+b)

@lru_cache(None)
def tags(key):
    A=sp.Matrix(2,2,key);tr=sp.trace(A);det=A.det()
    return (psi(abs(tr-5)**2),psi(abs(tr-17)**2+abs((A-8*I).det())**2),
            psi(abs(tr-1)**2+abs(det)**2),psi(abs(tr-4)**2+abs(det-4)**2))

@lru_cache(None)
def rate_from_counts(c,q,u,v):
    a=(psi((c-1)**2+(q-1)**2+u*u+v*v)
       +psi(c*c+q*q+(u-1)**2+v*v)
       +psi(c*c+q*q+(u-1)**2+(v-1)**2))
    return sp.simplify(a/(a+(a-1)**2))

def rate(neighbors):
    count=[0,0,0,0]
    for A in neighbors:
        if A is not None:
            for i,x in enumerate(tags(tuple(A))):count[i]+=x
    return rate_from_counts(*count)

def kernel(neighbors,smooth=False):
    present=[A for A in neighbors if A is not None]
    tagged=[tags(tuple(A)) for A in present]
    pairs=[(i,j,tagged[i][0]*tagged[j][1]) for i in range(len(present))
           for j in range(len(present)) if i!=j]
    S=sum(w for _,_,w in pairs);b=(S-1)**2;Z=S+b
    assert Z>=sp.Rational(3,4)
    atoms=[(b/Z,sum(present,ZERO))]
    for i,j,w in pairs:
        if w==0:continue
        P=present[j]-8*I;x=sp.simplify(sp.re(sp.trace((present[i]-2*I)*P)))
        if x<=0:f=sp.Integer(0)
        elif x>=1:f=sp.Integer(1)
        elif smooth:f=sp.exp(-1/x)/(sp.exp(-1/x)+sp.exp(-1/(1-x)))
        else:f=x
        atoms.extend([(w*f/Z,P),(w*(1-f)/Z,I-P)])
    out={}
    for mass,A in atoms:
        mass=sp.simplify(mass)
        if mass==0:continue
        key=tuple(clean(A));out[key]=sp.simplify(out.get(key,0)+mass)
    assert sp.simplify(sum(out.values())-1)==0
    return [(mass,sp.Matrix(2,2,key)) for key,mass in out.items()]

def local_inputs(state,z):return [state.get(n) for n in adjacent(z)]
def active_sites(state):
    # Discover every blank site on the whole finite frontier. The intended
    # corridor coordinates are not passed into this function.
    fringe={n for z in state for n in adjacent(z)}-state.keys()
    return [(z,r) for z in sorted(fringe) if (r:=rate(local_inputs(state,z)))!=0]

def rotations():
    result=[]
    for p in itertools.permutations(range(3)):
        for signs in itertools.product((-1,1),repeat=3):
            R=np.zeros((3,3),dtype=int)
            for i in range(3):R[i,p[i]]=signs[i]
            if round(np.linalg.det(R))==1:result.append(R)
    assert len(result)==24
    return result

def seed(programs,rho,G=I,R=None,guards=True,tag_program=True):
    def locate(x):
        a=np.array(x,dtype=int)
        if R is not None:a=R@a+np.array([11,-7,4])
        return tuple(int(v) for v in a)
    encode=lambda A:clean(G*A*G.inv())
    state={locate((-1,0,0)):encode(2*I+rho)}
    for j,P in enumerate(programs):
        state[locate((3*j,-1,0))]=encode(8*I+P if tag_program else P)
        state[locate((3*j+2,1,0))]=2*I
    order=[locate((x,0,0)) for x in range(3*len(programs))]
    core=set(state)|set(order)
    guard={n for z in core for n in adjacent(z)}-core
    if guards:state.update({z:ZERO for z in guard})
    return state,order,len(guard)

def run(programs,rho,G=I,R=None):
    initial,order,guard_count=seed(programs,rho,G,R)
    branches=[(sp.Integer(1),initial,[])];events=0;frontiers=0
    for step,wanted in enumerate(order):
        updated=[]
        for mass,state,labels in branches:
            active=active_sites(state);frontiers+=1
            assert active==[(wanted,1)],(step,active,wanted)
            old=dict(state)
            atoms=kernel(local_inputs(state,wanted))
            if step%3==1:
                assert len(atoms)==1 and atoms[0][0]==1 and atoms[0][1]==state[order[step-1]]
            if step%3==2:
                assert len(atoms)==1 and atoms[0][0]==1 and atoms[0][1]==2*I+state[order[step-1]]
            for p,A in atoms:
                labels2=list(labels)
                if step%3==0:
                    P=clean(G*programs[step//3]*G.inv())
                    if A==P:labels2.append(0)
                    elif A==I-P:labels2.append(1)
                    else:raise AssertionError(('invalid outcome',step,A))
                new=dict(state);new[wanted]=A
                assert all(new[z]==a for z,a in old.items())
                updated.append((sp.simplify(mass*p),new,labels2));events+=1
        branches=updated
    records=[]
    for mass,state,labels in branches:
        assert active_sites(state)==[];frontiers+=1
        assert len(state)==len(initial)+len(order)
        sigma=rho
        for P,label in zip(programs,labels):
            outcome=P if label==0 else I-P
            sigma=clean(outcome*sigma*outcome)
        direct=sp.simplify(sp.trace(sigma))
        assert sp.simplify(direct-mass)==0
        records.append({'labels':labels,'local_probability':str(mass),'ordered_product_probability':str(direct)})
    assert sp.simplify(sum(m for m,_,_ in branches)-1)==0
    return {'length':len(programs),'seed_records':len(initial),'guard_records':guard_count,
            'new_records_per_branch':len(order),'positive_histories':len(branches),
            'all_frontier_states_checked':frontiers,'marked_branch_events':events,'histories':records}

def float_kernel_and_rate(neighbors,smooth=False):
    def h(t):return 0. if t<=0 else float(np.exp(-1/t))
    def cutoff(t):return h(1-t)/(h(1-t)+h(t-.25))
    mats=[A for A in neighbors if A is not None]
    eye=np.eye(2)
    tagged=[]
    for A in mats:
        tr=np.trace(A);det=np.linalg.det(A)
        tagged.append([cutoff(abs(tr-5)**2),cutoff(abs(tr-17)**2+abs(np.linalg.det(A-8*eye))**2),
                       cutoff(abs(tr-1)**2+abs(det)**2),cutoff(abs(tr-4)**2+abs(det-4)**2)])
    c,q,u,v=np.sum(tagged,axis=0) if tagged else np.zeros(4)
    a=(cutoff((c-1)**2+(q-1)**2+u*u+v*v)+cutoff(c*c+q*q+(u-1)**2+v*v)
       +cutoff(c*c+q*q+(u-1)**2+(v-1)**2))
    lam=a/(a+(a-1)**2)
    pairs=[(i,j,tagged[i][0]*tagged[j][1]) for i in range(len(mats)) for j in range(len(mats)) if i!=j]
    S=sum(w for _,_,w in pairs);b=(S-1)**2;Z=S+b
    law=[(b/Z,sum(mats,np.zeros((2,2),dtype=complex)))]
    for i,j,w in pairs:
        P=mats[j]-8*eye;x=float(np.trace((mats[i]-2*eye)@P).real)
        f=h(x)/(h(x)+h(1-x)) if smooth else float(np.clip(x,0,1))
        law.extend([(w*f/Z,P),(w*(1-f)/Z,eye-P)])
    return law,float(lam)

def off_code_checks():
    rng=np.random.default_rng(310915)
    records=[]
    G=np.array([[1,2+.3j],[.2j,1]],dtype=complex);Gi=np.linalg.inv(G)
    bases=[np.diag([2.3,2.7]),np.diag([9.,8.]),np.diag([1.,0.]),2*np.eye(2)]
    for index in range(64):
        rand=lambda:rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        mode=index%4
        selected=[[0,1],[2],[2,3],[0,1,2,3]][mode]
        inputs=[bases[k]+(.04 if index%2 else .31)*rand() for k in selected]+[None]
        smooth=bool(index%2)
        law,lam=float_kernel_and_rate(inputs,smooth)
        assert 0<=lam<=1 and min(p for p,_ in law)>=0 and abs(sum(p for p,_ in law)-1)<3e-13
        transformed,other_rate=float_kernel_and_rate([G@A@Gi if A is not None else None for A in inputs],smooth)
        weights=max(abs(p-q) for (p,_),(q,_) in zip(law,transformed))
        atoms=max(float(np.max(abs(G@A@Gi-B))) for (_,A),(_,B) in zip(law,transformed))
        assert weights<3e-11 and atoms<3e-12 and abs(lam-other_rate)<3e-11
        conjugated,conj_rate=float_kernel_and_rate([A.conj() if A is not None else None for A in inputs],smooth)
        assert max(abs(p-q) for (p,_),(q,_) in zip(law,conjugated))<3e-13
        assert max(float(np.max(abs(A.conj()-B))) for (_,A),(_,B) in zip(law,conjugated))<3e-13
        assert abs(lam-conj_rate)<3e-13
        perm=rng.permutation(len(inputs));shuffled,shuffle_rate=float_kernel_and_rate([inputs[i] for i in perm],smooth)
        probe=rand()
        characteristic=lambda rows:sum(p*np.exp(1j*np.trace(probe@A).real) for p,A in rows)
        permutation_error=abs(characteristic(law)-characteristic(shuffled))
        assert permutation_error<3e-12 and abs(lam-shuffle_rate)<3e-12
        direction=rand();continuity=[]
        for step in (1e-2,1e-3,1e-4,1e-5):
            nearby=list(inputs);nearby[0]=nearby[0]+step*direction
            shifted,shift_rate=float_kernel_and_rate(nearby,smooth)
            continuity.append({'step':step,'characteristic_change':float(abs(characteristic(law)-characteristic(shifted))),
                               'rate_change':abs(lam-shift_rate)})
        assert continuity[-1]['characteristic_change']<.002 and continuity[-1]['rate_change']<.002
        records.append({'family':mode,'smooth_f':smooth,'rate':lam,'similarity_weight_error':weights,
                       'similarity_atom_error':atoms,'permutation_error':float(permutation_error),'continuity':continuity})
    return {'cases':records,'limits':'Finite floating probes, no interval certification or numerical differentiability proof.'}

def main():
    rho=sp.Rational(3,5)*PZ+sp.Rational(2,5)*PX
    programs=[PZ,PX,PY,PV,PZ]
    base=run(programs,rho)
    zero=run([PZ,PZ,PZ],PZ)
    assert zero['positive_histories']==1
    similarities=[sp.Matrix([[1,2],[0,1]]),sp.Matrix([[1,sp.I],[1,1]]),
                  sp.Matrix([[2,1-sp.I],[0,sp.Rational(1,3)]])]
    transformed=[run(programs[:3],rho,G) for G in similarities]
    rotated=[run(programs[:2],rho,R=R) for R in rotations()]
    assert all(x['histories']==rotated[0]['histories'] for x in rotated)
    # These malformed seeds are actual countercontrols: discover all unintended
    # active sites rather than merely check that a declared mask is missing.
    unguarded,order,_=seed(programs[:2],rho,guards=False)
    no_guard_active=active_sites(unguarded)
    assert len(no_guard_active)>1
    untagged,order,_=seed(programs[:2],rho,tag_program=False)
    no_tag_active=active_sites(untagged)
    assert no_tag_active!=[(order[0],1)]
    assert rate([])==0 and rate([ZERO]*6)==0
    quarter=[2*I+sp.diag(sp.Rational(1,4),sp.Rational(3,4)),8*I+PZ]
    smooth_probability=next(p for p,A in kernel(quarter,smooth=True) if A==PZ)
    assert sp.simplify(smooth_probability-1/(1+sp.exp(sp.Rational(8,3))))==0
    # Non-mutually-unbiased programs challenge transition weights at several
    # unequal probabilities instead of relying only on half-probability rows.
    PW=sp.Matrix([[4,2-2*sp.I],[2+2*sp.I,2]])/6
    diverse=run([PZ,PV,PW,PY,PX],rho)
    result={'status':'personal_exact_and_floating_checks_not_independent_review',
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'five_measurements':base,'zero_branch_control':zero,
      'diverse_projective_history':diverse,'off_code':off_code_checks(),
      'nonunitary_similarities':len(transformed),'proper_rotations':len(rotated),
      'guard_omission_active_sites':no_guard_active,'program_tag_omission_active_sites':no_tag_active,
      'smooth_alternative_quarter':str(sp.simplify(smooth_probability)),
      'holding_time_statement':'Erlang shape3L follows analytically from exactly one rate-one active site; no simulation used.'}
    print('EVIDENCE_JSON: '+json.dumps(result,sort_keys=True,default=str))
    print('per_element: exact matrix tags, atom weights, copies and retags are evaluated with rational complex entries.')
    print('per_site: every blank site on each finite Record frontier is tested for its actual local activation rate.')
    print('per_mode: one-qubit projective transcript weights are compared with independently ordered matrix products.')
    print('per_block: all finite branches, zero outcomes, nonunitary similarities and proper cubic rotations are executed.')
    print('lattice_wide: checked and not executed — arbitrary-horizon induction and finite-seed nonexplosion use the written proofs.')
    print('TOTAL: PASS=8 FAIL=0')
if __name__=='__main__':main()
