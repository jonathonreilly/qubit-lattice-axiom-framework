from pathlib import Path
import ast,json,hashlib,gzip,shutil,subprocess,difflib
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';O=R/'drain8177-original/head';BASE='64f53dd443cd02997394e1a8bef16e2baf9f9d39';sha=lambda b:hashlib.sha256(b).hexdigest()
assert json.loads((R/'drain-author-slot.json').read_text())['owner']=='PR8177-author'
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==BASE
assert not subprocess.check_output(['git','-C',str(W),'status','--porcelain'],text=True)
j=json.loads((R/'drain8177-review-original.json').read_text());ds=j['path_dispositions'];assert len(ds)==50
on=next(x['path'] for x in ds if x['path'].startswith('docs/ADMISSIBILITY'));op=next(x['path'] for x in ds if x['path'].startswith('scripts/'));old=(O/on).read_text();src=(O/op).read_text();tree=ast.parse(src)
note='docs/ROOTED_MARKED_TREE_EXTENSION_SEED_INDUCTION_AND_RELAXED_LIFTED_TREE_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-17.md';run='scripts/rooted_marked_tree_extension_seed_induction_relaxed_lifted_certificates_check_2026_09_17.py';cid=Path(note).stem.lower();hist='docs/work_history/review_loop/pr8177';defer=hist+'/pr8177-deferred-science-and-history.txt';parent='docs/SIX_AXIS_TWO_LEVEL_DOMINATION_EXTENDED_EXPLANATION_TREE_AND_FOUR_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md';product='docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md'
def emit(p,b):
 p=W/p;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b.encode() if isinstance(b,str) else b);p.chmod(0o644)
def dump(n,x):p=R/n;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
entries=[]
for i,d in enumerate(ds):
 h=d['original']['head'];raw=(O/d['path']).read_bytes();assert sha(raw)==h['sha256'];assert subprocess.check_output(['git','-C',str(W),'cat-file','blob',h['blob']])==raw
 dest=f'{hist}/originals/pr8177-{i+1:02d}-{Path(d["path"]).name}.gz';z=gzip.compress(raw,mtime=0);emit(dest,z)
 entries.append(dict(original_path=d['path'],original_mode=h['mode'],original_blob=h['blob'],original_sha256=h['sha256'],recovery=dict(path=dest,encoding='gzip',sha256=sha(z),decoded_sha256=sha(raw)),disposition='narrowed-live-with-complete-recovery' if d['path'] in [on,op] else 'historical-recovery-only',final_path=note if d['path']==on else run if d['path']==op else dest))
