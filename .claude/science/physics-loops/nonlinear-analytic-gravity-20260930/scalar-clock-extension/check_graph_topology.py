#!/usr/bin/env python3
"""Actual citation API topology comparison, without full graph/cache generation.

Recompute every discovered node/dependency and the changed note's fields and
helper closure. Preserve the old producer/base context and every manifest byte.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

repo=Path(__file__).resolve().parents[5]
pack=Path(__file__).resolve().parent
oldpack=pack.parent
sys.path.insert(0,str(repo/'docs/audit/scripts'))
import build_citation_graph as graph
import write_citation_graph_manifest as writer

start=time.monotonic()
def sha(data):return hashlib.sha256(data).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=repo)
head='6515ffa8570f21a0b3a8790fdd8a2879347550b8'
base='30a9461ee19a49b99fa6628fe942f08e504e8903'
assert git('rev-parse','HEAD').decode().strip()==head
oldrecord=json.loads((oldpack/'GRAPH_DELTA.json').read_text())
graphfile=repo/'docs/audit/data/citation_graph.json'
manifestfile=repo/'docs/audit/data/citation_graph_manifest.json'
graphbytes=graphfile.read_bytes();manifestbytes=manifestfile.read_bytes()
assert sha(graphbytes)==oldrecord['graph_sha256']
assert sha(manifestbytes)==oldrecord['after']['sha256']
assert manifestbytes==git('show',head+':docs/audit/data/citation_graph_manifest.json')
old=json.loads(graphbytes);manifest=json.loads(manifestbytes)
assert writer.compute_manifest(old)==manifest
policy_paths=('docs/audit/scripts/build_citation_graph.py',
 'docs/audit/scripts/write_citation_graph_manifest.py',
 'docs/audit/scripts/static_pipeline_checkpoint.py',
 'docs/audit/data/doc_authority_registry.json',
 'docs/audit/data/axiom_premise_nodes.json')
policies=[]
for name in policy_paths:
 data=(repo/name).read_bytes()
 assert data==git('show',head+':'+name)==git('show',base+':'+name),name
 policies.append({'path':name,'sha256':sha(data),'equal_old_base_and_head':True})
notes=graph.discover_notes();by_path={path:graph.claim_id_from_path(path) for path in notes}
tracked_docs=git('ls-tree','-r','--name-only',head,'--','docs').decode().splitlines()
expected_notes={str(repo/name) for name in tracked_docs if name.endswith('.md')
                and not graph.is_skipped(Path(name).relative_to('docs'))}
assert {str(path) for path in notes}==expected_notes
assert set(by_path.values())==set(old['nodes'])
# Match the exact last-path behavior of the actual builder for repeated IDs.
last_path={cid:path for path,cid in by_path.items()}
assert {cid:str(path.relative_to(repo)) for cid,path in last_path.items()}=={cid:node['path'] for cid,node in old['nodes'].items()}
newnodes={cid:{'deps':[]} for cid in old['nodes']}
edges=[];hash_changes=[];note_identities=[]
for path in notes:
 body=path.read_text(encoding='utf-8',errors='replace');cid=by_path[path]
 note_identities.append({'path':str(path.relative_to(repo)),'sha256':sha(body.encode())})
 if path==last_path[cid] and sha(body.encode())!=old['nodes'][cid]['note_hash']:
  hash_changes.append({'id':cid,'old_sha256':old['nodes'][cid]['note_hash'],'new_sha256':sha(body.encode())})
 for target in graph.extract_citations(body,path):
  other=by_path.get(target)
  if other is None or other==cid or other in newnodes[cid]['deps']:continue
  newnodes[cid]['deps'].append(other);edges.append({'from':cid,'to':other})
assert edges==old['edges']
assert all(newnodes[cid]['deps']==old['nodes'][cid]['deps'] for cid in newnodes)
assert writer.compute_manifest({'nodes':newnodes})==manifest
canonical='nonlinear_canonical_gravity_analytic_approximation_bounded_theorem_note_2026-09-30'
assert len(hash_changes)==1 and hash_changes[0]['id']==canonical,hash_changes
path=last_path[canonical];body=path.read_text();raw,typ=graph.extract_claim_type_hint(body)
primary=graph.extract_runner(body,path.relative_to(repo/'docs').as_posix())
current={'claim_id':canonical,'path':str(path.relative_to(repo)),'title':graph.extract_title(body),
 'claim_type_author_hint_raw':raw,'claim_type_author_hint':typ,
 'claim_type_seed_hint':typ or graph.extract_legacy_status_claim_type(body),
 'runner_path':primary,'helper_runner_paths':graph.helper_runner_paths_for_claim(canonical,primary),
 'note_hash':sha(body.encode()),'deps':newnodes[canonical]['deps']}
assert {k:v for k,v in current.items() if k!='note_hash'}=={k:v for k,v in old['nodes'][canonical].items() if k!='note_hash'}
# No top-level script was added/removed. Only the primary changed, and its
# actual helper closure remains empty; unrelated graph extraction is untouched.
tracked=set(git('ls-tree','-r','--name-only',head,'--','scripts').decode().splitlines())
actual={str(p.relative_to(repo)) for p in (repo/'scripts').glob('*.py')}
expected={p for p in tracked if p.endswith('.py') and p.count('/')==1}
assert actual==expected
script_delta=git('diff',head,'--name-only','--','scripts').decode().splitlines()
assert script_delta==[primary],script_delta
assert current['helper_runner_paths']==[]
assert graphfile.read_bytes()==graphbytes and manifestfile.read_bytes()==manifestbytes
out={'role':'Actual all-node citation topology comparison; not a fresh full graph build, producer receipt, audit, or current-main integration.',
 'old_graph_base':base,'current_branch_head':head,'old_graph_sha256':sha(graphbytes),
 'manifest_sha256':sha(manifestbytes),'manifest_bytes_unchanged':True,
 'discovered_note_count':len(notes),'node_count':len(newnodes),'edge_count':len(edges),
 'all_node_inventory_and_ordered_edges_equal':True,'all_manifest_entries_equal':True,
 'actual_source_hash_changes':hash_changes,'actual_changed_node':current,
 'policy_and_extractor_identities':policies,'actual_top_level_script_count':len(actual),
 'script_delta':script_delta,'changed_primary_actual_helpers':[],
 'note_identity_digest':sha(json.dumps(note_identities,sort_keys=True).encode()),
 'seconds':time.monotonic()-start}
f=pack/'graph/TOPOLOGY_RESULT.json';f.parent.mkdir(exist_ok=True)
if f.exists():raise SystemExit('Refusing to overwrite topology evidence')
f.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
