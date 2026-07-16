# Occupancy-Grain Candidate-Decider Triad Reduces to One Count Binary on the Supplied C3 Model: Bounded Theorem

claim_id: `acphilambda_occupancy_grain_three_candidate_deciders_common_count_binary_reduction_bounded_theorem_note_2026-07-16`

**Date:** 2026-07-16
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Premise weight:** conditional. This note derives an exact structural reduction
on a supplied `C3` model; it registers no primitive, adopts no convention, and
selects no horn of the open occupancy-grain obligation.
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:** [`scripts/acphilambda_grain_decider_reduction_2026_07_16.py`](../scripts/acphilambda_grain_decider_reduction_2026_07_16.py)
**Cache:** [`logs/runner-cache/acphilambda_grain_decider_reduction_2026_07_16.txt`](../logs/runner-cache/acphilambda_grain_decider_reduction_2026_07_16.txt)

## Purpose

The open occupancy-grain obligation asks whether the physical charged-lepton
matter action counts the `K`/CPT orbit once or twice. Three candidate deciders
have been floated for that obligation:

1. an **action reality class** (count-once `det_C`/holomorphic versus count-twice
   `|det_C|^2`/realified);
2. a **`K`/CPT quotient-measure pushforward** (orbit-sum pushforward versus
   single-representative restriction on the sector set);
3. a **record-formation locking-rule dictionary** (component completion versus
   slot completion of the doublet outcome).

This note proves, on a supplied minimal `C3` model, that all three candidate
deciders are parameterized by one common count binary `m` in `{1, 2}`, that
deciding any one fixes the other two through exact translations, and that the
whole obligation therefore concentrates onto that single still-open input. The
result is a bounded structural reduction. It is not a closure and not a no-go:
neither value of `m` is forced, derived, or preferred here.

## Supplied objects and consumed readings

The reduction consumes the following retained or open surfaces exactly as
written. Each block below is a verbatim reading; the runner gates every one
against its source file after whitespace flattening.

The open obligation's exact closure criterion:

```text
A closing theorem must derive the physical matter action and its measure, then
distinguish the count-once `det_C`/holomorphic realization from the
count-twice `|det_C|^2`/realified realization without inserting the desired
charged-lepton value or readout dictionary.
```

```text
Until such a theorem is independently audited and retained, every result that
uses this statistical-grain selection remains conditional or pending-chain.
```

The measure-binary no-go (`2A`), non-selection theorem:

```text
do not choose
  generator-channel / orbit / holomorphic count-once
over
  dimension / sector / real count-twice.
```

The formation-append non-supply no-go (`2C`), the unsupplied dictionary item,
its finite-separation readings, the both-completions lawfulness statement, and
its remaining matter-action route:

```text
the outcome-to-component dictionary that reads the doublet as count-twice or
count-once;
```

```text
| component dictionary | `x = 2r` | `r = 1/2` |
| slot dictionary | `x = r` | `r = 1` |
```

```text
Both completions are lawful as formation-rule completions: the difference is
only the unsupplied dictionary/weighting of the doublet outcome.
```

```text
Derive that the physical staggered/finite
Grassmann matter action implements the count-twice or count-once grain.
```

The determinant-power support note (`3A`), ledger-row audited claim scope:

```text
For every finite complex matrix K, the displayed realification has determinant |det_C(K)|^2 and the displayed ordered holomorphic Berezin Gaussian equals det_C(K); no physical carrier or occupancy-rule identification is included.
```

The Record axiom's readout additivity, and the framework's qualification clause
on unsupplied choices:

```text
Only records are readable. A readout value is determined by record content
alone. For any finite collection of pairwise-disjoint records, scalar readout
`I` is additive, with `I(empty)=0`.
```

```text
These axioms state only their named primitive content. Further physical
structure requires a retained derivation or bridge, or explicit approved-
primitive registration, before use as a premise. A choice not fixed by the
supplied structure remains a named conditional or open dependency.
```

## Declared reading D1 (supplied model)

Fix the cyclic shift `C` acting on the ordered index set `{0, 1, 2}` by
`C = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]`, so `C^3 = identity`. Let
`w = exp(2*pi*i/3)`. The character vectors

```text
u0 = (1, 1, 1)
e1 = (1, w, w^2)
e2 = (1, w^2, w)
```

