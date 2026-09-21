#!/usr/bin/env python3
"""Author path-load, contraction, and endpoint-word controls."""
from pathlib import Path
from collections import Counter
import datetime, hashlib, itertools, json, math
import numpy as np
import dimer_routed_transport_check as base

HERE=Path(__file__).resolve().parent

def path(x,y,N):
    current=list(x);out=[tuple(current)]
    for axis in range(3):
        distance=(y[axis]-current[axis])%N
        direction=1 if distance<=N//2 else -1
        steps=distance if direction==1 else N-distance
        for _ in range(steps):
            current[axis]=(current[axis]+direction)%N
            out.append(tuple(current))
    assert out[-1]==tuple(y) and len(out)-1<=3*N//2
    return out

def physical_loads():
    rows=[]
    for N in (4,6):
        sites=list(itertools.product(range(N),repeat=3));load=Counter()
        for x in sites:
            for y in sites:
                p=path(x,y,N)
                edges=[tuple(sorted((a,b))) for a,b in zip(p[:-1],p[1:])]
                assert len(set(edges))==len(edges)
                load.update(edges)
        assert len(load)==3*N**3
        assert set(load.values())=={N**4//4}
        rows.append(dict(N=N,ordered_pairs=N**6,physical_edges=len(load),
                         exact_load_per_edge=N**4//4))
    return rows

def contracted_loads():
    rows=[]
    for N in (8,10):
        xyz,index,nb=base.make_lattice(N);K=N**3//2
        black=np.flatnonzero(xyz.sum(axis=1)%2==0)
        coord=[tuple(map(int,xyz[x])) for x in black]
        lookup={tuple(map(int,x)):i for i,x in enumerate(xyz)}
        for kind in ('winding','columnar','irregular'):
            M,flips=base.matching(N,8*N**3 if kind=='irregular' else 0,91700+N,
                                  winding=kind=='winding')
            owner=np.full(N**3,-1,dtype=int);owner[black]=np.arange(K);owner[M[black]]=np.arange(K)
            multiplicity=Counter()
            for x in range(N**3):
                for axis in range(3):
                    a,b=int(owner[x]),int(owner[nb[2*axis,x]])
                    if a!=b:multiplicity[tuple(sorted((a,b)))]+=1
            assert max(multiplicity.values())<=2
            path_load=Counter();word_load=Counter();erased=0;max_length=0
            for a,b in itertools.combinations(range(K),2):
                physical=path(coord[a],coord[b],N)
                projection=[int(owner[lookup[x]]) for x in physical]
                simple=[];position={}
                for z in projection:
                    if z in position:
                        loc=position[z]
                        for removed in simple[loc+1:]:del position[removed]
                        erased+=len(simple)-loc-1
                        simple=simple[:loc+1]
                    else:position[z]=len(simple);simple.append(z)
                assert simple[0]==a and simple[-1]==b and len(set(simple))==len(simple)
                length=len(simple)-1;max_length=max(max_length,length)
                assert length<=3*N//2
                edges=[tuple(sorted((x,y))) for x,y in zip(simple[:-1],simple[1:])]
                original={tuple(sorted((x,y))) for x,y in zip(projection[:-1],projection[1:]) if x!=y}
                assert set(edges)<=original<=set(multiplicity)
                word=edges+edges[-2::-1]
                assert len(word)==2*length-1<=3*N-1
                tokens={z:z for z in simple}
                for x,y in word:tokens[x],tokens[y]=tokens[y],tokens[x]
                assert tokens[a]==b and tokens[b]==a
                assert all(tokens[z]==z for z in simple[1:-1])
                path_load.update(edges);word_load.update(word)
            assert max(path_load.values())<=N**4//2
            assert max(word_load.values())<=N**4
            lap=np.zeros((K,K))
            for a,b in multiplicity:
                lap[a,a]+=1;lap[b,b]+=1;lap[a,b]-=1;lap[b,a]-=1
            gap=float(np.linalg.eigvalsh(lap)[1])
            lower=1/(4*N*(3*N-1))
            assert gap>=lower-1e-12
            rows.append(dict(N=N,kind=kind,K=K,fixture_flips=flips,unordered_reference_pairs=math.comb(K,2),
                             largest_physical_edge_multiplicity=max(multiplicity.values()),
                             maximum_contracted_path_length=max_length,erased_projected_vertices=erased,
                             maximum_reference_path_load=max(path_load.values()),path_load_bound=N**4//2,
                             maximum_word_edge_load=max(word_load.values()),word_load_bound=N**4,
                             all_immutable_endpoint_words_exact=True,
                             numerical_one_exceptional_color_gap=gap,
                             proven_unit_rate_H_gap_lower_bound=lower))
            print(json.dumps(rows[-1]),flush=True)
    return rows

def main():
    out=HERE/'dimer_routed_diffusive_gap_checks';out.mkdir(exist_ok=False)
    physical=physical_loads();print('exact all-vertex physical loads passed',flush=True)
    contracted=contracted_loads()
    schedule=[]
    for N in (8,16,32,64,128,256):
        K=N**3//2;k0=1.1;gap=k0/(8*N*(3*N-1));epsilon=N**-4
        waiting=(K*math.log(14)/2+math.log(1/(2*epsilon)))/gap
        old_gap=k0/(4*(3*N-1)*(K-1))
        assert gap>=old_gap
        assert abs(gap/old_gap-(K-1)/(2*N))<1e-11
        schedule.append(dict(N=N,K=K,gap_lower_bound=gap,epsilon=epsilon,
                             sufficient_waiting_time=waiting,improvement_factor=(K-1)/(2*N)))
    result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in (
                    Path(__file__).name,'DIMER_ROUTED_DIFFUSIVE_GAP_COMPARISON.md',
                    'dimer_routed_transport_check.py','DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md')},
                physical_loads=physical,contracted_loads=contracted,schedule=schedule,
                scope='Exact finite combinatorial controls and numerical one-exceptional-color spectra; all-count-sector and all-volume bounds are proved in the note, not inferred from these samples.')
    (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
