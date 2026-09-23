import ast,difflib,gzip,hashlib,json,pathlib,re,shutil,subprocess
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';O=R/'drain8178-original'
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(W),*args],text=True).strip()
def out(p,b):
 p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('xb') as f:f.write(b if isinstance(b,bytes) else b.encode())
def jout(p,d):out(p,json.dumps(d,indent=2,ensure_ascii=False)+'\n')
assert git('rev-parse','HEAD')=='eadad252feffba1891b5b774822da85b92842578'
assert json.loads((R/'review-draft-slot.json').read_text())['owner']=='PR8178-author'
assert not git('status','--porcelain')
assert sha((R/'drain8178-review-original.json').read_bytes())=='b01afd62cdb927b10f6688c4ae70696fb0955d9f90c7be1f015f3b146c2ab459'
m=json.loads((O/'manifest.json').read_text());assert len(m['entries'])==21
note='docs/SUPPLIED_TORUS_AUXILIARY_FIELD_MODE_VARIANCE_AND_FINITE_BRACKET_BOUNDED_THEOREM_NOTE_2026-09-17.md'
runner='scripts/supplied_torus_auxiliary_field_mode_variance_finite_bracket_2026_09_17.py'
claim=pathlib.Path(note).stem.lower()
parent='docs/SPHERE_LEVEL_KERNEL_MOMENTS_WALK_LOCAL_LIMIT_AND_FINITE_PLANE_MIXING_BOUNDED_THEOREM_NOTE_2026-09-16.md'
parentclaim=pathlib.Path(parent).stem.lower()
archive='docs/history/pr8178-torus-auxiliary-recovery'
oldnote=next(e['path'] for e in m['entries'] if e['path'].startswith('docs/ADMISSIBILITY'))
oldrunner=next(e['path'] for e in m['entries'] if e['path'].startswith('scripts/'))
originalnote=(O/'head'/oldnote).read_text();old=(O/'head'/oldrunner).read_text()
recovery=[]
for e in m['entries']:
 row={'original_path':e['path'],'states':{},'disposition':('corrected live finite auxiliary theorem; full original stronger scope deferred' if e['path']==oldnote else 'corrected runner with exact original recovery' if e['path']==oldrunner else 'historical recovery only; no current campaign, audit or simulation authority')}
 for state in ('base','head','main'):
  x=e[state]
  if x is None:row['states'][state]=None;continue
  b=pathlib.Path(x['snapshot']).read_bytes();assert sha(b)==x['sha256']
  assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['blob']
  name='pr8178-'+state+'-'+hashlib.sha256(e['path'].encode()).hexdigest()[:12]+'-'+x['sha256'][:12]+'.gz'
  rel=archive+'/payloads/'+name
  out(W/rel,gzip.compress(b,mtime=0));assert gzip.decompress((W/rel).read_bytes())==b
  row['states'][state]={**x,'recovery_path':rel,'container_sha256':sha((W/rel).read_bytes()),'encoding':'gzip; mtime=0; original raw mode/blob/SHA retained'}
 recovery.append(row)
