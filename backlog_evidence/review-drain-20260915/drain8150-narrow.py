from pathlib import Path
import json,re,gzip
R=Path('/private/tmp/review-drain-20260915'); W=R/'drain-author-slot'
paths=json.loads((R/'drain8150-author-live-paths.json').read_text())
old=[gzip.decompress((W/'docs/work_history/review_loop/pr8150'/str(8148+i)/(str(8148+i)+'_'+Path(p).name+'.gz')).read_bytes()).decode() for i,p in enumerate(paths[::2])]
names=['ADMISSIBILITY_RULE_FORMATION_RATE_IDENTITIES_AND_FINITE_WINDOW_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md','ADMISSIBILITY_RULE_FORMATION_UNIT_CONDITIONAL_IDENTITIES_AND_FINITE_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md','ADMISSIBILITY_RULE_FORMATION_LAW_FLIP_IDENTITIES_AND_FINITE_MIXTURE_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md']
def section(s,title):
 return s.split('## '+title+'\n',1)[1].split('\n## ',1)[0].strip()+'\n'
def body(s,title,text):
 return re.sub(r'(?ms)^## '+re.escape(title)+r'\n.*?(?=^## |\Z)','## '+title+'\n\n'+text.strip()+'\n\n',s)
def common(i,title,scope):
 s=old[i]; s=re.sub(r'(?m)^claim_id:.*$', 'claim_id: '+names[i][:-3].lower(),s);s=re.sub(r'(?m)^claim_scope:.*$','claim_scope: '+json.dumps(scope),s);s=re.sub(r'(?m)^# .*$', '# '+title,s)
 s=body(s,'Machine status and trace','''```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain the named identities and finite witnesses; broad negative certification remains deferred."
conditional_surface_status: "Conditional on the declared six-axis menu, positive product rule and records-only reading."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
The original complete arguments and execution histories are preserved in
[the recovery manifest](work_history/review_loop/pr8150/original-manifest.json).
This source repair does not claim a completed independent audit.''')
 s=body(s,'Exact target and obligation graph',scope+'\n\nUniversal negative conclusions from the original version remain deferred; they are not consequences promoted by this landing surface.')
 s=body(s,'No-Go Discipline Gate','''### N1 — Deferred negative certification
The original route table mixes changes of scope and non-attempts with actual arguments; it does not establish five independent exact-target attack families. Broad negative certification is withheld. The original full proofs remain byte-exact in the recovery manifest, and the original branches remain recovery handles.

### N2 — Supplied model conditions
The finite menu, positive product rule, records-only reading and any stated clock or joint-law convention are supplied mathematical conditions. The original wall-independence assertion does not complete the negative gate.

### N3 — Hidden conditions
The displayed domains govern: fixed exterior records cannot be varied inside a proof about one fixed environment. Value-blind mixing and causal value-dependent scheduling are distinct constructions.

### N4 — Actual mathematical imports
The linked finite-window classification supplies the product law and its at-most-one-recorded-neighbour sufficient condition. The linked census supplies the recorded-set multiset reduction and the quoted rectangle value. These are conditional mathematical inputs; no broader parent conclusions are imported.

### N5 — Executed resolution
The primary runner states its exact finite domains in five resolution lines. Written identities beyond those domains are checked as arguments, not executed on the infinite lattice. Historical controls have their original domains and are not relabelled as current primary execution.

### N6 — Primitive boundary
No primitive selects a rate, unit, measure over orders or boundary condition. The supplied mathematical constructions do not adopt a framework clause.

### N7 — Remaining objection
Positive identities and finite witnesses do not themselves discharge the deferred universal negative certification. Arbitrary fixed-environment necessity additionally has an unresolved proof gap.

### N8 — Recovery
The original complete proofs, including deferred arguments, are recoverable from the manifest; this narrowing does not declare their mathematical negations.''')
 s=body(s,'Review record','''The original author controls, checker notes, proofs and outputs are preserved byte-exact in the recovery manifest. Their historical claims are not current review authority. This corrected draft awaits the original independent reviewer's affected-source confirmation and bounded final capture; no old output is restamped.''')
 return s
