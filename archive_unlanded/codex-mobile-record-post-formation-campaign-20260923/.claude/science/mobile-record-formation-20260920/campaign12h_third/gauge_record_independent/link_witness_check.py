#!/usr/bin/env python3
"""Exact spin-half-link witness, local identities and coherent route counting.

Only the neutral INPUT_WITNESS.json is read. Basis states are integer tuples
of matter charges and a bit mask of negative links. Each legal matrix element
is assembled from the supplied local operators, including K and K-dagger
separately. This is not a classical path-probability approximation.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from collections import defaultdict
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
INPUT = HERE / 'INPUT_WITNESS.json'
DATA = json.loads(INPUT.read_text())
N = DATA['N']
XYZ = list(product(range(N),repeat=3))
INDEX = {x:i for i,x in enumerate(XYZ)}


def shift(x,axis,sign=1):
    y=list(x);y[axis]=(y[axis]+sign)%N;return tuple(y)


EDGES = [(i,INDEX[shift(x,axis)]) for i,x in enumerate(XYZ) for axis in range(3)]
LOOKUP = {e:(j,1) for j,e in enumerate(EDGES)}
LOOKUP.update({(y,x):(j,-1) for j,(x,y) in enumerate(EDGES)})
FACES=[]
for x in XYZ:
    for i,j in combinations(range(3),2):
        verts=[x,shift(x,i),shift(shift(x,i),j),shift(x,j)]
        FACES.append(tuple(INDEX[v] for v in verts))
assert len(FACES)==192
assert len({frozenset(LOOKUP[(f[i],f[(i+1)%4])][0] for i in range(4)) for f in FACES})==192


def flux_divergence(mask):
    # The all-positive field has zero periodic divergence. Each negative
    # link changes it by -1 at the tail and +1 at the head.
    out=[0]*len(XYZ)
    for e,(x,y) in enumerate(EDGES):
        if (mask>>e)&1:out[x]-=1;out[y]+=1
    return tuple(out)


def e2(mask,e):return 1-2*((mask>>e)&1)


def physical(state):
    q,mask=state
    return all(x in (-1,0,1) for x in q) and q==flux_divergence(mask)


def matching_state(state):
    q,mask=state
    used=[]
    for e,(x,y) in enumerate(EDGES):
        if (mask>>e)&1:used.extend((x,y))
    return len(used)==len(set(used)) and set(used)=={i for i,a in enumerate(q) if a}


def hop(state,source,dest):
    q,mask=state
    if not q[source] or q[dest]:return None
    e,sign=LOOKUP[(source,dest)]
    delta=-sign*q[source]
    if e2(mask,e)!=-delta:return None
    new=list(q);new[dest]=new[source];new[source]=0
    return tuple(new),mask^(1<<e)


def birth(state,e):
    q,mask=state;x,y=EDGES[e]
    if q[x] or q[y]:return None
    delta=-e2(mask,e)
    new=list(q);new[x]=delta;new[y]=-delta
    return (tuple(new),mask^(1<<e)),('plus' if delta==1 else 'minus')


def field_loop(state,verts,orientation):
    q,mask=state;out=mask
    for i,x in enumerate(verts):
        e,sign=LOOKUP[(x,verts[(i+1)%len(verts)])]
        delta=orientation*sign
        if e2(out,e)!=-delta:return None
        out^=1<<e
    return q,out


def record_cycle(state,verts,orientation):
    q,mask=state
    if any(q[x]==0 for x in verts):return None
    new=list(q);out=mask
    for i,x in enumerate(verts):
        e,sign=LOOKUP[(x,verts[(i+1)%4])]
        if orientation==1:
            delta=-sign*q[x]
            new[x]=q[verts[(i-1)%4]]
        else:
            delta=sign*q[verts[(i+1)%4]]
            new[x]=q[verts[(i+1)%4]]
        if e2(out,e)!=-delta:return None
        out^=1<<e
    return tuple(new),out


def hopping_channels(state):
    q,mask=state;rows=[]
    for e,(x,y) in enumerate(EDGES):
        for src,dst in [(x,y),(y,x)]:
            out=hop(state,src,dst)
            if out is not None:
                rows.append((out,{'kind':'hop','edge':e,'source':src,'dest':dst}))
    return rows


def field_channels(state):
    rows=[]
    for f,verts in enumerate(FACES):
        for direction in (-1,1):
            out=field_loop(state,verts,direction)
            if out is not None:rows.append((out,{'kind':'field_plaquette','face':f,'direction':direction}))
    return rows


def hamiltonian_channels(state):
    rows=hopping_channels(state)+field_channels(state)
    for f,verts in enumerate(FACES):
        for direction in (-1,1):
            out=record_cycle(state,verts,direction)
            if out is not None:
                rows.append((out,{'kind':'record_cycle','face':f,'direction':direction}))
    return rows


def state_summary(state):
    q,mask=state
    return {'holes':[XYZ[i] for i,a in enumerate(q) if a==0],
            'record_count':sum(a!=0 for a in q),'negative_link_count':mask.bit_count(),
            'matter_charges':list(q),'negative_links':[e for e in range(len(EDGES)) if (mask>>e)&1]}


def local_controls():
    # Exhaust all local matter/link basis inputs. For a directed link, a
    # charge q moving forward changes E by -q. A birth changes charges by
    # (+1,-1) with U, or (-1,+1) with U-dagger.
    counts=defaultdict(int)
    for a,b,E in product((-1,0,1),(-1,0,1),(-1,1)):
        for sign in (-1,1):
            src,dst=(a,b) if sign==1 else (b,a)
            if src and dst==0:
                delta=-sign*src
                if E==-delta:
                    qa,qb=(0,src) if sign==1 else (src,0)
                    assert qa-a==delta and qb-b==-delta
                    assert abs(qa)+abs(qb)==abs(a)+abs(b)
                    counts['legal_directed_hops']+=1
        allowed_births=0
        if a==b==0:
            for charge,delta in [(1,1),(-1,-1)]:
                if E==-delta:
                    assert charge==delta and -charge==-delta
                    allowed_births+=1
        assert allowed_births==int(a==b==0)
        counts['local_basis_inputs']+=1
    # All four-site fully occupied matter/link inputs on one oriented face.
    signs=(1,1,-1,-1)
    face_maps={}
    for charges in product((-1,1),repeat=4):
        for fields in product((-1,1),repeat=4):
            if fields!=tuple(signs[i]*charges[i] for i in range(4)):continue
            outq=charges[-1:]+charges[:-1]
            outE=tuple(-x for x in fields)
            deltaE=[(outE[i]-fields[i])//2 for i in range(4)]
            for i in range(4):
                divchange=signs[i]*deltaE[i]-signs[(i-1)%4]*deltaE[(i-1)%4]
                assert divchange==outq[i]-charges[i]
            assert sorted(outq)==sorted(charges)
            face_maps[(charges,fields)]=(outq,outE)
    assert len(face_maps)==16 and len(set(face_maps.values()))==16
    counts['legal_occupied_cycle_inputs']=len(face_maps)
    counts['occupied_cycle_Gauss_and_content_checks']=16
    return dict(counts)


def main():
    started=time.monotonic()
    initial=(tuple(DATA['matter_charges']),sum(1<<e for e in DATA['negative_flux_edge_indices']))
    assert physical(initial) and matching_state(initial)
    assert initial[1].bit_count()==31
    assert {XYZ[i] for i,q in enumerate(initial[0]) if q==0}=={(0,0,0),(1,1,1)}
    assert not hopping_channels(initial)
    assert not field_channels(initial)
    assert not [e for e in range(len(EDGES)) if birth(initial,e)]
    # Full quantum birth support from the empty all-positive field: a sequence
    # of the distinct negative matching edges creates the witness exactly.
    state=((0,)*64,0)
    birth_word=[]
    for e in sorted(DATA['negative_flux_edge_indices']):
        result=birth(state,e)
        assert result is not None and result[1]=='minus'
        state=result[0];assert physical(state);birth_word.append(e)
    assert state==initial
    # Contractible six-edge loops test more than elementary plaquettes. Some
    # can be legal in a matching sector; every legal one preserves the jam.
    hex_checks=0;hex_enabled=0
    example=None
    for axes in permutations(range(3)):
        steps=[(axes[0],1),(axes[1],-1),(axes[2],1),
               (axes[0],-1),(axes[1],1),(axes[2],-1)]
        for x in XYZ:
            path=[x]
            for axis,sign in steps:path.append(shift(path[-1],axis,sign))
            assert path[-1]==x and len(set(path[:-1]))==6
            verts=tuple(INDEX[p] for p in path[:-1])
            for orientation in (-1,1):
                hex_checks+=1;out=field_loop(initial,verts,orientation)
                if out is not None:
                    hex_enabled+=1
                    assert physical(out) and matching_state(out)
                    assert out[1].bit_count()==31 and out[0]==initial[0]
                    assert not hopping_channels(out)
                    assert not [e for e in range(len(EDGES)) if birth(out,e)]
                    if example is None:example={'cycle':path[:-1],'orientation':orientation}
    # A noncontractible positive-x ring through 000 changes F by +4 and opens
    # a hop. It is outside the contractible-loop closure assertion.
    ring=tuple(INDEX[(x,0,0)] for x in range(4))
    winding=field_loop(initial,ring,-1)
    assert winding is not None and physical(winding)
    assert winding[1].bit_count()==35
    winding_hop=hop(winding,INDEX[(1,0,0)],INDEX[(0,0,0)])
    assert winding_hop is not None and physical(winding_hop)
    # Apply the specified occupied-record cycle, the two specified hops,
    # then its uniquely allowed pair birth.
    cycle=tuple(INDEX[tuple(x)] for x in DATA['specified_record_cycle'])
    postcycle=record_cycle(initial,cycle,1)
    assert postcycle is not None and physical(postcycle)
    assert record_cycle(postcycle,cycle,-1)==initial
    assert postcycle[1].bit_count()==33
    hop_vertices=[tuple(INDEX[tuple(x)] for x in pair) for pair in DATA['specified_hops']]
    target=postcycle
    for src,dst in hop_vertices:
        target=hop(target,src,dst);assert target is not None and physical(target)
    reversed_hops=postcycle
    for src,dst in reversed(hop_vertices):
        reversed_hops=hop(reversed_hops,src,dst)
    assert reversed_hops==target
    birth_vertices=tuple(INDEX[tuple(x)] for x in DATA['specified_birth_edge'])
    be,bs=LOOKUP[birth_vertices]
    assert bs==1
    final,bchannel=birth(target,be)
    assert bchannel=='plus' and physical(final) and all(final[0])
    assert final[1].bit_count()==34
    # Enumerate all Hermitian hopping, elementary pure-field, and record-cycle
    # channels needed for H^1,H^2,H^3 between the two fixed endpoint states.
    # K and K-dagger are kept separate, so duplicate channels add coherently.
    start=hamiltonian_channels(initial)
    backward=hamiltonian_channels(target)
    reverse_by_state=defaultdict(list)
    for z,label in backward:reverse_by_state[z].append(label)
    first=sum(z==target for z,label in start)
    second=sum(len(reverse_by_state[z]) for z,label in start)
    routes=[]
    for u,first_label in start:
        for v,middle_label in hamiltonian_channels(u):
            for last_reverse in reverse_by_state.get(v,[]):
                routes.append({'first':first_label,'second':middle_label,'third_reversed':last_reverse})
    assert first==second==0
    assert len(routes)==2
    for r in routes:
        assert r['first']['kind']=='record_cycle'
        assert r['second']['kind']==r['third_reversed']['kind']=='hop'
    result={'boundary':'Independent pre-author-source controls from supplied definitions and neutral INPUT_WITNESS.json.',
            'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
            'local_controls':local_controls(),
            'torus':{'N':N,'vertices':len(XYZ),'oriented_positive_links':len(EDGES),'elementary_faces_counted_once':len(FACES)},
            'initial_state':state_summary(initial),
            'initial_legal_hops':0,'initial_legal_births':0,'initial_legal_elementary_field_plaquettes':0,
            'contractible_hexagon_channels_tested':hex_checks,'enabled_contractible_hexagon_channels':hex_enabled,
            'one_enabled_hexagon_example':example,
            'birth_only_empty_to_witness_word':birth_word,
            'winding_countercontrol':{'ring':[XYZ[v] for v in ring],'orientation':-1,'negative_links_after':35,'opened_hop':[[1,0,0],[0,0,0]]},
            'post_record_cycle':state_summary(postcycle),'pre_final_birth':state_summary(target),'full_final_state':state_summary(final),
            'final_birth_edge':be,'final_birth_channel':bchannel,
            'coherent_matrix_elements_at_unit_coefficients':{'H':first,'H_squared':second,'H_cubed':len(routes)},
            'all_length_three_routes':routes,
            'general_leading_nojump_then_birth_amplitude':'i*sqrt(beta)*g*kappa_hop1*kappa_hop2*t^3/3 + O(t^4)',
            'leading_target_resolved_first_birth_density':'beta*g^2*kappa_hop1^2*kappa_hop2^2*t^6/9 + O(t^7)',
            'rate_convention':'Each elementary face occurs once as K+K-dagger, coefficient g; each undirected hopping channel occurs once with its coefficient. The specified face orientation can be reversed without changing K+K-dagger.',
            'scope':'Positive completion probability from this witness and reachable empty history only; no all-state completion claim for the added cycle model.',
            'runtime_seconds':time.monotonic()-started}
    (HERE/'LINK_WITNESS_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
