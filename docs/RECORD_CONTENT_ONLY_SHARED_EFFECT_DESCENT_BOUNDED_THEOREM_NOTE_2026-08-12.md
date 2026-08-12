---
claim_id: record_content_only_shared_effect_descent_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "At one M_2(C) site the Aug 10 atomic restriction assigns two probabilities to one shared effect. Any readout determined by effect-only record content must assign one scalar to that effect. Those two facts are compatible only if record content is allowed to encode the menu name, not only the effect. An effect-only content map and a menu-in-content map are both exhibited. The note edits no axiom, proves no axiom necessity, proves no Born uniqueness, and supplies no formation rate."
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
runner: scripts/record_content_only_shared_effect_descent_2026_08_12.py
---

# Record Content-Only Shared-Effect Descent

**Date:** 2026-08-12
**Type:** bounded_theorem
**Scope:** one-site Record readout versus the Aug 10 shared-effect
restriction kernel.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_content_only_shared_effect_descent_2026_08_12.py`](../scripts/record_content_only_shared_effect_descent_2026_08_12.py)

## Result Up Front

The current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) says:

> Only records are readable. A readout value is determined by record content alone.

The Aug 10 type-separation note
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md)
assigns two different normalized restriction values to one shared scaled
effect `E_0` in two ternary menus. Those two facts can hold together only if
the record that is read is allowed to encode the menu name, not only the
effect matrix.

Three exact statements locate the boundary.

1. **Effect-only content is menu-independent.** The map `Φ_eff(M,E)=E` stores
   the effect and forgets the menu. Any scalar `I` of that matrix assigns one
   value to `E_0` in both menus.
2. **Restriction is not an effect-only readout.** Recomputing the Aug 10
   atomic masses gives `K_ν(E_0|M_A)=25/142` and `K_ν(E_0|M_B)=2/11`. Those
   are two scalars on one effect, so they are not of the form `I ∘ Φ_eff`.
3. **Menu-in-content remains a live escape.** Encoding the pair
   `(label(M),E)` as `Φ_ctx(M,E)=E+i α_M I`, with `α_A=1` and `α_B=2`, and
   reading `I(Φ)=Im Tr(Φ)/2`, yields the two scalars `1` and `2`. Each value
   is a function of the stored matrix alone. The construction is not claimed
   to be physical.

No axiom is edited. The result is a compatibility theorem, not a Born
uniqueness theorem and not a formation-rate statement.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The three statements are exact on declared one-site content maps and the Aug 10 atomic restriction witness. Physical encoding of a menu in a record, axiom necessity, and Born uniqueness remain open."
trace_class: negative_route_pruning
target_claim_id: record_content_only_shared_effect_descent
target_blocker_text: "decide whether Aug 10 restriction can be a content-only Record readout of a shared effect"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for effect-only descent, restriction non-descent, and the displayed menu-in-content escape; physical realization remains open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site, with possibility domain `X=M_2(C)` as in the current Qubit
axiom. For a unit Bloch vector `n` write

`P(n)=(I+n · σ)/2`.

Reuse the Aug 10 shared-effect menus exactly. Fix

`E_0=(1/2)P(z)=((1/2,0),(0,0))`.

The two ternary scaled-projector menus sharing only `E_0` are

`M_A={E_0,(9/10)P(n_1),(3/5)P(n_2)}`

with

`n_1=(4 √2/9, 0, -7/9)`,
`n_2=(-2 √2/3, 0, 1/3)`,

and

`M_B={E_0,(3/4)P(m_1),(3/4)P(m_2)}`

with

`m_1=(2 √2/3, 0, -1/3)`,
`m_2=(-2 √2/3, 0, -1/3)`.

Each displayed vector has norm one. In both menus the scalar coefficients sum
to two and the coefficient-weighted Bloch vectors sum to zero, so each menu
sums to `I`. The parent note records the resolution check; the runner repeats
it.

The Aug 10 atomic measure `ν` lives on the five distinct effects in
`M_A ∪ M_B` and assigns mass proportional to the square of the effect's
trace. Writing `c=Tr(cP(n))` for a scaled rank-one effect, the five masses
before normalization are

`(1/2)^2=1/4`,
`(9/10)^2=81/100`,
`(3/5)^2=9/25`,
`(3/4)^2=9/16`,
`(3/4)^2=9/16`.

Their sum is

`Z=1/4+81/100+9/25+9/16+9/16`.

The common denominator `400` gives

`100/400+324/400+144/400+225/400+225/400=1018/400=509/200`.

Normalized restriction on each menu is then

`K_ν(E|M)=ν({E})/ν(M)`

whenever the denominator is positive.

A **content map** is a function `Φ` from outcome pairs `(M,E)` with `E∈M` into
`M_2(C)`. A **content-only readout** is a fixed scalar function `I` of that
matrix. The Record sentence quoted above requires the displayed readout to be
of this form once a content map has been chosen. It does not by itself choose
the map.

Two maps are used.

1. **Effect-only.** `Φ_eff(M,E)=E`. The menu name is discarded. On the shared
   effect this is the same Hermitian matrix in both menus.
2. **Menu-context.** `Φ_ctx(M,E)=E+i α_M I` with labels `α_A=1` and `α_B=2`.
   The pair `(label(M),E)` is written as one matrix in the Qubit possibility
   domain. The imaginary multiple of the identity is a label encoding, not a
   claimed physical formation mechanism.

The displayed readout throughout is the fixed content-only scalar

`I(Φ)=Im Tr(Φ)/2`.

This is additive in the matrix argument and vanishes at `0`. On a Hermitian
effect it is identically zero. On `Φ_ctx` it recovers the label `α_M`.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the Aug 10 restriction kernel on the shared
effect can be a Record readout of effect-only content, and whether writing the
menu name into the record restores formal compatibility with the content-only
sentence.

| Obligation | Role | Disposition |
|---|---|---|
| pin the current content-only Record sentence | premise | quoted from the axiom memo |
| reuse the Aug 10 menus and atomic masses | common objects | restated and recomputed |
| show every `I ∘ Φ_eff` is menu-independent on `E_0` | Theorem 1 | proved by substitution |
| recompute `K_ν(E_0|M_A)` and `K_ν(E_0|M_B)` | Theorem 2 input | exact fractions below |
| show restriction is not `I ∘ Φ_eff` | Theorem 2 | two unequal scalars |
| exhibit a content-only `I ∘ Φ_ctx` with two scalars | Theorem 3 | `1` and `2` |
| derive a physical menu-in-content encoding | autonomous closure | open |
| prove axiom necessity or Born uniqueness | non-claims | not attempted |

## Theorem 1 — Effect-Only Content Maps Are Menu-Independent On Shared Effects

Let `I` be any scalar function of a matrix in `M_2(C)`. Then

`I(Φ_eff(M_A,E_0))=I(E_0)=I(Φ_eff(M_B,E_0))`.

The two outcome pairs `(M_A,E_0)` and `(M_B,E_0)` produce the same record
content, so they produce the same readout. This is substitution, not an extra
continuity or positivity hypothesis.

For the displayed scalar the common value is explicit. The matrix of `E_0` is
Hermitian with real trace `1/2`, so

`I(Φ_eff(M_A,E_0))=Im(1/2)/2=0`

and likewise on `M_B`. Any other fixed function of `E_0` — for example
`Re Tr(E_0)/2=1/4` — is likewise the same in both menus.

Thus every content-only readout of an effect-only record is
menu-independent on shared effects.

## Theorem 2 — The Restriction Kernel Is Not An Effect-Only Content Readout

The Aug 10 atomic masses on `M_A` are `1/4`, `81/100`, and `9/25`. Their sum
is

`1/4+81/100+9/25=100/400+324/400+144/400=568/400=142/100`.

Normalized restriction of the shared effect is therefore

`K_ν(E_0|M_A)=(1/4)/(142/100)=(1/4)·(100/142)=25/142`.

The Aug 10 atomic masses on `M_B` are `1/4`, `9/16`, and `9/16`. Their sum is

`1/4+9/16+9/16=100/400+225/400+225/400=550/400=11/8`.

Normalized restriction of the shared effect is therefore

`K_ν(E_0|M_B)=(1/4)/(11/8)=(1/4)·(8/11)=2/11`.

These are unequal:

`25/142-2/11=(275-284)/1562=-9/1562`.

Suppose there existed a content-only scalar `I` with

`K_ν(E_0|M)=I(Φ_eff(M,E_0))`

on both menus. Theorem 1 would force `25/142=2/11`, contradicting the
difference just computed. Therefore the restriction kernel is not of the form
`I ∘ Φ_eff`.

The extra argument used by restriction is the menu itself. Under the Record
sentence that extra argument cannot change the readout unless it is written
into the record content.

## Theorem 3 — Menu-In-Content Maps Realize Two Scalars On The Shared Effect

Define `Φ_ctx(M,E)=E+i α_M I` with `α_A=1` and `α_B=2`, and keep
`I(Φ)=Im Tr(Φ)/2`. Then

`Φ_ctx(M_A,E_0)=((1/2+i,0),(0,i))`,

`Tr=1/2+2i`,
`I=Im(1/2+2i)/2=1`,

and

`Φ_ctx(M_B,E_0)=((1/2+2i,0),(0,2i))`,

`Tr=1/2+4i`,
`I=Im(1/2+4i)/2=2`.

The two matrices are distinct elements of `M_2(C)`. The readout is the same
function of the stored matrix in both cases, so it is content-only in the
sense of the quoted Record sentence. The two scalars differ because the menu
name was written into the content.

This is a live formal escape from Theorem 2: restriction-like menu dependence
can be rewritten as content dependence after a content map that sees the menu
label. The escape is not claimed to be a physical record-formation mechanism,
not claimed to be forced by the four axioms, and not claimed to select the
Born grade. A later construction would have to derive, from Record and
Admissibility structure, that forming records actually store a menu label in
this or some other injective way.

## Boundary And Non-Claims

The note does not:

- edit an axiom, or argue that an axiom update is necessary;
- identify `K_ν` with a physical Record law;
- prove uniqueness of the Born trace grade;
- supply a record-formation site or rate;
- construct a dynamics that writes `α_M` into a forming record;
- exhaust other content maps.

The discriminating gate is only this: a content map that depends only on the
effect matrix must give one `I` on `E_0`; a content map that also encodes the
menu name may give two `I` values. Both sides are exhibited. An honest miss
on either side would stand.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record content-only sentence | premise | quoted; no edit |
| Aug 10 menus, `ν`, and restriction arithmetic | common objects | restated and recomputed |
| `Φ_eff`, `Φ_ctx`, and `I(Φ)=Im Tr(Φ)/2` | declared maps | constructed here |
| physical menu-in-content encoding | escape route | live, not derived |
| axiom necessity, Born uniqueness, formation rate | non-claims | not used |

The exact advance is a compatibility theorem between the Record content-only
sentence and the Aug 10 shared-effect restriction witness. Independent audit
remains required before any effective status may change.
