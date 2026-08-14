---
claim_id: admissibility_m2_effect_label_record_carrier_atomic_born_law_factorization_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For a supplied finite qubit-effect resolution and distinct real outcome labels, the map kappa(E,ell)=E+i ell I injects the effect-label pair into the existing one-site domain M_2(C). Its Hermitian-part and imaginary-trace projections recover E and ell exactly and are covariant under simultaneous unitary conjugation. Combining this carrier with the common Gaussian uniformizer and any supplied normalized positive effect functional gives an exact atomic output law with masses omega(E_j); for the displayed second-moment functional it reproduces the two exact shared-effect menus and makes one fixed output-code atom vary with the preparation center. This is a conditional mathematical local-law factorization, not a derivation or selection of a Record content map or readout, density functional, effect program, program/preparation quotient, writer dynamics, formation site/rate, realized history, or frequency law. It proves only that the existing M_2(C) domain contains this explicit effect-plus-label carrier; it proves no physical type sufficiency, axiom sufficiency, necessity, adoption, or autonomous Born closure."
upstream_dependencies:
  - minimal_axioms
  - declared_imaginary_trace_functional_hermitian_kernel_bounded_theorem_note_2026-08-13
  - record_content_only_shared_effect_descent_bounded_theorem_note_2026-08-12
  - admissibility_gaussian_second_moment_quantile_decoder_effect_quotient_bounded_theorem_note_2026-08-10
  - admissibility_gaussian_content_only_uniformizer_weierstrass_decoder_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_m2_effect_label_record_carrier_atomic_born_law_factorization_2026_08_10.py
---

# M2 Effect-Label Carrier And Conditional Atomic-Law Factorization

