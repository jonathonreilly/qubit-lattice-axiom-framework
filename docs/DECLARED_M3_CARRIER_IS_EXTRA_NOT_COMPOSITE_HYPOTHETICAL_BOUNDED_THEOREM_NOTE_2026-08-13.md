---
claim_id: declared_m3_carrier_is_extra_not_composite_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "After the tensor/sum class of M_2 fails to host unital M_3, declaring M_3(C) as a one-object carrier is an extra object (a second carrier type), not a composite construction from Lattice+Qubit+S'. Sentence S names only one-site M_2(C). Displayed S' plus class C still excludes unital M_3 because 3 never divides 2^k and simplicity forces a unital map through one power-of-two summand. Displayed S'' names M_3 by declaration and is not adopted. C2 as a reading of 'full' removes a wall slogan, not the extra object. No QCD. No fifth axiom."
upstream_dependencies:
  - minimal_axioms
runner: scripts/declared_m3_carrier_is_extra_not_composite_hypothetical_2026_08_13.py
---

# Declared `M_3` Carrier Is Extra, Not Composite

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact leftover type after the `M_2` tensor/sum class fails to
host unital `M_3(C)`: a declared larger carrier is an extra object, not
a construction.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/declared_m3_carrier_is_extra_not_composite_hypothetical_2026_08_13.py`](../scripts/declared_m3_carrier_is_extra_not_composite_hypothetical_2026_08_13.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

This is a hypothetical leftover-type test, not an axiom edit.

Live Qubit names one-site `M_2(C)`. After finite tensor and finite direct
sum of that algebra fail to host unital `M_3`, the honest leftover type
is “declare a larger carrier.” That leftover is an extra object — a
second carrier type — not a composite construction from Lattice, Qubit,
and a displayed composite reading.

The C2 move that “full is a reading” removes a *wall slogan*. It does
not supply the extra object. Color remains extra unless some later
construction that is not in the tensor/sum class, and is not a silent
declaration, is actually given.

Display the leftover sentences. Do not adopt them. Do not adopt a fifth axiom.
Do not call the leftover QCD.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Dimensions of M_2(C) and M_3(C) are counted from standard matrix units. Unital exclusion from the tensor/sum class is the integer obstruction 3 never divides 2^k plus simplicity of M_3. S'' is displayed declaration, not a theorem of Lattice+Qubit+S'. Adoption of S', S'', a fifth axiom, and any QCD identification remain open and are refused here."
trace_class: negative_route_pruning
target_claim_id: declared_m3_carrier_is_extra_not_composite
target_blocker_text: "after tensor/sum fail, is declaring M_3 as a carrier a composite construction or an extra object"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for dimensions, class-C unital exclusion, and leftover type; other constructions remain unclaimed"
hypothetical_axiom_status: "C2 leftover: declaring M_3 as a carrier is an extra object; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Current Qubit sentence **S**, quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Let **S′** be the displayed, not adopted, C2 reading:

> The local algebra is `M_2`; a physical object may be a declared finite
> composite in the tensor/sum class `C` of `M_2`.

Let **S′′** be a second displayed, not adopted, sentence:

> There is also a declared one-object algebra `M_3(C)`.

Write `A2 = M_2(C)` and `A3 = M_3(C)`. The standard matrix units
`{E_{ij}: 1 ≤ i,j ≤ n}` are a basis of `M_n(C)` over `C`, so

`dim_C A2 = 2·2 = 4`, `dim_C A3 = 3·3 = 9`.

Let `C` be the smallest class of finite-dimensional unital C*-algebras
such that `M_2(C) ∈ C` and `C` is closed under finite tensor product and
finite direct sum. Every object of `C` is *-isomorphic to

`M_{2^{k_1}} ⊕ ⋯ ⊕ M_{2^{k_r}}`

for some `r ≥ 1` and `k_i ≥ 1`. Tensor of matrix algebras multiplies
sizes that are powers of two; direct sum concatenates those sizes.

A unital C-linear *-homomorphism `M_k(C) → M_m(C)` exists if and only if
`k` divides `m`. The algebra `A3` is simple: its only two-sided ideals
are `0` and itself. A unital *-hom `φ : A3 → ⊕_i M_{2^{k_i}}` composed
with the coordinate projections is therefore either zero or a unital
*-hom into that summand. Unitality forbids the all-zero case, so some
coordinate is a unital *-hom `A3 → M_{2^{k}}`. That exists if and only
if `3 | 2^{k}`.

These objects are reconstructed here. They are not imported from a QCD
package. Neither `S′` nor `S′′` is written into the axiom memo.

## Theorem 1 — `dim M_2=4`, `dim M_3=9`, `9>4`; `S` does not name `M_3`

Counting the standard matrix units gives `dim_C A2 = 4` and
`dim_C A3 = 9`. Therefore

`9 > 4`.

Sentence `S` names the algebraic presentation `M_2(C)`. It does not name
`M_3` and it does not name `M_3(C)`. The live axiom memo likewise does
not name `M_3(C)`.

This theorem is only a dimension comparison plus a textual non-naming.
It does not identify `A3` with a physical color algebra.

## Theorem 2 — `S′` plus class `C` still does not contain unital `M_3`

Grant `S′` only as a displayed reading. The allowed composites are then
the objects of `C`.

For every `k ≥ 1`, `2^{k}` is a power of two, so its only prime factor
is `2`. In particular

`3 ∤ 2^{k}`.

Hence there is no unital *-hom `A3 → M_{2^{k}}`. By simplicity of `A3`,
there is also no unital *-hom `A3 → ⊕_i M_{2^{k_i}}` for any finite list
of exponents. Explicit witnesses in `C` used by the runner are

`M_2`, `M_2 ⊗ M_2 ≅ M_4`, `M_2 ⊕ M_2`, `M_4 ⊕ M_2`.

Each has only power-of-two matrix-summand sizes, and `3` divides none of
those sizes. So class `C` contains no unital copy of `M_3`.
Sentence `S′` therefore does not supply `M_3`.

The check is exact integer remainder, not a float tolerance.

## Theorem 3 — `S′′` names `M_3` by declaration; that is extra

Sentence `S′′` names `M_3(C)` by declaration:

> There is also a declared one-object algebra `M_3(C)`.

That is an extra object — a second carrier type — not a theorem of
Lattice + Qubit + `S′`. Theorems 1 and 2 show that `S` does not name
`M_3` and that `S′` plus `C` does not construct it. The only remaining
move in this leftover is to put `M_3` in by hand.

Display `S′′`. Do not adopt it. Do not call it QCD. Do not adopt a fifth axiom.

## Theorem 4 — C2 as a reading removes a wall slogan, not the extra object

Read current `S` as “nothing physical is larger than one-site `A2`.”
That reading is a *wall slogan*: color cannot exist unless an axiom is
added.

Read `S` as naming only the one-site algebra, so that “full” is a
reading rather than a ban on every larger physical object. That move
removes the wall slogan. It does not produce `M_3`. Theorem 2 still
says unital `M_3` is not in class `C`. Theorem 3 still says a declared
one-object `M_3` is extra.

Color remains extra unless some other construction — not in `C`, and
not a silent declaration — is supplied later. This note does not
supply that construction. This note does not rewrite the Qubit axiom.

## Mutation Predicates

The runner identity gates call `dim_m2()` and `dim_m3()`, which count
standard matrix units.

The predicate “the axiom memo names `M_3(C)`” is tested against the
live memo text and must fail.

The predicate “`9 ≤ 4`” is tested as `dim_m3() ≤ dim_m2()` and must
fail.

## Claim Boundary

| Claim | Status in this note |
|---|---|
| `dim_C M_2(C)=4`, `dim_C M_3(C)=9`, `9>4` | proved by counting standard bases |
| `S` does not name `M_3` | textual; quoted Qubit sentence and live memo |
| `3 ∤ 2^{k}` for every finite `k` | prime factorization of a power of two |
| no unital `M_3` in class `C` | simplicity plus the divisibility obstruction |
| `S′` supplies `M_3` | false; Theorem 2 |
| `S′′` is a theorem of Lattice+Qubit+`S′` | false; it is a declaration |
| declared `M_3` is an extra object / second carrier type | Theorem 3 |
| C2 as a reading removes the extra object | false; it removes a wall slogan only |
| `S′` or `S′′` is the new Qubit axiom | not adopted |
| a fifth axiom is adopted | not adopted |
| `A3` is QCD | not claimed |

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| current Qubit sentence `S` | exact semantic baseline | current axiom memo | supplied; not rewritten |
| displayed sentence `S′` | C2 composite reading | this note | displayed; not adopted |
| displayed sentence `S′′` | declared one-object `M_3` | this note | displayed; not adopted |
| class `C` | finite tensor/sum closure of `M_2` | reconstructed here | comparison class only |
| `A2`, `A3` | dimension and unital-hom witnesses | constructed here | not identified with SM objects |
| color as physical content | none | not imported | remains extra |
| QCD | none | not used | not applicable |

Independent audit remains required before the repository may assign any
effective claim status.

## No-Go Discipline Gate

The negative claim is only: declaring `M_3` as a carrier after tensor/sum
fail is an extra object, not a composite in `C`. The gate does not
certify that every later construction of a nine-dimensional algebra is
impossible.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Live sentence `S` names `M_3` | quote Qubit | Theorem 1: `S` names `M_2(C)` only | **ATTEMPTED** |
| Dimension coincidence | set `9 ≤ 4` | mutation: `9 > 4` | **ATTEMPTED** |
| Unital `M_3` in class `C` | require `3 | 2^{k}` or a simple factor | Theorems 2: never | **ATTEMPTED** |
| `S′` as a construction of `M_3` | composites in `C` supply color | Theorem 2: `S′` does not supply `M_3` | **ATTEMPTED** |
| `S′′` as a theorem | declaration equals derivation | Theorem 3: extra object | **ATTEMPTED** |
| C2 reading as removing the extra | wall slogan = extra object | Theorem 4: slogan only | **ATTEMPTED** |
| Adopt `S′` or `S′′` | rewrite Qubit | refused | **CLOSED HERE** |
| Adopt a fifth axiom / call it QCD | name color or QCD | refused | **CLOSED HERE** |
| Other constructions not in `C` | later non-class, non-declaration route | not claimed | **LIVE / OUT OF SCOPE** |

The broad statement “the axioms cannot derive color by any route” is
not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `9>4` / `3 ∤ 2^{k}` | no: dimension does not decide matrix-size divisibility | no: non-divisibility does not compute `3^2` | independent identities |
| `S` non-naming / class-`C` exclusion | no: text does not prove unital homs | no: class `C` is not the live sentence | independent leftovers |
| class-`C` exclusion / declared `S′′` | no: exclusion does not write `S′′` | no: a declaration is not a hom | extra vs construction |
| wall-slogan removal / extra object | no: Theorem 4 separates them | no: extra remains after the slogan drops | independent readings |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `A2`, `A3`, class `C` | reconstructed finite matrix objects |
| unital C-linear *-hom | standard finite-factor criterion `k | m` |
| simplicity of `A3` | standard; forces factoring through one summand |
| `S′`, `S′′` | explicit hypothetical readings; not adopted |
| color / QCD | comparison language only; not identified |
| observations or fitted constants | none |
| float approximations | none; integer remainder only |

### N4 — hostile counter-reading

A reader might say: “C2 already allowed composites, so writing `M_3`
is just naming the composite we wanted.” Class `C` is exactly those
composites. Unital `M_3` is not among them. Writing `M_3` is a new
carrier type, not a name for an object already in `C`.

### N5 — exhaustion claim refused

Only the tensor/sum class and the silent-declaration leftover are
typed here. Other constructions are not exhausted.

### N6 — axiom-edit refusal

No axiom sentence is edited. The Qubit one-site `M_2(C)` wording remains
the live parent.

### N7 — adoption refusal

`hypothetical_axiom_status` records the leftover and marks it
**not adopted**. Neither `S′` nor `S′′` is adopted. No fifth axiom is
proposed.

### N8 — FAIL / DO NOT SHIP

Do not ship any of the following as consequences of this note:

- “an axiom update is necessary”
- “declared `M_3` is a composite in `C`”
- “`A3` is QCD”
- “`S′` or `S′′` is now axiom content”

## Live Parent Quote

The only parent on the current public axiom memo is the Qubit
one-site sentence, quoted for non-mutation:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

That sentence names a local algebra. It does not name `M_3`, the class
`C` as axiom content, a declared one-object `M_3(C)`, a color primitive,
or QCD.
