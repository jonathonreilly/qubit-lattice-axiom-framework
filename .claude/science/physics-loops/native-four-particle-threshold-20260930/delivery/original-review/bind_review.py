import datetime, hashlib, json, pathlib, subprocess
ROOT=pathlib.Path('/private/tmp/toe-native-four-particle-threshold-20260930')
OUT=pathlib.Path(__file__).parent
PACK='.claude/science/physics-loops/native-four-particle-threshold-20260930/'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(ROOT),*a]).decode().strip()
tree=git('write-tree');base='30a9461ee19a49b99fa6628fe942f08e504e8903'
assert tree=='d4774b427e5c9ed059d64dd01bc5aefc636c261e' and git('rev-parse','HEAD')==base
assert not git('diff','--name-only') and not git('ls-files','--others','--exclude-standard')
paths=git('diff','--cached','--name-only','--no-renames').splitlines()
roles={
'CHANGED_PATHS.json':'Explicit proposed-path inventory, reconciled against actual no-renames Git delta and hashes; not a coverage verdict.',
'COMPACT_SOURCE_DUALITY_FREEZE.json':'Historical author freeze of duality candidate; hash reconciled.',
'COMPACT_SOURCE_DUALITY_PRE.md':'Historical author scientific candidate, read in full and subsumed by the reviewed canonical argument; no independent current claim or review authority.',
'CONTRACT.md':'Author task and resource contract; does not grant science status.',
'FINAL_BINDINGS.json':'Final author source/evidence bindings independently checked against bytes.',
'FINAL_CHECKS.json':'Author focused-check record; current cache identities and historical checks reconciled; no independent verdict inferred.',
'GOVERNANCE_BINDINGS.json':'Procedure/authority identity record; selected procedure bytes independently compared.',
'HANDOFF.md':'Frozen author handoff with explicit pending review/integration; historical pending statement retained.',
'PRIOR_CONTEXT.json':'Dated neighboring-source/open-proposal retrieval record; no novelty or premise inference.',
'PROVENANCE.json':'Historical development/reuse and resource-limit disclosure; cited prior science is not used as a premise.',
'REVIEW_HISTORY.md':'Author preparation/conformance history, not an independent review.',
'STATE.yaml':'Author conditional-support checkpoint; no retention or audit authority.',
'TRACE_GATE.md':'Author positive-theorem scope and no-go applicability explanation, independently assessed.',
'VOCAB_REPORT.md':'Focused vocabulary report retained as historical mechanical evidence.',
}
def role(p):
 if p.startswith('docs/NATIVE_FOUR_PARTICLE_'):
  return 'Current scientific source: canonical claim' if 'BOUNDED_THEOREM' in p else 'Current scientific source: owned supporting proof, fully reviewed in canonical unit; never a non-science exemption'
 if p.startswith('scripts/'):
  return 'Current scientific implementation, entire source reviewed; exact primary/helper role and input closure checked'
 if p.startswith('outputs/'):
  return 'Controlled integer variational proposal; exact shape, integer data and byte identity checked; no optimizer-accuracy premise'
 if p.startswith('logs/'):
  return 'Current canonical source/input-bound execution cache; complete payload inspected, official freshness verified, no audit authority'
 if p=='docs/audit/data/citation_graph_manifest.json':
  return 'Allowed generated topology acknowledgment; actual base delta is three nodes/three edges and no old-node change; regenerate at integration'
 q=p.removeprefix(PACK)
 if q in roles:return roles[q]
 if q.startswith(('mutations/','mutations-footer/')):
  version='final current-source' if q.startswith('mutations-footer/') else 'historical pre-footer'
  if q.endswith('RESULTS.json'):return f'{version} aggregate mutation record: every listed mutation reconstructed and result/stdout/stderr reconciled'
  if q.endswith('mutation.txt'):return f'{version} explicit single-formula mutation description, inspected with actual replacement and hash'
  if q.endswith('result.json'):return f'{version} per-mutation result, checked against aggregate and source/output hashes'
  if q.endswith('stderr.txt'):return f'{version} actual assertion-failure traceback, inspected at intended mathematical assertion'
  if q.endswith('stdout.txt'):return f'{version} preserved empty stdout from rejected mutation; not missing successful evidence'
 if q.startswith('historical/before-footer/'):
  return 'Historical pre-footer source/cache/diff or encoding evidence; exact source deltas, gzip raw hashes and payload equivalence inspected; not current executable evidence'
 if q.startswith(('preexecution/','preexecution-final/','preexecution-footer/')):
  if q.endswith('INITIAL_CANONICAL_SOURCE.md'):return 'Historical initial scientific source; actual delta to full-read canonical source inspected, no current independent claim'
  if q.endswith('receipt.stderr.txt'):return 'Preserved empty stderr of successful historical author mechanical preflight'
  return 'Historical author schema-2 mechanical preflight/source freeze/receipt; actual tree source pins and record hash checked, expressly not independent reviewer standing'
 if q.startswith('execution-footer/'):return 'Final execution-envelope metadata; current canonical cache and preexecution identities reconciled'
 if q.startswith('execution/'):
  return 'Historical first-run/environment/comparison metadata; disclosed author reuse, raw old cache and current payload compared; no independent proof claim'
 if q.startswith('graph/'):
  return 'Graph-generation or footer-equivalence evidence; actual manifest delta and script-only footer changes independently checked; not full combined validation'
 raise AssertionError(p)