# unit
s=common(1,'Formation-unit conditional identities, a sufficient agreement condition, and finite witnesses','Positive-law uniqueness; exact repeated-value normalizer identities; sufficient sequential/joint agreement for arbitrary fixed exterior records when each site with an inside recorded neighbour has exactly one recorded neighbour; exact finite star, plaquette, domino and path witnesses at (3,1,2). Arbitrary fixed-environment necessity and universal exclusions are deferred.')
s=body(s,'Result up front','''Joint formation is a supplied model convention: use the positive law whose one-site conditionals, given all neighbours, equal the product rule. The ratio argument below establishes uniqueness and the displayed edge product establishes existence. This convention is not forced by the axiom sentence.

For any fixed exterior records, sequential formation agrees with this joint law under the sufficient condition stated below. The original necessity proof changed exterior records while claiming to hold them fixed; it does not establish the arbitrary-environment converse. The inherited universal multi-site environment exclusion is therefore deferred.

The primary's isolated-star classes are `k = 0,1,2,3,6`, with exact total variations `0,0,1/72,5/144,103375/1492992`. The historical control also evaluated `k=4,5`, with values `505/10368,575/10368`; those are historical evidence, not additional current-primary domains. The plaquette's 24 orders give `455/31176` for 16 path orders and `37/1299` for 8 diagonal-first orders.''')
s=body(s,'Prior art and what is new','''The linked finite-window classification supplies the sufficient at-most-one-neighbour condition and the census supplies the multiset key. The uniqueness proof is the Brook–Besag ratio argument, restated completely below. The added content is the arbitrary-fixed-boundary sufficient condition, the repeated-value normalizer formulas and the finite unit comparisons. The joint-law convention remains a modelling choice.''')
u2=section(old[1],'Theorem U2 — the criterion'); lemma=u2.split('**Lemma',1)[1].split('*Proof of U2.*',1)[0]
s=body(s,'Theorem U2 — the criterion','''**Sufficient condition.** For any fixed exterior configuration `v_O`, if every `x` with `A_x ∩ U ≠ ∅` has `|A_x|=1`, then `μ_σ(·|v_O)=μ_U^{joint}(·|v_O)`.

*Proof.* Multiply the sequential factors. Every inside edge and every edge from the unit to its exterior contributes one `K`. A normalizer with an inside recorded value is `K_1=1`; every other normalizer depends on `v_O` alone (including the empty-set constant). The product is therefore the joint edge product times a factor independent of `v_U`. Normalization proves equality. ∎

**Lemma'''+lemma+'''
The lemma compares repeated-value configurations. Its strict comparisons are available in isolation or when all fixed exterior values are the same `b`; they do not permit replacing an arbitrary fixed exterior configuration by `b`. The original necessity argument and its universal fixed-environment conclusion are deferred. The primary checks agreement with the sufficient-condition predicate on its listed finite examples; those examples are not a proof of necessity for arbitrary environments.''')
s=body(s,'Theorem U3 — the star does not separate the readings in isolation; the plaquette does','''**Finite witnesses at `(3,1,2)`.** The primary evaluates isolated-star classes `k=0,1,2,3,6`, giving `0,0,1/72,5/144,103375/1492992` respectively. The sufficient condition proves agreement for `k=0,1`. Exact enumeration gives the other three distances. The isolated plaquette's 24 orders give the two positive distances stated above. The class ratios at the three diagonal types are also computed exactly. No universal convex-mixture exclusion is promoted here.''')
s=body(s,'Theorem U4 — in a recorded environment every multi-site unit separates the readings','''**Finite environment comparisons.** The primary evaluates two star orders (`k=0,6`) in the all-`+x` environment and three (`k=0,1,6`) in its fixed mixed environment. It evaluates all two domino orders and all six path orders in the fixed mixed environment. Each listed multi-site comparison has positive exact total variation. The single-site comparison agrees.

For any fixed exterior configuration, a one-site unit has the same sequential and joint law directly from their definitions. The original claim about every connected multi-site unit in every fixed environment relied on the unsupported converse and remains deferred. No claim that every unit after a first unit necessarily has a full recorded environment is made.''')
s=body(s,'The clause candidates (recorded, not adopted)','''A supplied single-site sequential law and a supplied joint law on a specified unit are two mathematical constructions. The sufficient condition and finite comparisons describe their relation at the stated scope. Neither construction is selected by this note.''')
s=body(s,'Falsifiers','''A failed reconstruction of the positive three-site law; a failure of either displayed normalizer identity; a sequential/joint disagreement under the sufficient condition; or an incorrect exact distance on a listed executed unit would falsify the retained result. An arbitrary-environment example is not silently added to the executed domains.''')
fence='This note proves conditional identities and a sufficient agreement condition and reports finite unit witnesses; arbitrary fixed-environment necessity and universal multi-site exclusions are deferred; no unit, order, rule or coupling is selected as physical, and no clause is adopted.'
s=body(s,'Boundaries and non-claims',fence+'\n\n'+section(old[1],'Boundaries and non-claims').split('No plane',1)[1].join(['No plane','']) if False else fence+'\n\nNo plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.\n\nThe menu, weights and formation conventions are declared mathematical inputs, not empirical or axiom-selected values.')
s=body(s,'Imports','''The linked axiom memo supplies only its quoted sentences. The linked finite-window classification and census supply the mathematical inputs identified above. The Brook–Besag positive-law ratio proof is restated, not used as unexplained authority. The triples, units, exterior configurations and order samples are declared model inputs.''')
s=s.replace('E the environment theorem','E finite environment comparisons')
s=s.replace('## Theorem U2 — the criterion','## Theorem U2 — sufficient agreement and normalizer identities').replace('## Theorem U3 — the star does not separate the readings in isolation; the plaquette does','## Theorem U3 — finite star and plaquette witnesses').replace('## Theorem U4 — in a recorded environment every multi-site unit separates the readings','## Theorem U4 — finite environment witnesses')
(W/'docs'/names[1]).write_text(s);(W/paths[2]).unlink(missing_ok=True)
# store draft information; next sections appended in next bounded edit
(R/'drain8150-new-names.json').write_text(json.dumps(names,indent=2)+'\n')
(R/'drain8150-unit-fence.txt').write_text(fence)
# rate
s=common(0,'Formation-rate identities and finite-window witnesses','Positive-total-rate memoryless clocks give causal scheduling weights; value-blind clocks give order mixtures. Exact finite witnesses at (3,1,2), seeded growth equality on connected trees, plaquette coefficient identities and a finite rank-five witness are retained. Universal rate-law and convex-mixture exclusions are deferred.')
s=body(s,'Result up front','''Independent memoryless clocks with positive total rate at every reachable nonfinal state define a finite formation process. Value-blind rates give a mixture over sequential order laws; value-dependent rates give causal scheduling weights that depend on the pattern. These weights are not posterior probabilities of orders conditional on the completed pattern.

The exact rectangle, cube and plaquette witnesses below distinguish the declared clocks at `(3,1,2)`. Seeded growth on a connected tree agrees with the static law. The plaquette algebra gives exact coefficient and difference identities. The original universal exclusions of clock laws and convex mixtures remain deferred pending complete negative certification. No plaquette conclusion is extended to larger windows.''')
s=s.replace('The window `Λ` is the set of sites that can form; the process stops when `Λ` is\nrecorded.','The window `Λ` is the set of sites that can form. Require `Σ_{x∉S} λ_x(S,v_S)>0` at every reachable nonfinal state, so each finite next step is defined; the process stops when `Λ` is recorded.')
s=body(s,'Prior art and what is new','''The linked census supplies the multiset key and the quoted rectangle value; the linked finite-window classification supplies the sufficient one-recorded-neighbour factorization. Competing independent exponential clocks are the usual continuous-time Markov jump construction (Gillespie); seeded cluster growth has the Eden support rule. These names identify mathematical context, not empirical or axiomatic authority. The retained new content is the explicit clock witnesses, seeded-tree construction and plaquette coefficient identities.''')
s=s.replace('`μ_R(v) = Σ_σ P_R(σ | v) μ_σ(v)`, where `P_R(σ | v)` uses at each step only\nthe values recorded before it.','`μ_R(v) = Σ_σ W_R(σ; v) μ_σ(v)`, where `W_R(σ; v)` is the product of the causal site-choice probabilities, each using only previously recorded values. The joint order-pattern mass is `W_R(σ;v) μ_σ(v)`; when `μ_R(v)>0`, the posterior order probability is this joint mass divided by `μ_R(v)`, not `W_R(σ;v)` itself.')
s=s.replace('`720` orders (B2).','`720` orders on 30 sampled rectangle patterns (B2); the plaquette comparison enumerates all 1296 patterns.')
s=s.replace('B applies to every order it charges. Under the uniform law an order in which\ntwo non-adjacent sites form before their common neighbour has positive\nprobability and gives a site with two recorded neighbours. ∎ Executed:', 'B applies to every order it charges. ∎ The uniform-law differences on the two finite trees follow from the exact enumerations below, not merely from charging an order with two recorded neighbours. Executed:')
r4=section(s,'Theorem R4 — no covariant rate law reaches the static law on a plaquette');r4=r4[r4.index('*Proof.*'):];r4=r4.replace('*Proof.*','*Derivation of the coefficient identities.*',1)
r4=r4.replace('In\nneither case the two ratios differ while the static law\'s ratio is constant. ∎','These are the positive normalizer gaps used in the displayed difference identity. ∎')
r4=r4.split('\n*Reading.*',1)[0]
s=body(s,'Theorem R4 — no covariant rate law reaches the static law on a plaquette','''**Retained identity.** On equal-diagonal-type plaquette patterns, the finished-law ratio is the explicit expression below in `G(p,d)`. Its pairwise differences factor through the exact positive normalizer gaps. The universal no-clock-law conclusion from the original argument is deferred, not promoted as a new positive classification.

'''+r4)
s=body(s,'Corollaries R5 and R6','''**Mixture coefficient identity.** For `c_σ≥0`, `Σc_σ=1`, an order mixture on an equal-diagonal-type pattern has ratio `(c_path/6)d+(c_diag/36)d²` to `ΠK`. This follows by grouping the path and diagonal-first products derived above. Its difference between `d'>d>0` is `(d'-d)[c_path/6+c_diag(d'+d)/36]`. The universal convex-mixture exclusion remains deferred.

**Finite rank witness.** At `(3,1,2)`, the matrix of the four plaquette class laws and the declared parallel-growth law on all 1296 patterns has rank five (E5). This is an exact finite linear-algebra witness; it is not a classification of all value-dependent clocks.''')
s=body(s,'The clause candidates (recorded, not adopted)','''Uniform, seeded, attracting and parallel-growth rates are supplied examples. The listed finite statistics describe their differences; the seeded construction agrees with the static law on connected trees. No example is selected as physical. A realized-state reference does not supply a rate law, averaging measure or statistical prediction.''')
s=body(s,'Falsifiers','''A failure of the exponential jump integral, causal scheduling product, sampled class/product agreement, quoted exact finite distances, seeded-tree factorization, plaquette coefficient identities or rank-five witness would falsify the corresponding retained result. No larger-window exclusion is included.''')
fence='This note proves clock and plaquette identities, the seeded-tree construction and finite witnesses; universal clock-law and convex-mixture exclusions are deferred; no order, rate, rule or coupling is selected as physical, and no clause is adopted.'
s=body(s,'Boundaries and non-claims',fence+'\n\nNo plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.\n\nThe menu, weights and clock conventions are declared mathematical inputs, not empirical or axiom-selected values.')
s=body(s,'Imports','''The linked axiom memo supplies only its quoted sentences. The linked finite-window classification and census supply the mathematical inputs identified above. The exponential race integral is proved here; Gillespie and Eden identify context only. All rates, triples and windows are declared model inputs.''')
s=s.replace('## Theorem R4 — no covariant rate law reaches the static law on a plaquette','## Theorem R4 — plaquette coefficient identities').replace('## Corollaries R5 and R6','## Identities R5 and finite rank witness R6').replace('E the plaquette no-go','E the plaquette identities')
(W/'docs'/names[0]).write_text(s);(W/paths[0]).unlink(missing_ok=True);(R/'drain8150-rate-fence.txt').write_text(fence)
# flip
s=common(2,'Formation-law flip identities and finite mixture witnesses','Exact constant-pattern flip identities and their strictness condition for the positive six-axis product rule; mixtures supported on orders with at most one recorded neighbour give the static law; finite mixture witnesses at (3,1,2), including constant-boundary unit comparisons. Universal mixture necessity and cycle or environment exclusions are deferred.')
s=body(s,'Result up front','''The sequential product has an explicit ratio to its edge product. Changing one value of the constant pattern changes only normalizers whose recorded sets contain that site. The normalizer formulas below give an exact nonnegative difference and identify its strictness domain for a nonconstant rule.

Mixtures supported on orders with at most one recorded neighbour per site agree with the static law by the parent factorization. Exact finite mixtures on the path, star, rectangle and plaquette are evaluated at `(3,1,2)`. The uniform rectangle distance is `372254646387017/12790481418000000`. The original universal mixture converse and the cycle and environment exclusions remain deferred pending complete negative certification.''')
s=body(s,'Prior art and what is new','''The linked finite-window classification supplies the sequential product and the sufficient at-most-one-recorded-neighbour factorization. The linked census supplies the multiset reduction and uniform rectangle value. The retained contribution is the explicit flip identity, its constant-boundary version and the finite mixture computations. No negative conclusion from companion work is imported.''')
s=s.replace('**Statement.** For every window, every order `σ`, every value `b` and every\nsite `z`:', '**Statement.** For every finite window, every order `σ`, every value `b`, every site `z`, and a nonconstant positive triple (using the orthogonal flip when `p=q`):')
s=body(s,'Theorem X2 — the mixture theorem','''**Sufficient construction.** If every order charged by `P` has `|A_x(σ)|≤1` at every site, then `μ_P` is the static law. Each charged law equals the static law by the parent factorization, so their probability-weighted sum does also. ∎

**Difference identity.** Linearity gives
`μ_P(v^z)/Π_edges K(v^z) − μ_P(v)/Π_edges K(v) = Σ_σ P(σ)[w_σ(v^z)−w_σ(v)]`.
The summands have the signs proved in the flip lemma. The original promotion of this identity to a universal mixture necessity classification and cycle exclusion remains deferred.

**Finite evidence.** The path has 4 of 6 orders satisfying the sufficient condition; the four-leaf star has 48 of 120. Uniform and seeded pseudo-random mixtures over those orders agree exactly with the static law. The three sampled mixtures charging other orders have positive exact distances. On the rectangle the primary computes the uniform mixture and two sampled class mixtures, and on the plaquette one sampled class mixture. The recorded-set census also verifies the finite graph property on all classes of these windows and the cube. These domains do not mean every possible mixture was executed.''')
s=body(s,'Theorem X3 — units in a constant environment','''**Constant-boundary flip identity.** Let every fixed exterior record equal `b`. Divide the sequential unit law by the product of `K` over inside and unit–exterior edges. Normalizers depending only on exterior records contribute constants. For the inside constant pattern and an inside-site flip, every recorded set containing the flipped site has all its other values equal to `b`. The normalizer lemma therefore gives exactly the factor comparison of the flip proof, with strictness when that inside site lies in a recorded set of size at least two. ∎

The sufficient agreement condition follows by cancelling all normalizers that contain inside values when those recorded sets have size one. The primary computes all domino and path orders in the all-`+x` environment, one sampled mixture for each, and the isolated mixtures supported on qualifying orders. The original universal constant-environment mixture exclusion is deferred. This argument does not vary an arbitrary fixed exterior configuration and does not use the companion note's unsupported arbitrary-environment converse.''')
s=body(s,'X4 — the boundary','''For value-dependent clocks, causal scheduling weights `W_R(σ;v)` can change with the pattern. They are products of sequential site-choice probabilities, not posterior conditional order probabilities. The displayed linear difference identity for fixed mixing weights does not remove those extra terms. This note promotes no value-dependent clock exclusion, on a plaquette or on a larger window.''')
s=body(s,'Falsifiers','''A failure of the normalizer or flip identity, its stated strictness condition, the sufficient static-mixture construction, any quoted finite exact distance, or the constant-boundary factor comparison would falsify the retained result. The primary's finite sampled mixtures are not a universal negative certificate.''')
fence='This note proves flip identities and a sufficient static-mixture construction and reports finite mixture witnesses; universal mixture necessity and cycle or environment exclusions are deferred; no order, mixture, rule or coupling is selected as physical, and no clause is adopted.'
s=body(s,'Boundaries and non-claims',fence+'\n\nNo plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.\n\nThe menu, weights and mixture conventions are declared mathematical inputs, not empirical or axiom-selected values.')
s=body(s,'Imports','''The linked axiom memo supplies only its quoted sentences. The linked finite-window classification supplies the sequential product and sufficient factorization; the linked census supplies the multiset reduction and exact rectangle value. The normalizer lemma and constant-boundary comparison are proved here. No companion negative theorem is an input.''')
s=s.replace('## Theorem X2 — the mixture theorem','## Theorem X2 — sufficient mixtures and a difference identity').replace('## Theorem X3 — units in a constant environment','## Theorem X3 — constant-boundary flip identity')
(W/'docs'/names[2]).write_text(s);(W/paths[4]).unlink(missing_ok=True);(R/'drain8150-flip-fence.txt').write_text(fence)