are the eigenvectors of `C` with eigenvalues `1`, `w`, `w^2`. They index the
three sectors `{s0, s+, s-}`. Entrywise complex conjugation `K` fixes `s0` and
swaps `s+` with `s-` because `conj(e1) = e2`: one `K`-fixed sector `s0` and one
free `K`-orbit `{s+, s-}`.

Three carriers live on this sector set:

> **A (the `K`-real carrier).** `A = alpha*I + beta*C + gamma*C^2` with
> `alpha`, `beta`, `gamma` real and `beta != gamma`. Then `conj(A) = A`, and the
> spectrum is `lam_k = alpha + beta*w^k + gamma*w^(2k)` with `lam0` real,
> `lam2 = conj(lam1)`, and `im(lam1) = (sqrt(3)/2)*(beta - gamma)`. This is the
> object on which count-once and count-twice differ.

> **Z (the general complex circulant).** `Z = a0*I + a1*C + a2*C^2` with
> `a0`, `a1`, `a2` complex. It is used only to re-gate the `3A` determinant-power
> identity at full generality; it carries no occupancy identification.

> **M (the Hermitian registered-pattern control).** `M = a*I + b*C + conj(b)*C^2`
> with `a` real and `b` complex. Because `C^dagger = C^2`, `M` is Hermitian and
> its spectrum is entirely real. `M` is a pre-record reconstruction, not the
> registration itself; it is included only as a realist-slip control, so that no
> step silently reads a reconstructed pattern as a locked record.

The `C3` symmetry, the `K` conjugation, and any equal-per-mode normalization are
held throughout as supplied context and as carrier structure. None of them is
used as a selector between the two count settings.

## Declared reading D2 (the one count binary)

Let `m` in `{1, 2}` be the count applied to the free `K`-orbit `{s+, s-}`:
`m = 1` counts the conjugate pair once, `m = 2` counts it twice. Under the
supplied equal-per-mode normalization the doublet total weight is `W_d = m` and
the singlet weight is `W_s = 1`; the established dial map gives

```text
r = (W_d/2) / W_s = m/2,
```

so `m = 1` maps to `r = 1/2` and `m = 2` maps to `r = 1`. Equivalently, the
per-cell dial map `r = (1 - w_cell) / (2*w_cell)` with `w_cell = 1/(1 + W_d)`
reduces symbolically to `W_d/2`, giving the same pair. The binary `m` is the
single open input; nothing in this note fixes its value.

## T1 (model faithfulness)

The supplied model reproduces the claimed spectral facts exactly:
`det_C(A) = lam0*lam1*lam2`; `im(lam0) = 0`; `lam2 = conj(lam1)`;
`C e1 = w e1`; `A e1 = lam1 e1` and `A e2 = lam2 e2`; `conj(A) = A`; and the
free-orbit imaginary part `im(lam1) = (sqrt(3)/2)*(beta - gamma)` is nonzero
whenever `beta != gamma`. The Hermitian control `M` is not `K`-real:
`conj(M) != M` unless `b` is real, and its orbit values `lamM_1` and `lamM_2`
are two independent real numbers rather than a conjugate pair, so the
once-versus-twice count question posed on a conjugate pair does not arise on
`M`; this is what makes it a valid control rather than a fourth candidate
decider.

## T2 (global-power neutrality)

Multiplying both the doublet and singlet weights by the same positive factor
leaves the dial invariant: `r = (W_d/2) / W_s` is unchanged under
`(W_s, W_d) -> (2 W_s, 2 W_d)`. The count binary is therefore a genuinely
relative orbit-versus-singlet setting, not an artifact of an overall
normalization.

## T3 (each candidate decider carries both settings)

> **(a) Action reality class.** The count-once realization weights the free
> orbit by the holomorphic single-sector value `det_C` (free-orbit modulus power
> `1`); the count-twice realization weights it by the realified `|det_C|^2`
> (free-orbit modulus power `2`). By `3A`, the realification determinant equals
> `|det_C|^2` and the ordered holomorphic Berezin Gaussian equals `det_C`, so the
> only difference on the free orbit is the modulus power in `{1, 2}`.

