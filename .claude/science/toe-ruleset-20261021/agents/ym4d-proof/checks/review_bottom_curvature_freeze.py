#!/usr/bin/env python3
"""Bind this scoped review's actual inputs, coverage and diagnostic attempts.

No Git mutation, source repair, audit action, or science rerun. The receipt is
intentionally excluded from its own artifact list. Coverage is declared from
this review's reads; hashing a file is never treated as reading its proof.
"""
from pathlib import Path
import ast, datetime, hashlib, json, os, platform, re, subprocess, sys
import numpy, scipy
ROOT=Path('/Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972')
assert Path.cwd()==ROOT
L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C=L/'checks'
PREFIX='review_bottom_curvature_'
PIN='ca2bc7ddf64790da96cd43d42017d000fbfe4808'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def bind(p):
 p=Path(p);b=p.read_bytes()
 return dict(path=str(p),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def assert_binding(d):
 p=Path(d['path']);b=bind(p)
 assert b['sha256']==d['sha256'],(str(p),'hash changed')
 if 'bytes' in d:assert b['bytes']==d['bytes'],(str(p),'length changed')
 return b
expected={
 'BOTTOM_SECOND_CURVATURE_ASTRA.md':'b735eb1d551c9ba80925c0d22830b17ce823735bf7d9ac5d2e19ddabb2ff3ade',
 'CHARGED_STATIONARY_JET_ASTRA.md':'85b91738993f09f7e40a49f4c957c164a684bf499185629a82775229f6437254',
 'REVIEW_CHARGED_STATIONARY_JET_ASTRA.md':'f7e02d766c8885dceeeac8d2264784cdc65b85a771ae556efa5935d45236836d',
 'UNIFORM_SOFT_MINIMIZER_ASTRA.md':'203d4edbf97078d88fcb488f164e525d2671fe5a2a910c5f6e49f615e8f41bfe',
 'checks/bottom_second_curvature_receipt.json':'88d659a2a512fcc57b95dc077836ceb555dbeea177be36cde0abf4f6d0f977b4',
 'checks/bottom_second_curvature_source_manifest.json':'8d68afd95ce5cb2315977a06f8590555b739bc80bdee2afa18eda38388a9ee67',
 'checks/review_charged_jet_receipt.json':'ad4226851b1b1d7b29e87f19c42c18a021fd8dd7afbfb5a85eeff5007120962d',
 'checks/review_bottom_curvature_criteria.md':'9ba18d42b79c3a208a8c04b74f3aaca229b9db876e408440e541b724da5f7e79',
 'checks/review_bottom_curvature_supplement_criteria.md':'0516b59d3b02f43cd1abde0ee9c206e94add350a8d54fcc6457ac21608cda439'}
for p,h in expected.items():assert bind(L/p)['sha256']==h,(p,'frozen input mismatch')
orig=json.loads((C/'bottom_second_curvature_receipt.json').read_text())
up=json.loads((C/'review_charged_jet_receipt.json').read_text())
original_verified=[assert_binding(d) for d in orig['owned_artifacts']]
upstream_verified=[assert_binding(d) for d in up['owned_artifacts']]

full=['BOTTOM_SECOND_CURVATURE_ASTRA.md','CHARGED_STATIONARY_JET_ASTRA.md',
 'REVIEW_CHARGED_STATIONARY_JET_ASTRA.md','UNIFORM_SOFT_MINIMIZER_ASTRA.md',
 'checks/review_uniform_soft_scope_confirmation.md','PROCESS_LIGHT.md']
selected={
 'LINEAR_PACKAGE.md':[(52,174),(175,290),(475,538)],
 'PROOF_session16_snapshot.md':[(2380,2505),(2649,2798),(3230,3239)],
 'TUNIF.md':[(160,320),(321,440)],
 'CODEX_REVIEW_TUNIF2.md':[(1,255)],
 'REVIEW55_TUNIF.md':[(190,276)],
 'NQ_DEF.md':[(1,140),(203,288)],
 'REVIEW_S13_S14.md':[(75,122)],
 'REVIEW_S15_CONVERGENCE.md':[(1,65)],
 'NORMS.md':[(480,577)],
 'FLOW55.md':[(250,355),(562,576)],
 'UIR55.md':[(298,340)]}
reads=[]
for f in full:
 p=L/f;reads.append({**bind(p),'coverage':'complete','lines':len(p.read_text().splitlines()),'purpose':'source proof or explicit scope/process contract'})
for f,ranges in selected.items():
 p=L/f;lines=p.read_text().splitlines(keepends=True)
 slices=[]
 for a,b in ranges:
  s=''.join(lines[a-1:b]).encode()
  slices.append(dict(first_line=a,last_line=b,sha256=hashlib.sha256(s).hexdigest(),bytes=len(s)))
 reads.append({**bind(p),'coverage':'selected actual proof/consumer sections only','read_slices':slices})
for f in ['checks/bottom_second_curvature_receipt.json','checks/bottom_second_curvature_source_manifest.json','checks/bottom_second_curvature_attempts.json']:
 reads.append({**bind(L/f),'coverage':'complete metadata; no authority transferred to uninspected referenced proofs'})
reads.append({**bind(C/'review_charged_jet_receipt.json'),'coverage':'parsed binding fields and artifact list; complete upstream report separately read'})
for f in ['01','02']:
 reads.append({**bind(C/f'bottom_second_curvature_{f}.py'),'coverage':'complete, only after all independent scientific runs finished'})
 reads.append({**bind(C/f'bottom_second_curvature_{f}_out.json'),'coverage':'complete machine parse and exact reproduction comparison; not independent evidence'})
 reads.append({**bind(C/f'bottom_second_curvature_{f}_err.txt'),'coverage':'complete; empty'})
reads.append({**bind(C/'bottom_second_curvature_criteria.md'),'coverage':'complete after independent runs'})
reads.append({**bind(Path('AGENTS.md')),'coverage':'complete local repository instructions'})
installed=[]
for skill in ['physics-loop','review-loop']:
 p=Path('/Users/jonBridger/.codex/skills')/skill/'SKILL.md'
 installed.append({**bind(p),'coverage':'complete; reconciled against pinned authority'})
pinned_paths=[
 'docs/ai_methodology/SCIENCE_WORKFLOW.md',
 'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',
 'docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md',
 'docs/ai_methodology/skills/physics-loop/SKILL.md',
 'docs/ai_methodology/skills/review-loop/SKILL.md',
 'docs/audit/data/axiom_premise_nodes.json',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md',
 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md']
pinned_paths += ['docs/ai_methodology/skills/physics-loop/references/'+f for f in ['DISCOVERY.md','CLAIM_STATUS.md','DELIVERY.md','proof-search-governance.md']]
pinned_paths += ['docs/ai_methodology/skills/review-loop/references/'+f for f in ['REVIEW_SETUP.md','REVIEW_UNITS.md','SCIENCE_LENSES.md','FIXES_AND_REPORTING.md','AUDIT_COMPATIBILITY.md']]
method=[]
for p in pinned_paths:
 b=git('show',PIN+':'+p)
 method.append(dict(path=p,revision=PIN,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),coverage='complete pinned git-show read; truncated initial batches were followed by complete smaller reads'))
literature=[
 dict(authors='Luciano Abadias and Marta De Leon-Contreras',url='https://link.springer.com/article/10.1007/s00028-022-00851-1',coverage='Lemma 2.6, its proof, adjacent Remark 2.5 and warning; web text lines 394-440',role='Comparison only. Unweighted integer-lattice l1 differences; BC10-14 rebuild the weighted complex-cell argument. No global Gaussian pointwise estimate imported.',retrieval='successful primary HTML'),
 dict(authors='J. S. Dowker',url='https://arxiv.org/pdf/1207.2096v2',coverage='Section 2 defining generator/Bessel kernel; phase setup and equations (13)-(15), PDF pages 2-3 and 5-6 (1-based)',role='Real-phase image/Fourier normalization comparison. Complex character and d4 product proved in the source, not imported.',retrieval='successful primary PDF text'),
 dict(authors='Emmanuel Michta and Gordon Slade',url='https://alea.impa.br/articles/v19/19-38.pdf',coverage='Definitions (1.1)-(1.3), Lemma 2.1 and its proof (2.3)-(2.5), PDF pages 1-2 and 9-10 (1-based)',role='Scalar infinite-lattice normalization and heat/Bessel comparison only; no Appendix B or asymptotic result used. Surrounding search snippets are not whole-paper read coverage.',retrieval='successful primary PDF text')]
manifest=dict(schema='scoped-source-review-read-manifest-v1',created_utc=NOW,methodology_revision_at_start=PIN,
 late_process_decision={**bind(L/'PROCESS_LIGHT.md'),'coverage':'complete','owner_reported_commit':'43ac056899','application':'explicit grandfather clause for this already-running lane'},
 requested_reviewer='gpt-6-astra/max/fork-none',backend_identity_independently_verified=False,
 exposure='Source-exposed fresh context; coordinator brief and numerical summaries known before criteria. No author/predecessor checker implementation seen until independent runs completed.',
 local_reads=reads,installed_skills=installed,pinned_methodology_reads=method,primary_literature= literature,
 coverage_limits=['No full-PR review or audit assignment.','Selected supporting reads are not complete-file certification.','Author freeze code and raw read-slices verified by hash only, not reviewed as implementations.','No fresh theorem imported from historical Dimock/Balaban/BGM or Dybalski-Stottmeister-Tanimoto screening.','Root owns shared integration, combined pipeline and publication.'])
dump(C/(PREFIX+'read_manifest.json'),manifest)

runs=[]
run_specs=[('scalar','review_bottom_curvature_independent.py scalar','review_bottom_curvature_scalar_01',None),
 ('source','review_bottom_curvature_independent.py source','review_bottom_curvature_source_01',83506),
 ('supplement','review_bottom_curvature_supplement.py','review_bottom_curvature_supplement_01',70476),
 ('author01_reproduction','bottom_second_curvature_01.py','review_bottom_curvature_author01_reproduced',63724),
 ('author02_reproduction','bottom_second_curvature_02.py','review_bottom_curvature_author02_reproduced',36054)]
for name,program,outstem,sid in run_specs:
 stdout=C/(outstem+'_out.json');stderr=C/(outstem+'_err.txt');data=json.loads(stdout.read_text())
 assert data['passed']==data['total'] and all(c['passed'] for c in data['checks'])
 assert stderr.stat().st_size==0
 pyname=program.split()[0]
 cmd=f'OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 python3 {C}/{program} > {stdout} 2> {stderr}'
 r=dict(run=name,attempt=1,command=cmd,cwd=str(ROOT),program=bind(C/pyname),stdout=bind(stdout),stderr=bind(stderr),observed_exit_code=0,passed=data['passed'],total=data['total'],seconds=data.get('seconds',data.get('elapsed_seconds')),threshold_changes_after_results=0,implementation_changes_after_first_execution=0,
  output_mtime_utc=datetime.datetime.fromtimestamp(stdout.stat().st_mtime,datetime.timezone.utc).isoformat())
 if sid:r['tool_session_id']=sid
 if name.startswith('author'):
  num=name[6:8];a=json.loads((C/f'bottom_second_curvature_{num}_out.json').read_text());b=dict(data)
  a.pop('elapsed_seconds');b.pop('elapsed_seconds');assert a==b
  r['all_original_fields_exact_except']=['elapsed_seconds'];r['independent_evidence']=False
 else:r['independent_evidence']=True
 runs.append(r)
attempts=dict(schema='scoped-source-review-attempts-v1',created_utc=NOW,
 initial_criteria=bind(C/(PREFIX+'criteria.md')),supplement_criteria=bind(C/(PREFIX+'supplement_criteria.md')),
 chronology=['Full source/summary exposure; prospective reviewer criteria frozen.','New reviewer implementation written; scalar and source modes each run once.','A supplement was declared after those outputs, before its code, to obtain the top current directly from cubic evaluations.','Supplement written and run once. It imports only the reviewer cell/path implementation.','Only then author checker sources/criteria were inspected and both author programs rerun once.','Evidence/report packaging and scoped mechanical checks followed.'],
 timestamp_limits='File modification times record artifact writes, not independently authenticated experiment start times. Tool exits are observed; unavailable session IDs are omitted.',
 runs=runs,independent_predicates_passed=125,independent_predicates_total=125,author_reproduced_predicates=137,
 failures=[],failed_mutation_detectors=[],threshold_relaxations=[],operational_failures=[],
 diagnostic_limitations=['No interval arithmetic or exhaustive depth/volume/colour sampling.','Initial source current came from w2; supplement is the separately derived decisive current check.','Finite sample norm caps 2 and heat cap 8 were chosen in code before first execution; they are not uniform theorem constants.','Original criteria contain analytic proof targets as permitted for this already-running lane under PROCESS_LIGHT.'],
 runtime=dict(python=sys.version,numpy=numpy.__version__,scipy=scipy.__version__,platform=platform.platform(),thread_environment_on_scientific_commands={'OPENBLAS_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1','OMP_NUM_THREADS':'1'}))
dump(C/(PREFIX+'attempts.json'),attempts)

# Only clean transient bytecode generated from this reviewer's own helper.
cleaned=[]
cache=C/'__pycache__'
if cache.exists():
 for p in cache.glob(PREFIX+'*.pyc'):
  cleaned.append(str(p));p.unlink()
parsed=[]
for p in sorted(C.glob(PREFIX+'*.py')):
 ast.parse(p.read_text(),filename=str(p));parsed.append(str(p))
report=L/'REVIEW_BOTTOM_SECOND_CURVATURE_ASTRA.md'
links=[]
for target in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if '://' in target or target.startswith('#'):continue
 target=target.split('#')[0];p=report.parent/target
 # The receipt is created immediately below.
 assert p.exists() or p==C/(PREFIX+'receipt.json'),str(p)
 links.append(str(p))
assert (C/(PREFIX+'vocab_err.txt')).read_text()==''
vocab=(C/(PREFIX+'vocab_out.txt')).read_text()
mechanical=dict(all_reviewer_python_parses=True,parsed_files=parsed,original_author_bound_artifacts_verified=len(original_verified),upstream_review_bound_artifacts_verified=len(upstream_verified),frozen_expected_inputs_match=True,all_local_report_links_exist=True,local_report_links=links,vocabulary_exit_code=0,vocabulary_stdout=bind(C/(PREFIX+'vocab_out.txt')),vocabulary_stderr=bind(C/(PREFIX+'vocab_err.txt')),transient_reviewer_bytecode_removed=cleaned)
receipt_path=C/(PREFIX+'receipt.json')
owned=[report]+[p for p in sorted(C.glob(PREFIX+'*')) if p.is_file() and p!=receipt_path]
receipt=dict(schema='scoped-source-review-receipt-v1',created_utc=NOW,
 unit='bottom_second_curvature',reviewer={'requested':'gpt-6-astra/max/fork-none','backend_identity_verified':False,'family_disclosure':'Codex reviewing Codex work; no cross-family certification'},
 source=bind(L/'BOTTOM_SECOND_CURVATURE_ASTRA.md'),report=bind(report),read_manifest=bind(C/(PREFIX+'read_manifest.json')),attempts=bind(C/(PREFIX+'attempts.json')),
 methodology_revision_at_start=PIN,observed_head_at_freeze=git('rev-parse','HEAD').decode().strip(),
 disposition='CONFIRMED conditional source-specific BC3/CJ18 and conditional BC26; no whole-PR or audit verdict',
 confirmed=['Actual CJ19 source identities/scales including local BCH/Bianchi factorization.','Uniform complex-strip high-alias derivative Green counting norm.','Source-specific low-alias division from fixed-n germs with all external parameters.','Exact zero-total harmonic value and both-input reciprocal gluing.','Product exponential envelope and distinct row ell^-2/anchored-column ell^2 bounds.','Completed stationary quartic yields conditional full-colour BC26.'],
 open=['Finite-u all-depth analogue.','Jet convergence and complete finite-part increment/convergence.','Uniform nonlinear complex neighborhood and nonlinear RG.','Four-dimensional continuum Yang-Mills existence.','Positive physical continuum Hamiltonian mass gap.'],
 material_findings=[],source_repairs=[],independent_predicates=125,author_reproduction_predicates=137,
 scientific_review_rounds=1,pipeline_runs=0,git_mutations=0,pr_actions=0,audit_actions=0,
 limits=['Scope is this frozen source and explicitly consumed interfaces, not the whole theory or PR.','Conditional contracts are retained; no generic all-field inverse is claimed.','Numerics are support only and source-exposed; author reproductions are not independent evidence.','Existing lane completed under PROCESS_LIGHT grandfather allowance; consolidated proof remains a separate deliverable.'],
 mechanical_checks=mechanical,owned_artifacts=[bind(p) for p in owned],
 frozen_input_bindings=[bind(L/p) for p in expected if not p.startswith('checks/review_bottom_curvature')],
 author_receipt=bind(C/'bottom_second_curvature_receipt.json'),author_artifact_bindings=original_verified,
 upstream_review_receipt=bind(C/'review_charged_jet_receipt.json'),upstream_review_artifact_bindings=upstream_verified)
dump(receipt_path,receipt)
print(json.dumps(dict(report=bind(report),receipt=bind(receipt_path),read_manifest=bind(C/(PREFIX+'read_manifest.json')),attempts=bind(C/(PREFIX+'attempts.json')),owned_artifacts=len(owned),mechanical=mechanical),indent=2))
