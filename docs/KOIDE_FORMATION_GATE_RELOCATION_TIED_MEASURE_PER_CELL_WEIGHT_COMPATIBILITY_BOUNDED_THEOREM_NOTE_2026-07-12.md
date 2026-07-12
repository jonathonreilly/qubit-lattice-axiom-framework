# Formation-Gate Relocation — a Tied Two-Slice Measure Coexists with an Independent Per-Cell Formation Weight on the Registrable Quotient (Bounded Theorem, rhalf block 13)

**Date:** 2026-07-12
**Claim type:** bounded_theorem (exact compatibility, relocation, and residual
compression; no value of the formation weight is derived or preferred).
**Primary runner:**
[`scripts/frontier_formation_gate_relocation_2026_07_12.py`](../scripts/frontier_formation_gate_relocation_2026_07_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_formation_gate_relocation_2026_07_12.txt`](../logs/runner-cache/frontier_formation_gate_relocation_2026_07_12.txt)

> **CLAIMED (bounded):** the records-only, time-homogeneous, two-slice
> `C_3` corner construction may satisfy block 10 on the K-tied measure while
> an independent formation rule supplies any normalized weight `(w, 1-w)` on
> the two-element registrable menu `{singlet cell, doublet cell}`. Every landed
> block 9/10 check is unchanged because it is a statement about the measure,
> reflection, kernel, or registrable algebra and factors through projection
> away from the formation state. The exact energy matching is
> `r = (1-w)/(2w)` for `0 < w < 1`; `w = 1/2` is counting on the quotient and
> gives `r = 1/2`, while `w = 1/3` is restriction of normalized carrier trace
> and gives `r = 1`. The lane's residue is therefore one named formation-gate
> object, `w`.
>
> **NOT CLAIMED:** a derivation, selection, or preference of `w`, `r = 1/2`,
> or `r = 1`; an identification of measure granularity with formation
> weighting; a new formation dynamics; a result from either companion block
> listed as in preparation; or an enlargement of any block 9/10 theorem.

## Claim scope

This note is confined to the `C_3` singlet/doublet carrier and the
time-homogeneous two-slice records-only OS construction of block 10. It adds a
formation state only on block 10's P-even registrable quotient. The OS
reflection, two-slice crossing, `C_3[111]` probe coupling, and P-even orbit
clause are supplied at block 10's declared grade. The three-distinct-value
non-degeneracy element used there is a labeled comparator, never thresholded;
it is not used to set a formation weight here.

## Why this block is needed

Block 9 attached count-once/count-twice to the analytic section of the
Berezin weight. Block 10 then required weight-stage K-reality for the stated
records-only OS reconstruction and, under its named non-degeneracy element,
left the K-tied branch. The apparent further implication

```text
K-tied measure  =>  per-real-mode formation law  =>  r = 1
```

contains an extra arrow. A tied measure fixes the analytic type and the
OS/Hermitian reconstruction surface. A formation law fixes how the total
formation weight or energy is distributed over registrable alternatives.
Blocks 9 and 10 explicitly do not identify those two levels. This note makes
their coexistence and the missing arrow exact.

## T1 — exact compatibility and independence

### T1.1 The tied measure underneath

Let `C` be the three-cycle and

```text
W(a,b,c) = a I + b C + c C^2,
K(W) = [[-W, -I/2], [I/2, -W]].
```

On the K-tied slice, `a` is real and `c = conj(b)`, hence `W^dag = W`.
The runner dynamically reuses block 10's exact Gaussian-rational
Grassmann/Berezin engine and re-verifies the exact point

```text
a = 4/5,    b = 3/10 + i/5,    c = 3/10 - i/5.
```

At this point the two-slice partition function is exactly
`Z = 146081/250000 > 0`; the normalized records-only Gram on block 10's
registrable spanning set
`{1, N, TCsym, e2, e3}` is Hermitian, and all five leading principal minors
are exact positive rationals. Thus the underlying component is an explicit
Hermitian positive-definite records-only reconstruction on the tied measure,
not a hypothetical compatibility claim.

### T1.2 The formation state on top

Let `P_s` and `P_d` be the singlet and doublet cell projections. Block 10's
P-evenness/orbit ruling makes the two doublet members indistinguishable to
registrable readouts, so the doublet is **one registrable cell**. The menu is

```text
X_reg = {s, d},
A_reg = Fun(X_reg) = C P_s + C P_d ~= C + C.
```

For `0 <= w <= 1`, define the positive normalized formation state

```text
phi_w(x_s P_s + x_d P_d) = w x_s + (1-w) x_d.
```

Here `w` is the singlet-cell formation weight and `1-w` the doublet-cell
formation weight. The two-level model is the ordered pair

```text
M_w = (M_tied, phi_w),
```

where `M_tied` contains the tied two-slice Berezin measure, `theta`, the
crossing, and its records-only Gram. No change to `M_tied` is made when `w`
changes.

### T1.3 Independence theorem

Let `pi(M_tied, phi_w) = M_tied`. Every block 9/10 check has the form
`B_j(M_tied)`: determinant power and holomorphy/Wirtinger degree; the
K-tie/weight-reality fixed set; P-evenness of registrable readouts; the exact
two-slice partition function; Hermiticity and positivity of the records-only
Gram; and the branch/degeneracy statements. Therefore its extension to the
two-level model is exactly `B_j o pi`, and for every `w,w' in [0,1]`,

```text
(B_j o pi)(M_w) = B_j(M_tied) = (B_j o pi)(M_w').
```

This is an exact product-extension theorem: the entire state simplex of
`A_reg` lies over the same tied-measure point. It is stronger than a claim that
the two levels are merely plausible together; an explicit model exists and
all base certificates are invariant under its formation coordinate.

The scope boundary is also explicit in the landed sources. Block 9 says,
verbatim:

> no occupancy, weighting, or reading-section rule is adopted or derived.
> Both cells are lawful.

Block 10 likewise says that no occupancy, weighting, or reading-section rule
is adopted or derived and names the per-cell equipartition/dial-point law as a
surviving residual. Thus its count-twice statement fixes the **measure's
section grain**; promoting it to `phi_w = phi_{1/3}` would add the very formation
rule those statements disclaim.

## T2 — exact relocation of the fork arithmetic

Put the formation weights, rather than the measure's analytic degree, into the
channel energies:

```text
E_s = w E_tot,             E_d = (1-w) E_tot,
E_s = 3 a^2,               E_d = 6 |b|^2,
r = |b|^2/a^2.
```

For `0 < w < 1`, solving the two energy equations and taking their ratio gives

```text
a^2 = w E_tot/3,
|b|^2 = (1-w) E_tot/6,
r = |b|^2/a^2 = (1-w)/(2w),
w = 1/(1+2r).
```

No endpoint value is placed on the derivation path: the runner asks SymPy to
solve the energy equations first, forms `|b|^2/a^2` from that solution, and
only then compares the result with the displayed formula. Normalization leaves
one real coordinate on the two-element menu, so the former continuous dial is
exactly the one number `w` (with the energy ratio finite for `0 < w < 1`).

The named laws are exact specializations:

| formation law | solved cell weights `(w,1-w)` | solved `r` |
|---|---:|---:|
| per-outcome-cell: `E_s = E_d` | `(1/2, 1/2)` | `1/2` |
| per-real-mode: `E_d = 2 E_s` | `(1/3, 2/3)` | `1` |

Thus

```text
w = 1/2  <=>  uniform over the two registrable outcome cells
           <=>  per-outcome-cell law  <=>  r = 1/2,

w = 1/3  <=>  weights proportional to carrier dimensions (1,2)
           <=>  per-real-mode law     <=>  r = 1.
```

The repaired locked-record-outcomes note is cited only at its retained claim
scope: `origin/repair/koide-locked-record-outcomes-rho-map-20260711:docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md`,
Repair (2026-07-11) and Result T2. It supplies (i) the collision exhibit that a
Re/Im split assigns two statistical slots to one locked complex outcome under
the explicitly supplied one-record-one-slot reading, and (ii) the two exact
equipartition-granularity solves above. This note does **not** consume its
withdrawn `rho`-map and does **not** use `Z_sector/Z_orbit` to set `r`; the
repair expressly decouples that normalization fact from the `r` attribution.

## T3 — operator-algebra formalization

In the character basis of the supplied three-dimensional carrier `H = C^3`,
write

```text
P_s = diag(1,0,0),       rank(P_s) = 1,
P_d = diag(0,1,1),       rank(P_d) = 2,
P_s + P_d = I.
```

The P-even registrability ruling swaps the two doublet members and permits only
readouts constant on that pair. Hence the registrable readout algebra on this
spectrum is exactly

```text
A_reg = {x_s P_s + x_d P_d : x_s,x_d in C}
      ~= C + C.
```

Its two minimal central projections are `P_s` and `P_d`. There are two
different canonical state constructions, because they count different grains.

### T3.1 Restriction of the carrier trace

The normalized trace on the supplied carrier is

```text
tau_3(X) = Tr_H(X)/3.
```

Its restriction to `A_reg` is

```text
tau_3(x_s P_s + x_d P_d) = (1/3)x_s + (2/3)x_d,
```

so it is `phi_{1/3}`. It counts carrier dimension: one singlet direction and
two doublet directions. Equivalently its carrier density is `rho = I/3`.

At the graded-constraint note's own conditional declared grade, this is the
landed full-automorphism zero-information point:
`origin/claude/science/rhalf-graded-constraint-boundary-20260711:docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md`,
Theorem B. Under that note's proposed-core hypotheses plus its explicitly named
full-symmetry premise, it computes

```text
rho = I/3  ->  (w_s,w_d) = (1/3,2/3)  ->  r = 1.
```

The conditional grade matters: this citation identifies the canonical state
and its `r` image; it does not turn full symmetry into axiom content or a
formation rule here.

### T3.2 Counting on the registrable quotient

The counting state on the **minimal central projections of the quotient** is

```text
tau_cell(x_s P_s + x_d P_d) = (x_s+x_d)/2.
```

Thus it is `phi_{1/2}`, assigning one half to each registrable cell irrespective
of its carrier rank. In the carrier representation the density

```text
rho_cell = diag(1/2,1/4,1/4)
```

restricts to exactly this quotient state: its two doublet entries add to one
half. The same graded-constraint note, in “The `r = 1/2` point,” computes

```text
rho_cell  ->  (w_s,w_d) = (1/2,1/2)  ->  r = 1/2.
```

Therefore the exact distinction is

```text
restriction of carrier trace     versus     counting on the quotient,
dimension grain                              registrable-cell grain.
```

Both constructions are canonical relative to the object on which one counts.
The grain question is **which canonical construction the formation gate uses**.
Neither construction is selected or derived here, and canonicality alone does
not order or prefer them.

## T4 — the residue, renamed honestly

After T1-T3, the lane no longer needs separate objects called “tie selector,”
“occupancy grain,” and “dial point” on this surface. Block 10 supplies the tied
measure at the stated grade; P-even registrability supplies the two-cell
quotient; normalization makes its state simplex one-dimensional; and the
energy dictionary maps that one coordinate bijectively to `r` for positive
weights. The remaining object is

```text
formation weight w = phi_w(P_s) on X_reg = {s,d}.
```

It is an instance of exactly the open gate named by the minimal axioms. The
axioms' open-gates list says, verbatim:

> context selection, measurement basis selection, Born weights, probability rules, update laws, decoherence mechanisms, and formation rules (which admissible possibility a new record locks, at which site, with what weight, or at what rate);

The available ways to pay this residue, each kept at its stated grade, are:

| possible payer | declared grade here | disposition |
|---|---|---|
| formation dynamics | downstream formation-rule derivation/bridge | open gate; no supplier in this block |
| classification of law-expressible weights | prospective bounded companion, **in preparation** | no result consumed; could pay `w` only if it proves uniqueness on this menu |
| registration-compatibility asymmetry of the fork endpoints | prospective bounded companion, **in preparation** | no result consumed; could pay `w` only if one endpoint is excluded at its own grade |
| owner admission | explicit admission, not a derivation | named fallback; **not recommended** |

### What would kill the relocation

A landed binding theorem of the form

```text
formation state phi_w = F(the Berezin measure's section)
```

would collapse the product fiber in T1. In particular, a theorem forcing the
K-tied section to use carrier-dimension weighting would impose `w = 1/3`, and
T1's “all `w`” compatibility statement would fail.

The witnessed search surface was precisely where such a binding could have
been stated: block 9's “What this note does NOT claim,” block 10's claim box,
T3, Residual Atom 1, and reprove-and-cite ledger, and the minimal axioms'
“Open Gates And Admissions Outside The Axioms.” Block 9 instead contains the
verbatim no-weighting sentence quoted in T1; block 10 explicitly leaves the
per-cell dial residual; and the axioms put “with what weight” outside axiom
content. No theorem binding formation weights to the measure section was found
on that witnessed surface. This is a bounded source-scope statement, not a
claim about uninspected literature or future work.

## Residual Atoms

1. **The formation weight `w` on the registrable menu.** Domain:
   `X_reg = {singlet cell, doublet cell}` with the doublet one cell by the
   supplied P-even orbit clause. State: `phi_w = (w,1-w)`, `0 <= w <= 1`.
   Energy image for positive weights: `r = (1-w)/(2w)`. Special points:
   quotient counting gives `w = 1/2`; carrier-trace restriction gives
   `w = 1/3`. Status in this note: **not derived, selected, or preferred**;
   payable only by one of T4's explicitly named supplier routes.

2. **The energy dictionary.** The identification that a formation state
   distributes the total channel energy as shares —
   `E_s = w E_tot`, `E_d = (1-w) E_tot`, against block 9's landed channel
   decomposition `E_s = 3a^2`, `E_d = 6|b|^2` — is **this note's own declared
   modeling element** (the energy-to-formation-state bridge). It is what makes
   the relocation's `r`-image exact rather than merely analogical. It is not
   supplied by the Record axiom, by blocks 9/10, or by the R-D surface; an
   auditor who rejects it keeps T1 (compatibility) and T3 (the two canonical
   states) but loses the bijection `r = (1-w)/(2w)` of T2.

The tied measure, two-cell quotient, and endpoint arithmetic are inputs or
exact constructions already accounted for at their stated grades; none
supplies the value of Atom 1.

## What This Note Does Not Claim

- **Not** a derivation or preference of `w = 1/2`, `w = 1/3`, `r = 1/2`, or
  `r = 1`. Both named endpoint constructions remain lawful at this theorem's
  scope.
- **Not** a contradiction of blocks 9 or 10. The relocation occupies exactly
  their disclaimed occupancy/weighting/dial space while preserving block 10's
  tied, Hermitian-PD measure.
- **Not** an inference that the tied measure's count-twice analytic grain is
  itself the formation law. That inference is the missing binding theorem
  isolated in T4.
- **Not** an unconditional “zero-information” premise. `rho = I/3` is cited as
  the graded-constraint note's full-symmetry point at that note's explicitly
  conditional grade.
- **Not** use of the withdrawn locked-outcomes `rho`-map or an inference from
  the normalization ratio `Z_sector/Z_orbit` to `r`. Only the repaired
  collision exhibit and equipartition solves are cited.
- **Not** a result from either companion named “in preparation,” and not a
  formation dynamics.
- **Not** a thresholded comparator or empirical fit. The block 10
  three-distinct-value element is labeled, never thresholded, and is not used
  to choose `w`.
- **Not** a claim beyond the time-homogeneous, bilinear, two-slice `C_3` corner
  measure and its P-even registrable quotient.

## Reprove-and-cite ledger

### Reproven here by the runner

- Dynamic reuse of block 10's exact Gaussian-rational Berezin/OS engine, with
  no floating scan invoked; `W^dag = W`,
  `Z = det(W^2 + I/4) > 0`, exact Gram Hermiticity, and five exact positive
  Sylvester minors at `(a,b,c) = (4/5, 3/10+i/5, 3/10-i/5)`.
- The projector algebra `P_s P_d = 0`, `P_s + P_d = I`, ranks `(1,2)`,
  P-swap invariance, and `A_reg ~= C+C` with readouts constant on the doublet.
- The complete normalized positive state family `phi_w = (w,1-w)` and exact
  factorization of every reused measure certificate away from `w`.
- The symbolic energy solve `r = (1-w)/(2w)`, its inverse
  `w = 1/(1+2r)`, and the two endpoint solves from their laws rather than from
  hard-coded values.
- The normalized-carrier-trace restriction `(1/3,2/3)` and quotient-counting
  restriction `(1/2,1/2)`, including their exact carrier density matrices and
  `r` images.
- Verbatim source guards for block 9's disclaimer, block 10's surviving dial,
  and the axioms' formation-rule open gate.

### Cited at declared grade

- [Block 9](KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md):
  first-order section/measure localization and the verbatim disclaimer that no
  occupancy, weighting, or reading-section rule is adopted or derived.
- [Block 10](RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md):
  the time-homogeneous two-slice tied-measure reconstruction, exact engine,
  P-even orbit ruling, and explicit survival of the per-cell dial residual.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Record content,
  Qualification, and the verbatim formation-rule open-gate sentence.
- Repaired locked-record-outcomes note at
  `origin/repair/koide-locked-record-outcomes-rho-map-20260711`: only the
  retained collision exhibit and repaired equipartition solves; no withdrawn
  `rho`-map content.
- Graded-constraint boundary note at
  `origin/claude/science/rhalf-graded-constraint-boundary-20260711`: the
  conditional full-symmetry `rho = I/3 -> r = 1` identification and the
  `rho = diag(1/2,1/4,1/4) -> r = 1/2` designated two-cell identification,
  each at that note's own declared claim scope.

## Verification

Run:

```bash
python3 scripts/frontier_formation_gate_relocation_2026_07_12.py
```

Expected: sixteen numbered `[PASS]` lines, then
`TOTAL: PASS=16 FAIL=0`, followed by the short verdict-first T1-T4/source-scope
summary. Exit code 0 iff `FAIL=0`.

The derivation paths use only exact `Fraction`/Gaussian-rational and SymPy
`Rational` arithmetic. The block 10 engine is reused dynamically up to its
report marker; none of its floating-point scan helpers is invoked.
