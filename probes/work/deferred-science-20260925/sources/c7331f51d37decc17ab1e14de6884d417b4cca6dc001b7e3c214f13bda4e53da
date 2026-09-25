#!/usr/bin/env python3
"""Bind the final formatting-corrected PRE to unchanged scientific evidence."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name):return json.loads((HERE/name).read_text())
verification=read('PRE_VERIFICATION_RESULTS.json')
assert verification==read('verify.stdout.txt') and verification['all_checks_satisfied']
before=HERE/'history/PRE_before_math_delimiter_repair.md';after=HERE/'PRE.md'
repair=read('MATH_DELIMITER_REPAIR.json')
assert repair==read('math_repair.stdout.txt')
assert sha(before)==repair['before_sha256']==verification['PRE_sha256']
assert sha(after)==repair['after_sha256']
canonical=lambda s:s.replace(r'\(', '(').replace(r'\)', ')')
assert canonical(before.read_text())==canonical(after.read_text())
assert sha(HERE/'history/MATH_DELIMITER_REPAIR.diff')==repair['complete_diff_sha256']
assert after.read_text().count(r'\(')==after.read_text().count(r'\)')
assert after.read_text().count(r'\[')==after.read_text().count(r'\]')
executions=[]
for label,script in [('freeze','freeze_sources.py'),('occupation','occupation_spectrum.py'),
 ('primitive','primitive_colored_control.py'),('verify','verify_pre.py'),
 ('math_repair','repair_inline_math.py')]:
    receipt=read(label+'.execution.json')
    assert receipt['exit_code']==0 and receipt['script_sha256']==sha(HERE/script)
    for stream in ('stdout','stderr'):
        p=HERE/(label+'.'+stream+'.txt')
        assert sha(p)==receipt[stream+'_sha256'] and p.stat().st_size==receipt[stream+'_bytes']
    assert receipt['stderr_bytes']==0
    executions.append(dict(label=label,receipt_sha256=sha(HERE/(label+'.execution.json')),
                           elapsed_seconds=receipt['elapsed_seconds'],exit_code=0,stderr_bytes=0))
for source in read('SOURCE_PINS.json')['sources']:
    assert sha(Path(source['origin']))==sha(HERE/source['frozen_path'])==source['sha256']
for name,expected in verification['full_result_hashes'].items():assert sha(HERE/name)==expected
data=dict(created_utc=datetime.now(timezone.utc).isoformat(),scope=__doc__,
 source_sha256=sha(Path(__file__)),final_PRE_sha256=sha(after),
 verified_original_PRE_sha256=sha(before),formatting_only_identity=True,
 scientific_verification_sha256=sha(HERE/'PRE_VERIFICATION_RESULTS.json'),
 scientific_controls_unchanged=True,all_sources_refreshed_unchanged=True,
 complete_direct_Gram_representative_rows=sum(r['complete_direct_Gram_rows'] for r in verification['occupation']),
 complete_exact_Gram_sparse_entries=sum(r['exact_sparse_entries'] for r in verification['occupation']),
 complete_primitive_rows=sum(r['all_primitive_rows_consumed'] for r in verification['primitive']),
 total_primitive_paths=sum(r['primitive_path_count'] for r in verification['primitive']),
 original_resolved_birth_branches_rechecked=sum(r['resolved_birth_branches_rechecked'] for r in verification['primitive']),
 execution_bindings=executions,author_disclosure_received=False,
 all_checks_satisfied=True,authority_limit='Evidence binding only; no audit verdict')
with (HERE/'FINAL_BINDINGS.json').open('x') as f:json.dump(data,f,indent=2);f.write('\n')
print(json.dumps(data,indent=2))
