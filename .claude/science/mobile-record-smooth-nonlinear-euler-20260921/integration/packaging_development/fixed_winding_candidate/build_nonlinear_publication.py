from pathlib import Path
import hashlib,json,pprint,shutil
R=Path("/Users/jonreilly/Documents/Codex/mobile-record-nonlinear-publication-20260921")
P=Path('/Users/jonreilly/Documents/Codex/mobile-record-positive-quantum-publication-20260921')
A=Path("/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_second")
EV=".claude/science/mobile-record-smooth-nonlinear-euler-20260921";E=R/EV
NOTE='docs/MOBILE_RECORDS_SMOOTH_NONLINEAR_EULER_BOUNDED_THEOREM_NOTE_2026-09-21.md'
RUNNER='scripts/mobile_records_smooth_nonlinear_euler_2026_09_21.py'
CLAIM='mobile_records_smooth_nonlinear_euler_bounded_theorem_note_2026-09-21'
PRIMARY={
'DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md':'d6a3689bb2ab6bf627886a77f4f197bb6a2478da59264b0dde91d3bf1f131e69',
'DIMER_NONLINEAR_INITIAL_DRIFT.md':'a67bc5a0b8f9a85e0eccba11fc56870e7861410044ff5d6e28d1ddd05d384c78',
'DIMER_SMOOTH_NONLINEAR_EULER_LIMIT.md':'dbd07eca8db76c58f672791aa0f20b8483886352d79638931702306518b829b4'}
DEPENDENCIES={'DIMER_ROUTED_RECORD_TRANSPORT.md':'dc7bac51a1ffb273e11e9356713778aeb645acbfb280973f927c1f1de007d873'}
CHECKERS={'dimer_nonlinear_flux_check.py':'45f732b01260e3bd9e8651aefe42acb346a7a2f8bd30190f9f1b33313de57cc4',
'dimer_smooth_nonlinear_check.py':'d97be26aa22fad562ac9419566bcb09c4c97db01dcbd598bca0d601f968f7eb8'}
SUITES=(('dimer_nonlinear_flux_check.py','dimer_nonlinear_flux_checks/RESULTS.json',4),('dimer_smooth_nonlinear_check.py','dimer_smooth_nonlinear_checks/RESULTS.json',3))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for f,h in {**PRIMARY,**DEPENDENCIES,**CHECKERS}.items():assert sha(A/f)==h,f
for f in ['primary_sources','author_checks','author_original_outputs','independent','integration','mutation_results']:(E/f).mkdir(parents=True,exist_ok=True)
for f in {**PRIMARY,**DEPENDENCIES}:shutil.copy2(A/f,E/'primary_sources'/f)
for f in CHECKERS:shutil.copy2(A/f,E/'author_checks'/f)
for _,output,_ in SUITES:
 source=(A/output).parent;dest=E/'author_original_outputs'/source.name;dest.mkdir(exist_ok=True)
 for p in source.glob('*.json'):shutil.copy2(p,dest/p.name)
for f in ['DIMER_NONLINEAR_FLUX_ROOT_VERIFICATION.json','DIMER_SMOOTH_NONLINEAR_METHOD_CONTEXT.json']:shutil.copy2(A/f,E/'integration'/f)
intro=f'''---
claim_id: {CLAIM}
claim_type: bounded_theorem
claim_scope: "For the specified permanent-color exchange process on a fixed winding matching, any strictly positive periodic C3 solution of the derived fourteen-color conservation law governs the Euler-time process over its smooth interval when the initial relative entropy per pair vanishes. This is a conditional hydrodynamic limit with supplied rates and preparation, not a birth-selected state, moving-geometry theorem or quantum TOE."
upstream_dependencies:
  - minimal_axioms
  - mobile_records_moving_geometry_color_waves_bounded_theorem_note_2026-09-21
runner: {RUNNER}
---

# Smooth nonlinear evolution of permanent mobile record colors

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

The existing local exchange process for permanent record pairs supports a
finite-amplitude, fourteen-color conservation law over each stipulated smooth
time interval. This is not a derivation from the
[minimal record axioms](MINIMAL_AXIOMS_2026-06-29.md). The stochastic rates,
Euler clock scaling, fixed winding matching and inhomogeneous preparation
are specified assumptions.

The result strengthens the earlier initial-drift and stationary fluctuation
calculations in one concrete direction. Let K=N^3/2 and let p(t,x) be a fixed
periodic C3 solution, bounded away from the probability-simplex boundary.
If H(mu_N(0)|nu_N(0))=o(K), then the actual law satisfies
sup_t H(mu_N(t)|nu_N(t))/K ->0, with uniform-time weak empirical convergence
to p. The proof controls correlations by entropy dissipation and conditional
finite-block mixing. It does not assert a product law at later times or
convergence of the whole microscopic distribution in total variation.

The full nonlinear flux is
F_a=gamma p_a[e_a cross Y+X cross b_a-2 X cross Y].
Its exact thirteen-moment representation includes six vector components and
seven additional moments. The convex entropy sum p log p symmetrizes the
Jacobian on the simplex tangent. At anisotropic rest states the vector
sector generally has two distinct polarization speeds. Equal speeds on
three axes force isotropic second moments when gamma is nonzero. A hidden
cubic moment can remain invisible to that linear optical diagnostic.

The three source arguments follow in full. Original pending-review status
sentences are historical; the sealed reports define the completed selective
check coverage. Formal retention remains unaudited.

'''
titles=['I. Nonlinear flux, entropy and anisotropic optical diagnostics','II. The exact microscopic initial derivative','III. The smooth-time hydrodynamic theorem']
parts=[];trans=[]
for title,(f,h) in zip(titles,PRIMARY.items()):
 body=(A/f).read_text().split('\n',2)[2].rstrip();body='\n'.join('#'+line if line.startswith('#') else line for line in body.splitlines())
 parts.append('## '+title+'\n\n'+body+'\n');trans.append(dict(primary=f,source_sha256=h,published_body_sha256=hashlib.sha256(body.encode()).hexdigest()))
