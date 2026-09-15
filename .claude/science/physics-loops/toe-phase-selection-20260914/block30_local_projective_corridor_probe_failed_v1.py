#!/usr/bin/env python3
"""Exact local-kernel/corridor checks plus floating off-code continuity probes."""
from __future__ import annotations
from pathlib import Path
import hashlib,itertools,json
import numpy as np
import sympy as sp

I=sp.eye(2)
PZ=sp.diag(1,0)
PX=sp.Matrix([[1,1],[1,1]])/2
PY=sp.Matrix([[1,-sp.I],[sp.I,1]])/2
PV=sp.Matrix([[9,12],[12,16]])/25
DIRS=[(s if i==a else 0 for i in range(3)) for a in range(3) for s in (-1,1)]
DIRS=[tuple(v) for v in DIRS]

def simplify_matrix(a):return a.applyfunc(sp.simplify)
def matrix_key(a):return tuple(simplify_matrix(a))
def psi_exact(u):
    u=sp.simplify(u)
    if u<=sp.Rational(1,4):return sp.Integer(1)
    if u>=1:return sp.Integer(0)
    a=sp.exp(-1/(1-u));b=sp.exp(-1/(u-sp.Rational(1,4)))
    return a/(a+b)

def scalar_weight(x,mode):
    x=sp.simplify(sp.re(x))
    if x<=0:return sp.Integer(0)
    if x>=1:return sp.Integer(1)
    if mode=='born':return x
    a=sp.exp(-1/x);b=sp.exp(-1/(1-x))
    return sp.simplify(a/(a+b))

def kernel_exact(neighbors,mode='born'):
    present=[sp.Matrix(a) for a in neighbors if a is not None]
    r=[psi_exact(abs(sp.trace(a)-5)**2) for a in present]
    s=[psi_exact(abs(sp.trace(a)-1)**2+abs(a.det())**2) for a in present]
    pairs=[(i,j,sp.simplify(r[i]*s[j])) for i in range(len(present)) for j in range(len(present)) if i!=j]
    total=sp.simplify(sum(w for _,_,w in pairs));fallback=(total-1)**2
    norm=sp.simplify(total+fallback)
    mean=sum(present,sp.zeros(2))
    atoms=[(fallback/norm,mean)]
    for i,j,w in pairs:
        if w==0:continue
        prob=scalar_weight(sp.trace((present[i]-2*I)*present[j]),mode)
        atoms.extend([(w*prob/norm,present[j]),(w*(1-prob)/norm,I-present[j])])
    merged={}
    for weight,a in atoms:
        weight=sp.simplify(weight)
        if weight==0:continue
        key=matrix_key(a)
        merged[key]=sp.simplify(merged.get(key,0)+weight)
    assert sp.simplify(sum(merged.values())-1)==0
    return [(p,sp.Matrix(2,2,key)) for key,p in merged.items()]

def rotations():
    out=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1,1),repeat=3):
            a=np.zeros((3,3),dtype=int)
            for j in range(3):a[j,perm[j]]=signs[j]
            if round(np.linalg.det(a))==1:out.append(a)
    assert len(out)==24
    return out

def coordinate(a,rotation=None):
    value=np.asarray(a,dtype=int)
    if rotation is not None:value=rotation@value+np.array([11,-7,4])
    return tuple(int(t) for t in value)

def neighbors_at(state,site):
    return [state.get(tuple(site[i]+d[i] for i in range(3))) for d in DIRS]

