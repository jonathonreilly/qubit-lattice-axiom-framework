#!/usr/bin/env python3
"""Post-seal comparison using only independently defined graph rates."""
import sys
sys.dont_write_bytecode=True
import argparse
import hashlib
import itertools as it
import json
from pathlib import Path
import sympy as s
import independent_check as independent

HERE=Path(__file__).resolve().parent;RAW=HERE.parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def authenticate():
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['artifacts']+pre['dependencies']+pre['procedures']:
        p=Path(row['path']);assert p.stat().st_size==row['bytes'] and digest(p)==row['sha256']
    result=json.loads((RAW/'geometric_rare_birth_checks/RESULTS.json').read_text())
    for name,value in result['source_sha256'].items():assert digest(RAW/name)==value
    assert result['source_sha256']['geometric_rare_birth_check.py']=='2b34607932623c47e8744203bb5da18b6cae7b42eea248c7e2043301ddff5a3b'
    assert result['source_sha256']['GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md']=='b6ae15f48bdab91922f13ff610853646a7cf91c74391d55887af39b583584611'
    text=(RAW/'GEOMETRIC_RARE_BIRTH_RUN.log').read_text();decoder=json.JSONDecoder();objects=[]
    while text.strip():
        obj,end=decoder.raw_decode(text.lstrip());objects.append(obj);text=text.lstrip()[end:]
    assert objects[:-1]==result['rows']
    assert objects[-1]=={'complete':True,'groups':len(result['rows']),'source_sha256':result['source_sha256']}
    assert all(row['pass'] for row in result['rows']) and (RAW/'GEOMETRIC_RARE_BIRTH_RUN.stderr').read_bytes()==b''
    own=json.loads((HERE/'INDEPENDENT_RESULTS.json').read_text())
    graph=next(x for x in result['rows'] if x['name'].startswith('all_connected_regular'))
    assert graph['graphs']==own['regular_graphs']['connected_regular_bipartite_labeled_graphs']
    assert graph['near_states']==own['regular_graphs']['total_near_perfect_states_checked']
    cube=next(x for x in result['rows'] if x['name'].startswith('cube_exact_symbolic'))
    for author_key,own_key in [('probability','columnar_probability_from_empty'),('at_one','at_b_1'),('slow_limit','slow_limit'),('fast_limit','fast_limit')]:
        assert cube[author_key]==own['symbolic_cube_absorption'][own_key]
    return result,{'preseal_artifacts_unchanged':len(pre['artifacts']),'author_groups_authenticated':len(result['rows']),
                   'all_four_source_bindings_match':len(result['source_sha256'])==4,
                   'recorded_stdout_equals_results':True,'stderr_empty':True,
                   'author_runner_executed_or_imported':False}

def cube_geometry():
    coords=list(it.product((0,1),repeat=3));index={x:i for i,x in enumerate(coords)}
    edges={independent.edge(i,j) for i in range(8) for j in range(i+1,8)
           if sum(abs(a-b) for a,b in zip(coords[i],coords[j]))==1}
    transforms=[{i:index[tuple(x[perm[j]]^bits[j] for j in range(3))] for i,x in enumerate(coords)}
                for perm in it.permutations(range(3)) for bits in it.product((0,1),repeat=3)]
    def representative(m):return min(tuple(sorted(independent.edge(T[a],T[b]) for a,b in m)) for T in transforms)
    return coords,edges,representative

def certificate_comparison():
    coords,edges,representative=cube_geometry();states=independent.own.all_matchings(8,edges)
    certificate=json.loads((RAW/'geometric_rare_birth_checks/CUBE_HARMONIC_CERTIFICATE.json').read_text())
    b=s.symbols('b',positive=True);parse=lambda x:s.sympify(x,locals={'b':b})
    orbits=[tuple(tuple(e) for e in m) for m in certificate['orbits']];oi={m:i for i,m in enumerate(orbits)}
    assert sorted(set(representative(m) for m in states))==orbits
    Q=s.Matrix([[parse(x) for x in row] for row in certificate['generator']]);u=s.Matrix([parse(x) for x in certificate['harmonic_solution']])
    for m in states:
        row=s.zeros(1,len(orbits));i=oi[representative(m)]
        for kind,data,target in independent.own.channels(m,edges):
            rate=b if kind=='birth' else 1
            row[oi[representative(target)]]+=rate;row[i]-=rate
        assert (Q[i,:]-row).applyfunc(s.expand)==s.zeros(1,len(orbits))
        if len(m)==4:
            columnar=len({next(j for j in range(3) if coords[a][j]!=coords[c][j]) for a,c in m})==1
            assert u[i]==int(columnar)
        else:assert s.factor((row*u)[0])==0
    assert certificate['full_state_boundary_and_harmonic_checks']==len(states)
    return {'original_states_checked':len(states),'quotient_rows_and_lifted_harmonic_solution_match':True}

def killed_chain_comparison(result):
    coords,edges,representative=cube_geometry()
    certificate=json.loads((RAW/'geometric_rare_birth_checks/CUBE_KILLED_CHAIN.json').read_text())
    author=next(row for row in result['rows'] if row['name']=='full_near_perfect_killed_chain_all_targets')
    assert all(certificate[k]==author[k] for k in ('near_states','full_states','rows'))
    rows=[]
    for row in certificate['rows']:
        beta=s.Rational(row['beta'])
        near,full,S,A,U=independent.last_birth_matrix(8,edges,beta)
        h=A*s.ones(len(full),1)
        assert S==S.T and all(x==4 for x in list(s.ones(1,len(near))*A)) and sum(h)==36
        assert (-S+beta*s.diag(*h))*U==beta*A and all(x>=0 for x in U)
        deviation=max(sum(abs(U[i,j]-s.Rational(1,len(full))) for j in range(len(full)))/2 for i in range(len(near)))
        assert deviation==s.Rational(row['worst_start_TV']) and float(deviation)==row['decimal']
        rows.append({'beta':str(beta),'independently_recomputed_exact_worst_start_TV':str(deviation)})
    return {'near_states':len(near),'full_states':len(full),'rows':rows}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    author,authentication=authenticate()
    result={'authentication':authentication,'cube_certificate':certificate_comparison(),
            'cube_killed_chain':killed_chain_comparison(author),
            'limits':['Author exact transform event/cycle totals and eight N=4,6,8,12 periodic path receipts were authenticated, not independently replayed.',
                      'Independent blind controls include all small graph connectivity and separate complete path reconstructions, plus distant and winding N=4 cycles.',
                      'No production kinetics, phase, fixed-rate thermodynamic or wave result was accessed.']}
    args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
