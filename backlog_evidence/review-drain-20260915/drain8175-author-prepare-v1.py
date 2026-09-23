from pathlib import Path
import ast,json,hashlib,gzip,shutil,difflib,subprocess,re
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';O=R/'drain8175-original/head';BASE='51cac1ae0ed3f9d0f399a63a716f8cf351fc5938';HEAD='798f661da7140ff6f73c5e4f4984d80b67b3447a'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==BASE
assert not subprocess.check_output(['git','-C',str(W),'status','--porcelain'],text=True)
owner=json.loads((R/'drain-author-slot.json').read_text());assert owner['owner']=='PR8175-author'
def emit(p,s,mode=0o644):
 p=W/p;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(s.encode() if isinstance(s,str) else s);p.chmod(mode)
def dump(p,x):assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
review=json.loads((R/'drain8175-review-original.json').read_text());disp=review['path_dispositions'];assert len(disp)==28
oldnote=next(x['path'] for x in disp if x['path'].startswith('docs/ADMISSIBILITY'));oldrun=next(x['path'] for x in disp if x['path'].startswith('scripts/'));original=(O/oldnote).read_text();oldsource=(O/oldrun).read_text()
note='docs/EXTENDED_EXPLANATION_TREE_FINITE_WITNESS_COUNTS_AND_RATIONAL_RECURSION_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md';runner='scripts/extended_explanation_tree_finite_witness_counts_rational_certificates_check_2026_09_16.py';cid=Path(note).stem.lower();stem=Path(runner).stem
hist='docs/work_history/review_loop/pr8175';deferred=hist+'/pr8175-deferred-science.txt';entries=[]
for i,d in enumerate(disp):
 raw=(O/d['path']).read_bytes();h=d['head'];assert sha(raw)==h['sha256'];assert subprocess.check_output(['git','-C',str(W),'cat-file','blob',h['blob']])==raw
 dest=f'{hist}/originals/{i+1:02d}-{Path(d["path"]).name}.gz';encoded=gzip.compress(raw,mtime=0);emit(dest,encoded)
 entries.append(dict(original_path=d['path'],mode=h['mode'],git_blob=h['blob'],original_sha256=h['sha256'],recovery=dict(path=dest,encoding='gzip',sha256=sha(encoded),decoded_sha256=sha(raw)),disposition='narrowed' if d['path'] in [oldnote,oldrun] else 'historical-recovery-only',canonical_path=note if d['path']==oldnote else runner if d['path']==oldrun else None))
