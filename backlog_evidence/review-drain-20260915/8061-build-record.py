from pathlib import Path
import sys,json,hashlib,subprocess,re,ast,gzip
r=Path('/private/tmp/review-drain-20260915');w=r/'author-pool/author-backlog';sys.path[:0]=[str(w/'docs/audit/scripts'),str(w/'scripts')]
import build_citation_graph as g,audit_packet_script_deps as a
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:{'path':str(p),'sha256':sha(p)};bind=lambda ps:[{'path':p,'sha256':sha(w/p)} for p in sorted(set(ps))];git=lambda *x:subprocess.check_output(['git','-C',str(w),*x],text=True).strip()
inv=json.loads((r/'check8061/inventory.json').read_text());f=json.loads((r/'8061-author-preexecution.json').read_text());assert git('write-tree')==f['tree'];assert not git('diff','--name-only')
for p,h in (f['source_paths']|f['inputs']).items():assert sha(w/p)==h,p
assert sha(r/'8061-author-capture.py')==f['capture_script_sha256']
anchors=json.loads((r/'8061-archive-anchor.json').read_text());pm=json.loads((r/'8061-proof-source-map.json').read_text());proofs={p for p in pm.values() if p.endswith('.md')};assert len(proofs)==5
rows={}
for c in inv['constituents']:
 pr=str(c['pr']);rows[pr]=[];entries={e['original_path']:e for e in json.loads(Path(anchors[pr]['manifest_path']).read_text())['entries']}
 modes={}
 for line in git('ls-tree','-r',c['head']).splitlines():
  info,p=line.split('\t');mode,typ,blob=info.split();modes[p]=(mode,blob)
 statuses={line.split('\t')[-1]:line.split('\t')[0] for line in git('diff','--name-status',c['merge_base'],c['head']).splitlines()}
 for p in c['paths']:
  path=p['path'];mode,blob=modes[path];target=None;encoding=None
  if path.startswith('.claude/'):
   e=entries[path];target=anchors[pr]['mapping'][path];encoding=e['encoding'];disposition='Exact historical proof/code/control/data and failed-attempt provenance, fully read or explicitly parsed as described in science report; historical verdicts are not authority.'
   if '/live_inputs/' in path:disposition='Exact current live finite geometry/target ledger, independently read and checked under8059; all rational rows require final canonical replay.'
  elif path in pm:
   target=pm[path];encoding='raw' if target.endswith('.md') else 'gzip';disposition='CURRENT supporting scientific proof fully reviewed under canonical8061, including all corollaries and premises; exact bytes linked and pinned, not autonomous.' if target in proofs else 'Historical projection review or original8058 autonomous snapshot preserved exactly; current8058 source is actual dependency, historical verdict is not authority.'
  elif '/audit/data/' not in path and path.startswith(('docs/','scripts/','outputs/')):
   target=path;disposition='Canonical source/input/output retained with only independently cold-reviewed execution/provenance packaging; full math and all input obligations reviewed. Final output awaits actual capture.'
  else:disposition='Generated citation manifest excluded from scientific authority; original fully read and recoverable in frozen Git/external original. Current main bytes preserved; coordinator combined gate regenerates.'
  row=dict(original_path=path,original_sha256=p['sha256'],original_mode=mode,original_git_blob=blob,status=statuses[path],final_path=target,final_sha256=sha(w/target) if target else None,disposition=disposition,recovery=c['head']+':'+path+'; '+str(r/f'check8061/original-{pr}'/path))
  if encoding:row['encoding']=encoding
  if target and encoding:
   raw=(w/target).read_bytes();raw=gzip.decompress(raw) if encoding=='gzip' else raw;assert hashlib.sha256(raw).hexdigest()==p['sha256'],path
  rows[pr].append(row)
