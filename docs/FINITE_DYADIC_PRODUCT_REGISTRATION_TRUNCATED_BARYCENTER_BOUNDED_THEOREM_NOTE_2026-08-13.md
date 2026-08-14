---
claim_id: finite_dyadic_product_registration_truncated_barycenter_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Finite floor-difference product registration on D×U_n with a uniform 2^{-n} truncation bound, an exact non-dyadic image exclusion at 3/10 and 2/5, and an affine-versus-barycenter split; not a physical compiler, Record readout, or axiom edit"
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
  - admissibility_barycenter_evaluation_menu_kernel_bounded_theorem_note_2026-08-12
  - admissibility_registered_partition_barycenter_pushforward_bounded_theorem_note_2026-08-12
runner: scripts/finite_dyadic_product_registration_truncated_barycenter_2026_08_13.py
---

# Finite Dyadic Product Registration And Truncated Barycenter

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact floor-difference registration on the product of the one-site
density body with a finite dyadic register; uniform truncation; never-dyadic
obstruction at the declared biased Diracs; affine-versus-barycenter split at
finite resolution.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/finite_dyadic_product_registration_truncated_barycenter_2026_08_13.py`](../scripts/finite_dyadic_product_registration_truncated_barycenter_2026_08_13.py)

**Runner cache:**
[`logs/runner-cache/finite_dyadic_product_registration_truncated_barycenter_2026_08_13.txt`](../logs/runner-cache/finite_dyadic_product_registration_truncated_barycenter_2026_08_13.txt)

## Result Up Front

The August 12 registered-partition theorem gives an exact inverse-transform
construction on the declared product `D×[0,1]`. This note gives its finite
dyadic analogue on `D×U_n`. The finite construction is an explicit
approximation theorem on a newly supplied mathematical product law. It does
not derive an auxiliary register, its law, or a physical event compiler from
the four axioms.

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
3. **Finite dyadic image exclusion (scoped negative).** Every atomic mass of
   uniform counting measure on `U_n` lies in `2^{-n}Z`. Hence there is no
   finite `n` for which the truncated `E_0` mass equals `Tr(ρ E_0)` at every
   declared Dirac `ρ∈{I/2, diag(3/5,2/5), diag(4/5,1/5)}` in both hostile
   menus. The mixed state is exact for `n≥2`; the two biased states never are.
4. **Affine in `μ`, not barycenter evaluation.** For
   `μ=(3/5)δ_{P(z)}+(2/5)δ_{P(-z)}`, the truncated kernel is the corresponding
   mixture of the atomic truncated masses. On `E_0` that mixture equals
   `3/10` exactly, while the single Dirac at the barycenter is not `3/10`.
   Finite-n floor registration is therefore affine in `μ` and is not a
   function of the barycenter alone. For every finite-support `μ`, the
   continuum limit recovers barycenter evaluation uniformly at rate
   `2^{-n}`. The ordinary binary encoding of `k∈U_n` is mathematical data; no
   identification with formed records or physical readout is made.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The current Record sentences are likewise quoted only as a semantic boundary:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The current Record axiom supplies no named scalar functional, no additivity
law, and no readout value at absence. None is used below.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Floor-difference registration, the uniform 2^{-n} truncation bound, the 3/10 and 2/5 dyadic image exclusion, and the affine-versus-barycenter split are proved by elementary floor arithmetic on declared one-site objects; the auxiliary register law and every physical Record interpretation remain supplied or open."
trace_class: upstream_support
target_claim_id: admissibility_distribution_to_effect_grade_bridge
target_blocker_text: "derive an atom-splitting event registration from the actual Admissibility law on X and a content-only Record bridge"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "A physical compiler must derive an auxiliary atom-splitting law from the actual Admissibility law and connect event labels to Record content; this finite product theorem supplies neither bridge."
conditional_surface_status: "exact for floor-difference registration on D×U_n, the uniform error bound, and the finite dyadic image exclusion at 3/10 and 2/5; the auxiliary law and every physical Record interpretation remain open"
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

The barycenter-evaluation parent
[`ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md`](ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md)
supplies the exact comparison target `Tr(ρ_μE)`. The registered-partition
parent
[`ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md`](ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md)
supplies the continuum inverse-transform construction on `D×[0,1]`. The
present note discretizes that supplied second factor and quantifies exactly
what is lost at finite resolution.

Each `k∈U_n` has an ordinary `n`-bit binary encoding. This fact types the
finite set only. A physical interpretation would additionally require formed
auxiliary records, a selected pair of admissible contents at each site, and a
law that supplies the independent uniform register distribution. Those are
outside the theorem.

## Exact Target And Obligation Graph

**Exact target.** On the declared one-site objects, construct a μ-independent
finite product partition of `D×U_n` whose counting-measure pushforward
approximates barycenter evaluation uniformly; decide for which declared Diracs
the truncated `E_0` mass is exact; and record the finite dyadic image exclusion and
the affine-versus-barycenter split.

| Obligation | Role | Disposition |
|---|---|---|
| define μ-independent sets `A_n(i|M)` on `D×U_n` | positive interface | Theorem 1 |
| prove `{A_n(i|M)}` partitions `D×U_n` and `Σ_i q_i=2^n` | partition | Theorem 1 |
| bound `|q_i/2^n-Tr(ρ E_i)|` uniformly | truncation | Theorem 2 |
| separate exact dyadic pairings from never-exact pairings | dichotomy | Theorem 3 |
| characterize the dyadic image and rule out one finite `n` exact at all three declared Diracs | scoped negative | Theorem 4 |
| compare mixture-of-endpoints to the Dirac at the barycenter | affine split | Theorem 5 |
| encode `k∈U_n` as an ordinary binary word without physical interpretation | finite-set typing | boundary paragraph |
| derive an auxiliary atom-splitting register and its law from the axioms | physical compiler | open |
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

For fixed `k`, each membership condition is a finite conjunction of
inequalities involving the continuous functions `ρ↦Tr(ρE_j)` and integer
floors. Its preimage is Borel. Because `U_n` is finite and discrete, every
`A_n(i|M)` is therefore a Borel subset of `D×U_n`. The product sets are
pairwise disjoint because the integer bins are, and their union is `D×U_n`.
The definition uses only the menu matrices, the trace pairing at `ρ`, and
`n`; it does not mention `μ`.

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

If the truncation is exact at both atoms, this equals `Tr(ρ_μ E_i)`.
The converse is not needed and is not claimed: weighted truncation errors can
in principle cancel. For the shared effect `E_0` the endpoints `1/2` and `0`
are dyadic, so the mixture equals `3/10` exactly. The single-Dirac value
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
is therefore affine in `μ` and is not barycenter evaluation. For any
finite-support `μ=Σ_k p_kδ_{ρ_k}`, Theorem 2 and the triangle inequality give

`|w_n(μ,E_i|M)-Tr(ρ_μE_i)|`
`≤Σ_k p_k|q_i(ρ_k)/2^n-Tr(ρ_kE_i)|<2^{-n}`.

Thus the finite kernels converge uniformly to barycenter evaluation at rate
`2^{-n}` on the declared finite menus.

## Binary-Encoding Boundary

Every register point `k∈U_n` has an ordinary `n`-bit binary encoding. This
mathematical bijection does not identify those bits with formed records and
does not supply their physical law.

**Premises used (quoted only).**

- "When present, a record locks exactly one admissible local possibility."
- "A readout value is determined by record content alone."
- "A site with no record cannot be read."

The lock sentence allows one present record to carry one admissible local
possibility. It does not create `n` auxiliary records, select a binary content
pair at each one, or choose the uniform product law `λ_n`; the current Record
surface also contains no named scalar functional or finite-additivity rule.
This note claims no physical menu compiler, makes no claim that a compiler is
impossible, and proposes no axiom text.

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
  the current Record lock/content-only/unreadable-at-absence sentences are
  quoted only as a semantic boundary. No scalar readout functional,
  additivity rule, or value at absence is imported.
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

## Review Record

Review-loop repair of PR #6170 made four source-level corrections before
landing:

1. removed the retired scalar Record functional, finite-additivity rule, and
   value-at-absence premise, and renamed the package as a mathematical finite
   product construction rather than a Record-bit theorem;
2. rewired the construction to the landed August 12 barycenter and exact
   continuum registered-partition parents;
3. replaced direct-blocker-closure framing with upstream-support framing,
   because the auxiliary-register law and the Record event bridge remain open;
4. removed the unsupported converse that mixture equality would force atomic
   exactness, while retaining the proved forward implication and the exact
   `E_0` endpoint-mixture calculation.

The finite partition, error bound, dyadic image exclusion, and
affine-versus-barycenter split remain the reviewed theorem surface.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four-axiom surface | one-site possibility domain and semantic boundary | supplied; no edit; no scalar/additivity/absence-value premise |
| August 10 type-separation note | hostile menus, restriction witness, partition interface left open | parent dependency |
| August 12 barycenter-evaluation note | exact affine grade and restriction separation | direct parent dependency |
| August 12 registered-partition note | exact continuum inverse-transform cells on `D×[0,1]` | direct parent dependency discretized here |
| floor arithmetic and dyadic rationals | Theorems 2--4 | definition-level mathematics |
| product measure `μ⊗λ_n` and floor-difference bins | Theorems 1, 5 | constructed here |
| finite-support barycenter evaluation `Tr(ρ_μ E)` | comparison target | parent kernel; not equal to `w_n` at finite `n` on non-dyadic pairings |
| physical auxiliary-register compiler | formed auxiliary records, selected binary contents, and an independent uniform law | open |
| content-only event-label bridge | physical Record readout | open |
| observed probabilities, frequencies, fits | none | not used |

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The August 12 registered-partition parent supplies exact continuum inverse-transform cells on `D×[0,1]` while leaving the physical auxiliary law and Record bridge open. This note supplies a finite dyadic discretization, its exact error bound, and its image exclusion. It is upstream mathematical support and does not claim to close either physical bridge. |
| V2 | New content? | On reviewed main, the August 10 note names the interface, the barycenter parent constructs the effect grade, and the August 12 partition parent constructs exact continuum cells. None gives the finite floor-difference kernel on `D×U_n`, the `2^{-n}` bound, the `3/10`/`2/5` dyadic image exclusion, or the affine-but-not-barycentric finite-resolution split. The universal-QG barycentric-dyadic refinement nets are a different object on `PL S^3×R`. |
| V3 | Independently checkable? | Textbook floor functions do not mention the August 10 menus, the restriction pair `25/142` versus `2/11`, or the `3/10` never-dyadic obstruction on those states. The runner recomputes menus, restriction, floor-difference masses, and the mixture split in exact `Q(√2)` arithmetic. |
| V4 | More than a restatement? | Yes. The exact `1/4` versus `3/10` dichotomy, and the split in which the mixture of endpoints equals `3/10` while the Dirac at the barycenter does not, are not restatements of the parent type-separation or of the parent grade. |
| V5 | One-step relabel? | No. Discretizing the continuum inverse-transform cells introduces floor error and changes the finite kernel's factorization through the barycenter. The exact image exclusion and mixture-versus-barycenter split require new arithmetic beyond the parent identities. |

## No-Go Discipline Gate (Theorem 4 only)

The negative claim is restricted to exact equality of the truncated `E_0`
mass to `Tr(ρ E_0)` at all three declared Diracs for one finite `n`. The
gate does not ship a global non-derivability theorem.

### N1 — materially distinct routes

| Route family | Exact attack | Result | Marker |
|---|---|---|---|
| uniform-dyadic image | characterize all counting masses as `m/2^n` | `3/10` and `2/5` are outside that image for every finite `n` | **ATTEMPTED** |
| continuum atom splitting | replace `U_n` by `[0,1]` with Lebesgue measure | exact escape supplied by the August 12 parent, but it changes the finite-register hypothesis | **ATTEMPTED** |
| non-uniform finite weights | keep a finite register but assign atom weights with a factor of five | exact escape for selected values, but it replaces uniform `λ_n` | **ATTEMPTED** |
| register cardinality divisible by five | replace `2^n` points by a finite register whose size is divisible by `5` | can represent `3/10` and `2/5` at suitable cardinality, but it is not the declared dyadic register | **ATTEMPTED** |
| stochastic kernel on the original state | sample the event directly with probability `Tr(ρE)` | exact live escape, but it changes deterministic floor-bin registration into a stochastic kernel | **ATTEMPTED** |
| mixture-level cancellation | represent a biased barycenter as a mixture of spectral endpoints | realizes `3/10` exactly for the endpoint mixture, but does not make the Dirac at that barycenter exact; this is Theorem 5's separation | **ATTEMPTED** |
| terminating binary expansion | assert that `3/10` or `2/5` has a finite binary expansion | unique factorization rules this out because the reduced denominator contains `5` | **RULED OUT BY PRIOR** |

### N2 — wall independence

Theorem 4 claims no collection of independent walls. It proves one exact
image exclusion under one conjunction of explicit hypotheses: finite dyadic
register, uniform counting measure, the displayed floor bins, and the
declared Dirac family. N2 is therefore not applicable; the alternative
mechanisms in N1 are escapes that change a hypothesis, not walls whose count
is being inflated.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `D`, `U_n`, `D×U_n` | declared mathematical domains |
| floor-difference bins | explicit construction |
| declared Dirac family | explicit hypothesis of Theorem 4 |
| August 10 menus | declared finite hostile family |
| uniform `λ_n` | declared counting measure |
| physical auxiliary-register compiler | open; not assumed |
| continuum factor | live escape; not executed here |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one-site possibility domain, Admissibility distribution sentence, and current Record boundary | exact current text; no scalar/additivity/absence-value premise and no edit |
| August 10 type-separation note | hostile menus, restriction numbers, registered-partition interface left open | parent dependency; finite registration constructed here |
| August 12 barycenter-evaluation note | `Tr(ρ_μE)` comparison target | exact positive target; no physical law imported |
| August 12 registered-partition note | continuum `D×[0,1]` inverse-transform cells | exact escape and direct parent discretized here |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | `E_0` and the remaining declared menu members at named Diracs | no classification of every map from measures to effects |
| per site | one `M_2(C)` density body times `U_n` | no composite theorem |
| per mode | not executed; no spectral or harmonic modes occur in the theorem | no mode-level no-go |
| per block | finite-n exact-equality obstruction only | no dynamics, formation rate, or Record identification |
| lattice-wide | checked and not executed | no lattice-wide no-go |

The obstruction is per-Dirac / one-site / declared menus; it is not
lattice-wide.

### N6 — live partial-closure paths

1. The explicit Lebesgue factor of the August 12 parent, recovering
   barycenter evaluation exactly.
2. Non-affine kernels outside barycenter evaluation.
3. A physical compiler that produces an atom-splitting auxiliary law from
   Admissibility structure.
4. A content-only bridge from the mathematical event label to Record
   readout.

No axiom sentence is required by the finite dyadic image exclusion. Those four paths
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

August 10 separates the global measure, menu kernel, and registered-event
types. The August 12 barycenter note supplies the exact affine grade, and the
August 12 registered-partition note supplies exact continuum atom splitting.
The present residual is narrower: the uniform dyadic discretization of those
cells cannot be exact at the two declared non-dyadic Diracs for any finite
`n`. The continuum parent is an explicit escape, so no global registration
negative is inferred.

**Gate disposition.** PASS for the scoped uniform-dyadic image exclusion.
FAIL / DO NOT SHIP for "no registration exists", "the axioms cannot supply an
auxiliary register", or "continuum is impossible".

## Primary Runner

[`scripts/finite_dyadic_product_registration_truncated_barycenter_2026_08_13.py`](../scripts/finite_dyadic_product_registration_truncated_barycenter_2026_08_13.py)
recomputes the floor-difference partition, the uniform truncation bound, the
exact-versus-never-dyadic dichotomy, the finite dyadic image exclusion, the mixture
split, and the hostile-menu controls, all in exact `Q(√2)` arithmetic.
Identity gates call `floor_diff_mass` and `truncated_pushforward`; replacing
either by restriction `25/142` or by raw `Tr(ρ E)` must fail those checks.
Executed depths are `n=1` (the mixed quarter is not exact) and `n=3` (the
mixed quarter is exact and `3/10` is not), with `n=2` included as a cheap
witness that `1/4` becomes exact at the first dyadic threshold.
