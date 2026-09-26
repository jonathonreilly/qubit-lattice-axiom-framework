#!/usr/bin/env python3
"""Exact gauge-dressed occupied-record circulation and a renewal certificate."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,itertools,json

HERE=Path(__file__).resolve().parent


def local_operator():
    signs=(1,1,-1,-1);count=0
    def gauss(q,b):
        # Twice the local Gauss generator; untouched outside links cancel.
        return tuple(signs[i]*(2*b[i]-1)-signs[i-1]*(2*b[i-1]-1)-2*q[i] for i in range(4))
    for q in itertools.product((-1,0,1),repeat=4):
        for b in itertools.product((0,1),repeat=4):
            if 0 in q or not all(2*b[i]-1==signs[i]*q[i] for i in range(4)):continue
            qout=(q[-1],)+q[:-1];bout=tuple(1-x for x in b)
            assert gauss(q,b)==gauss(qout,bout)
            assert Counter(q)==Counter(qout)
            # The adjoint transports qout_(i+1)=q_i along the reversed edge.
            assert all(2*bout[i]-1==-signs[i]*qout[(i+1)%4] for i in range(4))
            count+=1
    assert count==16
    return dict(local_basis_dimension=3**4*2**4,nonzero_forward_matrix_elements=count,
                all_Gauss_differences_exact_zero=True,each_record_species_count_preserved=True,
                reverse_circulation_is_adjoint=True,requires_all_four_sites_occupied=True)


def geometry(N):
    vertices=list(itertools.product(range(N),repeat=3));where={x:i for i,x in enumerate(vertices)}
    edges=[]
    def step(x,d):
        y=list(x);y[d]=(y[d]+1)%N;return tuple(y)
    for a,x in enumerate(vertices):
        for d in range(3):edges.append((a,where[step(x,d)],d))
    lookup={(a,d):e for e,(a,b,d) in enumerate(edges)};faces=[]
    for a,x in enumerate(vertices):
        for d,e in itertools.combinations(range(3),2):
            faces.append([(lookup[(a,d)],1),(lookup[(where[step(x,d)],e)],1),
                          (lookup[(where[step(x,e)],d)],-1),(lookup[(a,e)],-1)])
    return vertices,edges,faces


def divergence(bits,edges,V):
    q=[0]*V
    for bit,(a,b,d) in zip(bits,edges):q[a]+=bit;q[b]-=bit
    return tuple(q)


def hops(state,edges):
    bits,q=state
    for e,(a,b,d) in enumerate(edges):
        if (q[a]==0)==(q[b]==0):continue
        change=1-2*bits[e]
        if abs(q[a]+change)+abs(q[b]-change)!=1:continue
        newbits=list(bits);newbits[e]=1-newbits[e]
        newq=list(q);newq[a]+=change;newq[b]-=change
        yield e,(tuple(newbits),tuple(newq))


def cycles(state,edges,faces):
    bits,q=state
    for f,face in enumerate(faces):
        for sense in (1,-1):
            directed=face if sense==1 else [(e,-sgn) for e,sgn in reversed(face)]
            sites=[edges[e][0 if sgn==1 else 1] for e,sgn in directed]
            if any(q[a]==0 for a in sites):continue
            if not all(2*bits[e]-1==sgn*q[a] for (e,sgn),a in zip(directed,sites)):continue
            newbits=list(bits);newq=list(q)
            for e,sgn in directed:newbits[e]=1-newbits[e]
            for i,a in enumerate(sites):newq[sites[(i+1)%4]]=q[a]
            yield (f,sense,tuple(sites)),(tuple(newbits),tuple(newq))


def completion_path():
    source=HERE/'GAUGE_RECORD_EXTREME_FLUX_RESULTS.json';r=json.loads(source.read_text())['cases'][0]
    assert r['N']==4
    vertices,edges,faces=geometry(4);bits=[1]*len(edges)
    for e in r['final_negative_flux_edge_indices']:bits[e]=0
    initial=(tuple(bits),tuple(r['final_charge']));assert divergence(initial[0],edges,64)==initial[1]
    assert not list(hops(initial,edges))
    cycle_list=list(cycles(initial,edges,faces));assert len(cycle_list)==68
    key,after_cycle=next((key,state) for key,state in cycle_list if key[:2]==(4,-1))
    after_hop1=dict(hops(after_cycle,edges))[2]
    adjacent=dict(hops(after_hop1,edges))[52]
    holes=[i for i,q in enumerate(adjacent[1]) if q==0]
    assert [vertices[i] for i in holes]==[(0,0,1),(1,0,1)]
    birth_edge=3;a,b,d=edges[birth_edge];assert set((a,b))==set(holes)
    finalbits=list(adjacent[0]);change=1-2*finalbits[birth_edge];finalbits[birth_edge]=1-finalbits[birth_edge]
    finalq=list(adjacent[1]);finalq[a]+=change;finalq[b]-=change
    final=(tuple(finalbits),tuple(finalq))
    states=[initial,after_cycle,after_hop1,adjacent,final]
    for state in states:assert divergence(state[0],edges,64)==state[1]
    assert [sum(q!=0 for q in st[1]) for st in states]==[62,62,62,62,64]
    assert Counter(final[1])=={1:32,-1:32}
    # Exact coefficient of the shortest Hamiltonian path to this adjacent-hole state.
    # Initial ordinary hops and pure plaquettes vanish; two ordinary hops are
    # indispensable to bring the holes from distance three to distance one.
    paths=[]
    for ckey,st1 in cycle_list:
        for e1,st2 in hops(st1,edges):
            for e2,st3 in hops(st2,edges):
                if st3==adjacent:paths.append(dict(cycle=ckey[:2],hop_edges=[e1,e2]))
    assert len(paths)==2
    # Track distinguishable internal payloads without adding them to the qutrit
    # certificate: each displayed operation is a permutation of whole records.
    payload={i:i for i,q in enumerate(initial[1]) if q}
    old=dict(payload);sites=key[2]
    for i,a0 in enumerate(sites):payload[sites[(i+1)%4]]=old[a0]
    for e in (2,52):
        a0,b0,d=edges[e]
        source_site,target=(a0,b0) if a0 in payload else (b0,a0)
        assert target not in payload;payload[target]=payload.pop(source_site)
    assert set(payload.values())==set(old.values()) and set(payload)==set(range(64))-set(holes)
    return dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),N=4,
                initial_vacancies=[[0,0,0],[1,1,1]],collective_cycle=dict(face=4,sense=-1,sites=[vertices[a] for a in sites]),
                ordinary_hop_edges=[2,52],adjacent_vacancies=[vertices[h] for h in holes],birth_edge=birth_edge,
                final_record_count=64,final_positive_count=32,final_negative_count=32,
                complete_path_Gauss_law_exact=True,all_existing_payloads_permuted_bijectively=True,
                enabled_initial_record_cycles=len(cycle_list),shortest_H_cubed_paths=paths,
                H_cubed_matrix_element='2 g kappa^2',
                earliest_no_jump_amplitude='i g kappa^2 t^3/3 + O(t^4)',
                chosen_full_birth_probability_density='beta g^2 kappa^4 t^6/9 + O(t^7)',
                scope='A specific added four-record interaction releases this exact trap with positive quantum completion probability. This does not prove almost-sure filling from every state.')


def main():
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             local_operator=local_operator(),completion=completion_path())
    encoded=json.dumps(out,indent=2)+'\n';(HERE/'GAUGE_COLLECTIVE_RECORD_CYCLE_RESULTS.json').write_text(encoded);print(encoded,end='')


if __name__=='__main__':main()
