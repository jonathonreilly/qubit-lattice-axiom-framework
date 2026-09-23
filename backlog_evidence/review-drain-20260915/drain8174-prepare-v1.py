from pathlib import Path
import ast,difflib,gzip,hashlib,json,os,re,shutil,stat,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';O=R/'drain8174-original';H=O/'head'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert json.loads((R/'author-draft-slot.json').read_text())['owner']=='PR8174-author'
assert git('rev-parse','HEAD')=='6332b12b59c83c5b08cc7b4ad90898cb6666050d'
assert not git('status','--porcelain','--untracked-files=all')
inv=json.loads((O/'inventory.json').read_text()); assert len(inv['paths'])==25
oldnote=next(p for p in H.glob('docs/*.md'));oldrun=next((H/'scripts').glob('*.py'))
note='docs/SIX_AXIS_TWO_LEVEL_DOMINATION_EXTENDED_EXPLANATION_TREE_AND_FOUR_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md'
runner='scripts/six_axis_two_level_domination_extended_explanation_tree_four_rational_certificates_2026_09_16.py'
cid=Path(note).stem.lower();archive=Path('docs/work_history/repo/review_feedback/pr8174-evidence')
parent='docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md'
inputs=[note,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md',parent]
created=[]
def put(p,data,mode=0o644):
 q=W/p;assert not q.exists();q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data if isinstance(data,bytes) else data.encode());q.chmod(mode);created.append(str(p));return q
def out(name,data):
 p=R/name;assert not p.exists();p.write_text(json.dumps(data,indent=2)+'\n');return p
entries=[]
for e in inv['paths']:
 p=e['path'];raw=(H/p).read_bytes();assert hashlib.sha256(raw).hexdigest()==e['head_sha256']
 mode,kind,blob=e['head'].split('\t')[0].split();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==blob
 # Plain readable proof/code; compress text outputs and generated data without trimming any byte.
 plain=Path(p).suffix in ('.md','.py'); enc='identity' if plain else 'gzip'
 name=Path(p).stem[:100]+'-'+e['head_sha256'][:16]+Path(p).suffix+('' if plain else '.gz')
 stored=archive/'kept'/name;q=put(stored,raw if plain else gzip.compress(raw,mtime=0),int(mode,8)&0o777 if plain else 0o644)
 entries.append(dict(original_path=p,original_mode=mode,git_blob=blob,raw_sha256=e['head_sha256'],stored_path='kept/'+name,stored_sha256=sha(q),encoding=enc,bytes=len(raw)))
