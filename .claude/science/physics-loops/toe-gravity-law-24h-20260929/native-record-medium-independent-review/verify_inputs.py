from pathlib import Path
import hashlib,json,subprocess,sys,ast,difflib
from datetime import datetime,timezone
R=Path('/private/tmp/toe-native-record-medium-20260930'); O=Path(__file__).parent
P=Path('.claude/science/physics-loops/native-record-medium-20260930')
BASE='fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7';HEAD='30fddd97f8909d791d4e116c4635b25122487862';TREE='9d573bb2397c8a67803005a281473bee8371c7fd'
def sha(b):return hashlib.sha256(b).hexdigest()
def g(*args):return subprocess.check_output(['git',*args],cwd=R)
def read(p):return (R/p).read_bytes()
def j(p):return json.loads(read(p))
assert not Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929/STOP_REQUESTED.json').exists()
assert g('rev-parse','HEAD').decode().strip()==HEAD
assert g('rev-parse','HEAD^{tree}').decode().strip()==TREE
assert g('rev-parse','origin/main').decode().strip()==BASE
assert not g('status','--porcelain')
author=j(P/'FINAL_BINDINGS.json'); paths=g('diff','--name-only','--no-renames',BASE,HEAD).decode().splitlines()
assert set(paths)=={x['path'] for x in author['files']}|{str(P/'FINAL_BINDINGS.json')}
roles={x['path']:x['role'] for x in author['files']};roles[str(P/'FINAL_BINDINGS.json')]='author final inventory; not evidence of scientific coverage'
rows=[]
for path in paths:
 b=read(path);assert b==g('show',HEAD+':'+path)==g('show',':'+path)
 expected=next((x['sha256'] for x in author['files'] if x['path']==path), '9ed509711ca299af8ed534c9b09e51d98e0a3cbb98398b83fe79a8f76a3e7c5a');assert sha(b)==expected
 if path.endswith('.py'):compile(b,path,'exec')
 if path.endswith('.json'):json.loads(b)
 role=roles[path]
 if '/provenance/' in path or '/historical/' in path: judgment='Preserved unchanged as historical source/check/recovery evidence; not a current autonomous claim, dependency or source-review verdict. Current mathematical content is re-proved in the canonical note; old unchanged-H0 obstruction assertions are not adopted.'
 elif '/mutations/' in path:judgment='Accepted as deliberate failure evidence, not a passing scientific runner; exact mutation and actual assertion traceback verified against canonical source.'
 elif path.startswith('docs/') and 'MANENT_MARKERS' in path:judgment='Accepted as the complete current conditional mathematical argument, all sections independently reconstructed at stated domains.'
 elif path.startswith('scripts/'):judgment='Accepted as seven finite exact controls with disclosed reused builder; analytic proof supplies general quantifiers.'
 elif 'citation_graph_manifest' in path:judgment='Accepted only as topology acknowledgment; one node and two intended edges; prior entries unchanged, no verdict.'
 elif path.startswith('logs/'):judgment='Accepted actual source/input-bound cache; finite controls only, no theorem or audit inference.'
 else:judgment='Accepted as dated author process, conformance, source identity or execution evidence; no scientific authority or future permission inferred. Actual current scope checked against canonical note.'
 rows.append(dict(original_path=path,original_sha256=sha(b),disposition='accepted unchanged',recovery=f'{HEAD}:{path}',final_path=path,final_sha256=sha(b),git_blob=g('rev-parse',HEAD+':'+path).decode().strip(),role=role,reviewer_judgment=judgment))
# Direct historical original recovery, not trust in the author's count.
prov=j(P/'FINAL_PROVENANCE_CHECK.json');historical=[]
for row in prov['historical_copies']:
 assert read(row['path'])==Path(row['original']).read_bytes()
 assert sha(read(row['path']))==row['sha256'];historical.append(row['path'])
# Full mutation bytes are equal to the read primary except the exact inspected change.
plan=j(P/'MUTATION_PLAN.json');src=read(plan['runner']).decode();mutation=[]
for item in plan['mutations']:
 assert src.count(item['old'])==1
 q=P/'mutations'/item['name'];assert Path(str(R/q)+'.py').read_text()==src.replace(item['old'],item['new'])
 execution=j(Path(str(q)+'.execution.json'));err=read(Path(str(q)+'.stderr.txt'));out=read(Path(str(q)+'.stdout.txt'))
 assert execution['exit_code']==1 and execution['termination_reason'] is None and b'AssertionError' in err
 assert sha(err)==execution['stderr_sha256'] and sha(out)==execution['stdout_sha256'];mutation.append(item)
