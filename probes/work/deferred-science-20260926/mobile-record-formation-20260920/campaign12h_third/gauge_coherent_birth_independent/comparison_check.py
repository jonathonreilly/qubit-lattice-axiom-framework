#!/usr/bin/env python3
"""Post-seal checks: no author code imports or author-checker reruns."""
from collections import Counter,deque
from itertools import combinations
from pathlib import Path
import hashlib,json,math,sys,time
sys.dont_write_bytecode=True
import sympy as s
from open_box_check import box,enumerate_physical
from coherent_instrument_check import local

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent
PRIME=1000003


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def authenticate():
    pre=HERE/'PRE_COMPARISON_SEAL.json'
    assert sha(pre)=='fc30598ddaf5e586a999301ba3ad4561a78a6614268399d09fa8fb435519cc3b'
    own=json.loads(pre.read_text())
    seal=AUTHOR/'GAUGE_COMPLETION_AND_COHERENT_BIRTH_AUTHOR_SEAL.json'
    assert sha(seal)=='016efff81e95874edb19222e7d5b490bc0b1e1693aed003b04a58d444fa71f08'
    author=json.loads(seal.read_text())
    for row in own['sources']+own['artifacts']+author['artifacts']:
        p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
    stems=['GAUGE_CONFIGURATION_CONNECTIVITY_SCREEN','GAUGE_OCCUPATION_OBSERVABILITY',
           'GAUGE_OPEN_BOX_JAM_SCREEN','GAUGE_COHERENT_PAIR_BIRTH','GAUGE_BIRTH_FRESH_MEMORY_DILATION']
    for stem in stems:
        receipt=json.loads((AUTHOR/(stem+'_RUN_RECEIPT.json')).read_text())
        result=json.loads((AUTHOR/(stem+'_RESULTS.json')).read_text())
        script=AUTHOR/receipt['command'][-1]
        assert receipt['returncode']==0 and receipt['script_sha256']==result['script_sha256']==sha(script)
        assert (AUTHOR/(stem+'_RUN.stderr')).read_bytes()==b''
        if stem=='GAUGE_OPEN_BOX_JAM_SCREEN':
            expected=dict(result)
            expected['cases']=[{k:v for k,v in r.items() if k not in {'negative_edges','charge','exact_empty_birth_sequence'}} for r in result['cases']]
            assert json.loads((AUTHOR/(stem+'_RUN.log')).read_text())==expected
        else:assert (AUTHOR/(stem+'_RUN.log')).read_bytes()==(AUTHOR/(stem+'_RESULTS.json')).read_bytes()
    observability=json.loads((AUTHOR/'GAUGE_OCCUPATION_OBSERVABILITY_RESULTS.json').read_text())
    assert observability['inventory_script_sha256']==sha(AUTHOR/'gauge_configuration_connectivity_screen.py')
    return dict(prior_bindings_authenticated=len(own['sources'])+len(own['artifacts']),
                frozen_author_artifacts_authenticated=len(author['artifacts']),
                all_five_success_receipts_and_complete_log_relationships_verified=True)


def faces_of(vertices,edges):
    index={v:i for i,v in enumerate(vertices)}
    lookup={(x,y):(e,1) for e,(x,y) in enumerate(edges)}
    lookup.update({(y,x):(e,-1) for e,(x,y) in enumerate(edges)})
    faces=[]
    for x in vertices:
        for a,b in combinations(range(3),2):
            y=list(x);y[a]+=1;z=list(x);z[b]+=1;w=list(y);w[b]+=1
            if tuple(y) in index and tuple(z) in index and tuple(w) in index:
                faces.append(tuple(index[v] for v in (x,tuple(y),tuple(w),tuple(z))))
    return faces,lookup