out(W/(archive+'/pr8178-original.delta.gz'),gzip.compress((O/'original.delta').read_bytes(),mtime=0))
jout(W/(archive+'/pr8178-original-identities.json'),{'pr':8178,'original_manifest':m,'recovery':recovery,'delta':{'path':archive+'/pr8178-original.delta.gz','raw_sha256':sha((O/'original.delta').read_bytes())}})
nt=r'''---
claim_id: CLAIM
claim_type: bounded_theorem
claim_scope: "For a supplied gain-one additive real two-component field on a finite periodic L by L plane, with iid centered site/level noises of covariance sigma2 I and zero initial field: exact Fourier multiplier, Hermitian mode covariance, plane and site variance, convergence of the nonzero-mode field to its stationary law, exact residual bound, real variance-one scale and integer crossing, scalar-proxy asymptotic rate, and finite lattice-sum variance bracket. The optional sigma2=A(3 beta)/(3 beta) is a supplied parametrization; no nonlinear memory or sharp logarithmic asymptotic follows."
upstream_dependencies:
  - PARENTCLAIM
runner: RUNNER
---

# Supplied torus auxiliary field: mode variance and a finite bracket

## Scope, supplied objects and dependency

Let L be a positive integer, N=L², and t a nonnegative integer. Sites form
(Z/LZ)². Independently supply the recurrence θ(t+1)=Pθ(t)+ξ(t), θ(0)=0,
where θ is real and two-component and
P f(x)=[f(x)+f(x−e₁)+f(x−e₂)]/3. Noises are iid across sites and levels,
centered, with finite second moment and covariance σ²I₂, σ²>0. Independence
between the two components is unnecessary for the componentwise identities.

One optional parametrization is σ²=A(3β)/(3β), β>0,
A(κ)=coth κ−1/κ. The [sphere kernel moments and finite-plane mixing proof](PARENTLINK)
supplies the aligned raw transverse variance and 0<A(κ)<1. It also proves
that the exact nonlinear Cartesian mean has derivative
A(3β)(θ₁+θ₂+θ₃)/3. Only its normalized mean direction has gain one.
Combining gain one with this additive iid noise is a **supplied auxiliary
model**, not an exact nonlinear linearization or a derivation of independent
noise away from alignment. This parent is a mathematical dependency for the
optional noise parametrization and the observable distinction. All finite
recurrence arguments below are self-contained for arbitrary σ²>0. No static
response theorem, physical rule selection, primitive or new axiom is imported.

## Exact characters, covariance and site variance

Use the unitary transform θ̂(k)=L⁻¹Σₓexp(−ik·x)θ(x),
k=(2π/L)n. Changing variable y=x−eⱼ in a shift gives
L⁻¹Σₓexp(−ik·x)θ(x−eⱼ)=exp(−ikⱼ)θ̂(k). Hence

φ(k)=[1+exp(−ik₁)+exp(−ik₂)]/3, u(k)=|φ(k)|²,

9u=3+2cos k₁+2cos k₂+2cos(k₁−k₂),

1−u=(4/9)[sin²(k₁/2)+sin²(k₂/2)+sin²((k₁−k₂)/2)].

Thus 0≤u≤1 and equality u=1 requires k₁,k₂∈2πZ: only the zero
mode. Orthogonality of finite roots of unity gives, per component,
E[ξ̂(k)overline{ξ̂(l)}]=σ²δₖₗ. This is diagonal **Hermitian covariance**.
Since the field is real, ξ̂(−k)=overline{ξ̂(k)}; conjugate modes are not
independent complex random variables. Temporal independence suffices below.

Unfolding the recursion gives θ(t)=Σⱼ₌₀ᵗ⁻¹Pʲξ(t−1−j). Each mode's
Hermitian variance is therefore σ²Σⱼ₌₀ᵗ⁻¹uʲ, namely σ²t at k=0 and
σ²(1−uᵗ)/(1−u) otherwise. Translation invariance and the unitary transform
give the component site variance

v_t=(σ²/L²)[t+Σₖ≠₀(1−uₖᵗ)/(1−uₖ)].

Alternatively averaging the recurrence gives θ̄(t+1)=θ̄(t)+ξ̄(t), since
both shifts preserve the site sum. Independent site noises imply
Var ξ̄=σ²/L², hence Var θ̄(t)=σ²t/L². This agrees with θ̄=θ̂(0)/L.

## Stationary limit and exact transient

Define V_L(t)=(σ²/L²)Σₖ≠₀(1−uₖᵗ)/(1−uₖ) and
V_L=(σ²/L²)Σₖ≠₀1/(1−uₖ). For L=1 both are zero. For L≥2 let
ρ_L=maxₖ≠₀uₖ<1. Subtracting the two finite sums proves

0≤V_L−V_L(t)=(σ²/L²)Σₖ≠₀uₖᵗ/(1−uₖ)≤ρ_LᵗV_L.

This is a stationary **limit**, not stationarity of the zero-start field.
For example a mode u=1/9 and σ²=1 has variances 0,1,10/9,… .
For existence at the law level, let Q remove the spatial average and extend
the iid noise sequence to all integer times. The backward sum
Z_t=Σⱼ≥₀PʲQξ(t−1−j) converges in mean square: the squared tail per
component, summed over sites in the unitary basis, is
σ²Σₖ≠₀uₖᵐ/(1−uₖ), which tends to zero. Independent centered time
increments remove cross terms. The resulting law is time stationary and
Z_{t+1}=PZ_t+Qξ(t). The zero-start nonzero field has the law of a truncated
backward sum, so converges in distribution (indeed in this coupling in mean
square). Gaussianity is asserted only if the supplied noise is Gaussian.

The finite bracket proved below implies every nonzero gap
1−uₖ≥16/(9L²), since |k|≥2π/L. Thus
ρ_Lᵗ≤exp(−16t/(9L²)). Conversely k=(2π/L,0) has
u=1−(8/9)sin²(π/L). Its variance e-fold scale [−log u]⁻¹ is
asymptotic to 9L²/(8π²), using sin x/x→1 and −log(1−x)/x→1.
The slow relaxation scale is therefore of order L², not of order V_L.
The residual inequality states the additional logarithmic factor needed for
any chosen relative tolerance; it does not assert a finite exact equilibration time.

## Real variance-one scale and scalar proxy

Define τ_L=L²/σ² as a real scale. The first integer t with
Var θ̄(t)≥1 is ceil(τ_L), since t/τ_L≥1 exactly when t≥τ_L.
At real interpolation t=τ_L, each component has variance one, and the
two-component root mean square norm is √2. This is not an angular hitting time.
Define the scalar proxy solely by M_t=exp(−v_t). Then exactly

M_t=exp(−t/τ_L)exp(−V_L(t)),

and exp(t/τ_L)M_t→exp(−V_L). Its asymptotic exponential rate is
1/τ_L. No equality with a nonlinear magnetization is assumed.
For the optional parametrization τ_L=3βL²/A(3β). The runner retains the
original rational enclosures at β∈{6,12,24,48}, L∈{16,32,64}, each of
width below 1/10. Coarser enclosing intervals include [4879,4880],
[19516,19517], [78064,78065] for β=6, and [9479,9480],
[18691,18692], [37121,37122] for L=16 at β=12,24,48. These bound real
scales; the integer crossing is the ceiling, not a rounded real value.

For completeness the exact enclosure method is as follows. For x≥0,
truncate exp(x) after degree n with x<n+2. The next term is
xⁿ⁺¹/(n+1)!; all successive term ratios are at most x/(n+2), so the positive
tail is bounded above by that next term divided by 1−x/(n+2).
Apply this to x=2κ. The function (E+1)/(E−1)−1/κ decreases for E>1,
so substituting the upper/lower exp bounds in reverse order encloses A(κ).
Positive reciprocals then enclose τ_L. The π bounds use
π=16 arctan(1/5)−4 arctan(1/239) and alternating-series upper/lower
remainders. These are mathematical enclosures, not fitted constants.

## Complete finite lattice-sum bracket

Choose representatives nᵢ∈(−L/2,L/2], k=2πn/L, and let
S_L=Σₙ≠₀1/|n|². The matrix M=(1/9)[[2,−1],[−1,2]] has eigenvalues
1/9 and 1/3. Since |sin y|≤|y| for all real y,

1−u≤[k₁²+k₂²+(k₁−k₂)²]/9=kᵀMk≤|k|²/3.

Concavity of sin on [0,π/2] puts it above its endpoint chord:
sin y≥2y/π. Therefore sin²(kᵢ/2)≥kᵢ²/π² for |kᵢ|≤π.
Dropping the third nonnegative sine square gives
1−u≥4|k|²/(9π²). Inverting these positive inequalities for each nonzero
mode, substituting |k|²=(2π/L)²|n|², summing and multiplying by σ²/L² yields

(3/(4π²))σ²S_L ≤ V_L ≤ (9/16)σ²S_L.

For L=1 the empty sums make both bounds zero. This proof is uniform in L.
It does not establish a sharp logarithmic coefficient, additive constant,
or equality with infinite-plane spread at time L².

## Exact finite checks and limits of the evidence

For L=2,3,4 all mode cosines are rational. The exact covariance recurrence
Σ_{t+1}=PΣ_tPᵀ+I, Σ₀=0, yields component site variance trΣ_t/L² and
plane variance 1ᵀΣ_t1/L⁴. The preserved finite fixtures compare these to the
mode sum through t=12 for L=2,3 and t=8 for L=4. Other retained fixtures
check V_L's bracket, the eigenvalues, a 20-point sine enclosure grid and
S_16,S_32,S_64. The last two increments are tested against the original
rational interval around 2πlog2; this is a finite check, not an asymptotic proof.
The analytic sine proof above supplies all-mode coverage, not the grid.

The [runner](RUNNERLINK) plans 16 top-level checks: 11 mathematical checks
and 5 input/reporting checks. Four original mathematical mutation families
remain; four new mathematical mutations target the corrected sign, conjugacy,
residual and ceiling. Two original prose-fence mutations are preserved only
in recovery. None of this corrected runner has been executed during preparation.
No claim of 16 passes or 8 killed mutations is made. Ordinary output is stdout;
optional AUDIT_RESULT_SIDECAR writes one exclusively created external JSON.
A future canonical cache may be generated only by controlled capture.

N5 scope: per element, symbolic multiplier/geometric identities and exact
sine-grid fixtures; per site, the stated tiny-torus covariance fixtures;
per mode, the finite exact conjugacy/residual and bracket fixtures; per block,
the twelve supplied variance-scale enclosures; lattice-wide, the complete
conditional finite-L proofs above, with no nonlinear or sharp-asymptotic
execution claim. These are evidence categories, not five closed negative routes.

## History and deferred science

[PR8178 recovery](history/pr8178-torus-auxiliary-recovery/README.md) contains
every original path, raw identity and original delta. The [readable deferred
argument](history/pr8178-torus-auxiliary-recovery/pr8178-deferred-science.md)
retains the entire original note, nonlinear estimates, sharper asymptotic
argument, limitations and correction trail. These are historical proposals,
not premises of this theorem. In particular finite noisy fit failures do not
prove estimator impossibility, and no formal negative certificate is claimed.
The original branch remains required for the unlanded science.
'''
nt=nt.replace('CLAIM',claim).replace('PARENT'+claim,parentclaim) if False else nt
for a,b in [('PARENTCLAIM',parentclaim),('CLAIM',claim),('RUNNERLINK','../'+runner),('RUNNER',runner),('PARENTLINK',pathlib.Path(parent).name)]:nt=nt.replace(a,b)
out(W/note,nt)
# Narrow code changes; original computational helper ASTs and finite fixtures preserved.
s=old;s=s[:s.index('"""')]+'''"""Exact finite checks for a supplied real gain-one additive torus field.

No nonlinear memory theorem or sharp logarithmic asymptotic is claimed.
Ordinary runs emit stdout; AUDIT_RESULT_SIDECAR optionally requests a unique
external JSON result. This runner does not execute historical simulators.
"""'''+s[s.index('"""',s.index('"""')+3)+3:]
s=s.replace('import re\n','import re\nimport hashlib\nimport json\nimport os\n').replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 60')
a=s.index('AUDIT_INPUT_PATHS =');b=s.index('MUTATION_GATE =')
s=s[:a]+f'AUDIT_INPUT_PATHS = (\n    {note!r},\n    {parent!r},\n)\nROOT = Path(__file__).resolve().parents[1]\nCLAIM_ID = {claim!r}\nPARENT_SHA256 = {sha((W/parent).read_bytes())!r}\n\n'+s[b:]
s=s.replace('    "claim_transition_injected": "F",\n    "claim_classical_name_in_theorem": "F",','    "fourier_sign_wrong": "F",\n    "real_modes_independent_wrong": "F",\n    "zero_start_stationary_wrong": "F",\n    "integer_crossing_floor_wrong": "F",')
a=s.index('def family_a(');b=s.index('# ============================================================================================ family B',a)
s=s[:a]+'''def family_a(checks: Checks, texts) -> None:
    note, parent = texts
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "one declared claim identity (metadata)")
    checks.check("A2", hashlib.sha256(parent.encode()).hexdigest() == PARENT_SHA256, "actual corrected sphere-kernel input hash (metadata)")
    checks.check("A3", Path(AUDIT_INPUT_PATHS[1]).name in note, "direct mathematical parent link present (metadata)")
    checks.check("A4", all(Path(ROOT, p).is_file() for p in AUDIT_INPUT_PATHS), "all literal declared inputs exist (metadata)")


'''+s[b:]
s=s.replace('phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3','phi = (1 + sp.exp(-sp.I * k1) + sp.exp(-sp.I * k2)) / 3')
s=s.replace('e^{i k1} + e^{i k2}','e^{-i k1} + e^{-i k2}')
s=s.replace('the memory time tau_L','the supplied real variance-one scale tau_L')
s=s.replace('(the growth 2 pi log L + O(1))','(finite fixtures only; no logarithmic asymptotic proved by this check)')
a=s.index('FENCES =');b=s.index('# ============================================================================================ family G',a)
s=s[:a]+'''def family_f(checks: Checks, note_text: str) -> None:
    # A real L=4 torus, with exact fourth roots of unity, tests the convention.
    L = 4
    sites = [(a, b) for a in range(L) for b in range(L)]
    U = sp.Matrix([[sp.I ** (-(a*x+b*y)) / L for x,y in sites] for a,b in sites])
    P = (sp.eye(L*L) + shift_matrix(L,0) + shift_matrix(L,1))/3
    sign = 1 if mut("fourier_sign_wrong") else -1
    D = sp.diag(*[(1+sp.I**(sign*a)+sp.I**(sign*b))/3 for a,b in sites])
    checks.check("F1", U*P*U.H == D, "negative-character convention verified by exact real-space transform at L=4")
    conjugation = sp.zeros(L*L,L*L)
    for i,(a,b) in enumerate(sites):
        conjugation[i,sites.index(((-a)%L,(-b)%L))] = 1
    expected = sp.eye(L*L) if mut("real_modes_independent_wrong") else conjugation
    checks.check("F2", U*U.H == sp.eye(L*L) and U*U.T == expected, "Hermitian covariance diagonal; real-field pseudo-covariance pairs opposite modes")
    ok = True
    for L in (2,3,4):
        modes = [u_mode(L,a,b) for a in range(L) for b in range(L) if (a,b)!=(0,0)]
        rho = max(modes)
        V = V_exact(L)
        for t in (0,1,2,8):
            residual = V - (site_variance_modes(L,t)-Fraction(t,L*L))
            exact = sum((u**t/(1-u) for u in modes),Fraction(0))/(L*L)
            bound = Fraction(0) if mut("zero_start_stationary_wrong") else rho**t*V
            ok = ok and residual == exact and 0 <= residual <= bound
    checks.check("F3", ok, "zero-start residual equals finite tail and is bounded by rho^t V on exact tiny tori")
    ok = True
    for tau in (Fraction(5,2),Fraction(3),Fraction(7,3)):
        crossing = tau.numerator//tau.denominator if mut("integer_crossing_floor_wrong") else -(-tau.numerator//tau.denominator)
        ok = ok and Fraction(crossing-1)/tau < 1 <= Fraction(crossing)/tau
    checks.check("F4", ok, "first integer variance-one crossing uses ceiling, including noninteger real scales")


'''+s[b:]
a=s.index('N5_LINES =');b=s.index('\n\n\ndef family_g',a)
s=s[:a]+'''N5_LINES = (
    "per_element: this run checks symbolic multiplier/geometric identities, eigenvalues and exact sine-grid fixtures; outcomes above",
    "per_site: this run checks exact L=2,3 through t=12 and L=4 through t=8 covariance fixtures; outcomes above",
    "per_mode: this run checks tiny-torus finite brackets, L=4 real conjugacy and finite residual fixtures; outcomes above",
    "per_block: this run encloses twelve supplied real variance-one scales and checks integer-crossing fixtures; outcomes above",
    "lattice_wide: conditional finite-L proof is in the note; no simulation, nonlinear memory or sharp logarithmic asymptotic tested",
)'''+s[b:]
s=s.replace('    return 0 if checks.failed == 0 else 1','''    sidecar = os.environ.get("AUDIT_RESULT_SIDECAR")
    if sidecar:
        destination = Path(sidecar)
        if not destination.is_absolute() or destination.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError("AUDIT_RESULT_SIDECAR must be an absolute external per-attempt path")
        with destination.open("x", encoding="utf-8") as f:
            json.dump({"passed": checks.passed, "failed": checks.failed,
                       "failed_families": sorted(checks.failed_families),
                       "mutation": ACTIVE_MUTATION,
                       "expected_mutation_family": MUTATION_GATE.get(ACTIVE_MUTATION),
                       "input_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
                       "scope": "finite auxiliary checks; not universal execution or nonlinear proof"}, f, indent=2)
            f.write("\\n")
    return 0 if checks.failed == 0 else 1''')