assert sum(map(len,rows.values()))==814
controls=[ref(r/'check8061'/x) for x in ['inventory.json','control_gap.py','control_gap.json','control_ledger.py','control_ledger.json','read_vectors.py','read_vectors.json','read_vectors_prelaunch_failure.json','control_projection.py','control_projection.json','archive-check.json','authority-context.json','history-md-map.json','history-code-map.json','data-read-map.json']]
report=r/'review-8061-provisional.json';assert not report.exists()
review=dict(status='Complete original science review and corrected-source cold confirmation; actual full replay pending, no final verdict',reviewer_session='/root/review_8012',base=f['base'],tree=f['tree'],original_inventory=ref(r/'check8061/inventory.json'),constituent_dispositions=rows,source_hashes=f['source_paths'],actual_inputs=f['inputs'],supporting_proofs=sorted(proofs),working_science_report=ref(r/'review-8061-working.md'),controls=controls,archive_anchor=ref(r/'8061-archive-anchor.json'),proof_map=ref(r/'8061-proof-source-map.json'),capture_wrapper=ref(r/'8061-author-capture.py'),cold_confirmation='Final literal verified-byte loaders, isolated default full replay, historical-readiness distinction, input/manifest closure, runtime environment metadata, scopes and resource watchdog fully cold-read. No mathematical algorithm changed. Runtime NumPy/interpreter identities recorded by actual worker after execution, not inferred from supervisor.',current_main_preservation='All proposal paths are additions against current base; no inherited current-main source is overwritten. Two historical generated manifest modifications excluded.',full_pipeline_runs=0,audit_verdict=None)
report.write_text(json.dumps(review,indent=2)+'\n');rr=ref(report)
pairs={8059:('docs/NATIVE_L6_SIXTH_PREFIX_GAP_CERTIFICATE_NOTE_2026-09-08.md','scripts/native_l6_sixth_prefix_gap_certificate_2026_09_08.py'),8061:('docs/NATIVE_L6_NONLINEAR_STAR_VERTEX_NOTE_2026-09-09.md','scripts/native_l6_nonlinear_star_vertex_2026_09_09.py')}
paths=git('diff','--cached','--name-only').splitlines();notes=[];helpers=set();parents=set();runtime=set();context=set()
for pr,(n,primary) in pairs.items():
 body=(w/n).read_text();hs=g.helper_runner_paths_for_claim(g.claim_id_from_path(w/n),primary);assert set(hs)=={'scripts/'+x+'.py' for x in a.transitive_helpers(Path(primary).stem)};assert len(hs)==(2 if pr==8059 else 6)
 cs=sorted(p.relative_to(w).as_posix() for p in g.extract_citations(body,w/n));ps=[p for p in cs if '/work_history/' not in p and p.startswith('docs/')];parents.update(ps);context.update(set(cs)-set(ps));helpers.update(hs)
 for file in [primary,*hs]:
  runtime.add(file)
  for node in ast.parse((w/file).read_text()).body:
   if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in node.targets):runtime.update(ast.literal_eval(node.value))
 m=re.search(r'^claim_id: (.+)$',body,re.M)
 notes.append(dict(path=n,claim_id=g.claim_id_from_path(w/n),declared_claim_id=m[1] if m else None,claim_type=g.extract_claim_type_hint(body)[1],primary_runner=primary,helpers=sorted(hs),citations=cs,repository_dependencies=ps,dependency_rationale='Current supplied native dictionary, U0 endpoint/normalization,8051 dispersion and finite8059 denominator or8058 structural star theorem are linked actual source dependencies. Five exact8061 mathematical fragments are current supporting proofs. Woodbury/Newton/CAR/projection and explicit floating-operation hypotheses are mathematical inputs distinct from framework axioms. Historical acceptance receipts are integrity/provenance checks, not scientific authority.'))
context.update(['docs/MINIMAL_AXIOMS_2026-06-29.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json','docs/ai_methodology/skills/review-loop/SKILL.md','docs/ai_methodology/skills/review-loop/references/UNIT_RECEIPT.md','docs/ai_methodology/skills/no-go-discipline/SKILL.md','docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md'])
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/ai_methodology/skills/review-loop/scripts/review_receipt.py','docs/ai_methodology/skills/review-loop/scripts/review_workspace.py']
# Future canonical caches are linked but cannot be bound before their first actual run.
context={p for p in context if (w/p).exists()}
record=dict(schema_version=2,unit_id='PR8059-PR8061',constituents=[dict(id='PR'+str(c['pr']),head=c['head'],delta_base=c['merge_base'],dispositions=dict(rr,json_pointer='/constituent_dispositions/'+str(c['pr']))) for c in inv['constituents']],source=dict(base=f['base'],commit=git('rev-parse','HEAD'),tree=f['tree'],paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=bind(helpers),parents=bind(parents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8012',report=rr,references=controls+[review['working_science_report'],review['archive_anchor'],review['proof_map'],review['capture_wrapper']]),notes=notes,non_science_notes=[],supporting_proofs=[])
for p in paths:
 if not p.endswith('.md') or p in [x[0] for x in pairs.values()]:continue
 if p in proofs:
  body=(w/p).read_text();assert g.extract_claim_type_hint(body)[0] is None
  cs=sorted(x.relative_to(w).as_posix() for x in g.extract_citations(body,w/p));assert cs==[]
  record['supporting_proofs'].append(dict(path=p,canonical_note=pairs[8061][0],citations=cs,rationale='CURRENT scientific proof fully read and checked under8061: projection/corollaries, exact adapted space, four-solve transport, phase convention or elementary-operation error envelope. Not autonomous; premises and interaction included in owner review.',review_reference=rr))
 else:record['non_science_notes'].append(dict(path=p,rationale='Exact historical source/review/control provenance or recovery README, fully classified; no current claim or inherited review authority adopted.',review_reference=rr))
out=r/'8061-unit-preexecution-v2.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n');print(f['tree'],len(paths),len(runtime),len(record['supporting_proofs']))
