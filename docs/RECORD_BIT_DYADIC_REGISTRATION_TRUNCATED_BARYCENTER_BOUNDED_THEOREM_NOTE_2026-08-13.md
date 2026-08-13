---
claim_id: record_bit_dyadic_registration_truncated_barycenter_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Finite floor-difference registration on D×U_n with a uniform 2^{-n} truncation bound, a never-dyadic obstruction at 3/10, and an affine-versus-barycenter split; not a physical compiler and not an axiom edit"
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/record_bit_dyadic_registration_truncated_barycenter_2026_08_13.py
---

# Record-Bit Dyadic Registration And Truncated Barycenter On Finite Product Registers

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact floor-difference registration on the product of the one-site
density body with a finite dyadic register; uniform truncation; never-dyadic
obstruction at the declared biased Diracs; affine-versus-barycenter split at
finite resolution.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_bit_dyadic_registration_truncated_barycenter_2026_08_13.py`](../scripts/record_bit_dyadic_registration_truncated_barycenter_2026_08_13.py)

## Result Up Front

The August 10 type-separation note names a sufficient interface: registered
measurable partitions whose pushforward supplies a menu-independent effect
grade, and leaves a physical construction of those partitions open. This note
supplies a finite Record-typed product family `D×U_n` and a floor-difference
kernel on that family. It is a discrete replacement for a continuum `[0,1]`
factor, not a derivation of that factor from the four axioms.

1. **Floor-difference registration is a partition.** For each finite
   resolution `M` of `I` and each density `ρ`, the integer bins assigned by
   prefix-sum floors are pairwise disjoint, exhaust the finite register
   `U_n={0,...,2^n-1}`, and satisfy `Σ_i q_i(ρ)=2^n`. The product sets
   `A_n(i|M)` therefore partition `D×U_n` independently of any measure `μ`.
2. **Uniform truncation, with an exact / never-exact split.** For every
   `ρ∈D` and every menu member,
   `|q_i(ρ)/2^n - Tr(ρ E_i)| < 2^{-n}`. At `ρ=I/2` the shared pairing
   `Tr(ρ E_0)=1/4` is exact for every `n≥2`. At `ρ=diag(3/5,2/5)` the pairing
   `3/10` is never dyadic, so the truncated mass is never `3/10`. At
   `ρ=diag(4/5,1/5)` the pairing `2/5` is likewise never exact. Spectral
   endpoints of `E_0` are exact: `1/2` at `δ_{P(z)}` for `n≥1`, and `0` at
   `δ_{P(-z)}`.
3. **Finite-n obstruction (scoped negative).** There is no finite `n` such
   that the truncated `E_0` mass equals `Tr(ρ E_0)` at every declared Dirac
   `ρ∈{I/2, diag(3/5,2/5), diag(4/5,1/5)}` in both hostile menus. The mixed
   state is exact for `n≥2`; the two biased states never are.
4. **Affine in `μ`, not barycenter evaluation.** For
   `μ=(3/5)δ_{P(z)}+(2/5)δ_{P(-z)}`, the truncated kernel is the corresponding
   mixture of the atomic truncated masses. On `E_0` that mixture equals
   `3/10` exactly, while the single Dirac at the barycenter is not `3/10`.
   Finite-n floor registration is therefore affine in `μ` and is not a
   function of the barycenter alone. Continuum `n→∞` recovers barycenter
   evaluation uniformly at rate `2^{-n}`. Encoding `k∈U_n` as `n` binary
   Record bits on `n` auxiliary sites is a declared typing, not a physical
   menu compiler.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The current Record sentences are likewise quoted only as premises:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Floor-difference registration, the uniform 2^{-n} truncation bound, the 3/10 never-dyadic obstruction, and the affine-versus-barycenter split are proved by elementary floor arithmetic on declared one-site objects; physical independence and uniformity of Record bits remain open."
trace_class: direct_blocker_closure
target_claim_id: admissibility_distribution_to_effect_grade_bridge
target_blocker_text: "derive distribution-to-effect-grade identification/functionality and universal binary-and-ternary physical menu eligibility"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "A physical compiler that produces independent uniform Record bits, or a continuum factor, remains open; do not adopt axiom text."
conditional_surface_status: "exact for floor-difference registration on D×U_n and the finite-n obstruction at 3/10; physical bit independence/uniformity open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `D` be the `2x2` density body

`D={ρ∈M_2(C): ρ=ρ^†, ρ≥0, Tr(ρ)=1}`.

A finite-support probability on `D` is

`μ=Σ_k p_k δ_{ρ_k}`, `p_k>0`, `Σ_k p_k=1`, `ρ_k∈D`.

Its barycenter is `ρ_μ=Σ_k p_k ρ_k∈D`. Barycenter evaluation is the kernel

`w_μ(E)=Tr(ρ_μ E)`.

The finite register is the dyadic set

`U_n={0,1,...,2^n-1}`

with uniform counting measure `λ_n({k})=2^{-n}`. The product registration
space is `D×U_n`, equipped with the product of the Borel structure on `D` and
the discrete σ-algebra on `U_n`.

Write `P(n)=(I+n·σ)/2` for a unit Bloch vector `n`. The declared hostile menus
are those of
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md):

`E_0=(1/2)P(z)`,

`M_A=(E_0, (9/10)P(n_1), (3/5)P(n_2))` with
`n_1=(4√2/9,0,-7/9)` and `n_2=(-2√2/3,0,1/3)`,

`M_B=(E_0, (3/4)P(m_1), (3/4)P(m_2))` with
`m_1=(2√2/3,0,-1/3)` and `m_2=(-2√2/3,0,-1/3)`.

Each displayed vector is unit. Matrix addition gives `Σ M_A=I` and `Σ M_B=I`.
The five effects are pairwise distinct. Menus are ordered tuples: prefix
sums, and therefore the floor bins, depend on order. The shared effect `E_0`
is first in both declared menus.

For a finite menu `M=(E_1,...,E_r)` with `Σ_i E_i=I` and for `ρ∈D`, set

`S_0(ρ)=0`, `S_i(ρ)=Σ_{j=1}^{i} Tr(ρ E_j)` for `i=1,...,r`.

Because `Σ E_i=I` and `Tr(ρ)=1`, one has `S_r(ρ)=1`. The floor-difference
counts and product sets are

`q_i(ρ)=⌊2^n S_i(ρ)⌋-⌊2^n S_{i-1}(ρ)⌋`,

`A_n(i|M)={(ρ,k)∈D×U_n: ⌊2^n S_{i-1}(ρ)⌋ ≤ k < ⌊2^n S_i(ρ)⌋}`.

For finite-support `μ=Σ_k p_k δ_{ρ_k}`,

`(μ⊗λ_n)(A_n(i|M))=Σ_k p_k q_i(ρ_k)/2^n`.

Call this number `w_n(μ, E_i | M)`. The menu appears only through prefix
order. The continuum length of the fiber assigned to a fixed effect `E` at a
fixed `ρ` is always `Tr(ρ E)`, so the shared `E_0` pairing is
order-independent as a length. When `2^n Tr(ρ E)` is an integer, the
truncated mass of that increment is likewise order-independent and equals the
pairing. When the increment is not an integer, the truncated mass may depend
on the bin's placement among the prefix sums.

When `E_0` is first, `S_0=0` and `q_1(ρ)=⌊2^n Tr(ρ E_0)⌋`, so both declared
menus assign the same truncated `E_0` mass at every `ρ`.

The August 10 atomic restriction witness `ν` places mass proportional to
`(Tr E)^2` on the five distinct menu atoms. Its normalization is
`Z=509/200`, and

`K_ν(E_0|M_A)=25/142`, `K_ν(E_0|M_B)=2/11`,

with difference `-9/1562`. Restriction is a hostile control in this note, not
the constructed truncated kernel.

The parent
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
supplies uniqueness of a trace form once a menu-independent grade exists on
the full binary/ternary scaled family. The present note constructs a finite
product registration and a truncated kernel on the declared menus. It does
not rerun the frame lift.

A declared encoding of each `k∈U_n` as `n` binary Record bits on `n`
auxiliary sites is a typing of the discrete factor, not a derivation from
Admissibility or Record.

## Exact Target And Obligation Graph

**Exact target.** On the declared one-site objects, construct a μ-independent
finite product partition of `D×U_n` whose counting-measure pushforward
approximates barycenter evaluation uniformly; decide for which declared Diracs
the truncated `E_0` mass is exact; and record the finite-n obstruction and
the affine-versus-barycenter split.

| Obligation | Role | Disposition |
|---|---|---|
| define μ-independent sets `A_n(i|M)` on `D×U_n` | positive interface | Theorem 1 |
| prove `{A_n(i|M)}` partitions `D×U_n` and `Σ_i q_i=2^n` | partition | Theorem 1 |
| bound `|q_i/2^n-Tr(ρ E_i)|` uniformly | truncation | Theorem 2 |
| separate exact dyadic pairings from never-exact pairings | dichotomy | Theorem 3 |
| rule out one finite `n` exact at all three declared Diracs | scoped negative | Theorem 4 |
| compare mixture-of-endpoints to the Dirac at the barycenter | affine split | Theorem 5 |
| type `k∈U_n` as Record bits without claiming a compiler | residual | Theorem 6 |
| derive independent uniform bits, or a continuum factor, from the axioms | physical compiler | open |
| identify the event label with Record readout | content-only bridge | open; Record premises only quoted |

## Theorem 1 — Floor-Difference Registration Is A Partition

**Claim.** For every finite menu `M=(E_1,...,E_r)` with `Σ_i E_i=I`, every
`ρ∈D`, and every finite resolution `n≥1`, the integer sets

`K_i(ρ)={k∈U_n: ⌊2^n S_{i-1}(ρ)⌋ ≤ k < ⌊2^n S_i(ρ)⌋}`

are pairwise disjoint, their union is `U_n`, and `Σ_i q_i(ρ)=2^n`. Hence
`{A_n(i|M)}` is a μ-independent partition of `D×U_n`.

**Proof.** Each pairing `Tr(ρ E_j)` is nonnegative because each effect is
Hermitian with spectrum in `[0,1]` and `ρ` is a density. The prefix sums are
therefore nondecreasing, and

`S_r(ρ)=Σ_j Tr(ρ E_j)=Tr(ρ Σ_j E_j)=Tr(ρ I)=1`,

with `S_0(ρ)=0` by definition. The integers
`⌊2^n S_i(ρ)⌋` are likewise nondecreasing, start at `⌊0⌋=0`, and end at
`⌊2^n·1⌋=2^n`. Adjacent half-open integer intervals with those endpoints
partition `{0,1,...,2^n-1}`. Empty intervals occur precisely when
`q_i(ρ)=0` and do not disturb the partition. Summing telescopes:

`Σ_i q_i(ρ)=⌊2^n S_r(ρ)⌋-⌊2^n S_0(ρ)⌋=2^n`.

The product sets `A_n(i|M)` are the graphs of these integer bins over `D`.
They are pairwise disjoint because the bins are, and their union is `D×U_n`.
The definition uses only the menu matrices, the trace pairing at `ρ`, and
`n`. It does not mention `μ`.

## Theorem 2 — Uniform Truncation Bound

**Claim.** For every `ρ∈D`, every menu member, and every finite `n≥1`,

`|q_i(ρ)/2^n - Tr(ρ E_i)| < 2^{-n}`.

**Proof.** Set `a=2^n S_i(ρ)` and `b=2^n S_{i-1}(ρ)`, so
`a-b=2^n Tr(ρ E_i)` and `q_i(ρ)=⌊a⌋-⌊b⌋`. Write
`a=⌊a⌋+{a}` and `b=⌊b⌋+{b}` with fractional parts in `[0,1)`. Then

`(⌊a⌋-⌊b⌋)-(a-b)={b}-{a}`,

and `| {b}-{a} |<1`. Dividing by `2^n` gives the bound. Equality to the
pairing holds if and only if `{a}={b}`; in particular it holds whenever
`a` and `b` are integers, and, when the increment occupies an initial
prefix from `0`, if and only if `2^n Tr(ρ E_i)` is an integer.

## Theorem 3 — Exact Dyadic Cases Versus Never-Exact Cases

**Claim.** On the declared menus, with `E_0` first:

- At `ρ=I/2`, `Tr(ρ E_0)=1/4`. For every `n≥2` one has `2^n/4∈Z`, so
  `q_1(ρ)/2^n=1/4` exactly, in both menus. At `n=1`,
  `⌊2·(1/4)⌋/2=0≠1/4`.
- At `ρ=diag(3/5,2/5)`, `Tr(ρ E_0)=3/10`. For every finite `n≥1`,
  `2^n·3/10∉Z`, because a factor `5` remains in the denominator after all
  factors of `2` are cancelled. Therefore `q_1(ρ)/2^n≠3/10` for every
  finite `n`: the pairing `3/10` is never dyadic.
- At `ρ=diag(4/5,1/5)`, `Tr(ρ E_0)=2/5`. The same unique-factorization
  obstruction applies: `5` does not divide `2^{n+1}`, so `2^n·2/5∉Z` and
  the truncated mass is never `2/5`.
- Spectral endpoints of `E_0`: at `δ_{P(z)}` the pairing `1/2` is exact
  for every `n≥1`; at `δ_{P(-z)}` the pairing `0` is exact.

**Proof.** The pairings are matrix arithmetic:
`E_0=diag(1/2,0)`, so `Tr((I/2)E_0)=1/4`,
`Tr(diag(3/5,2/5)E_0)=3/10`, `Tr(diag(4/5,1/5)E_0)=2/5`,
`Tr(P(z)E_0)=1/2`, and `Tr(P(-z)E_0)=0`. With `E_0` first,
`q_1(ρ)=⌊2^n Tr(ρ E_0)⌋`. This equals `2^n Tr(ρ E_0)` if and only if the
scaled pairing is an integer. The integer claims are the dyadic statements
above. A rational in lowest terms is a dyadic rational only if its
denominator is a power of two; `3/10` is not a dyadic rational, and
`2/5` is not a dyadic rational, so neither can equal any mass `m/2^n`.

The same pairings hold in both hostile menus because they depend only on
`E_0`. Restriction values `25/142` and `2/11` are distinct from `1/4`,
`3/10`, and `2/5`.

## Theorem 4 — Finite-n Obstruction On The Declared Dirac Family

**Claim.** There is no finite `n` such that

`w_n(δ_ρ, E_0 | M)=Tr(ρ E_0)`

for every declared Dirac `ρ∈{I/2, diag(3/5,2/5), diag(4/5,1/5)}` and both
hostile menus `M∈{M_A,M_B}`.

**Proof.** By Theorem 3 the mixed state is exact for every `n≥2` and fails
at `n=1`. The two biased states fail for every finite `n`. Therefore no
single finite `n` can be exact at all three Diracs. The claim is a derived
no-go boundary inside the positive truncation theorem: it is not a no-go
against registration, against a continuum factor, or against a later
physical compiler.

**Scope.** The negative is restricted to exact equality of this truncated
kernel to the three declared pairings at finite `n`. It does not address
`n→∞`, a different Dirac family, a non-uniform measure on `U_n`,
μ-dependent bin edges, or a non-affine kernel.

## Theorem 5 — Mixture Identity For The Truncated Kernel

**Claim.** For `μ=(3/5)δ_{P(z)}+(2/5)δ_{P(-z)}` and every menu member,

`w_n(μ, E_i | M)=(3/5) q_i(P(z))/2^n + (2/5) q_i(P(-z))/2^n`.

This equals `Tr(ρ_μ E_i)` if and only if the truncation is exact at both
atoms. For the shared effect `E_0` the endpoints `1/2` and `0` are dyadic,
so the mixture equals `3/10` exactly. The single-Dirac value
`w_n(δ_{ρ_μ}, E_0 | M)` is not `3/10`.

**Proof.** The displayed mixture identity is the definition of
`(μ⊗λ_n)(A_n(i|M))` on a two-point first factor. At the atoms,
Theorem 3 gives `q_1(P(z))/2^n=1/2` and `q_1(P(-z))/2^n=0` for every
`n≥1`, hence

`w_n(μ, E_0 | M)=(3/5)·(1/2)+(2/5)·0=3/10=Tr(ρ_μ E_0)`,

with barycenter `ρ_μ=diag(3/5,2/5)`. The same barycenter, taken as a single
Dirac, is the never-dyadic case of Theorem 3, so
`w_n(δ_{ρ_μ}, E_0 | M)≠3/10`.

The split is load-bearing. The map `μ ↦ w_n(μ, E | M)` is affine in `μ`
because it is a mixture of the atomic truncated masses. It is not a function
of the barycenter `ρ_μ` alone at finite `n` for non-dyadic pairings:
`w_n(μ, E_0 | M)≠w_n(δ_{ρ_μ}, E_0 | M)`. Continuum barycenter evaluation
`w_μ(E)=Tr(ρ_μ E)` is a function of `ρ_μ` only. Finite-n floor registration
is therefore affine in `μ` and is not barycenter evaluation. Theorem 2
recovers barycenter evaluation uniformly as `n→∞` at rate `2^{-n}`.

## Theorem 6 — Record Typing Residual

**Claim.** A declared encoding of each register point `k∈U_n` as `n` binary
Record bits on `n` auxiliary sites is a typing of the discrete factor, not a
derivation that those bits are independent of `ρ` or uniformly distributed.

**Premises used (quoted only).**

- "When present, a record locks exactly one admissible local possibility."
- "A readout value is determined by record content alone."
- "For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`."

