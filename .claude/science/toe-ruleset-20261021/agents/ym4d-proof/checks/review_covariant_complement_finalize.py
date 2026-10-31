"""Mechanical review freeze; never executes or rewrites author mathematics."""
from pathlib import Path
import ast, datetime, hashlib, json, re, subprocess, sys
L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof'); B=L/'checks'; P='review_covariant_complement_'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def identity(p, **extra):
 p=Path(p); return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,**extra)
def put(name,d): (B/(P+name+'.json')).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def read(name): return json.loads((B/name).read_text())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
entry=read(P+'entry.json'); ar=read('covariant_complement_receipt.json'); am=read('covariant_complement_read_manifest.json')
expected_receipt='a9536686abb45d8f5fae790fd0c7685ce159a1a0f961cd8cdcd5145fb31d22d4'
assert sha(B/'covariant_complement_receipt.json')==expected_receipt
pins=[]
for item in ar['artifacts']+am['inputs']:
 got=sha(item['path']); pins.append(dict(path=item['path'],expected=item['sha256'],actual=got,match=got==item['sha256']))
mismatches=[x for x in pins if not x['match']]
assert len(pins)==36 and len(mismatches)==1
assert mismatches[0]['path']==str(L/'LITERATURE_BRIDGES.md')
assert mismatches[0]['expected']=='282318a0c398d49a8c69bc1f2173c90ef463634beaba55e2f4d2792af8b64815'
assert mismatches[0]['actual']=='ae281c9e310a4b4b21f6a5347813ead4d279967e03ef4b1fee82f64a4a26fcb1'
# Narrow exception documented after human/analytic review of non-load-bearing context.
assert all(x['match'] for x in entry['packet_verification'])
cover={
 'PROCESS_LIGHT.md':'Full owner process; supersedes inconsistent lane workflow. Independent source review only; coordinator owns Git and integration.',
 'COVARIANT_SOURCE_ACTIVITY_ASTRA.md':'Lines1-104 and508-635: definitions/SA4 and scope/remaining complement SA28-SA33. Its selected-sector proof is not a premise of this unit and is not independently certified here.',
 'covariant_source_activity_receipt.json':'Full frozen metadata and artifact inventory. Hash identity only; no checker or proof coverage inherited.',
 'COVARIANT_SOFT_BACKGROUND_ASTRA.md':'Lines1-215: CB1-CB8 definitions, path means and local coordinates. No stronger covariance/mixing theorem imported.',
 'SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md':'Lines1-730: entire argument through H28, definitions H1-H15, source domain H19-H20c, actual gas H21-H25, joint consumer and beginning of evidence. Later evidence narrative not needed or claimed read.',
 'REVIEW_SOURCE_HISTORY_RETURN_ASTRA.md':'Full report. Adopt only exact reviewed H identities and pointwise gas convergence at their stated assumptions; no whole-PR or outer-sea result.',
 'SOURCE_SEA_CONSTRUCTION_ASTRA.md':'Lines1-365: Sea1-Sea16 and exact integrated-V reference. Comparison consumer only; no fixed-V theorem imported.',
 'REVIEW_SOFTHARD_R2.md':'Full report; exact current-versus-next-variable return mismatch and open sea consumer.',
 'HIST.md':'Lines270-288: joint next-level interior integration and unchanged exterior convention. No complete HIST theorem reviewed.',
 'PLD.md':'Lines481-505: section9.4 SC-k normalized sea logarithm and derivative consumer.',
 'LARGE55.md':'Lines488-527 and725-744: invariant action/reference obligations I1-I9 and E13/E14 boundary-price consumers.',
 'LITERATURE_BRIDGES.md':'Lines1-22: bounded register scope and B01-B12, chiefly B03/B06/B07 relevant to localization and gauge context. Not an exhaustive literature read.',
 'ASSUMPTIONS_AND_IMPORTS.md':'Full current register: mathematical model data, theorem imports versus comparisons, no new adopted physical primitive.',
 'review_source_history_literature.md':'Full local primary-reading ledger, checked as source attribution; its external coverage is not represented as this reviewer own coverage.',
 'uniform_one_loop_read_manifest.json':'Lines1-130 and165-182: inventory/provenance context and exact methodology fields. No listed proof or external read is inherited as reviewer coverage.'}
