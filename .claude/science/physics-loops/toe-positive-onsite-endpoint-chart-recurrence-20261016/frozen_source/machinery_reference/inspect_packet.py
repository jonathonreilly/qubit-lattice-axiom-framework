"""Metadata/source inspection only; no original scientific program is imported."""
from pathlib import Path
import ast,copy,hashlib,json,runpy,sys
D=Path(sys.argv[1]).resolve();P=D/'proposal';PK='.claude/science/physics-loops/toe-preparation-angle-energy-moments-20261016'
NOTE='docs/PREPARATION_ANGLE_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md'
script=P/'scripts/preparation_angle_energy_moments_2026_10_16.py'
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
mutants=[expect_rejected('unbound_canonical_refusal',read,'binding')]
targets={
 'altered_original_body':NOTE,
 'altered_controlling_qualification':source['preparation_angle_moment_root_review/FINAL_QUALIFICATIONS.md']['recovery_path'],
 'missing_preserved_failed_root_receipt':source['runs/preparation_angle_moments_acceptance/EXECUTION.json']['recovery_path'],
 'missing_successful_v2_source_capture':source['runs/preparation_angle_moments_acceptance_v2/executed_source.py']['recovery_path'],
 'missing_failed_root_full_stderr':source['runs/preparation_angle_moments_acceptance/stderr']['recovery_path'],
 'altered_parent_binding':PK+'/PARENT_BINDING.json',
 'altered_future_approval':PK+'/ACTUAL_BINDING.json',
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
# These tests target receipt predicates directly, independently of manifest hashes.
src=lambda alias:read(source[alias]['recovery_path'])
semantic=[]
for label,run_name,field,value in [
 ('failed_exit_relabelled_success','preparation_angle_moments_acceptance','exit_code',0),
 ('successful_exit_relabelled_failure','preparation_angle_moments_acceptance_v2','exit_code',1),
 ('wrong_original_child_argv','preparation_angle_moments_acceptance_v2','argv',['python3','/wrong.py']),
 ('wrong_capture_location','preparation_angle_moments_acceptance_v2','source_capture',None),
 ('wrong_executed_source_hash','preparation_angle_moments_acceptance_v2','child_source_at_launch',None),
 ('missing_full_stream','preparation_angle_moments_acceptance','missing_stream',None),
]:
 target='runs/'+run_name+'/EXECUTION.json';r=copy.deepcopy(json.loads(src(target)))
 if field=='source_capture':r[field]['path']=r['child_source_at_launch']['path']
 elif field=='child_source_at_launch':r[field]['sha256']='0'*64
 elif field!='missing_stream':r[field]=value
 def altered(alias,r=r,target=target,field=field,run_name=run_name):
  if alias==target:return json.dumps(r).encode()
  if field=='missing_stream' and alias=='runs/'+run_name+'/stderr':raise FileNotFoundError('Removed actual complete stderr')
  return src(alias)
 status,pin=api['ROOT_RUNS'][run_name]
 try:api['verify_root_record'](altered,run_name,status,pin)
 except (ValueError,FileNotFoundError) as exc:semantic.append({'name':label,'rejected':True,'reason':str(exc)})
 else:raise AssertionError('Semantic receipt mutation accepted: '+label)
# Parse every new executable source and compare exact selected baseline functions.
function_rows=[];diffs=[]
import difflib
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 old=(D/'machinery_reference'/name).read_text();new=(D/name).read_text()
 a=ast.parse(old);b=ast.parse(new)
 old_functions={n.name:ast.get_source_segment(old,n) for n in ast.walk(a) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
 for n in ast.walk(b):
  if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
   text=ast.get_source_segment(new,n);previous=old_functions.get(n.name)
   function_rows.append({'file':name,'function':n.name,'first_line':n.lineno,'last_line':n.end_lineno,'source_sha256':sha(text.encode()),'baseline_source_sha256':sha(previous.encode()) if previous is not None else None,'exact_source_reuse':text==previous,'ast_sha256':sha(ast.dump(n,include_attributes=False).encode())})
 diffs.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='machinery_reference/'+name,tofile=name))
ast.parse(script.read_text())
(D/'CODE_REUSE_MAP.json').write_text(json.dumps({'baseline':'inhomogeneous_comb_qualified_publication_draft','scope':'source function identity only; changed globals and source-specific predicates require review','functions':function_rows},indent=2)+'\n')
(D/'CODE_FULL_DIFF.patch').write_text(''.join(diffs))
result={'kind':'source_integrity_and_metadata_mutants_only','checked':checked,'direct_original_interval_comparison':True,'scoped_metadata_mutants':mutants,'direct_receipt_predicate_mutants':semantic,'function_rows':len(function_rows),'exact_source_function_reuses':sum(r['exact_source_reuse'] for r in function_rows),'mathematics_tested_by_this_execution':False,'historical_scientific_replays':0,'canonical_primary_execution':None,'root_source_wrapper_review':None}
(D/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