**Residual.** Content-only readout and finite additivity permit a scalar
reading of `n` disjoint one-bit records, and the lock sentence permits each
bit to lock one admissible local possibility. They do not force the joint
law of those bits to be the uniform counting measure `λ_n`, and they do not
force that law to be independent of the system density `ρ`. The current
Admissibility sentence says that the distribution over possibilities is
determined by nearest-neighbor conditions; if the auxiliary sites neighbor
the system site, dependence on `ρ` is not ruled out. This note does not
claim a physical menu compiler, does not claim that no compiler exists, and
does not propose axiom text.

## Hostile-Menu Controls

All identities below are recomputed from the declared matrices.

**Menu resolutions.** Both `M_A` and `M_B` sum to `I` by the parent Bloch
construction. Direct matrix addition confirms the same. Each member is a
scaled projector, and the five matrices are pairwise distinct.

**Restriction control.** On the five atoms,

`Z=Σ(Tr E)^2=1/4+81/100+9/25+9/16+9/16=509/200`,

`K_ν(E_0|M_A)=(1/4)/(1/4+81/100+9/25)=25/142`,

`K_ν(E_0|M_B)=(1/4)/(1/4+9/16+9/16)=2/11`,

difference `-9/1562`.

**Truncated `E_0` versus restriction.** At `I/2` and `n≥2` the truncated
mass is exactly `1/4` in both menus. The values `1/4`, `3/10`, and `2/5`
are distinct from both `25/142` and `2/11`. Replacing the constructed
function by restriction therefore cannot satisfy the mixed-state identity
gate.