rows=[]
for item in am['inputs']:
 rows.append(identity(item['path'],read_coverage=cover[Path(item['path']).name],author_frozen_sha256=item['sha256'],frozen_pin_verified_at_entry=True,changed_since_author_freeze=sha(item['path'])!=item['sha256']))
rows += [identity(L/'COVARIANT_COMPLEMENT_ASTRA.md',read_coverage='Complete527-line source: lines1-520 plus final8lines; CC1-CC23 and all evidence/scope/attribution statements.'),identity(L/'PROOF.md',read_coverage='Lines1158-1218 and2214-2284: actual S1-S4 conventions, Decision4 paired-root normalized compact kernel and normalizer.'),identity(L/'RLARGE.md',read_coverage='Lines270-310 and880-925: actual defect/completion definitions and remaining localization context; no full RLARGE theorem imported.')]
method=[]
for x in entry['methodology_identities']:
 p=Path(x['path'])
 if p.exists():
  cov='Read applicable reference; local bytes checked equal fetched main at entry.'
  if p.name=='REVIEW_UNITS.md': cov='Read initial scope plus full relevant original-review, frozen-input, per-unit and combined integration rules, including reread90-155. No canonical integration receipt or combined gate claimed.'
  if p.name=='UNIT_RECEIPT.md': cov='Schema reference inspected in initial batch with truncation; no complete-schema reading or canonical receipt validation claimed. This is a source-review evidence receipt; canonical enrollment remains coordinator-owned.'
  method.append(identity(p,read_coverage=cov,entry_sha256=x['sha256']))
for path,cov in [
 ('AGENTS.md','Full applicable worktree instructions.'),
 ('docs/MINIMAL_AXIOMS_2026-06-29.md','Full active axiom document; target is conditional model analysis, no primitive adoption.'),
 ('docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','Full primitive-check methodology.'),
 ('docs/audit/data/axiom_premise_nodes.json','Full premise-node registry; read-only.'),
 ('docs/audit/data/premise_decision_history.json','Full decision history; read-only.'),
 ('docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md','Full applicable proof-search governance.'),
 ('docs/repo/REVIEW_FEEDBACK_WORKFLOW.md','Full workflow; no shared queue writes.'),
 ('docs/repo/ACTIVE_REVIEW_QUEUE.md','Lines1-85 current workflow/context; no queue-wide disposition.'),
 ('docs/repo/DEFERRED_DECISIONS.md','Lines1-85 plus visible86-205 context with some batch output truncation; no deferred adoption consumed.'),
 ('docs/repo/CONTROLLED_VOCABULARY.md','Relevant initial naming rules and reread88-115; initial batch had partial truncation.'),
 ('docs/CANONICAL_HARNESS_INDEX.md','Initial entries and bounded index context; no unrelated retained-lane theorem consumed.'),
 ('docs/audit/README.md','Lines1-100: audit boundaries; no verdict assigned.'),
 ('/Users/jonBridger/.codex/skills/review-loop/SKILL.md','Full installed skill router; current-main methodology and PROCESS_LIGHT control task scope.')]:
 if Path(path).exists(): method.append(identity(path,read_coverage=cov))
external=[
 dict(url='https://arxiv.org/html/1410.2798v3',identity='Dimock, A Covariant Axial Gauge',read_coverage='Abstract/introduction and sections2.1-2.2, web lines35-145 including tree constraints/Prop1. No whole-paper read.',role='Attribution and abelian/dimension mismatch; no nonabelian theorem imported.'),
 dict(url='https://arxiv.org/html/1212.5562v2',identity='Dimock, The Renormalization Group According to Balaban II. Large Fields',read_coverage='Introduction/model web lines58-129 and AppendixF lines3090-3155, equations633-646.',role='Independent-site/small-localized-interaction hypothesis comparison; no outer-cut-law theorem imported.'),
 dict(url='https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf',identity='Balaban, CMP116 (1988), DOI10.1007/BF01239022',read_coverage='Original scan parsed text printedpages1-2, lines0-80; incidental beginning of page3 visible. Not whole paper; no PDF-byte hash.',role='Localization then exponentiation architecture; no detailed lemma imported.'),
 dict(url='https://doi.org/10.1007/BF01239022',access='Failed tool retrieval; original scan alternate used. Not mathematical counterevidence.')]