**Date:** 2026-08-10
**Type:** bounded_theorem
**Construction:** exact carrier theorem plus conditional local-law factorization
**Scope:** one `M_2(C)` site, finite supplied qubit-effect resolutions, distinct
real labels, the displayed Gaussian uniformizer and second-moment functional,
and a condition-dependent atomic output law.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_m2_effect_label_record_carrier_atomic_born_law_factorization_2026_08_10.py`](../scripts/admissibility_m2_effect_label_record_carrier_atomic_born_law_factorization_2026_08_10.py)
**Runner cache:**
[`logs/runner-cache/admissibility_m2_effect_label_record_carrier_atomic_born_law_factorization_2026_08_10.txt`](../logs/runner-cache/admissibility_m2_effect_label_record_carrier_atomic_born_law_factorization_2026_08_10.txt)

## Result Up Front

The current one-site domain already contains an explicit algebraic carrier for
the effect-plus-label objects left open by the reviewed Gaussian compiler. Let
`E` be a Hermitian qubit effect, let `ell` be a real outcome label, and define

`kappa(E,ell)=E+i ell I_2`.

This is one element of the already supplied possibility domain `M_2(C)`. The
two fixed algebraic projections

`Q(R)=(R+R^dagger)/2`,

`L(R)=(1/2) Im Tr R`

obey `Q(kappa(E,ell))=E` and `L(kappa(E,ell))=ell`. Consequently `kappa` is
injective on effect-label pairs. It is covariant under every simultaneous
unitary conjugation because the label occupies the central anti-Hermitian
direction. The existing eight-real-dimensional matrix type carries the four
real effect coordinates and one real label coordinate with three real
coordinates unused.

Now supply a finite effect resolution `(E_1,...,E_r)`, distinct labels
`(ell_1,...,ell_r)`, and a normalized positive functional `omega`. The atomic
measure

`nu=sum_j omega(E_j) delta_(kappa(E_j,ell_j))`

is a probability distribution on the existing one-site domain. The one fixed
algebraic fiber event for `kappa(E_j,ell_j)` has probability `omega(E_j)`.
When
`omega_C(E)=Tr(rho_C E)` is the displayed Gaussian second-moment functional,
the reviewed common Gaussian uniformizer provides an exact deterministic
sampler of `nu`. At `C=P_z`, two rational ternary resolutions sharing
`E_0=(1/2)P_z` give the exact vectors

`(3/10,19/50,8/25)` and `(3/10,7/20,7/20)`.

The shared effect and label produce the same exact matrix codeword in both
programs with mass `3/10`. Along `C=tP_z`, that same codeword has mass

`(t^2+2)/(2(t^2+4))`,

so one fixed output-code event has the required preparation-dependent mass.
This does not contradict the current-main fixed-kernel theorem: the measure
being tested is the condition-dependent atomic pushforward `nu`, not the
untranslated raw Gaussian measure `mu_C`.

This closes only the algebraic carrier and projection questions for the
displayed conditional construction. The current Record clause does not select
`kappa`, `Q`, or `L` as physical content or readout. The construction does not
select the positive functional, derive the effect resolution from a physical
neighbor pattern, establish a preparation/program quotient, or turn the
sampler into an autonomous writer or history law. No canonical axiom is
edited, and the fixed TOE percentages do not move.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact M_2(C) effect-label injection, fixed algebraic projections, unitary covariance, exact atomic effect-weight law, shared-effect codeword, and Gaussian-uniformizer factorization; Record content/readout selection, local-law selection, physical program/preparation registration, occurrence, histories, and axiom adoption remain open."
trace_class: upstream_support
target_claim_id: admissibility_record_m2_effect_label_atomic_born_law_bridge
target_blocker_text: "derive or explicitly supply one covariant nearest-neighbor map from physical preparation/program conditions to a normalized positive functional and operational-effect resolution, then connect Record formation events into trials and histories"
source_of_blocker_text: reviewed_current_main_gaussian_compiler_boundary
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Test whether an existing M_2(C)-native contact/action construction selects the positive functional and operational-effect quotient; if not, retain the exact Admissibility-side candidate wording below as the narrow update surface."
conditional_surface_status: "the existing one-site domain contains an exact effect-plus-label carrier and supports a fixed algebraic fiber in a supplied Born-form atomic law; physical Record content/readout selection, law selection, and the program quotient are not derived"
hypothetical_axiom_status: "the displayed encoding requires no separate factor in the one-site algebraic domain; no physical type sufficiency, edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Obligation Graph

**Exact target.** Decide whether one selected effect and one real output label
can be represented inside the current one-site possibility domain, then
separate that algebraic representation from Record content/readout and law
selection.

| Obligation | Role | Disposition |
|---|---|---|
| inject one qubit effect and one real label into one local possibility | algebraic carrier | closed by `kappa(E,ell)` |
| recover the effect and label by fixed matrix functions | algebraic projections | closed by `Q` and `L` |
| preserve simultaneous unitary/proper-cubic covariance | physical symmetry | closed for the carrier and co-transported program |
| select the carrier and projections as physical Record content/readout | Record bridge | open; not supplied by Record |
| optionally sum declared labels over a supplied finite collection | mathematical aggregate | algebraically additive; not a Record premise |
| assign exact normalized effect masses | one-shot probability | closed conditional on supplied `omega` and effect resolution |
| reproduce the displayed Gaussian target by a deterministic sampler | factorization | closed conditional on `rho_C`, program, and common uniformizer |
| give one shared effect the same code and mass across supplied programs | fixed-preparation effect descent | closed in the displayed pair |
| derive `omega`, program, and preparation/effect equivalence from physical neighbors | local-law selection | open |
| cause the rule, formation site/rate, trials, and realized histories | autonomy/history | open |

The construction is deliberately type-ordered. `kappa`, `Q`, and `L` are
fixed matrix maps. Their use as Record content or readout is a separate open
bridge. The atomic distribution is another separately supplied law. A formula
that represents the desired law does not prove that the current four axioms
select it.

## Theorem 1 — An Exact M2 Effect-Label Carrier

Let

`Eff_2={E in M_2(C): E=E^dagger, 0<=E<=I_2}`.

For `(E,ell) in Eff_2 x R`, set

`kappa(E,ell)=E+i ell I_2`.

Define on all of `M_2(C)`

`Q(R)=(R+R^dagger)/2`,

`L(R)=(1/2) Im Tr R`.

Because `E` is Hermitian and has real trace,

`Q(kappa(E,ell))=E`,

`L(kappa(E,ell))=(1/2) Im(Tr E+2i ell)=ell`.

Thus `(Q,L)` is a left inverse of `kappa`; in particular, `kappa` is
injective. No effect-label collision is possible on the code surface.

The real dimension count is also explicit. `M_2(C)` has eight real
coordinates, its Hermitian subspace has four, and the central anti-Hermitian
label direction uses one more. Three real anti-Hermitian traceless coordinates
remain unused. This count is only a capacity statement, not a claim that every
program or preparation can be encoded canonically.

### Covariance

For every unitary `V`,

`kappa(VEV^dagger,ell)=V kappa(E,ell) V^dagger`,

`Q(VRV^dagger)=VQ(R)V^dagger`,

`L(VRV^dagger)=L(R)`.

The scalar label is not tied to a Bloch axis. Hence any supplied unitary
implementation of a proper-cubic rotation co-transports the effect while
leaving its label fixed. Applying the same formula at every translated site
introduces no privileged site.

## Theorem 2 — Candidate Content Projections And An Optional Aggregate

If a separate formation bridge writes a codeword `R=kappa(E,ell)` as Record
content, then the pair-valued candidate `(Q(R),L(R))` depends on that matrix
alone. This is compatible with content-only dependence, but the current Record
axiom selects neither the encoding nor these functions as physical readout.

For any separately supplied finite collection `F` of codewords, one may also
define the mathematical scalar

`I_L(F)=sum_(R in F) L(R)`,

with `I_L(empty)=0`. If `F` and `G` are disjoint, then

`I_L(F union G)=I_L(F)+I_L(G)`.

This sum is algebraically additive by definition. The current Record axiom
supplies no named scalar functional, finite-additivity clause, empty-set value,
or finite-collection readout. Thus `I_L` is an optional mathematical aggregate,
not framework premise or a physical readout claim.

Distinct labels can be chosen globally for a finite program. If the same
effect is intended to have the same operational outcome in two programs, use
the same label. The resulting codeword is literally identical; no
context-dependent algebraic projection is required. Physical formation and
readout selection remain separate.

## Theorem 3 — Conditional Atomic Effect-Weight Law

Let `(E_1,...,E_r)` be a supplied finite effect resolution:

`E_j>=0`, `sum_j E_j=I_2`.

Let the real labels be distinct and let `omega` be a supplied normalized
positive linear functional on `M_2(C)`. Then

`p_j=omega(E_j)>=0`, `sum_j p_j=omega(I_2)=1`.

Therefore

`nu_(omega,M)=sum_j p_j delta_(kappa(E_j,ell_j))`

is a probability measure on `M_2(C)`. Its support contains only existing local
possibilities. The fixed algebraic fiber satisfies

`nu_(omega,M)({R:Q(R)=E_j and L(R)=ell_j})=omega(E_j)`.

If two supplied programs at the same preparation contain the same effect and
label, their corresponding decoded atom has the same mass because the mass is
a function of `omega` and `E`, not of the remaining menu entries.

This theorem is a template for a current-compatible Admissibility completion:
the local distribution can be `nu_(omega_eta,M_eta)` when one fixed covariant
neighbor rule supplies `omega_eta` and `M_eta` and the resulting distribution
varies with `eta`. The four axioms do not select that map, and the theorem does
not assert that every arbitrary supplied pair satisfies the covariance and
variation clauses.

## Theorem 4 — Gaussian Uniformizer Factorization

Use the displayed Gaussian family

`d mu_C(A)=pi^(-4) exp(-||A-C||_HS^2)d^8A`

with Hermitian `C`, the common Gaussian uniformizer

`U(A)=Phi(Im Tr A)`,

and the second-moment functional

`omega_C(E)=Tr(rho_C E)`,

`rho_C=(C^2+2I_2)/(Tr(C^2)+4)`.

For a supplied ordered resolution write `p_j=omega_C(E_j)`, `c_0=0`, and
`c_j=sum_(k<=j)p_k`. Define the mathematical sampler

`W_(C,M)(A)=kappa(E_j,ell_j)` when `c_(j-1)<=U(A)<c_j`,

with the measure-zero upper endpoint assigned to the final interval. Since
`U` is uniform under every `mu_C`,

`(W_(C,M))_* mu_C=nu_(omega_C,M)`.

The sampler is deterministic after `A`, `C`, and the ordered program are
supplied. It is not a dynamics or Record-writing theorem. Equivalently, `nu`
may be used
directly as the local Admissibility distribution without positing a temporal
Gaussian-to-Record conversion.

Under simultaneous transport

`C -> VCV^dagger`, `E_j -> VE_jV^dagger`,

the weights and quantile cuts are unchanged and every output codeword is
conjugated by `V`. The factorization is therefore covariant conditional on a
covariantly supplied program.

## Theorem 5 — Exact Shared-Effect Fixtures

At `C=P_z`,

`rho_C=diag(3/5,2/5)`.

Take the shared effect

`E_0=diag(1/2,0)`

and labels `(1,2,3)`. The following two rational ternary resolutions make the
carrier checks independent of irrational Bloch coordinates:

`M_A=(E_0, diag(1/2,1/5), diag(0,4/5))`,

`M_B=(E_0, [[1/4,1/4],[1/4,1/2]], [[1/4,-1/4],[-1/4,1/2]])`.

Every entry is positive semidefinite and each menu sums to `I_2`. Direct trace
evaluation gives

`p(M_A)=(3/10,19/50,8/25)`,

`p(M_B)=(3/10,7/20,7/20)`.

These are the same exact weight vectors as the current-main Gaussian compiler
fixtures, now on rational effect matrices chosen to expose the matrix carrier.
The menus share only `E_0`; with the shared label `1`, they share exactly the
codeword

`kappa(E_0,1)=diag(1/2+i,i)`.

Its mass is `3/10` in both programs. `Q` and `L` recover `E_0` and `1` without
knowing which program was used.

Along `C=tP_z`, the same second-moment functional gives

`omega_t(E_0)=(t^2+2)/(2(t^2+4))`.

It equals `1/4` at `t=0`, `3/10` at `t=1`, and `3/8` at `t=2`. Thus a single
fixed codeword has a condition-dependent mass in the atomic law. The
current-main analytic fixed-kernel boundary is bypassed by changing the output
law through a supplied local factorization, not by finding a forbidden fixed
kernel on the raw Gaussian input.

## Exact Axiom-Side Residual

The carrier theorem establishes one narrow algebraic statement:

> The existing `M_2(C)` domain contains an injective representation of one
> qubit effect and one real label; this displayed representation needs no
> separate product factor.

If a separate formation bridge writes the codeword and a readout bridge
selects `Q` and `L`, those functions are compatible with content-only
dependence. Record supplies neither bridge, so no physical type-sufficiency or
Record-closure conclusion follows from the injection.

What remains is predominantly a law-selection obligation. One precise
sufficient candidate addition to Admissibility is:

> For each Record-forming site, the same fixed nearest-neighbor rule derives a
> normalized positive linear functional `omega_eta` and a finite registered
> operational-effect resolution `(E_(eta,j),ell_j)` with
> `sum_j E_(eta,j)=I_2`. It assigns the local possibility
> `E_(eta,j)+i ell_j I_2` probability `omega_eta(E_(eta,j))`. The assignment is
> translation- and proper-cubic-covariant. Neighbor conditions registered as
> the same preparation and outcomes registered as the same effect have the
> same functional value.

This wording would directly supply Born-form one-shot masses and a physical
preparation/effect quotient while retaining the existing `M_2(C)` domain. It
is hypothetical wording only. The theorem does not prove that this
addition is necessary, minimal, preferable to a downstream retained bridge,
or sufficient for histories. It is not adopted and the canonical axiom memo
is unchanged.

Separate obligations remain for:

- deriving rather than stipulating `eta -> omega_eta` and the effect program;
- identifying which physical neighbor patterns instantiate one preparation
  and one operational effect;
- selecting the raw second moment rather than another covariant positive
  functional;
- causing formation at particular sites and rates;
- defining trials, causal order, conditional independence or correlations,
  frequency typicality, and one realized history;
- coupling the probability/Record construction to the causal-time and
  gravity/source lanes.

## Relation To Prior Results

The current
[`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md), lines 31--73 and 79--84,
supply the `M_2(C)` possibility domain, a neighborhood-varying probability
distribution, and content-only Record dependence when a record is present.
They supply no scalar functional, finite additivity, content map, density
functional, effect program, atomic law, or operational quotient.

