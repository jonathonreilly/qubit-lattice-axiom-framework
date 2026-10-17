"""Focused deterministic publication checks, without changing cached inputs."""
from pathlib import Path
import ast
import copy
import datetime
import hashlib
import gzip
import json
import py_compile
import re
import subprocess
import sys

sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent
W=D.parents[1]/'correlation_worktree'
Q=W/'.claude/science/physics-loops/toe-structural-coefficient-box-20261017'
E=Q/'evidence'
F=W/'outputs/structural_coefficient_box_2026_10_17_inputs'
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
import runner_cache
import build_citation_graph
import forensic_evidence_readiness
import no_go_discipline_gate

primary='scripts/structural_coefficient_box_2026_10_17.py'
helper='scripts/structural_coefficient_box_check_2026_10_17.py'
note='docs/STRUCTURAL_COEFFICIENT_BOX_BOUNDED_THEOREM_NOTE_2026-10-17.md'
claim='structural_coefficient_box_bounded_theorem_note_2026-10-17'
output='outputs/structural_coefficient_box_2026_10_17.json'
cache_rel='logs/runner-cache/structural_coefficient_box_2026_10_17.txt'
graph_rel='docs/audit/data/citation_graph_manifest.json'
def digest(p):
    b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')

manifest=json.loads((F/'ARTIFACT_MANIFEST.json').read_text())
rows=manifest['files']; assert len(rows)==47
for row in rows:
    p=W/row['path']; assert p.is_file() and not p.is_symlink(),row['path']
    assert digest(p)=={k:row[k] for k in ('bytes','sha256')},row['path']
assert {str(p.relative_to(W)) for p in F.rglob('*') if p.is_file()}=={r['path'] for r in rows}|{str((F/'ARTIFACT_MANIFEST.json').relative_to(W))}

s=json.loads((Q/'SOURCE_MANIFEST.json').read_text())
nb=(W/note).read_bytes(); frozen=(W/s['candidate']['path']).read_bytes()
assert digest(W/note)=={k:s['note'][k] for k in ('bytes','sha256')}
assert nb[s['body_offset_zero_based']:s['body_offset_zero_based']+s['body_bytes']]==frozen
assert hashlib.sha256(frozen).hexdigest()==s['candidate_body_sha256']
adapt=json.loads((E/'METADATA_ADAPTATION.json').read_text())
assert adapt['all_other_calculation_statements_ast_identical'] and adapt['frozen_argument_byte_identical']
assert len(adapt['metadata_edits'])==2
for field,rel in [('canonical_primary',primary),('canonical_helper',helper)]:
    assert digest(W/rel)=={k:s[field][k] for k in ('bytes','sha256')}=={k:adapt[field][k] for k in ('bytes','sha256')}
format_record=json.loads((E/'WHITESPACE_ADAPTATION.json').read_text())
for row in format_record['files']:
    assert digest(W/row['path'])==row['after']
    current_ast=ast.dump(ast.parse((W/row['path']).read_text()),include_attributes=False)
    assert hashlib.sha256(current_ast.encode()).hexdigest()==row['ast_sha256']
    assert row['complete_module_ast_unchanged']

result=json.loads((W/output).read_text())
declared=runner_cache.declared_input_paths(W/primary)
assert len(declared)==50 and set(declared)==set(result['input_sha256'])
for rel,h in result['input_sha256'].items():assert digest(W/rel)['sha256']==h,rel
checks=result['independent']['checks']
assert len(checks)==157 and all(v is True for v in checks.values())
assert result['actual_combined_process_limits']['cpu_soft_hard_seconds']==[60,60]
assert result['actual_combined_process_limits']['external_wall_cap_seconds']==60
assert result['author']['limits']['historical_source_run_limits']=={'cpu_cap_seconds':10,'external_wall_cap_seconds':20}
assert result['independent']['resources']['historical_source_run_limits']=={'cpu_cap_seconds':45,'external_wall_cap_seconds':60}
for entry in (result['author']['limits'],result['independent']['resources']):
    assert entry['actual_combined_process_limits']=={'cpu_cap_seconds':60,'external_wall_cap_seconds':60}

