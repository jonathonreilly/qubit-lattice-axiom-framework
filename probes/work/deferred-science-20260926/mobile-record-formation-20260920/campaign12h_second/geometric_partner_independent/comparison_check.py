#!/usr/bin/env python3
"""Post-seal evidence comparison. Imports only this review's own checker.

The cube generator is rebuilt without symmetry lumping; the author cube
certificate and rational answers are compared, not used to define rates.
No author code is imported or executed, and no production files are written.
"""
import sys
sys.dont_write_bytecode=True
import argparse
from collections import Counter,deque
import hashlib
import itertools as it
import json
from pathlib import Path
import sympy as s
import independent_check as own

HERE=Path(__file__).resolve().parent
RAW=HERE.parent

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def authenticated_inputs():
    seal=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in seal['artifacts']+[seal['primary_source']]+seal['procedures']:
        p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
    expected={'GEOMETRIC_PARTNER_RECORD_FORMATION.md':'1bc76bc39c672c7eec318fb4e999dc6e2b1f80aad9a058683dbeb7f7ae247969',
              'geometric_partner_formation_check.py':'3766230651e8e69c8f51228cd3c3e7ded55140e96bf4b28255042e28e87cb259'}
    result=json.loads((RAW/'geometric_partner_checks/RESULTS.json').read_text())
    assert result['sources_sha256']==expected
    for name,digest in expected.items():assert sha(RAW/name)==digest
    decoder=json.JSONDecoder();text=(RAW/'GEOMETRIC_PARTNER_FORMATION_RUN.log').read_text();objects=[]
    while text.strip():
        obj,end=decoder.raw_decode(text.lstrip());objects.append(obj);text=text.lstrip()[end:]
    assert objects[:-1]==result['rows']
    assert objects[-1]=={'groups':len(result['rows']),'all_pass':result['all_pass'],'sources_sha256':expected}
    assert (RAW/'GEOMETRIC_PARTNER_FORMATION_RUN.stderr').read_bytes()==b''
    assert result['all_pass'] and all(row['pass'] for row in result['rows'])
    return result,{'unchanged_preseal_artifacts':len(seal['artifacts']),
                   'source_bindings':expected,'recorded_author_groups':len(result['rows']),
                   'author_stdout_matches_results':True,'author_stderr_empty':True,
                   'author_execution_repeated':False}