patch=(R/'drain8175-original/original.patch').read_bytes();patchpath=hist+'/pr8175-original-delta.patch.gz';enc=gzip.compress(patch,mtime=0);emit(patchpath,enc)
manifest=dict(schema_version=1,kind='exact-original-recovery-manifest',pr=8175,head=HEAD,delta_base=review['original_base'],entries=entries,original_delta=dict(path=patchpath,encoding='gzip',sha256=sha(enc),decoded_sha256=sha(patch)))
emit(hist+'/pr8175-original-manifest.json',json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
emit(hist+'/README.md','''# PR8175 complete original recovery and deferred science

The [manifest](pr8175-original-manifest.json) binds all 28 original paths,
Git modes, blobs and decoded SHA-256 hashes, and the complete original delta.
Deterministic gzip preserves every byte independently of branch retention.
Decode with `gzip -dc originals/<name>.gz` and restore the listed mode.
Full original controls, failed candidate constructions, searches, outputs,
cache and campaign records remain historical. Their author PASS assertions
are not review or audit authority; no shared current-main file is replaced.

The [readable deferred argument](pr8175-deferred-science.txt) contains the
precise corrected negative inference and the complete original note verbatim.
The finite positive constructions, charge identities and rational arithmetic
remain live in the canonical note. Formal negative certification is incomplete;
the original branch must be retained on partial closure. No fifth route family
has been invented. The exact witnesses do not prove that a global constant two
is sharp. Historical sampling and hill-climbing have no exhaustive scope.
''')
emit(deferred,'''PR8175 — readable deferred science and complete original proof recovery

STATUS: precise mathematical negative inference preserved, formal negative
packet DEFERRED. Not a live bounded claim or an independent wall/premise.

Corrected inference. For the declared construction, the exact finite trees
have (E,|A|,|S|,F)=(16,10,1,0),(20,12,1,0),(23,12,2,1).
Substitution gives E-3(|S|-1)-|A|=6,8,8 and ratios8/5,5/3,5/3.
If a constant c satisfies E<=3(|S|-1)+c|A| on every tree produced by this
construction, apply that assertion to the second finite tree:20<=12c,
so c>=5/3. In particular c=1 fails for this construction. This proof is
valid mathematics, not refuted by the incomplete procedural packet.

The fork-free local patterns (b,a,e)=(1,1,2),(2,2,1),(3,3,0) have
r=1-b and e=3r+2a. Since a>0, they force c>=2 only for a universal
PER-REFINEMENT inequality e<=3r+c a covering those patterns. They do not
force the same constant in a GLOBAL sum with compensating refinements.
A neutral two-step period has (r,e,a)=(0,4,2), but chains of arbitrary
length are not constructed. W1,W2,W3 contain exactly2,1,1 consecutive
periods, respectively, not2 each. The global lower bound is5/3. The upper
bound2 is conditional on a separately justified universal construction
budget; the original open handoff is not accepted proof authority here.
No global sharpness2, exclusion of constants in[5/3,2), compulsory change
of pole rule, or general restriction on other constructions is established.

The original six listed concerns do not constitute five normalized closed
attack families. Witness validation and global compensation are relevant;
different constructions are outside scope, attainment2 is unproved, and
counterfactual recursion arithmetic is a separate question. No N1 PASS is
asserted. The original branch remains the handle for this deferred work.

The following COMPLETE ORIGINAL NOTE is byte-preserved as text, including
all proof details, witness descriptions, old errors, claims and history.
Its global-sharpness rhetoric, period counts and author certification are
superseded by the corrections above; no omitted theorem is replaced by a
summary. The exact original bytes also remain in the manifest archive.

================ COMPLETE ORIGINAL NOTE ================

'''+original)
def part(a,b):return original.split(a,1)[1].split(b,1)[0]
objects='Declared objects.'+part('Declared objects.','## Prior art and what is new')
objects=objects.replace("This is block 30's automaton `η'` with the uniforms replaced by the marks they produce: `ζ` is the set of sites at which the uniform falls below the relevant noise level.","This is a declared deterministic marked automaton; no probabilistic domination or selected physical rule is assumed.")
objects=objects.replace("— block 30's construction",'— declared construction')
a=objects.index('- **The budgets.**');b=objects.index('- **The witnesses.**',a)
objects=objects[:a]+'''- **Finite counts.** `F=#forks`, `E=sum e`, `|A|=sum a`; for the explicitly reconstructed trees these equal distinct edge/node counts. The arithmetic ratio is `(E-3(|S|-1))/|A|` when `|A|>=1`. No universal budget is imported.\n'''+objects[b:]
a=objects.index('- **The recursion of block 25');objects=objects[:a]+'''- **Declared polynomial recursion.** `D=(1+xU)^2(1+3xD)(1+yF)^6`, `U=(1+xU)^3(1+yF)^6`, `F=(1+xU)^3(1+3xD)(1+yF)^5`, `R=(1+xU)^3(1+3xD)(1+yF)^6`. A rational triple `(Dbar,Ubar,Fbar)>=1` is a super-solution when it dominates the three right sides. Here `x=t+epsilon_2/t`, `y=epsilon_1/t^3` are declared algebraic weights only. No probability or formation threshold follows from a certificate.\n\n'''
t1='## Theorem T1 — accounting identities and local period\n\n'+part('## Theorem T1 — the accounting identities and the two-level period','## Theorem T2')
a=t1.index('*Remark (what');t1=t1[:a]
t1=t1.replace("(block 30's spanning identity, restated: each pole's charge either travels to its excuse, gaining `1/3` or losing `2/3`, or is carried across the forks with the fork endpoints' charges telescoping)","(the pole-assignment identity justified below)")
t1=t1.replace('and at most `1 − b + f` otherwise','and at most `1 − b + f` when each created fork has nonnegative span; that condition is checked on the three finite witnesses, not imported as a universal construction theorem')
t1=t1.replace("Executed on the three witnesses' logs (B2).","The three witness logs satisfy these identities (B2); the runner also checks equality of accumulated counts with independently recounted distinct edges/nodes. For a general refinement history, the telescoping assertion is conditional on termination at singleton seeds and the stated pole assignment, not an existence theorem for all marked inputs.")
t1=t1.replace("Each of the three witnesses realises the pair as consecutive refinements of its log (B3: `4` occurrences; W1 twice, W2 twice). Whether the pair can be repeated an arbitrary number of times is not proved here; the witnesses contain two periods each.","The exact consecutive-period counts in `(W1,W2,W3)` are `(2,1,1)` (B3), four in total. The equality is local arithmetic; arbitrary repetitions and a sharp global ratio are not asserted.")
t1+='''**Pole-assignment proof.** Regard the finite cluster/fork incidence tree as an abstract tree. For each charge k, the terminal is the cluster containing its excuse u_k; every other vertex takes the intersection point on its first edge toward that terminal. Remove a leaf vertex not carrying all terminals. For each charge whose terminal is outside the leaf, the leaf's assigned point is its unique edge intersection q. For charges with terminal in the leaf, the adjacent vertex currently carries q, and deleting the leaf transfers their terminal value to that neighbor. Thus the change in the sum over all vertices for all charges is `sum_k M_k(q)=0`. Repeating leaf removal reduces the sum to `sum_k M_k(u_k)`. The coordinate calculation in T1.1 makes this `Span(K)+1-b`. Subtracting old cluster span and adding one to the fork counter per new fork gives the exact rise formula. Summing these actual potential differences gives the terminal potential minus the initial potential. At a singleton seed all three poles coincide, so their span is zero. This proves the stated identity under the explicit finite refinement conditions without importing the separate global budget.\n\n'''
# Positive exhibition only; negative implication has full corrected proof in deferred text.
t2='''## Theorem T2 — three exact finite constructions

The complete marks and deterministic construction are specified above and in
the linked primary. Reconstruct the automaton in increasing level order,
choose the first two live predecessor indices at each processed site, and
apply the declared cluster/pole algorithm. Recount edges and nodes separately.
The resulting finite identities are:

| Witness | E | amplified nodes | seeds | forks | ratio | consecutive periods |
|---|---:|---:|---:|---:|---|---:|
| W1 |16|10|1|0|8/5|2|
| W2 |20|12|1|0|5/3|1|
| W3 |23|12|2|1|5/3|1|

**Proof by explicit finite construction.** W1 has27nodes,10refinements and10bad
pairs; W2 has33nodes,12refinements and12bad pairs; W3 has37nodes,13refinements,
12bad pairs and one fork. Every excuse arrow joins a processed-type live
site to a live predecessor, each amplification arrow joins a site with exactly
one live predecessor to that predecessor, and each seed has no live predecessor.
The point graph contains the root, is connected and has one fewer edges than
vertices, hence is a tree. All vertices are live sites. W1's eleven marks
are exactly its seed and ten amplified sites. These are finite claims verified
by the explicit algorithm and independently recounted witness records;
B2/B3/C1/C2/C5 reconstruct and test them, rather than assume a global theorem.
Subtracting the integer counts gives `E-3(|S|-1)-|A|=(6,8,8)` and
`3(|S|-1)+2|A|-E=(4,4,4)`; the ratios in the table follow by division. ∎

'''
t2+=part('*Reading of the witnesses.*','## Theorem T3').join(['*Reading of the witnesses.*',''])
t2+='''The fixed seeded sample in C4 has300cones of depths3through8 and four integer
noise percentages. Its resulting maximum is a property of that sample only.
It does not provide an upper bound over all inputs or demonstrate uniform
search coverage. The historical40000-cone search, candidate collapse,
hill-climbs and refuter outputs are fully archived; none is rerun in preparation.
The global negative inference from these counts is preserved separately with
explicit incomplete formal certification, not promoted by this finite table.

'''
# All exact certificate literals copied, not recomputed.
tree=ast.parse(oldsource);fd=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='family_d');certnode=next(x.value for x in fd.body if isinstance(x,ast.Assign) and x.targets[0].id=='certs');certsrc=ast.get_source_segment(oldsource,certnode)
t3='''## Theorem T3 — rational polynomial certificates

For positive supplied `(p,q,r)`, define purely rational quantities
`d1=1-p^3/(p^3+q^3+4r^3)`,
`d2=1-p^2 q/(pq(p+q)+4r^3)`,
`d3=1-p^2 r/(r(p^2+q^2)+r^2(p+q)+2r^3)` and
`epsilon_1=d1`, `epsilon_2=max(d2,d3)`.
These may also be computed by enumerating the six signed coordinate axes:
weights p for equal values, q for opposite values on the same axis, and r
for perpendicular axes, taking predecessor triples `(a,a,a)`, `(a,a,-a)`
and `(a,a,b)` with b perpendicular to a. Summing the six products gives
exactly the three displayed denominators; dividing the target a product by
each sum gives the stated deviations. This defines the algebra without an
imported menu theorem or a probability domination claim.

At each tuple below, `(t,Dbar,Ubar,Fbar)` is an exact super-solution for the
declared recursion with `x=t+epsilon_2/t`, `y=epsilon_1/t^3`:

```python
'''+certsrc+'''
```

Here `Fraction(n,d)` denotes the exact rational n/d. Substitute each tuple
into the four finite products above. Clearing their positive denominators
verifies `Dbar>=rD`, `Ubar>=rU`, `Fbar>=rF`, the three values at least1,
`x<4/27`, and `epsilon_1 Rbar<1/100000`; D1 checks these exact inequalities.
Independent original review recomputed the six-menu deviations and expanded
all binary port choices, rather than using the same closed forms.

The elementary identity
`t(4/27-t)=4/729-(t-2/27)^2`
proves its maximum on `[0,4/27]` is `4/729`, attained at `2/27`.
Direct rational substitution gives `d3(367,1,2)>4/729>d3(368,1,2)`.
The four comparison ratios `4165/453`, `2085/232`, `8330/905`, `6247/677`
each lie strictly between8and10 by cross multiplication (D2/D3).
These are arithmetic comparisons, not validated old/new formation regions.
The original conditional probability interpretation requires a separate
construction/count theorem and the budget discussed in deferred science;
no such theorem or threshold is imported here. ∎

'''
fences=('This note retains exact finite construction counts, local charge identities and rational polynomial certificates for explicitly declared objects; no physical rule, order or coupling is selected.','A local ratio-two period does not establish a sharp global constant; the universal upper budget is not imported from an open handoff.','Formal negative certification is deferred in the readable recovery argument; finite witness validity is not a claim of five closed attack families.')
header=f'''---
claim_id: {cid}
claim_type: bounded_theorem
claim_scope: "Exact finite marked-automaton constructions and charge identities for the declared explanation-tree algorithm: counts16/10/1,20/12/1,23/12/2, exact consecutive periods2/1/1 and local neutral arithmetic; four exact rational polynomial super-solutions and completed-square maximum. No global sharpness, universal upper budget, physical formation threshold or completed negative certification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: {runner}
---

# Finite explanation-tree witness counts and rational recursion certificates

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support; declared finite combinatorics and arithmetic, unaudited.
**Primary:** [exact finite checks](../{runner}).
**Cache:** [source-bound execution evidence](../logs/runner-cache/{stem}.txt).
**Recovery:** [full original history and deferred science](work_history/review_loop/pr8175/README.md).

## Result up front

Three explicit finite constructions have ratios8/5,5/3,5/3 and consecutive
local-period counts2,1,1. A two-refinement neutral period has `(r,e,a)=(0,4,2)`.
That local identity does not decide a global sharp constant. All witness marks,
algorithmic steps, accounting identities and rational certificates are retained.
The full corrected negative argument is readable in the recovery packet with
formal certification deferred; incomplete N1 coverage is not a mathematical
refutation. No primary, random-cone fixture or mutation was run during author
preparation. The expected primary count remains20checks; its new exact
per-witness period target replaces the former aggregate-only check.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite witness accounting and rational recursion arithmetic"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "original-reviewer affected confirmation and exact-source bounded evidence; global conclusions remain deferred"
conditional_surface_status: "explicit finite construction and algebraic identities only; no open handoff used as theorem authority"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axioms memo](MINIMAL_AXIOMS_2026-06-29.md) supplies framework context:
one fixed covariant nearest-neighbor rule; conditional probabilities vary
with nearest-neighbor conditions; records form; only records are readable.
It does not select the marked automaton, tree algorithm or weights below.
The primary also pins and reads the context-only finite product-law note
`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`.
No theorem from that note is needed by the finite construction. The historical
open handoffs are archived provenance, not mathematical authority. The
polynomial recursion and six-menu arithmetic are defined explicitly here.

'''
footer='''## No-Go Discipline Gate — DEFERRED applicability record

N1 is incomplete for formal negative certification. Witness validity and
implementation agreement are concrete finite tests; global compensation is
addressed only by the exhibited arithmetic. A different construction is
outside scope; attainment of a global constant2 is unproved; certificate
arithmetic is a separate question. These are not five closed attack families.
N2: no repository wall is imported. N3: marked inputs, outside-zero window,
winning-pair rule, pole assignment and polynomial weights are explicit.
N4: the axioms are framework context, product-law source is context-only,
and historical handoffs have no theorem authority. N5: finite sites and
refinements are executed by the primary when captured; no spectral modes or
infinite lattice are executed. N6: preserve original branch and full negative
proof as deferred science. N7: the global constant may still improve below2;
the local period does not force a change of construction. N8: a seeded sample
maximum does not imply a worst-case bound; earlier historical claims remain
recovery, not repeated authority.

## Boundaries and non-claims

'''+ '\n\n'.join(fences)+'''

## Imports

Finite graph connectivity, a finite tree's edge count, rational arithmetic,
and a completed-square identity suffice. The declared pole-assignment identity
is proved at scope. No global probabilistic domination, formation threshold,
physical identification or accepted no-go wall is imported. Historical
sampling and search outputs remain in their original exact recovery files.

## Verification

Expected output is `TOTAL: PASS=20 FAIL=0`: four input checks, three accounting,
five finite witness/sample checks, three certificate checks, four packaging
checks and one resolution-report check. There are ten mutation definitions,
including a new targeted period-count corruption; this is a source census,
not a new execution result. The primary writes stdout only. The unchanged
seeded300-cone fixture is finite evidence, not an exhaustive theorem.

'''+f'''```bash
python3 {runner}
python3 {runner} --list-mutations
python3 {runner} --mutation period_counts_wrong
```
'''
newnote=header+objects+t1+t2+t3+footer
# Literal terminology corrections only; never a Markdown formula regex.
newnote=newnote.replace('block 30','the historical construction').replace('40 000','40,000')
emit(note,newnote)
s=oldsource;start=s.index('"""');end=s.index('"""',start+3)+3
s=s[:start]+'''"""Exact finite marked-automaton witness counts, local charge accounting and
rational polynomial certificates. Global negative certification and a sharp
constant two are deferred; no physical threshold is obtained. All three exact
witness fixtures and the original seeded300-cone sample are retained. This
primary runs no historical hill-climb or annealing search and writes stdout.
"""'''+s[end:]
s=s.replace('import random','import hashlib\nimport random',1).replace(oldnote,note).replace(Path(oldnote).stem.lower(),cid).replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 60')
s=s.replace('    "period_arithmetic_wrong": "B",','    "period_arithmetic_wrong": "B",\n    "period_counts_wrong": "B",')
s=s.replace('    pairs_total = 0\n','    pairs_total = 0\n    per_witness_pairs = []\n    expected_pairs = (2, 2, 0) if mut("period_counts_wrong") else (2, 1, 1)\n')
s=s.replace('        ok3 = ok3 and (pairs >= 1 or w_ is W3)','        per_witness_pairs.append(pairs)')
s=s.replace('checks.check("B3", ok3 and pairs_total >= 4,','checks.check("B3", ok3 and tuple(per_witness_pairs) == expected_pairs and pairs_total == 4,')
s=s.replace("the witnesses' logs contain {pairs_total} such consecutive pairs","the exact per-witness counts are {tuple(per_witness_pairs)}, total {pairs_total}; no global sharpness follows")
# Reporting-only changes preserve all construction/fixture/certificate calculations.
s=s.replace("block 30's budget",'the comparison expression with coefficient two')
s=s.replace('so no per-refinement inequality gives the sharper budget','these are exact local arithmetic comparisons; formal negative certification remains deferred')
s=s.replace("block 30's executed maximum 2/3 was a sampling artefact",'this fixed seeded sample is not a global upper bound')
s=s.replace("a factor 9 below block 30's region on every line",'pure polynomial inequalities, not a formation region')
s=s.replace("the refutation leaves block 30's ceiling 256/531441 in force",'this algebra does not establish any universal construction budget or formation region')
s=s.replace('the refuted budget would have moved every line by a factor between 8 and 10','the four historical comparison numbers differ by a factor between 8 and 10')
s=s.replace("the sharper budget 3(|S|-1) + |A| = 10 fails by 6",'the arithmetic difference E-[3(|S|-1)+|A|] equals6')
s=s.replace('T3 (the stake): had the sharper budget held, the amplification weight would be epsilon_2/t and the rational triples','T3: at the declared algebraic weight epsilon_2/t the rational triples')
s=s.replace('T3 (the stake): under the sharper budget the ceiling would be','T3: the declared scalar expression has maximum')
inputs=[note,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md'];pins={p:sha((W/p).read_bytes()) for p in inputs}
s=s.replace('ROOT = Path(__file__).resolve().parents[1]','INPUT_SHA256 = '+repr(pins)+'\nROOT = Path(__file__).resolve().parents[1]')
s=s.replace('all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS)','all(Path(ROOT, p).is_file() and hashlib.sha256(Path(ROOT, p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS)').replace('"all declared inputs exist"','"all three declared source/context inputs match literal SHA-256 pins"')
s=s.replace('"block 01\'s note (on main) carries its claim_id and the rule\'s product form"','"the pinned context-only product-law note carries its identity and product-form heading"')
a=s.index('FENCES = (');b=s.index('FORBIDDEN = (',a);s=s[:a]+'FENCES = '+repr(fences)+'\n'+s[b:]
a=s.index('N5_LINES = (');b=s.index('\n\n\ndef family_g',a)
n5=('per_element: executed — exact rational charge increments and local rise/count identities on every refinement of the three specified witnesses','per_site: executed — three marked windows of112,112,225sites, tree connectivity and live-predecessor edge types; unchanged finite fixtures','per_mode: checked and not executed — no spectral decomposition is present; witness classes and seeded cones are finite configurations, not modes','per_block: executed — exact witness period counts2,1,1, the fixed seeded300-cone sample, four rational certificates and scalar completed-square maximum','lattice_wide: checked and not executed — no exhaustive input search, infinite lattice simulation, sharp global budget or formal negative certification')
s=s[:a]+'N5_LINES = '+repr(n5)+s[b:]
compile(s,runner,'exec');emit(runner,s,0o644)
# Independent AST equality except reporting strings and the explicitly requested B3 repair.
class Normalize(ast.NodeTransformer):
 def visit_Constant(self,n):return ast.copy_location(ast.Constant('<text>'),n) if isinstance(n.value,str) else n
na=ast.parse(s);checks={}
for x in tree.body:
 if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name not in ['family_a','family_b','family_f','family_g']:
  y=next(y for y in na.body if type(y)==type(x) and y.name==x.name);checks[x.name]=ast.dump(Normalize().visit(x))==ast.dump(Normalize().visit(y));assert checks[x.name],x.name
# Every fixture and every rational certificate literal preserved; parse data only.
for name in ['W1','W2','W3']:
 a=next(x.value for x in tree.body if isinstance(x,ast.Assign) and x.targets[0].id==name);b=next(x.value for x in na.body if isinstance(x,ast.Assign) and x.targets[0].id==name);assert ast.dump(a)==ast.dump(b)
paths=subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines();assert len(paths)==34,len(paths)
existing={Path(p).name for p in subprocess.check_output(['git','-C',str(W),'ls-files','docs'],text=True).splitlines()};newdocs=[p for p in paths if p.startswith('docs/') and p.endswith(('.md','.txt')) and Path(p).name not in ['README.md','SKILL.md']];assert not [p for p in newdocs if Path(p).name in existing];assert len({Path(p).name for p in newdocs})==len(newdocs)
rows=[dict(path=p,mode='100755' if (W/p).stat().st_mode&0o111 else '100644',sha256=sha((W/p).read_bytes())) for p in paths];snap=R/'drain8175-prepared-source-v1';assert not snap.exists()
for p in paths:(snap/p).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/p,snap/p)
j=dict(schema_version=1,kind='author-preparation-not-review-verdict',pr=8175,owner='PR8175-author',base=BASE,head=HEAD,source_count=len(rows),source=rows,original_count=28,original_manifest=dict(path=hist+'/pr8175-original-manifest.json',sha256=sha((W/hist/'pr8175-original-manifest.json').read_bytes())),canonical_notes=[note],primaries=[runner],deferred_science=[deferred],snapshot=str(snap),primary_runs=0,simulation_runs=0,mutation_runs=0,staged=False,mathematical_function_ast_comparison=checks,explicit_computational_change='B3 exact per-witness periods(2,1,1), new targeted period_counts_wrong expected(2,2,0); no construction/fixture/certificate change',branch_preservation_required=True,document_basename_collisions=[])
dump(R/'drain8175-author-prepared-v1.json',j);dump(R/'drain8175-source-freeze-v1.json',dict(schema_version=1,source=rows,base=BASE,snapshot=str(snap),prepared_sha256=sha((R/'drain8175-author-prepared-v1.json').read_bytes())))
dump(R/'drain8175-author-dispositions-v1.json',dict(schema_version=1,constituents=[dict(pr=8175,head=HEAD,dispositions=entries)],original_delta=manifest['original_delta'],claims=[dict(original='T1 charge/potential identity and local period',destination=note,disposition='complete finite conditional accounting proof retained; exact per-witness counts corrected; global sharpness withdrawn'),dict(original='T2 finite witness construction and exact arithmetic',destination=note,disposition='complete construction/marks and exact counts retained'),dict(original='T2 universal budget exclusion and local necessary constant',destination=deferred,disposition='full valid corrected negative proof readable; formal packet deferred; upper2 conditional'),dict(original='T3 rational certificates',destination=note,disposition='complete exact literals, algebra and completed-square proof retained; probability interpretation deferred'),dict(original='historical searches, failed candidate, raw controls and author status',destination=hist+'/pr8175-original-manifest.json',disposition='all original bytes and full delta preserved; no new execution or authority')]))
(R/'drain8175-author-corrections-v1.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),newnote.splitlines(True),fromfile=oldnote,tofile=note))+''.join(difflib.unified_diff(oldsource.splitlines(True),s.splitlines(True),fromfile=oldrun,tofile=runner)))
print(json.dumps(dict(source_count=len(rows),prepared_sha256=sha((R/'drain8175-author-prepared-v1.json').read_bytes())),indent=2))
