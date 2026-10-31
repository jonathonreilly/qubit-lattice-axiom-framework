#!/usr/bin/env python3
"""Freeze this bounded author unit only; no git or shared-register writes."""
from pathlib import Path
import ast,datetime,hashlib,json,platform,re,sys
import numpy,scipy
ROOT=Path('/Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972')
assert Path.cwd()==ROOT
L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C=L/'checks';stem='bottom_second_curvature_';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def info(p):
 p=Path(p);return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)
def write(name,obj):(C/(stem+name)).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
old_manifest=C/'charged_stationary_jet_source_manifest.json'
old_receipt=C/'charged_stationary_jet_receipt.json'
review_receipt=C/'review_charged_jet_receipt.json'
assert sha(old_manifest)=='c8ad3708cb24b231e64538c79da61420ebc35a8c6042bc86f7f2a5955296467d'
assert sha(old_receipt)=='83ba5129c3b6ca9c6e0d6a4577938531658ddf8fa2a8f21d728831d3edb66b6a'
assert sha(review_receipt)=='ad4226851b1b1d7b29e87f19c42c18a021fd8dd7afbfb5a85eeff5007120962d'
old=json.loads(old_manifest.read_text());oldr=json.loads(old_receipt.read_text());rev=json.loads(review_receipt.read_text())
for packet in [oldr,rev]:
 for item in packet['owned_artifacts']:assert sha(item['path'])==item['sha256'],item['path']
review=L/'REVIEW_CHARGED_STATIONARY_JET_ASTRA.md'
assert sha(review)=='f7e02d766c8885dceeeac8d2264784cdc65b85a771ae556efa5935d45236836d'
selected=[('LINEAR_PACKAGE.md',175,290,'Fresh complete selected read; underlying file matches inherited hash.'),
 ('PROOF_session16_snapshot.md',2649,2745,'Fresh complete selected EXP-id/real/strip read; immutable snapshot hash matches inherited source.'),
 ('REVIEW_S13_S14.md',75,122,'Fresh complete selected read, reread before freeze; periodic-gluing and cancellation repairs.'),
 ('REVIEW_S15_CONVERGENCE.md',1,65,'Fresh complete selected read, reread before freeze; confirmation of applied alias/strip repairs.'),
 ('ASSUMPTIONS_AND_IMPORTS.md',38,46,'Fresh current tail read; earlier complete historical version is separately bound by inherited manifest. Current header/earlier rows not newly claimed as full-read.'),
 ('LITERATURE_BRIDGES.md',42,50,'Fresh current tail B32-B36 and scope read; earlier complete historical version separately bound.'),
 ('CHARGED_STATIONARY_JET_ASTRA.md',1,10000,'Entire frozen author argument known from prior unit and completely reread here.'),
 ('REVIEW_CHARGED_STATIONARY_JET_ASTRA.md',1,10000,'Full new upstream review: first combined output truncated later metadata, followed by bounded250-end reread. No reviewer checker code was read/imported.')]
slices=[]
for name,a,b,cov in selected:
 p=L/name;lines=p.read_text().splitlines(keepends=True);b=min(b,len(lines));text=''.join(lines[a-1:b]);slices.append(dict(**info(p),read_lines=[a,b],read_coverage=cov,selection_sha256=hashlib.sha256(text.encode()).hexdigest(),text=text))
write('read_slices.json',dict(captured_utc=now,selections=slices))
inherited=[];deltas=[]
for item in old['sources']:
 p=Path(item['path']);row=dict(item);row['coverage_inherited_from']=str(old_manifest)
 if p.exists():
  row['current_sha256']=sha(p);row['current_matches_consumed_version']=row['current_sha256']==item['sha256']
  if not row['current_matches_consumed_version']:deltas.append(dict(path=str(p),historical_sha256=item['sha256'],current_sha256=row['current_sha256']))
 inherited.append(row)
