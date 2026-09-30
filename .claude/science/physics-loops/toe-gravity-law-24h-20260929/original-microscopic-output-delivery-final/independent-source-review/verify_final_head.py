"""Read-only final-head verification; new outputs stay in review directory."""
from pathlib import Path
import hashlib,json,subprocess
p=Path('.claude/science/physics-loops/original-microscopic-output-20260930'); o=p/'independent-source-review'
h=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git',*a])
head='72170ba4af249bf1b3e89a41c6209a8f2d69d464'; base='fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7'; tree='a94bbf6eed29403a1ef64474408a129989ca1e5a'
assert git('rev-parse','HEAD').decode().strip()==head
assert git('rev-parse','HEAD^{tree}').decode().strip()==tree
assert git('rev-parse','origin/main').decode().strip()==base
remote=git('ls-remote','origin','refs/heads/main').decode().strip();assert remote.split()[0]==base
assert not git('diff','--name-only') and not git('diff','--cached','--name-only')
original=json.loads((o/'SOURCE_IDENTITIES_AND_DISPOSITIONS.json').read_text()); delivery=json.loads((p/'FINAL_DELIVERY_MAP.json').read_text())
assert h((o/'REPORT.md').read_bytes())=='777349c8864590935c0d29b953afae3fd16d4b8b83dff680e93088554a0c1a59'
assert h((p/'FINAL_DELIVERY_MAP.json').read_bytes())=='5cd50c0942b288a9467ebed2bcd8519df853fe5ca831d41a680f1aebc1228b24'
assert delivery['preserved_reviewed_dispositions']==original['original_dispositions']
paths=git('diff','--name-only','--no-renames',base,head).decode().splitlines();assert len(paths)==157
orig={r['original_path']:r for r in original['original_dispositions']}
add={r['path']:r for r in delivery['added_paths']}; map_path=str(p/'FINAL_DELIVERY_MAP.json')
assert set(paths)==set(orig)|set(add)|{map_path}
for x in paths:
 b=Path(x).read_bytes();assert b==git('show',head+':'+x)
 expected=orig[x]['final_sha256'] if x in orig else add[x]['sha256'] if x in add else '5cd50c0942b288a9467ebed2bcd8519df853fe5ca831d41a680f1aebc1228b24'
 assert h(b)==expected
record=json.loads((p/'FINAL_UNIT_RECORD_PRECOMMIT.json').read_text()); check=json.loads((p/'FINAL_UNIT_CHECK.stdout').read_text()); execution=json.loads((p/'FINAL_UNIT_CHECK_EXECUTION.json').read_text())
assert h((p/'FINAL_UNIT_RECORD_PRECOMMIT.json').read_bytes())==check['record_sha256']=='6e08a7dca4d58dc3c50c42d435e6b1317945f3bd55dc40b97444b79e1ef779a6'
assert h((p/'FINAL_UNIT_CHECK.stdout').read_bytes())==execution['stdout_sha256']=='5cdf7e33ad5872c0ab7fc1cf34fc9ba44a67c344eba62d8d75fce131380be17c'
assert check['mechanical_status']=='ok' and check['cache_checked'] and execution['exit_code']==0 and execution['stop_reason'] is None
assert check['tree']==record['source']['tree']=='b1cc2981ef281dba4ba9ef070e682f747077a8ae'
prepaths=git('diff','--name-only',base,check['tree']).decode().splitlines();assert len(prepaths)==149
assert set(prepaths)=={r['path'] for r in record['source']['paths']}
for r in record['source']['paths']:
 assert h(git('show',check['tree']+':'+r['path']))==r['sha256']==h(Path(r['path']).read_bytes())
for rows in record['inputs'].values():
 for r in rows:assert h(Path(r['path']).read_bytes())==r['sha256']==h(git('show',head+':'+r['path']))
for r in original['current_inputs']+original['methods']:
 assert h(Path(r['path']).read_bytes())==r['sha256']
for r in json.loads((o/'READ_SCOPE.json').read_text())['reads']:
 assert h(Path(r['path']).read_bytes())==r['sha256']
existing=git('diff','--name-only','--diff-filter=MDR',base,head).decode().splitlines();assert existing==['docs/audit/data/citation_graph_manifest.json']
old=json.loads(git('show',base+':'+existing[0]));new=json.loads(Path(existing[0]).read_text());assert all(new['nodes'][k]==v for k,v in old['nodes'].items())
assert new['node_count']-old['node_count']==5 and new['edge_count']-old['edge_count']==6
for args in [('diff','--check',base,head),('diff','--check'),('diff','--cached','--check')]:assert not git(*args)
rows=list(original['original_dispositions'])
for x in sorted(set(paths)-set(orig)):
 d='accepted immutable original independent source-review artifact; no audit authority' if '/independent-source-review/' in x else 'accepted additive delivery/provenance/check record; does not change science or confer combined validation'
 rows.append({'original_path':x,'original_sha256':h(Path(x).read_bytes()),'disposition':d,'recovery':x,'final_path':x,'final_sha256':h(Path(x).read_bytes())})
result={'reviewer_session':'/root/microscopic_output_source_review','source_only_verdict':'PASS WITH BOUNDED CLAIMS','base':base,'current_main':base,'remote_main_observed':remote,'final_head':head,'final_tree':tree,'original_source_report_sha256':h((o/'REPORT.md').read_bytes()),'all_original_141_paths_unchanged':True,'final_path_count':157,'precommit_checked_tree':check['tree'],'precommit_checked_path_count':149,'postcheck_additions':sorted(set(paths)-set(prepaths)),'original_and_current_inputs_unchanged':True,'modified_existing_main_paths':existing,'prior_graph_entries_unchanged':len(old['nodes']),'new_graph_nodes':5,'new_graph_edges':6,'combined_gate':'not run or claimed','final_dispositions':rows}
(o/'FINAL_HEAD_IDENTITIES_AND_DISPOSITIONS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='final_dispositions'},indent=2))