The
[`declared imaginary-trace theorem`](DECLARED_IMAGINARY_TRACE_FUNCTIONAL_HERMITIAN_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-13.md)
already proves that `J(H)=0` on Hermitian matrices and `J(i ell I)=ell`. The
[`shared-effect descent theorem`](RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md)
already uses `E+i alpha I` as one formal two-menu context tag. Those priors
supply the two algebraic ingredients but neither constructs the generic
effect-label injection together with an arbitrary finite positive-functional
atomic law nor factors that law through the Gaussian uniformizer. Those
integrated finite-law statements are the novel content here.

The
[`Gaussian compiler source`](ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md),
supplies the second-moment functional and exact quantile masses but leaves
physical program storage open. The present carrier encodes the selected
effect and label algebraically in the one-site domain; it does not derive that
encoding as Record content.

The
[`common-uniformizer boundary`](ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER_WEIERSTRASS_DECODER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
lines 121--306 and 436--458, proves that raw Gaussian content cannot be read by
one fixed bounded kernel to obtain the varying target, while an indexed
threshold succeeds. The atomic sampler is an explicit mathematical
realization of that indexed escape and makes clear where the index enters.

## No-Go Discipline Gate

The positive claim is the exact carrier and conditional atomic-law
factorization. The only negative conclusion is that this construction alone
does not select its physical law or produce histories. No global Born,
Admissibility, Record, contact, or axiom no-go is claimed.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| separate algebraic product factor | append an external effect/label coordinate | not required for this displayed representation because `kappa` is injective in `M_2(C)`; physical content selection remains open | **ATTEMPTED** |
| relax content-only dependence | let the readout inspect an external program | not needed by the candidate projections after the selected effect and label are supplied in the codeword; neither writing nor readout is derived | **ATTEMPTED** |
| raw Gaussian fixed kernel | decode the untranslated `mu_C` by one bounded kernel | excluded only on the current-main open-center slice | **ATTEMPTED** |
| Gaussian indexed sampler | use common `U` and condition-dependent cumulative cuts, then emit `kappa` | succeeds mathematically and yields the atomic law | **ATTEMPTED** |
| direct atomic Admissibility law | assign `nu_(omega_eta,M_eta)` without a temporal sampler | succeeds as a compatible conditional completion when the supplied map meets covariance and variation | **ATTEMPTED** |
| changed continuous law | choose one fixed event whose mass is already `omega_eta(E)` | remains viable; not classified here | **ATTEMPTED** |
| contact-derived writer | derive the cut and codeword from an existing local process | remains viable; no such derivation is claimed here | **ATTEMPTED** |
| record-derived preparation/program fields | infer the quotient from a larger record process | remains viable after process and occurrence bridges | **ATTEMPTED** |
| finite-history construction | wire output atoms into trials and correlations | remains viable and is outside the one-site theorem | **ATTEMPTED** |

The direct-law route prevents the absence of a writer dynamics from being
misstated as an independent mathematical obstruction. The law-selection and
history questions remain physical obligations.

### N2 — wall independence and collapse

The one-site algebraic carrier, projections, and atom-splitting resource are
closed inside the displayed construction. Record selection remains open along
with three further residuals.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| Record content/readout selection / positive-functional local-law selection | no: a content map does not assign masses | no: a law does not identify its atoms as readable content | independent |
| positive-functional/local-law selection / preparation-effect quotient | no: a functional formula does not identify physically equivalent conditions | no: an equivalence relation does not select probability values | independent |
| positive-functional/local-law selection / occurrence-history law | no: one-shot masses do not cause trials or order Records | no: an occurrence process need not carry Born-form masses | independent |
| preparation-effect quotient / occurrence-history law | no: operational identity does not form Records | no: Records forming do not identify equal preparations or effects | independent |

A separate dynamic writer wall collapses into local-law selection because the
direct atomic law is a live route. A writer is one possible implementation,
not a logically necessary extra stage.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `M_2(C)` as full one-site domain | supplied by Qubit |
| Hermitian qubit effects and real labels | supplied mathematical program objects; not selected physically |
| central anti-Hermitian label direction | derived from the existing algebra; no extra dimension imported |
| `Q` and `L` as physical Record readout | absent; only declared mathematical projections are used |
| finite label sum `I_L` | optional declared aggregate; current Record supplies no scalar or additivity |
| normalized positive functional `omega` | explicit conditional input |
| finite effect resolution | explicit conditional input |
| Gaussian family and second moment | inherited displayed completion; not selected by current axioms |
| common uniformizer | inherited exact theorem on that completion |
| atomic pushforward | derived measure; not asserted as a temporal process |
| equal effect/label across programs | explicit fixture and proposed operational registration |
| preparation/program quotient | absent and explicitly open |
| formation sites, rates, trials, history | absent and explicitly open |

No observed probability, preferred basis, apparatus, target frequency,
formation rate, IID ensemble, causal clock, or gravity source is imported.

### N4 — source residual matching

| Source location | Source residual used | Residual attacked here | Closure claimed here | Match |
|---|---|---|---|---:|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), current Qubit/Admissibility/Record clauses | `M_2(C)` domain, varying local distribution, and content-only dependence; no scalar/additivity/content map | test algebraic carrier capacity and a compatible atomic-law template | exact conditional construction only; no Record selection | yes |
| [`declared imaginary-trace theorem`](DECLARED_IMAGINARY_TRACE_FUNCTIONAL_HERMITIAN_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-13.md), kernel/right-inverse sections | `J(H)=0` and `J(i ell I)=ell`; no physical readout | combine the label line with an arbitrary Hermitian effect | generic effect-label carrier only | yes |
| [`shared-effect descent theorem`](RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md), context-bearing witness | one formal `E+i alpha I` two-menu tag; no formation/readout selection | generalize to arbitrary finite effects/labels and a positive-functional atomic law | integrated finite-law factorization only | yes |
| [`compiler source`](ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md), exact-compiler sections | exact weights exist but physical program storage is open | encode selected effect and label in one matrix | carrier and mathematical sampler only | yes |
| [`uniformizer source`](ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER_WEIERSTRASS_DECODER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md), fixed-kernel and indexed-escape sections | fixed raw kernel fails; indexed threshold succeeds | emit a fixed algebraic output after indexed selection | atomic pushforward escape only | yes |