> **(b) `K`/CPT quotient-measure pushforward.** Start from the same
> `K`-invariant sector measure `mu = (mu0, t, t)` (`K`-invariance forces equal
> values on `s+` and `s-`). Two lawful constructions on the quotient sector set
> `{fixed, orbit}`: the orbit-sum pushforward sums over the conjugate pair and
> gives `(mu0, 2t)` = count-twice; the single-representative restriction keeps
> one representative and gives `(mu0, t)` = count-once. They agree on the fixed
> sector and differ by exactly the free-orbit cardinality `2`. This is a
> pushforward-versus-restriction alternative on the sector set, computed from the
> orbit partition alone.

> **(c) Record-formation locking dictionary.** The unsupplied
> outcome-to-component dictionary reads the doublet either as the component
> completion `x = 2r` (equipartition `x = 1` gives `r = 1/2`, count-once) or as
> the slot completion `x = r` (equipartition `x = 1` gives `r = 1`, count-twice).
> Both completions are lawful formation-rule completions per `2C`.

## T4 (exact translations)

The three deciders are one decider under the following exact dictionary. Write
the free-orbit weight exponent for the reality class, the orbit factor for the
measure, and the doublet weight for the dictionary; each equals the count binary
`m`, and each maps to the same dial value `r = m/2`.

| guise | count-once (`m = 1`) | count-twice (`m = 2`) | dial image |
|---|---|---|---|
| action reality class | single-sector holomorphic weight, free-orbit modulus power `1` | realified weight, free-orbit modulus power `2` | `r = m/2` |
| quotient-measure | single-representative restriction `(mu0, t)` | orbit-sum pushforward `(mu0, 2t)` | `r = m/2` |
| formation dictionary | component completion `x = 2r` | slot completion `x = r` | `r = m/2` |

Deciding any one column entry decides the row, and deciding the count binary `m`
decides all three guises simultaneously.

## T5 (concentration corollary)

The obligation's quoted closure criterion demands one distinction: count-once
`det_C`/holomorphic versus count-twice `|det_C|^2`/realified. On the supplied
model that distinction is the D2 binary `m`, and by T4 the three candidate
deciders are exact translations of one another through `m`. Consequently, if a
retained derivation of the physical matter action and its measure presents any
one of the three guises, fixing that guise's setting fixes `m`, the dial
`r = m/2`, and the other two guises with it; the closure criterion is then met
exactly when such a derivation supplies `m` without inserting the desired
charged-lepton value or readout dictionary. This corollary is a prose
consequence of T4 and the quoted criterion, conditional on the physical action
presenting one of these guises. This note supplies the reduction, not the
value.

## Negative controls

> **N1 (no forcing).** Both `m = 1` (`r = 1/2`) and `m = 2` (`r = 1`) are lawful
> here. Nothing in the supplied model, the `C3` symmetry, the `K` conjugation,
> or the equal-per-mode normalization selects one over the other. `1/2 != 1`.

> **N2 (free-orbit non-triviality).** At `(alpha, beta, gamma) = (2, 1, 0)` the
> free orbit is genuinely complex: `im(lam1) != 0` and `lam1 != lam1*conj(lam1)`,
> so count-once and count-twice are actually distinct on this carrier and the
> reduction is not vacuous.

> **N3 (Hermitian realist-slip control).** The Hermitian carrier `M` has
> all-real spectrum and `det_C(M) = lamM0*lamM1*lamM2` with each `lamM_k` real.
> `M` is not `K`-real (`conj(M) != M` unless `b` is real), and its orbit values
> `lamM_1` and `lamM_2` are two independent reals with no conjugate pairing, so
> the count question posed on a conjugate pair does not arise on `M`. Reading
> `M` as if it were the registration would manufacture a spurious count, which
> the control forbids.

> **N4 (Born comparator).** The equipartition comparator `((2/3)/2)/(1/3) = 1`
> reproduces the `r = 1` slot reading arithmetic exactly and is disjoint from the
> `r = 1/2` component reading, confirming the two dictionary completions are the
> two distinct arithmetic outcomes and not a single disguised one.

## Bounded consequence

On the supplied `C3` model, the action reality class, the `K`/CPT
quotient-measure pushforward, and the record-formation locking dictionary are
three guises of one count binary `m` in `{1, 2}`, related by the exact
translations of T4, and the occupancy-grain obligation reduces to deciding `m`.