put(archive/'original-delta.patch.gz',gzip.compress((O/'original.patch').read_bytes(),mtime=0))
put(archive/'archive-manifest.json',json.dumps(dict(schema_version=1,original_head=inv['head'],original_base=inv['base'],entries=entries,delta=dict(path='original-delta.patch.gz',raw_sha256=sha(O/'original.patch'),stored_sha256=sha(W/archive/'original-delta.patch.gz'))),indent=2)+'\n')
orig=oldnote.read_text()
def section(a,b):return orig[orig.index(a):orig.index(b)]
objects=section('Declared objects.','## Prior art and what is new')
objects=objects.replace('As in block 25 (PR #8168), restated:', 'Supplied model:').replace('As in block 25:', 'Definitions:').replace("(block 25's count, restated in T3)", '(restated in the count theorem below)')
objects=objects.replace('positive orbit weights', 'orbit weights p >= q > 0, r > 0')
t2=section('## Theorem T2', '\nExecuted (C2–C4):')
t2=t2.replace("The construction is block 25's with three changes:", 'The extended construction has three features:').replace("(block 25's T2(b))", '(because the coordinate maxima on a sibling pair sum to one)')
start=t2.index('*(T2.3, the spanning lemma.)*');end=t2.index('*(T2.4, refinement and accounting.)*')
span=(W/parent).read_text().split('## Theorem T3 — the spanning lemma\n',1)[1].split('## Theorem T4',1)[0]
span=span.replace(' ∎ (Asserted at every refinement executed: D1–D3.)',' ∎')
t2=t2[:start]+'*(T2.3, the spanning lemma and complete pole transport.)*\n\n'+span+'\n'+t2[end:]
t2=t2.replace('as in block 25 —', 'under the following invariant —')
local='''**Finite localization before refinement.** Fix a site x at level n > 0. Its ancestor cone down to level zero consists of the finitely many x − a with a in the nonnegative integer triples and sum(a) <= n. Every positive-level site's three predecessors belong to the cone. Set sites outside it to zero for this construction and keep the prescribed zero level; induction in level shows that all values in this cone equal the values of the infinite process. Apply the cluster construction to this finite directed graph. Restricting a cluster in this way changes no predecessor of any included positive-level point, hence no winning pair, seed or amplified classification used by the construction. All paths and shortest paths below are now finite. The resulting finite explanation tree embeds in the original infinite graph. This supplies the infinite-process use without assuming finite global clusters.\n\n'''
t2=t2.replace('**Proof.** ',local+'**Proof.** ',1)
t3=section('## Theorem T3 — the count', '## Theorem T4')
t3=t3.replace("(block 25's lift: the words of edge types along root paths, injective, with at most one *down* child per vertex and none after an *up* letter)", '(the words of edge types along root paths, injective, with at most one *down* child per vertex and none after an *up* letter)')
t3=t3.replace(' ∎ (D1: the lift\'s slot structure re-executed on the enumerated subtrees with `≤ 4` edges as in block 25; D2: the certificates.)',' ∎')
t3+='''**The complete slot count.** Give each edge its displacement label: three down, three up, six fork labels. A rooted lattice tree has a unique root path to each vertex; reading its labels gives a word, and projecting that word's displacements recovers the lattice vertex and all edges. Thus distinct rooted trees have distinct lifts. After a down step, the reverse up slot is occupied, leaving two up slots, at most one of three down slots, and six fork slots; its contribution is D. After an up step, the reverse down arrow is occupied, so there are no further down slots, three up slots and six fork slots; its contribution is U. After a fork step, five fork slots remain with three up slots and at most one of three down slots; this is F. The root has all six fork slots and the root expression R. Independent optional up/fork slots give factors (1+xU) and (1+yF); the choice of zero or one of three down slots gives (1+3xD). These are precisely the four displayed recursions. Forgetting geometric collisions only adds lifted subtrees, so this count is an upper bound. Height truncations increase from (1,1,1); a finite super-solution bounds every truncation and therefore their nonnegative weight sum.\n\n'''
t1='''## Theorem T1 — two-level domination on the stated weight domain

**Statement.** For p >= q > 0 and r > 0 the deviations below satisfy d1 <= d2 <= max(d2,d3). Each di is strictly decreasing in p for all p,q,r > 0. Under the supplied conditionally independent level product law, the dissent indicator from the all-a plane is coupled below the two-level automaton.

**Proof of formulas and monotonicity.** Sum the six product weights for triples (a,a,a), (a,a,−a), (a,a,b), b perpendicular to a. Their aligned probabilities are respectively p³/(p³+q³+4r³), p²q/(pq(p+q)+4r³), and p²/(p²+q²+r(p+q)+2r²). Therefore

```
d1 = 1 − p³/(p³+q³+4r³),
d2 = 1 − p²q/(pq(p+q)+4r³),
d3 = 1 − p²/(p²+q²+r(p+q)+2r²).
∂p d1 = −3p²(q³+4r³)/(p³+q³+4r³)²,
∂p d2 = −(q³p²+8qr³p)/(pq(p+q)+4r³)²,
∂p d3 = −p(rp+2q²+2rq+4r²)/(p²+q²+r(p+q)+2r²)².
```

Every derivative is strictly negative. Put A=p³+q³+4r³ and B=pq(p+q)+4r³. Direct subtraction gives

```
d2 − d1 = p²(p−q)[q²(p+q)+4r³]/(A B) >= 0.
```

Here p >= q is essential: at (p,q,r)=(1/10,1,1), d1=5000/5001 while d2=d3=410/411. This exact example explains the scope correction; it does not invalidate the four large-p certificates.

**Proof of the coupling.** Build both processes level by level with independent uniforms at different sites. If at least two comparison predecessors dissent, set the comparison value to one and it dominates. If exactly one comparison predecessor dissents, at most one actual predecessor differs from a. The actual dissent probability is one of d1,d2,d3, hence at most epsilon2=max(d2,d3) by the factorization. If no comparison predecessor dissents, all actual predecessors equal a and dissent has probability epsilon1=d1. Draw actual dissent as 1{U<d} and comparison dissent as 1{U<epsilon_i}. Conditional on actual dissent, use an additional independent draw for the five non-a possibilities to recover the entire six-state product kernel. This constructs the correct conditionally independent laws and preserves domination by induction. Finite ancestor cones make the induction local at every infinite-plane site. ∎

'''
t4='''## Theorem T4 — four rational certificates and six invariant laws

**Statement.** Under the supplied process and weight hypotheses, from the all-a plane, P(v_x != a) < 10^−7 at every later site on each ray: p >= 4165 at (p,1,2); p >= 2085 at (p,1,1); p >= 8330 at (p,2,4); p >= 6247 at (p,1,3). The level process has at least six pairwise distinct translation-invariant invariant laws. The inequalities hold for real p on these rays, in particular for integers.

**Exact certificates.** With x=t+epsilon2/t² and y=epsilon1/t³, the following positive rational triples dominate the three recursion right sides, entry by entry:

| (p,q,r) | t | Dbar | Ubar | Fbar |
|---|---|---|---|---|
| (4165,1,2) | 99/1000 | 56694252249173/500000000000 | 3279872914431/1000000000000 | 168429466648591/1000000000000 |
| (2085,1,1) | 49/500 | 88632394933177/1000000000000 | 3254100818939/1000000000000 | 131311435970231/1000000000000 |
| (8330,2,4) | 99/1000 | 56694252249173/500000000000 | 3279872914431/1000000000000 | 168429466648591/1000000000000 |
| (6247,1,3) | 99/1000 | 24445325573453/250000000000 | 3264868815393/1000000000000 | 9064364177089/62500000000 |

For each row define Rbar=(1+x Ubar)³(1+3x Dbar)(1+y Fbar)⁶. Substitution in exact rational arithmetic gives epsilon1 Rbar < 1/10^7. Approximate values, for readability only, are respectively 7.6934551567, 7.2441560890, 7.6934551567 and 6.4848260436 times 10^−8; the strict rational inequalities are the certificates. All entries are at least one. Since the deviations decrease with p, the same t and triple remain super-solutions along the entire larger-p ray. T1 and T3 therefore prove the stated uniform probability bound.

**Invariant-law construction.** The finite-menu configuration space M^{Z²} is compact metrizable. The level kernel P is Feller: a cylinder's next-step law depends continuously on finitely many old coordinates, and cylinder functions uniformly approximate continuous functions. It commutes with plane translations. If lambda_t is the level-t law from the all-a plane, the Cesaro average lambda^(T)=T^−1 sum_{t=1}^T lambda_t has a weakly convergent subsequence by compactness. For every continuous f,

```
|lambda^(T)(Pf) − lambda^(T)(f)|
 = |lambda_(T+1)(f) − lambda_1(f)|/T <= 2||f||/T.
```

Feller continuity passes this identity to the limit mu_a, making it invariant. Translation invariance also passes to the limit. The single-site dissent indicator is continuous, so mu_a(v_y != a) <= 10^−7. For b != a, mu_a(v_y=a) >= 1−10^−7 > 10^−7 >= mu_b(v_y=a); the six laws are distinct. If one also imports barycentric decomposition of stationary laws for this compact Feller process, at least six extreme stationary laws exist: if there were at most five, each mu_a would be a mixture of these finitely many laws, so some extreme law would give v_y=a probability greater than 1/2; the same extreme law cannot do this for two distinct a. The six directly constructed laws need no extremal-decomposition import. ∎

The earlier single-noise sufficient thresholds are 285718, 142861, 571436 and 428576 on the corresponding rays. Their ratios to the four displayed integers are at least 68 and approximately 69, not at least 69. These compare sufficient certificates, not physical thresholds or optimal integers for this method.

'''
t5='''## Theorem T5 — positive fixed-point parametrization

For 1 <= v < 3/2 put x=(v−1)/v³ and y=0. Then U=v³, D=v²/(1−3xv²), F=v³(1+3xD) give a finite nonnegative fixed point of all three recursions. The denominator equals (3−2v)/v and is positive. Direct substitution proves the claim; all three entries are at least one and bound the iteration from (1,1,1). The map x(v) has derivative (3−2v)/v⁴ and increases from 0 to 4/27 on this half-open interval. Also t²(4/27−t) has derivative t(8/27−3t), and its maximum on [0,4/27] is 256/531441 at t=8/81.

The complete corrected full-domain, strict-endpoint and necessary-route-bound argument is preserved readably in the deferred-science recovery. That scoped mathematical proof remains valid; its formal negative-certification promotion and the broader route-exhaustion conclusions are deferred. It is not a premise of the positive certificate theorem.

'''
head=f'''---
claim_id: {cid}
claim_type: bounded_theorem
claim_scope: "For a supplied six-axis product kernel with p >= q > 0, r > 0, records-only level order, independent conditional site draws and an all-a initial plane: the two-level dissent coupling, complete extended explanation-tree construction with forks=|S|-1 and E<=3(|S|-1)+2|A|, lifted recursion bound, and four exact rational sufficient certificates imply sitewise dissent below 10^-7 and six distinct invariant laws on the stated large-p rays. Positive fixed-point parametrization is also given. No actual threshold, optimal integer, exhaustive route exclusion, physical selection or deferred-science premise is claimed."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - {Path(parent).stem.lower()}
runner: {runner}
---

# Six-axis two-level domination, extended explanation trees and four rational certificates

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit authority:** independent audit lane only.
**Primary runner:** [{Path(runner).name}](../{runner})
**Planned cache:** [{Path(runner).stem}.txt](../logs/runner-cache/{Path(runner).stem}.txt)

## Result up front

Separating rare seed dissent from amplification of existing dissent gives four exact sufficient bounds. The complete coupling and tree argument follows below, with its supplied hypotheses. The four rational certificates improve the earlier sufficient integers by at least 68 (approximately 69). They do not locate an actual transition. Fresh corrected-source execution is pending; the source defines 17 checks and 11 mathematical mutations. Historical outputs remain exact recovery, not a fresh result.

## Machine status and trace

```yaml
actual_current_surface_status: proposed_retained
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Sufficient stability bounds for a supplied level product process"
source_of_blocker_text: source_note
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independent affected-source review and bounded evidence capture; sharper counting remains research"
conditional_surface_status: "p >= q > 0, r > 0; supplied six-axis menu, records-only level order, independent conditional updates and all-a initial plane"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the lattice, one-site possibility, admissibility and fixed-record vocabulary. The [product-rule parent]({Path(inputs[2]).name}) defines the six-axis orbit weights and the records-only product conditional. The [single-noise formation theorem]({Path(parent).name}) supplies the earlier sufficient-certificate comparison and the pole-transport construction reproduced completely below. These are conditional source results, not physical rule selection. The registered primitives supply units, graining and pointwise realized-state evaluation at their own scope; no choice of these weights, menu, initial state or process is attributed to them.

All product weights and all updates here are supplied mathematical hypotheses: p >= q > 0, r > 0; records form in level order, with independent draws at distinct sites conditional on the previous level; the initial plane is all a. Weak compactness on a finite-alphabet product space and, only for the optional extreme-law conclusion, stationary barycentric decomposition are standard mathematical imports.

'''
end=f'''## No-Go Discipline Gate

### N1 — Actual route record and deferred promotion
The historical list mixed tests of one construction with proposed alternatives. It does not establish five normalized attempted negative families. No formal negative packet PASS or exhaustive route closure is asserted. The exact original list, complete corrected route-bound proof and untested sharper constructions are retained in [historical recovery](work_history/repo/review_feedback/pr8174-evidence/README.md). The positive theorem does not use deferred conclusions.

### N2 — Relation of open obligations
Sharper bad-pair accounting and an overlap-controlled tree-of-trees count are open research obligations. Their independence is not established and no numerical wall count is claimed.

### N3 — Explicit hypotheses
The menu, p >= q > 0, r > 0, records-only product update, level order, conditional independence and constant plane are supplied. Compactness and optional extremal decomposition are mathematical imports, not hidden physical premises.

### N4 — Source roles
The axiom memo supplies framework vocabulary, the product-rule parent the conditional model, and the single-noise parent the earlier certificate comparison and reproduced transport construction. Historical simulations and floating scans are not threshold or negative-certificate authorities.

### N5 — Resolution
The primary defines finite exact formula checks, all 216 triples at five declared weight triples, exhaustive small cones, 1200 seeded random cones, 66103 finite lifted-tree candidates and four rational certificates. The original primary output reports 932+2321+843=4096 explained configurations; the distinct 1500-random-cone historical construction control reports 4290. These are separate historical protocols. Corrected-source outcomes remain pending. Infinite-plane statements use the written localization, probability and compactness proofs, not an executed infinite lattice.

### N6 — Partial paths
Treating amplified nodes as leaves loses the two-level improvement; it does not make the ordered region empty, since epsilon2 tends to zero along fixed-q,r large-p rays. No new primitive is requested. Other counting and coupling arguments remain open.

### N7 — Strongest unresolved alternative
An overlap-controlled cluster or tree-of-trees argument, or a sharper bad-pair potential, might improve the sufficient region. The historical packet supplies neither an explicit overlap/cycle witness closing all constructions nor a proof of the sharper budget. Their estimates remain proposals.

### N8 — Historical comparison
The prior single-noise construction is a positive sufficient result. The archived finite simulations and floating scans cannot establish a true infinite-volume threshold or exhaustive optimality. The branch retains recovery value for those deferred proposals.

## Boundaries and imports

The result is conditional on the stated model and initial plane. No physical rule, formation schedule, coupling value or readout bridge is selected. No actual threshold or optimal integer is claimed. The two-level tree proof and rational certificates stand independently of the deferred negative packet. Standard compactness and optional stationary-law decomposition have precisely the roles stated in T4. No fitted or observed value is an input.

## Review and verification record

Original source findings corrected the weight domain and strict endpoint, supplied complete localization and pole transport, separated finite controls from universal proofs, repaired input/graph links, and quarantined unsupported threshold and no-go claims. All original source and raw evidence is recovered exactly in the [archive](work_history/repo/review_feedback/pr8174-evidence/README.md); historical author PASS wording is not present-day review authority.

The paired runner preserves the original construction, cone fixtures, random seed, lifted enumeration and four rational certificates. It strengthens derivative and domain controls and writes input/source-bound JSON under logs/runner-cache. Eleven mathematical mutations are declared, with no successful outcomes claimed before execution. Two original prose-only mutations remain recoverable in the historical runner. Expected baseline contract: `TOTAL: PASS=17 FAIL=0`, subject to actual future execution. Neither primary nor mutation execution occurred during preparation.
'''
body=head+objects+t1+t2+'\n'+t3+t4+t5+end
put(note,body)
# Complete readable negative proof, scoped and quarantined; do not erase its mathematics.
deferred='''# Deferred science and corrected route-bound proof

This is readable recovery, not a live claim or dependency authority. The corrected scoped mathematical argument below is valid; its formal negative-certification promotion remains deferred because the historical packet does not establish five distinct attempted negative-route families. That procedural limitation does not refute the mathematics. Broader optimal-threshold, exhaustive-route and simulation conclusions are unproved. Preserve the original branch as their recovery handle.

## Complete corrected full-domain and route-bound argument (historical T5)

Let the domain consist of nonnegative (x,y) at which iteration of the three recursions from (1,1,1) stays bounded. At y=0 a finite U fixed point has U=v³ and x=(v−1)/v³, v>=1. Its derivative is (3−2v)/v⁴; the maximum is 4/27 at v=3/2. For 0<=x<4/27 choose the least root 1<=v<3/2. Then 1−3xv²=(3−2v)/v>0, D=v²/(1−3xv²), and F=v³(1+3xD) form a finite fixed point bounding all iterates. At x=4/27 the least scalar root is v=3/2, but the D equation becomes D=9/4+D, impossible for finite D. For x>4/27 no finite scalar U fixed point exists. Monotonicity of the polynomial iteration means a bounded iteration would have a finite fixed-point limit. Thus the full domain at y=0 is exactly 0<=x<4/27, with the endpoint excluded, even though the scalar U iteration alone remains bounded there.

Increasing y increases every right side, so membership at any y>=0 implies x<4/27. For x=t+epsilon2/t² with 0<t<=1, this implies epsilon2<t²(4/27−t). The maximum on 0<=t<=4/27 is at t=8/81, with value 256/531441 (differentiate: t(8/27−3t)). Therefore this exact recursion method requires epsilon2<256/531441. Along (p,1,2), d3 decreases with p; d3(4150)=8311/17230811=16622/34461622 is greater than 256/531441, while d3(4165)=8341/17355566 is smaller. This brackets a necessary comparison, and the separate exact certificate at 4165 supplies sufficiency there. It neither identifies the least certifiable integer in 4151..4164 nor excludes order below the method's sufficient range. ∎

## Preserved proposals and actual attempt status

1. The existing extended-tree construction was checked historically on finite exhaustive/random cones. These are tests of the positive construction, not distinct exhaustive negative routes.
2. Amplified nodes as noise leaves use the larger noise epsilon2 and lose the two-level improvement. The historical claim that the region empties is withdrawn: epsilon2 tends to zero at large p, recovering the single-noise small-noise regime.
3. Bad amplified poles must be kept in the present potential accounting. The packet supplies the accounting argument, not a theorem excluding different charge or potential constructions.
4. Fresh trees under amplified leaves were proposed with epsilon2 weight and no bad-pair cost, suggesting a rough p around 200 if an appropriate overlap-controlled estimate could be proved. Overlaps and cycles are a named obligation. No explicit complete cycle witness or exhaustive impossibility proof was supplied.
5. The sharper E<=3(|S|−1)+|A| budget is an unresolved proposal. The measured worst 2/3 over the sampled trees is finite evidence, not its proof. The rough p around 500 estimate remains conditional.
6. Counting amplification clusters rather than all substructures is a further open counting proposal; the comparison of 4/27 with a branching value 1/3 is not proof of an improved lattice bound.

The original six-list N1 and full campaign proposals remain verbatim in kept files, with every failed/could-not result and raw scan retained. No five-route PASS, wall independence or universal exclusion is fabricated. Reopen only with exact hypotheses, complete proof/certificate, real distinct-route evidence where required, and independent review.

## Historical finite simulation context

The original claim that truth is eleven and the factor-380 attribution are withdrawn from current science. The preserved coupled simulation uses L=128, T=1500, seed30 and p=12,30,200 at q=1,r=2; finite observed dissent and zero coupling violations are exactly that protocol. The separate reference to a (10.5,11) interval comes from an unlanded sibling and supplies no premise. No infinite-volume or infinite-time bridge is established. Floating fixed-point routines return after finite iteration caps; negative margins in approximate fixed points and all raw outputs are retained. Only the four exact rational super-solution inequalities support the current certificates.
'''
for e in entries:
 if e['original_path'].endswith('.out.txt') or e['original_path'].startswith('logs/'):
  deferred+='\n### Exact historical output: '+e['original_path']+'\n\n```text\n'+(H/e['original_path']).read_text()+'\n```\n'