footer=f'''
## Verification and remaining physics

[The evidence packet](../{EV}/README.md) preserves three complete source
arguments, the unchanged transport dependency, seven author mathematical
groups and two completed selective independent reconstructions. Three
mutations target the nonlinear flux, entropy-flux correction and exponential
block bound. The proofs supply the all-volume conclusions; finite checks
test their load-bearing steps and counterexamples.

The entropy method has established antecedents, including Toth and Valko's
[one-dimensional systems with several conservation laws](https://arxiv.org/abs/math/0210426).
That abstract supplies methodological context. No theorem from that work is
imported into this three-dimensional proof; the required block geometry,
conditional centering, current replacement and exponential estimate are
proved here.

The smooth-time theorem uses finite-sector irreducibility at fixed block
size and takes N to infinity before the block size grows. It asserts no
numerical convergence rate. Its initial-drift O(1/N) estimate is a separate
Taylor bound. The initial author's finite-N threshold failure and the narrow
grid extension remain in the independent source history.

Smooth existence is an explicit hypothesis. Birth preparation of a spatially
varying profile, coupled moving-geometry nonlinear evolution, shock selection,
quantum dynamics, matter, gravity and empirical identification remain open.
The homogeneous birth preparation and earlier linear waves cannot supply
these missing conclusions by composition.
'''
(R/NOTE).write_text(intro+'\n'.join(parts)+footer)
(E/'PUBLICATION_TRANSFORM.json').write_text(json.dumps(dict(note=NOTE,parts=trans,change='Complete arguments preserved; only titles and heading levels transformed.'),indent=2)+'\n')
inputs=(NOTE,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/MOBILE_RECORDS_MOVING_GEOMETRY_COLOR_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md',*[EV+'/primary_sources/'+f for f in {**PRIMARY,**DEPENDENCIES}],*[EV+'/author_checks/'+f for f in CHECKERS])
mut={
'omit_nonlinear_population_flux':('dimer_nonlinear_flux_check.py','e.cross(Y)+X.cross(b)-2*X.cross(Y)','e.cross(Y)+X.cross(b)'),
'omit_entropy_flux_half_M':('dimer_nonlinear_flux_check.py','-eta*M-(0 if omit else M/2)','-eta*M'),
'double_block_exponential_coefficient':('dimer_smooth_nonlinear_check.py','alpha=F(1,224)','alpha=F(1,112)')}
for name,(f,old,new) in mut.items():assert (A/f).read_text().count(old)==1,name
template=(P/'scripts/mobile_records_positive_quantum_curl_limits_2026_09_21.py').read_text();start=template.index('ROOT=');end=template.index('sha=lambda')
header="ROOT=Path(__file__).resolve().parents[1]\nCLAIM_ID=%r\nEVIDENCE=%r\nCHECK_DIRECTORY=EVIDENCE+'/author_checks'\nNOTE=%r\nAUDIT_TIMEOUT_SEC=1200\nPRIMARY_SOURCES=%r\nCHECKER_DEPENDENCIES=()\nSUITES=%r\nAUDIT_INPUT_PATHS=%s\nMUTATIONS=%s\n"%(CLAIM,EV,NOTE,tuple({**PRIMARY,**DEPENDENCIES}),SUITES,pprint.pformat(inputs),pprint.pformat(mut))
template=template[:start]+header+template[end:];template=template.replace('supplied positive quantum curl limits','smooth nonlinear permanent-color evolution').replace("prefix='positive-quantum-curl-controls-'","prefix='smooth-nonlinear-controls-'")
start=template.index('   expected={');end=template.index('   total+=count',start)
template=template[:start]+"""   expected={
    'dimer_nonlinear_flux_check.py':('moment_fluxes','entropy_symmetrizer','optical_diagnostic','actual_initial_drift'),
    'dimer_smooth_nonlinear_check.py':('blocks','fixed_sector','entropy_algebra'),
   }[filename]
   payload=data.get('groups',data)
   assert len(expected)==count and all(key in payload for key in expected)
"""+template[end:]
(R/RUNNER).write_text(template)
(E/'README.md').write_text(f'''# Smooth nonlinear permanent-color evolution

Three complete new arguments, one unchanged model dependency and two sealed
independent reconstructions support a conditional smooth-time Euler theorem.
Formal retained status remains unaudited. Reproduce with Python, NumPy and SymPy:

~~~
python3 {RUNNER}
python3 {EV}/verify_evidence.py
~~~

The runner copies inputs into a temporary directory, executes seven mathematical
groups plus source bookkeeping and leaves producer inputs unchanged. Three
mutations must fail. The full proof uses a fixed-block then volume-limit
argument; finite controls do not prove all-volume mixing or infer a convergence
exponent. Independent capsules preserve pre-comparison evidence, reports,
countercontrols and the initial-drift threshold failure. Authentication establishes
byte identity, not scientific correctness.
''')
print(json.dumps(dict(note_sha256=sha(R/NOTE),runner_sha256=sha(R/RUNNER),groups=7,mutations=list(mut))))

