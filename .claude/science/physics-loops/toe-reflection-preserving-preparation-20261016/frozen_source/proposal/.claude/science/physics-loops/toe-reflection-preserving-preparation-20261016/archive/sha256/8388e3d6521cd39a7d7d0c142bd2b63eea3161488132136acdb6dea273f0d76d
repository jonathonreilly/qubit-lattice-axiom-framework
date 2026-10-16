"""Metadata/source inspection only; no original scientific program is imported."""
from pathlib import Path
import hashlib,json,runpy,sys
D=Path(sys.argv[1]).resolve();P=D/'proposal';PK='.claude/science/physics-loops/toe-interacting-preparation-control-work-20261016'
NOTE='docs/INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md'
script=P/'scripts/interacting_preparation_control_work_2026_10_16.py'
api=runpy.run_path(str(script),run_name='source_metadata_inspection')
read=lambda rel:(P/rel).read_bytes()
checked=api['verify_payload'](read)
sha=lambda b:hashlib.sha256(b).hexdigest()
maps=json.loads(read(PK+'/BODY_MAP.json'))['bodies'];note=read(NOTE)
for row in maps:
 original=(D.parent/row['source']).read_bytes()
 assert note[row['start_byte_inclusive']:row['end_byte_exclusive']]==original
 assert sha(original)==row['sha256']
source_rows=json.loads(read(PK+'/SOURCE_MANIFEST.json'))['sources'];source={r['source']:r for r in source_rows}
def expect_rejected(label,reader,phase='payload'):
 try:
  if phase=='payload':api['verify_payload'](reader)
  else:api['verify_actual_binding'](reader,checked)
 except (ValueError,FileNotFoundError) as exc:return {'name':label,'rejected':True,'reason':str(exc)}
 raise AssertionError('Metadata mutation was accepted: '+label)
mutants=[]
mutants.append(expect_rejected('unbound_canonical_refusal',read,'binding'))
targets={
 'altered_original_body':NOTE,
 'altered_fault_qualification':source['interacting_local_fault_work_root_review/FINAL_QUALIFICATIONS.md']['recovery_path'],
 'missing_actual_scientific_source':source['interacting_ramp_bridge_exposed_check/runs/ramp_interface/SOURCE_AT_LAUNCH.py']['recovery_path'],
 'missing_preserved_failed_metadata':source['interacting_local_fault_work_candidate/METADATA_CHECK.stderr.txt']['recovery_path'],
 'missing_root_actual_acceptance_source':source['runs/interacting_preparation_acceptance/executed_source.py']['recovery_path'],
 'missing_parent_attachment':source['publication_integration/inhomogeneous_comb/ATTACHMENT.json']['recovery_path'],
}
for name,path in targets.items():
 def mutant(rel,path=path,name=name):
  if rel==path:
   if name.startswith('missing'):raise FileNotFoundError('Scoped metadata removal: '+name)
   if name=='altered_original_body':
    body=bytearray(read(rel));i=maps[0]['start_byte_inclusive']+10;body[i]^=1;return bytes(body)
   return read(rel)+b'\nSCOPED METADATA MUTANT\n'
  return read(rel)
 mutants.append(expect_rejected(name,mutant))
result={'kind':'source_integrity_and_metadata_mutants_only','checked':checked,'direct_original_interval_comparison':True,'scoped_metadata_mutants':mutants,'mathematics_tested_by_this_execution':False,'historical_scientific_replays':0,'canonical_primary_execution':None,'root_source_wrapper_review':None}
(D/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