helpers=build_citation_graph.resolve_helper_runner_paths(primary)
assert helpers==[helper],helpers
row={'claim_id':claim,'note_path':note,'runner_path':primary,'helper_runner_paths':helpers,'claim_type':'bounded_theorem'}
issue=forensic_evidence_readiness.cached_row_readiness_issue(row,{claim:row},W)
assert issue is None,issue
assert runner_cache.cache_status(primary)=='fresh'
execution=json.loads((Q/'CANONICAL_EXECUTION.json').read_text())
assert execution['status']=='ok' and execution['exit_code']==0
assert digest(W/cache_rel)==execution['cache'] and digest(W/output)==execution['canonical_result']
assert digest(W/primary)==execution['runner_at_receipt']
for stream in ('stdout','stderr'):assert digest(E/('canonical.'+stream))==execution[stream]
compiled=[primary,helper]+[str(p.relative_to(W)) for root in (F,Q) for p in root.rglob('*.py')]
for rel in compiled:
    cfile=D/(hashlib.sha256(rel.encode()).hexdigest()+'.pyc')
    py_compile.compile(str(W/rel),cfile=str(cfile),doraise=True)
old_result=json.loads((E/'canonical_attempt_1/canonical_result.json').read_text())
new_result=copy.deepcopy(result)
assert [k for k in old_result['input_sha256'] if old_result['input_sha256'][k]!=new_result['input_sha256'][k]]==[note]
for obj in (old_result,new_result):
    obj['input_sha256'].pop(note)
    obj['author'].pop('elapsed_seconds')
    obj['independent']['resources'].pop('elapsed_seconds')
    obj['actual_combined_process_limits'].pop('elapsed_seconds')
assert old_result==new_result
repeat=json.loads((E/'CANONICAL_REPEAT_COMPARISON.json').read_text())
assert hashlib.sha256(json.dumps(old_result,sort_keys=True,separators=(',',':')).encode()).hexdigest()==repeat['compared_payload_sha256']
first_receipt=json.loads((E/'canonical_attempt_1/CANONICAL_EXECUTION.json').read_text())
first_cache=gzip.decompress((E/'canonical_attempt_1/canonical_cache.txt.gz').read_bytes())
assert {'bytes':len(first_cache),'sha256':hashlib.sha256(first_cache).hexdigest()}==first_receipt['cache']
assert digest(E/'canonical_attempt_1/canonical_result.json')==first_receipt['canonical_result']
assert digest(E/'canonical_attempt_1/note.md')==json.loads((E/'NOTE_REFRESH.json').read_text())['old_note']

mut=json.loads((E/'mutations/RESULTS.json').read_text());assert len(mut['cases'])==8
plan=json.loads((E/'mutations/PLAN.json').read_text())
assert digest(E/'mutations/PLAN.json')==mut['plan']
before_format={Path(r['path']).name:r['before'] for r in format_record['files']}
assert plan['source_pins']['author']==before_format[Path(primary).name]
assert plan['source_pins']['independent']==before_format[Path(helper).name]
for case in mut['cases']:
    folder=E/'mutations'/case['name']
    assert case['exit_code']==1 and not case['timed_out'] and case['scientific_assertion_rejected']
    mutated=gzip.decompress((folder/'mutated.py.gz').read_bytes())
    assert {'bytes':len(mutated),'sha256':hashlib.sha256(mutated).hexdigest()}==case['source']
    ast.parse(mutated.decode())
    for stream in ('stdout','stderr'):assert digest(folder/stream)==case[stream]
    stderr=(folder/'stderr').read_text()
    assert 'AssertionError' in stderr and case['expected_scientific_assertion'] in stderr

graph=json.loads((E/'GRAPH_VERIFICATION.json').read_text())
assert graph['added']==[claim] and not graph['removed'] and not graph['rewired']
assert graph['new_edges']==[{'from':claim,'to':'two_body_autonomous_halt_bounded_theorem_note_2026-10-17'}]
refresh=json.loads((E/'NOTE_REFRESH.json').read_text())
assert graph['new_node']['note_hash']==refresh['old_note']['sha256']
assert refresh['new_note']==digest(W/note)
assert refresh['all_graph_fields_except_note_hash_identical']
assert refresh['graph_extraction_before']==refresh['graph_extraction_after']=={k:v for k,v in graph['new_node'].items() if k!='note_hash'}
assert refresh['graph_builder_sha256']==digest(W/'docs/audit/scripts/build_citation_graph.py')['sha256']
raw,hint=build_citation_graph.extract_claim_type_hint(nb.decode())
current_surface={'claim_id':build_citation_graph.claim_id_from_path(W/note),'path':note,
                 'title':build_citation_graph.extract_title(nb.decode()),
                 'claim_type_author_hint_raw':raw,'claim_type_author_hint':hint,
                 'claim_type_seed_hint':hint or build_citation_graph.extract_legacy_status_claim_type(nb.decode()),
                 'runner_path':build_citation_graph.extract_runner(nb.decode(),Path(note).relative_to('docs').as_posix()),
                 'helper_runner_paths':helpers,
                 'deps':[build_citation_graph.claim_id_from_path(x) for x in build_citation_graph.extract_citations(nb.decode(),W/note)]}