allowed_deltas={str(L/'ASSUMPTIONS_AND_IMPORTS.md'),str(L/'LITERATURE_BRIDGES.md')}
assert all(d['path'] in allowed_deltas for d in deltas),deltas
external=[
 dict(url='https://link.springer.com/article/10.1007/s00028-022-00851-1',title='Abadias–De Leon-Contreras, Discrete Hölder spaces...',coverage='Abstract/introduction (retrieved lines61-150); selected Remark2.5 and complete Lemma2.6 with proof (lines397-440). Not the full paper.',role='Unweighted discrete heat difference comparison; weighted complex-character estimate proved directly in BC10-14.'),
 dict(url='https://arxiv.org/pdf/1207.2096v2',title='Dowker, Heat-kernels on the discrete circle and interval',coverage='Abstract plus phase-periodic setup and equations13-15, PDF pages4-5, retrieved lines230-286. Later returned context scanned but not imported.',role='Exact real-character image/Fourier mechanism; complex extension proved directly.'),
 dict(url='https://arxiv.org/abs/2303.10754',title='Dybalski–Stottmeister–Tanimoto, Lattice Green functions for pedestrians',coverage='Abstract and metadata only.',role='Method comparison; no theorem imported.'),
 dict(url='https://arxiv.org/html/2303.10754v2',coverage='Failed retrieval: HTTP404.',role='No content read or imported.'),
 dict(url='https://alea.impa.br/articles/v19/19-38.pdf',title='Michta–Slade, Asymptotic behaviour of the lattice Green function',coverage='Published pages957-958 definitions1.1-1.3; pp965-966 Lemma2.1 with proof2.3-2.5. Lemma2.2/AppendixB location seen, proof not read.',role='Scalar infinite-lattice normalization comparison, phi=2d times their symbol; no complex-cell/source theorem imported.')]
manifest=dict(unit='bottom_second_curvature',captured_utc=now,methodology_revision='ca2bc7ddf64790da96cd43d42017d000fbfe4808',
 inherited_manifest=info(old_manifest),inherited_read_coverage=inherited,methodology=old['methodology'],inherited_external=old['external'],
 fresh_sources=[{k:v for k,v in s.items() if k!='text'} for s in slices],fresh_external=external,
 historical_context_deltas=deltas,read_slice_artifact=info(C/(stem+'read_slices.json')),
 upstream_review=dict(report=info(review),receipt=info(review_receipt),source=info(L/'CHARGED_STATIONARY_JET_ASTRA.md'),receipt_artifact_hashes_all_verified=True,scope='CJ11-CJ17 and CJ18-implies-quartic confirmed within named normalized-tree/linear contracts; new CJ18 proof not reviewed'),
 read_honesty='Hashes identify bytes, not full read coverage. The inherited manifest preserves its truncated exploratory reads and later bounded coverage. New output JSON predicates were all programmatically inspected; selected numerical diagnostics were read. A combined upstream-read output truncated the later inherited manifest; that was not treated as a new full read. The upstream report tail was reread to complete its coverage.',
 implementation_exposure='New programs were written without predecessor/helper imports. The charged author mathematics and summaries were already known. First completed new runs preceded reading the newly returned independent upstream review. No independence claim for this author unit.',
 route_origin='High-alias heat splitting and Cauchy/Weierstrass continuation were coordinator-proposed mechanisms, derived and tested here, not asserted as supplied theorems.',
 roots_and_primitive_status='Supplied Wilson/normalized-soft SU(N) model, periodic geometry, fixed kappa interval and counting/root gauge domains. No new physical primitive or empirical fit. Full continuum existence and physical gap remain open.',
 root_owned_operations='No git mutation, shared summary, audit surface, lock, publication or worker launch performed by this unit.')
