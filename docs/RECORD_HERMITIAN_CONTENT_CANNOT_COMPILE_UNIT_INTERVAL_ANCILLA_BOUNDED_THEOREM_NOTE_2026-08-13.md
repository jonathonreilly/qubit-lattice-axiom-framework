---
claim_id: record_hermitian_content_cannot_compile_unit_interval_ancilla_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "If locked record content is a Hermitian 2x2 matrix, then I=Im Tr/2 vanishes, so a continuous ancilla u in [0,1] cannot be recovered from that content-only scalar. On the density body the same I is identically zero and is not the trace pairing Tr(ρ E). Storing u so that I recovers u requires non-Hermitian content; C_u=i u I is an explicit formal encoding, not a physical compiler and not an axiom edit."
upstream_dependencies:
  - minimal_axioms
runner: scripts/record_hermitian_content_cannot_compile_unit_interval_ancilla_2026_08_13.py
---

# Hermitian Content-Only I Cannot Compile The Unit-Interval Ancilla

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site linear algebra on Hermitian versus non-Hermitian
content in `M_2(C)`, for the additive content-only scalar `I=Im Tr/2`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_hermitian_content_cannot_compile_unit_interval_ancilla_2026_08_13.py`](../scripts/record_hermitian_content_cannot_compile_unit_interval_ancilla_2026_08_13.py)

## Result Up Front

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) says:

> Records form.
>
> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

Those clauses make readout additive and content-determined. They do not choose
a matrix formula for `I`. The campaign scalar used here, and in the adjacent
content-only descent arithmetic, is the fixed real-linear rule

`I(C)=Im Tr(C)/2`

on one-site content `C∈M_2(C)`. This note asks a single compiling question:
can a continuous registration ancilla `u∈[0,1]` be recovered from that
content-only `I` if locked content is required to stay Hermitian?

Three exact statements locate the boundary.

1. **Hermitian content is silent for this `I`.** Every `2x2` Hermitian matrix
   has real trace, so `I(C)=0`. In particular every density `ρ` has
   `I(ρ)=0`, independently of `ρ`. The trace pairing `Tr(ρ E)` — the
   Newton/Born pairing of a locked density with a supplied effect — is a
   different number: `Tr(ρ)=1` always, while `Tr(ρ E)` varies with both
   arguments. Therefore `I` does not read the Born grade of a locked
   density, and cannot recover an independent ancilla that is not among the
   four real parameters of Hermitian content.
2. **A non-Hermitian label stores `u`.** The matrices `C_u=i u I` satisfy
   `I(C_u)=u` for every `u∈[0,1]`. For `u≠0` one has `C_u^†=-C_u≠C_u`, so
   the encoding leaves the Hermitian body. The same `I` applied to the
   Hermitian label `u I` returns `0`, not `u`. The shifted label
   `E+i u I` with Hermitian `E` likewise has `I=u`.
3. **The encoding is a live formal escape, not a compiler.** Writing `u`
   into the anti-Hermitian center is compatible with content-only additivity.
   It is not derived from Record or Admissibility, not a physical
   registration compiler of the product factor `[0,1]`, and not an axiom
   edit.

No axiom sentence is edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The three statements are exact 2x2 identities for I=Im Tr/2 on declared Hermitian and non-Hermitian matrices. A physical compiler of the unit-interval factor from Record and Admissibility structure remains open."
trace_class: negative_route_pruning
target_claim_id: record_hermitian_content_cannot_compile_unit_interval_ancilla
target_blocker_text: "decide whether Hermitian content-only I can recover the product registration coordinate u in [0,1]"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for I=0 on Hermitians, I(C_u)=u off the Hermitian body, and the pairing/I split on densities; physical compilation remains open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site, with possibility domain `X=M_2(C)` as in the current Qubit
axiom. A matrix `C=((a,b),(c,d))` is Hermitian when `C=C^†`, equivalently
when `a,d∈R` and `c=conj(b)`. That real vector space is four-dimensional:
the parameters of

`C=((p, q+i r),(q-i r, s))`, `p,q,r,s∈R`,

or, equivalently, the real coefficients of `{I,σ_x,σ_y,σ_z}`.

The density body is

`D={ρ∈M_2(C): ρ=ρ^†, ρ≥0, Tr(ρ)=1}`.

Every `ρ∈D` is Hermitian, so it lies in that four-parameter space with the
further constraints `p+s=1` and positivity.

The displayed readout is the fixed content-only scalar

`I(C)=Im Tr(C)/2`.

This rule is real-linear on `M_2(C)`, additive in the matrix argument, and
vanishes at the zero matrix. It is not complex-linear:
`I(i I)=1` while `i I(I)=0`.

**Vanishing locus, stated carefully.** If `C` is Hermitian then `Tr(C)` is
real, so `I(C)=0`. The vanishing is on Hermitian matrices. It is not a
vanishing on `i` times Hermitian matrices: if `H` is Hermitian then

`I(i H)=Tr(H)/2`.

That identity is why a central anti-Hermitian label can store a real
scalar, and why the same rule cannot store that scalar in Hermitian
content.

Any real-linear functional of Hermitian matrices is determined by the four
real parameters of `C`. The particular functional `I` is the zero functional
on that space. Other real-linear functionals — for example `Re Tr/2`, or
`Tr(C E)` at a fixed Hermitian `E` — may read Bloch data of a locked
density. None of those four parameters is an independent ancilla coordinate
adjoined to `D`.

## Reconstructed Product Ancilla

To name the coordinate that Hermitian content fails to compile, reconstruct
the product registration that realizes the trace pairing as a pushforward.
This reconstruction is local mathematics in the present note. It is not a
citation-graph dependency.

Let `Y=D×[0,1]` and let `λ` be Lebesgue measure on `[0,1]`. For a finite
resolution `M=(E_1,...,E_r)` of `I` and for `ρ∈D`, set

`S_0(ρ)=0`, `S_i(ρ)=Σ_{j=1}^{i} Tr(ρ E_j)`.

Then `S_r(ρ)=1`. The cells

`A(i|M)={(ρ,t)∈Y: S_{i-1}(ρ) ≤ t < S_i(ρ)}`

are pairwise disjoint, cover `Y` up to a null singleton, and do not depend
on a choice of measure. For every finite-support `μ=Σ_k p_k δ_{ρ_k}` on
`D`,

`(μ⊗λ)(A(i|M))=Σ_k p_k λ([S_{i-1}(ρ_k),S_i(ρ_k)))=Σ_k p_k Tr(ρ_k E_i)=Tr(ρ_μ E_i)`.

The extra factor `[0,1]` is a declared registration ancilla. At fixed
Hermitian `ρ`, the fiber coordinate `u∈[0,1]` varies independently of `ρ`.
The fiber length assigned to a fixed effect `E` is the pairing
`Tr(ρ E)`, not `I(ρ)`.

Witnesses used below, all exact:

`E_0=diag(1/2,0)`,
`ρ_*=I/2`,
`ρ_{3/5}=diag(3/5,2/5)`.

Matrix multiplication gives `Tr(ρ_* E_0)=1/4` and
`Tr(ρ_{3/5} E_0)=3/10`. Both numbers are the reconstructed fiber lengths.
Both densities have `I=0`.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the content-only scalar `I=Im Tr/2` can
recover a continuous ancilla `u∈[0,1]` from Hermitian locked content, and
whether a declared non-Hermitian label restores formal recoverability
without becoming a physical compiler.

| Obligation | Role | Disposition |
|---|---|---|
| pin Records form / content alone / `I(empty)=0` | premise | quoted from the axiom memo |
| prove `I=0` on every Hermitian `2x2` | Theorem 1 | real trace |
| separate `I(ρ)` from `Tr(ρ E)` on `D` | Theorem 1 | `0` versus `1/4`, `3/10` |
| show no function of Hermitian `ρ` recovers independent `u` | Theorem 1 | `u` is not a parameter of `ρ` |
| exhibit `C_u=i u I` with `I(C_u)=u` | Theorem 2 | direct trace |
| prove `C_u` is non-Hermitian for `u≠0` | Theorem 2 | `C_u^†=-C_u` |
| reject the Hermitian label `u I` | Theorem 2 discriminator | `I(u I)=0` |
| identify the encoding as a physical compiler | Theorem 3 | not claimed |
| edit an axiom sentence | non-claim | not attempted |

## Theorem 1 — Hermitian Content Makes `I` Silent

**Claim.** If locked content `C` is a Hermitian `2x2` matrix, then
`I(C)=0`. Consequently a continuous ancilla `u∈[0,1]` cannot be recovered
from `I(C)`. If the locked content is a density `ρ∈D`, then `I(ρ)=0`
independently of `ρ`, so `I` does not read the Born grade.

**Proof.** Let `C=C^†` in `M_2(C)`. The diagonal entries of a Hermitian
matrix are real, so `Tr(C)∈R` and `Im Tr(C)=0`. Therefore

`I(C)=Im Tr(C)/2=0`.

The same identity holds on a real basis of the Hermitian space:

`I(I)=Im(2)/2=0`,
`I(σ_x)=I(σ_y)=I(σ_z)=0`.

A general Hermitian matrix is `C=p I+q σ_x+r σ_y+s σ_z` with real
coefficients, and real-linearity gives `I(C)=0`. Thus `I` is the zero
functional on the four real parameters of Hermitian content.

Every density is Hermitian, so `I(ρ)=0` for every `ρ∈D`. The value does
not depend on which density is locked. By contrast the pairing used by the
reconstructed product registration is

`Tr(ρ_* E_0)=1/4`, `Tr(ρ_{3/5} E_0)=3/10`.

Those are not `I(ρ)`. They are also not functions of `I(ρ)`, because
`I` is constant on `D` while the pairing is not. The pairing can vary
because it uses a second Hermitian argument `E`. The Record scalar of the
locked `ρ` has no such second argument: it is a function of record content
alone.

Now let `u∈[0,1]` be independent of a locked Hermitian matrix `C` — in
particular, let `u` be the fiber coordinate of `Y=D×[0,1]` at a fixed
`ρ`. Any function of `C` alone is independent of `u`. Specializing to the
displayed `I`,

`u ↦ I(C)`

is the constant map `0`. A constant map on `[0,1]` is not injective and
does not recover `u`. Replacing `I` by any other function of Hermitian
content — including any real-linear functional of the four parameters of
`C` — still yields a function of `C` alone, hence still cannot recover an
independent ancilla.

**Scope.** The negative is only this: Hermitian content plus the displayed
content-only `I` cannot compile `u`. It is not a claim that every
real-linear functional of all of `M_2(C)` vanishes, and it is not a
vanishing statement on `i` times Hermitian matrices.

## Theorem 2 — Storing `u` Forces Non-Hermitian Content

**Claim.** If a matrix `C_u∈M_2(C)` is to satisfy `I(C_u)=u` for a
nonconstant family of `u∈[0,1]`, then `C_u` cannot remain Hermitian.
The explicit family

`C_u=i u I`

obeys `I(C_u)=u` for every real `u`, and is non-Hermitian whenever
`u≠0`.

**Proof.** Suppose `C_u` is Hermitian for every `u` in a nondegenerate
subinterval of `[0,1]`. Theorem 1 forces `I(C_u)=0` on that subinterval,
so `u` is not recovered. Therefore any encoding that `I` reads must leave
the Hermitian body on a nonempty open set of ancilla values.

The displayed family works. One has

`C_u=((i u, 0),(0, i u))`,
`Tr(C_u)=2 i u`,
`I(C_u)=Im(2 i u)/2=u`.

The adjoint is `C_u^†=-i u I=-C_u`. Equality `C_u=C_u^†` holds if and
only if `u=0`. For every `u∈(0,1]` the matrix is non-Hermitian.

The Hermitian competitor `u I` fails as a discriminator:

`I(u I)=Im(2u)/2=0`.

So placing the ancilla on the real center is invisible to this `I`;
placing it on the imaginary center is visible. The same arithmetic gives
the shifted labels used as a formal product embedding,

`E+i u I`, `I(E+i u I)=I(E)+u`.

When `E` is Hermitian, `I(E)=0` and the readout is again exactly `u`.
Additivity of `I` on matrices is the finite-sum counterpart of the Record
additivity clause, and the zero matrix — the empty-content witness —
has `I(0)=0`, matching `I(empty)=0`.

Samples used by the runner are the exact points
`u∈{0,1/5,1/4,1/2,3/5,1}` together with the Hermitian controls
`I`, `σ_x`, `σ_y`, `σ_z`, `ρ_*`, `ρ_{3/5}`, and a generic four-parameter
Hermitian. On that sample, `I` is identically `0` on every Hermitian
matrix and equals `u` on every `C_u` and every `E_0+i u I`.

## Theorem 3 — Formal Escape, Not A Physical Compiler

**Claim.** The encoding `C_u=i u I` is a live formal escape from
Theorem 1. It is not a physical compiler of the unit-interval factor, and
it is not an axiom sentence.

**Proof of the formal half.** The Qubit possibility domain is already
`M_2(C)`, which contains non-Hermitian matrices. The map `u↦C_u` lands in
that domain. The readout `I=Im Tr/2` is a function of the stored matrix
alone, hence content-only in the sense of the quoted Record sentence. It
is additive and vanishes at empty content. Distinct ancilla values produce
distinct matrices and distinct readouts. Therefore, as linear algebra,
nothing in the quoted clauses forbids reading `u` after it has been
written into the anti-Hermitian center.

**Proof of the non-compiler half.** The quoted clauses do not select the
formula `I=Im Tr/2`, do not require forming records to store `C_u`, and
do not produce the product space `Y=D×[0,1]` from Admissibility structure.
The factor `[0,1]` in the reconstructed registration remains a declared
coordinate. Identifying that coordinate with `C_u`, or with
`ρ+i u I`, would be an additional map from a registration fiber to record
content. No such map is derived here. In particular this note does not
argue that an axiom update is necessary, and it does not write any such
map into the axiom memo.

The discriminating gate is only this: `I=Im Tr/2` on Hermitian matrices
is `0`; a non-Hermitian label `E+i u I` with `u∈[0,1]` can store `u`.
Both sides are exhibited. An honest miss on either side would stand.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- identify `I=Im Tr/2` as the unique physically available Record scalar;
- identify `Tr(ρ E)` with a Record readout of the locked `ρ`;
- derive the product factor `[0,1]` from Record or Admissibility;
- claim that forming records store `C_u` or `E+i u I`;
- prove uniqueness of the Born trace grade;
- supply a formation site or rate;
- exhaust other non-Hermitian encodings.

The four axioms continue to say only what they say. Records form. A
readout value is determined by record content alone. Scalar `I` is
additive, with `I(empty)=0`. Those sentences are used as premises. They
are not enlarged.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record sentences, including Records form, content alone, and `I(empty)=0` | premise | quoted; no edit |
| `I(C)=Im Tr(C)/2` | declared content-only scalar | used here |
| Hermitian `2x2` calculus and the four real parameters | Theorem 1 | standard linear algebra |
| reconstructed `Y=D×[0,1]` and fiber length `Tr(ρ E)` | location of the ancilla | local reconstruction, not a parent |
| `C_u=i u I` and `E+i u I` | formal encodings | constructed here |
| physical compiler of `[0,1]` | residual | open |
| axiom necessity, Born uniqueness, formation rate | non-claims | not used |

The exact advance is a compiling obstruction for Hermitian content under
the displayed `I`, together with an explicit non-Hermitian formal escape.
Independent audit remains required before any effective status may change.
