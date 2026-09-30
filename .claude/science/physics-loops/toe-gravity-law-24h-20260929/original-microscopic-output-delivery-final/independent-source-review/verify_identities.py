"""Read-only candidate/recovery verification; writes only this review directory."""
from pathlib import Path
import ast, gzip, hashlib, json, subprocess
root=Path.cwd()
p=Path('.claude/science/physics-loops/original-microscopic-output-20260930')
out=p/'independent-source-review'
h=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git',*a])
base='fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7'
method='7146fe17a76de41badcaca3c3c7cac6d11eb2a00'
assert git('rev-parse','HEAD').decode().strip()==base
assert git('rev-parse','origin/main').decode().strip()==base
assert git('write-tree').decode().strip()=='370b66434f8e51e13a9e4437175e41e702d3e96b'
manifest=json.loads((p/'FINAL_AUTHOR_MANIFEST.json').read_text())
assert h((p/'FINAL_AUTHOR_MANIFEST.json').read_bytes())=='c6c707a57e661351211ad9d2dcb886fa1c427431151511eaf1b6bc5ab71f1e35'
paths=git('diff','--cached','--name-only','--no-renames',base).decode().splitlines()
assert set(paths)=={r['path'] for r in manifest['rows']}|{str(p/'FINAL_AUTHOR_MANIFEST.json')}
for r in manifest['rows']:
 b=Path(r['path']).read_bytes(); assert h(b)==r['sha256']; assert b==git('show',':'+r['path'])
assert not git('diff','--name-only')
existing=git('diff','--cached','--name-only','--diff-filter=MDR',base).decode().splitlines()
assert existing==['docs/audit/data/citation_graph_manifest.json']
old=json.loads(git('show',base+':docs/audit/data/citation_graph_manifest.json'))
new=json.loads(Path(existing[0]).read_text())
assert all(new['nodes'][k]==v for k,v in old['nodes'].items())
assert new['node_count']-old['node_count']==5 and new['edge_count']-old['edge_count']==6
archives=json.loads((p/'ARCHIVED_EVIDENCE.json').read_text())['rows']
for r in archives:
 b=Path(r['archive']).read_bytes(); assert h(b)==r['archive_sha256']; assert h(gzip.decompress(b))==r['original_sha256']
mut=json.loads((p/'MUTATION_RESULTS.json').read_text())
runner=Path('scripts/original_microscopic_local_output_2026_09_30.py'); source=runner.read_bytes()
assert h(source)==mut['runner_sha256']
for r in mut['mutations']:
 d=p/'mutations'/r['name']; b=(d/'mutation.diff.gz').read_bytes(); raw=gzip.decompress(b)
 assert h(b)==r['diff_container_sha256'] and h(raw)==r['raw_diff_sha256']
 data=json.loads((d/'output.json').read_text())
 assert data['runner_sha256']==r['mutated_runner_sha256']
 assert r['expected_failure'] in data['failures'] and data['fail_count']>0 and r['exit_code']==1
 assert 'FAIL '+r['expected_failure'] in (d/'stdout.txt').read_text()
 assert not (d/'stderr.txt').read_bytes()
inputs=next(ast.literal_eval(x.value) for x in ast.parse(source).body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in x.targets))
output=json.loads(Path('outputs/original_microscopic_local_output_2026_09_30.json').read_text())
assert output['runner_sha256']==h(source) and output['pass_count']==6 and output['fail_count']==0
for x in inputs: assert output['inputs'][x]==h(Path(x).read_bytes())==mut['input_sha256'][x]
for cat,rows in manifest['actual_source_input_tooling_map'].items():
 for r in rows: assert h(Path(r['path']).read_bytes())==r['sha256']
methods=['docs/ai_methodology/skills/review-loop/SKILL.md','docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md','docs/ai_methodology/SCIENCE_WORKFLOW.md','docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md','docs/ai_methodology/skills/no-go-discipline/SKILL.md','docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md','docs/ai_methodology/skills/physics-loop/references/CLAIM_STATUS.md']
methods+=['docs/ai_methodology/skills/review-loop/references/'+x+'.md' for x in ['REVIEW_SETUP','REVIEW_UNITS','SCIENCE_LENSES','FIXES_AND_REPORTING','AUDIT_COMPATIBILITY','UNIT_RECEIPT']]
for x in methods: assert git('show',method+':'+x)==Path(x).read_bytes()
rows=[]
for x in paths:
 if x.startswith('docs/proofs/') or x==inputs[0]: role='accepted current conditional mathematical source; complete argument read'
 elif x==str(runner): role='accepted finite-control implementation; complete code read, no theorem certification'
 elif x=='docs/audit/data/citation_graph_manifest.json': role='accepted topology acknowledgment; all prior entries preserved; no audit verdict'
 elif '/recovery/' in x: role='historical recovery retained byte-for-byte; no current premise or reusable formal review'
 elif '/mutations/' in x: role='finite-control failure evidence; hashes/output consistency checked, not theorem evidence'
 elif x.startswith('outputs/') or x.startswith('logs/'): role='source-bound author finite execution; paired output/cache read'
 else: role='author process/provenance only; no independent scientific or audit authority'
 rows.append({'original_path':x,'original_sha256':h(Path(x).read_bytes()),'disposition':role,'recovery':x,'final_path':x,'final_sha256':h(Path(x).read_bytes())})
result={'scope':'mechanical verification only; independent mathematical judgment is REPORT.md','base':base,'reviewed_main':base,'methodology':method,'staged_tree':'370b66434f8e51e13a9e4437175e41e702d3e96b','candidate_path_count':len(paths),'existing_changed_paths':existing,'prior_graph_entries_unchanged':len(old['nodes']),'archive_rows_checked':len(archives),'mutation_rows_checked':len(mut['mutations']),'current_inputs':[{'path':x,'sha256':h(Path(x).read_bytes())} for x in inputs],'methods':[{'path':x,'sha256':h(Path(x).read_bytes())} for x in methods],'original_dispositions':rows}
(out/'SOURCE_IDENTITIES_AND_DISPOSITIONS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['current_inputs','methods','original_dispositions']},indent=2))
