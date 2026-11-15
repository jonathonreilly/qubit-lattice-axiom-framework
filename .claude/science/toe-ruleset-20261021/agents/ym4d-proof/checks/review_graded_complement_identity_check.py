#!/usr/bin/env python3
"""Read-only evidence/source identity checks; no mathematical numerical experiment.

Writes only the reviewer's new result. It does not execute or restamp any
producer program, receipt, result or source. Source correction is checked
against its preserved Git object, independently of the author's checker.
"""
from pathlib import Path
import ast, datetime, hashlib, json, re, subprocess
L = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
O = L/'checks/review_graded_complement_identity_check.json'
assert not O.exists(), 'Do not overwrite a frozen verification'
checks=[]
def digest(data): return hashlib.sha256(data).hexdigest()
def identity(path, data=None):
    p=Path(path); data=p.read_bytes() if data is None else data
    return {'path':str(p),'bytes':len(data),'sha256':digest(data)}
def check(record, category, data=None):
    now=identity(record['path'],data)
    assert now['sha256']==record['sha256'], (category,record['path'],record['sha256'],now['sha256'])
    if 'bytes' in record: assert now['bytes']==record['bytes'], (category,record['path'],'bytes')
    now['category']=category;checks.append(now);return now
source=L/'GRADED_COMPLEMENT_ASTRA.md'
correction_path=L/'checks/graded_complement_distance_correction.json'
corr=json.loads(correction_path.read_text())
assert digest(correction_path.read_bytes())=='282e0e1bd399ace20932fcccc0bef91f290a1ee809b290d7749fef603ae7722b'
old=subprocess.check_output(['git','show',corr['base_revision']+':'+str(source)])
new=source.read_bytes()
assert digest(old)==corr['source_before_sha256']=='6201ec6ec1846e205dd1a3d7dd1df1a3bebb9c6bead14874aff40482d2bb0335'
assert digest(new)==corr['source_after_sha256']=='22e30738d5d59adc65c146c7e9fa3bd671462d694a7ae1fe14e73804774e5341'
before=corr['exact_change']['before'].encode();after=corr['exact_change']['after'].encode()
assert old.count(before)==1 and new==old.replace(before,after,1)
initial=json.loads((L/'checks/review_graded_complement_initial_read_manifest.json').read_text())
for record in initial['sources']:
    check(record,'initial independent source unchanged',old if record['path']==str(source) else None)
assert digest((L/'checks/review_graded_complement_initial_findings.md').read_bytes())=='0eda43b5c95efa260e0369536876658fb8f7c60bfa974e412c6666ce210eddce'
assert digest((L/'checks/review_graded_complement_initial_read_manifest.json').read_bytes())=='681da6a5196481322d5f69ba18fd5c0ddca88d498384c61b7b2cb1c18dc9615f'
receipt_path=L/'checks/graded_complement_receipt.json'
receipt=json.loads(receipt_path.read_text())
assert digest(receipt_path.read_bytes())=='234be158e85297de2d7511d0bd5026655ef637c3d4c5165db6863e66d7054d54'
for record in receipt['owned_files']:
    check(record,'original author owned',old if record['path']==str(source) else None)
for record in receipt['input_pins']: check(record,'author input')
for record in receipt['predecessor_receipt_pins']: check(record,'predecessor receipt')
manifest=json.loads((L/'checks/graded_complement_read_manifest.json').read_text())
for packet in manifest['immutable_predecessor_packets']:
    r=json.loads(Path(packet['receipt']['path']).read_text())
    key='artifacts' if 'artifacts' in r else 'owned_files'
    assert len(r[key])==packet['frozen_owned_count']
    assert {(x['path'],x['sha256']) for x in r[key]}=={(x['path'],x['sha256']) for x in packet['frozen_owned_verified']}
    for record in r[key]: check(record,'four preserved predecessor packets')
for name,key in [('covariant_soft_background_receipt.json','files'),('covariant_source_activity_receipt.json','bound_files')]:
    r=json.loads((L/'checks'/name).read_text())
    for record in r[key]: check(record,name)
fr=json.loads((L/'checks/fixed_source_radius_domain_correction.json').read_text())
for record in fr['unchanged_original_artifacts_verified']: check(record,'FR original non-source artifacts')
frc=json.loads((L/'checks/review_fixed_source_radius_domain_confirmation.json').read_text())
for key in ['before','after','current_source','author_correction_receipt','author_correction_note','diff']:
    check(frc[key],'FR affected confirmation')
methodology=[]
rev='01589af3faf806b736c42dc2f3bd625e9edead9f'
for record in manifest['reused_methodology_reads']:
    check(record,'author reused methodology identity')
    if not Path(record['path']).is_absolute():
        data=subprocess.check_output(['git','show',rev+':'+record['path']])
        assert digest(data)==record['sha256'], ('selected main methodology mismatch',record['path'])
        methodology.append(identity(record['path'],data))
syntax=[]
for name in ['graded_complement_freeze.py','graded_complement_freeze_attempt01.py']:
    p=L/'checks'/name;ast.parse(p.read_text(),filename=str(p));syntax.append(str(p))
links=[]
fenced=False
for line in new.decode().splitlines():
    if line.startswith('```'): fenced=not fenced;continue
    if fenced or line.startswith('    '): continue
    for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',line):
        if not target.startswith(('http://','https://')):
            assert (L/target.split('#',1)[0]).exists(),target
            links.append(target)
assert new.endswith(b'\n') and all(line.rstrip()==line for line in new.decode().splitlines())
counts={}
for c in checks:counts[c['category']]=counts.get(c['category'],0)+1
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'PASS: mechanical identities only','head_observed':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'origin_main_observed':subprocess.check_output(['git','rev-parse','origin/main'],text=True).strip(),'original_source_commit':corr['base_revision'],'original_source':identity(source,old),'current_source':identity(source,new),'correction':identity(correction_path),'exact_single_phrase_replacement':True,'initial_independent_findings_unchanged':True,'counts':counts,'checks':checks,'selected_main_methodology_identity_count':len(methodology),'author_programs_syntax_checked_not_executed':syntax,'local_links_checked':links,'new_numerical_experiments':0,'author_files_mutated':0,'scope':'source/receipt identities, preserved old evidence, source correction, syntax and local link existence; not mathematical proof or backend/model attestation'}
with O.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'result':result['result'],'counts':counts,'source_sha256':digest(new),'output':str(O),'output_sha256':digest(O.read_bytes())},indent=2))
