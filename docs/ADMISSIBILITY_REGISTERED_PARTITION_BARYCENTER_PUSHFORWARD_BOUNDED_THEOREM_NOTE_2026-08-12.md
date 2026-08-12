---
claim_id: admissibility_registered_partition_barycenter_pushforward_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "Dirac obstruction on D/X plus explicit product partitions of D×[0,1] whose pushforward of finite-support μ is Tr(ρ_μ E); not a physical compiler, not an axiom edit"
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py
---

# Registered Partitions That Push Finite-Support Measures To Barycenter Evaluation

**Date:** 2026-08-12
**Type:** bounded_theorem
**Scope:** exact Dirac obstruction for μ-independent measurable partitions of
the density body or of `M_2(C)`, together with an explicit product
registration on `D×[0,1]` whose pushforward of every finite-support measure
equals barycenter evaluation on the August 10 hostile menus.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py`](../scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py)

## Result Up Front

The August 10 type-separation note names a sufficient interface: registered
measurable partitions whose pushforward supplies a menu-independent effect
grade. This note constructs that interface on a declared product lift and
records a scoped obstruction that forces the lift for atomic measures.

1. **Dirac obstruction (scoped negative).** There is no family of
   μ-independent measurable subsets `A(i|M)` of the density body `D`, or of
   the current possibility domain `X=M_2(C)`, such that for every Dirac
   `μ=δ_ρ` one has `μ(A(i|M))=Tr(ρ E_i)` on the August 10 menus. Dirac measure
   of a measurable set is in `{0,1}`, while `Tr((I/2)E_0)=1/4∉{0,1}` and
   `Tr(diag(3/5,2/5) E_0)=3/10∉{0,1}`. Raw atomic Admissibility mass on `D`
   (or on `X` with support in `D`) cannot be pushed by a partition of that
   space to the barycenter kernel.
2. **Product registration is a partition.** On `Y=D×[0,1]`, the cumulative
   interval sets `A(i|M)` built from prefix sums of `Tr(ρ E_j)` are pairwise
   disjoint, cover `Y`, and do not depend on `μ`.
3. **Pushforward equals the barycenter kernel.** For every finite-support
   `μ=Σ_k p_k δ_{ρ_k}` on `D` and Lebesgue measure `λ` on `[0,1]`,
   `(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i)=w_μ(E_i)`. The identity is exact finite
   arithmetic. The set `A` depends on `M`, but the pushforward of the shared
   effect `E_0` is the same number in both hostile menus.
4. **Hostile-menu identities recomputed.** On the August 10 menus the
   pushforward of `E_0` is `1/4` at `I/2`, `3/10` at `diag(3/5,2/5)`, and
   `2/5` at `diag(4/5,1/5)`, in both menus; each menu normalizes; these values
   disagree with restriction `25/142` and `2/11`; spectral endpoints of `E_0`
   are `1/2` and `0`; reordering a menu moves the `E_0` interval without
   changing its Lebesgue length.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The current Record content-only sentence is likewise quoted only as a premise:

A readout value is determined by record content alone.

The product factor `[0,1]` is a declared registration coordinate. It is not
derived from the four axioms, not a primitive of the axiom surface, and not a
physical menu compiler.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Dirac obstruction on D/X and the product-partition pushforward identity are proved by elementary measure and finite-arithmetic steps on declared one-site objects; physical derivation of the registration coordinate from Record and Admissibility structure remains open."
trace_class: direct_blocker_closure
target_claim_id: admissibility_distribution_to_effect_grade_bridge
target_blocker_text: "derive distribution-to-effect-grade identification/functionality and universal binary-and-ternary physical menu eligibility"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "A physical compiler that produces the product registration from Record and Admissibility structure remains open; do not adopt axiom text."
conditional_surface_status: "exact for the Dirac obstruction and the declared product pushforward on finite-support measures and the Aug 10 menus; physical registration remains open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `D` be the `2x2` density body

`D={ρ∈M_2(C): ρ=ρ^†, ρ≥0, Tr(ρ)=1}`.

Write `X=M_2(C)` for the current one-site possibility domain. A finite-support
probability on `D` is

`μ=Σ_k p_k δ_{ρ_k}`, `p_k>0`, `Σ_k p_k=1`, `ρ_k∈D`.

Its barycenter is `ρ_μ=Σ_k p_k ρ_k∈D`. Barycenter evaluation is the kernel

`w_μ(E)=Tr(ρ_μ E)`.

The product registration space is

`Y=D×[0,1]`

with the product σ-algebra of the Borel structure on `D` and Lebesgue
measurable sets on `[0,1]`. Let `λ` denote Lebesgue measure on `[0,1]`.

Write `P(n)=(I+n·σ)/2` for a unit Bloch vector `n`. The declared hostile menus
are those of
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md):

`E_0=(1/2)P(z)`,

`M_A=(E_0, (9/10)P(n_1), (3/5)P(n_2))` with
`n_1=(4√2/9,0,-7/9)` and `n_2=(-2√2/3,0,1/3)`,

`M_B=(E_0, (3/4)P(m_1), (3/4)P(m_2))` with
`m_1=(2√2/3,0,-1/3)` and `m_2=(-2√2/3,0,-1/3)`.

Each displayed vector is unit. Matrix addition gives `Σ M_A=I` and `Σ M_B=I`.
The five effects are pairwise distinct. Parenthetical aliases: the first
remaining `M_A` effect is `(9/10)P(n_1)`; the second remaining `M_A` effect is
`(3/5)P(n_2)`; the two remaining `M_B` effects are the equal-coefficient pair
`(3/4)P(m_1)` and `(3/4)P(m_2)`.

For a finite menu `M=(E_1,...,E_r)` with `Σ_i E_i=I` and for `ρ∈D`, set

`S_0(ρ)=0`, `S_i(ρ)=Σ_{j=1}^{i} Tr(ρ E_j)` for `i=1,...,r`.

Because `Σ E_i=I` and `Tr(ρ)=1`, one has `S_r(ρ)=1`. Define

`A(i|M)={(ρ,t)∈Y: S_{i-1}(ρ) ≤ t < S_i(ρ)}`

for `i=1,...,r-1`, and close the last interval on the right at `t=1` if desired
(the singleton `{t=1}` is Lebesgue-null). These sets depend on `M` and on the
trace pairing, not on a choice of measure `μ`.

The August 10 atomic restriction witness `ν` places mass proportional to
`(Tr E)^2` on the five distinct menu atoms. Its normalization is
`Z=509/200`, and

`K_ν(E_0|M_A)=25/142`, `K_ν(E_0|M_B)=2/11`,

with difference `-9/1562`. Restriction is a hostile control in this note, not
the constructed pushforward.

Optional embedding remark (not a numbered theorem). The map

`ι(ρ,t)=ρ + i(t-1/2)I`

injects `Y` into `X`. The same partition sets may therefore be viewed as
subsets of `X` after this declared lift. The lift is essential: without it
Theorem 1 applies. This note does not claim that the embedding is physical,
and does not identify the imaginary-multiple-of-identity coordinate with any
menu-label encoding.

The parent
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
supplies uniqueness of a trace form once a menu-independent grade exists on
the full binary/ternary scaled family. The present note constructs registered
partitions that push finite-support measures to that grade on the declared
menus. It does not rerun the frame lift.

## Exact Target And Obligation Graph

**Exact target.** On the declared one-site objects, decide whether a
μ-independent measurable partition of `D` or of `X` can realize the
barycenter kernel on Dirac measures; if not, construct an explicit
μ-independent product partition of a declared lift whose pushforward equals
barycenter evaluation on every finite-support measure and on the August 10
menus.

| Obligation | Role | Disposition |
|---|---|---|
| rule out μ-independent partitions of `D` realizing fractional Dirac grades | Dirac obstruction | Theorem 1 |
| rule out the same construction on `X` with support in `D` | Dirac obstruction | Theorem 1 |
| define μ-independent measurable sets `A(i|M)` on a declared lift | positive interface | Theorem 2 |
| prove `(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i)` for finite-support `μ` | pushforward identity | Theorem 3 |
| recompute hostile-menu numbers against restriction | control identities | Theorem 4 |
| derive the registration coordinate from Record/Admissibility structure | physical compiler | open |
| identify the event label with Record readout | content-only bridge | open; Record premise only quoted |

## Theorem 1 — Dirac Obstruction On Atomic Support

**Claim.** There is no family of μ-independent measurable subsets
`A(i|M)⊂D`, or `A(i|M)⊂X`, such that for every Dirac probability `μ=δ_ρ` on
`D` one has

`μ(A(i|M))=Tr(ρ E_i)`

for every member `E_i` of the August 10 menus `M_A` and `M_B`.

**Proof.** Let `A⊂D` be any measurable set that does not depend on the choice
of Dirac measure. For any `ρ∈D`,

`δ_ρ(A) ∈ {0,1}`,

because a Dirac measure evaluates the indicator of membership. Take
`ρ_*=I/2`. Matrix pairing gives

`Tr(ρ_* E_0)=Tr((I/2)·(1/2)P(z))=(1/2)·(1/2)=1/4`,

since `Tr(P(z))=1`. The value `1/4` is not in `{0,1}`. Therefore no single
measurable set `A` can satisfy `δ_{ρ_*}(A)=Tr(ρ_* E_0)`.

The same contradiction appears at the non-mixed state
`ρ=diag(3/5,2/5)`. Because `E_0=(1/2)P(z)=diag(1/2,0)`,

`Tr(ρ E_0)=(3/5)·(1/2)=3/10 ∉ {0,1}`.

If the ambient space is enlarged from `D` to `X=M_2(C)` while the measures
remain Diracs supported on `D`, the same arithmetic applies: Dirac measure of
any measurable subset of `X` is still in `{0,1}` at those points. Hence no
μ-independent measurable partition of `D` or of `X` pushes every Dirac on `D`
to the barycenter kernel on the declared menus.

**Scope.** This is a scoped negative only. It is not a no-go against product
lifts, fiber lifts, non-atomic measures, μ-dependent constructions that change
the measure, or non-affine kernels. In particular it does not address the
product construction of Theorems 2--3, which changes the measure from `μ` on
`D` to `μ⊗λ` on `Y`.

## Theorem 2 — Product Registration Is A Partition

**Claim.** For every finite menu `M=(E_1,...,E_r)` with `Σ_i E_i=I`, the sets
`A(i|M)` defined above are pairwise disjoint, their union is `Y`, and they do
not depend on any choice of measure `μ`.

**Proof.** Fix `ρ∈D`. The numbers `S_i(ρ)` are nondecreasing because each
`Tr(ρ E_j)≥0` for effects (Hermitian, spectrum in `[0,1]`). Moreover

`S_r(ρ)=Σ_{j=1}^{r} Tr(ρ E_j)=Tr(ρ Σ_j E_j)=Tr(ρ I)=1`,

and `S_0(ρ)=0` by definition. Therefore the half-open intervals

`[S_{0}(ρ),S_1(ρ)), ..., [S_{r-1}(ρ),S_r(ρ))`

(with the last right endpoint closed at `1` if preferred) form a partition of
`[0,1]` up to the null singleton `{1}`. The product sets

`A(i|M)={ρ}×[S_{i-1}(ρ),S_i(ρ))` (fiberwise)

are pairwise disjoint because the intervals are, and their union over `i` is
`{ρ}×[0,1]` (up to null points). Varying `ρ` over `D` gives a partition of
`Y`. The definition uses only the menu matrices and the trace pairing at `ρ`;
it does not mention `μ`.

## Theorem 3 — Pushforward Equals The Barycenter Kernel

**Claim.** For every finite-support probability `μ=Σ_k p_k δ_{ρ_k}` on `D`,
every finite resolution `M=(E_1,...,E_r)` of `I`, and every index `i`,

`(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i)=w_μ(E_i)`.

**Proof.** By definition of product measure for a finite atomic first factor,

`(μ⊗λ)(A(i|M))=Σ_k p_k λ({t∈[0,1]: S_{i-1}(ρ_k) ≤ t < S_i(ρ_k)})`.

Each fiber set is an interval of length

`S_i(ρ_k)-S_{i-1}(ρ_k)=Tr(ρ_k E_i)`,

so

`(μ⊗λ)(A(i|M))=Σ_k p_k Tr(ρ_k E_i)=Tr((Σ_k p_k ρ_k) E_i)=Tr(ρ_μ E_i)`.

The identity is exact finite arithmetic, not an approximation. Menu
independence on a shared effect follows at once: the set `A(i|M)` depends on
which menu contains the effect and on the ordering of the other members, but
the Lebesgue length of the fiber assigned to a fixed effect `E` at a fixed
`ρ` is always `Tr(ρ E)`. Consequently the pushforward of `E_0` is
`Tr(ρ_μ E_0)` in both `M_A` and `M_B`.

## Theorem 4 — Hostile-Menu Identities Recomputed

All identities below are recomputed from the declared matrices; none is
imported as an un-checked number.

**Menu resolutions.** Both `M_A` and `M_B` sum to `I` by the parent Bloch
construction (scalar coefficients sum to two; coefficient-weighted Bloch
vectors sum to zero). Direct matrix addition confirms the same. Each member
is a scaled projector, and the five matrices are pairwise distinct.

**Restriction control.** On the five atoms,

`Z=Σ(Tr E)^2=1/4+81/100+9/25+9/16+9/16=509/200`,

`K_ν(E_0|M_A)=(1/4)/(1/4+81/100+9/25)=25/142`,

`K_ν(E_0|M_B)=(1/4)/(1/4+9/16+9/16)=2/11`,

difference `-9/1562`.

**Mixed state.** At `ρ_*=I/2`, fiber length of `E_0` is
`Tr((I/2)E_0)=1/4` in both menus. Summing fiber lengths over each menu
returns `1`.

**Biased states.** At `ρ=diag(3/5,2/5)`, the `E_0` length is `3/10` in both
menus. At `ρ'=diag(4/5,1/5)`, the `E_0` length is `2/5` in both menus. Both
menus normalize at each of these states.

