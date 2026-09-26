#!/usr/bin/env python3
"""Integer stabilizer twirls and a modular exact rank certificate."""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,itertools,json,math
import numpy as np
P=Path(__file__).resolve().parent;PRIME=65537
assert all(PRIME%d for d in range(2,math.isqrt(PRIME)+1))

def rank_mod(matrix):
    a=[[int(v)%PRIME for v in rr] for rr in matrix];ids=list(range(len(a)));r=0;chosen=[]
    for c in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r];ids[r],ids[piv]=ids[piv],ids[r];chosen.append(ids[r])
        inv=pow(a[r][c],-1,PRIME);a[r]=[v*inv%PRIME for v in a[r]]
        for i in range(r+1,len(a)):
            mul=a[i][c]
            if mul:a[i]=[(v-mul*w)%PRIME for v,w in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r,chosen

def det_mod(matrix):
    a=[[int(v)%PRIME for v in rr] for rr in matrix];det=1
    for c in range(len(a)):
        p=next((i for i in range(c,len(a)) if a[i][c]),None)
        if p is None:return 0
        if p!=c:a[c],a[p]=a[p],a[c];det=-det
        pivot=a[c][c];det=det*pivot%PRIME;inv=pow(pivot,-1,PRIME)
        for i in range(c+1,len(a)):
            mul=a[i][c]*inv%PRIME
            for j in range(c,len(a)):a[i][j]=(a[i][j]-mul*a[c][j])%PRIME
    return det%PRIME

def main():
    group=[]
    for perm in itertools.permutations(range(3)):
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in itertools.product((-1,1),repeat=3):
            if parity*math.prod(signs)!=1:continue
            R=np.zeros((3,3),dtype=np.int64)
            for i in range(3):R[i,perm[i]]=signs[i]
            U=np.zeros((4,4),dtype=np.int64);U[0,0]=1;U[1:,1:]=R;V=np.kron(U,U)
            assert np.array_equal(V.T@V,np.eye(16,dtype=int));group.append((R,V,parity))
    a0=np.array([1,0,0]);b0=np.ones(3,dtype=int)
    HA=[V for R,V,a in group if np.array_equal(R@a0,a0)];HB=[V for R,V,a in group if np.array_equal(R@b0,b0)]
    assert (len(HA),len(HB))==(4,3)
    va=np.array([(7*i*i+3*i+5)%17-8 for i in range(16)],dtype=np.int64)
    vb=np.array([(11*i**3+4*i+1)%19-9 for i in range(16)],dtype=np.int64)
    SA=np.eye(16,dtype=np.int64)+sum((np.outer(V@va,V@va) for V in HA),np.zeros((16,16),dtype=np.int64))
    SB=np.eye(16,dtype=np.int64)+sum((np.outer(V@vb,V@vb) for V in HB),np.zeros((16,16),dtype=np.int64))
    for H,S in [(HA,SA),(HB,SB)]:assert all(np.array_equal(V@S@V.T,S) for V in H)
    assert int(np.trace(SA))==16+4*int(va@va) and int(np.trace(SB))==16+3*int(vb@vb)
    labels=[(0,tuple(z*int(i==j) for j in range(3))) for i in range(3) for z in (1,-1)]+[(1,b) for b in itertools.product((-1,1),repeat=3)]
    matrices=[];traces=[];coset_counts=[]
    for orbit,color in labels:
        start=a0 if orbit==0 else b0;S=SA if orbit==0 else SB
        candidates=[V@S@V.T for R,V,a in group if tuple(R@start)==color]
        assert candidates and all(np.array_equal(candidates[0],Q) for Q in candidates)
        matrices.append(candidates[0]);traces.append(int(np.trace(S)));coset_counts.append(len(candidates))
    checks=0
    for R,V,a in group:
        for i,(orbit,color) in enumerate(labels):
            target=labels.index((orbit,tuple(R@np.array(color))))
            assert traces[i]==traces[target] and np.array_equal(V@matrices[i]@V.T,matrices[target]);checks+=1
    columns=np.array([M.ravel() for M in matrices],dtype=np.int64).T
    rank,selected=rank_mod(columns);assert rank==14 and len(selected)==14
    minor=columns[selected,:];det=det_mod(minor);assert det!=0
    normalized=[[int(columns[i,j])*pow(traces[j],-1,PRIME)%PRIME for j in range(14)] for i in range(256)]
    differences=[[(rr[j]-rr[0])%PRIME for j in range(1,14)] for rr in normalized]
    affine,_=rank_mod(differences);assert affine==13
    T=sum((math.prod(color)*matrices[i] for i,(orbit,color) in enumerate(labels) if orbit==1),np.zeros((16,16),dtype=np.int64))
    assert np.any(T)
    assert all(np.array_equal(V@T@V.T,a*T) for R,V,a in group)
    hilbert=F(sum(a*int(np.trace(V)) for R,V,a in group),24)
    operator=F(sum(a*int(np.trace(V))**2 for R,V,a in group),24)
    assert hilbert==0 and operator==7
    overlap=min(F(int(np.trace(matrices[i]@matrices[j])),traces[i]*traces[j]) for i in range(14) for j in range(i))
    assert overlap>0
    out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'boundary':'Independent construction and modular rank before author checker/results.',
         'proper_rotations':24,'stabilizer_sizes':[len(HA),len(HB)],'integer_seed_A':va.tolist(),'integer_seed_B':vb.tolist(),
         'traces':[int(np.trace(SA)),int(np.trace(SB))],'strict_eigenvalue_lower_bounds':[str(F(1,int(np.trace(SA)))),str(F(1,int(np.trace(SB))))],
         'coset_representatives_per_color':coset_counts,'exact_covariance_relations':checks,
         'prime':PRIME,'prime_trial_division_verified':True,'modular_column_rank':rank,'affine_rank_mod_prime':affine,
         'selected_zero_based_operator_rows':selected,'integer_minor_determinant_mod_prime':det,
         'selected_integer_minor':minor.tolist(),'normalization_traces_nonzero_mod_prime':all(t%PRIME for t in traces),
         'alternating_hilbert_multiplicity':str(hilbert),'alternating_operator_multiplicity':str(operator),
         'cubic_operator_nonzero_entries':int(np.count_nonzero(T)),'cubic_density_Frobenius_squared':str(F(int(np.sum(T*T)),int(np.trace(SB))**2)),
         'minimum_distinct_pair_Hilbert_Schmidt_overlap':str(overlap),
         'positivity_proof':'Each unnormalized state is I plus a sum of integer vector outer products, conjugated by an orthogonal matrix. It dominates I exactly; division by its positive trace gives the stated lower bound.',
         'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    with (P/'INDEPENDENT_RESULTS.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('integer covariance, strict positivity, modular rank 14/affine 13, and cubic character verified')
if __name__=='__main__':main()
