from pathlib import Path
import subprocess,hashlib,json,gzip,difflib,datetime
BASE='ea3d4f6236160233f6f9e183b4b6eb5ba3252607'
TREE='e4b261bde8908d41acbf69663901ac96164080bf'
MAIN='fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7'
PACK='.claude/science/physics-loops/native-dilute-thermodynamics-20260930/'
CAMPAIGN=Path('/Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/.claude/science/physics-loops/toe-gravity-law-24h-20260929')
def git(*args): return subprocess.check_output(['git',*args])
def blob(rev,p): return git('show',rev+':'+p)
def sha(b): return hashlib.sha256(b).hexdigest()
paths=git('diff','--name-only','--no-renames',BASE,TREE).decode().splitlines()
assert len(paths)==158
contents={p:blob(TREE,p) for p in paths}
ready=json.loads((CAMPAIGN/'native-dilute-thermodynamics-delivery-handoff/READY_TREE.json').read_bytes())
assert ready['staged_tree']==TREE and set(paths)=={x['path'] for x in ready['files']}
for x in ready['files']: assert sha(contents[x['path']])==x['sha256']
inv=json.loads(contents[PACK+'FINAL_BINDINGS.json'])
assert set(paths)-{PACK+'FINAL_BINDINGS.json'}=={x['path'] for x in inv['files']}
for x in inv['files']: assert sha(contents[x['path']])==x['sha256']
source_map=json.loads(contents[PACK+'CAMPAIGN_SOURCE_MAP.json'])
for x in source_map['sources']:
 assert sha(contents[x['archive_path']])==x['sha256']
 assert contents[x['archive_path']]==(CAMPAIGN/x['original_campaign_path']).read_bytes()
archive_checks=[]
for p,b in contents.items():
 if p.endswith('.gz'):
  old=gzip.decompress(b);current='docs/'+Path(p).name[:-3]
  assert old.rstrip()==contents[current].rstrip()
  archive_checks.append({'path':p,'decoded_sha256':sha(old),'current':current,'only_terminal_whitespace':True})
primary=contents['scripts/native_dilute_thermodynamics_2026_09_30.py']
mut=json.loads(contents[PACK+'mutations/results.json'])
mutation_checks=[]
for i,row in enumerate(mut['results'],1):
 prefix=PACK+f"mutations/{i:02d}_{row['name']}/"
 expected=primary.replace((row['original_assignment']+'\n').encode(),(row['mutated_assignment']+'\n').encode(),1)
 assert contents[prefix+'candidate.py']==expected
 assert sha(expected)==row['candidate_sha256']
 rec=json.loads(contents[prefix+'run.execution.json']);assert rec==row['execution']
 for file,h in rec['capture_sha256'].items():assert sha(contents[prefix+file])==h
 stderr=contents[prefix+'run.stderr.txt'].decode()
 assert 'AssertionError' in stderr and row['expected_assertion'] in stderr
 assert rec['exit_code']==1 and rec['termination_reason'] is None
 assert json.loads(contents[prefix+'wrapper.stdout.txt'])==rec
 assert not contents[prefix+'wrapper.stderr.txt'] and not contents[prefix+'run.stdout.txt']
 mutation_checks.append({'name':row['name'],'single_assignment_verified':True,'specific_assertion_verified':True})
for p,b in contents.items():
 if p.endswith('.execution.json'):
  rec=json.loads(b)
  for file,h in rec['capture_sha256'].items():assert sha(contents[str(Path(p).parent/file)])==h
cache=contents['logs/runner-cache/native_dilute_thermodynamics_2026_09_30.txt'].decode()
primary_result=json.loads(contents[PACK+'primary/cache_result.json'])
assert primary_result['result']['stdout']==contents[PACK+'primary/run.stdout.txt'].decode()
assert primary_result['result']['stdout'] in cache
assert 'TOTAL: PASS=7 FAIL=0' in cache
oldmanifest=json.loads(blob(BASE,'docs/audit/data/citation_graph_manifest.json'))
newmanifest=json.loads(contents['docs/audit/data/citation_graph_manifest.json'])
assert all(newmanifest['nodes'].get(k)==v for k,v in oldmanifest['nodes'].items())
added={k:v for k,v in newmanifest['nodes'].items() if k not in oldmanifest['nodes']}
assert len(added)==4 and newmanifest['edge_count']-oldmanifest['edge_count']==14
context=json.loads(contents[PACK+'CONTRACT_FREEZE.json'])['base_inputs']
for x in context:
 assert sha(blob(TREE,x['path']))==x['sha256']
 assert blob(BASE,x['path'])==blob(TREE,x['path'])
 if 'NATIVE_FOUR_PARTICLE' not in x['path']: assert blob(MAIN,x['path'])==blob(TREE,x['path'])
# Distinguish frozen main delta; do not restore or integrate stale authority bytes.
main_delta=git('diff','--name-status','--no-renames',MAIN,TREE).decode().splitlines()
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base':BASE,'tree':TREE,'main':MAIN,'original_path_count':len(paths),'ready_inventory_matches_git':True,'final_bindings_matches_git_excluding_self':True,'historical_lossless_files_verified':len(source_map['sources']),'gzip_checks':archive_checks,'mutations':mutation_checks,'all_execution_capture_hashes_verified':True,'primary_cache_matches_actual_capture':True,'manifest':{'preserved_nodes':len(oldmanifest['nodes']),'added_nodes':added,'edge_delta':14},'unchanged_bound_premises':context,'actual_main_delta':main_delta,'stop_requested':Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929/STOP_REQUESTED.json').exists(),'scope':'Byte/provenance checks; full current math was read separately. Historical report bodies not independently re-certified.'}
Path('independent-source-review/FROZEN_EVIDENCE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['actual_main_delta','unchanged_bound_premises','mutations']},indent=2))