def graph_and_projected_H_certificate(lengths):
    vertices,edges=box(lengths);states=enumerate_physical(vertices,edges)
    faces,lookup=faces_of(vertices,edges)
    pattern={m:sum((q!=0)<<i for i,q in enumerate(qs)) for m,qs in states.items()}
    hops={m:set() for m in states};births={m:set() for m in states}
    fields={m:Counter() for m in states};cycles={m:Counter() for m in states}
    for m,qs in states.items():
        for e,(x,y) in enumerate(edges):
            other=m^(1<<e);db=1-2*int(bool(m&(1<<e)))
            if qs[x]==qs[y]==0:births[m].add(other)
            elif (qs[x]==0)!=(qs[y]==0) and (qs[x]+db,qs[y]-db)==(qs[y],qs[x]):hops[m].add(other)
        assert len({pattern[v] for v in hops[m]})==len(hops[m])
        for face in faces:
            for order in (face,(face[0],face[3],face[2],face[1])):
                links=[lookup[(order[i],order[(i+1)%4])] for i in range(4)]
                flip=sum(1<<e for e,sgn in links);other=m^flip
                if all(0<=int(bool(m&(1<<e)))+sgn<=1 for e,sgn in links):
                    assert states[other]==qs;fields[m][other]+=1
                if all(qs[x]!=0 for x in order) and all(0<=int(bool(m&(1<<e)))-sgn*qs[x]<=1 for (e,sgn),x in zip(links,order)):
                    expected=list(qs)
                    for i,x in enumerate(order):expected[order[(i+1)%4]]=qs[x]
                    assert states[other]==tuple(expected);cycles[m][other]+=1
    for m in states:
        for v in hops[m]:assert m in hops[v]
        for graph in (fields,cycles):
            for v,c in graph[m].items():
                assert pattern[v]==pattern[m] and graph[v][m]==c
    # Exact integer H with unequal coefficients; forward/reverse cycle
    # multiplicities remain separate until their matrix elements are added.
    H={m:Counter({v:2 for v in hops[m]}) for m in states}
    max_cycle_multiplicity=0
    for m in states:
        H[m].update({v:3*c for v,c in fields[m].items()})
        H[m].update({v:5*c for v,c in cycles[m].items()})
        max_cycle_multiplicity=max([max_cycle_multiplicity]+list(cycles[m].values()))
    for m,row in H.items():
        for v,c in row.items():assert H[v][m]==c
        for v in hops[m]:
            projected={u:c for u,c in row.items() if pattern[u]==pattern[v]}
            assert projected=={v:2}
    # Every reached basis vector has an explicit word in projected H maps.
    # Division by 2 is valid over Q and over the independently verified prime.
    assert all(PRIME%a for a in range(2,math.isqrt(PRIME)+1))
    sectors=[]
    for records in range(0,len(vertices),2):
        sector={m for m,q in states.items() if sum(x!=0 for x in q)==records}
        contact=sector.intersection(m for m in states if births[m])
        depth={m:0 for m in contact};queue=deque(contact)
        while queue:
            m=queue.popleft()
            for v in hops[m]:
                if v not in depth:depth[v]=depth[m]+1;queue.append(v)
        assert depth.keys()==sector
        sectors.append(dict(records=records,dimension=len(sector),contact_rank=len(contact),
                            full_rank_over_Q_and_Fp_from_projected_H_words=len(depth),
                            maximum_word_length=max(depth.values())))
    # Check the additional support-reachability claim independently.
    empty=(1<<len(edges))-1;seen={empty};queue=deque([empty])
    while queue:
        m=queue.popleft()
        for v in hops[m]|births[m]:
            if v not in seen:seen.add(v);queue.append(v)
    assert len(seen)==len(states)
    author=json.loads((AUTHOR/'GAUGE_OCCUPATION_OBSERVABILITY_RESULTS.json').read_text())
    case=next(c for c in author['cases'] if c['shape']==list(lengths))
    for model in case['models']:
        assert model['coefficients']['kappa']%PRIME!=0
        for actual,expected in zip(sectors,model['sectors']):
            assert actual['records']==expected['records']
            assert actual['dimension']==expected['sector_dimension']==expected['generated_rank_mod_prime']
            assert actual['contact_rank']==expected['initial_contact_rank']
    return dict(shape=lengths,physical_dimension=len(states),ordinary_hop_birth_reachable_states=len(seen),
                actual_integer_H_coefficients=[2,3,5],all_projected_off_pattern_columns_are_single_hops=True,
                maximum_record_cycle_channel_multiplicity=max_cycle_multiplicity,
                prime=PRIME,sectors=sectors,
                scope='Constructive basis-vector words certify full rank over Q and this prime; no author elimination code is imported or replayed.')