**Disagreement with restriction.** The values `1/4`, `3/10`, and `2/5` are
distinct from both `25/142` and `2/11`.

**Spectral endpoints.** At `δ_{P(z)}`, the `E_0` interval has length
`Tr(P(z)E_0)=1/2`. At `δ_{P(-z)}`, the length is `0`.

**Order independence of lengths.** Reversing the order of `M_A` moves the
placement of the `E_0` interval among the prefix sums, but the multiset of the
three fiber lengths is unchanged, and the `E_0` length remains `Tr(ρ E_0)`.

**Mixture equals barycenter.** For the two-point law
`μ=(3/5)δ_{P(z)}+(2/5)δ_{P(-z)}`, Theorem 3 gives

`(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i)`

on every member of both menus, with barycenter `ρ_μ=diag(3/5,2/5)`.

## Boundary And Non-Claims

- No axiom sentence is edited. The Admissibility distribution sentence and the
  Record content-only sentence are quoted only as premises.
- The extra `[0,1]` factor is a declared registration coordinate. It is not
  derived from the four axioms, not a new primitive of the axiom surface, and
  not an axiom edit.
- This note is not a physical menu compiler, not a formation site or rate, and
  not a Record-content identification of the event label.
- Partitions are not unique: reorderings and null modifications give other
  families with the same pushforward lengths.
