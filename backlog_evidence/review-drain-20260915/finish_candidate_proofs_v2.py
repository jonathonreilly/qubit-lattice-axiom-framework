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
# Unit receipts distinguish claim-owned proof inputs from autonomous graph claims.
for name,h in r['review_evidence_hashes'].items():
 assert digest(out/name)==h,('review evidence drift',name)
collection=json.loads((out/(label+'-collected-units.json')).read_text())
owned_proofs={};all_proof_bindings=[]
for unit in collection['units']:
 record_name=unit.get('canonical_unit_record')
 if not record_name:continue
 assert record_name in r['review_evidence_hashes'],('unbound unit record',record_name)
 record_path=out/record_name;record=json.loads(record_path.read_text())
 if record['schema_version']!=2:continue
 bound={x['path']:x['sha256'] for x in record['source']['paths']}
 for entries in record['inputs'].values():
  for x in entries:
   assert x['path'] not in bound or bound[x['path']]==x['sha256']
   bound[x['path']]=x['sha256']
 for proof in record.get('supporting_proofs',[]):
  note=proof['canonical_note'];path=proof['path']
  if note not in r['dependency_expectations']:continue
  owner=next(n for n in record['notes'] if n['path']==note)
  assert r['source_owners'].get(note)=='review-'+unit['unit'],('proof owner mismatch',note)
  assert path in bound and r['inputs'].get(path)==bound[path] and digest(root/path)==bound[path]
  ref=proof['review_reference'];ref_name=Path(ref['path']).relative_to(out).as_posix()
  assert r['review_evidence_hashes'].get(ref_name)==ref['sha256'],('unbound proof review',path)
  all_proof_bindings.append({'canonical_note':note,'source_path':path,'sha256':bound[path],
    'unit_record':record_name,'unit_record_sha256':r['review_evidence_hashes'][record_name],
    'review_reference':ref,'role':'Current proof owned by this canonical claim; not an autonomous graph parent.',
    'load_bearing_parent_of_owner':path in owner['repository_dependencies']})
  if path not in owner['repository_dependencies']:continue
  bindings=[b for b in r['dependency_expectations'][note]['declared_authority_bindings'] if b['source_path']==path]
  assert len(bindings)==1 and bindings[0]['sha256']==bound[path],('proof binding mismatch',path)
  binding=bindings[0];key=(note,binding['graph_id']);assert key not in owned_proofs
  owned_proofs[key]={'canonical_note':note,'source_path':path,'sha256':bound[path],
                    'unit_record':record_name,'unit_record_sha256':r['review_evidence_hashes'][record_name],
                    'review_reference':ref,'role':'Current proof owned by this canonical claim; not an autonomous graph parent.'}
r['owned_supporting_proof_bindings']=all_proof_bindings
rows=json.loads((root/'docs/audit/data/audit_ledger.json').read_text())['rows']
affected={k:v for k,v in rows.items() if v.get('note_path') in r['source_owners']}
science={k:v for k,v in affected.items() if not v.get('note_path','').startswith('docs/work_history/')}
assert len(science)==a.notes,(len(science),a.notes)
for k,v in science.items():
 assert v['audit_status']=='unaudited' and v['claim_type']=='bounded_theorem',(k,v['audit_status'],v['claim_type'])
 if not v['deps']:
  expectation=r.get('dependency_expectations',{}).get(v['note_path'],{})
  assert expectation.get('allow_empty_repository_deps') is True and expectation.get('independent_review') and expectation.get('reason'),('missing reviewed repository dependency expectation',k)
 # Declared load-bearing repository sources must still be present even when other context links exist.
 required=r.get('dependency_expectations',{}).get(v['note_path'],{}).get('required_claim_ids',[])
 owned={claim for (note,claim) in owned_proofs if note==v['note_path']}
 assert owned.isdisjoint(v['deps']),('owned proof unexpectedly a graph parent',k,owned,v['deps'])
 assert (set(required)-owned).issubset(v['deps']),('declared dependency missing',k,required,v['deps'])
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