assert current_surface==refresh['graph_extraction_after']
assert graph['manifest_sha256']==digest(W/graph_rel)['sha256']
assert len(graph['executions'])==2 and all(r['exit_code']==0 for r in graph['executions'])
failed=json.loads((E/'graph_attempt_1/GRAPH_EXECUTIONS.json').read_text())
assert len(failed)==1 and failed[0]['exit_code'] is None and failed[0]['wall_cap_seconds']==60
no_go=no_go_discipline_gate.source_requires_no_go_discipline(note,nb.decode(),'bounded_theorem')
assert not no_go,no_go

texts=[W/note,*sorted(Q.glob('*.md'))]
vocab=subprocess.run([sys.executable,'scripts/vocab_lint.py','--report-only','--report-path',str(E/'VOCAB_REPORT.json'),*[str(p.relative_to(W)) for p in texts],primary,helper],cwd=W,capture_output=True,text=True,timeout=20)
(E/'vocab.stdout').write_text(vocab.stdout);(E/'vocab.stderr').write_text(vocab.stderr)
assert vocab.returncode==0 and '0 files with violations' in vocab.stdout,vocab.stdout+vocab.stderr

def outside_code(text):
    lines=[];fence=None
    for line in text.splitlines():
        found=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line)
        if fence:
            if found and found[1][0]==fence[0] and len(found[1])>=len(fence) and not found[2].strip():fence=None
            continue
        if found:fence=found[1];continue
        lines.append(line)
    assert fence is None
    return re.sub(r'(`+).*?\1','','\n'.join(lines))
# This publication evidence map intentionally excludes itself and final
# PUBLISH_CHECKS, preventing recursive hashes. All checked source/output
# identities remain in the map and the final ready-path list.
evidence_rows=[]
for p in sorted(E.rglob('*')):
    if p.is_file():evidence_rows.append({'path':str(p.relative_to(W)),**digest(p)})
write(Q/'PUBLICATION_EVIDENCE.json',{'scope':'Publication receipts outside the declared canonical input closure; not additional theorem premises.','files':evidence_rows})
links=[];pending_links=[]
for p in texts:
    for target in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)',outside_code(p.read_text())):
        if target.startswith(('http:','https:','#')):continue
        raw=p.parent/target.split('#')[0]
        assert not raw.is_symlink(),(p,target)
        dest=raw.resolve()
        if not dest.is_file():
            assert dest==Q/'ROOT_WRAPPER_REVIEW.json',(p,target)
            pending_links.append({'source':str(p.relative_to(W)),'target':str(dest.relative_to(W)),
                                  'status':'Root-owned record explicitly requested and to be written by root after this packet completion; absent at this check.'})
            continue
        links.append({'source':str(p.relative_to(W)),'target':str(dest.relative_to(W))})

# Check the untracked authored surfaces as diffs too; plain git diff does not.
whitespace=[]
check_paths=[W/note,W/primary,W/helper,W/output,W/cache_rel,W/graph_rel,
             *[p for root in (F,Q) for p in root.rglob('*') if p.is_file()]]
for rel in sorted({str(p.relative_to(W)) for p in check_paths}):
    proc=subprocess.run(['git','diff','--no-index','--check','/dev/null',rel],cwd=W,capture_output=True,text=True)
    assert not proc.stdout and not proc.stderr,(rel,proc.stdout,proc.stderr)
    whitespace.append(rel)
