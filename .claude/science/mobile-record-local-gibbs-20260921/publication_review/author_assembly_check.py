#!/usr/bin/env python3
"""Author assembly authentication; the independent math review is separate."""
from pathlib import Path
import ast,hashlib,json,re,subprocess,zipfile,datetime
HERE=Path(__file__).resolve().parent;OUT=HERE.parent;ROOT=OUT.parents[2]
sha=lambda b:hashlib.sha256(b).hexdigest()
NOTE='docs/MOBILE_RECORDS_LOCAL_GIBBS_CIRCULATIONS_AND_WINDING_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-21.md'
RUNNER='scripts/mobile_records_local_gibbs_circulations_and_winding_transport_2026_09_21.py'
CLAIM='mobile_records_local_gibbs_circulations_and_winding_transport_bounded_theorem_note_2026-09-21'
known=['70a9abf1588e90e8a7065a5e1d6155f8f56997672b0303c0ea6cbca71fc1bf12','28949032a1b110e642a8d3765dd880a4d8487be02cc70b3b095275d7cde59069']
identities={}
def read(p):
 data=p.read_bytes();identities[str(p.relative_to(ROOT))]=dict(bytes=len(data),sha256=sha(data));return data
note=read(ROOT/NOTE).decode();transform=json.loads(read(OUT/'PUBLICATION_TRANSFORM.json'))
sections=re.split(r'(?m)(?=^## Part [AB]\. |^## Evidence and open physical work)',note)[1:3]
assert len(sections)==len(transform['parts'])==2
for part,spec,expected in zip(sections,transform['parts'],known):
 raw=read(OUT/'primary_sources'/spec['source']);assert sha(raw)==spec['source_sha256']==expected
 body=raw.decode().split('\n',2)[2].rstrip();old,new=spec['replacement']['old'],spec['replacement']['new'];assert body.count(old)==1
 body=body.replace(old,new);body='\n'.join('#'+l if l.startswith('#') else l for l in body.splitlines())
 assert part.split('\n',2)[2].rstrip()==body and sha(body.encode())==spec['published_body_sha256']
manifest=json.loads(read(OUT/'INDEPENDENT_CAPSULES.json'));assert len(manifest['capsules'])==1;cap=manifest['capsules'][0]
archive=read(OUT/cap['archive']);assert sha(archive)==cap['zip_sha256']
with zipfile.ZipFile(OUT/cap['archive']) as z:
 assert sha(z.read('review/REPORT.md'))=='edd446648733d0bdc3a7732fb7541a22b22940e8549c6757f9c67f428c387e63'
 assert sha(z.read('review/FINAL_SEAL.json'))=='6eefb9331502b7b7094fd9e8a2a62abd918ecb8c3446bf181f16f86e27ebe6f7'
 assert sha(z.read('review/CORRECTION_ACK.json'))=='2075af3294f430c9cc93f781332750cc0d4f2ea7b3453622af2f05d0560bbe09'
 bound={r['sha256']:z.read(r['member']) for r in cap['bindings'] if r['disposition']=='bundled'}
 for spec,h in zip(transform['parts'],known):assert read(OUT/'primary_sources'/spec['source'])==bound[h]
verifier=subprocess.run(['python3',str(OUT/'verify_evidence.py')],cwd=ROOT,capture_output=True,text=True);assert verifier.returncode==0
v=json.loads(verifier.stdout);assert(v['capsules'],v['bundled_members'],v['bundled_source_bindings'],v['seal_rows'])==(1,40,29,44)
runner=read(ROOT/RUNNER);values={}
for n in ast.parse(runner).body:
 if isinstance(n,ast.Assign) and len(n.targets)==1 and getattr(n.targets[0],'id',None) in ('SUITES','AUDIT_INPUT_PATHS','MUTATIONS'):values[n.targets[0].id]=ast.literal_eval(n.value)
expected_ids={p:sha(read(ROOT/p)) for p in values['AUDIT_INPUT_PATHS']};expected_ids[RUNNER]=sha(runner)
for name,_,_ in values['SUITES']:
 data=read(OUT/'author_checks'/name);assert data==bound[sha(data)]
runs=json.loads(read(OUT/'AUTHOR_RUNS.json'))['runs'];assert len(runs)==7
for run in runs:
 raw=read(OUT/run['result']);assert sha(raw)==run['result_sha256'];result=json.loads(raw)
 log=read(OUT/run['log']);assert sha(log)==run['log_sha256'];assert result['identities']==expected_ids
 mutation=run['mutation'];assert result['mutation']==mutation
 if mutation is None:assert result['passed'] and result['control_count']==18 and run['returncode']==0
 else:
  name,old,new=values['MUTATIONS'][mutation];code=read(OUT/'author_checks'/name).decode();assert code.count(old)==1
  child=result['suites'][-1];assert child['executed_source_sha256']==sha(code.replace(old,new).encode())
  assert not result['passed'] and run['returncode']==1 and 'AssertionError' in child['stderr']
  assert not any(x in child['stderr'] for x in ['SyntaxError','ModuleNotFoundError','TimeoutExpired'])
mp='docs/audit/data/citation_graph_manifest.json';old=json.loads(subprocess.check_output(['git','show','5d784d8ccda5268f2b7c056fcdf0d81fdb703319:'+mp],cwd=ROOT));new=json.loads(read(ROOT/mp));graph=json.loads(read(ROOT/'docs/audit/data/citation_graph.json'))
assert set(new['nodes'])-set(old['nodes'])=={CLAIM} and all(new['nodes'][k]==v for k,v in old['nodes'].items())
assert new['node_count']==old['node_count']+1 and new['edge_count']==old['edge_count']+1
computed={k:dict(out_degree=len(v.get('deps',[])),deps_hash=sha('\n'.join(sorted(v.get('deps',[]))).encode())[:12]) for k,v in graph['nodes'].items()};assert computed==new['nodes']
assert graph['nodes'][CLAIM]['note_hash']==sha(note.encode()) and graph['nodes'][CLAIM]['runner_path']==RUNNER
cache=read(ROOT/'logs/runner-cache'/('mobile_records_local_gibbs_circulations_and_winding_transport_2026_09_21.txt')).decode()
h=hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
for rel in values['AUDIT_INPUT_PATHS']:
 p=rel.encode();data=read(ROOT/rel);h.update(len(p).to_bytes(8,'big'));h.update(p);h.update(len(data).to_bytes(8,'big'));h.update(data)
assert 'runner_sha256: '+sha(runner) in cache and 'input_fingerprint_sha256: '+h.hexdigest() in cache and '\nstatus: ok\n' in cache and '\nexit_code: 0\n' in cache
for rel,identity in identities.items():assert sha((ROOT/rel).read_bytes())==identity['sha256']
result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Author assembly verification only. Known independent mathematical review reused at exact hashes; no new independent review or audit verdict.',source_identities=identities,source_bodies=2,capsules=1,bundled_members=40,bundled_bindings=29,seal_rows=44,external_pdf_exclusions=2,author_controls=18,substantive_mutation_rejections=6,old_manifest_entries_unchanged=len(old['nodes']),graph_delta=dict(nodes=1,edges=1),all_passed=True)
(HERE/'AUTHOR_ASSEMBLY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='source_identities'},indent=2))
