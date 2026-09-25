#!/usr/bin/env python3
"""Own exact two-occupied-B flat-field reduction and finite Perron controls.

No parent or author program is imported. A simple torus uses unique nearest
neighbors (thus L2 is the cube of degree3). All matrix entries and final
Collatz bounds are exact integers/rationals; floating eigensolvers only propose
the positive vector used in the rational certificate.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations,product
from pathlib import Path
import hashlib,json,time
import numpy as np
from scipy.sparse import csr_matrix

HERE=Path(__file__).resolve().parent


def geometry(side):
    vertices=list(product(range(side),repeat=3))
    A=[v for v in vertices if sum(v)%2==0];B=[v for v in vertices if sum(v)%2==1]
    def near(v):
        return sorted({tuple((x+(s if k==mu else 0))%side for k,x in enumerate(v))
                       for mu in range(3) for s in (-1,1)})
    adjacency={v:near(v) for v in vertices}
    pairs=sorted({tuple(sorted((u,v))) for b in B for u,v in combinations(adjacency[b],2)})
    return A,B,adjacency,pairs


def run(side):
    A,B,near,Apairs=geometry(side);n=len(B);index={b:j for j,b in enumerate(B)}
    Bpairs=list(combinations(range(n),2));pair_index={p:j for j,p in enumerate(Bpairs)}
    shape=(len(Apairs),len(Bpairs));ri=[];ci=[];values=[]
    square_sum=np.zeros((n,n),dtype=np.int64)
    q0=0;shared_total=0;disjoint_total=0;r_count=Counter()
    for row,(u,v) in enumerate(Apairs):
        multiplicity=Counter(tuple(sorted((index[b],index[d]))) for b in near[u] for d in near[v] if b!=d)
        support=sorted({j for pair in multiplicity for j in pair});loc={j:k for k,j in enumerate(support)}
        local=np.zeros((len(support),len(support)),dtype=np.int64)
        for (i,j),m in multiplicity.items():
            ri.append(row);ci.append(pair_index[i,j]);values.append(m)
            local[loc[i],loc[j]]=local[loc[j],loc[i]]=m
        local_square=local@local
        square_sum[np.ix_(support,support)]+=local_square
        vacuum=sum(m*m for m in multiplicity.values());total=sum(multiplicity.values())
        shared=int(np.sum(np.sum(local,axis=1)**2))-2*vacuum
        disjoint=total*total-vacuum-shared
        q0+=vacuum;shared_total+=shared;disjoint_total+=disjoint
        r_count[len(set(near[u])&set(near[v]))]+=1
    W=csr_matrix((np.array(values,dtype=np.int64),(ri,ci)),shape=shape)
    s=np.diag(square_sum).copy();off=square_sum.copy();np.fill_diagonal(off,0)
    assert len(set(map(int,s)))==1
    assert len(set(map(int,off.sum(axis=1))))==1
    beta=int(off.sum(axis=1)[0]-s[0])

    def matrix_row(pair_number):
        x,y=Bpairs[pair_number];row=defaultdict(int)
        row[pair_number]=q0-int(s[x])-int(s[y])
        for source,spectator in ((x,y),(y,x)):
            for target in np.flatnonzero(off[source]):
                target=int(target)
                if target!=spectator:
                    row[pair_index[tuple(sorted((target,spectator)))]]+=int(off[source,target])
        gram=(W[:,pair_number].T@W).tocoo()
        for dest,value in zip(gram.col,gram.data):
            dest=int(dest);value=int(value)
            intersection=len(set(Bpairs[dest])&{x,y})
            row[dest]+= -value if intersection==1 else value
        row={j:v for j,v in row.items() if v}
        assert all(value>=0 for value in row.values())
        return row

    def orbit(pair):
        a,b=(B[j] for j in pair)
        return tuple(sorted(min((x-y)%side,(y-x)%side) for x,y in zip(a,b)))
    labels=sorted({orbit(p) for p in Bpairs});which={label:j for j,label in enumerate(labels)}
    orbit_index=[which[orbit(p)] for p in Bpairs]
    bins=[[j for j,o in enumerate(orbit_index) if o==k] for k in range(len(labels))]
    sizes=[len(group) for group in bins]
    quotient=[];saved=[];row_checks=0
    for k,group in enumerate(bins):
        first=matrix_row(group[0]);coarse=[0]*len(labels)
        for dest,value in first.items():coarse[orbit_index[dest]]+=value
        quotient.append(coarse)
        # Distinct translated/oriented configurations test the exact orbit reduction.
        for j in sorted(set(group[:3]+group[-2:])):
            check=[0]*len(labels)
            for dest,value in matrix_row(j).items():check[orbit_index[dest]]+=value
            assert check==coarse;row_checks+=1
        saved.append(dict(pair_number=group[0],occupied_B=[B[j] for j in Bpairs[group[0]]],
            entries=[dict(occupied_B=[B[j] for j in Bpairs[dest]],value=value) for dest,value in sorted(first.items())]))
    assert all(sizes[i]*quotient[i][j]==sizes[j]*quotient[j][i] for i in range(len(labels)) for j in range(len(labels)))
    offset=[[value-(q0 if i==j else 0) for j,value in enumerate(row)] for i,row in enumerate(quotient)]
    sym=np.array(offset,dtype=float)*np.sqrt(np.array(sizes)[:,None]/np.array(sizes)[None,:])
    assert np.max(abs(sym-sym.T))<1e-10
    eig,vectors=np.linalg.eigh(sym);vector=vectors[:,-1]
    if vector.sum()<0:vector=-vector
    vector=vector/np.sqrt(sizes)
    assert np.min(vector)>0
    vector=vector/np.max(vector)
    proposal=[max(1,int(round(x*10**12))) for x in vector]
    ratios=[Fraction(sum(a*w for a,w in zip(row,proposal)),proposal[i]) for i,row in enumerate(offset)]
    lower,upper=min(ratios),max(ratios)
    # Exact uniform two-particle Rayleigh quotient, not an eigensolver assertion.
    average=Fraction(sum(sizes[i]*sum(quotient[i]) for i in range(len(labels))),sum(sizes))
    formula=Fraction(q0*(n-2)*(n-3)+2*shared_total*(n-3)+2*disjoint_total,n*(n-1))
    assert average==formula
    if side>=6:
        assert q0==321*n and beta==3024
        assert average-q0==Fraction(6048)-Fraction(774,n-1)
    elif side==4:
        assert q0==270*n and beta==2580
        assert average-q0==Fraction(5160)-Fraction(1380,n-1)
    else:
        assert side==2 and q0==54 and lower==upper==-5
    return dict(L=side,A_count=len(A),B_count=n,degree=len(near[A[0]]),overlapping_A_pairs=len(Apairs),
        common_neighbor_inventory={str(k):v for k,v in sorted(r_count.items())},
        magnetic_Q0=q0,physical_one_pair_matter_dimension=(n+2)*len(Bpairs),
        occupation_dimension=len(Bpairs),pair_creation_matrix_nonzeros=W.nnz,
        one_B_diagonal_loss=int(s[0]),one_B_offdiagonal_row_sum=int(off.sum(axis=1)[0]),one_B_row_increment=beta,
        total_ordered_shared_pair_weight=shared_total,total_ordered_disjoint_pair_weight=disjoint_total,
        orbit_labels=labels,orbit_sizes=sizes,orbit_quotient_offset_from_Q0=offset,
        exact_detailed_balance=True,translated_oriented_rows_checked=row_checks,
        uniform_trial_increment=str(average-q0),minimum_row_increment=min(map(sum,offset)),
        maximum_row_increment=max(map(sum,offset)),
        proposed_positive_integer_vector=proposal,
        exact_Perron_increment_lower=str(lower),exact_Perron_increment_upper=str(upper),
        lower_decimal=float(lower),upper_decimal=float(upper),
        floating_eigenvalue_diagnostic=float(eig[-1]),
        relative_ground_energy_coefficient_in_1_over_tau_g2_interval=[float(-upper/2),float(-lower/2)],
        saved_occupation_rows=saved)


if __name__=='__main__':
    tic=time.perf_counter();rows=[run(L) for L in (2,4,6,8)]
    data=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        rows=rows,elapsed_seconds=time.perf_counter()-tic,
        no_field_truncation=True,no_author_code=True,
        proof_limit='Flat magnetic coefficient and exact rational finite-matrix checks; no finite-g spectrum or dynamics simulation')
    raw=json.dumps(data,indent=2)+'\n'
    with (HERE/'OCCUPATION_SPECTRUM_RESULTS.json').open('x') as output:output.write(raw)
    print(json.dumps({k:([{a:b for a,b in row.items() if a!='saved_occupation_rows'} for row in v] if k=='rows' else v) for k,v in data.items()},indent=2))