tracked=subprocess.run(['git','diff','--check'],cwd=W,capture_output=True,text=True)
assert tracked.returncode==0,tracked.stdout+tracked.stderr
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip()
branch=subprocess.check_output(['git','branch','--show-current'],cwd=W,text=True).strip()
assert head=='0e8375354c42963234cc4b15b14ab6bb553c713d'
assert branch=='physics-loop/toe-structural-coefficient-box-20261017'
staged=subprocess.check_output(['git','diff','--cached','--name-only'],cwd=W,text=True)
assert not staged,staged
root_review=json.loads((Q/'ROOT_WRAPPER_REVIEW.json').read_text())
assert digest(Q/'ROOT_WRAPPER_REVIEW.json')['sha256']=='9f943f6d46cc3621082f84bfc7be5e843955398a601c42a8adaf8a05e2b3f738'
for key,rel in [('note',note),('primary',primary),('helper',helper)]:
    assert digest(W/rel)=={k:root_review[key][k] for k in ('bytes','sha256')}

record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status':'Focused publication packet checked and root wrapper/implementation approval recorded for conditional publication. All paths unstaged; publication and landing remain separate.',
        'scope':'Deterministic packaging and actual finite exact execution. Source theorem acceptance is reused; no new independent science verdict.',
        'parent_head':head,'branch':branch,'artifact_hashes_verified':47,'declared_input_count':50,
        'frozen_argument_byte_identical':True,'metadata_only_calculation_ast_adaptation':True,
        'all_other_calculation_statements_ast_identical':True,'whitespace_complete_ast_preserved':True,
        'helper_discovery':helpers,'independent_check_count':157,'deterministic_readiness_issue':issue,
        'cache_status':'fresh','canonical_execution':execution,
        'canonical_identities':{rel:digest(W/rel) for rel in (note,primary,helper,output,cache_rel,graph_rel)},
        'canonical_result_input_hashes':result['input_sha256'],'mutation_cases_and_archived_streams':8,
        'graph':graph,'graph_after_note_refresh':refresh,'first_graph_timeout_retained':True,'vocabulary_violating_files':0,
        'no_go_gate_trigger':no_go,'compiled_sources':compiled,'regular_local_links':links,'pending_root_owned_links':pending_links,
        'publication_file_whitespace_checked':whitespace,'retained_whitespace_exceptions':[],
        'tracked_diff_whitespace_exit_code':tracked.returncode,
        'pr9662_verified_inventory':json.loads((E/'PR9662_VERIFICATION.json').read_text()),
        'source_manifest':digest(Q/'SOURCE_MANIFEST.json'),'publication_evidence_map':digest(Q/'PUBLICATION_EVIDENCE.json'),
        'root_wrapper_review':digest(Q/'ROOT_WRAPPER_REVIEW.json'),
        'editable_prompt_files_changed':[],'staged_paths':[],
        'remaining_gates':['Root final staged-path review and regular child PR preparation','Parent PR9661 landing or inclusion in integrated delta','Shared exact integrated-current-main pipeline, strict lint and changed-evidence checks','Independent retained audit'],
        'post_execution_input_changes':False,
        'canonical_repeat':json.loads((E/'CANONICAL_REPEAT_COMPARISON.json').read_text())}
record['publication_envelope_repair']=json.loads((E/'PACKET_REPAIR.json').read_text())
write(Q/'PUBLISH_CHECKS.json',record);write(D/'FOCUSED_VERIFICATION.json',record)
assert runner_cache.cache_status(primary)=='fresh'

ready=[W/note,W/primary,W/helper,W/output,W/cache_rel,W/graph_rel,*[p for p in F.rglob('*') if p.is_file()],*[p for p in Q.rglob('*') if p.is_file()]]
ready=sorted(set(ready));ready_rows=[{'path':str(p.relative_to(W)),**digest(p)} for p in ready]
write(D/'READY_PATHS.json',{'scope':'Exact unstaged publication paths; generated citation_graph.json and unrelated paths excluded.','parent_head':head,'files':ready_rows,'file_count':len(ready_rows),'pending_root_owned_paths':[x['target'] for x in pending_links]})
print(json.dumps({k:record[k] for k in ['status','artifact_hashes_verified','declared_input_count','independent_check_count','helper_discovery','cache_status','mutation_cases_and_archived_streams','vocabulary_violating_files','deterministic_readiness_issue','no_go_gate_trigger','post_execution_input_changes']},indent=2))
print(json.dumps({'ready_paths':len(ready_rows),'ready_map':digest(D/'READY_PATHS.json')},indent=2))
