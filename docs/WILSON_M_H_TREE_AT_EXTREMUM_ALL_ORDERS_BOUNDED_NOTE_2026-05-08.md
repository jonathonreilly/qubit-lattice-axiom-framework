# Wilson-Corrected m_H_tree at Extremum, All Orders in r — Bounded Note

**Date:** 2026-05-08
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/frontier_wilson_m_h_tree_at_extremum_all_orders.py`](../scripts/frontier_wilson_m_h_tree_at_extremum_all_orders.py)

## Scope split (audit-named, 2026-06-20)

Per the independent audit of this row, the note's content is split into
two scopes, and the structure below reflects that split:

- **Part I — clean algebraic curvature-scale core (standalone derived
  content).** The finite-sum, all-orders-in-`r` curvature-scale formula
  (eq. (2) / (3)), its `r = 0` and small-`r` reductions, and the
  binomial-moment identities. This is exact finite-sum arithmetic over
  the cited curvature input; it is *not* a physical Higgs-pole mass.
- **Part II — physical / Higgs-matching readout (explicitly conditional;
  not supplied here).** The external-`m_H_PDG` matching equation, the
  bisection root `r_all_orders ≈ 0.26855`, and the leading-order shift
  comparisons. This readout is conditional on the unsupplied
  readout-identification, channel-selection (uniform-`N_taste = 16`),
  tree-level mean-field, nonzero-`r`, and parent-`u_0` normalization
  closures. The split does **not** supply those closures; it segregates
  the conditional readout from the derived core.

The audit-named alternative to supplying those closures is exactly this
split: Part I is the standalone derived scope; Part II is flagged
conditional. (A companion diagnostic-core artifact is recorded in
[`WILSON_M_H_TREE_AT_EXTREMUM_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md`](WILSON_M_H_TREE_AT_EXTREMUM_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md);
this note's own Part I/Part II structure is the within-note realization
of the same split.)

## Part I — Claim: clean algebraic curvature-scale core

Building on the exact-in-`r` curvature at the Wilson-shifted extremum
`m^* = -4 r` derived in
[`WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`](WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md)
(forward-reference; sister branch — note that the sister filename's
`LEADING_ORDER_IN_R` qualifier refers to that note's own leading-order
expansion of the curvature about `r = 0`; the sister note's eq. (1)
itself, which we cite below, is the *exact* curvature at `m^*`),

```text
d^2 V^W / dm^2  |_{m = m^*}
   =  ( 1 / 4 ) · Σ_{k=0}^{4}  binomial(4, k) ·
        ( ( k - 2 )^2 r^2  -  u_0^2 )  /  ( ( k - 2 )^2 r^2  +  u_0^2 )^2,         (1)
```

the sign-flipped per-channel curvature-scale-squared diagnostic
`Q_W(r, u_0)`, obtained by taking the curvature magnitude termwise and
dividing by the uniform diagnostic all-corners count `16` (the parent
Higgs note's
[`HIGGS_MASS_FROM_AXIOM_NOTE.md`](HIGGS_MASS_FROM_AXIOM_NOTE.md) eqs.
`[3]–[5]` per-channel identification under the uniform-`N_taste = 16`
admission — non-derived; bounded in
[`HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md`](HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md)
forward-reference), is the *all-orders-in-r* closed form

```text
Q_W(r, u_0)  ≡  ( m_H_tree^W / v )^2
   =  ( 1 / 64 ) · Σ_{k=0}^{4}  binomial(4, k) ·
        ( u_0^2  -  ( k - 2 )^2 r^2 )  /  ( ( k - 2 )^2 r^2  +  u_0^2 )^2.        (2)
```

The symbol `m_H_tree^W` is retained for continuity with the older
source surface; under the parent's current boundary it should be read
as a per-channel diagnostic curvature scale (`m_curv,W`), NOT a
physical Higgs-pole mass. Equivalently:

```text
m_H_tree^W
   =  ( v / 8 ) · sqrt( Σ_{k=0}^{4} binomial(4, k) ·
                          ( u_0^2 - ( k - 2 )^2 r^2 )
                        / ( ( k - 2 )^2 r^2 + u_0^2 )^2 ).                       (3)