def jam_certificates():
    data=json.loads((AUTHOR/'GAUGE_OPEN_BOX_JAM_SCREEN_RESULTS.json').read_text());out=[]
    for row in data['cases']:
        N=row['N'];vertices,edges=box((N,N,N));faces,lookup=faces_of(vertices,edges)
        q=[0]*len(vertices);seen=set();negative=set()
        assert row['negative_edges']==row['exact_empty_birth_sequence']
        for e in row['exact_empty_birth_sequence']:
            x,y=edges[e];assert x not in seen and y not in seen and q[x]==q[y]==0
            seen.update((x,y));q[x]=-1;q[y]=1;negative.add(e)
        assert q==row['charge'] and len(negative)==row['matching_edges']==(N**3-2)//2
        assert [list(vertices[i]) for i,x in enumerate(q) if x==0]==row['holes']
        hop=[];birth=[];enabled_fields=0
        for e,(x,y) in enumerate(edges):
            bit=int(e not in negative);db=1-2*bit
            if q[x]==q[y]==0:birth.append(e)
            elif (q[x]==0)!=(q[y]==0) and (q[x]+db,q[y]-db)==(q[y],q[x]):hop.append(e)
        for face in faces:
            for order in (face,(face[0],face[3],face[2],face[1])):
                links=[lookup[(order[i],order[(i+1)%4])] for i in range(4)]
                enabled_fields+=all(0<=int(e not in negative)+sgn<=1 for e,sgn in links)
        assert not hop and not birth and enabled_fields==0
        assert len(faces)==3*N*(N-1)**2
        out.append(dict(N=N,internal_links=len(edges),plaquettes=len(faces),
                        sequential_legal_births=len(negative),charge_entries_checked=len(q),
                        legal_hops=0,legal_births=0,legal_elementary_field_channels=0))
    return out


def retained_outcome_countercontrol():
    vp,vm,_,_,_=local();psi=s.zeros(18,1);psi[0]=1
    A=(vp,vm);B=((vp+vm)/s.sqrt(2),(vp-vm)/s.sqrt(2))
    probabilities=lambda ops:[s.simplify((psi.T*K.T*K*psi)[0]) for K in ops]
    first=probabilities(A);second=probabilities(B)
    assert first==[1,0] and second==[s.Rational(1,2),s.Rational(1,2)]
    hadamard=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
    assert hadamard.T*hadamard==s.eye(2)
    return dict(coarse_chi='0 for both instruments',coarse_maps_identical_by_exact_Kraus_rotation=True,
                normalized_retained_outcome_probabilities=[[str(v) for v in first],[str(v) for v in second]],
                finding='Chi classifies the coarse birth CP map, not individually retained outcome refinements.')


if __name__=='__main__':
    started=time.monotonic()
    result={'boundary':'Post-seal source comparison; author checkers neither imported nor rerun.',
            'authentication':authenticate(),
            'constructive_observability_certificates':[graph_and_projected_H_certificate((2,2,2)),graph_and_projected_H_certificate((2,2,3))],
            'open_box_jam_certificates':jam_certificates(),
            'instrument_refinement_countercontrol':retained_outcome_countercontrol(),
            'runtime_seconds':time.monotonic()-started}
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
