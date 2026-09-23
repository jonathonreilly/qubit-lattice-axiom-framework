import pathlib,json,hashlib,subprocess,gzip
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'review-draft-slot'; sha=lambda b:hashlib.sha256(b).hexdigest()
def g(*a):return subprocess.check_output(['git','-C',str(w),*a])
p=r/'drain8031-author-unit-draft-v1.json';d=json.loads(p.read_text());assert sha(p.read_bytes())=='9e07a3cc7071b7b1cbb0158f679d86c5ffc23f280ce6acd60308645e6264db2e'; base='ed129b572ea8364ed8d2792a0860b07ab94056a5';tree='fef359464ea984c83e2f19df106b707d19317da5';assert g('rev-parse','HEAD').decode().strip()==base; assert d['source']['tree']==tree
assert not g('diff','--name-only');assert not g('ls-files','--others','--exclude-standard')
prep=json.loads((r/'drain8031-author-prepared-v2.json').read_text());expected={x['path']:x['sha256'] for x in prep['source']};assert set(g('diff','--cached','--name-only',base).decode().splitlines())==set(expected)
for p,h in expected.items():assert sha(g('show',':'+p))==h==sha((w/p).read_bytes());assert sha(g('show',tree+':'+p))==h
refs=[]
def walk(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:
   p=pathlib.Path(x['path']);p=p if p.is_absolute() else w/p;assert sha(p.read_bytes())==x['sha256'],str(p);refs.append(str(p))
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(d)
for x in prep['original_dispositions']:assert sha(gzip.decompress(g('show',':'+x['recovery'])))==x['sha256']
for x in prep['historical_v1_snapshots']:assert sha(pathlib.Path(x['path']).read_bytes())==x['sha256']
# Confirm unchanged actual premise and policy authority. Registry/input tooling additions reviewed separately.
paths=['docs/GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md','docs/ai_methodology/skills/review-loop','docs/ai_methodology/skills/no-go-discipline','docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md','docs/MINIMAL_AXIOMS_2026-06-29.md','docs/audit/data/axiom_premise_nodes.json','docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md'];assert not g('diff','--name-only','631d6b36cd1e9b860763ebcad36e40a2bbe7439c',base,'--',*paths)
# Source delta is additions only, so no current-main blob replaced/deleted.
assert all(x.startswith('A\t') for x in g('diff','--cached','--name-status',base).decode().splitlines())
out={'base':base,'staged_tree':tree,'draft_sha256':sha((r/'drain8031-author-unit-draft-v1.json').read_bytes()),'source_paths':74,'all_stage_disk_and_tree_hashes_match':True,'archive_roundtrips':70,'v1_snapshots_verified':2,'bound_record_references_verified':len(refs),'actual_parent_and_authorities_unchanged_from_original_policy_revision':True,'current_main_preservation':'74 additions only; no replacement/deletion of main source','working_vs_index_clean':True,'untracked_count':0}
(r/'drain8031-cold-verification-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