dispositions=[]
for p in paths:
 h=sha(ROOT/p);r=role(p)
 dispositions.append({'original_path':p,'original_sha256':h,'disposition':'accepted unchanged','recovery':f'Original staged Git tree {tree}:{p}; source worktree {ROOT}; no deletion or replacement authorized by this report.','final_path':p,'final_sha256':h,'reviewed_role':r})
report_ref={'path':str(OUT/'ORIGINAL_REVIEW.md'),'sha256':sha(OUT/'ORIGINAL_REVIEW.md')}
parent='docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md'
canonical='docs/NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md'
proofs=[p for p in paths if p.startswith('docs/NATIVE_FOUR_PARTICLE_') and p!=canonical]
context=['docs/MINIMAL_AXIOMS_2026-06-29.md','docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json','docs/audit/data/premise_decision_history.json','docs/repo/DEFERRED_DECISIONS.md','docs/repo/CONTROLLED_VOCABULARY.md','docs/repo/REVIEW_FEEDBACK_WORKFLOW.md','docs/repo/ACTIVE_REVIEW_QUEUE.md','docs/CANONICAL_HARNESS_INDEX.md','docs/audit/README.md','docs/ai_methodology/SCIENCE_WORKFLOW.md']
gov=json.loads((ROOT/PACK/'GOVERNANCE_BINDINGS.json').read_text())
context+= [x['path'] for x in gov['selected_procedures_unchanged_on_science_base'] if x['path'].startswith('docs/ai_methodology/skills/review-loop/') or x['path'] in ['docs/ai_methodology/skills/no-go-discipline/SKILL.md','docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md','docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md','docs/ai_methodology/skills/physics-loop/references/assumption-import-audit.md','docs/ai_methodology/skills/physics-loop/references/CLAIM_STATUS.md','docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md']]
bind=lambda ps:[{'path':p,'sha256':sha(ROOT/p)} for p in sorted(set(ps))]
record={'reviewer_session':'/root/native_four_particle_source_review','requested_configuration':{'model':'gpt-6-astra','reasoning_effort':'low'},'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_verdict':'PASS WITH BOUNDED CLAIMS','scope':'Original frozen staged source only; final committed head and combined integration gates pending','material_findings':[],'findings_fixed':0,'known_findings_skipped':0,'original_base':base,'original_head':base,'original_tree':tree,'reviewed_local_origin_main':git('rev-parse','origin/main'),'selected_procedure_revision':gov['selected_revision'],'report':report_ref,'original_dispositions':dispositions,'source_paths':bind(paths),'inputs':{'runtime':bind(proofs+['outputs/native_four_particle_threshold_2026_09_30/compact_trial.json']),'helpers':bind(['scripts/native_four_particle_normalization_2026_09_30.py']),'parents':bind([parent]),'context':bind(context),'tooling':bind(['scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','docs/audit/scripts/ledger_io.py','docs/ai_methodology/skills/review-loop/scripts/review_receipt.py'])},'supporting_proofs':[{'path':p,'canonical_note':canonical,'rationale':'Current scientific proof fully read and independently checked as part of the single supplied-model theorem.','review_reference':report_ref} for p in proofs],'non_science_notes':[{'path':p,'rationale':role(p),'review_reference':report_ref} for p in paths if p.endswith('.md') and not p.startswith('docs/NATIVE_FOUR_PARTICLE_')],'checks_run':['Manual independent occupation/projector, compact-source duality, capacity, normalization, guarded frame, Schur and physical logarithmic-cutoff derivations','Exact rational cached 15x15 form inspection and directional contractions; no proposed scientific function imported','All 18 historical/current mutation source hashes and actual assertion failures reconciled','All original path byte/index identities, author inventory, final bindings and historical preflight tree pins reconciled','Historical gzip roundtrip and old/new scientific payload equivalence','Official primary/helper cache freshness and timeout/input metadata','Focused in-memory compile and working/staged/base-to-HEAD whitespace checks'],'checks_not_run':['No identical successful primary/helper rerun','No new full mutation execution; actual source-matching successful mutation evidence inspected','No full pipeline, strict lint, changed-evidence gate or current-main integration','No independent audit or final committed-head confirmation'],'evidence':[{'path':str(OUT/p),'sha256':sha(OUT/p)} for p in ['check_evidence.py','EVIDENCE_INSPECTION.json']],'current_main_preservation':'At checked local origin/main equal to source base, all existing science unchanged; only topology manifest modified. Future integration/current-main movement must be inspected separately.','audit_referral_claim_id':'native_four_particle_threshold_bounded_theorem_note_2026-09-30','full_pipeline_count':0,'integration_retries':0,'commits_created':[]}
(OUT/'ORIGINAL_REVIEW.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'report':report_ref,'json':{'path':str(OUT/'ORIGINAL_REVIEW.json'),'sha256':sha(OUT/'ORIGINAL_REVIEW.json')},'dispositions':len(dispositions),'tree':tree},indent=2))