def corridor(programs,rho,similarity=None,rotation=None):
    G=I if similarity is None else sp.Matrix(similarity)
    Gi=G.inv()
    convert=lambda a:simplify_matrix(G*a*Gi)
    locate=lambda a:coordinate(a,rotation)
    prepared={locate((-1,0,0)):convert(2*I+rho)}
    for j,P in enumerate(programs):
        prepared[locate((3*j,-1,0))]=convert(P)
        prepared[locate((3*j+2,1,0))]=2*I
    branches=[(sp.Integer(1),prepared,[],[])]
    checked_events=0
    for j,P in enumerate(programs):
        updated=[]
        for mass,state,sequence,labels in branches:
            event=locate((3*j,0,0));copy=locate((3*j+1,0,0));next_carrier=locate((3*j+2,0,0))
            actual_neighbors=neighbors_at(state,event)
            assert sum(v is not None for v in actual_neighbors)==2
            atoms=kernel_exact(actual_neighbors)
            for weight,R in atoms:
                expected_plus=convert(P);expected_minus=convert(I-P)
                if R==expected_plus:label=0
                elif R==expected_minus:label=1
                else:raise AssertionError(('unexpected measurement output',j,R))
                nxt=dict(state);nxt[event]=R
                copy_inputs=neighbors_at(nxt,copy)
                assert sum(v is not None for v in copy_inputs)==1
                copied=kernel_exact(copy_inputs)
                assert len(copied)==1 and copied[0][0]==1 and copied[0][1]==R
                nxt[copy]=copied[0][1]
                retag_inputs=neighbors_at(nxt,next_carrier)
                assert sum(v is not None for v in retag_inputs)==2
                retagged=kernel_exact(retag_inputs)
                assert len(retagged)==1 and retagged[0][0]==1 and retagged[0][1]==2*I+R
                nxt[next_carrier]=retagged[0][1]
                assert all(nxt[k]==v for k,v in state.items())
                original_R=P if label==0 else I-P
                updated.append((sp.simplify(mass*weight),nxt,sequence+[original_R],labels+[label]))
                checked_events+=3
        branches=updated
    records=[]
    for mass,state,sequence,labels in branches:
        sigma=rho
        for R in sequence:sigma=simplify_matrix(R*sigma*R)
        direct=sp.simplify(sp.trace(sigma))
        assert sp.simplify(mass-direct)==0
        assert len(state)==1+5*len(programs)
        records.append({'labels':labels,'local_kernel_probability':str(mass),'ordered_matrix_probability':str(direct)})
    assert sp.simplify(sum(branch[0] for branch in branches)-1)==0
    return {'length':len(programs),'positive_histories':len(records),'executed_branch_events':checked_events,'records':records}

def exact_checks():
    rho=sp.Rational(3,5)*PZ+sp.Rational(2,5)*PX
    programs=[PZ,PX,PY,PV,PZ]
    base=corridor(programs,rho)
    repeated=corridor([PZ,PZ,PZ],PZ)
    assert repeated['positive_histories']==1
    similarities=[sp.Matrix([[1,2],[0,1]]),sp.Matrix([[1,sp.I],[1,1]]),sp.Matrix([[2,1-sp.I],[0,sp.Rational(1,3)]])]
    transformed=[corridor(programs[:3],rho,similarity=G) for G in similarities]
    for result in transformed:assert result['positive_histories']==8
    rotated=[corridor(programs[:2],rho,rotation=R) for R in rotations()]
    assert all(r['records']==rotated[0]['records'] for r in rotated)
    encoded=[2*I+sp.diag(sp.Rational(1,4),sp.Rational(3,4)),PZ,None,None,None,None]
    born=kernel_exact(encoded);smooth=kernel_exact(encoded,mode='smooth')
    get_plus=lambda atoms:next(p for p,A in atoms if A==PZ)
    assert get_plus(born)==sp.Rational(1,4)
    assert sp.simplify(get_plus(smooth)-1/(1+sp.exp(sp.Rational(8,3))))==0
    # Explicit endpoint derivatives of the exact encoded path.
    endpoints=[]
    for eps in [sp.Rational(1,10),sp.Rational(1,100),sp.Rational(1,1000)]:
        vals=[]
        for t in (-eps,sp.Integer(0),eps):
            rho_t=I-PZ+t*(2*PZ-I)
            atoms=kernel_exact([2*I+rho_t,PZ])
            plus=sum(p for p,A in atoms if A==PZ)
            vals.append(plus)
        assert vals==[0,0,eps]
        endpoints.append({'step':str(eps),'left_derivative':str((vals[1]-vals[0])/eps),'right_derivative':str((vals[2]-vals[1])/eps)})
    return {'direct_histories':base,'zero_branch_control':repeated,'nonunitary_similarity_cases':len(transformed),
      'proper_rotation_cases':len(rotated),'born_quarter':str(get_plus(born)),
      'smooth_alternative_quarter':str(get_plus(smooth)),'endpoint_derivatives':endpoints}

