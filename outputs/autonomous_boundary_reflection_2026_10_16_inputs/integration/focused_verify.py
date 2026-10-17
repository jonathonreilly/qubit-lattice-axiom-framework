from pathlib import Path
import datetime, hashlib, json, re, sys, py_compile
N=Path(__file__).resolve().parents[1]; W=N.parent/'correlation_worktree'; D=N/'reflection_integration'
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
import runner_cache, build_citation_graph, forensic_evidence_readiness, no_go_discipline_gate
F=W/'outputs/autonomous_boundary_reflection_2026_10_16_inputs'
Q=W/'.claude/science/physics-loops/toe-autonomous-boundary-reflection-20261016'
primary='scripts/autonomous_boundary_reflection_2026_10_16.py'
note='docs/AUTONOMOUS_BOUNDARY_REFLECTION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
manifest=json.loads((F/'ARTIFACT_MANIFEST.json').read_text())
for rel,pin in manifest['files'].items():
 b=(F/rel).read_bytes(); assert len(b)==pin['bytes'] and hashlib.sha256(b).hexdigest()==pin['sha256'],rel
s=json.loads((Q/'SOURCE_MANIFEST.json').read_text()); nb=(W/note).read_bytes()
assert hashlib.sha256(nb).hexdigest()==s['note']['sha256']
for b in s['unchanged_bodies']:
 raw=(W/b['source']).read_bytes(); assert nb[b['body_byte_start_inclusive']:b['body_byte_end_exclusive']]==raw
 assert len(raw)==b['bytes'] and hashlib.sha256(raw).hexdigest()==b['sha256']
r=json.loads((W/'outputs/autonomous_boundary_reflection_2026_10_16.json').read_text())
for rel,h in r['input_sha256'].items(): assert hashlib.sha256((W/rel).read_bytes()).hexdigest()==h,rel
helpers=build_citation_graph.resolve_helper_runner_paths(primary)
assert helpers==['scripts/autonomous_boundary_reflection_check_2026_10_16.py'],helpers
row={'claim_id':'autonomous_boundary_reflection_bounded_theorem_note_2026-10-16','note_path':note,'runner_path':primary,'helper_runner_paths':helpers,'claim_type':'bounded_theorem'}
issue=forensic_evidence_readiness.cached_row_readiness_issue(row,{row['claim_id']:row},W); assert issue is None,issue
cache=runner_cache.cache_status(primary); assert cache=='fresh',cache
compiled=[]
for rel in [primary,*helpers]:
 py_compile.compile(str(W/rel),cfile=str(D/(Path(rel).name+'.pyc')),doraise=True);compiled.append(rel)
links=[]
for p in [W/note,*Q.glob('*.md')]:
 text=re.sub(r'```.*?```', '', p.read_text(), flags=re.S)
 text=re.sub(r'`[^`]*`', '', text)
 for target in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)',text):
  if target.startswith(('http:','https:','#')):continue
  dest=(p.parent/target.split('#')[0]).resolve();assert dest.is_file() and not dest.is_symlink(),(p,target)
  links.append({'source':str(p.relative_to(W)),'target':str(dest.relative_to(W))})
mut=json.loads((F/'mutations/RESULTS.json').read_text())
assert len(mut['cases'])==10
for c in mut['cases']:
 assert c['exit_code']==1 and c['scientific_assertion_rejected'],c['name']
 # Complete stderr was previously reviewed; verify archived streams retain those exact bytes.
 for stream in ['stdout','stderr']:
  p=F/'mutations'/c['name']/stream
  b=p.read_bytes();assert len(b)==c[stream]['bytes'] and hashlib.sha256(b).hexdigest()==c[stream]['sha256'],str(p)
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'artifact_hashes_verified':len(manifest['files']),'unchanged_bodies':len(s['unchanged_bodies']),'canonical_result_input_hashes':r['input_sha256'],'helper_discovery':helpers,'declared_inputs':runner_cache.declared_input_paths(W/primary),'deterministic_readiness_issue':issue,'cache_status_separately_checked':cache,'no_go_gate_trigger':no_go_discipline_gate.source_requires_no_go_discipline(note,nb.decode(),'bounded_theorem'),'compiled_sources':compiled,'relative_regular_file_links':links,'mutation_cases_and_archived_streams':len(mut['cases']),'scope':'Deterministic packaging and finite execution evidence only; no independent retained audit or general all-future numerical verification.'}
(D/'FOCUSED_VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['relative_regular_file_links','canonical_result_input_hashes']},indent=2))
