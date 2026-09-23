from pathlib import Path
import ast,json,hashlib,gzip,shutil,difflib,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';O=R/'drain8176-original/head';BASE='3dca18ddd0082dc23bb12c7ca38939b901c28736'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert json.loads((R/'review-draft-slot.json').read_text())['owner']=='PR8176-author'
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==BASE
assert not subprocess.check_output(['git','-C',str(W),'status','--porcelain'],text=True)
report=json.loads((R/'drain8176-review-original.json').read_text());ds=report['path_dispositions'];assert len(ds)==29
on=next(d['path'] for d in ds if d['path'].startswith('docs/ADMISSIBILITY'));op=next(d['path'] for d in ds if d['path'].startswith('scripts/'))
old=(O/on).read_text();src=(O/op).read_text();tree=ast.parse(src)
note='docs/MARKED_TREE_SINGLE_SEED_DYNAMIC_PROGRAM_AND_FINITE_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-17.md';run='scripts/marked_tree_single_seed_dynamic_program_finite_rational_certificates_check_2026_09_17.py';cid=Path(note).stem.lower();hist='docs/work_history/review_loop/pr8176';defer=hist+'/pr8176-deferred-science.txt'
def emit(p,data):
 p=W/p;assert not p.exists(),p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data.encode() if isinstance(data,str) else data);p.chmod(0o644)
def dump(p,d):assert not p.exists(),p;p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
entries=[]
for i,d in enumerate(ds):
 b=(O/d['path']).read_bytes();h=d['head'];assert sha(b)==h['sha256'];assert subprocess.check_output(['git','-C',str(W),'cat-file','blob',h['blob']])==b
 dest=f'{hist}/originals/pr8176-{i+1:02d}-{Path(d["path"]).name}.gz';z=gzip.compress(b,mtime=0);emit(dest,z)
 entries.append(dict(original_path=d['path'],original_mode=h['mode'],original_blob=h['blob'],original_sha256=sha(b),recovery=dict(path=dest,encoding='gzip',sha256=sha(z),decoded_sha256=sha(b)),disposition='narrowed-canonical-and-complete-recovery' if d['path'] in [on,op] else 'complete-historical-recovery',final_path=note if d['path']==on else run if d['path']==op else dest))
