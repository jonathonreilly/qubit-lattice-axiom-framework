"""Mechanical coordinator receipt/cleanup/FF publication for a reviewed frozen train.
Independent scientific acceptance is supplied by immutable per-unit records;
this helper does not create a review verdict or run/apply an audit.
Run only after the sequential pipeline/strict/evidence process exited zero.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, tarfile
p=argparse.ArgumentParser();p.add_argument('label');p.add_argument('--notes',type=int,required=True);p.add_argument('--push',action='store_true');a=p.parse_args()
root=Path.cwd();out=root.parent;label=a.label
r=json.loads((out/(label+'-record.json')).read_text())
def git(*args):return subprocess.check_output(['git',*args],text=True).strip()
def call(*args):subprocess.run(args,check=True)
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
assert git('rev-parse','HEAD')==r['source_head'],'candidate source commit moved'
evidence=(out/(label+'-evidence.txt')).read_text()
assert f'checked={a.notes} failures=0 control_failures=0' in evidence
assert 'OK: no errors' in (out/(label+'-strict.log')).read_text()
for path,h in r['inputs'].items():assert digest(root/path)==h,('input drift',path)
assert set(git('diff','--name-only',r['base']+'...HEAD').splitlines())==set(r['source_owners'])
rows=json.loads((root/'docs/audit/data/audit_ledger.json').read_text())['rows']
affected={k:v for k,v in rows.items() if v.get('note_path') in r['source_owners']}
non_science_expectations=r.get('non_science_expectations',{})
for path,expected in non_science_expectations.items():
 assert path in r['source_owners'] and expected['claim_type']=='meta'
 assert expected['review'] in r['review_evidence_hashes']
 assert digest(out/expected['review'])==r['review_evidence_hashes'][expected['review']]
 assert digest(root/path)==expected['sha256']
 matches=[v for v in affected.values() if v.get('note_path')==path]
 assert len(matches)==1 and matches[0]['claim_type']=='meta' and matches[0]['audit_status']=='unaudited', ('unreviewed or promoted meta row',path)
science={k:v for k,v in affected.items() if not v.get('note_path','').startswith('docs/work_history/') and v.get('note_path') not in non_science_expectations}
assert len(science)==a.notes,(len(science),a.notes)
for k,v in science.items():
 assert v['audit_status']=='unaudited' and v['claim_type']=='bounded_theorem',(k,v['audit_status'],v['claim_type'])
 if not v['deps']:
  expectation=r.get('dependency_expectations',{}).get(v['note_path'],{})
  assert expectation.get('allow_empty_repository_deps') is True and expectation.get('independent_review') and expectation.get('reason'),('missing reviewed repository dependency expectation',k)
 # Declared load-bearing repository sources must still be present even when other context links exist.
 required=r.get('dependency_expectations',{}).get(v['note_path'],{}).get('required_claim_ids',[])
 assert set(required).issubset(v['deps']),('declared dependency missing',k,required,v['deps'])
 print(k,v['claim_type'],v['audit_status'],v.get('helper_runner_paths'),flush=True)
(out/(label+'-validated-rows.json')).write_text(json.dumps(affected,indent=2)+'\n')
sys.path.insert(0,str(root/'scripts'))
from science_fix_loop import publication_changed_paths,strip_generated_audit_outputs,generated_audit_output
changed=publication_changed_paths(root)
with tarfile.open(out/(label+'-generated-validation.tar.gz'),'w:gz') as archive:
 for path in changed:
  if generated_audit_output(path) and (root/path).is_file():archive.add(root/path,arcname=path)
(out/(label+'-validation.patch')).write_bytes(subprocess.check_output(['git','diff','HEAD']))
strip_generated_audit_outputs(root,changed)
manifest='docs/audit/data/citation_graph_manifest.json';remaining=git('diff','--name-only','HEAD').splitlines()
assert remaining in [[],[manifest]],remaining
assert not git('diff','--name-only'),'unstaged final changes'
if remaining:
 print(git('diff','--cached','--stat'),flush=True)
 call('git','commit','-m','Acknowledge reviewed source topology for '+label)
for args in [('diff','--check'),('diff','--cached','--check'),('diff',r['base']+'...HEAD','--check')]:call('git',*args)
assert not git('status','--porcelain')
for path,h in r['inputs'].items():assert digest(root/path)==h,('post-cleanup input drift',path)
r.update(candidate_commit=git('rev-parse','HEAD'),candidate_tree=git('rev-parse','HEAD^{tree}'),combined_gate='PASS',full_pipeline_count=1,changed_evidence_rows=a.notes,validation_logs={name:digest(out/name) for name in [label+'-pipeline.log',label+'-strict.log',label+'-evidence.txt',label+'-validated-rows.json']},audit_boundary='No verdict applied; source rows unaudited in validation. Existing main authority preserved; regenerated audit outputs stripped.',landing_state='validated; not pushed')
receipt=out/(label+'-landing.json');receipt.write_text(json.dumps(r,indent=2)+'\n')
if a.push:
 call('git','fetch','origin','main')
 if git('rev-parse','origin/main')!=r['base']:
  r['landing_state']='NOT PUSHED: main advanced';r['observed_new_base']=git('rev-parse','origin/main');receipt.write_text(json.dumps(r,indent=2)+'\n');raise SystemExit('Main advanced: rebuild/revalidate, never reuse this base receipt')
 for num,head in r['heads'].items():
  state=json.loads(subprocess.check_output(['gh','pr','view',str(num),'--json','headRefOid,state']))
  assert state['state']=='OPEN' and state['headRefOid']==head,('PR changed',num,state)
 call('git','merge-base','--is-ancestor',r['base'],'HEAD')
 call('git','push','origin','HEAD:refs/heads/main')
 call('git','fetch','origin','main')
 call('git','merge-base','--is-ancestor',r['candidate_commit'],'origin/main')
 r['landing_state']='LANDED';receipt.write_text(json.dumps(r,indent=2)+'\n');print('LANDED',r['candidate_commit'],flush=True)