```

Equation (2) is exact in `r` (and in `u_0`). It reduces to the
parent eq. `[5]` `(m_H_tree / v)^2 = 1 / (4 u_0^2)` at `r = 0` (each
summand is `1/u_0^2`, summing to `16/u_0^2`, dividing by `64` gives
`1/(4 u_0^2)`); and it reduces to PR-#761's leading-order form
`(1/(4u_0^2)) · (1 - 3 r^2 / u_0^2) + O(r^4)` at small `r`. Part I is
the standalone derived content: a finite-sum algebraic identity in the
symbolic inputs `r` and `u_0`. It carries no external mass comparison
and no readout identification.

## Part II — Physical / Higgs-matching readout (CONDITIONAL; not supplied here)

The remainder of this section records the physical Higgs-matching
readout. It is **explicitly conditional** on the unsupplied
readout-identification, channel-selection, tree-level mean-field,
nonzero-`r`, and parent-`u_0` normalization closures listed in the
Scope split and the Boundaries section; this note does **not** supply
those closures, so the matching value below is not a derivation of a
physical Higgs mass or of a canonical Wilson coefficient.

Setting (2) equal to `(m_H_PDG / v)^2` (with `m_H_PDG = 125.10 GeV`
used as comparison input only, not load-bearing for derivation) gives
an exact algebraic comparison equation in `r`. Bisecting in `Fraction`
arithmetic (canonical `u_0 = 0.8776`, `v = 246.22 GeV`) on the
bracket `[0.26, 0.28]` gives the all-orders matching value

```text
r_all_orders  ≈  0.26855   ± 10^{-5}                                              (4)
```

vs the leading-order matching value `r_leading ≈ 0.23572` from
[`WILSON_M_H_TREE_AT_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`](WILSON_M_H_TREE_AT_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md)
(forward-reference; sister branch). The sister note's `r_leading ≈
0.23572` is the *mass-level linear-Taylor* matching value, obtained by
truncating `sqrt(1 - 3 r^2/u_0^2)` linearly to give `m_H_W ≈ m_H_zero·(1
- (3/2) r^2/u_0^2)` and solving for `r`. The relative shift between
this leading-order value and all-orders is

```text
( r_all_orders  -  r_leading )  /  r_leading   ≈   13.9 %                        (5)
```

(mass-level linear-Taylor comparison). For an apples-to-apples
square-form comparison, the square-form leading-order matching equation
`(m_H_W/v)^2 = (1/(4u_0^2))·(1 - 3 r^2/u_0^2) = (m_H_PDG/v)^2` (no
sqrt-truncation) solves exactly to `r_LO_square ≈ 0.22925`, giving

```text
( r_all_orders  -  r_LO_square )  /  r_LO_square   ≈   17.1 %                    (5')
```

Both comparisons (5) and (5') describe the same all-orders shift; they
differ in *which* leading-order observable is being squared. Either
way the all-orders correction is non-trivial (`~14–17 %`) and is not
captured by the leading-order Taylor truncation.

The all-orders value sits within the perturbative-Taylor
radius-of-convergence boundary `r < u_0 / 2 ≈ 0.439` (set by the
dominant `k = 0, 4` summands, which control the ratio test). At
`r ≈ 0.269` the dimensionless expansion parameter is
`(2r/u_0)^2 ≈ 0.37`, so the perturbative Taylor expansion converges
but with non-negligible higher-order corrections — successive Taylor
contributions fall by a factor `~2-3` at `r ≈ 0.269` (asymptotic
ratio `~4` only at much smaller `r`). The all-orders closed form (2)
is the unique resummation that captures these corrections exactly.

Part I (the clean algebraic curvature-scale core, eqs. (2)–(3) with
their reductions) is the standalone derived content. Part II records the
all-orders matching value as an explicitly conditional readout: it does
**not** close the +12% Higgs gap chain, and the matching readout (4) is
conditional on:
1. the **readout identification** — a bridge from the diagnostic `Q_W`
   slot to a physical Higgs-pole observable slot, separate from the
   channel, correction-model, `r`-selection, and `u_0` normalization
   choices below (not supplied here);
2. the uniform-`N_taste = 16` channel selection (non-derived);
3. the tree-level mean-field formalism (no CW corrections, no RGE
   running);
4. a non-zero Wilson coefficient `r` (not part of the canonical pure-
   Kogut-Susskind staggered setup);
5. the parent-`u_0` normalization surface (the older rounded
   `u_0 = 0.8776` comparator used by the matching arithmetic below is
   not reconciled here with the current B1 plaquette surface
   `u_0 = <P>^(1/4) = 0.877681381...`).

Any of (1)–(5) failing voids the matching readout. None of (1)–(5) is
supplied by this note; the split narrows the derived scope to Part I and
flags Part II conditional rather than supplying these closures.

## Post-audit algebraic-core split (2026-06-18 companion; within-note split 2026-06-20)

The clean finite-sum curvature algebra in eq. (2) is also recorded as a
standalone companion artifact in
[`WILSON_M_H_TREE_AT_EXTREMUM_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md`](WILSON_M_H_TREE_AT_EXTREMUM_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md).
That note is the B1-synced diagnostic-core artifact: it keeps
`r` and `u_0` symbolic for the theorem, uses the current B1
`u_0 = <P>^(1/4) = 0.877681381...` only for numerical diagnostic
checks, and excludes the physical Higgs-pole readout, external
mass-comparison matching equation, uniform-channel physical selection,
and nonzero-`r` derivation from scope.

The 2026-06-20 audit-named within-note split (the Part I / Part II
structure above) is the realization of the same split inside this note:
Part I is the standalone derived curvature-scale core; Part II is the
explicitly conditional physical/Higgs-matching readout. The matching
content of this note remains conditional on the closures (1)–(5) listed
above.

## Proof-Walk

### Part I — clean algebraic curvature-scale core (derived)

| Step | Load-bearing input | Lattice-action input? |
|---|---|---|
| Exact curvature at `m^* = -4r` from sister extremum note: `(1/4) Σ_k binomial(4,k)·((k-2)^2 r^2 - u_0^2)/((k-2)^2 r^2 + u_0^2)^2` | sister forward-reference [`WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`](WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md) | no |
| Per-channel diagnostic count division by uniform-`N_taste = 16` (parent eqs. `[4]–[5]`): `\|d^2V/dm^2\|_per-channel = \|total\|/16` (admitted diagnostic denominator, not a physical channel-selection derivation — see Part II conditional closure (2)) | parent Higgs note + admitted convention | no |
| Sign flip: total curvature is negative (tachyonic), so `\|d^2V/dm^2\| = u_0^2 - (k-2)^2 r^2` per term, etc. | algebraic sign | no |
| Resulting diagnostic `Q_W(r,u_0) = \|per-channel\| = (1/64) · Σ_k binomial(4,k) · (u_0^2 - (k-2)^2 r^2) / ((k-2)^2 r^2 + u_0^2)^2` (eq. (2)) | direct substitution | no |
| Reduction at `r = 0`: each summand `→ 1/u_0^2`; sum `→ 16/u_0^2`; divide by 64 `→ 1/(4 u_0^2)`; matches parent eq. `[5]` | binomial-state-count `Σ binom = 16` | no |
| Reduction at leading order in `r^2` via Taylor `(u_0^2 - x) / (u_0^2 + x)^2 = 1/u_0^2 - 3 x / u_0^4 + O(x^2)` with `x = (k-2)^2 r^2`: leading term gives `1/(4 u_0^2)`, second term gives `-(3/64) · Σ binom·(k-2)^2 r^2 / u_0^4 = -(3·16)/(64·u_0^4) r^2 = -3 r^2 / (4 u_0^4)`. Combining: `(1/(4u_0^2))·(1 - 3 r^2 / u_0^2) + O(r^4)`, matching PR #761 | scalar Taylor + binomial-moment `Σ binom·(k-2)^2 = 16` | no |

Every Part I step is exact-rational arithmetic or scalar calculus on a
known closed form. The Wilson plaquette form, staggered phases, link
unitaries, and lattice scale `a` do not appear as load-bearing inputs to
(2)–(3). Part I is the standalone derived scope of this note.

### Part II — physical / Higgs-matching readout (CONDITIONAL; not supplied here)

The steps below are recorded as a conditional matching computation. They
are exact-rational arithmetic, but they are **not** a derivation of a
physical Higgs mass or of a canonical Wilson coefficient: they are
conditional on the closures (1)–(5) of Part II (readout identification,
channel selection, tree-level mean-field, nonzero `r`, and parent-`u_0`
normalization), none of which is supplied here.

| Step | Load-bearing input | Conditional on |
|---|---|---|
| All-orders matching equation: `Q_W = (m_H_PDG / v)^2` with `m_H_PDG = 125.10` (comparison input only), giving `(2)` evaluated at unknown `r` equal to a known rational target | algebraic equation in one variable `r` | readout identification + external mass comparison |
| Bisection in `Fraction`: bracket `r ∈ [0.26, 0.28]` (chosen so that the bracket endpoints have opposite-sign `Q_W - (m_H_PDG/v)^2` — verified directly: `f(0.26) > 0`, `f(0.28) < 0`); evaluate at midpoint and halve bracket until width `≤ 10^{-5}` | exact-rational bisection | nonzero `r` + channel selection |
| Result: `r_all_orders ≈ 0.26855` after N bisection steps | bisection convergence | nonzero `r` (matching value, NOT an `r` derivation) |
| Comparison to leading-order linear-form (PR #761): `r_leading ≈ 0.23572`; relative shift `(r_all_orders - r_leading)/r_leading ≈ 0.139` (≈ 13.9 %) | scalar arithmetic | same conditional readout |
| Validity check: `r_all_orders ≈ 0.269 < u_0 / 2 ≈ 0.439`, well within the radius of convergence of the perturbative Taylor expansion (set by the dominant `k = 0, 4` summands, where the relevant ratio is `(2r/u_0)^2 ≈ 0.37 < 1`) | scalar comparison | parent-`u_0` normalization surface |

Every Part II step is exact-rational arithmetic or `Fraction` bisection,
but the resulting matching value is conditional, not a derived physical
readout. The Wilson plaquette form, staggered phases, link unitaries,
and lattice scale `a` do not appear as load-bearing inputs to (4)–(5).

## Exact Arithmetic Check

The runner verifies, at exact rational precision via
`fractions.Fraction`:

(A) **Exact closed form.** Direct evaluation of (2) at several
`(r, u_0)` pairs, including `r = 0` (which gives `1/(4 u_0^2)`
exactly, matching parent eq. `[5]`).

(B) **Reduction to PR-#761 leading order.** Taylor-expand (2) in `r^2`
at `r = 0`. The leading term is `1/(4 u_0^2)`, the next term is
`-3 r^2 / (4 u_0^4)`, summing to `(1/(4u_0^2))·(1 - 3 r^2 / u_0^2) +
O(r^4)`. Verified by extracting the coefficient of `r^2 / u_0^4` in
the Taylor expansion at small `r`; it equals `-3/4` exactly (the
runner extracts this directly).

(C) **Bisection for `r_all_orders`.** Solve `(m_H_W / v)^2 = (m_H_PDG /
v)^2` by bisection in `Fraction` arithmetic on the bracket `[0.26,
0.28]`. The `m_H_PDG = 125.10 GeV` is used as comparison input only
(NOT load-bearing for derivation; runner labels this explicitly).
Bracket endpoints verified opposite-sign: `f(0.26) > 0`, `f(0.28) < 0`.
Bisect until the bracket width is `≤ 10^{-5}`. Result: `r_all_orders
∈ [0.26854, 0.26856]`, i.e. `0.26855 ± 10^{-5}`.

(D) **Comparison to leading-order.** `r_leading = 0.23572` (from PR
#761, which solves the linear-Taylor matching equation). Relative
shift `(r_all_orders - r_leading) / r_leading ≈ 0.139 = 13.9 %`. The
leading-order linear-Taylor approximation under-estimates `r` by
about `14 %`.

(E) **Perturbative-validity confirmation.** `r_all_orders ≈ 0.269 <
u_0 / 2 ≈ 0.439`, well within the radius of convergence of the
perturbative Taylor expansion of the all-orders form. The dominant
expansion parameter is `(2r / u_0)^2 ≈ 0.37` (set by the `k = 0, 4`
summands, where `(k - 2)^2 = 4`), so successive Taylor coefficients
fall by a factor `~3-5` per order — convergent but slow, which is
why leading-order is `~14 %` off.

## Dependencies

- [`WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`](WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md)
  for the exact curvature at `m^* = -4r`. **Forward-reference;** on a
  sister branch.
- [`WILSON_M_H_TREE_AT_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`](WILSON_M_H_TREE_AT_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md)
  for the leading-order matching value `r ≈ 0.235`. **Forward-reference;**
  on a sister branch.
- [`WILSON_CORRECTED_V_TASTE_TREE_LEVEL_BOUNDED_NOTE_2026-05-08.md`](WILSON_CORRECTED_V_TASTE_TREE_LEVEL_BOUNDED_NOTE_2026-05-08.md)
  for the `V_taste^W` formula. **Forward-reference;** on a sister
  branch.
- [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md)
  for the staircase multiplicities `binomial(4, k)`.
- [`HIGGS_MASS_FROM_AXIOM_NOTE.md`](HIGGS_MASS_FROM_AXIOM_NOTE.md)
  for the parent tree-level setup, eqs. `[3]–[6]`, and the uniform-
  `N_taste = 16` channel admission. (Per Gap #3 lite 2026-05-10 the
  parent note's headline quantity is now labeled `m_curv_tree` — a
  per-channel symmetric-point curvature scale of V_taste, NOT a
  Higgs-mass pole; this all-orders Wilson-correction note continues to
  use the older `m_H_tree` symbol internally for its bounded
  source-surface calculation, but the imported quantity should be read
  as `m_curv_tree` for first-principles-honest scope.)
- [`HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md`](HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md)
  for the boundary statement that the uniform-`N_taste = 16` choice is
  itself a non-derived admission. **Forward-reference;** on a sister
  branch.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
  for non-load-bearing staggered-Dirac realization gate context.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  for the current Lattice, Quantum, Record framework baseline.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner. The runner handles the forward-references
gracefully (per the established pattern: `[INFO]` rather than `[FAIL]`
when a sister-branch note is not yet on `origin/main`).

## Boundaries

**Derived scope (Part I).** Only the clean algebraic curvature-scale
core — eq. (2)/(3), its `r = 0` reduction to `1/(4 u_0^2)`, and its
small-`r` reduction to PR-#761's leading order — is the standalone
derived content of this note. It is a finite-sum identity in symbolic
`r` and `u_0`.

**Conditional scope (Part II) — this note does not close:**

- the +12% Higgs gap chain in [`HIGGS_MASS_FROM_AXIOM_NOTE.md`](HIGGS_MASS_FROM_AXIOM_NOTE.md). The all-orders matching value `r ≈ 0.269` is **conditional** on the following unsupplied closures:
  1. the **readout identification** — a bridge from the diagnostic `Q_W`
     slot to a physical Higgs-pole observable slot, separate from the
     channel, correction-model, `r`-selection, and `u_0` normalization
     choices below (not supplied here);
  2. the uniform-`N_taste = 16` channel selection (non-derived);
  3. the tree-level mean-field formalism (no CW corrections, no RGE
     running);
  4. a non-zero Wilson coefficient `r`, **not** part of the canonical
     pure-Kogut-Susskind staggered setup;
  5. the parent-`u_0` normalization surface — the matching arithmetic
     uses the older rounded `u_0 = 0.8776` comparator, not reconciled
     here with the current B1 plaquette surface
     `u_0 = <P>^(1/4) = 0.877681381...`.
  Any of (1)–(5) failing voids the matching readout;
- the physical Higgs mass `m_H` numerical value (`m_H_PDG = 125.10` is
  treated as a comparison input only, not a derivation input);
- the value of the Wilson coefficient `r` itself (the `r ≈ 0.269`
  value is the *all-orders matching value under the admissions*, not a
  derivation of `r`);
- the plaquette mean-field link `u_0` numerical value;
- the staggered-Dirac realization gate;
- the `g_bare = 1` derivation;
- any parent theorem/status promotion;
- the exact algebraic matching root for `r`. The bisection result
  `r ≈ 0.26855 ± 10^{-5}` is approximate; it is not a derivation of
  a canonical Wilson coefficient.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_wilson_m_h_tree_at_extremum_all_orders.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: split into Part I [CORE] (derived) and Part II [CONDITIONAL
READOUT]. Part I: the all-orders curvature-scale core Q_W = (1/64) Σ_k
binomial(4,k) · (u_0^2 - (k-2)^2 r^2) / ((k-2)^2 r^2 + u_0^2)^2 verified
at exact rational precision; reduces to 1/(4u_0^2) at r=0 (matches parent
eq. [5]) and to PR-#761's leading order at small r. Part II
(CONDITIONAL): bisection gives the matching value r_all_orders ≈ 0.26855
± 10^{-5}, a ~14% shift from the leading-order matching value 0.23572 —
exact-rational arithmetic, but CONDITIONAL on the unsupplied
readout-identification, uniform-N_taste=16 channel-selection, tree-level
mean-field, nonzero-r, and parent-u_0 normalization closures; NOT a
derived physical Higgs mass or a derivation of a canonical Wilson
coefficient.
```

## Repair section (2026-06-20): source-side scope split

The independent audit returned this row `audited_conditional` with the
re-audit handle: *"missing_bridge_theorem: split the clean algebraic
curvature-scale core from the physical/Higgs matching readout, OR add
retained readout, channel-selection, tree-level mean-field, nonzero-r,
and parent-u_0 normalization closure before re-audit."*

This repair takes the **source-side split alternative** (it does *not*
attempt the retained-closure derivations). The split:

- introduces an audit-named **Scope split** section and restructures the
  note into **Part I — clean algebraic curvature-scale core** (the
  standalone derived content: eq. (2)/(3), the `r = 0` reduction to
  `1/(4 u_0^2)`, and the small-`r` reduction to PR-#761's leading order)
  and **Part II — physical / Higgs-matching readout (CONDITIONAL; not
  supplied here)** (the external-`m_H_PDG` matching equation, the
  bisection root `r_all_orders ≈ 0.26855`, and the leading-order shift
  comparisons);
- segregates the Proof-Walk into a Part I core block and a Part II
  conditional-readout block;
- enumerates, in the Boundaries section, the five unsupplied closures the
  Part II readout is conditional on: (1) readout identification,
  (2) uniform-`N_taste = 16` channel selection, (3) tree-level mean-field,
  (4) nonzero Wilson coefficient `r`, and (5) parent-`u_0` normalization
  surface (the older rounded `u_0 = 0.8776` comparator vs the current B1
  `u_0 = <P>^(1/4) = 0.877681381...`);
- segregates the runner checks: the algebraic-core checks (Parts 4–5) are
  labeled `[CORE]`; the physical-matching checks (Parts 6–8) are labeled
  `[CONDITIONAL READOUT]`; a new Part 11 `[SPLIT]` check verifies the
  Part I / Part II structure and the five enumerated closures.

No derived value is changed by this repair. The split narrows the derived
scope to the Part I algebraic core; the Part II matching readout is now
explicitly conditional on the named (unsupplied) closures, rather than
presented alongside the core as one undifferentiated headline.

This source note does not set, predict, or alter any audit verdict or
effective status; later status is generated by the audit pipeline after
independent review.
