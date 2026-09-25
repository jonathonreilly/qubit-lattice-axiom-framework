#!/usr/bin/env python3
"""Check PRE source/log bindings and every saved exact row, without imports.

The occupation rows are independently recomputed from the direct intermediate
four-B-set Gram formula, not from the normal-order implementation under test.
No author code or live scientific runner is loaded or executed.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations,product
from pathlib import Path
import hashlib,json,time

HERE=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name):return json.loads((HERE/name).read_text())


def verify_occupation(data):
    reports=[]
    for row in data['rows']:
        L=row['L'];vertices=tuple(product(range(L),repeat=3))
        AA=tuple(v for v in vertices if sum(v)%2==0)
        BB=tuple(v for v in vertices if sum(v)%2==1)
        near={v:tuple(w for w in vertices if sum(min((x-y)%L,(y-x)%L)
                       for x,y in zip(v,w))==1) for v in vertices}
        kernels=[]
        for u,v in combinations(AA,2):
            if not set(near[u])&set(near[v]):continue
            kernel=Counter(tuple(sorted((b,d))) for b in near[u] for d in near[v] if b!=d)
            kernels.append(kernel)
        assert len(kernels)==row['overlapping_A_pairs']
        q0=sum(sum(m*m for m in kernel.values()) for kernel in kernels)
        assert q0==row['magnetic_Q0']
        labels=list(map(tuple,row['orbit_labels']))
        def label(J):
            x,y=J
            return tuple(sorted(min((a-b)%L,(b-a)%L) for a,b in zip(x,y)))
        size=Counter(label(J) for J in combinations(BB,2))
        assert [size[k] for k in labels]==row['orbit_sizes']
        checked_entries=0
        for i,saved in enumerate(row['saved_occupation_rows']):
            J=frozenset(map(tuple,saved['occupied_B']));actual=Counter()
            for kernel in kernels:
                for D,m in kernel.items():
                    if J.intersection(D):continue
                    R=J.union(D)
                    for inward in combinations(sorted(R),2):
                        k=kernel.get(inward,0)
                        if k:actual[tuple(sorted(R.difference(inward)))]+=m*k
            expected={tuple(map(tuple,e['occupied_B'])):e['value'] for e in saved['entries']}
            assert dict(actual)==expected
            checked_entries+=len(expected)
            coarse=Counter()
            for target,weight in actual.items():coarse[label(target)]+=weight
            offset=[coarse[k]-(q0 if j==i else 0) for j,k in enumerate(labels)]
            assert offset==row['orbit_quotient_offset_from_Q0'][i]
        matrix=row['orbit_quotient_offset_from_Q0'];sizes=row['orbit_sizes']
        assert all(sizes[i]*matrix[i][j]==sizes[j]*matrix[j][i]
                   for i in range(len(sizes)) for j in range(len(sizes)))
        w=row['proposed_positive_integer_vector'];assert min(w)>0
        ratios=[Fraction(sum(a*b for a,b in zip(line,w)),w[i]) for i,line in enumerate(matrix)]
        assert min(ratios)==Fraction(row['exact_Perron_increment_lower'])
        assert max(ratios)==Fraction(row['exact_Perron_increment_upper'])
        average=Fraction(sum(sizes[i]*sum(line) for i,line in enumerate(matrix)),sum(sizes))
        assert average==Fraction(row['uniform_trial_increment'])
        reports.append(dict(L=L,complete_direct_Gram_rows=len(row['saved_occupation_rows']),
            exact_sparse_entries=checked_entries,all_quotient_entries_recomputed=True,
            exact_Collatz_lower=str(min(ratios)),exact_Collatz_upper=str(max(ratios))))
    return reports


def verify_primitive(data,occupation):
    lookup={r['L']:r for r in occupation['rows']};reports=[]
    for row in data['rows']:
        L=row['L'];previous=lookup[L]
        saved={tuple(map(tuple,r['occupied_B'])):
               {tuple(map(tuple,e['occupied_B'])):e['value'] for e in r['entries']}
               for r in previous['saved_occupation_rows']}
        assert len(row['rows'])==row['initial_colored_words']
        paths=0;compared=0
        for r in row['rows']:
            full={tuple(map(tuple,e['occupied_B'])):e['value'] for e in r['complete_occupation_row']}
            assert len(full)==r['occupation_destinations']
            assert sum(full.values())==r['primitive_paths'];paths+=r['primitive_paths']
            raw=json.dumps([dict(occupied_B=k,value=v) for k,v in sorted(full.items())],sort_keys=True).encode()
            assert hashlib.sha256(raw).hexdigest()==r['occupation_row_sha256']
            J=tuple(map(tuple,r['occupied_B']))
            if r['directly_compared_to_saved_row']:
                assert full==saved[J];compared+=1
        assert paths==row['total_primitive_paths']
        assert compared==row['direct_reference_rows']
        if L==2:
            matrix=row['full_colored_matrix'];assert len(matrix)==36
            assert all(len(line)==36 and sum(line)==49 and min(line)>=0 for line in matrix)
            assert all(matrix[i][j]==matrix[j][i] for i in range(36) for j in range(36))
        for birth in row['resolved_birth_checks']:
            assert birth['squared_norm']==row['degree']-1==len(birth['branches'])
            a=tuple(birth['a']);b=tuple(birth['b']);sigma=birth['sigma']
            for branch in birth['branches']:
                J=tuple(map(tuple,branch['occupied_B']));z=next(x for x in J if x!=b)
                charge_delta=Counter({a:sigma-1,b:-sigma,z:1})
                for e in branch['electric_change']:
                    charge_delta[tuple(e['A'])]-=e['value']
                    charge_delta[tuple(e['B'])]+=e['value']
                assert all(x==0 for x in charge_delta.values())
                assert branch['amplitude']==1
        reports.append(dict(L=L,all_primitive_rows_consumed=len(row['rows']),
            primitive_path_count=paths,exact_occupation_comparisons=compared,
            resolved_birth_branches_rechecked=sum(len(b['branches']) for b in row['resolved_birth_checks'])))
    return reports


if __name__=='__main__':
    tic=time.perf_counter();pins=read('SOURCE_PINS.json');source_checks=[]
    for source in pins['sources']:
        frozen=HERE/source['frozen_path'];origin=Path(source['origin'])
        assert sha(origin)==sha(frozen)==source['sha256']
        assert len(frozen.read_bytes())==source['bytes']
        source_checks.append(dict(origin=str(origin),sha256=sha(origin),bytes=source['bytes']))
    assert read('freeze.stdout.txt')==pins
    executions=[]
    for label,script in [('freeze','freeze_sources.py'),('occupation','occupation_spectrum.py'),
                         ('primitive','primitive_colored_control.py')]:
        receipt=read(label+'.execution.json');assert receipt['exit_code']==0
        assert receipt['script_sha256']==sha(HERE/script)
        for stream in ('stdout','stderr'):
            path=HERE/(label+'.'+stream+'.txt')
            assert sha(path)==receipt[stream+'_sha256']
            assert path.stat().st_size==receipt[stream+'_bytes']
        assert receipt['stderr_bytes']==0
        executions.append(dict(label=label,script_sha256=receipt['script_sha256'],
            receipt_sha256=sha(HERE/(label+'.execution.json')),stdout_sha256=receipt['stdout_sha256']))
    occupation=read('OCCUPATION_SPECTRUM_RESULTS.json');primitive=read('PRIMITIVE_COLORED_RESULTS.json')
    assert occupation['source_sha256']==sha(HERE/'occupation_spectrum.py')
    assert primitive['source_sha256']==sha(HERE/'primitive_colored_control.py')
    assert primitive['comparison_data_sha256']==sha(HERE/'OCCUPATION_SPECTRUM_RESULTS.json')
    summary={**occupation,'rows':[{k:v for k,v in r.items() if k!='saved_occupation_rows'} for r in occupation['rows']]}
    assert summary==read('occupation.stdout.txt')
    summary={**primitive,'rows':[{k:v for k,v in r.items() if k not in ('rows','full_colored_matrix')} for r in primitive['rows']]}
    assert summary==read('primitive.stdout.txt')
    results=dict(scope=__doc__,source_sha256=sha(Path(__file__)),source_checks=source_checks,
        execution_bindings=executions,occupation=verify_occupation(occupation),
        primitive=verify_primitive(primitive,occupation),
        full_result_hashes={name:sha(HERE/name) for name in ('OCCUPATION_SPECTRUM_RESULTS.json','PRIMITIVE_COLORED_RESULTS.json')},
        PRE_sha256=sha(HERE/'PRE.md'),elapsed_seconds=time.perf_counter()-tic,
        all_checks_satisfied=True,no_author_code=True,
        authority_limit='Own deterministic evidence checks; not an audit or a finite-g spectral reproduction')
    with (HERE/'PRE_VERIFICATION_RESULTS.json').open('x') as out:json.dump(results,out,indent=2);out.write('\n')
    print(json.dumps(results,indent=2))