# Cache equality, exact returned payload and independently reconstructed v1 fingerprint.
res=j(P/'primary/cache_result.json')['result'];assert res['stdout']==read(P/'primary/run.stdout.txt').decode() and not res['stderr']
inputs=ast.literal_eval(next(n.value for n in ast.parse(src).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets)))
f=hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
for name in inputs:
 n=name.encode();b=read(name);f.update(len(n).to_bytes(8,'big'));f.update(n);f.update(len(b).to_bytes(8,'big'));f.update(b)
cache=read('logs/runner-cache/native_permanent_markers_coherent_media_2026_09_30.txt').decode();assert f.hexdigest() in cache
assert res['stdout']==cache.split('----- stdout -----\n',1)[1].split('\n----- stderr -----',1)[0]
assert res['exit_code']==0 and res['status']=='ok' and res['timeout_sec']==30
# Manifest has no prior-content change.
old=json.loads(g('show',BASE+':docs/audit/data/citation_graph_manifest.json'));new=j('docs/audit/data/citation_graph_manifest.json')
assert all(new['nodes'][k]==v for k,v in old['nodes'].items())
assert set(new['nodes'])-set(old['nodes'])=={'native_permanent_markers_coherent_media_bounded_theorem_note_2026-09-30'}
assert new['node_count']-old['node_count']==1 and new['edge_count']-old['edge_count']==2
# All execution captures match their actual execution records.
captures=[]
for q in (R/P).rglob('*.execution.json'):
 d=json.loads(q.read_text())
 for name,digest in d.get('capture_sha256',{}).items():assert sha((q.parent/name).read_bytes())==digest;captures.append(str(q.parent/name))
for args in [('diff','--check'),('diff','--cached','--check'),('diff','--check',BASE,HEAD)]: assert subprocess.run(['git',*args],cwd=R).returncode==0
context=[]
for name in [x['path'] for x in j(P/'SOURCE_BINDINGS.json')['sources']]+['scripts/native_qubit_pair_density_onset_2026_09_30.py','scripts/runner_cache.py','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/repo/REVIEW_FEEDBACK_WORKFLOW.md','docs/repo/ACTIVE_REVIEW_QUEUE.md','docs/repo/DEFERRED_DECISIONS.md','docs/repo/CONTROLLED_VOCABULARY.md','docs/CANONICAL_HARNESS_INDEX.md','docs/audit/README.md','docs/audit/data/premise_decision_history.json']:
 b=read(name);assert b==g('show',BASE+':'+name);context.append(dict(path=name,sha256=sha(b),revision=BASE))
receipt=dict(utc=datetime.now(timezone.utc).isoformat(),reviewer_session='/root/native_record_medium_whole_unit_review',base=BASE,commit=HEAD,tree=TREE,methodology='7146fe17a76de41badcaca3c3c7cac6d11eb2a00',same_session_equal_tree_confirmation=True,original_dispositions=rows,deleted_paths=[],context_inputs=context,historical_originals_verified=historical,mutations_verified=mutation,execution_capture_files_verified=captures,checks={'path_count':len(paths),'syntax_files':sum(p.endswith('.py') for p in paths),'manifest_added_nodes':1,'manifest_added_edges':2,'prior_manifest_entries_unchanged':len(old['nodes']),'cache_input_fingerprint':f.hexdigest(),'three_diff_checks':True,'source_index_HEAD_equal':True,'working_tree_clean':True},unrun=['canonical primary rerun (unchanged once-executed successful evidence reused)','mutation reruns (exact actual artifacts inspected)','full pipeline','strict audit lint','changed audit evidence integration check','final schema2/cache gate (root responsibility)','formal audit'])
(O/'SOURCE_DISPOSITIONS.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'verified':receipt['checks'],'historical_originals':len(historical),'commit':HEAD,'tree':TREE,'source_dispositions_sha256':sha((O/'SOURCE_DISPOSITIONS.json').read_bytes())},indent=2))
