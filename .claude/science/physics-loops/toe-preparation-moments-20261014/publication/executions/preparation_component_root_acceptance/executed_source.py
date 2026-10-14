import ast,hashlib,json
from pathlib import Path
from common import N,pin,check_pin,read_json,write_json,now
P=N/'preparation_moment_publication_components';D=N/'publication_integration/preparation'
f=read_json(P/'FINAL_FREEZE.json')
assert pin(P/'FINAL_FREEZE.json')['sha256']=='558e6691fa872f1b53cba5ffdcbf571bb1e44ebad12dff275f34a66575163839'
for row in f['members']:check_pin(P/row['path'],row)
assert {str(p.relative_to(P)) for p in P.rglob('*') if p.is_file()}=={r['path'] for r in f['members']}|{'FINAL_FREEZE.json'}
m=read_json(P/'review_maps/PROGRAM_AND_FRAMING_MAP.json');programs={}
for item in m['programs']:
 current=Path(item['current']['path']);check_pin(current,item['current']);raw=current.read_bytes();lines=raw.splitlines(keepends=True);ast.parse(raw)
 for row in item['functions']+item['current_module_statements']:
  segment=raw[row['byte_start_0']:row['byte_end_exclusive']]
  assert segment==b''.join(lines[row['start_line_1']-1:row['end_line_1']])
  assert len(segment)==row['bytes'] and hashlib.sha256(segment).hexdigest()==row['sha256']
 if item['previous']:check_pin(item['previous']['path'],item['previous'])
 check_pin(P/item['complete_diff'],item['complete_diff_identity'])
 programs[item['label']]=pin(current)
for row in m['framing']:
 check_pin(row['prior']['path'],row['prior']);check_pin(P/row['current']['path'],row['current']);check_pin(P/row['diff']['path'],row['diff'])
for row in f['recorded_actual_runs']:
 check_pin(P/row['receipt']['path'],row['receipt']);r=read_json(P/row['receipt']['path'])
 assert r['exit_code']==0 and r['source_unchanged'] and r['source_sha256_before']==r['source_sha256_after']
 assert pin((P/row['receipt']['path']).parent/'executed_source.py')['sha256']==r['source_sha256_before']
 for key in ('stdout','stderr'):check_pin(P/r[key]['path'],r[key])
root_run=N/'runs/preparation_components_source_check';r=read_json(root_run/'EXECUTION.json');assert r['exit_code']==0
check=read_json(root_run/'stdout');assert check['live_origins_compared']==616 and check['mathematical_predicates']==0
result={'utc':now().isoformat(),'component_review_complete':True,'freeze':pin(P/'FINAL_FREEZE.json'),'scope':'Source-only composition acceptance. No new mathematical check, canonical execution, retained audit, or future publication is asserted.',
 'fully_reviewed_programs':programs,'program_map':pin(P/'review_maps/PROGRAM_AND_FRAMING_MAP.json'),'source_replay':pin(root_run/'EXECUTION.json'),
 'review_coverage':['Complete current builder initially read; final write/build functions and complete changed module statements read, all other builder functions reused at identity.','Complete source checker and primary functional template read; generated literal-only substitutions independently reproduced by unchanged checker.','Complete recorder, repair, history checker, mapper and freezer read. All actual recorded streams and both pre-child failures inspected.','Complete current four framing fragments/five sidecars previously read; final one-line scalar correction read. Complete unchanged generic, sharper and chain arguments and necessary premises reuse recorded analytic and source acceptance.','All 511 members checked; current 411 payload, 616 origin records and 482 inner aliases verified. All mapped current function/global segments and prior/current source pins verified.','Large inventory data are deterministically verified; prior truncated metadata displays are not asserted as full semantic reads.'],
 'scientific_limits':['Conditional supplied preparation, full old/reference marginal control, installed same K/scalar, charged variance and penalty loads.','Restricted reserved-strip chain only; no native realization, common cap, optimality or broad no-go.','Generic section4 uses complete chain Appendix; sharper depends on be8; only be8 is an external theorem edge.'],
 'new_math_executions':0,'editable_prompts_changed':[],'remaining':['Fresh source/parent guards','Root bound derivative and integrity controls','Canonical cache and graph preservation','Focused compatibility and regular PR']}
write_json(D/'COMPONENT_ROOT_ACCEPTANCE.json',result)
write_json(D/'PREPARE_DRIVER_REVIEW.json',{'utc':now().isoformat(),'approved_for_root_execution':True,'source':pin(N/'publication_integration/prepare_preparation.py'),'common':pin(N/'publication_integration/common.py'),'component_review':pin(D/'COMPONENT_ROOT_ACCEPTANCE.json'),'review':'Complete root source read. Exact clean branch/HEAD/ref/actual-parent and source membership guards, unique local bound payload, five explicit metadata/helper changes, byte-identical note/proofs, exact fresh-path-only installation. No staging, cache, graph, PR or science execution by this driver.'})
print({'acceptance':pin(D/'COMPONENT_ROOT_ACCEPTANCE.json'),'driver_review':pin(D/'PREPARE_DRIVER_REVIEW.json'),'members':len(f['members']),'program_comparisons':len(programs)})