### N5 — resolution and rhetoric audit

| Statement | Per element | Per site | Per mode | Per block | Lattice-wide |
|---|---|---|---|---|---|
| carrier inversion | every matrix entry of rational fixtures | one `M_2(C)` codeword | identity, Pauli-X, and phase conjugations | all supplied finite labels/effects | covariance only; no formation |
| atomic law | every menu effect and weight | one output site | two programs and several `t` conditions | displayed functional/program family | one fixed formula if neighbors supply the program |
| shared-effect descent | exact shared codeword | same output site | both rational ternary programs | fixed preparation `C=P_z` | no apparatus-equivalence derivation |
| Gaussian factorization | every quantile interval | one mathematical input/output pair | common uniformizer and atomic output | displayed Gaussian completion | no temporal dynamics or histories |

The runner cache emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure and primitive paths

1. A retained local contact may derive the positive functional, program,
   effect-label code, and Record readout from neighbor Records.
2. Admissibility may directly select the atomic law, with no writer stage.
3. A changed continuous law may give the target mass to one fixed decoded
   event without atomic output.
4. A record-derived process may define preparation and program equivalence
   before applying the same carrier.
5. Owner-approved wording may explicitly supply the sufficient local-law
   clause stated above.
6. A separate causal-time construction may define trials and histories while
   reusing the one-site atomic law.

