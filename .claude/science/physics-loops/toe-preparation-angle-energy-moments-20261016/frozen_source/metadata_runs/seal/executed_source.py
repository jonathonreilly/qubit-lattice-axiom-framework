"""Verify completed metadata receipts; the parent recorder seals after this exits."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,sys
D=Path(sys.argv[1]).resolve();P=D/'proposal';PK='.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def dump(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
for mode in ['build','inspection']:
 d=D/'metadata_runs'/mode;r=json.loads((d/'EXECUTION.json').read_text());l=json.loads((d/'LAUNCH.json').read_text())
 assert all(r[k]==v for k,v in l.items())
 assert r['exit_code']==0 and r['timed_out'] is False and r['scientific_programs_run']==0 and r['inputs_unchanged_after_run'] is True
 for key in ['child_source_at_launch','original_source_at_launch','source_capture','recorder_at_launch','input_identities_at_launch','stdout','stderr']:
  assert pin(Path(r[key]['path']))==r[key],(mode,key)
 assert r['argv'][2]==r['child_source_at_launch']['path']==r['source_capture']['path']
 assert r['original_source_at_launch']['sha256']==r['child_source_at_launch']['sha256']
 assert (d/'stderr').read_bytes()==b''
manifest=json.loads((P/PK/'INPUT_MANIFEST.json').read_text())
for row in manifest['inputs']:
 b=(P/row['path']).read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
maps=json.loads((P/PK/'BODY_MAP.json').read_text())['bodies']
template=(D/'primary_template.py').read_text();generated=template.replace('__MANIFEST_SHA256__',sha((P/PK/'INPUT_MANIFEST.json').read_bytes())).replace('__AUDIT_INPUT_PATHS__',repr([r['path'] for r in manifest['inputs']]+[PK+'/INPUT_MANIFEST.json'])).replace('__EXPECTED_BODIES__',repr({r['name']:r['sha256'] for r in maps}))
assert (P/'scripts/preparation_angle_energy_moments_2026_10_16.py').read_bytes()==generated.encode()
v=json.loads((D/'VERIFICATION.json').read_text())
assert v['mathematics_tested_by_this_execution'] is False and all(x['rejected'] for x in v['scoped_metadata_mutants']+v['direct_receipt_predicate_mutants'])
assert v==json.loads((D/'metadata_runs/inspection/stdout').read_text())
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 text=(D/name).read_text();ast.parse(text)
 assert not any(line.rstrip()!=line for line in text.splitlines()),name
assert (D/'ROOT_READ_GUIDE.md').is_file() and (D/'CODE_REUSE_MAP.json').is_file() and (D/'CODE_FULL_DIFF.patch').is_file()
result={'utc':utc(),'kind':'completed_metadata_verification_before_parent_recorded_seal','proposal_inputs':len(manifest['inputs']),'immutable_bodies':len(maps),'packaging_metadata_receipts_verified':['build','inspection'],'metadata_mutants_rejected':len(v['scoped_metadata_mutants'])+len(v['direct_receipt_predicate_mutants']),'generated_primary_matches_template':True,'scientific_programs_run':0,'canonical_primary_executed':False,'root_wrapper_review':None}
dump(D/'SEAL_RESULT.json',result);print(json.dumps(result,indent=2))