put('read_manifest',dict(created_utc=now,reviewer=entry['reviewer'],source_inputs=rows,methodology=method,author_artifact_reads='Complete source, complete main/posthoc checker and criteria, current launcher, receipt/read manifest, main/posthoc mathematical results, and recorded runtime/parser failures. Empty stderr/stdout checked by byte length. Original JSON-lines output parsed mechanically, with mathematical records fully reviewed in results JSON. Hash identity is not a proof of reading.',external_reads=external,independence='Independent analytic plan, preregistered numerical criteria, implementation and19/19 run preceded author-checker/criteria exposure. Target aggregate outcomes were known. Same-family fresh context. Later author replays are reproductions.',concurrent_changes='Root reports unrelated SA/UL/TSE review integration and Claude REC_CONT HOLD/REC_LIB status update. None is a CC premise; no new such theorem consumed. All21 author artifacts and other14 inputs remain exact. LITERATURE_BRIDGES original282318... pin was verified at entry; currentae281... changes navigation/SA-UL review status only, confirmed by root and scoped reread. No source evidence is restamped.'))
orig=read('covariant_complement_01_results.json'); replay=read(P+'author_results.json')
without_time=lambda d:{k:v for k,v in d.items() if k!='elapsed_seconds'}
assert without_time(orig)==without_time(replay)
post=read('covariant_complement_posthoc_results.json'); post_rep=read(P+'posthoc_results.json'); assert post==post_rep
assert (orig['passed'],orig['total'],orig['mutations'])==(23,24,6)
failed=[x for x in orig['records'] if not x['passed']]; assert len(failed)==1 and failed[0]['name']=='actual_boundary_shell_u40'
assert (post['passed'],post['total'],post['posthoc'])==(3,3,True)
ind=read(P+'independent_01.stdout.json'); assert len(ind['checks'])==19 and all(x['pass'] for x in ind['checks'])
# Raw author stdout uses one JSON object per line, followed by an aggregate.
raw_lines=(B/'covariant_complement_02_output.txt').read_text().splitlines()
parsed_raw=[json.loads(s) for s in raw_lines if s.strip()]
assert len(parsed_raw)==25
assert parsed_raw[:24]==orig['records']
assert json.loads((B/'covariant_complement_posthoc03_output.txt').read_text())==post
runs=[]
for name,exit_code in [('independent_01',0),('author_01',1),('posthoc_01',0)]:
 r=read(P+name+'_run.json'); g=read(P+name+'_gate.json')
 assert r['exit_code']==exit_code and r['termination_reason'] is None
 assert g['passes'] and g['system_wide_free_percentage']>=50 and g['load1']<20
 assert r['peak_rss_kib']<300*1024 and Path(r['stderr']).stat().st_size==0
 runs.append(dict(name=name,execution=r,gate=g))
report=L/'REVIEW_COVARIANT_COMPLEMENT_ASTRA.md'
# Remove an unnecessary unverified fragment from the actual known primary URL.
report.write_text(report.read_text().replace('https://arxiv.org/html/1212.5562v2#A6','https://arxiv.org/html/1212.5562v2'))
receipt_path=B/(P+'receipt.json'); receipt_path.write_text('{}\n')
links=[]; missing=[]
for p in [report,L/'COVARIANT_COMPLEMENT_ASTRA.md',B/(P+'criteria.md')]:
 clean='\n'.join(line for line in p.read_text().splitlines() if not line.startswith('    '))
 clean=re.sub(r'`[^`]*`','',clean)
 for dest in re.findall(r'\]\(([^)\n]+)\)',clean):
  if re.match(r'^(https?://|#)',dest):continue
  dest=dest.split('#')[0]; resolved=(p.parent/dest).resolve(); ok=resolved.exists()
  links.append(dict(source=str(p),target=dest,exists=ok))
  if not ok: missing.append(dest)
assert not missing, missing
pyfiles=sorted(B.glob(P+'*.py'))
for p in pyfiles: ast.parse(p.read_text(),filename=str(p))
trailing=[]
for p in [report,*B.glob(P+'*.md'),*pyfiles]:
 for n,line in enumerate(p.read_text().splitlines(),1):
  if line.rstrip()!=line:trailing.append((str(p),n))