- Non-affine kernels remain live. Theorem 1 does not address them.
- Independent audit is required. This note authors no audit verdict.
- Status prose is bounded-support / bounded_theorem only. No broader surface
  status is asserted.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | exact semantic baseline | supplied; no edit |
| August 10 type-separation note | hostile menus, restriction witness, partition interface | parent dependency |
| August 9 frame-lift note | menu-independent trace-form target | parent dependency |
| Dirac measure range `{0,1}` | Theorem 1 | definition-level mathematics |
| product measure `μ⊗λ` and fiber Lebesgue length | Theorems 2--3 | constructed here |
| finite-support barycenter evaluation `Tr(ρ_μ E)` | pushforward target | constructed as the image of the partition |
| physical registration compiler | derivation of `[0,1]` from Record/Admissibility | open |
| content-only event-label bridge | physical Record readout | open |
| observed probabilities, frequencies, fits | none | not used |

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | August 10 named registered measurable partitions as a sufficient interface and left their construction open. This note supplies an explicit product family whose pushforward is barycenter evaluation, and records the Dirac obstruction that forces a lift for atomic measures. |
| V2 | New content? | Searched `origin/main` at `c820f8e38f` by `git grep` for registered event partition / pushforward / barycenter. Only the August 10 type-separation note names the registered-partition interface and leaves it open; no landed construction of `A(i|M)` with `(μ⊗λ)(A)=Tr(ρ_μ E)` appears on that commit. Flavor/Koide notes that use the word "partition" concern different objects. The Dirac obstruction, product registration, and finite-support pushforward identity are new on this surface. |
| V3 | Independently checkable? | Yes. The runner recomputes menu sums, restriction weights, fiber lengths, pushforwards, spectral endpoints, order independence, and the Dirac range contradiction from the matrices in exact `Q(√2)` arithmetic. |
| V4 | More than a restatement? | Yes. The parents separate types and name a sufficient interface; this note constructs the partitions and proves the pushforward identity on finite-support measures. |
| V5 | One-step relabel? | No. Naming the interface and naming barycenter evaluation do not by themselves produce measurable sets `A(i|M)` or the product measure identity. |

