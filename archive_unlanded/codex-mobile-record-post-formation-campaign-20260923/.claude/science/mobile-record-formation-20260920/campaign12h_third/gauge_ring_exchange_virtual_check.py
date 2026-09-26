#!/usr/bin/env python3
"""Exact virtual-path coefficient in an explicitly enlarged matter space.

Four distinguishable bosonic payload species, one particle each. Multiple
records may temporarily occupy a vertex with energy U*n(n-1)/2. This is NOT
the exact one-record-per-site microscopic premise of the original model.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from collections import Counter,defaultdict
import itertools,json,hashlib

HERE=Path(__file__).resolve().parent
CHARGES=(1,1,1,-1)
SIGNS=(1,1,-1,-1)


def charge_at(positions):
    q=[0]*4
    for a,x in enumerate(positions):q[x]+=CHARGES[a]
    return tuple(q)


def gauss(state):
    positions,bits=state;q=charge_at(positions)
    return tuple(SIGNS[i]*(2*bits[i]-1)-SIGNS[i-1]*(2*bits[i-1]-1)-2*q[i] for i in range(4))


def energy(state):
    counts=Counter(state[0]);return sum(n*(n-1)//2 for n in counts.values())


def neighbours(state):
    positions,bits=state
    for a,x in enumerate(positions):
        for direction in (1,-1):
            y=(x+direction)%4;e=x if direction==1 else y
            delta=-direction*SIGNS[e]*CHARGES[a]
            if (delta==1 and bits[e]!=0) or (delta==-1 and bits[e]!=1):continue
            p=list(positions);p[a]=y;b=list(bits);b[e]=1-b[e]
            yield (tuple(p),tuple(b))


def main():
    initial=((0,1,2,3),(1,1,0,1))
    target=((1,2,3,0),(0,0,1,0))
    sector=gauss(initial);assert gauss(target)==sector
    basis=[(p,b) for p in itertools.product(range(4),repeat=4) for b in itertools.product((0,1),repeat=4) if gauss((p,b))==sector]
    basis_set=set(basis);P=[state for state in basis if energy(state)==0];Pset=set(P)
    degrees=[]
    for state in basis:
        nn=list(neighbours(state));degrees.append(len(nn))
        for other in nn:
            assert other in basis_set and gauss(other)==sector
            assert state in set(neighbours(other))
    # Resolvent paths through Q at each intermediate stage. Units U=1.
    frontier={initial:Fraction(1)};selected=[]
    for step in range(1,5):
        next_frontier=defaultdict(Fraction)
        for state,value in frontier.items():
            for other in neighbours(state):
                if step<4:
                    if other in Pset:continue
                    next_frontier[other]+=value/Fraction(energy(other))
                elif other in Pset:next_frontier[other]+=value
        frontier=next_frontier
        selected.append(str(frontier.get(target,Fraction(0))))
    assert frontier[target]==20
    # Direct independently enumerated edge-order histories.
    histories=Counter()
    for order in itertools.permutations(range(4)):
        st=initial;costs=[]
        for step,a in enumerate(order):
            p=list(st[0]);p[a]=(a+1)%4;b=list(st[1]);b[a]=1-b[a]
            nxt=(tuple(p),tuple(b));assert nxt in set(neighbours(st));st=nxt
            if step<3:costs.append(energy(st))
        assert st==target;histories[tuple(costs)]+=1
    assert histories=={(1,1,1):16,(1,2,1):8}
    # Folded fourth-order paths returning to P after two steps vanish for
    # this full labeled four-cycle; verify without a permutation argument.
    midP=Counter()
    for st1 in neighbours(initial):
        for st2 in neighbours(st1):
            if st2 in Pset:midP[st2]+=1
    folded_paths=0
    for st2,multiplicity in midP.items():
        for st3 in neighbours(st2):
            for st4 in neighbours(st3):
                if st4==target:folded_paths+=multiplicity
    assert folded_paths==0
    assert not any(st in Pset for st in neighbours(initial))
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                full_labeled_basis_dimension=4**4*2**4,selected_Gauss_sector_dimension=len(basis),
                low_energy_one_per_site_dimension=len(P),twice_Gauss_generator=sector,
                maximal_hopping_degree=max(degrees),all_hops_Gauss_covariant_and_reversible=True,
                intermediate_Q_weighted_target_amplitudes_by_step=selected,
                exact_fourth_order_Feshbach_entry='-20*t^4/U^3',
                energy_history_counts={','.join(map(str,k)):v for k,v in histories.items()},
                folded_two_plus_two_hop_paths_to_target=folded_paths,
                all_existing_species_counts_conserved=True,
                microscopic_limitation='Virtual multiple occupancy is explicitly allowed. The result supplies neither a native one-record-per-site Hamiltonian nor an effective irreversible birth instrument.',
                known_mechanism='Fourth-order ring exchange is established Hubbard-model physics; this calculation checks its charge/field dressing and premise cost in the stated finite model.')
    encoded=json.dumps(result,indent=2)+'\n';(HERE/'GAUGE_RING_EXCHANGE_VIRTUAL_RESULTS.json').write_text(encoded);print(encoded,end='')


if __name__=='__main__':main()