assert not trailing,trailing
paths=[str(report),str(L/'COVARIANT_COMPLEMENT_ASTRA.md'),str(B/(P+'*')),str(B/'covariant_complement_*')]
diffs=[]
for flags in [[],['--cached'],['origin/main...HEAD']]:
 cmd=['git','diff','--check',*flags,'--',*paths]
 p=subprocess.run(cmd,capture_output=True,text=True); assert p.returncode==0,(cmd,p.stderr,p.stdout)
 diffs.append(dict(command=cmd,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
put('verification',dict(utc=now,source_author_artifact_and_input_pins=pins,author_receipt_sha256=expected_receipt,author_records_exact_except_elapsed_time=True,main_failed_predicate_retained=failed,posthoc_exact=True,independent_total=19,original_stdout_matches_results=True,links=links,python_ast_files=[str(p) for p in pyfiles],trailing_whitespace=[],scoped_diff_checks=diffs,diff_scope='Untracked author/reviewer content is excluded from Git diffs and separately byte/hash/link/AST/whitespace checked. These are not the coordinator integration gate.',mechanical_read_error='One read used missing skills/review-loop/references/REVIEW_UNITS.md; corrected to docs/ai_methodology/skills/review-loop/references/REVIEW_UNITS.md. No mathematics executed or evidence changed.',head_at_freeze=head))
owned=[report]+sorted(p for p in B.glob(P+'*') if p.is_file() and p!=receipt_path)
receipt=dict(schema='source-review-evidence-v1; not canonical integration receipt',frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer=entry['reviewer'],verdict='LAND',scope='Frozen bounded CC1-CC23 original-law local density/shell unit, CC19 away from full failure readers, CC20-CC21 raw Re(epsilon) envelope; no whole complement/normalized sea/RG/continuum/gap conclusion.',report=identity(report),author_receipt=identity(B/'covariant_complement_receipt.json'),author_source=identity(L/'COVARIANT_COMPLEMENT_ASTRA.md'),author_read_manifest=identity(B/'covariant_complement_read_manifest.json'),owned_files=[identity(p) for p in owned],source_inputs=rows,execution_summaries=runs,independent=dict(passed=19,total=19,mutation_predicates=4,formal_proof=False),author_replay=dict(passed=23,total=24,mutation_predicates=6,exit_code=1,mathematical_records_exact=True,failed_predicate='actual_boundary_shell_u40',failed_ratio=failed[0]['data']['successive_ratios'][0]),posthoc_replay=dict(passed=3,total=3,posthoc=True,retroactive_pass=False),binding_findings=0,source_fix_iterations=0,preserved_failure_records=['covariant_complement_01_stderr.txt','covariant_complement_01_output.txt','covariant_complement_01_results.json','covariant_complement_packaging_failure01.json',P+'environment_probe_failure.json',P+'packaging_failure01.json'],review_iteration_count=1,author_artifacts_unchanged=21,original_input_pins_unchanged=14,context_input_changed=mismatches[0],context_change_disposition='Original author register identity preserved; root confirms table/navigation/review-status changes only. Consumed B03/B06/B07 unchanged. Current register separately snapshotted; no new SA/UL premise or math re-execution.',source_exposure=entry['source_exposure'],head_at_entry=entry['head_at_entry'],head_at_freeze=head,methodology_ref=entry['methodology_ref'],primitives_adopted=[],full_theory_status=dict(continuum_existence='OPEN',physical_continuum_mass_gap='OPEN'),operations='Reviewer edits confined to designated report and checks/review_covariant_complement_*. No Git commit/push, author source mutation, audit/ledger/axiom/shared-status write. Coordinator lock read only. Receipt excludes its own hash to avoid circularity; caller must pin final receipt hash.')
receipt_path.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
assert all(sha(x['path'])==x['sha256'] for x in receipt['owned_files'])
assert all(Path(x['source']).exists() and (Path(x['source']).parent/x['target']).exists() for x in links)
print(json.dumps(dict(verdict='LAND',report=identity(report),receipt=identity(receipt_path),owned_files=len(owned),author_pins=len(pins),independent='19/19',author_replay='23/24',posthoc='3/3 separately',head=head),indent=2))