s=s.replace('# float-scan-marker-line\n','')
ast.parse(s);out(W/runner,s)
# Proof/history is readable in addition to exact byte recovery.
deferred='''# PR8178 deferred science and correction record

This appendix is historical recovery, not a live claim or dependency authority.
The original branch must remain because the sharper asymptotics and nonlinear
memory proposals remain unlanded. No formal negative certification is granted.

## Exact boundary and reopen conditions

The live note proves the supplied additive finite-torus recurrence only.
The exact nonlinear mean gain is A(3β), whereas gain one belongs to a supplied
auxiliary recurrence or normalized direction observable. The negative Fourier
sign, Hermitian covariance with real conjugacy, stationary limit, residual,
O(L²) slow relaxation and ceiling crossing replace the original statements.
The full original argument below is not silently endorsed by preservation.

The original finite bracket and all finite fixtures survive. The proposed
S_L=2πlog L+O(1), sharper V_L=2γlog L+constant+o(1), and identification
with infinite-plane spread at t=L² require complete new asymptotic proofs;
finite sums and direct summations do not prove those assertions. Reopen only
with the complete claimed-strength proof and independent affected review.

The nonlinear MSD values are historical finite-lag chordal estimators.
At β=6, lag25, the reported L16 value 1.344±.014 differs from L32
1.416±.005 by .072 versus combined reported error about .014866.
The β12,L32,lag1000 linear calibration row .960±.015 contradicts the
blanket within-three-percent statement. These discrepancies are preserved.
For unit directions, E|u(t+ell)−u(t)|²/(2ell)≤2/ell, so this quantity
cannot have a positive lag-independent asymptotic diffusion constant.
Discarding a trajectory prefix does not prove stationarity. Neither average
magnitude nor an inverse square of that average proves the proposed nonlinear
memory scale |m|²τ or captures all correlations and amplitude fluctuations.
The original failed exponential fits, NaN/error/negative outcomes, alternate
sampler and apparently successful MSD rows all remain exact in the payloads.
No new simulations replace them. Reopen nonlinear conclusions only with a
specified observable and regime, complete physical-law argument and adequately
controlled evidence. The failure of one estimator at supplied seeds does not
prove an impossibility theorem. The original five diagnostic items are not
five closed negative route families; certification remains deferred.

## Full original note, verbatim (historical, superseded where corrected)

````text
'''+originalnote+'\n````\n\nEnd of complete original note. Exact raw bytes and identity are also recoverable from the mapping.\n'
out(W/(archive+'/pr8178-deferred-science.md'),deferred)
readme='''# PR8178 complete original recovery

Historical source only; author certificates and generated audit surfaces are
not audit outcomes or theorem authority. The live corrected proof is
[the supplied torus auxiliary theorem](../../SUPPLIED_TORUS_AUXILIARY_FIELD_MODE_VARIANCE_AND_FINITE_BRACKET_BOUNDED_THEOREM_NOTE_2026-09-17.md).
The [deferred appendix](pr8178-deferred-science.md) preserves the entire original
argument readably and explains the exact corrected boundary and reopen conditions.

[The identity mapping](pr8178-original-identities.json) contains all 21 original
paths and every available base/head/main mode, Git blob, raw SHA256 and length.
Each payload is deterministic gzip, preserving exact raw bytes, including
trailing whitespace, failed fits, raw errors, simulators and campaign history.
Use Python gzip.decompress or gzip -dc to recover bytes; restore the recorded
original mode and verify both raw SHA256 and Git blob. No archived program is
an active runner. The [full original delta](pr8178-original.delta.gz) is also
preserved. Current campaign and generated audit files are not overwritten.
The original branch is retained for the deferred unique science.

## Original head recovery

'''
for row in recovery:readme+=f"- `{row['original_path']}`: [{pathlib.Path(row['states']['head']['recovery_path']).name}](payloads/{pathlib.Path(row['states']['head']['recovery_path']).name})\n"
out(W/(archive+'/README.md'),readme)
# Freeze and AST-only preservation, without importing or executing science.
oldtree=ast.parse(old);newtree=ast.parse(s)
helpers=['exp_bounds','A_bounds','pi_bounds','cos_exact','u_mode','site_variance_modes','V_exact','shift_matrix','covariance_recursion','lattice_sum']
def fn(tree,name):return ast.dump(next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name),include_attributes=False)
preserved={n:fn(oldtree,n)==fn(newtree,n) for n in helpers};assert all(preserved.values())
assert fn(oldtree,'family_c')==fn(newtree,'family_c')
# family_d changes only its user-facing strings, not arithmetic, inputs, loops or tolerances.
class StripStrings(ast.NodeTransformer):
 def visit_Constant(self,node):return ast.copy_location(ast.Constant(value='<string>'),node) if isinstance(node.value,str) else node