put(archive/'DEFERRED_SCIENCE.md',deferred)
readme='# Exact PR8174 recovery\n\nOriginal head `'+inv['head']+'`; merge base `'+inv['base']+'`. Every original path, Git mode, blob and raw SHA is recorded in [archive manifest](archive-manifest.json). Historical claims and PASS records are uncorrected provenance, never present-day authority. Gzip objects decode byte-for-byte, including original EOF whitespace; restore the recorded Git mode. Plain proofs and programs remain readable. The complete original delta is [compressed here](original-delta.patch.gz). Retain the original branch for unique deferred science.\n\n[Complete corrected deferred argument and raw outputs](DEFERRED_SCIENCE.md).\n\n'
for e in entries:readme+='- `'+e['original_path']+'`: ['+Path(e['stored_path']).name+']('+e['stored_path']+') ('+e['encoding']+').\n'
put(archive/'README.md',readme)
# Narrow runner changes. Core construction and all original fixtures/certificates preserved.
src=oldrun.read_text();oldsrc=src
src=src.replace('import random\n','import random\nimport hashlib\nimport json\n')
src=src.replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 900\nAUDIT_MEMORY_MB = 768')
a=src.index('AUDIT_INPUT_PATHS = (');b=src.index('\nROOT =',a)
src=src[:a]+'AUDIT_INPUT_PATHS = '+repr(tuple(inputs))+'\nEXPECTED_INPUT_SHA256 = '+repr({p:sha(W/p) for p in inputs})+src[b:]
src=src.replace(re.search(r'CLAIM_ID = "([^"]+)"',src)[1],cid,1)
src=src.replace('    "claim_transition_injected": "F",\n    "claim_classical_name_in_theorem": "F",','    "domination_domain_wrong": "B",\n    "ceiling_endpoint_wrong": "E",')
src=src.replace('        self.passed = 0','        self.results = []\n        self.passed = 0').replace('        if ok:\n            self.passed', '        self.results.append(dict(tag=tag, passed=bool(ok), detail=msg))\n        if ok:\n            self.passed',1)
src=src.replace('    note, axioms, block01 = texts','    note, axioms, block01, single_noise = texts')
src=src.replace('all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS)', 'all(Path(ROOT, p).exists() and hashlib.sha256(Path(ROOT, p).read_bytes()).hexdigest() == EXPECTED_INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS)')
src=src.replace('all declared inputs exist','all declared inputs exist and match exact pins, including the single-noise comparison parent')
a=src.index('    der_ok =');b=src.index('    # d_1 <=',a)
src=src[:a]+'''    derivatives = (
        -3*p**2*(q**3+4*r**3)/(p**3+q**3+4*r**3)**2,
        -(q**3*p**2+8*q*r**3*p)/(p*q*(p+q)+4*r**3)**2,
        -p*(r*p+2*q**2+2*r*q+4*r**2)/(p**2+q**2+r*(p+q)+2*r**2)**2,
    )
    der_ok = all(sp.simplify(sp.diff(d,p)-expected)==0 for d,expected in zip((d1,d2,d3),derivatives))
    checks.check("B1", ok and der_ok, "Three exact closed forms and all three explicit strictly negative derivative identities for positive weights")
    gap = p**2*(p-q)*(q**2*(p+q)+4*r**3)/((p**3+q**3+4*r**3)*(p*q*(p+q)+4*r**3))
    small = deviations(Fraction(1,10),1,1)
    domain_ok = sp.simplify(d2-d1-gap)==0 and small==(Fraction(5000,5001),Fraction(410,411),Fraction(410,411))
    domain_ok = domain_ok and (small[0] <= max(small[1:]) if mut("domination_domain_wrong") else small[0] > max(small[1:]))
    checks.check("B3", domain_ok, "Exact p>=q domination factorization and small-p counterexample to the withdrawn unrestricted domain")
''' +src[b:]
src=src.replace("so the recursion's domain at y = 0 is x <= 4/27", 'scalar U maximum only; full-domain endpoint separately checked')
needle='    d3 = deviations(4150, 1, 2)[2]'
insert='''    denominator = sp.simplify(1-3*((v-1)/v**3)*v**2)
    endpoint_slope = 3*Fraction(4,27)*Fraction(3,2)**2
    endpoint_constant = Fraction(3,2)**2
    endpoint_ok = sp.simplify(denominator-(3-2*v)/v)==0 and endpoint_slope==1 and endpoint_constant==Fraction(9,4)
    if mut("ceiling_endpoint_wrong"):
        endpoint_ok = endpoint_ok and endpoint_slope < 1
    checks.check("E3", endpoint_ok, "Full recursion denominator (3-2v)/v; at the endpoint D=9/4+D, so bounded scalar U alone is insufficient; deferred route-bound diagnostic")
'''
src=src.replace(needle,insert+needle)
a=src.index('# ============================================================================================ family F');b=src.index('# ============================================================================================ main',a)
src=src[:a]+'''# Honest resolution statements; these lines are not counted as scientific checks.
N5_LINES = (
    "per_element: finite exact closed-form and derivative identities, factorization and amplified-excuse increments are checked",
    "per_site: finite all-216 predecessor triples at five weight triples; no sitewise physical or infinite-time threshold is measured",
    "per_mode: exact small cones and original1200 seeded random cones, with finite 66103 lifted-tree enumeration; no exhaustive larger-cone claim",
    "per_block: four exact rational super-solutions and algebraic endpoint diagnostics; conditional positive certificates only",
    "lattice_wide: checked and not executed — written finite-localization, tree-bound and compactness proofs under supplied hypotheses",
)

''' +src[b:]
src=src.replace('    family_f(checks, texts[0])\n    family_g(checks)','    for line in N5_LINES:\n        print(line)')
src=src.replace('    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")','''    result = dict(checks=checks.results, passed=checks.passed, failed=checks.failed,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}, mutation=ACTIVE_MUTATION)
    suffix = "--"+ACTIVE_MUTATION if ACTIVE_MUTATION else ""
    output = ROOT/"logs/runner-cache"/(Path(__file__).stem+suffix+".json")
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("x") as stream:
        json.dump(result,stream,indent=2)
        stream.write("\\n")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")''')