write('source_manifest.json',manifest)
attempts=[]
for num,session,command in [('01',99081,'python3 '+str(C/(stem+'01.py'))),('02',7693,'OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 '+str(C/(stem+'02.py')))]:
 p=C/(stem+num+'.py');out=C/(stem+num+'_out.json');err=C/(stem+num+'_err.txt');j=json.loads(out.read_text())
 ast.parse(p.read_text());assert j['passed']==j['total'] and all(x['passed'] for x in j['checks']);assert err.read_bytes()==b''
 attempts.append(dict(attempt=1,program=info(p),command=command+' > '+str(out)+' 2> '+str(err),cwd=str(ROOT),tool_session_id=session,observed_exit_code=0,stdout=info(out),stderr=info(err),passed=j['passed'],total=j['total'],elapsed_seconds=j['elapsed_seconds'],threshold_changes=0,implementation_changes_after_first_run=0))
write('attempts.json',dict(created_utc=now,criteria=info(C/(stem+'criteria.md')),criteria_written_before_code=True,attempts=attempts,
 failures=[],retrieval_failures=[dict(url='https://arxiv.org/html/2303.10754v2',outcome='404; abstract retrieved separately')],
 false_starts='No new numerical predicate failed. Prior charged-unit failures remain in its immutable packet; no new file overwrote them.',
 runtime=dict(python=sys.version,numpy=numpy.__version__,scipy=scipy.__version__,platform=platform.platform()),
 limits='Finite controls are ordinary floating-point support, not interval certification, all-depth sampling, or proof of the complex analytic estimates. No full repository pipeline run by this bounded worker.'))
main=L/'BOTTOM_SECOND_CURVATURE_ASTRA.md';receipt=C/(stem+'receipt.json')
allpaths=[main]+sorted(p for p in C.glob(stem+'*') if p.is_file() and p!=receipt)
for p in allpaths:
 if p.suffix=='.py':ast.parse(p.read_text())
links=[]
for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',main.read_text()):
 if '://' in target:continue
 target=target.split('#')[0]
 if not target:continue
 p=main.parent/target;assert p.exists() or p==receipt,(target,p);links.append(str(p))
payload=dict(unit='bottom_second_curvature',frozen_utc=now,claim='Author proof of source-specific CJ18 and conditional full-colour quartic bound under the named normalized-tree/linear/current contracts; fresh independent review pending.',
 source=info(main),methodology_revision=manifest['methodology_revision'],owned_artifacts=[info(p) for p in allpaths],
 upstream_author_receipt=info(old_receipt),upstream_review_receipt=info(review_receipt),
 mechanical_checks=dict(all_python_parsed=True,new_predicates_passed=sum(a['passed'] for a in attempts),new_predicates_total=sum(a['total'] for a in attempts),both_exit_codes=0,both_stderr_empty=True,all_old_author_artifacts_unchanged=len(oldr['owned_artifacts']),upstream_review_receipt_artifacts_match=len(rev['owned_artifacts']),local_link_targets=links),
 theorem_boundary=['CJ18 actual Euler/Bianchi/harmonic source only','BC9 high-alias derivative Green bound, not generic inverse','BC17-20 source-specific analytic division with nonuniform fixed-depth germ','full weighted row ell^-2 and anchored-column ell^2 density','conditional full-colour D4 bound via completed stationary quartic'],
 open_outside_scope=['independent review of this new argument','finite-u all-depth analogue','full finite-part increment/convergence','nonlinear complex neighborhood and RG','continuum Yang-Mills existence','physical positive continuum Hamiltonian mass gap'],
 operations='No git/staging/PR/shared-status/audit changes. Coordinator owns integration and review.')
receipt.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
for target in links:assert Path(target).exists(),target
for row in payload['owned_artifacts']:assert sha(row['path'])==row['sha256']
print(json.dumps(dict(source=info(main),receipt=info(receipt),manifest=info(C/(stem+'source_manifest.json')),artifacts=len(allpaths),new_checks=payload['mechanical_checks']['new_predicates_passed'],upstream_hashes_unchanged=True,context_deltas=deltas),indent=2))
