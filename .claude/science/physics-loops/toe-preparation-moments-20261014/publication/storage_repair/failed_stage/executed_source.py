import json,shutil,sys
from pathlib import Path
from common import N,W,pin,check_pin,read_json,write_json,run,git_read,stage_exact,now,require_campaign_active
D=N/'publication_integration/preparation';c=read_json(N/'preparation_moment_publication_components/INPUTS.json');packet=c['packet'];prepared=read_json(D/'PREPARED_SOURCE.json');extra=read_json(D/'PUBLICATION_EVIDENCE_PACKAGE.json')
require_campaign_active();assert git_read('rev-parse','HEAD').decode().strip()==prepared['base_head']
for name in ['HANDOFF.md','TRACE_GATE.md','REVIEW_HISTORY.md']:
 target=W/packet/name;assert not target.exists();shutil.copyfile(D/name,target)
paths=sorted(set(prepared['installed_paths'])|set(extra['files'])|{packet+'/'+x for x in ['HANDOFF.md','TRACE_GATE.md','REVIEW_HISTORY.md']}|{'docs/audit/data/citation_graph_manifest.json','logs/runner-cache/'+Path(c['helper']).stem+'.txt'})
before={name:pin(W/name) for name in paths}
for flag,label in [('--fix','vocabulary_fix'),('--report-only','vocabulary_report')]:run(D,label,['python3','scripts/vocab_lint.py',flag,*paths])
for name,expected in before.items():check_pin(W/name,expected)
python_files=[name for name in paths if name.endswith('.py')];run(D,'python_compile',['python3','-m','py_compile',*python_files])
sys.path.insert(0,str(W/'scripts'));import runner_cache
assert runner_cache.cache_status(c['helper'])=='fresh'
stage_exact(paths)
status=git_read('status','--porcelain','-z','--untracked-files=all')
assert {row[3:].decode() for row in status.split(b'\0') if row}==set(paths)
compat=json.loads(run(D,'focused_compatibility',['python3','docs/audit/scripts/check_changed_audit_evidence.py','--base','HEAD','--include-worktree','--json']))
assert compat['failures']==[] and compat['control_failures']==[]
assert compat['changed_path_count']==len(paths)
summary={'utc':now().isoformat(),'base':prepared['base_head'],'paths':len(paths),'python_files':len(python_files),'vocabulary_fix_and_report_exit':0,'vocabulary_source_drift':False,'python_compile_exit':0,'canonical_cache_status':'fresh','graph_delta':{'nodes':1,'edges':1,'old_complete_nodes_preserved':7114,'old_complete_edges_preserved':16053},'focused_existing_ledger_compatibility':compat,'mathematical_predicates_executed':0,'combined_current_main_validation':'pending separate landing review','independent_retained_audit':'not performed','editable_prompts_changed':[]}
review=W/packet/'REVIEW_HISTORY.md'
with review.open('a') as stream:
 stream.write('\nActual focused repository check snapshot:\n\n```json\n'+json.dumps(summary,indent=2)+'\n```\n\nAn empty checked list means no existing scientific claim was audited. The changed-path count includes this existing review file; this final append changes only its explanatory result record. Scientific source and canonical inputs remain byte-identical.\n')
run(D,'vocabulary_final_review',['python3','scripts/vocab_lint.py','--fix',packet+'/REVIEW_HISTORY.md'])
run(D,'vocabulary_final_review_report',['python3','scripts/vocab_lint.py','--report-only',packet+'/REVIEW_HISTORY.md'])
for name,expected in before.items():
 if name!=packet+'/REVIEW_HISTORY.md':check_pin(W/name,expected)
staged=stage_exact(paths)
for name,expected in staged.items():
 import hashlib
 assert hashlib.sha256(git_read('show',':'+name)).hexdigest()==expected['sha256']
assert runner_cache.cache_status(c['helper'])=='fresh'
write_json(D/'STAGED_VERIFICATION.json',dict(summary,staged_pins=staged,review_record=pin(review)))
print(summary)