src=src.replace('Scope.  T1:','Scope. Supplied p >= q > 0, r > 0. T1:').replace('its own source for floating-point literals.','exact arithmetic bodies are preserved; no float-scan or prose-count PASS is used.')
put(runner,src,0o755)
compile(src,runner,'exec')
# AST identity of computational helpers, all four certificate definitions and core fixture families.
def nodes(s):return {n.name:n for n in ast.parse(s).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
o,n=nodes(oldsrc),nodes(src);unchanged=[]
for name in ('mut','normalize_text','add','sub','level','M','preds','is_fork','cone','run_automaton','Explainer','check_tree','phi_of','conditional','deviations','test_config','family_c','step','gf_coefficients','exp_bounds','family_d'):
 assert ast.dump(o[name],include_attributes=False)==ast.dump(n[name],include_attributes=False),name;unchanged.append(name)
checks=[c.args[0].value for c in ast.walk(ast.parse(src)) if isinstance(c,ast.Call) and isinstance(c.func,ast.Attribute) and c.func.attr=='check' and c.args and isinstance(c.args[0],ast.Constant)]
assert len(checks)==17,checks
# Preserve original literal math paragraphs and four certificate bodies via exact source inclusion checks.
assert section('*(T2.1, clusters', '*(T2.2, the excuse identity.)*') in body
mapping=[]
for e in entries:
 p=e['original_path'];final=note if p==str(oldnote.relative_to(H)) else runner if p==str(oldrun.relative_to(H)) else None
 mapping.append(dict(original_path=p,original_mode=e['original_mode'],original_blob=e['git_blob'],original_sha256=e['raw_sha256'],disposition='narrowed' if final else 'deferred' if '/specs/' in p else 'superseded',reason='Corrected canonical full proof/program with exact original recovery' if final else 'Historical attempts, controls, failures or author/generated state preserved exactly; no stale current-main replacement or fresh evidence claim',recovery=str(archive/e['stored_path']),encoding=e['encoding'],stored_sha256=e['stored_sha256'],final_path=final,final_sha256=sha(W/final) if final else None))
patch=''.join(difflib.unified_diff(orig.splitlines(True),body.splitlines(True),fromfile=str(oldnote.relative_to(H)),tofile=note))+''.join(difflib.unified_diff(oldsrc.splitlines(True),src.splitlines(True),fromfile=str(oldrun.relative_to(H)),tofile=runner))
(R/'drain8174-author-correction-v1.diff').write_text(patch)
out('drain8174-author-full-mapping-v1.json',mapping)
out('drain8174-author-preservation-v1.json',dict(original_count=25,all_raw_hashes_and_git_blobs_verified=True,unchanged_computational_asts=unchanged,mathematical_changes=['T1 sufficient domain/factorization and explicit three derivatives','T2 full finite localization and pole-transport proof','T4 full invariant-law argument and exact four certificate table','T5 strict full-domain endpoint corrected and readable negative proof deferred; positive parametrization live'],original_fixture_families_unchanged=['family_c','family_d'],current_science_runs=0))
for e in json.loads((O/'main-loss-guard.json').read_text())['conflicting_existing_paths']:
 assert git('ls-tree','HEAD','--',e['path'])==e['main']
assert not git('diff','--name-only','HEAD')
assert set(git('ls-files','--others','--exclude-standard').splitlines())==set(created)
out('drain8174-author-prepared-v1.json',dict(status='Prepared source only; independent affected review pending',base=git('rev-parse','HEAD'),original_head=inv['head'],original_merge_base=inv['base'],notes=[dict(path=note,sha256=sha(W/note))],runners=[dict(path=runner,sha256=sha(W/runner))],archive_manifest=dict(path=str(archive/'archive-manifest.json'),sha256=sha(W/archive/'archive-manifest.json')),deferred_science=dict(path=str(archive/'DEFERRED_SCIENCE.md'),sha256=sha(W/archive/'DEFERRED_SCIENCE.md')),source_paths=created,original_report=ref(R/'drain8174-review-original.json'),original_inventory=ref(O/'inventory.json'),branch_retention_required=True,checks=checks,primary_executions=0,mutation_executions=0,simulation_executions=0))
print(json.dumps(dict(source_files=len(created),note_sha=sha(W/note),runner_sha=sha(W/runner),checks=checks),indent=2))