## No-Go Discipline Gate (Theorem 1 only)

The negative claim is restricted to μ-independent measurable partitions of
`D` or of `X` realizing fractional Dirac grades on the declared menus. The
gate does not ship a global non-derivability theorem.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| μ-independent partition of `D` | require `δ_ρ(A(i|M))=Tr(ρ E_i)` for all Diracs | Theorem 1: Dirac values in `{0,1}`, while `1/4` and `3/10` are not | **ATTEMPTED** |
| μ-independent partition of `X` with support in `D` | same equality with ambient space `X` | same `{0,1}` contradiction at the same Diracs | **ATTEMPTED** |
| fractional Dirac mass at a boundary point | assign mass `1/4` to a single point by altering Dirac axioms | forbidden by the definition of a probability measure / Dirac measure | **RULED OUT BY PRIOR** |
| μ-dependent partitions of `D` | allow `A` to depend on `μ` while still evaluating Diracs as set-membership | each single Dirac still returns `{0,1}` for any fixed measurable set | **ATTEMPTED** |
| product `Y=D×[0,1]` with `μ⊗λ` | change the measure by a Lebesgue fiber | escapes the obstruction; this is the positive construction of Theorems 2--3, not a counterexample to the scoped no-go | **ATTEMPTED** (escape) |
| Naimark PVM on a dilation with Dirac on the dilated density | evaluate set-measure of a dilated atomic support | set-measure remains `{0,1}`; the Born number is the kernel itself, not a partition of the atomic support | **ATTEMPTED** |
| effect-valued / POVM-as-partition | treat POVM elements as the partition | different type: POVM elements are operators, not a measurable-set partition of `D` or `X` | **ATTEMPTED** |

