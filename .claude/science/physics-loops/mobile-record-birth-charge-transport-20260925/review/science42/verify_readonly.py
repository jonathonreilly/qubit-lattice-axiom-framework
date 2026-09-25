#!/usr/bin/env python3
"""Genuinely read-only PRE42 verifier: reads fixed manifest paths, prints JSON.
No writers, subprocesses, dynamic imports, control execution, or directory scans.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path
import difflib
import hashlib
import json

BASE=Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def rational_pair(x):
    return tuple(Q(v) for v in x)


def pair_norm2(x):
    return sum(v*v for v in rational_pair(x))


def main():
    pins=read_json(BASE/'EVIDENCE_PINS.json')
    observations=[]
    for row in pins['members']:
        path=BASE/row['path']
        assert path.is_relative_to(BASE)
        raw=path.read_bytes()
        assert len(raw)==row['bytes']
        assert hashlib.sha256(raw).hexdigest()==row['sha256'],row['path']
        observations.append(dict(path=str(path),sha256=row['sha256'],bytes=len(raw)))
    sources=read_json(BASE/'SOURCE_PINS.json')['sources']
    assert len(sources)==6
    for row in sources:
        assert sha(Path(row['origin']))==row['sha256'],row['origin']
        assert sha(BASE/row['snapshot'])==row['sha256']
        observations.append(dict(path=row['origin'],sha256=row['sha256'],bytes=row['bytes']))
    primitives=read_json(BASE/'primitive_attempt01/stdout.json')
    remainders=read_json(BASE/'remainder_attempt01/stdout.json')
    execution=[]
    for directory,program in (('primitive_attempt01','primitive_birth_charge_control.py'),
                              ('remainder_attempt01','low_wave_remainder_control.py')):
        root=BASE/directory
        receipt=read_json(root/'EXECUTION.json')
        assert receipt['exit_code']==0 and receipt['source_unchanged']
        assert (root/'stderr.txt').read_bytes()==b''
        assert receipt['source_sha256']==sha(root/'source.py')==sha(BASE/program)
        assert receipt['stdout_sha256']==sha(root/'stdout.json')
        assert receipt['stderr_sha256']==sha(root/'stderr.txt')
        execution.append(dict(directory=directory,exit_code=0,empty_stderr=True,
                              elapsed_seconds=receipt['elapsed_seconds'],
                              source_sha256=receipt['source_sha256']))
    groups=('graphs','primitive_fields','moments','selected_mark_moments',
            'coherent_vs_dephased','fourier')
    expected_counts=dict(graphs=4,primitive_fields=10,moments=60,
                         selected_mark_moments=8,coherent_vs_dephased=4,fourier=64)
    assert primitives['group_counts']==expected_counts
    assert {key:len(primitives[key]) for key in groups}==expected_counts
    assert primitives['external_programs_imported'] is False
    assert primitives['status']=='all exact assertions passed'
    assert remainders['status']=='all rational interval assertions passed'
    assert remainders['group_count']==len(remainders['rows'])==16
    for row in primitives['graphs']:
        M=sum(d*(d-1) for d in row['degrees'])
        assert row['ordered_wedges']==M
        assert row['actual_loss_over_kappa']==2*M
        assert row['invalid_all_label_coherent_norm2']==3*M
        assert row['charge_pattern_multiplicities_match']
    for row in primitives['primitive_fields']:
        assert row['gauss_and_regional_charge_tests']
        assert row['resolved_plus_total_norm2']==row['resolved_minus_total_norm2']
        assert row['actual_output_branches']==row['coherent_edges_total_norm2']
        assert row['actual_output_branches']==2*row['resolved_plus_total_norm2']
    for row in primitives['moments']:
        assert row['exact']
        assert Q(row['variance_absolute'])==Q(row['second_absolute'])-pair_norm2(row['mean'])>=0
    for row in primitives['coherent_vs_dephased']:
        assert row['charge_diagonal_equal']
        assert Q(row['coherent_purity'])==1
        assert Q(row['sign_dephased_purity'])==Q(1,2)
        assert Q(row['density_difference_HS2'])==Q(1,2)
        assert row['offdiagonal_sign_entries']>0
    seen=set()
    for row in primitives['fourier']:
        m=tuple(row['mode'])
        seen.add(m)
        C=Q(sum((1,0,-1,0)[i] for i in m),3)
        assert C==Q(row['C'])
        exceptional=m in ((0,0,0),(2,2,2))
        assert rational_pair(row['A_character'])==((1,0) if exceptional else (0,0))
        for sigma in (1,-1,0):
            stat=row['statistics'][str(sigma)]
            second=(Q(12,5)*(1-C*C) if sigma==1 else
                    Q(16,5)*(1-C)+Q(12,5)*(1-C)**2 if sigma==-1 else 4*(1-C))
            local_mean=((1-sigma)*(C-1) if sigma else C-1, Q(0))
            global_mean=local_mean if exceptional else (Q(0),Q(0))
            assert Q(stat['second'])==second
            assert rational_pair(stat['center_mean'])==local_mean
            assert rational_pair(stat['global_mean'])==global_mean
            assert Q(stat['center_variance'])==second-pair_norm2(stat['center_mean'])>=0
            assert Q(stat['global_variance'])==second-pair_norm2(stat['global_mean'])>=0
    assert len(seen)==64
    for row in remainders['rows']:
        k=tuple(Q(x) for x in row['k'])
        lo,hi=map(Q,row['rigorous_second_moment_interval'])
        quadratic=Q(2,3)*sum(x*x for x in k)
        quartic=Q(1,18)*sum(x**4 for x in k)
        sixth=Q(1,540)*sum(abs(x)**6 for x in k)
        assert Q(row['quadratic'])==quadratic
        assert Q(row['quartic_correction'])==quartic
        assert Q(row['sixth_error_bound'])==sixth
        assert quadratic-quartic<=lo<=hi<=quadratic
        assert quadratic-quartic-sixth<=lo<=hi<=quadratic-quartic+sixth
        assert tuple(map(Q,row['quadratic_error_interval']))==(quadratic-hi,quadratic-lo)
    lines=['Lossless scientific-row readout; exact rational strings retained.',
           'Primitive status: '+primitives['status'],
           'Group counts: '+json.dumps(primitives['group_counts'],sort_keys=True)]
    for key in groups:
        lines.append('\nGROUP '+key)
        for i,row in enumerate(primitives[key]):
            lines.append(str(i)+' '+json.dumps(row,sort_keys=True,separators=(',',':')))
    lines.extend(['\nGROUP low_wave_remainders','Status: '+remainders['status'],
                  'Cosine truncation/error degrees: '+str(remainders['cosine_truncation_degree'])+'/'+str(remainders['cosine_error_degree'])])
    for i,row in enumerate(remainders['rows']):
        lines.append(str(i)+' '+json.dumps(row,sort_keys=True,separators=(',',':')))
    assert (BASE/'CONTROL_READOUT.txt').read_text()=='\n'.join(lines)+'\n'
    old=(BASE/'PRE_DRAFT01_BEFORE_PAIR_SCOPE_REPAIR.md').read_text()
    new=(BASE/'PRE.md').read_text()
    diff=''.join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='PRE_DRAFT01',tofile='PRE_corrected'))
    assert (BASE/'PRE_PAIR_SCOPE_REPAIR.diff').read_text()==diff
    assert 'N(a) intersect N(c) nonempty' in new
    assert 'omitting zero pair operators' in old and 'omitting zero pair operators' not in new
    counts=dict(group_rows=sum(expected_counts.values())+16,
                primitive_outputs=sum(row['primitive_output_checks'] for row in primitives['graphs']),
                exact_Gram_entries=sum(row['exact_Gram_entries'] for row in primitives['graphs']),
                selected_mark_moments=sum(row['exact_selected_mark_moment_comparisons'] for row in primitives['selected_mark_moments']))
    assert counts==dict(group_rows=166,primitive_outputs=5956,exact_Gram_entries=5649,selected_mark_moments=1266)
    print(json.dumps(dict(status='all fixed evidence and arithmetic checks passed',
                          verified_utc=datetime.now(timezone.utc).isoformat(),
                          mode='read only; no scientific execution or imports',
                          members_verified=len(pins['members']),origins_verified=len(sources),
                          observations=observations,executions=execution,counts=counts,
                          prior_premise_transcription_repair_preserved=True,
                          author42_exposure=False),indent=2,sort_keys=True))


if __name__=='__main__':
    main()