The primitive-registry scan used
`docs/audit/data/axiom_premise_nodes.json` and the approved primitive sources.
The scale reference supplies units only, kinetic isotropy supplies a
kinetic-form ratio only, and the realized-state primitive supplies pointwise
evaluation only. None selects a positive functional, effect program,
preparation quotient, content map/readout, atomic law, writer, formation
site/rate, or history.

### N7 — hostile steelman

> Admissibility already grants one neighbor-dependent distribution over
> `M_2(C)`. The atomic measure displayed here is therefore a valid realization,
> and no axiom amendment or temporal writer is needed. Calling its selection a
> missing axiom may confuse an unspecified law with an inconsistent ontology.

This steelman is accepted. The construction proves compatibility and a
sufficient downstream bridge, not entailment. The missing item can be closed
by a retained derivation of the local law rather than an axiom amendment. The
hypothetical wording is recorded only because the campaign asks what an axiom
update would have to supply if no derivation is found.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| current-main type separation distinguishes a whole-domain measure from a menu kernel | the Gaussian compiler builds program-relative events | the atomic output makes the relevant algebraic fibers literal atoms without confusing them with raw Gaussian points |
| the Aug 12 shared-effect theorem exhibits one formal context tag | the Aug 13 imaginary-trace theorem gives its generic label right inverse | this theorem integrates those ingredients with an arbitrary finite positive-functional atomic law |
| the Gaussian compiler leaves physical program storage open | the common uniformizer supplies a condition-independent random scalar | the carrier stores the selected effect and outcome label algebraically, while program and Record selection remain upstream |
| the fixed-kernel theorem excludes one raw Gaussian route | indexed thresholding remains live | the indexed sampler followed by fixed algebraic projection is that live escape |
| prior record-process work reconstructed fields from Records | implementation and occurrence remained open | a later process can reuse `kappa` only after deriving physical content/readout selection |