**Order as length.** Reversing `M_A` moves the placement of the `E_0`
increment among the prefix sums. The continuum length remains `Tr(ρ E_0)`.
When that scaled pairing is an integer, the truncated mass is likewise
unchanged.

## Boundary And Non-Claims

- No axiom sentence is edited. The Admissibility distribution sentence and
  the Record lock, content-only, and additivity sentences are quoted only as
  premises.
- The discrete factor `U_n` is a declared registration coordinate. It is not
  derived from the four axioms, not a new primitive of the axiom surface, and
  not an axiom edit.
- This note is not a physical menu compiler, not a formation site or rate,
  and not a Record-content identification of the event label.
- Finite-n floor registration is not barycenter evaluation. The continuum
  comparison is an approximation bound, not an executed continuum
  construction.
- Partitions are not unique: reorderings and null modifications of empty
  bins give other families with the same counting masses when increments are
  integral, and possibly different masses otherwise.
- Non-affine kernels remain live. Theorem 4 does not address them.
- Independent audit is required. This note authors no audit verdict.
- Status prose is bounded-support / bounded_theorem only. No broader surface
  status is asserted.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | exact semantic baseline | supplied; no edit |
| August 10 type-separation note | hostile menus, restriction witness, partition interface left open | parent dependency |
| August 9 frame-lift note | menu-independent trace-form target | parent dependency |
| floor arithmetic and dyadic rationals | Theorems 2--4 | definition-level mathematics |
| product measure `μ⊗λ_n` and floor-difference bins | Theorems 1, 5 | constructed here |
| finite-support barycenter evaluation `Tr(ρ_μ E)` | comparison target | parent kernel; not equal to `w_n` at finite `n` on non-dyadic pairings |
| physical bit compiler | independent uniform Record bits, or a continuum factor | open |
| content-only event-label bridge | physical Record readout | open |
| observed probabilities, frequencies, fits | none | not used |

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | August 10 states that the strongest missing lemma is "a physical construction that produces registered measurable event partitions" from Record and Admissibility structure, and leaves that construction open. This note supplies a finite Record-typed product family `D×U_n` together with the exact truncation bound and the never-dyadic obstruction. It does not claim that the upstream interface is unratified. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git ls-tree` / `git grep` for dyadic registration, truncated barycenter, unit-interval ancilla, product registration, and registration coordinate. Hits: the August 10 type-separation note names the registered-partition interface and leaves construction open; the universal-QG barycentric-dyadic notes are a different object (refinement nets on `PL S^3×R`); the formation-gate "registration coordinate" is a different object (the grain `(w,1-w)`). No landed floor-difference kernel on the August 10 menus appears on that commit. Unmerged pull requests 6160–6163 construct continuum product partitions and kernels; they are not on `origin/main` and are not premises. The discrete `U_n` construction, the `3/10` never-dyadic obstruction, and the affine-but-not-barycentric split are new. |
| V3 | Independently checkable? | Textbook floor functions do not mention the August 10 menus, the restriction pair `25/142` versus `2/11`, or the `3/10` never-dyadic obstruction on those states. The runner recomputes menus, restriction, floor-difference masses, and the mixture split in exact `Q(√2)` arithmetic. |
| V4 | More than a restatement? | Yes. The exact `1/4` versus `3/10` dichotomy, and the split in which the mixture of endpoints equals `3/10` while the Dirac at the barycenter does not, are not restatements of the parent type-separation or of the parent grade. |
| V5 | One-step relabel? | No. The claim is not a corollary of August 10 (negative type-separation) or August 9 (grade granted). The closest landed wording is the August 10 hypothetical partition interface. The closest unmerged comparison is a continuum factor `D×[0,1]`; the present object is a finite discrete replacement with a new non-barycentric split. |

## No-Go Discipline Gate (Theorem 4 only)

The negative claim is restricted to exact equality of the truncated `E_0`
mass to `Tr(ρ E_0)` at all three declared Diracs for one finite `n`. The
gate does not ship a global non-derivability theorem.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| finite-n floor registration | require `w_n(δ_ρ,E_0\|M)=Tr(ρ E_0)` at all three declared Diracs | Theorem 4: `1/4` is exact only for `n≥2`; `3/10` and `2/5` are never dyadic | **ATTEMPTED** |
| `n=∞` / continuum Lebesgue factor | replace `U_n` by `[0,1]` with Lebesgue measure | an escape from the finite-n claim, not a counterexample to it | **ATTEMPTED** (escape) |
| shrink the Dirac family to dyadic pairings | keep only `I/2` and the spectral endpoints | a different claim; the declared family includes `3/10` | **ATTEMPTED** |
| non-uniform `λ_n` | change the counting weights on `U_n` | a different measure; masses need not lie in `2^{-n}Z` | **ATTEMPTED** |
| μ-dependent bin edges | let the partition depend on `μ` rather than only on `ρ` and `M` | a different object; Theorem 4 is about the constructed μ-independent bins | **ATTEMPTED** |
| one-site Hermitian content as `U_n` | identify register points with on-site matrix entries | typing residual (Theorem 6), not an exact-equality repair of Theorem 4 | **ATTEMPTED** |
| treat `3/10` as a dyadic rational | assert `2^n·3/10∈Z` for some finite `n` | forbidden by unique factorization: `5` does not divide `2^n·3` | **RULED OUT BY PRIOR** |

### N2 — wall independence

Theorem 4 closes only exact finite-n equality on the declared Dirac family
for this truncated kernel. It does not close continuum lifts, non-affine
kernels, a physical bit compiler, or a content-only event-label bridge.
Those walls remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `D`, `U_n`, `D×U_n` | declared mathematical domains |
| floor-difference bins | explicit construction |
| declared Dirac family | explicit hypothesis of Theorem 4 |
| August 10 menus | declared finite hostile family |
| uniform `λ_n` | declared counting measure |
| physical bit compiler | open; not assumed |
| continuum factor | live escape; not executed here |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility distribution sentence; Record lock, content-only, and additivity sentences | quoted as premises only; no edit |
| August 10 type-separation note | hostile menus, restriction numbers, registered-partition interface left open | parent dependency; finite registration constructed here |
| August 9 frame-lift note | menu-independent trace-form target | not re-proved; not a premise of Theorem 4 |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | `E_0` and the remaining declared menu members at named Diracs | no classification of every map from measures to effects |
| per site | one `M_2(C)` density body times `U_n` | no composite theorem |
| per mode | prefix-sum floor bins on the declared menus | no spectral/harmonic mode exhaustion |
| per block | finite-n exact-equality obstruction only | no dynamics, formation rate, or Record identification |
| lattice-wide | checked and not executed | no lattice-wide no-go |

The obstruction is per-Dirac / one-site / declared menus; it is not
lattice-wide.

### N6 — live partial-closure paths

1. The continuum limit `n→∞`, or an explicit Lebesgue factor, recovering
   barycenter evaluation uniformly at rate `2^{-n}`.
2. Non-affine kernels outside barycenter evaluation.
3. A physical compiler that produces independent uniform Record bits from
   Record and Admissibility structure.
4. A content-only bridge from the mathematical event label to Record
   readout.

No axiom sentence is required by the finite-n obstruction. Those four paths
remain live.

### N7 — hostile steelman

> Use only states whose pairings are dyadic, or take `n` large enough that
> `2^{-n}` is smaller than any physical distinction. Then Theorem 4 is an
> artifact of an unphysical exact-equality demand.

**Answer.** Theorem 2 already grants the approximation bound. Theorem 4 is
exact equality on the declared finite Dirac family, which includes the
never-dyadic pairing `3/10`. Changing the family, or replacing equality by
an approximation, is a different claim.

### N8 — cross-cycle echo

August 10 Theorems 1--3 are the parent negatives (singleton mass, atomless
restriction, contextual restriction). The present negative is a different
residual: this truncated kernel cannot be exact at all three declared Diracs
for any finite `n`. The positive construction does not cancel the parent
negatives; it answers the open partition interface those negatives
motivated, inside a finite discrete replacement.

**Gate disposition.** PASS for the scoped finite-n exact-equality
obstruction. FAIL / DO NOT SHIP for "no registration exists", "the axioms
cannot supply bits", or "continuum is impossible".

## Primary Runner

[`scripts/record_bit_dyadic_registration_truncated_barycenter_2026_08_13.py`](../scripts/record_bit_dyadic_registration_truncated_barycenter_2026_08_13.py)
recomputes the floor-difference partition, the uniform truncation bound, the
exact-versus-never-dyadic dichotomy, the finite-n obstruction, the mixture
split, and the hostile-menu controls, all in exact `Q(√2)` arithmetic.
Identity gates call `floor_diff_mass` and `truncated_pushforward`; replacing
either by restriction `25/142` or by raw `Tr(ρ E)` must fail those checks.
Executed depths are `n=1` (the mixed quarter is not exact) and `n=3` (the
mixed quarter is exact and `3/10` is not), with `n=2` included as a cheap
witness that `1/4` becomes exact at the first dyadic threshold.