b=(R/'drain8176-original/delta.patch').read_bytes();z=gzip.compress(b,mtime=0);patchpath=hist+'/pr8176-original-delta.patch.gz';emit(patchpath,z)
man=dict(schema_version=1,kind='exact-original-recovery-manifest',pr=8176,head=report['original_head'],delta_base=report['original_base'],entries=entries,original_delta=dict(path=patchpath,sha256=sha(z),decoded_sha256=sha(b),encoding='gzip'))
emit(hist+'/pr8176-original-manifest.json',json.dumps(man,indent=2)+'\n')
emit(hist+'/README.md', '''# PR8176 exact recovery and deferred mathematical implications

The [manifest](pr8176-original-manifest.json) preserves all29 original paths,
Git modes/blobs and decoded SHA-256 hashes, plus the complete original delta.
Deterministic gzip payloads retain every proof, failed general DP, integer
program, search, refuter, output and campaign record byte for byte. Decode
with `gzip -dc originals/<name>.gz`; restore the manifest mode.
Recovery is independent of branch retention. The original branch must also
remain available on partial closure because formal negative certification
and broader scientific obligations remain deferred.

The [readable deferred science](pr8176-deferred-science.txt) preserves the full
valid uniform-budget implication with its repaired domain and the complete
original note. Historical incorrect claims are explicitly superseded there.
Historical PASS/results and unseeded search outputs are not current authority.
No shared campaign, current-main manifest or generated status is replaced.
''')
emit(defer,'''PR8176: corrected mathematical implications; formal negative packet DEFERRED

This is readable recovery, not an autonomous live bounded/no-go claim.
The finite single-seed DP proof and explicit witnesses remain canonical.
The original universal ratio definition is undefined on an isolated seed:
its only tree has E=A=F=0,S=1 and satisfies every nonnegative-c budget.
For finite realizations define coverage directly: there exists a family tree
with E-3(S-1)-cA<=0. Do not identify this predicate with a restricted ratio
minimum unless its A>0 domain is nonempty and A=0 alternatives are handled.
The raw W3 ratio -12/17 is not clamped to zero.

Correct uniform-budget implication. In ZA the unique seed has three live
successors, each amplified. Every root-to-seed arrow chain therefore includes
an amplified node, so every tree has A>=1. The exact finite minimum at c=1
is0: every tree has E-3(S-1)>=A. For c<1 its cost is at least(1-c)A>0.
Consequently any uniform budget that supplies some family tree for EVERY
realization must have c>=1. This valid implication is not refuted by an
incomplete procedural negative packet. It does not prove c=1 suffices globally.

Conditional scalar implication. Given c>=1, epsilon2>0 and
0<t<1 with t+epsilon2/t^c<4/27, necessarily t<4/27 and
 epsilon2<t^c(4/27-t)<=t(4/27-t)
 =4/729-(t-2/27)^2<=4/729.
For positive real p and d3=(2p+11)/(p^2+2p+11), d3<4/729 is equivalent,
by multiplying positive denominators, to4p^2-1450p-7975>0, hence
p>(725+sqrt(557525))/4. The rounded exclusion p<=367 is for INTEGER p.
p=36799/100 passes this scalar test; it is not a complete recursion certificate.
A stochastic domination theorem, count bound and physical application are
not proved by these algebraic implications. Four rational super-solutions
are only four supplied-recursion points, not all p>=453 or an optimum.
No global construction upper bound2, phase theorem or strength near11 is
imported from historical/unlanded campaign handoffs.

N1 has actual component/extra-seed and DP coverage arguments, not five
normalized attacked families. Different families are outside scope; c=1
attainment is open; c>1 possibilities strengthen rather than attack the bound;
point certificates address another claim. Formal negative certification is
therefore deferred without falsifying the valid argument. Preserve the branch.
The following complete original note retains all original proof and historical
detail. Its ratio-domain claim,108-mark count, real rounded floor, global/phase
rhetoric and historical author certification are superseded above and in the
canonical note; its bytes are also preserved exactly in the gzip archive.

================ COMPLETE ORIGINAL NOTE ================

'''+old)
def part(a,b):return old.split(a,1)[1].split(b,1)[0]
objects='Declared objects.'+part('Declared objects.','## Prior art and what is new')
a=objects.index(' The **cost**');b=objects.index('- **The component.**',a)
objects=objects[:a]+''' The **cost** for any real c is `E-3(|S|-1)-c|A|`, including trees with `|A|=0`. Write `m(c)` for its minimum over the finite nonempty family. The raw ratio statistic `rho(eta,x)` is the minimum of `(E-3(|S|-1))/|A|` over trees with `|A|>=1` ONLY when that restricted family is nonempty; otherwise it is undefined. We assert no universal coverage equivalence from this restricted statistic. An isolated seed has just its singleton tree, cost0 for every c and undefined rho. Ratios such as W3's `-12/17` remain negative raw statistics.\n'''+objects[b:]
objects=objects.replace('the 108 marks','the 36 marks').replace("block 31's witnesses",'the three supplied finite witnesses')
a=objects.index('- **The recursion.**');objects=objects[:a]+'''- **The supplied recursion.** `D=(1+xU)^2(1+3xD)(1+yF)^6`, `U=(1+xU)^3(1+yF)^6`, `F=(1+xU)^3(1+3xD)(1+yF)^5`, `R=(1+xU)^3(1+3xD)(1+yF)^6`. These are declared finite polynomial products, not a supplied probability theorem. The scalar comparison condition is explicitly `x<4/27`. The deviations are defined in T4 below.\n\n'''
# Remove source-specific contextual inference while retaining all object definitions.
objects=objects.replace("(the same as on the infinite lattice, since the marks are inside the box)","(outside values fixed to zero for this finite problem)")
t1='## Theorem T1 — finite component reduction and dynamic program\n\n'+part('## Theorem T1 — the reduction','## Theorem T2')
t1=t1.replace('a set `N` of 1-sites','a set `N` of 1-sites contained in `C(eta,x)`')
t1=t1.replace('∎ Executed:', '∎ Historical original-source execution (not a fresh corrected-source run):')
t2='''## Theorem T2 — exact finite minimum values

'''+part('**T2.1 (`Z_A`).**','**T2.3 (the constant).**')
a=t2.index(' Hence every tree');b=t2.index(' An optimal tree',a);t2=t2[:a]+t2[b:]
t2+='''**Proof and domain.** T1 enumerates precisely the node sets in each unique-seed component; its exact rational level transfer gives the displayed minima. Choosing one live predecessor per non-seed in the recovered node set gives the exhibited tree and its independently recounted E,A,S. A minimum of finitely many affine functions with slopes `-A<=0` is non-increasing and concave: for0<=lambda<=1, every tree's affine value at the interpolated c is at least the interpolation of the two minima, so the minimum is too. This is a finite optimization identity. The uniform-budget implication is preserved completely in the readable deferred argument, with formal negative certification withheld.\n\nThe root of ZA sits nine levels above the seed, whose three live successors are amplified. An optimal tree uses the chain `(2,2,3)->(2,1,3)->(2,1,2)->(1,1,2)->(1,0,2)->(1,0,1)->(0,0,1)->(0,0,0)`. Every root-to-seed chain includes an amplified node; the ratio domain is nonempty here. No assertion about a typical or infinite realization follows.\n\n'''
t3='''## Theorem T3 — explicit finite tree ratios

W1 has a single-seed component, minimum0 at c=3/4 and positive minimum at74/100, with an exhibited tree E=6,A=8,S=1. Its restricted ratio minimum is3/4. Indeed the zero minimum implies each E-(3/4)A>=0, while the exhibited tree attains equality and has A>0. The positive minimum at74/100 is a separate finite check.

W2 carries the explicitly listed tree E=7,A=11,S=2,F=1, ratio4/11. W3 carries the explicitly listed tree E=9,A=17,S=8,F=7, numerator `E-3(S-1)=-12`, raw ratio `-12/17`. These two displayed ratios are witness values, not asserted minima. They are not silently clamped. Their full arrow/fork fixtures are retained in the primary.

**Proof.** Rebuild the finite automaton in increasing level order. For each listed arrow check that its lower endpoint is a live predecessor; count exactly one such arrow from every non-seed and none from seeds. Each fork joins live siblings. The endpoint graph contains the specified root, is connected and has one fewer edges than nodes, hence is a tree. Recounting processed, amplified and seed nodes gives the integers above, and division gives the ratios. T1 supplies the W1 minimum. No global construction or sharpness theorem is invoked. ∎

'''
f=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='family_e');cert=next(n.value for n in f.body if isinstance(n,ast.Assign) and n.targets[0].id=='certs')
t4='''## Theorem T4 — four supplied-recursion certificates and scalar identities

For p,q,r>0 define
`d1=1-p^3/(p^3+q^3+4r^3)`,
`d2=1-p^2*q/(p*q*(p+q)+4r^3)`,
`d3=1-p^2*r/(r*(p^2+q^2)+r^2*(p+q)+2r^3)`.
Set epsilon1=d1,epsilon2=max(d2,d3), x=t+epsilon2/t, y=epsilon1/t^3.
These are supplied rational definitions. Equivalently enumerate six signed
coordinate axes with pair weights p for equal, q for opposite and r for
perpendicular axes: predecessor triples (a,a,a),(a,a,-a),(a,a,b) with b
perpendicular to a give the three denominators by summing their six product
weights. This is finite algebra, not a physical rule selection.

Each key below is ONE parameter point; each value is `(t,Dbar,Ubar,Fbar)`:

```python
'''+ast.get_source_segment(src,cert)+'''
```

`Fraction(n,d)` means n/d. Substitute into the four declared polynomials
and clear their positive denominators. Each triple dominates its three
right sides, all three entries are at least1, x<4/27 and epsilon1*Rbar<1/100000.
The primary retains those exact rational checks. These four points do not
establish an interval, optimality, a stochastic bound or an ordered phase.

The completed-square identity
`t*(4/27-t)=4/729-(t-2/27)^2`
gives maximum4/729 on[0,4/27], attained at2/27. For c>=1 and0<t<1,
`t^c<=t`. Thus, CONDITIONAL on epsilon2>0 and `t+epsilon2/t^c<4/27`,
`epsilon2<t^c*(4/27-t)<=t*(4/27-t)<=4/729`.
On(p,1,2), `d3=(2*p+11)/(p*p+2*p+11)`. For real p>0,
`d3<4/729` is equivalent to `4*p*p-1450*p-7975>0`, by positive-denominator
cross multiplication, or `p>(725+sqrt(557525))/4`. Direct substitution gives
`d3(367)>4/729>d3(368)`. The rounded necessary condition p>=368 is only
for positive INTEGER p; `p=36799/100` passes the scalar inequality but is
not a full recursion certificate. The broader negative route inference is
readable and deferred; no physical conclusion is imported. ∎

'''
fences=('This note retains exact finite marked-tree minima, explicit witness ratios and four supplied polynomial certificates; no physical rule, order or coupling is selected.','The ratio statistic is defined only on its nonempty positive-amplification domain; zero-amplification costs remain defined and negative witness ratios are not clamped.','Formal negative certification and global construction conclusions remain deferred; finite checks and point certificates do not supply five closed attack families.')
header=f'''---
claim_id: {cid}
claim_type: bounded_theorem
claim_scope: "Finite single-seed component reduction and exact level dynamic program; ZA/ZB/W1 minima, explicit W2/W3 tree ratios, four supplied-recursion rational point certificates and conditional scalar algebra. No global optimum, physical phase or completed negative certification."
upstream_dependencies:
  - minimal_axioms
runner: {run}
---

# Single-seed marked-tree dynamic programming and finite rational certificates

**Type:** bounded_theorem
**Status:** bounded-support; supplied finite objects, unaudited.
**Primary:** [exact finite checks](../{run}).
**Cache:** [source-bound execution evidence](../logs/runner-cache/{Path(run).stem}.txt).
**Recovery:** [complete original proofs, failures and deferred implications](work_history/review_loop/pr8176/README.md).

## Result up front

The finite component reduction and complete DP proof give the explicit minima
and tree constructions below. All five witness fixtures and four rational
certificates remain exact. ZA has20 marks; ZB has36. The finite ratio domain
is explicit, including the isolated-seed exception. The complete valid
uniform-budget implication is preserved readably with formal negative
certification deferred. No corrected-source execution occurred during author
preparation. Historical searches are recovery rather than live evidence.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite marked-tree optimization and supplied polynomial certificates"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "same-session affected source confirmation and bounded exact-source capture"
conditional_surface_status: "supplied finite objects only; broader negative certification deferred"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axioms memo](MINIMAL_AXIOMS_2026-06-29.md) supplies framework context:
one fixed covariant nearest-neighbor rule, probabilities varying with its
conditions, records forming and only records readable. It does not select
these finite objects. The primary reads and pins the context-only source
`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`.
No theorem from that context is required here. All automaton, graph, tree,
weights and polynomial definitions needed below are supplied explicitly;
historical campaign handoffs are not imported mathematical authority.

'''
footer='''## No-Go Discipline Gate — DEFERRED applicability record

N1: component containment/extra seeds and DP coverage are actual arguments;
the independent original review used a separate bottom-up integer DP, direct
sequential automaton and pairwise geometry, full finite tree validation, and
six-menu/port enumeration. These are not five normalized attacked families
against one negative target. Different families are outside scope; uniform
attainment at c=1 remains open; c>1 possibilities strengthen the lower bound;
point certificates address another question. No quota PASS is invented.
N2: no repository wall is imported. N3: finite outside-zero domain, graph,
marks, cost and restricted ratio domain are explicit. N4: axiom source is
framework context; product-law source is context only; open handoffs are
historical. N5: finite sites, subsets and rational points are tested when the
primary is captured; no spectral modes or infinite lattice is executed.
N6: preserve the original branch and complete readable negative argument.
N7: worst-case finite implications do not identify typical configurations or
supply a probability count. N8: historical unseeded/seeded searches and the
failed general DP stay exact recovery; sampled maxima are not global values.

## Boundaries and non-claims

'''+ '\n\n'.join(fences)+f'''

## Imports

Finite graph connectivity, finite dynamic programming, exact rational
arithmetic and concavity of a finite minimum of affine functions are proved
or used at the stated definition level. No stochastic domination, count
coverage, global upper budget or physical application is supplied here.
The original full proofs and historical attempts are preserved in recovery.

## Verification

Expected stdout is `TOTAL: PASS=22 FAIL=0`: the original19checks plus an
isolated-seed domain check, exact36-mark check and real-parameter scalar
boundary check. The original seeded tiny-realization batch is unchanged;
its accepted sample counts are reported at runtime. The program writes no
JSON. Only the three changed-claim targets need new mutation consideration;
unchanged historical mutations are retained, not routinely rerun.

```bash
python3 {run}
python3 {run} --list-mutations
```
'''
new=header+objects+t1+t2+t3+t4+footer
emit(note,new)
s=src;a=s.index('"""');b=s.index('"""',a+3)+3;s=s[:a]+'''"""Finite single-seed dynamic programming, explicit marked-tree ratios and
four supplied polynomial point certificates. Complete finite fixtures and
exact arithmetic retained; broader negative certification is deferred.
No physical phase, optimum or real rounded threshold is established.
Stdout-only checks; no historical search or optimizer is executed.
"""'''+s[b:]
s=s.replace('import random','import hashlib\nimport random',1).replace(on,note).replace(Path(on).stem.lower(),cid).replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 60')
s=s.replace('    "forks_dropped_in_family": "B",','    "forks_dropped_in_family": "B",\n    "isolated_seed_cost_wrong": "B",\n    "zb_mark_count_wrong": "C",\n    "real_boundary_rounded": "E",')
s=s.replace('def family_b(checks: Checks) -> None:\n','''def family_b(checks: Checks) -> None:
    eta_seed = {(0, 0, 0): 1}
    seed_cost, _, seed_nodes = single_seed_min(eta_seed, (0, 0, 0), Fraction(1))
    expected_seed = Fraction(1) if mut("isolated_seed_cost_wrong") else Fraction(0)
    checks.check("B3", seed_cost == expected_seed and tree_counts(eta_seed, seed_nodes) == (0, 0, 1), "isolated seed: zero cost and zero amplification; restricted positive-amplification ratio domain is empty")
''')
s=s.replace('def family_c(checks: Checks) -> None:\n','''def family_c(checks: Checks) -> None:
    mark_target = 108 if mut("zb_mark_count_wrong") else 36
    checks.check("C4", len(Z_B[2]) == len(set(Z_B[2])) == mark_target, "Z_B has exactly36 distinct marked sites; the original fixture bytes are retained")
''')
needle='    checks.check("E2", ok2,';a=s.index(needle);b=s.index('\n',a)
s=s[:a]+'''    checks.check("E2", ok2, f"T4: scalar maximum4/729 and integer crossing367/368; d3 values {d3a}, {d3b}; conditional algebra, not a physical route theorem")
    real_p = Fraction(36799, 100)
    real_d3 = deviations(real_p, 1, 2)[2]
    polynomial = 4 * real_p ** 2 - 1450 * real_p - 7975
    scalar_ok = real_d3 < Fraction(4, 729) and polynomial > 0
    if mut("real_boundary_rounded"):
        scalar_ok = scalar_ok and real_p >= 368
    checks.check("E3", scalar_ok, "real p=36799/100 satisfies the exact necessary polynomial inequality; this is not a full recursion certificate")'''+s[b:]