def mathfn(tree,name):return ast.dump(StripStrings().visit(ast.parse(ast.unparse(next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name)))),include_attributes=False)
assert mathfn(oldtree,'family_d')==mathfn(newtree,'family_d')
paths=git('ls-files','--others','--exclude-standard').splitlines()
tracked=git('ls-files').splitlines();basenames={pathlib.Path(p).name.casefold():p for p in tracked if p.lower().endswith('.md')}
for p in paths:
 if p.lower().endswith('.md') and pathlib.Path(p).name not in ('README.md','SKILL.md'):assert pathlib.Path(p).name.casefold() not in basenames,p
assert not git('diff','--name-only') and not git('diff','--cached','--name-only')
freeze=[];F=R/'drain8178-prepared-v1-source';assert not F.exists()
for p in paths:
 b=(W/p).read_bytes();out(F/p,b);freeze.append({'path':p,'mode':'100755' if (W/p).stat().st_mode&0o111 else '100644','sha256':sha(b),'bytes':len(b)})
jout(R/'drain8178-prepared-v1-source-freeze.json',{'base':git('rev-parse','HEAD'),'owner':'PR8178-author','files':freeze})
jout(R/'drain8178-author-full-mapping-v1.json',{'originals':recovery,'original_count':21,'source_count':len(paths),'branch_retention_required':True})
out(R/'drain8178-author-correction-v1.diff',''.join(difflib.unified_diff(originalnote.splitlines(True),nt.splitlines(True),fromfile=oldnote,tofile=note))+''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=oldrunner,tofile=runner)))
jout(R/'drain8178-author-preservation-v1.json',{'ast_only_no_execution':True,'unchanged_helper_asts':preserved,'family_c_unchanged':True,'family_d_arithmetic_ast_unchanged_ignoring_strings':True,'family_b_change':'negative Fourier convention; same modulus/gap identities and fixtures','family_f_change':'replace four prose-only gates with four corrected-claim mathematical controls; independent reviewer required','original_recoveries':21,'all_available_base_head_main_states_preserved':True,'source_count':len(paths),'tracked_and_index_unchanged':True,'markdown_basename_collisions':[]})
jout(R/'drain8178-author-prepared-v1.json',{'pr':8178,'owner':'PR8178-author','base':git('rev-parse','HEAD'),'original_head':m['head'],'source_files':freeze,'note':note,'runner':runner,'claim_id':claim,'runtime_inputs':[note,parent],'runtime_helpers':[],'expected_checks':16,'mathematical_checks':11,'metadata_checks':5,'planned_mathematical_mutations':8,'executed_corrected_programs':0,'status':'author preparation; independent affected review and later fresh-main closure required'})
print(json.dumps({'files':len(paths),'note':note,'runner':runner,'all_originals':21,'source_freeze_sha256':sha((R/'drain8178-prepared-v1-source-freeze.json').read_bytes())}))
