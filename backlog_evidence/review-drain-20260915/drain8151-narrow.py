from pathlib import Path
import json,re,ast
r=Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';inv=next(x for x in json.load(open(r/'drain8153-original-inventory.json')) if x['number']==8151);op=next(e['path'] for e in inv['original_paths'] if e['path'].startswith('docs/ADMISSIBILITY'));rp=next(e['path'] for e in inv['original_paths'] if e['path'].startswith('scripts/'));s=(r/'drain8153-originals/8151'/op).read_text();runner=(r/'drain8153-originals/8151'/rp).read_text();new='docs/ADMISSIBILITY_RULE_STATIC_SIX_AXIS_REFLECTION_IDENTITIES_AND_CONDITIONAL_CONTOUR_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md'
def sec(t):return s.split('## '+t+'\n',1)[1].split('\n## ',1)[0]
def change(t,b):
 global s
 s=re.sub(r'(?ms)^## '+re.escape(t)+r'\n.*?(?=^## |\Z)','## '+t+'\n\n'+b.strip()+'\n\n',s)
s=re.sub(r'(?m)^claim_id:.*$','claim_id: '+Path(new).stem.lower(),s)
s=re.sub(r'(?m)^claim_scope:.*$','claim_scope: "Spectrum and signed-permutation symmetry of the positive six-axis pair weight; real site-reflection sum-of-squares identity; full-direction bad-bond event counting; finite torus inequalities and contour arithmetic. Contour and limit implications require explicit independently supplied uniform probability bounds. Unconditional threshold216, long-range order and phase coexistence are not established here."',s)
s=re.sub(r'(?m)^# .*$', '# Static six-axis reflection identities and conditional contour bounds',s)
s=s.replace('**Status:** bounded-support (exact; both the two- and the three-dimensional statements are unconditional; unaudited)','**Status:** bounded-support (declared static model; conditional contour implications; unaudited)')
change('Result up front','''This note retains the spectrum, a real site-reflection sum-of-squares identity, an all-direction counting bound and finite exact controls for a supplied static six-axis product law. It also records what a separately proved uniform bad-bond bound would imply through contour arithmetic and finite-volume limits.

The original phase argument has a gap: site reflections preserve vertex parity, so a reflected canonical bond does not cover all transverse rows. Its reflected event cannot be replaced by the event that every bond in one direction is bad. Consequently the original parameter condition `p ≥ 216 max(q,r)` does not establish long-range order or several Gibbs states here. The full original proof remains in [the recovery manifest](work_history/review_loop/pr8151/original-manifest.json).

The retained arithmetic is `Σ_{n≥4}n/2^n=5/8`, `18·10/2^10=45/256`, and `5/24+45/256=295/768`. These become probability bounds only under the explicit additional hypothesis below. No new framework premise is adopted.''')
change('Machine status and trace','''```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain reflection identities, finite controls and conditional contour implications; the uniform bad-bond bound and unconditional phase conclusion remain open."
conditional_surface_status: "Supplied positive six-axis static model; conditional probability implications explicitly separated from proved identities."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
The original phase verdict and negative certification are deferred. No static/formation Green-function comparison is a premise or conclusion.''')
change('Prior art and what is new','''The linked uniqueness note supplies model context and a separate weak-coupling question; its threshold is not used here. The finite static measure and specification are defined below. Site-reflection positivity is a direct sum of squares. Peierls contour counting, the Whitney planar cut–cycle/Jordan separation result, and the Kolmogorov extension and backward martingale theorems provide the named mathematical context and imports specified below. They do not repair the missing uniform bad-bond probability bound.''')
change('Exact target and obligation graph','''| Object | Retained scope |
|---|---|
| Spectrum and signed permutations | Exact algebra on the six-axis matrix |
| Site reflection | Real-valued half-torus functions; positive symmetric weights |
| Finite inequalities | The two explicitly enumerated ring/torus probability comparisons only |
| All-direction counting | Correct event; `p≥m` counting regime, `p<m` trivial regime |
| Contour arithmetic | Counts and series; probability implication conditional on uniform planar bad-bond hypothesis |
| Torus limits | Existence/specification identity; uniqueness contradiction conditional on a separately supplied uniform correlation lower bound |
| Three dimensions | Finite cube control and conditional planar argument; no unconditional phase result |''')
s=s.replace('For every function `F`','For every real-valued function `F`').replace('No condition on `φ` is needed.','No positive-semidefinite matrix condition on `φ` is needed; its symmetric positive entries remain required.')
s=s.replace('twenty pseudo-random `F` on the ring of four sites and five on the `4×2` torus,\nat `(3,1,2)` and at the indefinite triple `(5,2,4)` (B2).','twenty pseudo-random real `F` on the ring of four sites at each of `(3,1,2)` and `(5,2,4)`, and three on the `4×2` torus at `(3,1,2)` only (B2). A complex-valued version requires conjugation; the stated square identity is real.')
change('Theorem T3 — the chessboard estimate','''**Finite controls.** At `(3,1,2)`, the runner enumerates a ring of four and the periodic `4×2` torus, with doubled bonds in the side-two direction. It checks `μ(bonds (0,1),(2,3) bad)^2 ≤ μ(all ring bonds bad)` and the explicitly selected two horizontal torus bonds satisfy `μ(two bad)^4 ≤ μ(all horizontal bad)`. These are exact finite inequalities, not a general dissemination proof.

**Unresolved dissemination step.** A site reflection sends `x_i` to `2k−x_i`, preserving vertex parity. A canonical horizontal bond therefore visits only even transverse rows. On side four its orbit contains eight of sixteen horizontal bonds in two dimensions, and sixteen of sixty-four in three dimensions. The original substitution of the all-direction event for this reflected event is invalid. At independent spins on the `4×4` torus, the actual reflected event has probability `1225/5184`, whereas the all-direction event has probability `1500625/26873856`, as recorded by the independent review control. These control values diagnose the source gap; the current primary does not recompute them. The original general chessboard/dissemination argument is preserved in the archive, with its conclusion deferred.''')
t4=sec('Theorem T4 — the disseminated bound').split('**Corollary',1)[0];t4=t4.replace('*Proof.* A configuration','*Proof for `p≥m`.* A configuration').replace('at `(3,1,2)` (C1).','at `(432,1,2)` (C1).')
t4+='\nFor `p<m`, the claimed root bound is trivial: a probability has root at most one, while `6m/p>1`. This bound concerns the all-direction event only; it supplies no bound for arbitrary specified bond sets.\n'
change('Theorem T4 — the disseminated bound',t4)
t5=sec('Theorem T5 — long-range order on the two-dimensional torus');t5=t5.replace('**Statement.** Let `d = 2` and `ε = 6m/p ≤ 1/36` (i.e. `p ≥ 216 m`); let','''**Additional unproved hypothesis.** For all planar bond sets `B` needed in the separating contour argument, assume a uniform bound `μ_L(B all bad)≤ε^{|B|/2}`, with `0<ε≤1/36`, for the full family of tori under discussion. This hypothesis is not supplied by the all-direction counting bound or by the finite controls. In particular, this note has not established it with `ε=6m/p`.

**Conditional statement.** Under that hypothesis in `d=2`, let''')
t5=t5.replace('by the corollary of\nT4 with `d = 2` and the count','by the additional uniform bad-bond hypothesis and the count').replace('threshold `p_0 = 216 m`','algebraic substitution `6m/p_0=1/36` at `p_0=216m`, not a proved phase criterion').replace('an illustration on the `4×2` torus','a separate finite illustration on the `4×2` torus')
change('Theorem T5 — long-range order on the two-dimensional torus',t5)
t6=sec('Theorem T6 — from long-range order to several Gibbs states');proof=t6.split('*Proof.*',1)[1].split('(v) *The orbit.*',1)[0];proof=proof.replace('by T5','by the additional correlation hypothesis');proof=proof.replace('Hence\nat least two Gibbs states.','Thus uniqueness contradicts the supplied correlation hypothesis. ∎')
change('Theorem T6 — from long-range order to several Gibbs states','''**Conditional implication.** For the supplied finite positive nearest-neighbour specification, torus local limits exist and are translation-invariant Gibbs states. Separately assume a sequence of tori has `μ_L(v_0=v_x)≥1/2` uniformly for each fixed displacement once the torus is sufficiently large, or along an unbounded coordinate-plane family of displacements in three dimensions. Then any resulting limit has that correlation lower bound, and uniqueness would contradict it by the argument below. This is a conditional implication, not a proof that the hypothesis holds at any coupling specified here.

*Proof.*'''+proof+'''
No orbit bound between two and six is retained. A nonuniform six-value marginal may have 48 cube-group images. Different one-site marginals distinguish states, but equal one-site marginals do not identify states. The original extremal-orbit paragraph is preserved only in the complete historical proof.''')
change('Theorem T7 — three dimensions, by the in-plane count','''**Conditional planar reduction.** Take a coordinate plane containing `0` and `x`. If their values differ, every path joining them inside that plane crosses a bad in-plane bond. The planar separation/counting argument applies to this event if a uniform bound `μ_L(B all bad)≤ε^{|B|/2}` has separately been proved for all required in-plane bond sets, with `ε≤1/36`. Under that additional hypothesis, the contour sum above and the conditional limit argument apply along displacements in the plane. The three-dimensional all-direction counting bound does not establish this hypothesis.

**Finite control.** The primary enumerates the periodic `2×2×2` torus at `(432,1,2)`, with each adjacent pair carrying two bonds. It checks the all-direction bound and a nearest-neighbour agreement probability above one half. These finite facts do not establish long-range order, the uniform in-plane hypothesis or phase coexistence on `Z³`.''')
change('No-Go Discipline Gate','''### N1 — Deferred negative certification
The original route list did not contain five distinct exact-target attacks. The unconditional nonuniqueness/phase conclusion remains deferred together with the incomplete negative certificate. Full original proofs and branches remain recovery sources.

### N2 — Conditions
The static reading, six-axis menu, positivity and torus model are declared mathematical conditions. The additional uniform bad-bond or correlation hypothesis is explicitly unproved here, not a new axiom and not a renamed conclusion.

### N3 — Source gap
Site reflections preserve parity. The actual reflected event and all-direction event have different geometry and different probabilities. No finite example fills this uniform gap.

### N4 — Imports
Planar separation, consistent-law extension and the backward martingale theorem are the standard mathematical imports named below. The uniqueness parent is context only; no strong-coupling result comes from it.

### N5 — Resolution
The spectrum and finite matrices/tori are executed domains. Contour formulas are exact arithmetic. Written conditional implications are checked arguments, not infinite-lattice executions.

### N6 — Primitive boundary
No primitive supplies a coupling, a probability bound or a selected state.

### N7 — Outstanding obligation
A valid uniform probability bound with correct reflected geometry and normalization is still required before deriving a phase conclusion. Equal one-site marginals cannot identify Gibbs states.

### N8 — Recovery
Original proof histories, controls and outputs are archived without promoting them to current evidence. The historical refuter calls a removed routine and cannot reproduce its output against the current primary unchanged.''')
change('Falsifiers','''A failed spectrum identity or signed-permutation invariance; a negative real reflection quadratic form; failure of a stated finite probability comparison or all-direction count; incorrect cycle counts `1,4,22` at lengths `4,6,8`; or incorrect series values would falsify the retained result. A counterexample to the additional unproved uniform probability hypothesis would affect a proposed application of the conditional argument, not turn that hypothesis into a theorem.''')
fences=['This note proves reflection identities, all-direction counting and finite controls, and gives explicitly conditional contour and limit implications; unconditional strong-coupling phase conclusions and the original state-orbit bound are deferred, and no coupling is selected as physical.','No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.','The static model and extra probability hypotheses are declared mathematical conditions; standard mathematical imports are explicitly named.']
change('Boundaries and non-claims','\n\n'.join(fences))
change('Imports','''The linked axiom memo supplies only its quoted sentences. The linked one-site uniqueness note provides model context and no strong-coupling conclusion. The finite static law and local conditional specification are defined here.

For the conditional contour step: Whitney planar cut–cycle duality and the Jordan separation theorem for lattice polygons, in the exact separation form stated above. For torus local limits: Kolmogorov extension for consistent finite-dimensional laws. For the conditional uniqueness contradiction: the backward martingale theorem in `L¹` for decreasing exterior sigma-fields. These are mathematical imports, not physical premises. No extremal-decomposition theorem is required by the retained proof.

Peierls and the Fröhlich–Israel–Lieb–Simon/Biskup treatment name historical mathematical context only; their names do not supply the missing probability bound.''')
change('Review record','''The original complete proof, author controls and outputs are preserved in the recovery manifest. The old control uses simple vertical pairs, whereas the current side-two torus doubles those bonds. The historical refuter calls a removed helper and is source-dependent evidence, not a current reproducible control. The independent original reviewer found the parity/dissemination gap and the false six-image bound. This author repair awaits that same reviewer's affected-source confirmation; no primary has been executed for this draft.''')
s=s.replace('## Theorem T3 — the chessboard estimate','## Theorem T3 — finite probability comparisons and the dissemination gap').replace('## Theorem T4 — the disseminated bound','## Theorem T4 — the all-direction bad-bond count').replace('## Theorem T5 — long-range order on the two-dimensional torus','## Theorem T5 — conditional planar contour bound').replace('## Theorem T6 — from long-range order to several Gibbs states','## Theorem T6 — conditional torus-limit implication').replace('## Theorem T7 — three dimensions, by the in-plane count','## Theorem T7 — conditional in-plane argument and finite cube control')
s=s.replace('B the spectrum and symmetry, reflection positivity, the chessboard instances; C the disseminated bound, the two-dimensional counts, series, winding bound, threshold and illustration; D the three-dimensional disseminated bound and illustration','B the spectrum and symmetry, reflection positivity and finite probability comparisons; C the all-direction count, contour arithmetic, parameter substitution and illustration; D the three-dimensional all-direction count and illustration')
(w/new).write_text(s);(w/op).unlink(missing_ok=True)
runner=runner.replace(op,new).replace(Path(op).stem.lower(),Path(new).stem.lower()).replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 300')
runner=re.sub(r'(?s)""".*?"""','"""Exact spectrum, real reflection, all-direction event and finite contour-arithmetic controls.\nThe uniform bad-bond hypothesis and unconditional phase conclusions remain unproved.\nHistorical runner and mutation identifiers are retained for recovery continuity.\n"""',runner,count=1)
runner=re.sub(r'(?s)FENCES = \(.*?\n\)','FENCES = '+repr(tuple(fences)),runner,count=1)
runner=runner.replace('T3: chessboard instances','T3: finite probability comparisons').replace('T5: at m = 2 the threshold is p_0 = 432','T5 arithmetic only: at m = 2 the parameter p_0 = 432').replace('i.e. p_0 = 216 m','algebraically p_0 = 216 m, with no phase conclusion')
runner=re.sub(r'(?m)^    "lattice_wide:.*$','    "lattice_wide: checked and not executed — written identities and conditional implications only; uniform bad-bond and phase conclusions not established",',runner)
runner=re.sub(r'(?m)^    print\("scope:.*$','    print("scope: spectrum, real reflection identities, all-direction counting and finite controls; conditional contour arithmetic only; unconditional phase result deferred")',runner)
runner=runner.replace('the chessboard instances on the ring','finite probability comparisons on the ring').replace('the disseminated ratios','the all-direction ratios')
ast.parse(runner);(w/rp).write_text(runner)
(r/'drain8151-author-live.json').write_text(json.dumps({'note':new,'runner':rp,'fences':fences},indent=2)+'\n')