### N2 — wall independence

Theorem 1 closes only the atomic-support partition route on `D`/`X`. It does
not close product lifts, non-atomic measures, non-affine kernels, or a
physical compiler. Those walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `D`, `X`, `Y` | declared mathematical domains |
| μ-independent measurable set | explicit hypothesis of Theorem 1 |
| Dirac range `{0,1}` | definition of Dirac measure |
| August 10 menus | declared finite hostile family |
| product registration coordinate `[0,1]` | declared lift for the positive construction; not current axiom content |
| physical menu compiler | open; not assumed |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility distribution sentence; Record content-only sentence | quoted as premises only; no edit |
| August 10 type-separation note | hostile menus, restriction numbers, registered-partition interface left open | parent dependency; partitions constructed here |
| August 9 frame-lift note | menu-independent trace-form target | not re-proved; not a premise of Theorem 1 |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | `E_0` and the remaining declared menu members at named Diracs | no classification of every map from measures to effects |
| per site | one `M_2(C)` site / one density body | no composite theorem |
| per mode | declared menus and the product fiber coordinate | no spectral/harmonic mode exhaustion |
| per block | atomic-support partition obstruction only | no dynamics, formation rate, or Record identification |
| lattice-wide | checked and not executed | no lattice-wide no-go |

The obstruction is per-Dirac / one-site / declared menus; it is not
lattice-wide.

### N6 — live partial-closure paths

1. Product (or other fiber) lifts with non-atomic second factors, as in
   Theorems 2--3.
2. Non-atomic measures on `D` or on `X` for which measurable sets of any
   prescribed measure exist.
3. Non-affine kernels outside barycenter evaluation.
4. A physical compiler that produces a registration coordinate from Record and
   Admissibility structure.
5. A content-only bridge from the mathematical event label to Record readout.

### N7 — hostile steelman

> August 10 already allowed the registered sets `A_η` to depend on the
> preparation condition `η`, and a non-atomic measure `μ_η` can always be split
> into measurable sets of any prescribed measures. Therefore Theorem 1 is
> empty: one can always find some sets realizing the Born numbers.

**Answer.** Theorem 1 is exactly about atomic-on-`D` measures and about
μ-independent set families evaluated as Dirac set-membership. Existence of
some measurable sets for one fixed non-atomic measure is not a registered
kernel construction: it does not supply a single family `A(i|M)` that works
uniformly for every Dirac and yields the barycenter kernel by pushforward.
The product construction of Theorems 2--3 is the explicit η-independent
family that works after the declared lift.

### N8 — cross-cycle echo

August 10 Theorems 1--3 are the parent negatives (singleton mass, atomless
restriction, contextual restriction). The present negative is a different
residual: partitions of the atomic support cannot realize a fractional grade.
The positive construction does not cancel the parent negatives; it answers the
open partition interface those negatives motivated.

**Gate disposition.** PASS for the scoped Dirac obstruction on μ-independent
partitions of `D`/`X`. FAIL / DO NOT SHIP for "no partition of any space can
realize Born numbers," "product lifts fail," "non-affine kernels fail," or
"the four axioms cannot supply a physical registration."

## Primary Runner

[`scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py`](../scripts/admissibility_registered_partition_barycenter_pushforward_2026_08_12.py)
recomputes the Dirac obstruction, the product partition cover, the
finite-support pushforward identity, the hostile-menu controls, spectral
endpoints, order independence, and a finite injectivity sample for the
optional embedding, all in exact `Q(√2)` arithmetic. Identity gates call the
constructed fiber length and pushforward; replacing either by restriction
must fail the checks.