def h_float(x):return 0. if x<=0 else float(np.exp(-1/x))
def psi_float(x):
    a=h_float(1-x);b=h_float(x-.25)
    return a/(a+b)
def kernel_float(neighbors,mode='born'):
    present=[np.asarray(a,dtype=complex) for a in neighbors if a is not None]
    r=[psi_float(abs(np.trace(a)-5)**2) for a in present]
    s=[psi_float(abs(np.trace(a)-1)**2+abs(np.linalg.det(a))**2) for a in present]
    pairs=[(i,j,r[i]*s[j]) for i in range(len(present)) for j in range(len(present)) if i!=j]
    total=sum(w for _,_,w in pairs);b=(total-1)**2;z=total+b
    atoms=[(b/z,sum(present,np.zeros((2,2),dtype=complex)))]
    for i,j,w in pairs:
        x=float(np.trace((present[i]-2*np.eye(2))@present[j]).real)
        if mode=='born':p=float(np.clip(x,0,1))
        else:p=h_float(x)/(h_float(x)+h_float(1-x))
        atoms.extend([(w*p/z,present[j]),(w*(1-p)/z,np.eye(2)-present[j])])
    return atoms,total,z

def float_checks():
    rng=np.random.default_rng(300915)
    tests=[]
    for index in range(40):
        rand=lambda: rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        A=2.5*np.eye(2)+.12*rand();A2=2.5*np.eye(2)+.12*rand()
        B=np.diag([1.,0.])+.08*rand();B2=np.diag([1.,0.])+.08*rand()
        inputs=[A,B,A2,B2,rand(),None]
        atoms,S,Z=kernel_float(inputs)
        assert abs(sum(p for p,_ in atoms)-1)<3e-13 and min(p for p,_ in atoms)>=0 and Z>=.75-1e-13
        G=np.array([[1.,2.+.3j],[.2j,1.]],dtype=complex);Gi=np.linalg.inv(G)
        other,_,_=kernel_float([None if a is None else G@a@Gi for a in inputs])
        weight_error=max(abs(p-q) for (p,_),(q,_) in zip(atoms,other))
        atom_error=max(float(np.max(abs(G@a@Gi-b))) for (_,a),(_,b) in zip(atoms,other))
        assert weight_error<2e-11 and atom_error<2e-12
        perm=rng.permutation(len(inputs));shuffled,_,_=kernel_float([inputs[i] for i in perm])
        probe=rand()
        characteristic=lambda law:sum(p*np.exp(1j*np.trace(probe@a).real) for p,a in law)
        perm_error=abs(characteristic(atoms)-characteristic(shuffled))
        assert perm_error<3e-12
        direction=rand();discrepancies=[]
        for step in (1e-2,1e-3,1e-4,1e-5):
            moved=list(inputs);moved[0]=inputs[0]+step*direction
            nearby,_,_=kernel_float(moved)
            discrepancies.append(float(abs(characteristic(atoms)-characteristic(nearby))))
        assert discrepancies[-1]<2e-3
        tests.append({'S':S,'normalizer':Z,'similarity_weight_error':weight_error,
             'similarity_atom_error':atom_error,'permutation_error':float(perm_error),
             'continuity_differences':discrepancies})
    return {'off_code_cases':tests,'numerical_limits':'Floating finite probes, not interval proofs.'}

def main():
    result={'status':'personal_finite_checks_not_independent_review',
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'exact':exact_checks(),'off_code':float_checks()}
    dest=Path(__file__).with_name('BLOCK30_LOCAL_PROJECTIVE_CORRIDOR_CHECKS.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'positive_histories':result['exact']['direct_histories']['positive_histories'],
        'similarities':result['exact']['nonunitary_similarity_cases'],'rotations':result['exact']['proper_rotation_cases'],
        'off_code_cases':len(result['off_code']['off_code_cases']),'output':str(dest)}))
if __name__=='__main__':main()
