"""Verify frozen saved outputs without importing/replaying the author's compiler.

Named risks: serialized route/count/target/output drift relative to source prose.
Exact JSON/permutation inspection plus floating reanalysis of already saved
matrices. No gate propagation, gate emission, interval proof or new simulation.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json
import math
import platform
import sys
import numpy as np

OUT=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_fixture_exposed_check')
SRC=OUT.parent/'local_conserving_sparse_compiler_fixture'
sha=lambda raw:hashlib.sha256(raw).hexdigest()
freeze_raw=(SRC/'FREEZE.json').read_bytes()
assert sha(freeze_raw)=='2b62a1ba9241999824241c41f191674c3a66c0829185e5bc6ea76052fcc40582'
freeze=json.loads(freeze_raw)
capture=OUT/'fixture_source';capture.mkdir(exist_ok=False)
rows=[]
for row in list(freeze['members'])+[{'path':'FREEZE.json','bytes':len(freeze_raw),'sha256':sha(freeze_raw)}]:
    rel=Path(row['path']);assert not rel.is_absolute() and '..' not in rel.parts
    raw=(SRC/rel).read_bytes();assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
    dest=capture/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
    rows.append({'original_path':str(SRC/rel),'capture':str(dest.relative_to(OUT)),'bytes':len(raw),'sha256':sha(raw)})
assert sha((capture/'REVIEW.md').read_bytes())=='c9e99e725b3efd8dabbf551c315e983113129de0ed12d5f9028c207f93fe9649'
authorrun=capture/'runs/attempt_01'
receipt=json.loads((authorrun/'EXECUTION.json').read_bytes())
assert receipt['returncode']==0
for key in ['source','launcher','stdout','stderr']:
    row=receipt[key]
    original=Path(row['path']);rel=original.relative_to(SRC)
    raw=(capture/rel).read_bytes()
    assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
assert (capture/'emitted_word_fixture.py').read_bytes()==(authorrun/'source_at_launch.py').read_bytes()
assert (capture/'run_fixture.py').read_bytes()==(authorrun/'launcher_at_launch.py').read_bytes()
assert (authorrun/'stderr.txt').read_bytes()==b''
parent_rows=[]
for row in json.loads((capture/'SOURCE_MANIFEST.json').read_bytes())['parents']:
    raw=Path(row['original_path']).read_bytes()
    assert sha(raw)==row['sha256'] and len(raw)==row['bytes']
    assert raw==(capture/row['packet_copy']).read_bytes()
    parent_rows.append(row)
prior=OUT.parent/'local_conserving_sparse_compiler_exposed_check'
prior_rows=[]
for name,expected in [('REVIEW.md','2af89ecefd2d682259e967cc96ef1f5965c37500de4d3cc9261cb39d50254a2a'),('FREEZE.json','54c2e39507456f530ae87534d58ed24412b5de0bfe1669f7ba6600781ae55fe9')]:
    raw=(prior/name).read_bytes();assert sha(raw)==expected
    dest=OUT/'prior_review'/name;dest.parent.mkdir(exist_ok=True);dest.write_bytes(raw)
    prior_rows.append({'original_path':str(prior/name),'capture':str(dest.relative_to(OUT)),'bytes':len(raw),'sha256':expected,'scope':'Identity and prior-exposure record; not a new parent review or copy of its entire closure.'})

saved=authorrun/'output'
report=json.loads((saved/'RESULT.json').read_bytes())
stdout=(authorrun/'stdout.txt').read_text()
decoder=json.JSONDecoder();printed,end=decoder.raw_decode(stdout)
assert printed==report
assert stdout[end:].strip()=='All predeclared fixture discriminators satisfied; numerical evidence only.'
for info in report['words'].values():
    raw=(saved/info['path']).read_bytes()
    assert sha(raw)==info['sha256'] and len(raw)==info['bytes']
words={name:json.loads((saved/(name+'_word.json')).read_bytes()) for name in ['logical','routed','mutant_logical','mutant_routed']}
segments=json.loads((saved/'segments.json').read_bytes())
assert len(segments)==3
position=0;mutant_expected=[]
for sector,row in enumerate(segments,1):
    assert row['sector']==sector
    assert row['phase_start']==position and row['phase_count']==1520
    assert row['givens_start']==position+1520 and row['givens_count']==608
    mutant_expected+=words['logical'][row['givens_start']:row['givens_start']+row['givens_count']]
    position+=2128
assert position==len(words['logical'])==6384
assert words['mutant_logical']==mutant_expected

route_reports=[]
for prefix in ['', 'mutant_']:
    logical=words[prefix+'logical'];routed=words[prefix+'routed']
    for word in [logical,routed]:
        for g in word:
            assert g['kind'] in {'A','Z','SWAP'}
            sites=g['sites'];assert all(type(x) is int and 0<=x<5 for x in sites)
            assert len(set(sites))==len(sites)
            assert len(sites)==(1 if g['kind']=='Z' else 2)
            if g['kind']=='Z':assert math.isfinite(g['phi']) and -math.pi<=g['phi']<=math.pi
    assert all(g['kind'] in {'A','Z'} for g in logical)
    cursor=0;hist=Counter();pairs=Counter()
    for idx,g in enumerate(logical):
        group=[]
        while cursor<len(routed) and routed[cursor]['logical_index']==idx:
            group.append(routed[cursor]);cursor+=1
        assert group
        if g['kind']=='Z':
            assert len(group)==1 and group[0]['kind']=='Z'
            assert group[0]['sites']==g['sites'] and group[0]['phi']==g['phi']
            assert group[0]['route_role']=='onsite'
        else:
            i,j=g['sites'];distance=abs(i-j);hist[distance]+=1;pairs[(i,j)]+=1
            assert len(group)==2*(distance-1)+1
            tokens=list(range(5));stage='out';out_edges=[];return_edges=[];local_count=0
            for physical in group:
                a,b=physical['sites'];assert abs(a-b)==1
                if physical['kind']=='SWAP':
                    if physical['route_role']=='out':
                        assert stage=='out';out_edges.append([a,b])
                    else:
                        assert physical['route_role']=='return' and stage in {'local','return'}
                        stage='return';return_edges.append([a,b])
                    tokens[a],tokens[b]=tokens[b],tokens[a]
                else:
                    assert physical['kind']=='A' and physical['route_role']=='local_A' and stage=='out'
                    stage='local';local_count+=1
                    assert [tokens[a],tokens[b]]==[i,j]
            assert local_count==1 and tokens==list(range(5))
            assert return_edges==list(reversed(out_edges))
    assert cursor==len(routed)
    c_log=dict(Counter(g['kind'] for g in logical));c_route=dict(Counter(g['kind'] for g in routed))
    assert c_log==report['counts']['by_kind'][prefix+'logical']
    assert c_route==report['counts']['by_kind'][prefix+'routed']
    assert c_route['SWAP']==sum(2*(d-1)*count for d,count in hist.items())
    route_reports.append({'word':prefix+'routed','logical_gates':len(logical),'physical_gates':len(routed),'counts':c_route,'all_route_groups_exactly_checked':True,'operand_order_and_return_permutation_exact':True,'A_distance_histogram':dict(sorted(hist.items())),'A_operand_pair_histogram':{f'{a},{b}':count for (a,b),count in sorted(pairs.items())}})

# The following is floating reanalysis of saved arrays, not a word propagation.
with np.load(saved/'complete_matrices.npz',allow_pickle=False) as archive:
    arrays={key:archive[key] for key in archive.files}
expected_shapes={'target_v':(2,2),'givens':(2,2),'target_u':(16,16),'input_j':(32,16),'expected':(32,16),'logical_u':(32,32),'routed_u':(32,32),'routed_isometry':(32,16),'mutant_isometry':(32,16),'positive_isometry':(32,16),'endpoint':(32,16)}
assert set(arrays)==set(expected_shapes)
for key,shape in expected_shapes.items():
    assert arrays[key].shape==shape and arrays[key].dtype==np.complex128
    assert np.isfinite(arrays[key]).all()
v=((5+12j)/13)*np.array([[3/5,4j/5],[4j/5,3/5]],complex)
u=np.eye(16,dtype=complex)
pairs=[(4,8),(6,12),(7,14)]
for pair in pairs:u[np.ix_(pair,pair)]=v
j=np.zeros((32,16),complex)
for column in range(16):j[2*column,column]=1
assert np.array_equal(arrays['target_v'],v)
assert np.array_equal(arrays['target_u'],u)
assert np.array_equal(arrays['input_j'],j)
assert np.array_equal(arrays['expected'],j@u)
assert np.array_equal(arrays['routed_isometry'],arrays['routed_u']@j)
selected=sorted(x for pair in pairs for x in pair)
outside=[x for x in range(16) if x not in selected]
op=lambda a:float(np.linalg.norm(a,ord=2))
actual=arrays['routed_isometry'];target=arrays['expected']
numeric={
 'complete_isometry_operator_norm':op(actual-target),
 'complete_isometry_frobenius_norm':float(np.linalg.norm(actual-target)),
 'maximum_column_l2_error':float(np.linalg.norm(actual-target,axis=0).max()),
 'identity_off_selected_operator_norm':op((actual-target)[:,outside]),
 'ancilla_one_leakage_operator_norm':op(actual[1::2,:]),
 'isometry_defect_operator_norm':op(actual.conj().T@actual-np.eye(16))}
for name,value in numeric.items():assert abs(value-report['nominal'][name])<1e-15
phi=5040*math.pi/4+math.fsum(abs(g['phi']) for g in words['routed'] if g['kind']=='Z')
assert phi==report['scalar']['positive_reserve_phase_Phi']
extra={
 'logical_and_routed_saved_matrices_equal':bool(np.array_equal(arrays['logical_u'],arrays['routed_u'])),
 'mutant_saved_operator_error':op(arrays['mutant_isometry']-target),
 'mutant_difference_from_24_over_13':abs(op(arrays['mutant_isometry']-target)-24/13),
 'positive_saved_operator_error':op(arrays['positive_isometry']-np.exp(-1j*phi)*actual),
 'endpoint_saved_operator_error':op(arrays['endpoint']-complex(*report['endpoint_illustration']['gamma'])*target),
 'all_columns_l2_error':[float(x) for x in np.linalg.norm(actual-target,axis=0)],
 'saved_full_routed_unitarity_defect':op(arrays['routed_u'].conj().T@arrays['routed_u']-np.eye(32))}
assert extra['mutant_difference_from_24_over_13']<1e-12
assert abs(extra['positive_saved_operator_error']-report['scalar']['positive_word_residual'])<1e-15
assert abs(extra['endpoint_saved_operator_error']-report['endpoint_illustration']['operator_residual'])<1e-15
summary={'utc':datetime.now(timezone.utc).isoformat(),'kind':'exact_structural_inspection_and_floating_saved_matrix_reanalysis','fixture_freeze_member_count':len(freeze['members']),'captured_source_records':len(rows),'source_and_receipt_hashes_verified':True,'compiler_imported_or_replayed':False,'gate_emission_executed':False,'gate_propagation_executed':False,'new_interval_certificate':False,'route_inspection':route_reports,'complete_target_saved_arrays_match':True,'nominal_saved_matrix_residuals':numeric,'additional_saved_matrix_findings':extra,'matrix_shapes':{k:list(v.shape) for k,v in arrays.items()},'python':sys.version,'numpy':np.__version__,'platform':platform.platform()}
(OUT/'ARTIFACT_INSPECTION.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'SOURCE_MANIFEST.json').write_text(json.dumps({'utc':summary['utc'],'fixture_source_records':rows,'unchanged_mathematical_parents':parent_rows,'prior_review_exposure':prior_rows,'coverage':'Complete fixture source and all saved route records; all saved arrays inspected/reanalyzed. No author source import or circuit replay.'},indent=2)+'\n')
print(json.dumps(summary,indent=2))