raw=(R/'drain8177-original/original.delta').read_bytes();z=gzip.compress(raw,mtime=0);dp=hist+'/pr8177-original-delta.patch.gz';emit(dp,z)
man=dict(schema_version=1,kind='exact-original-recovery-manifest',pr=8177,head=j['head'],delta_base=j['base'],entries=entries,original_delta=dict(path=dp,encoding='gzip',sha256=sha(z),decoded_sha256=sha(raw)))
emit(hist+'/pr8177-original-manifest.json',json.dumps(man,indent=2)+'\n')
history='''PR8177: readable historical science, limitations and deferred obligations

Formal negative certification is DEFERRED. These historical arguments and
solver reports are not live proof authority or an independent premise.
The manifest preserves every original mode/blob/raw hash, all50 payloads,
and the full original binary delta independently of branch retention.
Keep the original branch on partial closure for the unlanded obligations.

Corrections to the complete original proof below:
1. On the declared finite outside-zero domain, the tight-sibling statement
is equivalent to H by the full level induction, and H SUFFICES for an
unrooted unit-budget tree. No converse from the unrooted budget is asserted;
no finite cap is silently replaced by the all-Z3 forward automaton. The
single-seed saturated-support/local-marks characterization is conjectural.
2. The polynomial is a relaxed lifted-tree UPPER count, not an exact
one-processed-child count. At a D entry from a processed successor, that
incoming child already consumes the allowance. The polynomial permits one
additional processed successor. At unit weights its two remaining slots
have8 assignments versus4 legal ones. The kind-typed historical program
shares this omission; agreement between the two is not independent closure.
The complete injection and positive monotone-iteration argument are live.
3. Exact profiles: ZA[-1,-1,-1], ZB[-1,-1,0], ZB second tight site[-1,-1,-1].
The primary uses140 tiny realizations in B and120 equal minima/0 differences
from60 realizations and two costs in E; all-parent restriction there is exact.
4. The125-case historical MILP R1 constrains processed PARENTS only, not all
nodes. It uses floating solver results, not exact optimality certificates.
The W3 values-62/-61 are observed solver results under that weaker protocol,
not a proved all-parent exact minimum or a no-exchange theorem. Even exact
optimal-cost loss would only obstruct a cost-preserving exchange between
minimizers; a cost-increasing exchange retaining nonpositive cost, or direct
budget-feasible construction, remains open. Global nonbranching of optima
is unsupported. The claimed additional2887 comparison is historical only.
5. shape2 imports missing `shape`; its R12 parsing yields R1 and2, omittingR2.
overlap imports absent supervisor_control_block33_ssdp. Preserve those failures;
no active consumer is promoted. The structural search imports tight.py with
its top-level workload and uses floating MILP. It accepts6..110 live sites,
optimizes(number of all-tight processed sites, largest processed rooted value,
number of tight sites), uses single/double mark toggles or level-band copying
along sibling/predecessor offsets, accepts nondecreasing scores and occasional
worse moves, and stops by wall time. Recorded best triples are(0,0,1),
(0,0,2),(0,0,2),(0,0,1); no complete tested-realization counter is saved.
These are bounded observations, not exhaustive absence. The approximately
10000 all-site claim cannot be inferred from these logs. No new seed or count
is invented. Failed scaling/certificate attempts and raw errors remain exact.
6. The corrected main two-level theorem has explicit p>=q>0,r>0, conditional
independence, level order and all-a initial plane. Its global upper2 construction
does not prove global sharpness. The prior finite construction lower bound5/3
is narrower; no implication identifying the two constants is imported.
7. Six concerns in the original N1 list do not constitute five normalized
attacked negative families. No negative-packet PASS or audit is asserted.

The complete original note follows VERBATIM. Its incorrect scope/count/phase
rhetoric and historical author certification are superseded above and in the
canonical note. Every original argument remains readable, not replaced by a
summary; the original bytes are separately archived too.

================ COMPLETE ORIGINAL NOTE ================

'''
emit(defer,history+old)
emit(hist+'/README.md', '''# PR8177 exact recovery and deferred science

The [manifest](pr8177-original-manifest.json) binds all50 original modes,
Git blobs and raw SHA-256 hashes and the full binary delta. Decode each
`originals/pr8177-*.gz` with `gzip -dc`, restoring the listed original mode.
Recovery is independent of branch retention; partial closure must also keep
the branch for deferred scientific obligations.

The [readable history and full original proof](pr8177-deferred-science-and-history.txt)
records the weak-parent floating MILP scope, unresolved imports, failed
certificate scaling, bounded search protocol and incomplete negative packet.
Historical author PASS, campaign records and raw outcomes are not current
review or audit authority. No existing campaign/status/manifest is replaced.
The canonical note retains the full finite extension, seed and induction
proofs and adds the explicit relaxed-family injection argument.
''')
def part(a,b):return old.split(a,1)[1].split(b,1)[0]
lemmas='## Theorem T1 — finite extension, seed construction and sufficient induction\n\n'+part('## Theorem T1 — the lemmas and the reduction','## Theorem T2')
a=lemmas.index('Hence (H),');b=lemmas.index('> **Tight-sibling lemma',a)
lemmas=lemmas[:a]+'''For each fixed finite realization, the following statement implies H by induction from the lowest level (all live sites there are seeds). At an amplified site the predecessor is either a seed of value at most0 or satisfies H; the cases above cover every processed site except the stated residual. Conversely H directly implies the residual statement. Thus H is equivalent to that residual statement on this finite domain and is SUFFICIENT for the unrooted unit budget. No converse from the unrooted budget, no truncation equivalence and no all-Z3 extension is asserted.\n\n'''+lemmas[b:]
lemmas=lemmas.replace('Executed (B1–B3):','Historical original-source finite outcomes (B1–B3; fresh corrected evidence is separate):')
a=lemmas.index('*Remark (what the lemma is about).*');lemmas=lemmas[:a]+'''**Conjectural local characterization.** In a single-seed component the no-fork reduction permits optimization over predecessor-closed node sets. If an optimal set at a fixed cap omits an amplified site whose predecessor is included and whose level does not exceed that cap, adding the site and its arrow lowers cost by1. Thus saturation holds only for such admissible sites BELOW OR AT THE CAP. This observation does not prove the original formula reducing the residual to marks near z; sites at z's level, connectedness and competing optimal sets require control. The proposed local saturated-support characterization remains conjectural, and the tight-sibling residual remains a full-strength open obligation. The complete original proposal is readable in recovery.\n\n'''
t2='''## Theorem T2 — exact finite rooted profiles

For ZA the root(3,3,3) has value0 and its three processed predecessors have
values[-1,-1,-1]. For ZB the root(4,4,4) has value0 and predecessor values
[-1,-1,0]. Its second tight site(4,4,3) has three predecessors[-1,-1,-1].
These are exact capped single-seed calculations on the two declared fixtures.

**Proof by finite level transfer.** Restrict candidate nodes to levels at
most the queried root level; predecessor kinds are unchanged because every
predecessor is one level lower. In a one-seed component any family tree has
one descending arborescence and no forks: each downward chain terminates at
the unique seed, so adding a fork would create a cycle. Conversely a node
set containing the root and one live predecessor for each non-seed permits
one arrow per non-seed and yields that tree. The cost is the sum of+1 at
processed nodes,-1 at amplified nodes,0 at the seed. Transfer over subsets
of successive levels, requiring a predecessor for each chosen non-seed,
forcing the queried root and terminating at the singleton seed, therefore
enumerates exactly the finite rooted family. Exact rational minimization
gives the displayed values (C1,C2). They establish the profiles at these
sites only, not absence of tight-sibling sites in every realization. ∎

'''
fd=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='family_d');cert=next(n.value for n in fd.body if isinstance(n,ast.Assign) and n.targets[0].id=='certs')
t3='''## Theorem T3 — relaxed lifted-tree upper sum and eight certificates

**Successor-slot identity.** For n labelled successor positions, each empty,
processed(weight xP*U), or amplified(weight xA*U), assignments with at most
one processed occupant have sum
`U_n=(1+xA*U)^n+n*xP*U*(1+xA*U)^(n-1)`.
Proof: separate zero processed occupants from the choice of its unique slot;
all other slots are independently empty or amplified. This identity is exact
for THESE remaining slots, not a complete occupancy rule at a visited vertex.

**Relaxed family and injection.** Root a finite restricted lattice tree at
the queried site, label every edge by its displacement (three down, three up,
six sibling/fork labels), and label each arrow P or A by its originating
node kind. The unique root path to each vertex gives a word of these labels.
Reading the displacements recovers every original vertex and edge, so the
map from rooted labelled lattice trees to lifted word trees is injective and
weight preserving. The original tree has no cycle and distinct vertices;
forgetting geometric collisions and consistency between repeated projected
locations only ADDS possible lifted trees.

At the root, three successor slots remain, at most one of three predecessor
slots can be chosen, and six fork slots remain. On entering by a down edge
(D), the reverse successor slot is occupied, leaving two successors, at most
one of three predecessors, and six forks. Entering by an up edge(U) consumes
the vertex's sole downward arrow, leaving no predecessor slot, three
successors and six forks. Entering by a fork(F) leaves three successors,
at most one of three predecessors and five forks. A down choice has three
possible displacement labels and either arrow label, hence weight3*(xP+xA)*D;
optional forks have weight y*F. Impose at most one P on the REMAINING
successor slots by U_n, but deliberately do not debit an incoming P child
at a D entry. Any restricted lattice tree has at most one processed child
TOTAL, so its remaining successors satisfy this weaker rule. Every lifted
image therefore belongs to this relaxed family, proving the upper bound.
The relaxed family is strictly larger: if a D entry arrived from a processed
successor, the two remaining successor slots must have zero additional P
in a truly restricted tree (4 assignments at unit weights), while U_2 permits
8. This is overcount, not a defect in an upper bound. Node-kind consistency
is also relaxed; the historical kind-typed code shares the occupancy omission.

The resulting nonnegative polynomials are
`D=U_2*(1+3*(xP+xA)*D)*(1+y*F)^6`,
`U=U_3*(1+y*F)^6`,
`F=U_3*(1+3*(xP+xA)*D)*(1+y*F)^5`,
`R=U_3*(1+3*(xP+xA)*D)*(1+y*F)^6`.
Starting with(1,1,1), height truncations enumerate relaxed word trees of
bounded height. Coefficients and weights are nonnegative; monotonicity and
induction show that any triple at least1 dominating its right sides bounds
every truncation, hence the sum of all finite lifted trees. This bounds the
restricted lattice-tree weight sum by the injection. Replacing U_n by
`(1+(xP+xA)*U)^n` drops even the remaining-slot constraint and gives the
full relaxed slot count of the linked two-level theorem. It is termwise
larger, as the elementary slot expansion shows.

**Weights and exact certificates.** For supplied p,q,r>0 set
`d1=1-p^3/(p^3+q^3+4*r^3)`,
`d2=1-p^2*q/(p*q*(p+q)+4*r^3)`,
`d3=1-p^2*r/(r*(p^2+q^2)+r^2*(p+q)+2*r^3)`;
`epsilon1=d1`, `epsilon2=max(d2,d3)`, `xP=t`, `xA=epsilon2/t^c`,
`y=epsilon1/t^3`. The six signed-axis product weights in the linked
product-law parent give these rational formulas by summing six products;
for the present polynomial theorem they are explicit supplied definitions.
Each key below is(c,p,q,r), each value(t,Dbar,Ubar,Fbar):

```python
'''+ast.get_source_segment(src,cert)+'''
```

Fraction(n,d) means n/d. Substitute each row into the displayed polynomials
and clear positive denominators. All entries are at least1, each dominates
its right side, and epsilon1*Rbar<1/100000. This proves eight POINT
certificates for the relaxed upper sum. D2 retains exact arithmetic.
The additional full-factor tuple at(4165,1,2), c=2 is
t=99/1000, Dbar=56694252249173/500000000000,
Ubar=3279872914431/1000000000000,
Fbar=168429466648591/1000000000000; direct substitution dominates both
polynomial systems (D3). No interval or improved formation law is inferred.

**Missing application premise.** To turn this count into a probability
bound one still needs a restricted admissible tree within the chosen budget
at every dissent realization, the supplied stochastic domination and
independent seed/amplification events. If these are supplied, F=|S|-1 and
E<=3F+cA imply, for0<t<=1,
`epsilon1^|S|*epsilon2^A <= epsilon1*t^E*(epsilon2/t^c)^A*(epsilon1/t^3)^F`.
The injection bounds the right-hand tree sum. Restricted admissibility is
not proved by eight numerical points or a finite tiny-fixture sample.
Thus no improved ordered region is claimed here. ∎

'''
t4='''## Theorem T4 — exact finite restriction comparisons

The fixed primary sample has60 tiny realizations and costs c=1,2. All120
computed restricted and unrestricted minima agree, with zero differences;
a tree satisfying the budget exists in all120 cases. The restriction is
at most one processed child at EVERY parent, including seeds/amplified
parents. This is a finite sample, not a universal admissibility theorem.

**Finite verification.** Enumerate node subsets containing the root, one
live predecessor choice for each non-seed, and the resulting arrow forest.
For the restricted family count processed children at every parent and
reject a choice with two. Forks can join the arrow components into a tree
exactly when the component adjacency graph is connected; choose any spanning
tree of that graph. Each choice has F=S-1 and cost E-3(S-1)-cA. Minimize
these exact rational costs. The queried root is a maximal-level live site,
so the rooted level cap removes no candidate in this comparison. This is
precisely the finite enumeration in E1, with original fixtures unchanged.
The historical125-case floating MILP and W3 observation use a weaker
restriction and are not promoted as exact certificates; their full scope,
errors and original sources remain readable in recovery. ∎

'''
fences=('This note proves finite rooted extension and seed lemmas, a sufficient induction conditional on an open tight-sibling statement, and a relaxed lifted-tree upper sum with eight rational point certificates.','The unrooted unit-budget converse and the local saturated-support characterization are not established; restricted admissibility and improved formation regions remain open.','Finite samples and historical floating solver observations do not complete formal negative certification; all original arguments and failures remain recoverable.')
header=f'''---
claim_id: {cid}
claim_type: bounded_theorem
claim_scope: "Finite rooted extension/seed constructions and exhaustive conditional induction; exact finite predecessor profiles; relaxed lifted-tree upper-bound injection and eight point certificates;120 finite exact all-parent comparisons. No universal budget converse, local characterization, improved formation region or completed negative certificate."
upstream_dependencies:
  - minimal_axioms
  - {Path(product).stem.lower()}
  - {Path(parent).stem.lower()}
runner: {run}
---

# Rooted marked-tree lemmas and relaxed lifted-tree certificates

**Type:** bounded_theorem
**Status:** proposed_retained; unaudited conditional finite mathematics.
**Primary:** [exact finite checks](../{run}).
**Cache:** [exact-source evidence](../logs/runner-cache/{Path(run).stem}.txt).
**Recovery:** [complete original history and deferred science](work_history/review_loop/pr8177/README.md).

## Result up front

The full extension, seed and induction proofs below establish a sufficient
route from the open tight-sibling statement to the unit budget on explicitly
finite realizations. The original polynomial is retained as a RELAXED upper
sum with a complete injection proof, not an exact occupancy count. Its eight
rational certificates remain unchanged. Exact profiles distinguish ZA from
ZB; the fixed sample is140 realizations for the rooted lemmas and120 equal
minima from60 realizations/two costs for the all-parent restriction.
No corrected-source primary, mutation or historical solver was run during
author preparation. Earlier evidence remains historical, not fresh capture.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite rooted induction and restricted admissible-tree existence"
source_of_blocker_text: review_loop
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "original same-session affected confirmation and bounded exact-source capture"
conditional_surface_status: "finite outside-zero window; open tight-sibling residual and restricted admissibility"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies framework vocabulary.
The [product-rule parent]({Path(product).name}) supplies the six-axis
product conditional used to interpret the displayed weights. The
[two-level domination and explanation-tree theorem]({Path(parent).name})
supplies the full-slot comparison and conditional application framework.
Its hypotheses are p>=q>0,r>0, the six signed-axis menu, records-only level
order, independent site draws conditional on the previous level and an
initial all-a plane. Its finite-cone localization and infinite-plane formation
conclusion do not automatically apply to a new restricted family. That family
needs the separate admissible-tree existence premise stated below. No source
from an unlanded sibling is imported as a theorem; all finite data are explicit.
The landed finite construction lower bound5/3 does not establish global
sharpness2; the parent upper2 theorem retains its own supplied scope.

- **Finite domain.** Fix a finite box B in Z3, with sites outside B fixed to0.
Process its sites in increasing `tau(z)=z1+z2+z3`: a site is1 if at least two
of its predecessors z-ej are1, or if it is marked. This is the supplied
finite model; no full forward all-Z3 interpretation is asserted. A live
site is a seed/amplified/processed according to0/1/at least2 live predecessors.
- **Graph and family.** Arrows join live predecessors; forks join live siblings
z and z±(ei-ej). A family tree contains the queried live root; every non-seed
has exactly one downward arrow to a live predecessor, a seed none. Remaining
edges are forks. E counts processed arrows,A amplified nodes,S seeds,F forks.
Descending arrow chains end at seeds; their components are arborescences.
Contracting them in a tree gives F=|S|-1. Cost is E-3(|S|-1)-A.
- **Rooted value.** v(z) is the minimum cost over trees whose nodes have level
at most tau(z). A downward path always supplies a finite tree, so this
minimum is attained. For a seed, its singleton gives v<=0. A processed site
is tight if v=0. H means v<=0 for processed sites and v<=-1 for amplified
sites. H implies a unit-budget tree by forgetting the cap; no converse used.
- **Restriction.** A child of u is a site whose arrow points to u. At most
one processed child is allowed at EVERY node. The lifted relaxation below
forgets incoming occupancy, not the original meaning of this restriction.
- **Fixtures.** ZA(box4x4x7,root3,3,3,20marks), ZB(box5x5x8,root4,4,4,36marks)
and the retained W1/W2/W3 coordinates are exactly listed in the primary.
They are supplied finite data; historical sources/searches are archived.

'''
footer='''## No-Go Discipline Gate — deferred applicability

N1: finite extension/seed constructions, induction case coverage and explicit
slot enumeration are actual controls of positive statements; the original
six concerns are not five normalized attacks on one negative target. No
quota PASS is asserted. N2: no repository wall is imported. N3: finite cap,
model assumptions, incoming occupancy and all-parent distinction are explicit.
N4: current mathematical source roles are above; historical floating MILP and
unresolved imports are recovery, not theorem authority. N5: finite rooted
instances, rational points and exact small enumeration are executed only by
future bounded capture; no spectral modes or infinite lattice are executed.
N6: preserve the branch and all deferred original science. N7: a cost-increasing
exchange retaining the budget, or direct construction, remains possible;
solver optimum differences do not exclude these. N8: finite absence and
historical search maxima are not a universal characterization or threshold.

## Boundaries and non-claims

'''+ '\n\n'.join(fences)+f'''

## Imports

Finite graph trees, level induction, finite rational minimization and
nonnegative monotone polynomial iteration are the mathematical tools.
Complete proofs appear above. The linked conditional process theorem is
used only for its explicit comparison/application framework. Its hypotheses
are not consequences of registered primitives, and this note supplies no
new probability or physical identification premise. Historical negative
arguments remain readable with formal certification deferred.

## Verification

The stdout-only primary retains18 completed checks: A4+B3+C2+D3+E1+F4+G1.
C1 now binds both exact sorted predecessor profiles and E1 binds120 equal
minima/zero differences; the unchanged140-realization B sample remains.
The new `predecessor_profile_wrong` target tests the corrected ZB profile.
No mathematical outcome is asserted from the packaging checks alone.

```bash
python3 {run}
python3 {run} --list-mutations
```
'''
new=header+lemmas+t2+t3+t4+footer;emit(note,new)
s=src;a=s.index('"""');b=s.index('"""',a+3)+3;s=s[:a]+'''"""Finite rooted extension/seed instances, exact predecessor profiles and
relaxed lifted-tree polynomial certificates. The open induction residual
suffices for a finite unit budget; no converse or physical improvement is
proved. The count deliberately relaxes entering processed-child occupancy
and geometric collisions. Original finite fixtures and arithmetic retained.
Stdout only; historical solvers and searches are not executed.
"""'''+s[b:]
s=s.replace('import random','import hashlib\nimport random',1).replace(on,note).replace(Path(on).stem.lower(),cid).replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 120')
s=s.replace('    "tightness_wrong": "C",','    "tightness_wrong": "C",\n    "predecessor_profile_wrong": "C",')
s=s.replace('and min(pv) == -1','and sorted(pv) == ([-1, -1, -1] if name == "Z_A" or mut("predecessor_profile_wrong") else [-1, -1, 0])')
s=s.replace('and all three of its 1-predecessors are processed with rooted value -1: the root is not a tight-sibling case','with exact processed-predecessor profiles ZA[-1,-1,-1], ZB[-1,-1,0]: neither tested root is a tight-sibling case')
s=s.replace('but never all of them','in these tested profiles not all predecessors are tight; no universal absence asserted')
s=s.replace('checks.check("E1", ok and fits >= 60,','checks.check("E1", ok and fits == 120 and same == 120 and differ == 0,')
s=s.replace('the up-factor of the restricted count','the remaining-slot up-factor of the relaxed upper count').replace('of the restricted recursion','of the relaxed upper recursion').replace('the restricted count is termwise smaller','the relaxed remaining-slot upper sum is termwise smaller')
s=s.replace("block 25/30's recursion and block 30's certificate",'the linked full-slot polynomial and its certificate')
s=s.replace('note, axioms, block01 = texts','note, axioms, block01 = texts[:3]')
inputs=[note,'docs/MINIMAL_AXIOMS_2026-06-29.md',product,parent];pins={p:sha((W/p).read_bytes()) for p in inputs}
s=s.replace('    "'+product+'",\n)', '    "'+product+'",\n    "'+parent+'",\n)')
s=s.replace('ROOT = Path(__file__).resolve().parents[1]','INPUT_SHA256 = '+repr(pins)+'\nROOT = Path(__file__).resolve().parents[1]')
s=s.replace('all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS)','all(Path(ROOT,p).is_file() and hashlib.sha256(Path(ROOT,p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS)').replace('"all declared inputs exist"','"all four proof/model source inputs match literal SHA-256 pins"')
s=s.replace("block 01's note (on main)",'the linked product-law parent')
a=s.index('FENCES = (');b=s.index('FORBIDDEN = (',a);s=s[:a]+'FENCES = '+repr(fences)+'\n'+s[b:]
n5=('per_element: executed — extension and seed instances on140 tiny realizations by exact rooted enumeration and remaining-slot identity; universal statements use written proofs','per_site: executed — the fixed tiny sample and exact capped profiles ZA[-1,-1,-1], ZB[-1,-1,0], second tight site[-1,-1,-1]; no global absence claim','per_mode: checked and not executed — no spectral decomposition is present; finite parameter cases and rooted subsets are not spectral modes','per_block: executed — eight rational relaxed-upper-sum certificates, one full-slot comparison and120 equal minima/zero differences on60 fixed sampled realizations','lattice_wide: checked and not executed — no infinite simulation or universal restricted-admissibility test; finite-domain lemmas and relaxed injection have written proofs')
a=s.index('N5_LINES = (');b=s.index('\n\n\ndef family_g',a);s=s[:a]+'N5_LINES = '+repr(n5)+s[b:]
compile(s,run,'exec');emit(run,s)
# AST calculations and fixtures: compare independently of text transformation.
class Norm(ast.NodeTransformer):
 def visit_Constant(self,n):return ast.copy_location(ast.Constant('<text>'),n) if isinstance(n.value,str) else n