**Gate disposition:** PASS for the exact `M_2(C)` carrier, algebraic
projections, optional declared aggregate, conditional atomic law,
shared-effect fixture, and
Gaussian-uniformizer factorization. FAIL / DO NOT SHIP for current-axiom law
selection, Record content/readout selection, a derived physical
program/preparation quotient, autonomous writer dynamics, formation site/rate,
realized-history or frequency closure, physical type sufficiency, axiom
necessity/minimality, or any TOE percentage increase.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| Qubit `M_2(C)` domain | carrier space | supplied; unchanged |
| Admissibility distribution and Record readout clauses | semantic baseline | supplied; unchanged |
| Hermitian effects, finite resolution, and labels | mathematical program | explicit conditional input |
| `kappa`, `Q`, and `L` | carrier and algebraic projections | exact algebra proved here; no physical Record selection |
| normalized positive functional | target mass assignment | conditional input |
| Gaussian family, second moment, and common uniformizer | explicit factorization | inherited bounded completion |
| atomic output law | current-compatible constructed measure | derived conditional completion; not selected |
| preparation/effect quotient | physical identification | open |
| occurrence and histories | autonomous realization | open |
| canonical axiom edit | governance action | forbidden absent owner authority; not performed |

The theorem does not move the fixed TOE percentages because it retires no
current-axiom physical-selection or autonomous-history obligation. It shows
only that one supplied effect-label code fits algebraically in `M_2(C)`;
specifying or deriving the Record content/readout, local positive functional,
effect program, and physical quotient remains necessary before solving
occurrence/history separately.

## Review Record

The submission was originally stacked, but review-loop replayed its science on
reviewed current main. It consumes the landed Gaussian compiler and
fixed-kernel theorem and directly acknowledges the Aug 12 context-tag and Aug
13 imaginary-trace overlaps; no branch-local or closed-unmerged source is
imported. All load-bearing carrier, covariance, exact-menu, and atomic-law
arithmetic is rederived in this source and runner. The canonical axiom memo
remains unchanged. Independent audit is required before any effective status
changes. The authoring statement that no self-review occurred is preserved
only as submission history; this repaired candidate has undergone repo-native
review-loop review.