This is the firewall around the result. The dial settings `r = 0`, `r = 1/2`,
`r = 1` are registered as the lawful stable values, not forced; the quark and
neutrino sectors register other `r` values elsewhere, so `r = 1/2` is never
forced for the charged leptons here. The count binary `m` is named as the single
open input and is neither derived nor preferred. The `C3` symmetry, the `K`
conjugation, and the equal-per-mode normalization are supplied context and
carrier structure only, never selectors. The reduction concentrates the
obligation onto one input; it does not discharge it, does not close it, and adds
no premise, axiom, primitive, convention, or import.

## Honest auditor read / Boundary

What is proved: an exact structural equivalence among three candidate deciders
on a supplied finite `C3` model, plus the concentration corollary. Every
algebraic step of T1-T4 is computed by the runner in exact arithmetic; T5 is a
prose corollary of T4 and the quoted closure criterion. What is not proved:
which count
setting the physical charged-lepton matter action realizes. That is the open
input `m`, and it remains open. The reduction imports nothing beyond the cited
retained determinant-power identities (`3A` and the fermionic-realification
Pfaffian-power narrow theorem), the cited open obligation and
its two no-go route maps (`2A`, `2C`), and the framework axioms' readout and
qualification clauses. The supplied `C3` model is a minimal witness carrier, not
a claim about the physical matter action's form.

## Non-claims

This note derives no `r`, no `Q`, no mass, no mixing angle, no probability rule,
no species map, and no sector weight. It selects no horn of the occupancy-grain
obligation and changes no audit verdict. It does not register a primitive, adopt
a convention, or introduce any new coinage. It does not treat the Lattice,
Qubit, Admissibility, or Record axiom, or any approved primitive, as a source of
bounded status. The Hermitian carrier `M` is a control, not a physical registered
state. The reduction is conditional on the still-open count binary `m`.

## Load-bearing dependencies

Ledger grades below are recorded as of the writing date; grades are set by the
independent audit lane and can move. Verify the live ledger row before any
load-bearing use. The runner gates dependency filenames and verbatim quoted
content; it does not pin grades.

| Dependency | Ledger grade at writing (2026-07-16) | Consumed content |
|---|---|---|
| [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md) | `open_gate` (ledger row: `audited_renaming`) | the exact closure criterion and the pending-chain conditionality statement this note reduces |
| [`ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md`](ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md) | `retained` | realification-determinant modulus-square and holomorphic Berezin Gaussian `det_C`, the reality-class modulus powers `1` and `2` |
| [`ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md`](ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md) | `retained` | conjugate-sector direct-sum modulus square and single-sector Gaussian invariance backing the count-twice power `2` |
| [`ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md`](ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md) | `unaudited` | the axioms-plus-primitives non-selection theorem confirming neither horn is forced |
| [`ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`](ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md) | `unaudited` | the unsupplied outcome-to-component dictionary, the `x = 2r`/`x = r` readings, and the both-completions lawfulness statement |

## Runner verification map

| Block | Content | Result |
|---|---|---|
| SOURCE_GATES | verbatim quotes present in each source and in this note; dependency filenames cited and present | PASS |
| SPECTRAL (T1) | `C3` spectrum, `K` action, `A` eigenrelations, `im(lam1)` formula | PASS |
| DET_POWER (3A re-gate) | realification determinant equals `det_C` times its conjugate | PASS |
| REALITY_CLASS (T3a) | reality neutrality and modulus-power multiplicativity | PASS |
| GLOBAL_POWER (T2) | dial invariance under equal rescaling | PASS |
| QUOTIENT_MEASURE (T3b) | orbit partition, derived `K`-invariance forcing, pushforward versus restriction weights | PASS |
| DICTIONARY (T3c) | component/slot completions and the reduced dial map | PASS |
| FAITHFULNESS_CONTROLS (T1/N1-N4) | non-triviality, Hermitian control, Born comparator | PASS |
| TRANSLATION (T4) | the three guises produce one common count binary and dial pair | PASS |
| NOTE_HYGIENE | claim id, required sections, forbidden-pattern and decimal scans | PASS |

Run:

```bash
python3 scripts/acphilambda_grain_decider_reduction_2026_07_16.py
```

Cached run result:

```text
TOTAL: PASS=86 FAIL=0
```

## Relation to prior notes

This block-03 note is a sibling of the block-01 occupancy-grain menu-counting
correspondence note `ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md`;
that sibling is named for orientation only and is not a load-bearing dependency
of this note.

**No check passes by literal stipulation.**