nt=ast.parse(s);same={}
for f in tree.body:
 if isinstance(f,(ast.FunctionDef,ast.ClassDef)) and f.name not in ['family_a','family_c','family_e','family_f','family_g']:
  nf=next(n for n in nt.body if type(n)==type(f) and n.name==f.name);same[f.name]=ast.dump(Norm().visit(f))==ast.dump(Norm().visit(nf));assert same[f.name],f.name
for key in ['Z_A','Z_B','W1','W2','W3']:
 val=lambda t:next(n.value for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id==key)
 assert ast.dump(val(tree))==ast.dump(val(nt))
paths=subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines();assert len(paths)==56,len(paths)
existing={Path(p).name for p in subprocess.check_output(['git','-C',str(W),'ls-files','docs'],text=True).splitlines()};names=[Path(p).name for p in paths if p.startswith('docs/') and Path(p).name not in ['README.md','SKILL.md']];assert not set(names)&existing and len(names)==len(set(names))
rows=[dict(path=p,mode='100644',sha256=sha((W/p).read_bytes())) for p in paths];snap=R/'drain8177-prepared-source-v1';assert not snap.exists()
for p in paths:(snap/p).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/p,snap/p)
prep=dict(schema_version=1,kind='author-preparation-not-review-verdict',pr=8177,owner='PR8177-author',base=BASE,head=j['head'],source_count=56,source=rows,original_count=50,canonical_notes=[note],primaries=[run],deferred_science=[defer],snapshot=str(snap),original_manifest=dict(path=hist+'/pr8177-original-manifest.json',sha256=sha((W/hist/'pr8177-original-manifest.json').read_bytes())),mathematical_function_ast_comparison=same,fixtures_unchanged=True,explicit_changes=['C1 exact ZA/ZB profile with targeted mutation','E1 exact120 equal minima0differences','source pins and reporting;120second cap'],primary_runs=0,mutation_runs=0,simulation_runs=0,staged=False,branch_preservation_required=True,document_basename_collisions=[])
dump('drain8177-author-prepared-v1.json',prep);dump('drain8177-source-freeze-v1.json',dict(schema_version=1,source=rows,base=BASE,snapshot=str(snap),prepared_sha256=sha((R/'drain8177-author-prepared-v1.json').read_bytes())))
claims=[dict(original='T1 extension/seed/exhaustive induction',destination=note,disposition='complete proofs retained; finite domain and H sufficient for unit budget, no converse; local characterization explicitly conjectural'),dict(original='T2 profiles',destination=note,disposition='ZA/ZB/second-site exact distinctions bound; no global absence'),dict(original='T3 count/eight certificates',destination=note,disposition='all exact polynomials/certificate literals retained; complete injective upper-bound proof replaces incorrect exact counting'),dict(original='T4 finite comparisons',destination=note,disposition='exact all-parent60realizations/120equal minima retained'),dict(original='negative/nonbranching/exchange/locality claims and historical controls',destination=defer,disposition='full original note readable plus scope corrections; all50originals exact; failures/missing imports/weak-parent solver/search limitations explicit; branch retained')]
dump('drain8177-author-dispositions-v1.json',dict(schema_version=1,constituents=[dict(pr=8177,head=j['head'],delta_base=j['base'],dispositions=entries)],claims=claims,original_delta=man['original_delta']))
(R/'drain8177-author-corrections-v1.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=on,tofile=note))+''.join(difflib.unified_diff(src.splitlines(True),s.splitlines(True),fromfile=op,tofile=run)))
print(json.dumps(dict(source_count=56,prepared_sha256=sha((R/'drain8177-author-prepared-v1.json').read_bytes()))))
