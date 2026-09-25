#!/usr/bin/env python3
"""Final source, full-result/summary, numerical-prose and receipt binding."""
from datetime import datetime,timezone
from pathlib import Path
from fractions import Fraction
import ast,hashlib,json,math,re
HERE=Path(__file__).resolve().parent;AUTHOR=HERE/'post_sources/author'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def rat(x):return Fraction(x['numerator'],x['denominator'])
source_pins=read(HERE/'POST_SOURCE_PINS.json')
for r in source_pins['sources']:
    assert sha(HERE/r['frozen_path'])==r['sha256']
    if r.get('role')!='Procedure only':assert sha(Path(r['origin']))==r['sha256']
preseal=read(HERE/'PRE_SEAL.json')
assert sha(HERE/'PRE_SEAL.json')=='bed28ea9c81afb7822d0ddeeb552260e3e0547b6f387c9edb8dbd6aec83ee25b'
for r in preseal['members']:assert sha(HERE/r['path'])==r['sha256']
for r in read(HERE/'SOURCE_PINS.json')['sources']:assert sha(Path(r['origin']))==r['sha256']
author=read(AUTHOR/'NATIVE_PAIR_RESULTS.json');prior=read(HERE/'OCCUPATION_SPECTRUM_RESULTS.json')
own={r['L']:r for r in prior['rows']}
rootverify=read(AUTHOR/'ROOT_VERIFICATION.json')
comparisons=read(HERE/'POST_COMPARISON_RESULTS.json');assert comparisons['all_checks_satisfied']
local=comparisons['local_counts']
summary={**comparisons,'local_counts':{k:v for k,v in local.items() if k not in
    ('complete_near_rows','complete_far_rows','complete_synthetic_cases','L10_all_displacements')}}
summary['local_row_counts']={k:len(local[k]) for k in
    ('complete_near_rows','complete_far_rows','complete_synthetic_cases','L10_all_displacements')}
assert summary==read(HERE/'post_compare.stdout.txt')
assert comparisons['source_sha256']==sha(HERE/'post_compare.py')
import_names=[]
for node in ast.walk(ast.parse((HERE/'post_compare.py').read_text())):
    if isinstance(node,ast.Import):import_names.extend(a.name for a in node.names)
    if isinstance(node,ast.ImportFrom):import_names.append(node.module)
assert all(not name.startswith('native_pair') for name in import_names)
note=(AUTHOR/'NATIVE_ONE_PAIR_SPECTRAL_EDGE_ROOT.md').read_text()
decimal_rows={int(L):(Fraction(lo),Fraction(hi)) for L,lo,hi in re.findall(
    r'\| (4|6|8) \| \d+ \| \((-[0-9.]+), (-[0-9.]+)\) \|',note)}
assert len(decimal_rows)==3
numerical=[]
for r,check in zip(author['quotients'],comparisons['comparison']['quotients']):
    L=r['side'];o=own[L]
    assert r['vertices']==L**3 and r['A_sites']==o['A_count']
    assert r['degree']==o['degree'] and r['overlapping_A_pairs']==o['overlapping_A_pairs']
    assert r['all_weighted_symmetry_and_translation_checks_exact']
    assert math.isfinite(r['floating_top_delta_eigenvalue'])
    assert math.isfinite(r['floating_eigen_residual']) and r['floating_eigen_residual']>=0
    lower=rat(r['proposed_ground_gap_g2_tau_interval']['lower'])
    upper=rat(r['proposed_ground_gap_g2_tau_interval']['upper'])
    if L in decimal_rows:
        dlo,dhi=decimal_rows[L];assert dlo<lower<=upper<dhi
    rootrow=next(x for x in rootverify['quotient_certificates'] if x['side']==L)
    assert rootrow['rows']==r['translation_orbits']==check['author_translation_rows']
    assert rootrow['integer_entries']==check['exact_author_entries']
    assert rootrow['gap_exact']==r['proposed_ground_gap_g2_tau_interval']
    assert [rootrow['row_sum_min'],rootrow['row_sum_max']]==check['row_sum_interval']
    numerical.append(dict(L=L,metadata_matches_PRE=True,exact_gap=[str(lower),str(upper)],
        author_floating_residual=r['floating_eigen_residual'],
        floating_residual_independently_reproduced=False,
        displayed_decimal_interval_verified=(L in decimal_rows)))
assert rootverify['full_cube_integer_rows']==36
assert rootverify['unwrapped_near_rows']==len(local['complete_near_rows'])==84
assert rootverify['far_controls']==len(local['complete_far_rows'])==4
assert rootverify['synthetic_pair_cases']==len(local['complete_synthetic_cases'])==180
assert rootverify['executions']==comparisons['author_execution_bindings']
assert rootverify['verifier_sha256']==sha(AUTHOR/'verify_native_pair_evidence.py')
author_review=read(AUTHOR/'ROOT_REVIEW.json')
assert author_review['note_sha256']==sha(AUTHOR/'NATIVE_ONE_PAIR_SPECTRAL_EDGE_ROOT.md')
executions=[]
for label,script in [('post_freeze','post_freeze_sources.py'),('post_compare','post_compare.py')]:
    receipt=read(HERE/(label+'.execution.json'));assert receipt['exit_code']==0
    assert receipt['script_sha256']==sha(HERE/script)
    for stream in ('stdout','stderr'):
        p=HERE/(label+'.'+stream+'.txt')
        assert sha(p)==receipt[stream+'_sha256'] and p.stat().st_size==receipt[stream+'_bytes']
    assert receipt['stderr_bytes']==0
    executions.append(dict(label=label,receipt_sha256=sha(HERE/(label+'.execution.json')),
        elapsed_seconds=receipt['elapsed_seconds'],exit_code=0,stderr_bytes=0))
text=(HERE/'POST.md').read_text()
assert text.count(r'\(')==text.count(r'\)') and text.count(r'\[')==text.count(r'\]')
result=dict(created_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(Path(__file__)),
    POST_sha256=sha(HERE/'POST.md'),POST_comparison_sha256=sha(HERE/'POST_COMPARISON_RESULTS.json'),
    exact_author_origins_and_procedural_snapshots=len(source_pins['sources']),
    unchanged_PRE_members=len(preseal['members']),own_execution_bindings=executions,
    numerical_metadata_and_prose=numerical,
    complete_comparison_summary_projection_matches=True,
    original_author_receipts_unchanged=True,all_scientific_parents_unchanged=True,
    author_programs_executed_or_imported=False,all_checks_satisfied=True,
    scope='Exact bindings and numerical prose checks. Recorded floating residuals are author diagnostics; no audit or new eigenvalue run.')
with (HERE/'POST_FINAL_VERIFICATION.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
print(json.dumps(result,indent=2))