def cube_reconstruction(result):
    vertices=list(it.product((0,1),repeat=3));n=len(vertices)
    edges={own.edge(i,j) for i in range(n) for j in range(i+1,n)
           if sum(abs(a-b) for a,b in zip(vertices[i],vertices[j]))==1}
    faces=[]
    for subset in it.combinations(range(n),4):
        induced={e for e in edges if set(e)<=set(subset)}
        degree=Counter(x for e in induced for x in e)
        if len(induced)==4 and all(degree[x]==2 for x in subset):faces.append(frozenset(induced))
    assert len(faces)==6
    states=own.all_matchings(n,edges);index={m:i for i,m in enumerate(states)}
    assert len(states)==108
    def transitions(m):
        out=[(kind,data,target) for kind,data,target in own.channels(m,edges)]
        for face in faces:
            old=m&face
            if len(old)==2 and len(own.partners(old))==4:
                target=(m-old)|(face-old)
                out.extend([('flip',sign,target) for sign in (-1,1)])
        return out
    certificate=json.loads((RAW/'geometric_partner_checks/CUBE_CHANNELS.json').read_text())
    cert_states=[frozenset(tuple(e) for e in row['matching']) for row in certificate]
    assert len(set(cert_states))==len(states) and set(cert_states)==set(states)
    checked=0;kind_counts=Counter()
    for row,m in zip(certificate,cert_states):
        expected=Counter((kind,target) for kind,data,target in transitions(m))
        actual=Counter()
        for channel in row['channels']:
            target=cert_states[channel['target']];event=channel['event'];kind=event[0]
            assert channel['rate']==1
            if kind=='birth':
                a,b=event[1:];assert own.edge(a,b) in edges
                assert a not in own.partners(m) and b not in own.partners(m)
                assert target==m|{own.edge(a,b)}
            elif kind=='slide':
                a,b,c=event[1:];assert own.edge(a,b) in m and own.edge(b,c) in edges
                assert c not in own.partners(m)
                assert target==(m-{own.edge(a,b)})|{own.edge(b,c)}
            elif kind=='flip':
                corners,sign=event[1:];assert len(set(corners))==4 and sign in (-1,1)
                perimeter={own.edge(corners[j],corners[(j+1)%4]) for j in range(4)}
                assert frozenset(perimeter) in faces
                old=m&perimeter;assert len(old)==2 and len(own.partners(old))==4
                assert target==(m-old)|(perimeter-old)
            else:raise AssertionError(kind)
            actual[(kind,target)]+=channel['rate'];kind_counts[kind]+=1;checked+=1
        assert actual==expected
    author_cube=next(x for x in result['rows'] if x['name']=='complete_cube_graph_augmentation_and_exact_absorption')
    assert {str(k):v for k,v in Counter(map(len,states)).items()}==author_cube['count_census']
    assert checked==author_cube['channels']==912
    transient=[i for i,m in enumerate(states) if len(m)<4]
    full=[i for i,m in enumerate(states) if len(m)==4]
    evidence=[]
    for nu in (0,1):
        L=s.zeros(len(states))
        for m,i in index.items():
            for kind,data,target in transitions(m):
                rate=nu if kind=='flip' else 1
                L[i,index[target]]+=rate;L[i,i]-=rate
        assert L*s.ones(len(states),1)==s.zeros(len(states),1)
        Q=L.extract(transient,transient)
        inverse=(-Q).inv(method='DM')
        times=inverse*s.ones(len(transient),1)
        hit=inverse*L.extract(transient,full)*s.ones(len(full),1)
        assert hit==s.ones(len(transient),1) and all(t>0 for t in times)
        empty=transient.index(index[frozenset()]);value=times[empty]
        author=next(r for r in author_cube['exact_lumped_results'] if r['nu']==nu)
        assert value==s.Rational(author['expected_empty_filling_time'])
        evidence.append({'nu':nu,'transient_states':len(transient),'unlumped_exact_mean_empty_filling_time':str(value),
                         'all_transient_full_hit_probabilities':'1'})
    full_states={states[i] for i in full};seen={next(iter(full_states))};todo=deque(seen)
    while todo:
        m=todo.popleft()
        for kind,data,target in transitions(m):
            if kind=='flip' and target not in seen:seen.add(target);todo.append(target)
    assert seen==full_states
    return {'cube_states':len(states),'certificate_channels_checked':checked,'channel_kinds':dict(kind_counts),
            'unlumped_exact_absorption':evidence,'full_flip_component_size':len(seen)}

def twelve_vertex_census(result):
    points=list(it.product(range(3),range(2),range(2)))
    edges={own.edge(i,j) for i in range(len(points)) for j in range(i+1,len(points))
           if sum(abs(x-y) for x,y in zip(points[i],points[j]))==1}
    states=own.all_matchings(len(points),edges)
    row=next(x for x in result['rows'] if x['name']=='exhaustive_twelve_vertex_augmentations')
    assert len(states)==row['states'] and sum(len(m)<6 for m in states)==row['nonfull']
    return {'states':len(states),'full_matchings':sum(len(m)==6 for m in states),
            'event_total_2979':'Authenticated as an author execution output, not independently reconstructed here; depends on the chosen reference matching and path convention.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result,authentication=authenticated_inputs()
    out={'authentication':authentication,'independent_cube_comparison':cube_reconstruction(result),
         'independent_twelve_vertex_census':twelve_vertex_census(result),
         'coverage_limit':'The 18 deterministic periodic marked histories were read in source and authenticated against the recorded log/results, not rerun. No production simulator, kinetics, phase or wave result was inspected.'}
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