# Reporting strings only: leave the computational families otherwise intact.
s=s.replace('every tree has E >= 3(|S|-1) + |A|','finite minimum at c=1 is zero')
s=s.replace('with its concavity (a minimum of affine functions) and the values at 99/100 and 1, no tree of Z_A satisfies E <= 3(|S|-1) + c|A| for any c < 1, while E - 3(|S|-1) = 6 is the least over trees without amplification credit','the concavity proof is written in the note; these are finite rational values, with zero-credit minimum6')
s=s.replace('inside block 25\'s seed budget with no amplification credit at all','raw ratio -12/17, not clamped')
s=s.replace("T4 (the stake): if a construction attains c = 1,",'T4: for the supplied polynomial definitions,').replace("(block 31's certificates re-verified)",'(four points only; no parameter interval or physical conclusion)')
s=s.replace("block 31's first witness",'the first supplied witness').replace("block 01's note (on main)",'the context-only product-law note')
inputs=[note,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md'];pins={p:sha((W/p).read_bytes()) for p in inputs}
s=s.replace('ROOT = Path(__file__).resolve().parents[1]','INPUT_SHA256 = '+repr(pins)+'\nROOT = Path(__file__).resolve().parents[1]')
s=s.replace('all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS)','all(Path(ROOT,p).is_file() and hashlib.sha256(Path(ROOT,p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS)').replace('"all declared inputs exist"','"all three declared inputs match literal SHA-256 pins"')
a=s.index('FENCES = (');b=s.index('FORBIDDEN = (',a);s=s[:a]+'FENCES = '+repr(fences)+'\n'+s[b:]
n5=('per_element: executed — exact rational finite-subset costs, tree counts and the completed-square scalar maximum; full DP completeness is a written proof','per_site: executed — five fixed finite marked windows, component connectivity and predecessor/fork validation; Z_B contains36 distinct marks','per_mode: checked and not executed — no spectral decomposition is used; cost parameters and finite subsets are not spectral modes','per_block: executed — unchanged seeded tiny-fixture batch, exact finite minima, four supplied-recursion points and isolated-seed/real-scalar boundaries','lattice_wide: checked and not executed — no infinite lattice or global construction search; the written conditional implications have deferred formal negative certification')
a=s.index('N5_LINES = (');b=s.index('\n\n\ndef family_g',a);s=s[:a]+'N5_LINES = '+repr(n5)+s[b:]
compile(s,run,'exec');emit(run,s)
# Static independent comparison: no computational function calls.
class Norm(ast.NodeTransformer):
 def visit_Constant(self,n):return ast.copy_location(ast.Constant('<text>'),n) if isinstance(n.value,str) else n
nt=ast.parse(s);same={}
for f in tree.body:
 if isinstance(f,(ast.FunctionDef,ast.ClassDef)) and f.name not in ['family_a','family_b','family_c','family_e','family_f','family_g']:
  nf=next(x for x in nt.body if type(x)==type(f) and x.name==f.name);same[f.name]=ast.dump(Norm().visit(f))==ast.dump(Norm().visit(nf));assert same[f.name],f.name
for key in ['Z_A','Z_B','W1','W2','W3','W2_TREE','W3_TREE']:
 def val(t):return next(n.value for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id==key)
 assert ast.dump(val(tree))==ast.dump(val(nt)),key
paths=subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines();assert len(paths)==35,len(paths)
existing={Path(p).name for p in subprocess.check_output(['git','-C',str(W),'ls-files','docs'],text=True).splitlines()};names=[Path(p).name for p in paths if p.startswith('docs/') and Path(p).name not in ['README.md','SKILL.md']];assert len(names)==len(set(names));assert not set(names)&existing
rows=[dict(path=p,mode='100644',sha256=sha((W/p).read_bytes())) for p in paths];snap=R/'drain8176-prepared-source-v1';assert not snap.exists()
for p in paths:(snap/p).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/p,snap/p)
prepared=dict(schema_version=1,kind='author-preparation-not-review-verdict',pr=8176,owner='PR8176-author',base=BASE,head=report['original_head'],source_count=35,source=rows,original_count=29,canonical_notes=[note],primaries=[run],deferred_science=[defer],snapshot=str(snap),original_manifest=dict(path=hist+'/pr8176-original-manifest.json',sha256=sha((W/hist/'pr8176-original-manifest.json').read_bytes())),mathematical_function_ast_comparison=same,fixtures_unchanged=True,explicit_changes=['isolated-seed B3 domain check','ZB distinct-mark count C4','real scalar boundary E3; targeted mutations for these three checks','input SHA pins, reporting and60second timeout'],primary_runs=0,mutation_runs=0,simulation_runs=0,staged=False,branch_preservation_required=True,document_basename_collisions=[])
dump(R/'drain8176-author-prepared-v1.json',prepared);dump(R/'drain8176-source-freeze-v1.json',dict(schema_version=1,source=rows,base=BASE,snapshot=str(snap),prepared_sha256=sha((R/'drain8176-author-prepared-v1.json').read_bytes())))
claims=[dict(original='T1 full component/single-seed/DP proof',destination=note,disposition='complete proof retained; node sets explicitly in component; ratio restricted to nonempty A>0 domain'),dict(original='T2 finite minima and T3 witness trees',destination=note,disposition='finite minima/counts/fixtures retained; ZB36 marks bound; W3 raw negative ratio retained'),dict(original='T2 uniform-budget negative implication',destination=defer,disposition='complete correct argument readable; formal negative certification deferred; original note exact'),dict(original='T4 point certificates/scalar algebra',destination=note,disposition='four exact supplied points retained; real polynomial condition and integer scope corrected'),dict(original='T4 phase/global threshold/historical searches',destination=defer,disposition='unsupported physical/optimum/region authority withdrawn; full original proofs and failures preserved, branch retained')]
dump(R/'drain8176-author-dispositions-v1.json',dict(schema_version=1,constituents=[dict(pr=8176,head=report['original_head'],delta_base=report['original_base'],dispositions=entries)],claims=claims,original_delta=man['original_delta']))
(R/'drain8176-author-corrections-v1.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=on,tofile=note))+''.join(difflib.unified_diff(src.splitlines(True),s.splitlines(True),fromfile=op,tofile=run)))
print(json.dumps(dict(source_count=35,prepared_sha256=sha((R/'drain8176-author-prepared-v1.json').read_bytes()))))
